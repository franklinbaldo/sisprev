"""P10 domain library: detections + bidirectional validation over fingerprints (RFC 0001)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from achado_schema import build_achado_doc
from bundle import Bundle, collect_detections, stale_detection_refs, uncovered_detections, validate_bundle
from csv_to_okf import convert as csv_to_okf
from okf_common import ORIGINAL_CSV

if TYPE_CHECKING:
    from pathlib import Path

    from detections import Detection

_EXPECTED_P2_DETECTIONS = 7


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """A fresh bundle built from the real source CSV, no achados yet."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def _author_achado(bundle_dir: Path, doc_id: str, detection: Detection) -> None:
    """Write a minimal valid achado covering one detection, by fingerprint."""
    regra_ids = sorted(detection.regras)
    frontmatter = {
        "type": "Achado",
        "id": doc_id,
        "nome": f"Igualdade material entre {', '.join(regra_ids)}",
        "situacao": "aberto",
        "severidade": "informativo",
        "verificacao": "mecanica",
        "natureza": "dados",
        "deteccoes": [{"detector": detection.detector, "fingerprint": detection.fingerprint}],
        "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
        "detectado_em": "2026-07-17",
        "detectado_por": "franklinbaldo",
    }
    sections = {"Descrição": "d", "Evidências": "e", "Questão a investigar": "q", "Resolução": ""}
    (bundle_dir / "achados").mkdir(parents=True, exist_ok=True)
    (bundle_dir / "achados" / f"{doc_id}.md").write_text(
        build_achado_doc(frontmatter, sections),
        encoding="utf-8",
    )


def _author_all(bundle_dir: Path) -> list[Detection]:
    """Author one matching achado per detected group; returns the detections in doc order."""
    detections = sorted(collect_detections(Bundle.load(bundle_dir)), key=lambda d: sorted(d.regras))
    for i, detection in enumerate(detections, start=1):
        _author_achado(bundle_dir, f"achado-{i:04d}", detection)
    return detections


def test_fresh_bundle_detects_the_seven_groups(bundle_dir: Path) -> None:
    """The detector finds exactly the 7 material-equality groups."""
    detections = collect_detections(Bundle.load(bundle_dir))
    assert len(detections) == _EXPECTED_P2_DETECTIONS


def test_fresh_bundle_without_achados_flags_every_detection(bundle_dir: Path) -> None:
    """With no achados authored yet, every detection is a P14_DETECCAO_SEM_ACHADO."""
    violations = validate_bundle(Bundle.load(bundle_dir))
    assert {v.code for v in violations} == {"P14_DETECCAO_SEM_ACHADO"}
    assert len(violations) == _EXPECTED_P2_DETECTIONS


def test_authoring_matching_achados_makes_the_bundle_clean(bundle_dir: Path) -> None:
    """One authored achado per detection (by fingerprint) leaves zero violations."""
    _author_all(bundle_dir)
    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_breaking_a_documented_group_is_flagged(bundle_dir: Path) -> None:
    """P14.6: an achado whose fingerprint the detector no longer emits must fail."""
    _author_all(bundle_dir)

    # Break the regra-0012/regra-0013 group: now that fingerprint isn't emitted.
    regra_doc = bundle_dir / "regras" / "regra-0012.md"
    text = regra_doc.read_text(encoding="utf-8")
    regra_doc.write_text(text.replace("sexo: AMBOS", "sexo: MASCULINO", 1), encoding="utf-8")

    bundle = Bundle.load(bundle_dir)
    assert len(stale_detection_refs(bundle)) == 1
    assert any(v.code == "P14_ACHADO_SEM_DETECCAO" for v in validate_bundle(bundle))


def test_two_achados_claiming_the_same_detection_is_flagged(bundle_dir: Path) -> None:
    """P14.6: two open achados on one detection without an explicit relation is a violation."""
    detections = _author_all(bundle_dir)
    duplicate = min(detections, key=lambda d: sorted(d.regras))
    _author_achado(bundle_dir, "achado-0099", duplicate)

    codes = {v.code for v in validate_bundle(Bundle.load(bundle_dir))}
    assert "P14_DETECCAO_DUPLICADA" in codes


def test_inactivating_a_member_removes_its_detection(bundle_dir: Path) -> None:
    """An inactive member drops the group below two — the detection disappears."""
    doc = bundle_dir / "regras" / "regra-0013.md"
    text = doc.read_text(encoding="utf-8")
    doc.write_text(text.replace("---\n", "---\nstatus_regra: inativa\n", 1), encoding="utf-8")

    detections = collect_detections(Bundle.load(bundle_dir))
    assert not any(d.regras == frozenset({"regra-0012", "regra-0013"}) for d in detections)


def test_uncovered_detections_helper_matches_validation(bundle_dir: Path) -> None:
    """uncovered_detections() is the source of the P14_DETECCAO_SEM_ACHADO count."""
    bundle = Bundle.load(bundle_dir)
    assert len(uncovered_detections(bundle)) == _EXPECTED_P2_DETECTIONS
