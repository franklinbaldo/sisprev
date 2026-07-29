"""Tests for the local archive of official sources."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import arquivo_de_fontes

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_construir_registers_documented_transcription_for_scanned_pdf(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A useful Markdown transcription makes a scanned PDF searchable."""
    fontes_dir = tmp_path / "fontes-oficiais"
    arquivos_dir = fontes_dir / "arquivos"
    transcricoes_dir = fontes_dir / "transcricoes"
    arquivos_dir.mkdir(parents=True)
    transcricoes_dir.mkdir()

    url = "https://example.test/emenda_146.pdf"
    (arquivos_dir / "example-emenda_146.pdf").write_bytes(b"%PDF scanned")
    (transcricoes_dir / "example-emenda_146.md").write_text(
        "# ECE 146\n\n" + ("texto pesquisável " * 200),
        encoding="utf-8",
    )

    monkeypatch.setattr(arquivo_de_fontes, "FONTES_DIR", fontes_dir)
    monkeypatch.setattr(arquivo_de_fontes, "ARQUIVOS_DIR", arquivos_dir)
    monkeypatch.setattr(arquivo_de_fontes, "TRANSCRICOES_DIR", transcricoes_dir)
    monkeypatch.setattr(arquivo_de_fontes, "MANIFESTO", fontes_dir / "manifesto.yaml")
    monkeypatch.setattr(arquivo_de_fontes, "coletar_urls", lambda: {url: {"ece-146-2021"}})
    monkeypatch.setattr(arquivo_de_fontes, "_extrair_texto", lambda _pdf: None)

    manifesto = arquivo_de_fontes.construir(baixar=False)

    arquivos = manifesto["arquivos"]
    assert isinstance(arquivos, list)
    registro = cast("dict[str, object]", arquivos[0])
    assert registro["texto"] == "transcricoes/example-emenda_146.md"
    assert registro["observacao"] == (
        "PDF original sem camada de texto; transcrição derivada e documentada disponível"
    )
