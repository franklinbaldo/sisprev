"""Bootstrap safety and structural integrity checks for the OKF bundle.

Covers the two integrity risks a plain round-trip test can't see:
csv_to_okf.py silently clobbering a live (already-edited) bundle, and
okf_to_csv.py accepting a structurally corrupt bundle (dropped, duplicated,
or mislabeled regra doc) as long as the document count looks right.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import pytest
import yaml
from csv_to_okf import convert as csv_to_okf
from okf_common import ORIGINAL_CSV, BundleAlreadyInitializedError, BundleIntegrityError
from okf_to_csv import load_bundle

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """Build a fresh OKF bundle from the real source CSV in a temp dir."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def test_bootstrap_refuses_to_overwrite_an_edited_bundle(bundle_dir: Path) -> None:
    """A second, non-forced csv_to_okf run must not touch a bundle with audit edits."""
    edited_doc = bundle_dir / "regras" / "regra-0001.md"
    edited_text = edited_doc.read_text(encoding="utf-8").replace(
        "title: Aposentadoria por Invalidez Anterior E.C 20/1998",
        "title: CORRIGIDO EM AUDITORIA — não pode ser perdido",
    )
    edited_doc.write_text(edited_text, encoding="utf-8")

    with pytest.raises(BundleAlreadyInitializedError):
        csv_to_okf(ORIGINAL_CSV, bundle_dir)

    assert edited_doc.read_text(encoding="utf-8") == edited_text


def test_bootstrap_force_does_overwrite(bundle_dir: Path) -> None:
    """force=True is the explicit escape hatch — it does overwrite."""
    edited_doc = bundle_dir / "regras" / "regra-0001.md"
    edited_doc.write_text(
        edited_doc.read_text(encoding="utf-8").replace("title:", "title: EDITADO —"),
        encoding="utf-8",
    )

    csv_to_okf(ORIGINAL_CSV, bundle_dir, force=True)

    assert "EDITADO" not in edited_doc.read_text(encoding="utf-8")


def test_bootstrap_leaves_nothing_behind_on_a_bad_out_dir(tmp_path: Path) -> None:
    """A build failure must not leave a partially-written bundle at out_dir."""
    out_dir = tmp_path / "regras-sisprev"
    bad_csv = tmp_path / "not-a-real.csv"
    bad_csv.write_text("only,one,line\n", encoding="utf-8")

    with pytest.raises(pd.errors.EmptyDataError):
        csv_to_okf(bad_csv, out_dir)

    assert not out_dir.exists()


def _load_frontmatter(doc_path: Path) -> dict:
    text = doc_path.read_text(encoding="utf-8")
    _, fm_text, _ = text.split("---", 2)
    return yaml.safe_load(fm_text)


def _dump_frontmatter(doc_path: Path, frontmatter: dict) -> None:
    text = doc_path.read_text(encoding="utf-8")
    _, _, body = text.split("---", 2)
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    doc_path.write_text(f"---\n{fm_text}---{body}", encoding="utf-8")


def test_load_bundle_rejects_missing_doc(bundle_dir: Path) -> None:
    """A gap in the row_index sequence (a dropped regra doc) must fail loudly."""
    (bundle_dir / "regras" / "regra-0042.md").unlink()

    with pytest.raises(BundleIntegrityError, match="missing row_index"):
        load_bundle(bundle_dir)


def test_load_bundle_rejects_duplicate_row_index(bundle_dir: Path) -> None:
    """Two differently-named files resolving to the same numeric index must fail.

    Filenames are otherwise unique on disk, so the only way two docs collide
    on row_index is inconsistent zero-padding (regra-0042.md vs regra-42.md)
    — a sloppy manual copy is exactly the kind of mistake this should catch.
    """
    regras_dir = bundle_dir / "regras"
    frontmatter = _load_frontmatter(regras_dir / "regra-0042.md")
    frontmatter["id"] = "regra-42"
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body = (regras_dir / "regra-0042.md").read_text(encoding="utf-8").split("---", 2)[2]
    (regras_dir / "regra-42.md").write_text(f"---\n{fm_text}---{body}", encoding="utf-8")

    with pytest.raises(BundleIntegrityError, match="duplicate row_index"):
        load_bundle(bundle_dir)


def test_load_bundle_rejects_id_filename_mismatch(bundle_dir: Path) -> None:
    """A doc whose frontmatter id/row_index disagree with its own filename must fail."""
    doc_10 = bundle_dir / "regras" / "regra-0010.md"
    frontmatter = _load_frontmatter(doc_10)
    frontmatter["id"] = "regra-9999"
    _dump_frontmatter(doc_10, frontmatter)

    with pytest.raises(BundleIntegrityError, match="does not match filename"):
        load_bundle(bundle_dir)


def test_load_bundle_rejects_row_count_mismatch(bundle_dir: Path) -> None:
    """A dataset doc row_count that disagrees with the actual doc count must fail."""
    dataset_doc = bundle_dir / "regras-sisprev.md"
    text = dataset_doc.read_text(encoding="utf-8")
    dataset_doc.write_text(text.replace("row_count: 112", "row_count: 113"), encoding="utf-8")

    with pytest.raises(BundleIntegrityError, match="missing row_index"):
        load_bundle(bundle_dir)


def test_load_bundle_rejects_a_swapped_in_replacement_row(bundle_dir: Path) -> None:
    """The reviewer's exact scenario: one regra dropped, a different one added in its place.

    Deleting regra-0042.md and adding an out-of-sequence "replacement" (with
    a row_index the dataset doc never declared) must not silently keep the
    total document count looking right.
    """
    regras_dir = bundle_dir / "regras"
    (regras_dir / "regra-0042.md").unlink()

    frontmatter = _load_frontmatter(regras_dir / "regra-0041.md")
    frontmatter["id"] = "regra-0200"
    frontmatter["row_index"] = 200
    replacement_text = (regras_dir / "regra-0041.md").read_text(encoding="utf-8")
    _, _, body = replacement_text.split("---", 2)
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    (regras_dir / "regra-0200.md").write_text(f"---\n{fm_text}---{body}", encoding="utf-8")

    with pytest.raises(BundleIntegrityError) as exc_info:
        load_bundle(bundle_dir)

    message = str(exc_info.value)
    assert "missing row_index" in message
    assert "42" in message
    assert "beyond declared row_count" in message
