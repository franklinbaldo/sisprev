"""Tests for md_format — the deterministic-markdown gate (idempotency + LF)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from md_format import format_markdown, main

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_format_markdown_is_idempotent() -> None:
    """Formatting an already-formatted doc is a no-op — the normal form is stable."""
    once = format_markdown("#  Título\n\n\ntexto\n")
    assert format_markdown(once) == once


def test_check_flags_crlf_line_endings(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """--check must catch CRLF line endings.

    The LF normal form it enforces isn't visible to a universal-newline
    read, which would silently translate CRLF to LF before the comparison.
    """
    doc = tmp_path / "crlf.md"
    # Content already in mdformat normal form except for the endings, so the
    # only thing that can flag it is the CRLF.
    doc.write_bytes(b"# Titulo\r\n\r\ntexto\r\n")

    monkeypatch.setattr("sys.argv", ["md_format.py", "--check", str(doc)])
    assert main() == 1
    assert "crlf.md" in capsys.readouterr().err


def test_check_passes_on_lf(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A formatted LF doc passes --check with exit 0."""
    doc = tmp_path / "lf.md"
    doc.write_text(format_markdown("# Titulo\n\ntexto\n"), encoding="utf-8", newline="\n")

    monkeypatch.setattr("sys.argv", ["md_format.py", "--check", str(doc)])
    assert main() == 0
