"""Tests for the "derivar" command (RFC 0001, P10) — the only writer of derived artifacts."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bundle import Bundle
from csv_to_okf import convert as csv_to_okf
from gerar_indices import derive
from okf_common import ORIGINAL_CSV

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """A fresh bundle built from the real source CSV, no achados yet."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def test_derive_regenerates_regras_index_and_csv(bundle_dir: Path, tmp_path: Path) -> None:
    """derive() writes both the CSV and regras/index.md, matching the bundle's row count."""
    csv_out = tmp_path / "out.csv"
    rows = derive(bundle_dir, csv_out)

    row_count = len(Bundle.load(bundle_dir).regras)
    assert rows == row_count
    assert csv_out.exists()
    assert (bundle_dir / "regras" / "index.md").exists()


def test_derive_creates_an_empty_achados_index_when_none_exist_yet(bundle_dir: Path, tmp_path: Path) -> None:
    """A freshly bootstrapped bundle has no achados/ yet — derive() creates an empty index for it."""
    assert not (bundle_dir / "achados").is_dir()

    derive(bundle_dir, tmp_path / "out.csv")

    assert (bundle_dir / "achados" / "index.md").is_file()
    assert (bundle_dir / "index.md").read_text(encoding="utf-8").count("achado(s)") == 1


def test_derive_updates_achados_index_when_it_already_exists(bundle_dir: Path, tmp_path: Path) -> None:
    """A bundle with achados/ already present gets its index refreshed too."""
    (bundle_dir / "achados").mkdir()

    derive(bundle_dir, tmp_path / "out.csv")

    assert "0 achado(s)" in (bundle_dir / "index.md").read_text(encoding="utf-8")
