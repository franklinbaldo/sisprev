"""Rebuild a flat CSV from the okf/regras-sisprev/ bundle (uses pandas).

Reads the column order from the dataset doc's (``regras-sisprev.md``)
frontmatter and one row per ``regras/regra-NNNN.md`` doc, using the P13.2
normative map (``regra_schema.py``) as the single source for the CSV <-> .md
mapping. The output is a derived, disposable export — it defaults to
``data/regras-sisprev.csv``, never ``data/raw/regras-sisprev.csv`` (the
frozen original import used as the audit baseline). Writing to that path is
a hard error — see ``guard_not_original``.

Per RFC 0001 P12, the derived CSV carries the 27 original columns PLUS the
administrative fields (``status_regra``, ``motivo_inativacao``,
``status_auditoria``, ``auditado_por``, ``auditado_em`` — see
``regra_schema.ADMIN_FIELD_DEFAULTS`` — and ``atos_validacao``, JSON-encoded
since it's a list, not a scalar), appended at the end with explicit
defaults so no cell is ever "unknown".

Also regenerates ``regras/index.md`` from the live docs on every run, so
its titles can never silently drift from a ``nome`` corrected during audit
(see ``_regenerate_regras_index``).
"""

from __future__ import annotations

import argparse
import json
import logging
import re
from pathlib import Path

import pandas as pd
import yaml
from okf_common import (
    DATASET_DOC,
    DEFAULT_BUNDLE,
    DEFAULT_REBUILT_CSV,
    BundleIntegrityError,
    guard_not_original,
)
from regra_schema import (
    ADMIN_FIELD_DEFAULTS,
    ATOS_VALIDACAO_KEY,
    BODY_COLUMNS,
    BODY_HEADINGS,
    FRONTMATTER_KEYS,
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

    Regenerated on every convert() so a `nome` corrected during audit can
    never leave a stale copy behind in the listing.
    """
    toc_lines = []
    for doc_path in doc_paths:
        frontmatter, _ = parse_doc(doc_path.read_text(encoding="utf-8"))
        nome = frontmatter.get("nome", "")
        tipo = frontmatter.get("tipo_de_beneficio", "")
        toc_lines.append(f"* [{nome}]({doc_path.name}) - {tipo}")
    body = "# Regras\n\n" + "\n".join(toc_lines) + "\n"
    (bundle_dir / "regras" / "index.md").write_text(body, encoding="utf-8")


def _rows_from_docs(doc_paths: list[Path], columns: list[str]) -> list[dict]:
    """Read each doc into a row dict keyed by original CSV column name."""
    rows = []
    for doc_path in doc_paths:
        frontmatter, sections = parse_doc(doc_path.read_text(encoding="utf-8"))
        row = {}
        for col in columns:
            if col in BODY_COLUMNS:
                row[col] = sections.get(col, "")
            else:
                row[col] = frontmatter.get(FRONTMATTER_KEYS[col], "")
        rows.append(row)
    return rows


def _admin_rows_from_docs(doc_paths: list[Path]) -> list[dict]:
    """Read each doc's administrative fields (P2.1/P7/P11), with explicit defaults (P12).

    ``atos_validacao`` (P7) is a list, unlike the rest of ADMIN_FIELD_DEFAULTS
    (scalar strings) — it's JSON-encoded into its own CSV cell so the
    derived export still has no "unknown" or malformed cell.
    """
    rows = []
    for doc_path in doc_paths:
        frontmatter, _ = parse_doc(doc_path.read_text(encoding="utf-8"))
        row = {key: frontmatter.get(key, default) for key, default in ADMIN_FIELD_DEFAULTS.items()}
        row[ATOS_VALIDACAO_KEY] = json.dumps(
            frontmatter.get(ATOS_VALIDACAO_KEY, []),
            ensure_ascii=False,
        )
        rows.append(row)
    return rows


def validate_bundle_identity(bundle_dir: Path) -> None:
    """Public wrapper: raise BundleIntegrityError if the regra sequence is incoherent.

    Used by validar_regras.py (P10, camada 1) without reaching into the
    module's private helpers.
    """
    _, row_count = _read_dataset_meta(bundle_dir)
    _validate_identity(bundle_dir, row_count)


def load_bundle(bundle_dir: Path) -> pd.DataFrame:
    """Load every regra doc in bundle_dir into a DataFrame shaped like the original CSV.

    Returns only the 27 original columns — see load_bundle_extended() for
    the administrative fields (P12).

    Raises BundleIntegrityError if the docs don't form a coherent 1..N
    sequence — see _validate_identity.
    """
    columns, row_count = _read_dataset_meta(bundle_dir)
    doc_paths = _validate_identity(bundle_dir, row_count)
    rows = _rows_from_docs(doc_paths, columns)

    return pd.DataFrame(rows, columns=columns)


def load_bundle_extended(bundle_dir: Path) -> pd.DataFrame:
    """Load the bundle into a DataFrame with the 27 original columns PLUS admin fields (P12)."""
    columns, row_count = _read_dataset_meta(bundle_dir)
    doc_paths = _validate_identity(bundle_dir, row_count)
    rows = _rows_from_docs(doc_paths, columns)
    admin_rows = _admin_rows_from_docs(doc_paths)
    for row, admin_row in zip(rows, admin_rows, strict=True):
        row.update(admin_row)

    all_columns = [*columns, *ADMIN_FIELD_DEFAULTS, ATOS_VALIDACAO_KEY]
    return pd.DataFrame(rows, columns=all_columns)


def convert(bundle_dir: Path, out_path: Path) -> int:
    """Rebuild the CSV at out_path from bundle_dir. Returns the row count.

    The CSV carries the 27 original columns plus the administrative fields
    (P12). Also regenerates regras/index.md from the live docs (see
    _regenerate_regras_index). Raises OriginalCsvProtectedError if out_path
    is the frozen original, or BundleIntegrityError if the bundle is
    structurally corrupt.
    """
    guard_not_original(out_path)

    _, row_count = _read_dataset_meta(bundle_dir)
    doc_paths = _validate_identity(bundle_dir, row_count)
    _regenerate_regras_index(bundle_dir, doc_paths)

    df = load_bundle_extended(bundle_dir)

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
