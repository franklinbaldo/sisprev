"""Unit tests for the P2 material-equality detector."""

from __future__ import annotations

from bundle import Bundle, Regra
from concept import build_body
from detectors.igualdade_material import DETECTOR_ID, VERSION, detect
from regra_schema import blank_frontmatter

_EXPECTED_DETECTOR_VERSION = 4


def _regra(
    regra_id: str,
    *,
    nome: str = "Regra padrão",
    status: str = "ativa",
    frontmatter: dict[str, object] | None = None,
    sections: dict[str, str] | None = None,
) -> Regra:
    fm = blank_frontmatter()
    fm.update({"type": "Regra", "id": regra_id, "row_index": int(regra_id[-4:]), "nome": nome})
    fm["status_regra"] = status
    if frontmatter:
        fm.update(frontmatter)
    return Regra(doc_id=regra_id, frontmatter=fm, body=build_body(sections or {}))


def _bundle(*regras: Regra) -> Bundle:
    return Bundle(regras=tuple(regras))


def test_a_different_nome_does_not_distinguish_materially() -> None:
    """Verify changing only the name does not split a material group."""
    detections = detect(
        _bundle(
            _regra("regra-0001", nome="Regra A"),
            _regra("regra-0002", nome="Regra B"),
        )
    )
    assert len(detections) == 1
    assert detections[0].regras == frozenset({"regra-0001", "regra-0002"})
    assert detections[0].detector == DETECTOR_ID


def test_a_legacy_domain_field_distinguishes_materially() -> None:
    """Verify a differing legacy domain field splits the group."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "MASCULINO"}),
    )
    assert detect(bundle) == []


def test_a_future_domain_field_distinguishes_materially_by_default() -> None:
    """Verify future domain fields participate without detector edits."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"grau_deficiencia": "moderada"}),
        _regra("regra-0002", frontmatter={"grau_deficiencia": "leve"}),
    )
    assert detect(bundle) == []


def test_body_analysis_does_not_distinguish_materially() -> None:
    """The body is the auditor's analysis, not rule data — it is not material.

    Two rules with identical deployable frontmatter but different body
    (analysis) text are still materially equal (P13.2 refactor 2026-07).
    """
    bundle = _bundle(
        _regra("regra-0001", sections={"Análise": "texto A"}),
        _regra("regra-0002", sections={"Análise": "texto B"}),
    )
    detections = detect(bundle)
    assert len(detections) == 1


def test_a_future_frontmatter_field_distinguishes_materially_by_default() -> None:
    """Verify future authored frontmatter fields participate by default."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"campo_futuro": "valor A"}),
        _regra("regra-0002", frontmatter={"campo_futuro": "valor B"}),
    )
    assert detect(bundle) == []


def test_administrative_and_audit_fields_do_not_distinguish() -> None:
    """Verify administrative and audit metadata remain excluded."""
    bundle = _bundle(
        _regra(
            "regra-0001",
            frontmatter={"status_auditoria": "importada", "auditado_por": "alice"},
        ),
        _regra(
            "regra-0002",
            frontmatter={"status_auditoria": "revisada", "auditado_por": "bob"},
        ),
    )
    detections = detect(bundle)
    assert len(detections) == 1


def test_inactive_regras_do_not_participate() -> None:
    """Verify inactive rules are excluded from operational equality groups."""
    bundle = _bundle(
        _regra("regra-0001", status="ativa"),
        _regra("regra-0002", status="inativa"),
    )
    assert detect(bundle) == []


def test_two_independent_groups_are_not_merged() -> None:
    """Verify distinct material signatures produce separate groups."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0003", frontmatter={"sexo": "MASCULINO"}),
        _regra("regra-0004", frontmatter={"sexo": "MASCULINO"}),
    )
    groups = {detection.regras for detection in detect(bundle)}
    assert groups == {
        frozenset({"regra-0001", "regra-0002"}),
        frozenset({"regra-0003", "regra-0004"}),
    }


def test_fingerprint_is_stable_regardless_of_read_order() -> None:
    """Verify read order does not alter the detection fingerprint."""
    a = _regra("regra-0001")
    b = _regra("regra-0002")
    assert detect(_bundle(a, b))[0].fingerprint == detect(_bundle(b, a))[0].fingerprint


def test_detector_version_is_bumped_for_extensible_material_semantics() -> None:
    """Verify the semantic change deliberately invalidates old fingerprints."""
    assert VERSION == _EXPECTED_DETECTOR_VERSION


def test_fingerprint_changes_when_the_shared_material_content_changes() -> None:
    """Same group membership (ids), different shared value: fingerprint must not be reused.

    If a group's two members keep the same ids but their common material
    content drifts to a different shared value, an achado documenting the
    old content must not look "still reproduced" by the new fingerprint.
    """
    bundle_a = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "FEMININO"}),
    )
    bundle_b = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "MASCULINO"}),
        _regra("regra-0002", frontmatter={"sexo": "MASCULINO"}),
    )
    fp_a = detect(bundle_a)[0].fingerprint
    fp_b = detect(bundle_b)[0].fingerprint
    assert fp_a != fp_b
