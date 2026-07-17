"""P14 schema, lifecycle and current-tree identity tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from achado_schema import (
    Achado,
    build_achado_doc,
    load_achados,
    next_achado_id,
    parse_achado_doc,
    regenerate_achados_index,
    scaffold_achado,
    validate_achado,
    validate_bundle_achados,
)

if TYPE_CHECKING:
    from pathlib import Path

_VALID_FINGERPRINT = "sha256:" + "a" * 64
_VALID_FRONTMATTER: dict[str, object] = {
    "type": "Achado",
    "id": "achado-0001",
    "nome": "Igualdade material entre regra-0001 e regra-0002",
    "situacao": "aberto",
    "severidade": "informativo",
    "verificacao": "mecanica",
    "natureza": "dados",
    "deteccoes": [{"detector": "P2_IGUALDADE_MATERIAL_ATIVA", "fingerprint": _VALID_FINGERPRINT}],
    "regras_afetadas": ["/regras/regra-0001.md", "/regras/regra-0002.md"],
    "detectado_em": "2026-07-17",
    "detectado_por": "franklinbaldo",
}
_SECTIONS = {
    "Descrição": "Descrição.",
    "Evidências": "Evidência.",
    "Questão a investigar": "Questão.",
    "Resolução": "",
}
_KNOWN_REGRA_IDS = frozenset({"regra-0001", "regra-0002", "regra-0003"})
_MINIMAL_DATASET_DOC = "---\ntype: Dataset\nrow_count: 3\ndescription: Catálogo de teste.\n---\n\nCorpo.\n"


def _achado(*, doc_id: str = "achado-0001", drop: tuple[str, ...] = (), **overrides: object) -> Achado:
    frontmatter = {**_VALID_FRONTMATTER, **overrides}
    for key in drop:
        frontmatter.pop(key, None)
    return Achado(doc_id=doc_id, frontmatter=frontmatter, sections=dict(_SECTIONS))


def test_valid_achado_has_no_violations() -> None:
    """Verify a valid authored finding satisfies every schema rule."""
    assert validate_achado(_achado(), known_regra_ids=_KNOWN_REGRA_IDS) == []


def test_build_and_parse_round_trip() -> None:
    """Verify rendering and parsing preserve frontmatter and sections."""
    text = build_achado_doc(dict(_VALID_FRONTMATTER), dict(_SECTIONS))
    frontmatter, sections = parse_achado_doc(text)
    assert frontmatter == _VALID_FRONTMATTER
    assert sections == _SECTIONS


@pytest.mark.parametrize("field_name", ["situacao", "severidade", "verificacao"])
def test_rejects_invalid_enum(field_name: str) -> None:
    """Verify invalid enum values are rejected."""
    achado = Achado(
        doc_id="achado-0001",
        frontmatter={**_VALID_FRONTMATTER, field_name: "invalido"},
        sections=dict(_SECTIONS),
    )
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any(field_name in error for error in errors)


def test_rejects_unknown_frontmatter_field() -> None:
    """Verify unknown frontmatter fields cannot silently pass."""
    errors = validate_achado(_achado(detectador="erro"), known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("detectador" in error for error in errors)


def test_rejects_invalid_fingerprint() -> None:
    """Verify fingerprints use the complete canonical SHA-256 form."""
    errors = validate_achado(
        _achado(deteccoes=[{"detector": "P2", "fingerprint": "sha256:abc"}]),
        known_regra_ids=_KNOWN_REGRA_IDS,
    )
    assert any("fingerprint" in error for error in errors)


def test_manual_forbids_deteccoes() -> None:
    """Verify manual findings cannot claim mechanical detections."""
    errors = validate_achado(_achado(verificacao="manual"), known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("must not have 'deteccoes'" in error for error in errors)


def test_manual_without_deteccoes_is_valid() -> None:
    """Verify a manual finding needs no detector reference."""
    assert (
        validate_achado(
            _achado(verificacao="manual", drop=("deteccoes",)),
            known_regra_ids=_KNOWN_REGRA_IDS,
        )
        == []
    )


def test_open_achado_forbids_resolution_metadata() -> None:
    """Verify open investigations cannot anticipate their resolution effect."""
    errors = validate_achado(
        _achado(efeito_deteccao="pode_persistir"),
        known_regra_ids=_KNOWN_REGRA_IDS,
    )
    assert any("situacao=aberto" in error for error in errors)


@pytest.mark.parametrize("efeito", ["pode_persistir", "deve_desaparecer"])
def test_resolved_mechanical_requires_and_accepts_effect(efeito: str) -> None:
    """Verify resolved mechanical findings declare an explicit effect."""
    achado = _achado(
        situacao="resolvido",
        resolvido_em="2026-07-18",
        resolvido_por="franklinbaldo",
        efeito_deteccao=efeito,
    )
    achado.sections["Resolução"] = "Conclusão documentada."
    assert validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS) == []


def test_resolved_mechanical_without_effect_is_invalid() -> None:
    """Verify a mechanical resolution cannot leave its expected effect implicit."""
    achado = _achado(
        situacao="resolvido",
        resolvido_em="2026-07-18",
        resolvido_por="franklinbaldo",
    )
    achado.sections["Resolução"] = "Conclusão."
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("efeito_deteccao" in error for error in errors)


def test_resolution_date_cannot_precede_detection() -> None:
    """Verify the resolution date does not precede discovery."""
    achado = _achado(
        situacao="resolvido",
        resolvido_em="2026-07-16",
        resolvido_por="franklinbaldo",
        efeito_deteccao="pode_persistir",
    )
    achado.sections["Resolução"] = "Conclusão."
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("earlier" in error for error in errors)


def test_rejects_noncanonical_and_duplicate_regra_references() -> None:
    """Verify rule references are canonical and unique."""
    errors = validate_achado(
        _achado(regras_afetadas=["regra-0001.md", "regra-0001.md"]),
        known_regra_ids=_KNOWN_REGRA_IDS,
    )
    assert any("duplicates" in error for error in errors)
    assert any("non-canonical" in error for error in errors)


@pytest.mark.parametrize("heading", ["Descrição", "Evidências", "Questão a investigar"])
def test_requires_nonempty_authored_sections(heading: str) -> None:
    """Verify every authored investigation section contains content."""
    achado = _achado()
    achado.sections[heading] = " "
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any(heading in error for error in errors)


def test_filename_requires_exactly_four_digits() -> None:
    """Verify finding filenames use exactly four decimal digits."""
    errors = validate_achado(
        _achado(doc_id="achado-1", id="achado-1"),
        known_regra_ids=_KNOWN_REGRA_IDS,
    )
    assert any("achado-NNNN" in error for error in errors)


@pytest.fixture
def empty_bundle(tmp_path: Path) -> Path:
    """Create a minimal empty finding bundle."""
    (tmp_path / "achados").mkdir()
    (tmp_path / "regras-sisprev.md").write_text(_MINIMAL_DATASET_DOC, encoding="utf-8")
    return tmp_path


def _write_achado(bundle_dir: Path, number: int) -> None:
    doc_id = f"achado-{number:04d}"
    frontmatter = {**_VALID_FRONTMATTER, "id": doc_id}
    (bundle_dir / "achados" / f"{doc_id}.md").write_text(
        build_achado_doc(frontmatter, _SECTIONS),
        encoding="utf-8",
    )


def test_next_achado_id_is_max_plus_one(empty_bundle: Path) -> None:
    """Verify allocation advances beyond the current maximum id."""
    _write_achado(empty_bundle, 1)
    assert next_achado_id(empty_bundle) == "achado-0002"


def test_current_tree_rejects_id_gaps(empty_bundle: Path) -> None:
    """Verify the current tree cannot contain missing numeric ids."""
    _write_achado(empty_bundle, 1)
    _write_achado(empty_bundle, 3)
    errors = validate_bundle_achados(empty_bundle, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("missing [2]" in error for error in errors)


def test_regenerate_achados_index_lists_every_achado(empty_bundle: Path) -> None:
    """Verify the derived index lists every authored finding."""
    _write_achado(empty_bundle, 1)
    _write_achado(empty_bundle, 2)
    regenerate_achados_index(empty_bundle)
    index_text = (empty_bundle / "achados" / "index.md").read_text(encoding="utf-8")
    assert "achado-0001.md" in index_text
    assert "achado-0002.md" in index_text


def test_load_achados_returns_empty_for_missing_directory(tmp_path: Path) -> None:
    """Verify a bundle without an achados directory loads no findings."""
    assert load_achados(tmp_path) == []


def test_scaffold_achado_reserves_the_next_id_without_authoring_content(empty_bundle: Path) -> None:
    """scaffold_achado only reserves the id and lists the regras — TODOs stay invalid for the CI."""
    doc_id = scaffold_achado(empty_bundle, ["regra-0001", "regra-0002"])

    assert doc_id == "achado-0001"
    doc_text = (empty_bundle / "achados" / f"{doc_id}.md").read_text(encoding="utf-8")
    frontmatter, _ = parse_achado_doc(doc_text)
    assert frontmatter["severidade"] == "TODO"
    assert frontmatter["regras_afetadas"] == ["/regras/regra-0001.md", "/regras/regra-0002.md"]

    errors = validate_achado(
        Achado(doc_id=doc_id, frontmatter=frontmatter, sections={}),
        known_regra_ids=_KNOWN_REGRA_IDS,
    )
    assert errors  # the TODO scaffold is deliberately invalid until authored by hand


def test_scaffold_achado_never_reuses_an_id(empty_bundle: Path) -> None:
    """Scaffolding twice reserves two distinct, sequential ids."""
    first = scaffold_achado(empty_bundle, ["regra-0001"])
    second = scaffold_achado(empty_bundle, ["regra-0002"])

    assert first == "achado-0001"
    assert second == "achado-0002"
