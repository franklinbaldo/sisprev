"""RFC 0004 §1/§3/§14 — audited-unit identity, provenance and structural validation."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bundle import Bundle, Regra
from pydantic import ValidationError
from regra_schema import blank_frontmatter
from unidade_auditada_schema import (
    ProtocoloVerificacao,
    Proveniencia,
    UnidadeAuditada,
    load_unidades_auditadas,
    validate_bundle_auditado,
)

if TYPE_CHECKING:
    from pathlib import Path


def _legacy_bundle(*regra_ids: str) -> Bundle:
    return Bundle(regras=tuple(Regra(doc_id=rid, frontmatter=blank_frontmatter()) for rid in regra_ids))


def _unidade(
    doc_id: str, *, origens_legacy: list[str], estado_unidade: str = "elaboracao", **extra: object
) -> UnidadeAuditada:
    frontmatter: dict[str, object] = {
        "type": "UnidadeAuditada",
        "id": doc_id,
        "schema_version": 1,
        "estado_unidade": estado_unidade,
        "origens_legacy": origens_legacy,
        **extra,
    }
    return UnidadeAuditada(doc_id=doc_id, frontmatter=frontmatter)


def test_empty_bundle_dir_loads_as_no_units(tmp_path: Path) -> None:
    """The loader must accept an audited bundle with no `unidades/` directory at all."""
    assert load_unidades_auditadas(tmp_path) == []


def test_bundle_with_empty_unidades_dir_loads_as_no_units(tmp_path: Path) -> None:
    """An audited bundle with an empty `unidades/` directory loads as no units."""
    (tmp_path / "unidades").mkdir()
    assert load_unidades_auditadas(tmp_path) == []


def test_duplicate_id_is_flagged() -> None:
    """Two audited units sharing the same id are flagged."""
    unidades = [
        _unidade("invalidez-a", origens_legacy=["regra-0022"]),
        _unidade("invalidez-a", origens_legacy=["regra-0022"]),
    ]
    violations = validate_bundle_auditado(unidades, _legacy_bundle("regra-0022"))
    assert any(v.code == "AUDITADA_ID_DUPLICADO" for v in violations)


def test_unknown_origin_is_flagged() -> None:
    """An origens_legacy entry not present in the legacy bundle is flagged."""
    unidades = [_unidade("invalidez-a", origens_legacy=["regra-9999"])]
    violations = validate_bundle_auditado(unidades, _legacy_bundle("regra-0001"))
    assert any(v.code == "AUDITADA_ORIGEM_INEXISTENTE" for v in violations)


def test_one_to_n_decomposition_is_valid() -> None:
    """A single legacy origin split into >=2 audited units (RFC 0004 §1.2 — the 0022 case)."""
    unidades = [
        _unidade("invalidez-acidente", origens_legacy=["regra-0022"]),
        _unidade("invalidez-doenca", origens_legacy=["regra-0022"]),
    ]
    assert validate_bundle_auditado(unidades, _legacy_bundle("regra-0022")) == []


def test_n_to_one_consolidation_is_valid() -> None:
    """Several legacy origins consolidated into one audited unit (RFC 0004 §1.2)."""
    unidades = [_unidade("consolidada", origens_legacy=["regra-0001", "regra-0002"])]
    assert validate_bundle_auditado(unidades, _legacy_bundle("regra-0001", "regra-0002")) == []


def test_id_is_independent_of_row_index() -> None:
    """The audited unit's id carries no row_index at all — only origens_legacy does."""
    unidade = _unidade("invalidez-acidente-pos-2003", origens_legacy=["regra-0022"])
    assert "row_index" not in unidade.frontmatter
    assert validate_bundle_auditado([unidade], _legacy_bundle("regra-0022")) == []


def test_id_shaped_like_a_legacy_regra_id_is_rejected() -> None:
    """An audited unit id that reuses the regra-NNNN shape is rejected."""
    unidades = [_unidade("regra-0022", origens_legacy=["regra-0022"])]
    violations = validate_bundle_auditado(unidades, _legacy_bundle("regra-0022"))
    assert any(v.code == "AUDITADA_ID_INVALIDO" for v in violations)


def test_malformed_frontmatter_is_flagged_without_hiding_identity_errors() -> None:
    """An invalid schema_version must not blind the identity/provenance checks that still run."""
    unidade = _unidade("invalidez-acidente", origens_legacy=["regra-9999"], schema_version=2)
    violations = validate_bundle_auditado([unidade], _legacy_bundle("regra-0001"))
    codes = {v.code for v in violations}
    assert "AUDITADA_FRONTMATTER_INVALIDA" in codes
    assert "AUDITADA_ORIGEM_INEXISTENTE" in codes


_PROTOCOLO_VALIDO = {
    "pergunta": "x",
    "responsavel": "x",
    "meio_de_prova": "x",
    "momento": "x",
    "evidencia_exigida": "x",
}


@pytest.mark.parametrize("campo_em_branco", sorted(_PROTOCOLO_VALIDO))
def test_protocolo_verificacao_rejects_whitespace_only_field(campo_em_branco: str) -> None:
    """A field that's only whitespace must not pass min_length=1 by accident."""
    valores = {**_PROTOCOLO_VALIDO, campo_em_branco: "   "}
    with pytest.raises(ValidationError):
        ProtocoloVerificacao(**valores)


def test_proveniencia_rejects_a_whitespace_only_fonte_consultada() -> None:
    """A fontes_consultadas entry that's only whitespace must be rejected, not silently kept."""
    with pytest.raises(ValidationError):
        Proveniencia(fontes_consultadas=["   "])
