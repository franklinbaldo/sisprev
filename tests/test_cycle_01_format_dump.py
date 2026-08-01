from __future__ import annotations

import difflib
from pathlib import Path

from scripts.md_format import format_markdown


def test_cycle_01_is_formatted() -> None:
    path = Path("okf/regras-sisprev/ciclos/ciclo-01.md")
    original = path.read_text(encoding="utf-8")
    formatted = format_markdown(original)
    if formatted == original:
        return
    print("BEGIN_CYCLE_01_FORMAT_DIFF")
    print(
        "".join(
            difflib.unified_diff(
                original.splitlines(keepends=True),
                formatted.splitlines(keepends=True),
                fromfile="original",
                tofile="formatted",
            )
        )
    )
    print("END_CYCLE_01_FORMAT_DIFF")
    raise AssertionError("format diff emitted above")
