from __future__ import annotations

import base64
from pathlib import Path

from scripts.md_format import format_markdown


def test_cycle_01_is_formatted() -> None:
    path = Path("okf/regras-sisprev/ciclos/ciclo-01.md")
    original = path.read_text(encoding="utf-8")
    formatted = format_markdown(original)
    if formatted == original:
        return
    encoded = base64.b64encode(formatted.encode()).decode()
    print("BEGIN_CYCLE_01_FORMATTED_BASE64")
    for start in range(0, len(encoded), 120):
        print(encoded[start : start + 120])
    print("END_CYCLE_01_FORMATTED_BASE64")
    raise AssertionError("formatted output emitted above")
