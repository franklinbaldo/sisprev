"""Convert data/raw/regras-sisprev.csv into an OKF bundle under okf/regras-sisprev/.

One concept doc per rule row (``type: Regra``), plus a dataset doc
(``regras-sisprev.md``) that records the original column order so
``okf_to_csv.py`` can rebuild a CSV losslessly. The CSV <-> .md mapping
itself is declared once in ``regra_schema.py`` (RFC 0001, P13.2). See
https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

This is the ONE-TIME BOOTSTRAP for the bundle. After the initial import,
rules are edited directly in ``okf/regras-sisprev/regras/regra-*.md`` —
never in a CSV, never by re-running this script. Re-running it against the
existing --out bundle overwrites every regra doc from data/raw/regras-sisprev.csv
again, silently discarding any audit edits made since the import.
"""

from __future__ import annotations

import argparse
import logging
import shutil
import tempfile
from pathlib import Path

import pandas as pd
import yaml
from md_format import write_markdown
from okf_common import DATASET_DOC, DEFAULT_BUNDLE, ORIGINAL_CSV, BundleAlreadyInitializedError
from regra_schema import CSV_COLUMN_NAMES, FRONTMATTER_KEYS, render_schema_table

logger = logging.getLogger(__name__)

DATASET_DESCRIPTION = (
    "Catálogo de regras de aposentadoria e pensão por morte do Sisprev, "
    "com fundamentação legal, elegibilidade e forma de cálculo."
)


def load_rows(csv_path: Path) -> pd.DataFrame:
    """Read the rules CSV, skipping its stray leading blank export row.

    ``keep_default_na=False``: this is a text rules table, not numeric data —
    an empty cell means "empty string", not NaN. Validates the header
    against the P13.2 normative map (regra_schema.CSV_COLUMN_NAMES) — every
    original column must appear exactly once, in order.
    """
    df = pd.read_csv(csv_path, skiprows=1, keep_default_na=False, dtype=str)
    actual = tuple(df.columns)
    if actual != CSV_COLUMN_NAMES:
        msg = (
            f"{csv_path} columns don't match the P13.2 normative map "
            f"(regra_schema.COLUMNS).\nExpected: {CSV_COLUMN_NAMES}\nGot:      {actual}"
        )
        raise ValueError(msg)
    return df


def build_doc(row_index: int, row: pd.Series) -> str:
    """Render one CSV row as an OKF concept doc — all 27 columns in frontmatter.

    Every original column (fundamentação included) is a frontmatter key: the
    frontmatter *is* the deployable Sisprev rule. The body is left empty for
    the auditor's own analysis of the rule (never a CSV column, never
    deployed). NOME maps to ``nome`` like any other column (regra_schema.py) —
    no special-casing: the P13.2 map is the single source for every field.
    """
    frontmatter = {"type": "Regra", "id": f"regra-{row_index:04d}", "row_index": row_index}
    for col in CSV_COLUMN_NAMES:
        frontmatter[FRONTMATTER_KEYS[col]] = row[col]

    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    return f"---\n{fm_text}---\n"


def _write_regras(df: pd.DataFrame, regras_dir: Path) -> list[str]:
    """Write one concept doc per row into regras_dir. Returns its index.md TOC lines."""
    regras_dir.mkdir(parents=True, exist_ok=True)
    toc_lines = []
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        doc = build_doc(i, row)
        write_markdown(regras_dir / f"regra-{i:04d}.md", doc)
        toc_lines.append(f"* [{row['NOME']}](regra-{i:04d}.md) - {row['TIPO DE BENEFICIO']}")
    return toc_lines


def _write_regras_index(toc_lines: list[str], regras_dir: Path) -> None:
    """Write regras/index.md — a plain listing, no frontmatter (SPEC.md §6)."""
    body = "# Regras\n\n" + "\n".join(toc_lines) + "\n"
    write_markdown(regras_dir / "index.md", body)


def _write_dataset_doc(df: pd.DataFrame, out_dir: Path) -> None:
    """Write the dataset-level concept doc (frontmatter + "# Schema") — SPEC.md Appendix A."""
    frontmatter = {
        "type": "Dataset",
        "title": "Regras do Sisprev — Regime Próprio de Previdência (RO)",
        "description": DATASET_DESCRIPTION,
        "tags": ["previdencia", "aposentadoria", "pensao", "sisprev", "rondonia"],
        "source_file": "data/raw/regras-sisprev.csv",
        "row_count": len(df),
        "columns": list(CSV_COLUMN_NAMES),
    }
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body = (
        f"{DATASET_DESCRIPTION}\n\n"
        "# Schema\n\n"
        f"{render_schema_table()}\n\n"
        "# Regras\n\n"
        "Uma regra por linha da planilha original — ver [regras/](regras/index.md).\n"
    )
    write_markdown(out_dir / DATASET_DOC, f"---\n{fm_text}---\n\n{body}")


def _write_root_index(df: pd.DataFrame, out_dir: Path) -> None:
    """Write the bundle-root index.md. Frontmatter here is limited to okf_version (SPEC.md §11)."""
    fm_text = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    body = (
        "# Regras do Sisprev\n\n"
        f"* [{DATASET_DOC}]({DATASET_DOC}) - {DATASET_DESCRIPTION}\n"
        f"* [regras/](regras/index.md) - {len(df)} regras individuais, uma por linha da planilha original.\n"
    )
    write_markdown(out_dir / "index.md", f"---\n{fm_text}---\n\n{body}")


def _is_already_initialized(out_dir: Path) -> bool:
    """True if out_dir already holds a bootstrapped bundle (any regra-*.md)."""
    regras_dir = out_dir / "regras"
    return regras_dir.is_dir() and any(regras_dir.glob("regra-*.md"))


def convert(csv_path: Path, out_dir: Path, *, force: bool = False) -> int:
    """Write the OKF bundle (root index, dataset doc, regras/) into out_dir. Returns the row count.

    Refuses to touch out_dir if it already holds a bootstrapped bundle,
    unless force=True — see the module docstring. Builds into a temporary
    directory and only replaces out_dir after the build fully succeeds, so
    a failure partway through never leaves a half-written bundle behind.

    Raises BundleAlreadyInitializedError if out_dir already has regra docs
    and force is not set.
    """
    if not force and _is_already_initialized(out_dir):
        msg = (
            f"{out_dir} already contains regra docs — refusing to overwrite a live "
            "bundle (this would silently discard any audit edits made since the "
            "import). Pass force=True (CLI: --force) only if you understand you "
            "are discarding those edits."
        )
        raise BundleAlreadyInitializedError(msg)

    df = load_rows(csv_path)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_out = Path(tmp) / "bundle"
        regras_dir = tmp_out / "regras"
        toc_lines = _write_regras(df, regras_dir)
        _write_regras_index(toc_lines, regras_dir)
        _write_dataset_doc(df, tmp_out)
        _write_root_index(df, tmp_out)

        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tmp_out), str(out_dir))

    return len(df)


def main() -> None:
    """CLI entry point: convert --csv into an OKF bundle at --out."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=ORIGINAL_CSV)
    parser.add_argument("--out", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an already-initialized bundle — discards any audit edits made since import.",
    )
    args = parser.parse_args()

    n = convert(args.csv, args.out, force=args.force)
    logger.info("Wrote %d concept docs to %s", n, args.out / "regras")


if __name__ == "__main__":
    main()
