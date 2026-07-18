"""P13.2 invariants for the normative CSV <-> .md column map."""

from __future__ import annotations

from okf_common import ORIGINAL_CSV
from regra_schema import (
    ADMIN_FIELD_DEFAULTS,
    BODY_COLUMNS,
    BODY_HEADINGS,
    COLUMNS,
    CSV_COLUMN_NAMES,
    FRONTMATTER_COLUMNS,
    FRONTMATTER_KEYS,
    HEADING_TO_CSV_NAME,
    blank_frontmatter,
)


def test_every_original_column_appears_exactly_once() -> None:
    """The map must cover the real CSV header, in order, with no gaps or repeats."""
    header_line = ORIGINAL_CSV.read_text(encoding="utf-8").splitlines()[1]
    actual_header = tuple(header_line.split(","))

    assert actual_header == CSV_COLUMN_NAMES
    assert len(set(CSV_COLUMN_NAMES)) == len(CSV_COLUMN_NAMES)


def test_every_column_is_frontmatter_xor_body() -> None:
    """No column is silently dropped or double-mapped (P13.2 CI invariant)."""
    frontmatter_set = set(FRONTMATTER_COLUMNS)
    body_set = set(BODY_COLUMNS)

    assert frontmatter_set.isdisjoint(body_set)
    assert frontmatter_set | body_set == set(CSV_COLUMN_NAMES)


def test_body_headings_are_bijective_with_columns() -> None:
    """Every body heading round-trips back to its column (ida-e-volta bijetiva)."""
    assert set(HEADING_TO_CSV_NAME.values()) == set(BODY_COLUMNS)
    for csv_name, heading in BODY_HEADINGS.items():
        assert HEADING_TO_CSV_NAME[heading] == csv_name


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
    body_column_count = 3
    frontmatter_column_count = original_column_count - body_column_count

    assert len(COLUMNS) == original_column_count
    assert len(CSV_COLUMN_NAMES) == original_column_count
    assert len(BODY_COLUMNS) == body_column_count
    assert len(FRONTMATTER_COLUMNS) == frontmatter_column_count


def test_blank_frontmatter_has_every_frontmatter_key_defaulted_to_empty_string() -> None:
    """blank_frontmatter() is a ready-to-override base for synthetic Regra fixtures."""
    fm = blank_frontmatter()
    assert set(fm) == set(FRONTMATTER_KEYS.values())
    assert all(value == "" for value in fm.values())
