"""Unit tests for the P2 material-equality detector."""

from __future__ import annotations

from pathlib import Path

from bundle import Bundle, Regra
from detectors.igualdade_material import DETECTOR_ID, VERSION, detect
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS


def _regra(
    regra_id: str,
    *,
    nome: str = "Regra padrão",
    status: str = "ativa",
    frontmatter: dict[str, object] | None = None,
    sections: dict[str, str] | None = None,
) -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[column]: "" for column in FRONTMATTER_COLUMNS}
    fm.update({"type": "Regra", "id": regra_id, "row_index": int(regra_id[-4:]), "nome": nome})
    fm["status_regra"] = status
    if frontmatter:
        fm.update(frontmatter)
    return Regra(id=regra_id, frontmatter=fm, sections=sections or {})


def _bundle(*regras: Regra) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=())


def test_a_different_nome_does_not_distinguish_materially() -> None:
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
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "MASCULINO"}),
    )
    assert detect(bundle) == []


def test_a_future_domain_field_distinguishes_materially_by_default() -> None:
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"grau_deficiencia": "moderada"}),
        _regra("regra-0002", frontmatter={"grau_deficiencia": "leve"}),
    )
    assert detect(bundle) == []


def test_a_future_body_section_distinguishes_materially_by_default() -> None:
    bundle = _bundle(
        _regra("regra-0001", sections={"Como esta regra funciona": "texto A"}),
        _regra("regra-0002", sections={"Como esta regra funciona": "texto B"}),
    )
    assert detect(bundle) == []


def test_administrative_and_audit_fields_do_not_distinguish() -> None:
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
    bundle = _bundle(
        _regra("regra-0001", status="ativa"),
        _regra("regra-0002", status="inativa"),
    )
    assert detect(bundle) == []


def test_two_independent_groups_are_not_merged() -> None:
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
    a = _regra("regra-0001")
    b = _regra("regra-0002")
    assert detect(_bundle(a, b))[0].fingerprint == detect(_bundle(b, a))[0].fingerprint


def test_detector_version_is_bumped_for_extensible_material_semantics() -> None:
    assert VERSION == 2
