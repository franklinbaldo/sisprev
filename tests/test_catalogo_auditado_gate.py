"""RFC 0004 §14 — CI gate integration + non-regression against the real repo state."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bundle import Bundle
from catalogo_auditado_gate import check_catalogo_auditado
from okf_common import DEFAULT_BUNDLE

if TYPE_CHECKING:
    from pathlib import Path

_MANIFESTO_VAZIO = "schema_version: 1\ngrupos: []\n"
_LEGACY_ROW_COUNT = 112


def _unidade_valida_yaml(doc_id: str, origem: str) -> str:
    return (
        "---\n"
        "type: UnidadeAuditada\n"
        f"id: {doc_id}\n"
        "schema_version: 1\n"
        "estado_unidade: elaboracao\n"
        f"origens_legacy: [{origem}]\n"
        "---\n"
    )


def test_real_empty_audited_bundle_and_manifest_pass_cleanly() -> None:
    """RFC 0004 §14: an audited bundle with zero units, and an empty manifest, must both pass."""
    bundle_legado = Bundle.load(DEFAULT_BUNDLE)
    assert check_catalogo_auditado(bundle_legado) == []


def test_112_legacy_regras_are_untouched() -> None:
    """Non-regression: this PR must not change the frozen legacy row count."""
    assert len(Bundle.load(DEFAULT_BUNDLE).regras) == _LEGACY_ROW_COUNT


def test_malformed_audited_unit_fails_the_gate(tmp_path: Path) -> None:
    """An audited unit with an invalid frontmatter fails the gate."""
    bundle_auditado_dir = tmp_path / "regras-auditadas"
    (bundle_auditado_dir / "unidades").mkdir(parents=True)
    (bundle_auditado_dir / "unidades" / "invalido.md").write_text(
        "---\ntype: UnidadeAuditada\nid: invalido\nschema_version: 2\n---\n",
        encoding="utf-8",
    )
    manifesto_path = tmp_path / "manifesto-substituicao.yaml"
    manifesto_path.write_text(_MANIFESTO_VAZIO, encoding="utf-8")

    violations = check_catalogo_auditado(
        Bundle.load(DEFAULT_BUNDLE), bundle_auditado_dir=bundle_auditado_dir, manifesto_path=manifesto_path
    )

    assert any(v.code == "AUDITADA_FRONTMATTER_INVALIDA" for v in violations)


def test_malformed_manifest_fails_the_gate(tmp_path: Path) -> None:
    """A manifest with an unknown schema_version fails the gate."""
    bundle_auditado_dir = tmp_path / "regras-auditadas"
    (bundle_auditado_dir / "unidades").mkdir(parents=True)
    manifesto_path = tmp_path / "manifesto-substituicao.yaml"
    manifesto_path.write_text("schema_version: 2\ngrupos: []\n", encoding="utf-8")

    violations = check_catalogo_auditado(
        Bundle.load(DEFAULT_BUNDLE), bundle_auditado_dir=bundle_auditado_dir, manifesto_path=manifesto_path
    )

    assert any(v.code == "MANIFESTO_INVALIDO" for v in violations)


def test_missing_manifest_file_fails_the_gate(tmp_path: Path) -> None:
    """A missing production manifest file fails the gate."""
    bundle_auditado_dir = tmp_path / "regras-auditadas"
    (bundle_auditado_dir / "unidades").mkdir(parents=True)

    violations = check_catalogo_auditado(
        Bundle.load(DEFAULT_BUNDLE),
        bundle_auditado_dir=bundle_auditado_dir,
        manifesto_path=tmp_path / "nope.yaml",
    )

    assert any(v.code == "MANIFESTO_AUSENTE" for v in violations)


def test_active_group_in_the_production_shaped_manifest_fails_the_gate(tmp_path: Path) -> None:
    """RFC 0004 Fase 1A: no group may be active for real, even a structurally complete one."""
    bundle_auditado_dir = tmp_path / "regras-auditadas"
    (bundle_auditado_dir / "unidades").mkdir(parents=True)
    (bundle_auditado_dir / "unidades" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001").replace("elaboracao", "deployable"),
        encoding="utf-8",
    )
    manifesto_path = tmp_path / "manifesto-substituicao.yaml"
    manifesto_path.write_text(
        "schema_version: 1\n"
        "grupos:\n"
        "  - grupo: substituicao-regra-0001\n"
        "    origens_legacy: [regra-0001]\n"
        "    destinos_auditados: [unidade-a]\n"
        "    estado_grupo: ativo\n"
        "    decisao_completude:\n"
        "      decidido_por: teste\n"
        "      decidido_em: '2026-07-23'\n"
        "      justificativa: teste\n"
        "      fonte: teste\n",
        encoding="utf-8",
    )

    violations = check_catalogo_auditado(
        Bundle.load(DEFAULT_BUNDLE), bundle_auditado_dir=bundle_auditado_dir, manifesto_path=manifesto_path
    )

    assert any(v.code == "MANIFESTO_ATIVACAO_NAO_SUPORTADA" for v in violations)


def test_empty_audited_bundle_with_valid_unit_still_passes(tmp_path: Path) -> None:
    """A well-formed audited unit with a real origin, no manifest entry, changes nothing operationally."""
    bundle_auditado_dir = tmp_path / "regras-auditadas"
    (bundle_auditado_dir / "unidades").mkdir(parents=True)
    (bundle_auditado_dir / "unidades" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    manifesto_path = tmp_path / "manifesto-substituicao.yaml"
    manifesto_path.write_text(_MANIFESTO_VAZIO, encoding="utf-8")

    violations = check_catalogo_auditado(
        Bundle.load(DEFAULT_BUNDLE), bundle_auditado_dir=bundle_auditado_dir, manifesto_path=manifesto_path
    )

    assert violations == []
