"""Tests for Regra's typed P2.1/P3 administrative contract (RFC 0001) and its fallback."""

from __future__ import annotations

from bundle import Regra
from regra_schema import blank_frontmatter


def _regra(**overrides: object) -> Regra:
    fm = blank_frontmatter()
    fm["nome"] = "Regra de teste"
    fm.update(overrides)
    return Regra(doc_id="regra-0001", frontmatter=fm)


def test_admin_is_populated_for_a_well_formed_regra() -> None:
    """A regra with a valid status_regra/dispositivos gets a real, typed contract."""
    regra = _regra(status_regra="inativa", dispositivos=["/dispositivos/lei-teste/art-1.md"])
    assert regra.admin is not None
    assert regra.status_regra == "inativa"
    assert regra.dispositivos == ["/dispositivos/lei-teste/art-1.md"]


def test_status_regra_defaults_to_ativa_when_absent() -> None:
    """A regra that never mentions status_regra is ativa by default (P2.1)."""
    regra = _regra()
    assert regra.admin is not None
    assert regra.status_regra == "ativa"


def test_malformed_status_regra_falls_back_but_does_not_hide_dispositivos() -> None:
    """An out-of-enum status_regra invalidates .admin, but .dispositivos still reads correctly.

    One malformed field in the P2.1/P3 slice must not blind the other —
    active_regras() and check_p3_dispositivos() each depend on exactly one
    of these two fields, independently.
    """
    regra = _regra(status_regra="not-a-real-status", dispositivos=["/dispositivos/lei-teste/art-1.md"])

    assert regra.admin is None
    assert regra.status_regra == "not-a-real-status"  # raw passthrough, matches pre-typed behavior
    assert regra.dispositivos == ["/dispositivos/lei-teste/art-1.md"]


def test_malformed_dispositivos_falls_back_but_does_not_hide_status_regra() -> None:
    """A non-list dispositivos value invalidates .admin, but .status_regra still reads correctly."""
    regra = _regra(status_regra="ativa", dispositivos="not-a-list")

    assert regra.admin is None
    assert regra.status_regra == "ativa"
    assert regra.dispositivos == []


def test_empty_string_status_regra_falls_back_to_the_default() -> None:
    """A present-but-empty status_regra is treated as absent, matching ADMIN_FIELD_DEFAULTS."""
    regra = _regra(status_regra="")
    assert regra.status_regra == "ativa"
