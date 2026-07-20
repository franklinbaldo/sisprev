"""The committed data/regras-sisprev.csv must always match the committed bundle.

Rules are edited in okf/regras-sisprev/regras/*.md, never in a CSV by hand.
data/regras-sisprev.csv is a derived, always-regenerated export of that
bundle's current (possibly audit-corrected) state — this test (and CI) fail
if someone edits a regra doc without regenerating and committing it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
from okf_common import DEFAULT_BUNDLE, DEFAULT_REBUILT_CSV
from okf_to_csv import load_bundle

if TYPE_CHECKING:
    from pathlib import Path


def _read(csv_path: Path) -> pd.DataFrame:
    """Read a regras-sisprev CSV the same way the conversion scripts do."""
    return pd.read_csv(csv_path, skiprows=1, keep_default_na=False, dtype=str)


def test_committed_csv_matches_committed_bundle() -> None:
    """data/regras-sisprev.csv must be exactly what okf_to_csv.py would produce right now."""
    committed = _read(DEFAULT_REBUILT_CSV)
    current = load_bundle(DEFAULT_BUNDLE)

    pd.testing.assert_frame_equal(committed, current)
