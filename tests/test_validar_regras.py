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
    """Build a fresh bundle from the frozen source CSV."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def _author_achado(
    bundle_dir: Path,
    doc_id: str,
    detection: Detection,
    *,
    situacao: str = "aberto",
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
        "deteccoes": [{"detector": detection.detector, "fingerprint": detection.fingerprint}],
        "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
        "detectado_em": "2026-07-17",
        "detectado_por": "franklinbaldo",
    }
    resolution = ""
    if situacao == "improcedente":
        frontmatter.update(
            {
                "improcedente_em": "2026-07-18",
                "improcedente_por": "franklinbaldo",
            }
        )
        resolution = "A acusação não procede: o defeito descrito não existe."
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
    """The camada-2 (requires_achado) detections — camada-3 heuristics never need authoring."""
    return sorted(
        (d for d in collect_detections(Bundle.load(bundle_dir)) if d.requires_achado),
        key=lambda detection: sorted(detection.regras),
    )


def _author_all(bundle_dir: Path) -> list[Detection]:
    """Author one achado per camada-2 detection (the ones that require it); returns them."""
    detections = _detections(bundle_dir)
    for index, detection in enumerate(detections, start=1):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)
    return detections


def _dispor_corrigida(bundle_dir: Path, doc_id: str, detection: Detection) -> None:
    """Faz cada regra alcançada responder ``corrigida`` ao achado.

    É o que substituiu ``efeito_deteccao`` no achado: a expectativa de que a
    detecção desapareça passa a ser **derivada** das respostas da população,
    e não declarada por um campo que ninguém era obrigado a sustentar.
    """
    entrada = (
        "disposicao_de_achados:\n"
        f"  - achado: /achados/{doc_id}.md\n"
        "    disposicao: corrigida\n"
        "    justificativa: Campo corrigido na regra.\n"
        "    decidido_por: franklinbaldo\n"
        "    decidido_em: 2026-07-18\n"
    )
    for regra_id in sorted(detection.regras):
        doc = bundle_dir / "regras" / f"{regra_id}.md"
        text = doc.read_text(encoding="utf-8")
        doc.write_text(text.replace("---\n", "---\n" + entrada, 1), encoding="utf-8")


def _inactivate_second_member(bundle_dir: Path, detection: Detection) -> None:
    regra_id = sorted(detection.regras)[1]
    doc = bundle_dir / "regras" / f"{regra_id}.md"
    text = doc.read_text(encoding="utf-8")
    doc.write_text(text.replace("---\n", "---\nstatus_regra: inativa\n", 1), encoding="utf-8")


def test_fresh_bundle_detects_the_seven_p2_groups(bundle_dir: Path) -> None:
    """The P2 detector finds exactly the 7 material-equality groups."""
    assert len(_detections(bundle_dir)) == _EXPECTED_P2_DETECTIONS


def test_fresh_bundle_without_achados_flags_every_detection(bundle_dir: Path) -> None:
    """Verify every unregistered detection is reported."""
    violations = validate_bundle(Bundle.load(bundle_dir))
    assert {violation.code for violation in violations} == {"P14_DETECCAO_SEM_ACHADO"}
    assert len(violations) == _EXPECTED_P2_DETECTIONS


def test_authoring_matching_achados_makes_the_bundle_clean(bundle_dir: Path) -> None:
    """Verify authored findings cover all current detections."""
    _author_all(bundle_dir)
    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_breaking_an_open_documented_group_is_flagged(bundle_dir: Path) -> None:
    """Verify an open finding becomes stale when its detection disappears."""
    detections = _author_all(bundle_dir)
    _inactivate_second_member(bundle_dir, detections[0])

    bundle = Bundle.load(bundle_dir)
    assert len(stale_detection_refs(bundle)) == 1
    assert any(violation.code == "P14_ACHADO_SEM_DETECCAO" for violation in validate_bundle(bundle))


def test_improcedente_covers_a_current_detection(bundle_dir: Path) -> None:
    """A acusação que não procedia deixa a detecção de pé, e isso é cobertura."""
    detections = _detections(bundle_dir)
    _author_achado(bundle_dir, "achado-0001", detections[0], situacao="improcedente")
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)

    assert validate_bundle(Bundle.load(bundle_dir)) == []


def test_populacao_toda_corrigida_falha_enquanto_a_deteccao_reproduz(
    bundle_dir: Path,
) -> None:
    """Se toda regra alcançada diz ter corrigido, a ocorrência não devia reproduzir."""
    detections = _detections(bundle_dir)
    _author_achado(bundle_dir, "achado-0001", detections[0])
    _dispor_corrigida(bundle_dir, "achado-0001", detections[0])
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)

    codes = {violation.code for violation in validate_bundle(Bundle.load(bundle_dir))}
    assert "P14_DETECCAO_DEVERIA_DESAPARECER" in codes


def test_populacao_toda_corrigida_passa_quando_a_deteccao_some(
    bundle_dir: Path,
) -> None:
    """E o achado segue **aberto**: quem registra o tratamento é a disposição.

    Este é o par que a remoção do estado `resolvido` tornou necessário. Antes,
    corrigir o defeito derrubava o gate por detecção sumida e obrigava a fechar
    o achado com um selo próprio; agora a disposição da população é o que
    autoriza o desaparecimento, e o achado não precisa mentir sobre si.
    """
    detections = _detections(bundle_dir)
    _author_achado(bundle_dir, "achado-0001", detections[0])
    _dispor_corrigida(bundle_dir, "achado-0001", detections[0])
    for index, detection in enumerate(detections[1:], start=2):
        _author_achado(bundle_dir, f"achado-{index:04d}", detection)
    _inactivate_second_member(bundle_dir, detections[0])

    bundle = Bundle.load(bundle_dir)
    assert validate_bundle(bundle) == []
    assert [a.doc_id for a in bundle.achados_integralmente_corrigidos()] == ["achado-0001"]


def test_two_open_achados_claiming_same_detection_is_flagged(bundle_dir: Path) -> None:
    """Verify one current detection cannot silently belong to two open investigations."""
    detections = _author_all(bundle_dir)
    _author_achado(bundle_dir, "achado-0099", detections[0])

    codes = {violation.code for violation in validate_bundle(Bundle.load(bundle_dir))}
    assert "P14_DETECCAO_DUPLICADA" in codes


def test_uncovered_detections_helper_matches_validation(bundle_dir: Path) -> None:
    """uncovered_detections() counts only camada-2 (requires_achado) detections."""
    bundle = Bundle.load(bundle_dir)
    assert len(uncovered_detections(bundle)) == _EXPECTED_P2_DETECTIONS


def test_camada_3_detections_never_block(bundle_dir: Path) -> None:
    """P1/P9 heuristics are reported but never force an achado (RFC "semântica adiada")."""
    bundle = Bundle.load(bundle_dir)
    camada_3 = [d for d in collect_detections(bundle) if not d.requires_achado]
    assert camada_3  # they exist (nome repetido, co-ocorrências)
    # None of them appears in the blocking set, even with zero achados authored.
    assert all(d.requires_achado is False for d in camada_3)
    assert not any(d in uncovered_detections(bundle) for d in camada_3)
