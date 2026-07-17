#!/usr/bin/env python3
"""Rebuild regras-sisprev.csv from the okf/regras-sisprev/ bundle (uses pandas).

Reads the column order from the dataset doc's (``regras-sisprev.md``)
frontmatter and one row per ``regras/regra-NNNN.md`` doc, so the output
matches ``csv_to_okf.py``'s input row-for-row (the source export's stray
leading blank row is reproduced explicitly below).
"""

from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

import pandas as pd
import yaml
from okf_common import BODY_COLUMNS, BODY_HEADINGS, DATASET_DOC, DEFAULT_BUNDLE, DEFAULT_CSV, slugify_column

logger = logging.getLogger(__name__)

HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)
HEADING_TO_COLUMN = {heading: col for col, heading in BODY_HEADINGS.items()}


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


def load_bundle(bundle_dir: Path) -> pd.DataFrame:
    """Load every regra doc in bundle_dir into a DataFrame shaped like the original CSV."""
    dataset_text = (bundle_dir / DATASET_DOC).read_text(encoding="utf-8")
    _, dataset_fm_text, _ = dataset_text.split("---", 2)
    dataset_fm = yaml.safe_load(dataset_fm_text)
    columns: list[str] = dataset_fm["columns"]
    slugs = {col: slugify_column(col) for col in columns if col not in BODY_COLUMNS}

    doc_paths = sorted((bundle_dir / "regras").glob("regra-*.md"))
    rows = []
    for doc_path in doc_paths:
        frontmatter, sections = parse_doc(doc_path.read_text(encoding="utf-8"))
        row = {}
        for col in columns:
            row[col] = sections.get(col, "") if col in BODY_COLUMNS else frontmatter.get(slugs[col], "")
        rows.append(row)

    return pd.DataFrame(rows, columns=columns)


def convert(bundle_dir: Path, out_path: Path) -> int:
    """Rebuild the CSV at out_path from bundle_dir. Returns the row count."""
    df = load_bundle(bundle_dir)

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
    parser.add_argument("--out", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()

    n = convert(args.bundle, args.out)
    logger.info("Wrote %d rows to %s", n, args.out)


if __name__ == "__main__":
    main()
