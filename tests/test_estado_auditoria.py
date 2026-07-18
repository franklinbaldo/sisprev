"""Unit tests for the P7 state-machine validator — synthetic bundles, no disk."""

from __future__ import annotations

import datetime
from pathlib import Path

from achado_schema import Achado
from bundle import Bundle, Regra
from detections import Detection
from estado_auditoria import _SECOES_P13_1_OBRIGATORIAS, check_p7_estados
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS

_VALID_ATO = {
    "tipo": "parecer",
    "autoridade": "PGE",
    "identificador": "SEI 123",
    "fonte": "SEI",
}
_TODAY = datetime.date(2026, 7, 17)
_SECOES_COMPLETAS = dict.fromkeys(_SECOES_P13_1_OBRIGATORIAS, "Resposta de teste.")

# Frontmatter keys _regra() treats as "unset by default, drop if None" —
# distinguishes a caller explicitly passing None from never mentioning the
# field, matching how the real Regra.status_auditoria/atos_validacao
# properties distinguish an absent key from a present-but-empty one.
_OPTIONAL_FRONTMATTER_KEYS = ("atos_validacao", "auditado_por", "auditado_em")


def _regra(regra_id: str, *, sections: dict[str, str] | None = None, **frontmatter: object) -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = f"Regra {regra_id}"
    fm["status_auditoria"] = frontmatter.pop("status_auditoria", "importada")
    for key in _OPTIONAL_FRONTMATTER_KEYS:
        value = frontmatter.pop(key, None)
        if value is not None:
            fm[key] = value
    return Regra(id=regra_id, frontmatter=fm, sections=sections or {})


def _regra_revisada(regra_id: str, *, sections: dict[str, str] | None = None, **overrides: object) -> Regra:
    """A regra with a complete, valid audit trail — the baseline "clean revisada" fixture."""
    defaults: dict[str, object] = {
        "status_auditoria": "revisada",
        "auditado_por": "franklinbaldo",
        "auditado_em": "2026-07-16",
    }
    defaults.update(overrides)
    return _regra(
        regra_id, sections=sections if sections is not None else dict(_SECOES_COMPLETAS), **defaults
    )


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


def _regra_validada(regra_id: str, *, sections: dict[str, str] | None = None, **overrides: object) -> Regra:
    """A regra with a complete, valid audit trail and a well-formed ato — the "clean validada" fixture."""
    defaults: dict[str, object] = {
        "status_auditoria": "validada",
        "atos_validacao": [_VALID_ATO],
        "auditado_por": "franklinbaldo",
        "auditado_em": "2026-07-16",
    }
    defaults.update(overrides)
    return _regra(
        regra_id, sections=sections if sections is not None else dict(_SECOES_COMPLETAS), **defaults
    )


def _bundle(regras: list[Regra], achados: list[Achado] | None = None) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=tuple(achados or []))


def test_importada_has_no_invariants_to_violate() -> None:
    """A regra still importada is never flagged, regardless of achados/detections."""
    regra = _regra("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


# --- P8: status_auditoria is a closed enum ---


def test_unknown_status_auditoria_value_is_rejected() -> None:
    """A typo like "revisad" must not silently behave like "revisada"."""
    regra = _regra("regra-0001", status_auditoria="revisad")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "vocabulário fechado" in violations[0].message


def test_arbitrary_string_status_auditoria_is_rejected() -> None:
    """Any value outside ESTADOS is rejected, not just near-misses of real values."""
    regra = _regra("regra-0001", status_auditoria="foo")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert violations[0].code == "P7_ESTADO_INVALIDO"


# --- revisada: joins with achados/detectors ---


def test_revisada_with_no_blockers_is_valid() -> None:
    """A revisada regra with a complete trail and nothing referencing it is clean."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_revisada_flagged_by_open_bloqueante_achado() -> None:
    """A revisada regra referenced by an open bloqueante achado is invalid."""
    regra = _regra_revisada("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert violations[0].code == "P7_ESTADO_INVALIDO"
    assert "bloqueante aberto" in violations[0].message


def test_revisada_ignores_open_informativo_achado() -> None:
    """An informativo (non-bloqueante) achado never invalidates revisada."""
    regra = _regra_revisada("regra-0001")
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
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_revisada_flagged_by_active_p2_detection() -> None:
    """A revisada regra still part of a P2 material-equality group is invalid."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    detections = [_detection("P2_IGUALDADE_MATERIAL_ATIVA", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections, today=_TODAY)
    assert len(violations) == 1
    assert "P2_IGUALDADE_MATERIAL_ATIVA" in violations[0].message


def test_revisada_flagged_by_active_p1_detection() -> None:
    """A revisada regra still sharing a normalized nome is invalid (P1: unicidade como meta)."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    detections = [_detection("P1_NOME_REPETIDO", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections, today=_TODAY)
    assert len(violations) == 1
    assert "P1_NOME_REPETIDO" in violations[0].message


# --- P11: revisada/validada require a real auditor and date ---


def test_revisada_requires_auditado_por() -> None:
    """A revisada regra without an author leaves no audit trail."""
    regra = _regra_revisada("regra-0001", auditado_por=None)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "auditado_por" in violations[0].message


def test_revisada_requires_auditado_em() -> None:
    """A revisada regra without a date leaves no audit trail."""
    regra = _regra_revisada("regra-0001", auditado_em=None)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "auditado_em" in violations[0].message


def test_revisada_rejects_a_non_iso_auditado_em() -> None:
    """A malformed date string is not silently accepted."""
    regra = _regra_revisada("regra-0001", auditado_em="17/07/2026")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "não é uma data ISO válida" in violations[0].message


def test_revisada_rejects_a_future_auditado_em() -> None:
    """A revisão cannot be dated after today — that would predate the event."""
    regra = _regra_revisada("regra-0001", auditado_em="2026-07-18")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "está no futuro" in violations[0].message


def test_revisada_accepts_auditado_em_equal_to_today() -> None:
    """Today itself is a valid, non-future date."""
    regra = _regra_revisada("regra-0001", auditado_em="2026-07-17")
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


# --- P13.1: revisada requires the four boundary-of-automation sections ---


def test_revisada_with_no_sections_at_all_is_invalid() -> None:
    """auditado_por/auditado_em alone are not enough — the exact gap the review flagged."""
    regra = _regra_revisada("regra-0001", sections={})
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    for heading in _SECOES_P13_1_OBRIGATORIAS:
        assert heading in violations[0].message


def test_revisada_with_a_blank_section_is_invalid() -> None:
    """A present-but-whitespace-only section doesn't count as an answer."""
    sections = dict(_SECOES_COMPLETAS)
    sections["Resultado após a seleção"] = "   "
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "Resultado após a seleção" in violations[0].message


def test_revisada_with_one_missing_section_reports_only_that_one() -> None:
    """Three filled + one missing: the violation names only the missing section."""
    sections = dict(_SECOES_COMPLETAS)
    del sections["Documentos ou evidências necessários"]
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "Documentos ou evidências necessários" in violations[0].message
    assert "Critérios avaliados pelo Sisprev" not in violations[0].message


def test_validada_also_requires_the_p13_1_sections() -> None:
    """Validada inherits the section requirement from revisada, like every other P11/P13.1 check."""
    regra = _regra_validada("regra-0001", sections={})
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "Critérios avaliados pelo Sisprev" in violations[0].message


# --- validada: atos_validacao ---


def test_validada_requires_atos_validacao() -> None:
    """Validada without any atos_validacao is invalid."""
    regra = _regra_validada("regra-0001", atos_validacao=[])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "atos_validacao" in violations[0].message


def test_validada_with_a_complete_ato_is_valid() -> None:
    """Validada with one well-formed ato, a complete trail and no other blockers is clean."""
    bundle = _bundle([_regra_validada("regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_validada_rejects_ato_missing_required_fields() -> None:
    """Each ato de validação must declare tipo/autoridade/identificador/fonte."""
    incomplete_ato = {"tipo": "parecer", "autoridade": "PGE"}
    regra = _regra_validada("regra-0001", atos_validacao=[incomplete_ato])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "identificador" in violations[0].message
    assert "fonte" in violations[0].message


def test_validada_rejects_a_non_list_atos_validacao() -> None:
    """A malformed atos_validacao (wrong type entirely) is a violation, not a silent empty list."""
    regra = _regra_validada("regra-0001", atos_validacao="texto-malformado")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "deve ser uma lista" in violations[0].message


def test_validada_rejects_a_non_mapping_item_without_dropping_it_silently() -> None:
    """A mixed list (one valid ato + one malformed string) must surface the malformed item.

    This is the exact scenario the review flagged: a property that
    pre-filters to "only the dict items" would let this list quietly become
    [valid_ato] and pass — the malformed entry must be reported instead.
    """
    regra = _regra_validada("regra-0001", atos_validacao=[_VALID_ATO, "texto-malformado"])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "não é um mapeamento" in violations[0].message
    assert "texto-malformado" in violations[0].message


def test_validada_also_inherits_revisada_invariants() -> None:
    """Validada is not exempt from the revisada checks (open bloqueante achado still counts)."""
    regra = _regra_validada("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "bloqueante aberto" in violations[0].message
