"""Tests for the shared Concept base (RFC 0001) — parsing, caching, error typing."""

from __future__ import annotations

from concept import UNSET_BUNDLE_DIR, Concept, ConceptDocError, parse_concept_doc


def test_sections_is_cached_not_reparsed_on_every_access() -> None:
    """Concept.sections must be computed once per instance, not re-scanned per read.

    A frozen Concept's body never changes, so returning a fresh dict from
    parse_sections() on every access is pure repeated work — cached_property
    memoizes it; identity across repeated reads proves that.
    """
    concept = Concept(doc_id="x", frontmatter={}, body="# H\n\ntexto\n")
    assert concept.sections is concept.sections


def test_frontmatter_value_may_contain_a_triple_dash() -> None:
    """A ``---`` inside a frontmatter value must not be mistaken for a delimiter.

    P13.2 moved free-text fundamentação into the frontmatter, so an auditor
    can write ``---`` inside a value. The delimiter is a *line* that is
    exactly ``---``; a naive ``split("---")`` would truncate the value and
    silently drop every key after it.
    """
    doc = (
        "---\n"
        "type: Regra\n"
        "fundamentacao_integral: Art. 40 --- CF/88, EC 41/2003 --- fim\n"
        "nome: Depois do traço\n"
        "---\n"
    )
    frontmatter, body = parse_concept_doc(doc)
    assert frontmatter["fundamentacao_integral"] == "Art. 40 --- CF/88, EC 41/2003 --- fim"
    assert frontmatter["nome"] == "Depois do traço"
    assert body == ""


def test_concept_doc_error_is_a_value_error() -> None:
    """ConceptDocError must stay catchable as ValueError for backward compatibility.

    Bundle.load()'s regra loop has no regra-specific wrapper error (unlike
    Achado/Dispositivo) — the only guarantee it preserves is that a
    malformed doc still raises something a `except ValueError` catches, the
    same as the str.split()-raised ValueError this replaced.
    """
    assert issubclass(ConceptDocError, ValueError)


def test_unset_bundle_dir_is_never_a_real_directory() -> None:
    """UNSET_BUNDLE_DIR must never resolve to cwd or any other real directory.

    It's the default for Bundle.bundle_dir/dispositivos_dir and
    Concept.bundle_dir specifically because Path() (cwd) is real and would
    make every `.is_dir()` guard in the loaders treat "unset" as "walk the
    whole repository".
    """
    assert not UNSET_BUNDLE_DIR.is_dir()
