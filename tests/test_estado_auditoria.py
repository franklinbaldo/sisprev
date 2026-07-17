"""Unit tests for the P7 state-machine validator — synthetic bundles, no disk."""

from __future__ import annotations

from pathlib import Path

from achado_schema import Achado
from bundle import Bundle, Regra
from detections import Detection
from estado_auditoria import check_p7_estados
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS

_VALID_ATO = {
    "tipo": "parecer",
    "autoridade": "PGE",
    "identificador": "SEI 123",
    "fonte": "SEI",
}


def _regra(
    regra_id: str, *, status_auditoria: str = "importada", atos_validacao: list | None = None
) -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = f"Regra {regra_id}"
    fm["status_auditoria"] = status_auditoria
    if atos_validacao is not None:
        fm["atos_validacao"] = atos_validacao
    return Regra(id=regra_id, frontmatter=fm, sections={})


def _bloqueante_achado(doc_id: str, regra_id: str) -> Achado:
    return Achado(
        doc_id=doc_id,
        frontmatter={
            "situacao": "aberto",
            "severidade": "bloqueante",
            "regras_afetadas": [f"/regras/{regra_id}.md"],
        },
        sections={},
    )


def _detection(detector: str, *regra_ids: str) -> Detection:
    return Detection(detector=detector, fingerprint=f"sha256:{'a' * 64}", regras=frozenset(regra_ids))


def _bundle(regras: list[Regra], achados: list[Achado] | None = None) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=tuple(achados or []))


def test_importada_has_no_invariants_to_violate() -> None:
    """A regra still importada is never flagged, regardless of achados/detections."""
    regra = _regra("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    assert check_p7_estados(bundle, []) == []


def test_revisada_with_no_blockers_is_valid() -> None:
    """A revisada regra with nothing referencing it is clean."""
    regra = _regra("regra-0001", status_auditoria="revisada")
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, []) == []


def test_revisada_flagged_by_open_bloqueante_achado() -> None:
    """A revisada regra referenced by an open bloqueante achado is invalid."""
    regra = _regra("regra-0001", status_auditoria="revisada")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [])
    assert len(violations) == 1
    assert violations[0].code == "P7_ESTADO_INVALIDO"
    assert "bloqueante aberto" in violations[0].message


def test_revisada_ignores_open_informativo_achado() -> None:
    """An informativo (non-bloqueante) achado never invalidates revisada."""
    regra = _regra("regra-0001", status_auditoria="revisada")
    achado = Achado(
        doc_id="achado-0001",
        frontmatter={
            "situacao": "aberto",
            "severidade": "informativo",
            "regras_afetadas": ["/regras/regra-0001.md"],
        },
        sections={},
    )
    bundle = _bundle([regra], [achado])
    assert check_p7_estados(bundle, []) == []


def test_revisada_flagged_by_active_p2_detection() -> None:
    """A revisada regra still part of a P2 material-equality group is invalid."""
    regra = _regra("regra-0001", status_auditoria="revisada")
    bundle = _bundle([regra])
    detections = [_detection("P2_IGUALDADE_MATERIAL_ATIVA", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections)
    assert len(violations) == 1
    assert "P2_IGUALDADE_MATERIAL_ATIVA" in violations[0].message


def test_revisada_flagged_by_active_p1_detection() -> None:
    """A revisada regra still sharing a normalized nome is invalid (P1: unicidade como meta)."""
    regra = _regra("regra-0001", status_auditoria="revisada")
    bundle = _bundle([regra])
    detections = [_detection("P1_NOME_REPETIDO", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections)
    assert len(violations) == 1
    assert "P1_NOME_REPETIDO" in violations[0].message


def test_validada_requires_atos_validacao() -> None:
    """Validada without any atos_validacao is invalid."""
    regra = _regra("regra-0001", status_auditoria="validada")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [])
    assert len(violations) == 1
    assert "atos_validacao" in violations[0].message


def test_validada_with_a_complete_ato_is_valid() -> None:
    """Validada with one well-formed ato and no other blockers is clean."""
    regra = _regra("regra-0001", status_auditoria="validada", atos_validacao=[_VALID_ATO])
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, []) == []


def test_validada_rejects_ato_missing_required_fields() -> None:
    """Each ato de validação must declare tipo/autoridade/identificador/fonte."""
    incomplete_ato = {"tipo": "parecer", "autoridade": "PGE"}
    regra = _regra("regra-0001", status_auditoria="validada", atos_validacao=[incomplete_ato])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [])
    assert len(violations) == 1
    assert "identificador" in violations[0].message
    assert "fonte" in violations[0].message


def test_validada_also_inherits_revisada_invariants() -> None:
    """Validada is not exempt from the revisada checks (open bloqueante achado still counts)."""
    regra = _regra("regra-0001", status_auditoria="validada", atos_validacao=[_VALID_ATO])
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [])
    assert len(violations) == 1
    assert "bloqueante aberto" in violations[0].message
