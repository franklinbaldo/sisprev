"""Extract every sheet of the frozen ``Regras Sisprev.xlsx`` to text CSVs.

The workbook (``data/raw/regras-sisprev.xlsx``) carries, besides the flat
112-rule table that already froze into ``data/raw/regras-sisprev.csv`` (the
rules currently *in* the Sisprev system, the as-is baseline), several
analytical sheets: the PGE-RO legal team's proposed replacement rules
(to-be), broken out by benefit modality, each with its own
``Validação PGE``/``Validação Presidência`` status. Those sheets are the
source for the ``okf/regras-propostas`` bundle.

This is a ONE-TIME BOOTSTRAP, the xlsx analogue of ``csv_to_okf.py``: it
reads the frozen workbook and writes a faithful, diffable text mirror of
each sheet under ``data/raw/xlsx/``. The mirror is frozen raw too — extracted
once, never regenerated on every build. Re-running refuses to overwrite an
existing extraction unless ``--force`` is passed.

Run with the bootstrap-only openpyxl engine (a dev dependency, not a
runtime one — the bundle reads markdown, never the xlsx)::

    uv run python scripts/xlsx_to_csv.py
"""

from __future__ import annotations

import argparse
import csv
import logging
import re
import unicodedata
from pathlib import Path
from typing import TYPE_CHECKING

import openpyxl

if TYPE_CHECKING:
    from openpyxl.worksheet.worksheet import Worksheet

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_XLSX = REPO_ROOT / "data" / "raw" / "regras-sisprev.xlsx"
DEFAULT_OUT = REPO_ROOT / "data" / "raw" / "xlsx"


class ExtractionAlreadyExistsError(Exception):
    """Raised when the target dir already holds an extraction and --force is absent.

    The text mirror is frozen raw: extracted once from the frozen workbook,
    never silently overwritten. Pass --force only to deliberately rebuild it.
    """


class SlugCollisionError(Exception):
    """Raised when two sheet titles slugify to the same (or an empty) filename.

    Without this, the second sheet would silently overwrite the first, so a
    whole sheet would vanish from the supposedly faithful frozen mirror.
    """


def slugify(name: str) -> str:
    """Turn a sheet title into an ascii kebab-case filename stem.

    ``'Especial de professor' -> 'especial-de-professor'``. Strips accents so
    the frozen filenames stay portable across filesystems.
    """
    normalized = unicodedata.normalize("NFKD", name)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    kebab = re.sub(r"[^a-z0-9]+", "-", ascii_only.strip().lower())
    return kebab.strip("-")


def sheet_rows(worksheet: Worksheet) -> list[list[str]]:
    """Return the sheet's rows as strings, dropping wholly empty leading/trailing lines.

    Every cell is emitted verbatim (``None`` becomes ``""``) — no header
    inference, no type coercion: this is a faithful mirror of the frozen
    workbook, kept honest for diffing and grepping, not a cleaned dataset.
    """
    rows = [
        ["" if cell is None else str(cell) for cell in row] for row in worksheet.iter_rows(values_only=True)
    ]
    non_empty = [i for i, row in enumerate(rows) if any(cell.strip() for cell in row)]
    if not non_empty:
        return []
    first, last = non_empty[0], non_empty[-1]
    width = max(len(row) for row in rows[first : last + 1])
    return [row + [""] * (width - len(row)) for row in rows[first : last + 1]]


def extract(source: Path, out_dir: Path, *, force: bool) -> list[Path]:
    """Write one CSV per non-empty sheet of ``source`` into ``out_dir``.

    Returns the paths written. Refuses (``ExtractionAlreadyExistsError``) to
    touch an ``out_dir`` that already holds ``*.csv`` unless ``force`` is set.
    """
    existing = sorted(out_dir.glob("*.csv")) if out_dir.exists() else []
    if existing and not force:
        msg = (
            f"{out_dir} already holds {len(existing)} extracted CSV(s). "
            "The text mirror is frozen raw; pass --force to rebuild it deliberately."
        )
        raise ExtractionAlreadyExistsError(msg)

    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    slugs: dict[str, str] = {}
    for worksheet in workbook.worksheets:
        rows = sheet_rows(worksheet)
        if not rows:
            logger.info("skipping empty sheet %r", worksheet.title)
            continue
        slug = slugify(worksheet.title)
        if not slug:
            msg = f"sheet {worksheet.title!r} slugifies to an empty filename"
            raise SlugCollisionError(msg)
        if slug in slugs:
            msg = f"sheets {slugs[slug]!r} and {worksheet.title!r} both slugify to {slug!r} — would overwrite"
            raise SlugCollisionError(msg)
        slugs[slug] = worksheet.title
        target = out_dir / f"{slug}.csv"
        with target.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(rows)
        logger.info("wrote %s (%d rows)", target.relative_to(REPO_ROOT), len(rows))
        written.append(target)
    return written


def main() -> None:
    """CLI entry point: extract the frozen workbook's sheets to text CSVs."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_XLSX, help="frozen .xlsx to read")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="directory for the CSV mirror")
    parser.add_argument("--force", action="store_true", help="overwrite an existing extraction")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    written = extract(args.source, args.out, force=args.force)
    logger.info("extracted %d sheet(s) to %s", len(written), args.out.relative_to(REPO_ROOT))


if __name__ == "__main__":
    main()
