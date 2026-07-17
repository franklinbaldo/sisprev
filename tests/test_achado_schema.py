"""P14 invariants for the Achado concept (schema, ciclo de vida, doc I/O)."""

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
    validate_achado,
    validate_bundle_achados,
)

if TYPE_CHECKING:
    from pathlib import Path

_VALID_FRONTMATTER = {
    "type": "Achado",
    "id": "achado-0001",
    "nome": "Igualdade material entre regra-0001, regra-0002",
    "situacao": "aberto",
    "severidade": "bloqueante",
    "verificacao": "mecanica",
    "detector": "P2_IGUALDADE_MATERIAL_ATIVA",
    "natureza": "dados",
    "regras_afetadas": ["/regras/regra-0001.md", "/regras/regra-0002.md"],
    "detectado_em": "2026-07-17",
    "detectado_por": "scripts/validar_regras.py",
}
_SECTIONS = {"Descrição": "x", "Evidências": "y", "Questão a investigar": "z", "Resolução": ""}
_KNOWN_REGRA_IDS = frozenset({"regra-0001", "regra-0002", "regra-0003"})
_MINIMAL_DATASET_DOC = "---\ntype: Dataset\nrow_count: 3\ndescription: Catálogo de teste.\n---\n\nCorpo.\n"


def _achado(**overrides: object) -> Achado:
    frontmatter = {**_VALID_FRONTMATTER, **overrides}
    return Achado(doc_id="achado-0001", frontmatter=frontmatter, sections=dict(_SECTIONS))


def test_valid_achado_has_no_violations() -> None:
    """A frontmatter matching every P14.6 rule produces zero violations."""
    assert validate_achado(_achado(), known_regra_ids=_KNOWN_REGRA_IDS) == []


def test_build_and_parse_round_trip() -> None:
    """build_achado_doc -> parse_achado_doc must reproduce the same data."""
    text = build_achado_doc(dict(_VALID_FRONTMATTER), dict(_SECTIONS))
    frontmatter, sections = parse_achado_doc(text)

    assert frontmatter == _VALID_FRONTMATTER
    for heading, content in _SECTIONS.items():
        assert sections[heading] == content


@pytest.mark.parametrize("field_name", ["situacao", "severidade", "verificacao"])
def test_rejects_invalid_enum(field_name: str) -> None:
    """situacao/severidade/verificacao must be one of their closed enum values."""
    achado = _achado(**{field_name: "not-a-real-value"})
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any(field_name in e for e in errors)


def test_mecanica_requires_detector() -> None:
    """P14.6: verificacao=mecanica without a detector is invalid."""
    achado = _achado(verificacao="mecanica", detector=None)
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("requires 'detector'" in e for e in errors)


def test_manual_forbids_detector() -> None:
    """P14.6: verificacao=manual must never carry a detector code."""
    achado = _achado(verificacao="manual", detector="SOME_CODE")
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("must not have 'detector'" in e for e in errors)


def test_hibrida_requires_detector_but_detector_is_not_proof_of_merit() -> None:
    """P14.5: híbrido needs a detector for the mechanical condition, and that's all it proves."""
    achado = _achado(verificacao="hibrida", detector="P9_SEXO_FUNDAMENTACAO")
    assert validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS) == []


def test_rejects_empty_regras_afetadas() -> None:
    """P14.4: regras_afetadas is the only source of the achado<->regra relation — must not be empty."""
    achado = _achado(regras_afetadas=[])
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("regras_afetadas must not be empty" in e for e in errors)


def test_rejects_reference_to_unknown_regra() -> None:
    """Every regras_afetadas entry must resolve to a real regra doc."""
    achado = _achado(regras_afetadas=["/regras/regra-9999.md"])
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("unknown regra" in e for e in errors)


def test_resolved_requires_resolution_metadata() -> None:
    """P14.3: situacao=resolvido requires resolvido_em and resolvido_por."""
    achado = _achado(situacao="resolvido", resolvido_em=None, resolvido_por=None)
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("resolvido_em" in e for e in errors)
    assert any("resolvido_por" in e for e in errors)


def test_resolved_requires_nonempty_resolucao_section() -> None:
    """P14.3: situacao=resolvido requires a non-empty # Resolução body section."""
    achado = Achado(
        doc_id="achado-0001",
        frontmatter={
            **_VALID_FRONTMATTER,
            "situacao": "resolvido",
            "resolvido_em": "2026-07-18",
            "resolvido_por": "x",
        },
        sections={**_SECTIONS, "Resolução": "   "},
    )
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("Resolução" in e for e in errors)


def test_filename_id_mismatch_is_a_violation() -> None:
    """The frontmatter id must match the doc's own filename, like a regra's."""
    achado = Achado(doc_id="achado-0002", frontmatter=dict(_VALID_FRONTMATTER), sections=dict(_SECTIONS))
    errors = validate_achado(achado, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("does not match filename" in e for e in errors)


@pytest.fixture
def empty_bundle(tmp_path: Path) -> Path:
    """A minimal bundle dir: an achados/ folder plus the dataset doc regenerate_root_index needs."""
    (tmp_path / "achados").mkdir()
    (tmp_path / "regras-sisprev.md").write_text(_MINIMAL_DATASET_DOC, encoding="utf-8")
    return tmp_path


def test_next_achado_id_starts_at_0001(empty_bundle: Path) -> None:
    """The first achado in a fresh bundle is achado-0001."""
    assert next_achado_id(empty_bundle) == "achado-0001"


def test_next_achado_id_is_sequential_and_never_reused(empty_bundle: Path) -> None:
    """P14.3: ids increment; a resolved (or any existing) achado's number is never reissued."""
    doc = build_achado_doc({**_VALID_FRONTMATTER, "id": "achado-0001"}, _SECTIONS)
    (empty_bundle / "achados" / "achado-0001.md").write_text(doc, encoding="utf-8")

    assert next_achado_id(empty_bundle) == "achado-0002"


def test_regenerate_achados_index_lists_every_achado(empty_bundle: Path) -> None:
    """achados/index.md (P14.7) is generated, listing every achado doc present."""
    for i in (1, 2):
        frontmatter = {**_VALID_FRONTMATTER, "id": f"achado-{i:04d}"}
        doc = build_achado_doc(frontmatter, _SECTIONS)
        (empty_bundle / "achados" / f"achado-{i:04d}.md").write_text(doc, encoding="utf-8")

    regenerate_achados_index(empty_bundle)

    index_text = (empty_bundle / "achados" / "index.md").read_text(encoding="utf-8")
    assert "achado-0001.md" in index_text
    assert "achado-0002.md" in index_text


def test_regenerate_achados_index_also_refreshes_root_index(empty_bundle: Path) -> None:
    """P14.1: the bundle-root index.md gets an achados/ line reflecting the current count."""
    doc = build_achado_doc({**_VALID_FRONTMATTER, "id": "achado-0001"}, _SECTIONS)
    (empty_bundle / "achados" / "achado-0001.md").write_text(doc, encoding="utf-8")

    regenerate_achados_index(empty_bundle)

    root_index = (empty_bundle / "index.md").read_text(encoding="utf-8")
    assert "achados/" in root_index
    assert "1 achado" in root_index


def test_load_achados_returns_empty_for_missing_directory(tmp_path: Path) -> None:
    """A bundle with no achados/ directory yet has zero achados, not an error."""
    assert load_achados(tmp_path) == []


def test_validate_bundle_achados_detects_duplicate_numbers(empty_bundle: Path) -> None:
    """Same numeric id via inconsistent naming (achado-0001 vs achado-1) must fail — mirrors regra's check."""
    doc1 = build_achado_doc({**_VALID_FRONTMATTER, "id": "achado-0001"}, _SECTIONS)
    (empty_bundle / "achados" / "achado-0001.md").write_text(doc1, encoding="utf-8")
    doc2 = build_achado_doc({**_VALID_FRONTMATTER, "id": "achado-1"}, _SECTIONS)
    (empty_bundle / "achados" / "achado-1.md").write_text(doc2, encoding="utf-8")

    errors = validate_bundle_achados(empty_bundle, known_regra_ids=_KNOWN_REGRA_IDS)
    assert any("duplicate achado number" in e for e in errors)
