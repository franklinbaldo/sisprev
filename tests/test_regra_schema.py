"""P13.2 invariants for the normative CSV <-> .md column map."""

from __future__ import annotations

import pytest
from okf_common import ORIGINAL_CSV
from pydantic import ValidationError
from regra_schema import (
    ADMIN_FIELD_DEFAULTS,
    COLUMNS,
    CSV_COLUMN_NAMES,
    FRONTMATTER_COLUMNS,
    FRONTMATTER_KEYS,
    RegraAdminContrato,
    blank_frontmatter,
)


def test_every_original_column_appears_exactly_once() -> None:
    """The map must cover the real CSV header, in order, with no gaps or repeats."""
    header_line = ORIGINAL_CSV.read_text(encoding="utf-8").splitlines()[1]
    actual_header = tuple(header_line.split(","))

    assert actual_header == CSV_COLUMN_NAMES
    assert len(set(CSV_COLUMN_NAMES)) == len(CSV_COLUMN_NAMES)


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
