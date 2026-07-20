"""CSV -> OKF -> CSV round-trip must reproduce the same tabular data."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import pytest
from csv_to_okf import convert as csv_to_okf
from okf_common import ORIGINAL_CSV, OriginalCsvProtectedError
from okf_to_csv import convert as okf_to_csv
from okf_to_csv import load_bundle

if TYPE_CHECKING:
    from pathlib import Path


def _read(csv_path: Path) -> pd.DataFrame:
    """Read a regras-sisprev CSV the same way the conversion scripts do."""
    return pd.read_csv(csv_path, skiprows=1, keep_default_na=False, dtype=str)


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """Build a fresh OKF bundle from the real source CSV in a temp dir."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def test_bundle_has_one_doc_per_row(bundle_dir: Path) -> None:
    """Every CSV data row becomes exactly one concept doc."""
    original = _read(ORIGINAL_CSV)
    docs = list((bundle_dir / "regras").glob("regra-*.md"))
    assert len(docs) == len(original)


def test_roundtrip_matches_original(bundle_dir: Path, tmp_path: Path) -> None:
    """CSV -> bundle -> CSV reproduces the original DataFrame exactly."""
    original = _read(ORIGINAL_CSV)

    rebuilt_csv = tmp_path / "rebuilt.csv"
    okf_to_csv(bundle_dir, rebuilt_csv)
    rebuilt = _read(rebuilt_csv)

    pd.testing.assert_frame_equal(original, rebuilt)


def test_load_bundle_matches_original(bundle_dir: Path) -> None:
    """load_bundle() alone (no CSV write) already matches the original DataFrame."""
    original = _read(ORIGINAL_CSV)
    loaded = load_bundle(bundle_dir)

    pd.testing.assert_frame_equal(original, loaded)


def test_okf_to_csv_refuses_to_overwrite_original(bundle_dir: Path) -> None:
    """okf_to_csv.convert() must never write to the frozen original import."""
    original_bytes = ORIGINAL_CSV.read_bytes()

    with pytest.raises(OriginalCsvProtectedError):
        okf_to_csv(bundle_dir, ORIGINAL_CSV)

    assert ORIGINAL_CSV.read_bytes() == original_bytes
