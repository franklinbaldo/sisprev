#!/usr/bin/env python3
"""Convert data/raw/regras-sisprev.csv into an OKF bundle under okf/regras-sisprev/.

One concept doc per rule row (``type: regra``), plus an ``index.md`` dataset
doc that records the original column order so ``okf_to_csv.py`` can rebuild
the CSV losslessly. See https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd
import yaml
from okf_common import (
    BODY_COLUMNS,
    BODY_HEADINGS,
    DATASET_DOC,
    DEFAULT_BUNDLE,
    DEFAULT_CSV,
    render_schema_table,
    slugify_column,
)

logger = logging.getLogger(__name__)

DATASET_DESCRIPTION = (
    "Catálogo de regras de aposentadoria e pensão por morte do Sisprev, "
    "com fundamentação legal, elegibilidade e forma de cálculo."
)


def load_rows(csv_path: Path) -> pd.DataFrame:
    """Read the rules CSV, skipping its stray leading blank export row.

    ``keep_default_na=False``: this is a text rules table, not numeric data —
    an empty cell means "empty string", not NaN.
    """
    return pd.read_csv(csv_path, skiprows=1, keep_default_na=False, dtype=str)


def build_doc(row_index: int, row: pd.Series, columns: list[str], slugs: dict[str, str]) -> str:
    """Render one CSV row as an OKF concept doc (frontmatter + body)."""
    frontmatter = {
        "type": "Regra",
        "id": f"regra-{row_index:04d}",
        "row_index": row_index,
        "title": row["NOME"],
    }
    for col in columns:
        if col in BODY_COLUMNS:
            continue
        frontmatter[slugs[col]] = row[col]

    body_parts = [f"# {BODY_HEADINGS[col]}\n\n{row[col]}\n" for col in BODY_COLUMNS]
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    return f"---\n{fm_text}---\n\n" + "\n".join(body_parts)


def _write_regras(df: pd.DataFrame, columns: list[str], slugs: dict[str, str], regras_dir: Path) -> list[str]:
    """Write one concept doc per row into regras_dir. Returns its index.md TOC lines."""
    regras_dir.mkdir(parents=True, exist_ok=True)
    toc_lines = []
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        doc = build_doc(i, row, columns, slugs)
        (regras_dir / f"regra-{i:04d}.md").write_text(doc, encoding="utf-8")
        toc_lines.append(f"* [{row['NOME']}](regra-{i:04d}.md) - {row['TIPO DE BENEFICIO']}")
    return toc_lines


def _write_regras_index(toc_lines: list[str], regras_dir: Path) -> None:
    """Write regras/index.md — a plain listing, no frontmatter (SPEC.md §6)."""
    body = "# Regras\n\n" + "\n".join(toc_lines) + "\n"
    (regras_dir / "index.md").write_text(body, encoding="utf-8")


def _write_dataset_doc(df: pd.DataFrame, columns: list[str], out_dir: Path) -> None:
    """Write the dataset-level concept doc (frontmatter + "# Schema") — SPEC.md Appendix A."""
    frontmatter = {
        "type": "Dataset",
        "title": "Regras do Sisprev — Regime Próprio de Previdência (RO)",
        "description": DATASET_DESCRIPTION,
        "tags": ["previdencia", "aposentadoria", "pensao", "sisprev", "rondonia"],
        "source_file": "data/raw/regras-sisprev.csv",
        "row_count": len(df),
        "columns": columns,
    }
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body = (
        f"{DATASET_DESCRIPTION}\n\n"
        "# Schema\n\n"
        f"{render_schema_table(columns)}\n\n"
        "# Regras\n\n"
        "Uma regra por linha da planilha original — ver [regras/](regras/index.md).\n"
    )
    (out_dir / DATASET_DOC).write_text(f"---\n{fm_text}---\n\n{body}", encoding="utf-8")


def _write_root_index(df: pd.DataFrame, out_dir: Path) -> None:
    """Write the bundle-root index.md. Frontmatter here is limited to okf_version (SPEC.md §11)."""
    fm_text = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    body = (
        "# Regras do Sisprev\n\n"
        f"* [{DATASET_DOC}]({DATASET_DOC}) - {DATASET_DESCRIPTION}\n"
        f"* [regras/](regras/index.md) - {len(df)} regras individuais, uma por linha da planilha original.\n"
    )
    (out_dir / "index.md").write_text(f"---\n{fm_text}---\n\n{body}", encoding="utf-8")


def convert(csv_path: Path, out_dir: Path) -> int:
    """Write the OKF bundle (root index, dataset doc, regras/) into out_dir. Returns the row count."""
    df = load_rows(csv_path)
    columns = list(df.columns)
    slugs = {col: slugify_column(col) for col in columns if col not in BODY_COLUMNS}

    regras_dir = out_dir / "regras"
    toc_lines = _write_regras(df, columns, slugs, regras_dir)
    _write_regras_index(toc_lines, regras_dir)
    _write_dataset_doc(df, columns, out_dir)
    _write_root_index(df, out_dir)

    return len(df)


def main() -> None:
    """CLI entry point: convert --csv into an OKF bundle at --out."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--out", type=Path, default=DEFAULT_BUNDLE)
    args = parser.parse_args()

    n = convert(args.csv, args.out)
    logger.info("Wrote %d concept docs to %s", n, args.out / "regras")


if __name__ == "__main__":
    main()
