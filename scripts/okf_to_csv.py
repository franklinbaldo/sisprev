"""Rebuild a flat CSV from the okf/regras-sisprev/ bundle (uses pandas).

Reads the column order from the dataset doc's (``regras-sisprev.md``)
frontmatter and one row per ``regras/regra-NNNN.md`` doc. The output is a
derived, disposable export — it defaults to ``data/regras-sisprev.csv``,
never ``data/raw/regras-sisprev.csv`` (the frozen original import used as
the audit baseline). Writing to that path is a hard error — see
``guard_not_original``.

Also regenerates ``regras/index.md`` from the live docs on every run, so
its titles can never silently drift from a ``title`` corrected during
audit (see ``_regenerate_regras_index``).
"""

from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

import pandas as pd
import yaml
from okf_common import (
    BODY_COLUMNS,
    BODY_HEADINGS,
    DATASET_DOC,
    DEFAULT_BUNDLE,
    DEFAULT_REBUILT_CSV,
    BundleIntegrityError,
    guard_not_original,
    slugify_column,
)

logger = logging.getLogger(__name__)

HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)
HEADING_TO_COLUMN = {heading: col for col, heading in BODY_HEADINGS.items()}
DOC_NAME_RE = re.compile(r"^regra-(\d+)$")


def parse_doc(text: str) -> tuple[dict, dict[str, str]]:
    """Split a concept doc into its frontmatter dict and body sections keyed by column name."""
    _, fm_text, body = text.split("---", 2)
    frontmatter = yaml.safe_load(fm_text)

    sections: dict[str, str] = {}
    matches = list(HEADING_RE.finditer(body))
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        col = HEADING_TO_COLUMN.get(heading)
        if col:
            sections[col] = body[start:end].strip("\n")
    return frontmatter, sections


def _read_dataset_meta(bundle_dir: Path) -> tuple[list[str], int]:
    """Read (columns, row_count) from the dataset doc's frontmatter."""
    dataset_text = (bundle_dir / DATASET_DOC).read_text(encoding="utf-8")
    _, dataset_fm_text, _ = dataset_text.split("---", 2)
    dataset_fm = yaml.safe_load(dataset_fm_text)
    return dataset_fm["columns"], dataset_fm["row_count"]


def _validate_identity(bundle_dir: Path, expected_row_count: int) -> list[Path]:
    """Validate every regra doc's id/row_index matches its filename, forming exactly 1..N.

    Catches structural corruption (a dropped, duplicated, or mislabeled
    regra doc) that a bare document-count comparison would miss. Returns
    the doc paths in row_index order on success.

    Raises BundleIntegrityError with every problem found, not just the first.
    """
    doc_paths = sorted((bundle_dir / "regras").glob("regra-*.md"))
    errors: list[str] = []
    by_index: dict[int, Path] = {}

    for doc_path in doc_paths:
        stem = doc_path.stem
        match = DOC_NAME_RE.match(stem)
        if match is None:
            errors.append(f"{doc_path.name}: filename is not of the form regra-NNNN.md")
            continue

        expected_index = int(match.group(1))
        frontmatter, _ = parse_doc(doc_path.read_text(encoding="utf-8"))
        fm_id = frontmatter.get("id")
        fm_row_index = frontmatter.get("row_index")

        if fm_id != stem:
            errors.append(f"{doc_path.name}: frontmatter id={fm_id!r} does not match filename")
        if fm_row_index != expected_index:
            errors.append(
                f"{doc_path.name}: frontmatter row_index={fm_row_index!r}, expected {expected_index}"
            )
        if expected_index in by_index:
            errors.append(
                f"duplicate row_index {expected_index}: {by_index[expected_index].name} and {doc_path.name}"
            )
        else:
            by_index[expected_index] = doc_path

    expected_indices = set(range(1, expected_row_count + 1))
    missing = sorted(expected_indices - by_index.keys())
    extra = sorted(by_index.keys() - expected_indices)
    if missing:
        errors.append(f"missing row_index(es): {missing}")
    if extra:
        errors.append(f"row_index(es) beyond declared row_count={expected_row_count}: {extra}")

    if errors:
        msg = "Bundle integrity check failed:\n  " + "\n  ".join(errors)
        raise BundleIntegrityError(msg)

    return [by_index[i] for i in sorted(by_index)]


def _regenerate_regras_index(bundle_dir: Path, doc_paths: list[Path]) -> None:
    """Rewrite regras/index.md from the live docs — SPEC.md §6, no frontmatter.

    Regenerated on every convert() so a `title` corrected during audit can
    never leave a stale copy behind in the listing.
    """
    toc_lines = []
    for doc_path in doc_paths:
        frontmatter, _ = parse_doc(doc_path.read_text(encoding="utf-8"))
        title = frontmatter.get("title", "")
        tipo = frontmatter.get("tipo_de_beneficio", "")
        toc_lines.append(f"* [{title}]({doc_path.name}) - {tipo}")
    body = "# Regras\n\n" + "\n".join(toc_lines) + "\n"
    (bundle_dir / "regras" / "index.md").write_text(body, encoding="utf-8")


def _rows_from_docs(doc_paths: list[Path], columns: list[str], slugs: dict[str, str]) -> list[dict]:
    """Read each doc into a row dict keyed by original CSV column name."""
    rows = []
    for doc_path in doc_paths:
        frontmatter, sections = parse_doc(doc_path.read_text(encoding="utf-8"))
        row = {}
        for col in columns:
            if col in BODY_COLUMNS:
                row[col] = sections.get(col, "")
            elif col == "NOME":
                row[col] = frontmatter.get("title", "")
            else:
                row[col] = frontmatter.get(slugs[col], "")
        rows.append(row)
    return rows


def load_bundle(bundle_dir: Path) -> pd.DataFrame:
    """Load every regra doc in bundle_dir into a DataFrame shaped like the original CSV.

    Raises BundleIntegrityError if the docs don't form a coherent 1..N
    sequence — see _validate_identity.
    """
    columns, row_count = _read_dataset_meta(bundle_dir)
    slugs = {col: slugify_column(col) for col in columns if col not in BODY_COLUMNS and col != "NOME"}

    doc_paths = _validate_identity(bundle_dir, row_count)
    rows = _rows_from_docs(doc_paths, columns, slugs)

    return pd.DataFrame(rows, columns=columns)


def convert(bundle_dir: Path, out_path: Path) -> int:
    """Rebuild the CSV at out_path from bundle_dir. Returns the row count.

    Also regenerates regras/index.md from the live docs (see
    _regenerate_regras_index). Raises OriginalCsvProtectedError if out_path
    is the frozen original, or BundleIntegrityError if the bundle is
    structurally corrupt.
    """
    guard_not_original(out_path)

    columns, row_count = _read_dataset_meta(bundle_dir)
    slugs = {col: slugify_column(col) for col in columns if col not in BODY_COLUMNS and col != "NOME"}
    doc_paths = _validate_identity(bundle_dir, row_count)

    _regenerate_regras_index(bundle_dir, doc_paths)

    rows = _rows_from_docs(doc_paths, columns, slugs)
    df = pd.DataFrame(rows, columns=columns)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        fh.write("," * (len(df.columns) - 1) + "\n")  # stray blank row from the original export
        df.to_csv(fh, index=False, lineterminator="\n")

    return len(df)


def main() -> None:
    """CLI entry point: rebuild --out from the --bundle directory."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--out", type=Path, default=DEFAULT_REBUILT_CSV)
    args = parser.parse_args()

    n = convert(args.bundle, args.out)
    logger.info("Wrote %d rows to %s", n, args.out)


if __name__ == "__main__":
    main()
