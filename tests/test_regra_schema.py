"""P13.2 invariants for the normative CSV <-> .md column map."""

from __future__ import annotations

import pytest
from okf_common import DEFAULT_BUNDLE, ORIGINAL_CSV
from pydantic import ValidationError
from regra_schema import (
    ADMIN_FIELD_DEFAULTS,
    COLUMNS,
    CSV_COLUMN_NAMES,
    FRONTMATTER_COLUMNS,
    FRONTMATTER_KEYS,
    Precedente,
    RegraAdminContrato,
    blank_frontmatter,
    render_schema_table,
)


def _celulas(tabela: str) -> list[list[str]]:
    """As linhas de uma tabela markdown como células cruas, sem o preenchimento do mdformat.

    Comparar as strings inteiras não serve: o doc passa pelo `mdformat`, que
    alinha as colunas com espaços, e `render_schema_table()` devolve a forma
    compacta. O conteúdo das células é o que tem de coincidir.
    """
    linhas = [linha for linha in tabela.splitlines() if linha.startswith("|")]
    return [[c.strip() for c in linha.strip("|").split("|")] for linha in linhas if set(linha) - set("| -")]


def test_every_original_column_appears_exactly_once() -> None:
    """The map must cover the real CSV header, in order, with no gaps or repeats."""
    header_line = ORIGINAL_CSV.read_text(encoding="utf-8").splitlines()[1]
    actual_header = tuple(header_line.split(","))

    assert actual_header == CSV_COLUMN_NAMES
    assert len(set(CSV_COLUMN_NAMES)) == len(CSV_COLUMN_NAMES)


def test_schema_table_do_doc_dataset_em_sincronia_com_columns() -> None:
    """A "# Schema" publicada não pode divergir do mapa normativo que a gera.

    A tabela é escrita por `csv_to_okf.py`, que é bootstrap de uma vez só e se
    recusa a rodar de novo — enquanto `COLUMNS` continua se movendo. Sem esta
    asserção, editar uma célula do mapa deixa o doc do bundle (e a página que o
    publica) afirmando a versão antiga, em silêncio. Foi o que ia acontecer com
    a correção da `semantica_vazio` das quatro colunas de data (RFC 0011).
    """
    doc = (DEFAULT_BUNDLE / "regras-sisprev.md").read_text(encoding="utf-8")
    publicada = doc.split("# Schema", 1)[1].split("\n#", 1)[0]

    assert _celulas(publicada) == _celulas(render_schema_table())


def test_every_column_maps_to_a_frontmatter_key() -> None:
    """Every original column is a frontmatter key, no column dropped (P13.2).

    The frontmatter *is* the deployable rule (refactor 2026-07).
    """
    assert set(FRONTMATTER_COLUMNS) == set(CSV_COLUMN_NAMES)
    assert set(FRONTMATTER_KEYS) == set(CSV_COLUMN_NAMES)


def test_frontmatter_keys_are_unique() -> None:
    """Two columns must never collide on the same frontmatter key."""
    keys = list(FRONTMATTER_KEYS.values())
    assert len(keys) == len(set(keys))


def test_nome_maps_directly_from_nome_column() -> None:
    """P1 decision: NOME <-> nome, no title/nome duplication."""
    assert FRONTMATTER_KEYS["NOME"] == "nome"


def test_admin_fields_are_a_separate_namespace_from_original_columns() -> None:
    """Administrative fields (P2.1/P7) never collide with an original column's frontmatter key."""
    original_keys = set(FRONTMATTER_KEYS.values())
    assert original_keys.isdisjoint(ADMIN_FIELD_DEFAULTS.keys())


def test_columns_tuple_matches_derived_constants() -> None:
    """Sanity: the derived tuples/dicts are actually derived from COLUMNS, not hand-duplicated."""
    original_column_count = 27

    assert len(COLUMNS) == original_column_count
    assert len(CSV_COLUMN_NAMES) == original_column_count
    # Every column is a frontmatter key now (P13.2, refactor 2026-07).
    assert len(FRONTMATTER_COLUMNS) == original_column_count
    assert len(FRONTMATTER_KEYS) == original_column_count


def test_blank_frontmatter_has_every_frontmatter_key_defaulted_to_empty_string() -> None:
    """blank_frontmatter() is a ready-to-override base for synthetic Regra fixtures."""
    fm = blank_frontmatter()
    assert set(fm) == set(FRONTMATTER_KEYS.values())
    assert all(value == "" for value in fm.values())


def test_regra_admin_contrato_defaults_to_ativa_with_no_dispositivos() -> None:
    """An empty admin slice (key genuinely absent) defaults exactly like ADMIN_FIELD_DEFAULTS."""
    contrato = RegraAdminContrato.model_validate({})
    assert contrato.status_regra == ADMIN_FIELD_DEFAULTS["status_regra"]
    assert contrato.dispositivos == []


def test_regra_admin_contrato_ignores_domain_fields() -> None:
    """extra='ignore': validating the whole ~27-field frontmatter dict must not raise."""
    contrato = RegraAdminContrato.model_validate({**blank_frontmatter(), "status_regra": "inativa"})
    assert contrato.status_regra == "inativa"


def test_regra_admin_contrato_rejects_an_unknown_status_regra() -> None:
    """status_regra is a closed enum (P2.1: only ativa/inativa) — anything else is invalid."""
    with pytest.raises(ValidationError):
        RegraAdminContrato.model_validate({"status_regra": "foo"})


def test_precedente_exige_identificador_e_fonte() -> None:
    """Um precedente sem origem declarada não é conferível — e é o que ele promete ser."""
    with pytest.raises(ValidationError):
        Precedente.model_validate({"identificador": "0031.117501/2020-19"})
    with pytest.raises(ValidationError):
        Precedente.model_validate({"identificador": "", "fonte": "SEI"})


def test_precedente_recusa_campo_desconhecido() -> None:
    """`extra="forbid"`, como AtoValidacao: um campo com nome errado é erro, não é ignorado."""
    with pytest.raises(ValidationError):
        Precedente.model_validate({"identificador": "x", "fonte": "SEI", "tipo": "parecer"})


def test_precedente_nao_e_ato_de_validacao() -> None:
    """Os dois campos convivem sem se contaminar — um registra uso, o outro aprovação.

    O contrato administrativo aceita precedentes sem que nada nele passe a
    valer como ato de validação: `atos_validacao` é o que o P7 exige para
    `status_auditoria: validada`, e ele continua vazio aqui.
    """
    contrato = RegraAdminContrato.model_validate(
        {"precedentes": [{"identificador": "0031.117501/2020-19", "fonte": "SEI"}]},
    )

    assert len(contrato.precedentes) == 1
    assert contrato.model_dump().get("atos_validacao") is None
