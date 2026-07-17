"""P10 domain-library tests for detection/achado correspondence."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from achado_schema import build_achado_doc
from bundle import (
    Bundle,
    collect_detections,
    stale_detection_refs,
    uncovered_detections,
    validate_bundle,
)
from csv_to_okf import convert as csv_to_okf
from okf_common import ORIGINAL_CSV

if TYPE_CHECKING:
    from pathlib import Path

    from detections import Detection

_EXPECTED_P2_DETECTIONS = 7


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def _author_achado(
    bundle_dir: Path,
    doc_id: str,
    detection: Detection,
    *,
    situacao: str = "aberto",
    efeito_deteccao: str | None = None,
) -> None:
    regra_ids = sorted(detection.regras)
    frontmatter: dict[str, object] = {
        "type": "Achado",
        "id": doc_id,
        "nome": f"Igualdade material entre {', '.join(regra_ids)}",
        "situacao": situacao,
        "severidade": "informativo",
        "verificacao": "mecanica",
        "natureza": "dados",
        "deteccoes": [
            {"detector": detection.detector, "fingerprint": detection.fingerprint}
        ],
        "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
        "detectado_em": "2026-07-17",
        "detectado_por": "franklinbaldo",
    }
    resolution = ""
    if situacao == "resolvido":
        frontmatter.update(
            {
                "resolvido_em": "2026-07-18",
                "resolvido_por": "franklinbaldo",
                "efeito_deteccao": efeito_deteccao,
            }
        )
        resolution = "Investigação concluída e efeito mecânico registrado."
    sections = {
        "Descrição": "Descrição autoral.",
        "Evidências": "Evidência mecânica.",
        "Questão a investigar": "Questão aberta.",
        "Resolução": resolution,
    }
    (bundle_dir / "achados").mkdir(parents=True, exist_ok=True)
    (bundle_dir / "achados" / f"{doc_id}.md").write_text(
        build_achado_doc(frontmatter, sections),
        encoding="utf-8",
    )


def _detections(bundle_dir: Path) -> list[Detection]:
    return sorted(
        collect_detections(Bundle.load(bundle_dir)),
        key=lambda detection: sorted(detection.regras),
    )


def _author_all(bundle_dir: Path) -> list[Detection]:
    detections = _detections(bundle_dir)
    for index, detection in enumerate(detections, start=1):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)
    return detections


def _inactivate_second_member(bundle_dir: Path, detection: Detection) -> None:
    regra_id = sorted(detection.regras)[1]
    doc = bundle_dir / "regras" / f"{regra_id}.md"
    text = doc.read_text(encoding="utf-8")
    doc.write_text(
        text.replace("---\n", "---\nstatus_regra: inativa\n", 1), encoding="utf-8"
    )


def test_fresh_bundle_detects_the_seven_groups(bundle_dir: Path) -> None:
    assert len(_detections(bundle_dir)) == _EXPECTED_P2_DETECTIONS


def test_fresh_bundle_without_achados_flags_every_detection(bundle_dir: Path) -> None:
    violations = validate_bundle(Bundle.load(bundle_dir))
    assert {violation.code for violation in violations} == {"P14_DETECCAO_SEM_ACHADO"}
    assert len(violations) == _EXPECTED_P2_DETECTIONS


def test_authoring_matching_achados_makes_the_bundle_clean(bundle_dir: Path) -> None:
    _author_all(bundle_dir)
    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_breaking_an_open_documented_group_is_flagged(bundle_dir: Path) -> None:
    detections = _author_all(bundle_dir)
    _inactivate_second_member(bundle_dir, detections[0])

    bundle = Bundle.load(bundle_dir)
    assert len(stale_detection_refs(bundle)) == 1
    assert any(
        violation.code == "P14_ACHADO_SEM_DETECCAO"
        for violation in validate_bundle(bundle)
    )


def test_resolved_pode_persistir_covers_a_current_detection(bundle_dir: Path) -> None:
    detections = _detections(bundle_dir)
    _author_achado(
        bundle_dir,
        "achado-0001",
        detections[0],
        situacao="resolvido",
        efeito_deteccao="pode_persistir",
    )
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)

    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_resolved_deve_desaparecer_fails_while_detection_remains(
    bundle_dir: Path,
) -> None:
    detections = _detections(bundle_dir)
    _author_achado(
        bundle_dir,
        "achado-0001",
        detections[0],
        situacao="resolvido",
        efeito_deteccao="deve_desaparecer",
    )
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)

    codes = {violation.code for violation in validate_bundle(Bundle.load(bundle_dir))}
    assert "P14_DETECCAO_DEVERIA_DESAPARECER" in codes


def test_resolved_deve_desaparecer_passes_after_detection_disappears(
    bundle_dir: Path,
) -> None:
    detections = _detections(bundle_dir)
    _author_achado(
        bundle_dir,
        "achado-0001",
        detections[0],
        situacao="resolvido",
        efeito_deteccao="deve_desaparecer",
    )
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)
    _inactivate_second_member(bundle_dir, detections[0])

    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_two_open_achados_claiming_same_detection_is_flagged(bundle_dir: Path) -> None:
    detections = _author_all(bundle_dir)
    _author_achado(bundle_dir, "achado-0099", detections[0])

    codes = {violation.code for violation in validate_bundle(Bundle.load(bundle_dir))}
    assert "P14_DETECCAO_DUPLICADA" in codes


def test_uncovered_detections_helper_matches_validation(bundle_dir: Path) -> None:
    bundle = Bundle.load(bundle_dir)
    assert len(uncovered_detections(bundle)) == _EXPECTED_P2_DETECTIONS
