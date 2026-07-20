r"""Deterministic markdown formatting for every generated .md (idempotency).

Every script that *writes* a bundle document routes through ``write_markdown``
so regeneration always produces byte-identical output, on any platform:

- ``mdformat`` normalises the markdown (headings, lists, GFM tables) to a
  stable normal form;
- the ``frontmatter`` plugin re-serialises the YAML frontmatter consistently,
  so a value's line-wrapping never drifts between yaml.safe_dump and a later
  edit;
- writing with ``newline="\n"`` forces LF endings, so a Windows run of
  ``gerar_indices`` can't introduce CRLF churn a Linux CI would revert.

The formatting is content-preserving: it restyles, never rewrites — the CSV
round-trip (``okf_to_csv``) and every detector read the *parsed* frontmatter
values, which are identical before and after formatting.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import mdformat

# GFM covers pipe tables (used by the dataset "# Schema" doc and the analysis
# reports); frontmatter keeps the YAML block intact and canonically styled.
_MD_EXTENSIONS = frozenset({"frontmatter", "gfm"})

# number=True keeps ordered lists numbered consecutively (1. 2. 3.) instead of
# mdformat's default of rewriting every marker to "1." — the consecutive form
# matches how the RFC/prose docs are hand-authored, so formatting them causes
# no churn.
_MD_OPTIONS = {"number": True}


def format_markdown(text: str) -> str:
    """Return ``text`` in mdformat's stable normal form (frontmatter + GFM)."""
    return mdformat.text(text, extensions=_MD_EXTENSIONS, options=_MD_OPTIONS)


def write_markdown(path: Path, text: str) -> None:
    """Write a generated markdown doc, formatted and with LF endings.

    The single write path for every generated ``.md`` — using it everywhere
    is what makes ``gerar_indices``/``csv_to_okf`` regeneration idempotent.
    """
    path.write_text(format_markdown(text), encoding="utf-8", newline="\n")


def _iter_markdown(paths: list[Path]) -> list[Path]:
    """Every .md under the given files/dirs, sorted, so runs are deterministic."""
    found: set[Path] = set()
    for path in paths:
        if path.is_dir():
            found.update(path.rglob("*.md"))
        elif path.suffix == ".md":
            found.add(path)
    return sorted(found)


def main() -> int:
    """Format (or, with --check, verify) every .md under the given paths.

    The single entry point for both the pre-commit format step and the CI
    gate, so the CLI can never drift from ``write_markdown``'s formatting —
    both go through ``format_markdown`` (same extensions and options).
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="files or directories to format")
    parser.add_argument("--check", action="store_true", help="report unformatted files, write nothing")
    args = parser.parse_args()

    unformatted: list[Path] = []
    for md_path in _iter_markdown(args.paths):
        # newline="" keeps the on-disk endings intact — the default universal-
        # newline read would translate CRLF to LF before the comparison, so a
        # CRLF file would pass the check the LF-normal-form is meant to catch.
        original = md_path.read_text(encoding="utf-8", newline="")
        formatted = format_markdown(original)
        if formatted == original:
            continue
        if args.check:
            unformatted.append(md_path)
        else:
            md_path.write_text(formatted, encoding="utf-8", newline="\n")

    if args.check and unformatted:
        sys.stderr.write("Markdown not formatted (run: uv run python scripts/md_format.py okf docs):\n")
        sys.stderr.writelines(f"  {p}\n" for p in unformatted)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
