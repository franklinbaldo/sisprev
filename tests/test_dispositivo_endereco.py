"""Tests for the P3 structural address — nesting, slug, label and legal order.

Pure unit tests: this module has no filesystem or document dependency, and
the invariants here are exactly the ones the previous flat
``artigo``/``paragrafo``/``inciso``/``alinea`` schema could not state.
"""

from __future__ import annotations

import pytest
from dispositivo_endereco import (
    Componente,
    ComponenteInvalidoError,
    TipoComponente,
    chave_de_ordem,
    romano_para_int,
    rotulo_do_endereco,
    slug_do_endereco,
    validar_aninhamento,
)
from pydantic import ValidationError


def _art(valor: str, sufixo: str | None = None) -> Componente:
    return Componente(tipo=TipoComponente.ARTIGO, valor=valor, sufixo=sufixo)


def _par(valor: str, sufixo: str | None = None) -> Componente:
    return Componente(tipo=TipoComponente.PARAGRAFO, valor=valor, sufixo=sufixo)


def _inc(valor: str) -> Componente:
    return Componente(tipo=TipoComponente.INCISO, valor=valor)


def _al(valor: str) -> Componente:
    return Componente(tipo=TipoComponente.ALINEA, valor=valor)


_CAPUT = Componente(tipo=TipoComponente.CAPUT)
_PAR_UNICO = Componente(tipo=TipoComponente.PARAGRAFO_UNICO)


# --- valor/sufixo shape -------------------------------------------------


def test_level_that_takes_a_value_requires_one() -> None:
    """An artigo without a valor is not an address, it's a fragment."""
    with pytest.raises(ValidationError, match="requires a 'valor'"):
        Componente(tipo=TipoComponente.ARTIGO)


def test_singular_level_rejects_a_value() -> None:
    """``caput`` is singular by definition — "caput 2" is not a thing."""
    with pytest.raises(ValidationError, match="takes no 'valor'"):
        Componente(tipo=TipoComponente.CAPUT, valor="1")


def test_inciso_must_be_a_roman_numeral() -> None:
    """Incisos are numbered in Roman numerals; an Arabic one is a transcription error."""
    with pytest.raises(ValidationError, match="Roman numeral"):
        _inc("3")


def test_inciso_made_of_roman_letters_but_unreadable_is_rejected() -> None:
    """'IL' is spelled with Roman letters and still has no value — so it has no order.

    Accepting it would let the document validate and then raise inside
    ``chave_de_ordem`` when the index is regenerated, which is exactly the
    crash-instead-of-violation the contract exists to prevent.
    """
    with pytest.raises(ValidationError, match="cannot be ordered"):
        _inc("IL")


def test_alinea_must_be_a_single_lowercase_letter() -> None:
    """Alíneas are lettered a), b), c) — never numbered."""
    with pytest.raises(ValidationError, match="single lowercase letter"):
        _al("A")


def test_artigo_value_carries_no_typography() -> None:
    """The value is data, not display: "Art. 40" belongs to the label, not the field."""
    with pytest.raises(ValidationError, match="positive integer"):
        _art("Art. 40")


def test_suffix_is_separate_from_the_number() -> None:
    """Art. 6º-A is (6, "A") — sortable — never the opaque string "6º-A"."""
    componente = _art("6", "A")
    numero_do_artigo = 6
    assert componente.valor == "6"
    assert componente.sufixo == "A"
    assert componente.numero == numero_do_artigo


def test_suffix_is_rejected_on_a_level_that_never_takes_one() -> None:
    """There is no "inciso I-A" in this corpus' drafting conventions."""
    with pytest.raises(ValidationError, match="takes no 'sufixo'"):
        Componente(tipo=TipoComponente.INCISO, valor="I", sufixo="A")


# --- nesting ------------------------------------------------------------


def test_valid_addresses_have_no_nesting_violations() -> None:
    """Every address shape this corpus actually uses must validate."""
    for componentes in (
        [_art("40")],
        [_art("40"), _CAPUT],
        [_art("40"), _inc("I")],
        [_art("40"), _par("1"), _inc("I")],
        # The caput of a *paragraph* — an address the old schema could not
        # express at all, and the reason "caput" is not a fixed depth.
        [_art("40"), _par("1"), _CAPUT],
        [_art("3"), _PAR_UNICO],
        [_art("1"), _inc("II"), _al("a")],
        [_art("6", "A")],
    ):
        assert validar_aninhamento(componentes) == [], componentes


def test_address_must_start_with_an_artigo() -> None:
    """A paragraph with no article names nothing."""
    erros = validar_aninhamento([_par("1")])
    assert any("must start with an artigo" in e for e in erros)


def test_empty_address_is_rejected() -> None:
    """An address with no componentes cannot identify a provision."""
    assert validar_aninhamento([]) == ["address must have at least one componente (the artigo)"]


def test_levels_must_go_outermost_inwards() -> None:
    """An inciso cannot contain a paragraph — that inverts the norm's structure."""
    erros = validar_aninhamento([_art("40"), _inc("I"), _par("1")])
    assert any("cannot nest inside" in e for e in erros)


def test_nothing_nests_inside_a_caput() -> None:
    """The caput is the unit's opening text: it has no enumerated children."""
    erros = validar_aninhamento([_art("40"), _CAPUT, _inc("I")])
    assert any("nothing can nest inside it" in e for e in erros)


def test_alinea_requires_an_inciso() -> None:
    """This is the orphan state the four flat optional fields silently admitted."""
    erros = validar_aninhamento([_art("1"), _al("a")])
    assert erros == ["'alinea' must hang off an 'inciso'"]


def test_item_requires_an_alinea() -> None:
    """Items hang off alíneas, never directly off an inciso."""
    erros = validar_aninhamento([_art("1"), _inc("II"), Componente(tipo=TipoComponente.ITEM, valor="1")])
    assert erros == ["'item' must hang off an 'alinea'"]


# --- slug ---------------------------------------------------------------


def test_slug_prefixes_every_level() -> None:
    """Each segment names its own level, so no reading depends on position."""
    assert slug_do_endereco([_art("40"), _par("1"), _inc("I")]) == "art-40-par-1-inc-i"
    assert slug_do_endereco([_art("1"), _inc("II"), _al("a")]) == "art-1-inc-ii-al-a"
    assert slug_do_endereco([_art("40"), _CAPUT]) == "art-40-caput"
    assert slug_do_endereco([_art("3"), _PAR_UNICO]) == "art-3-par-unico"
    assert slug_do_endereco([_art("6", "A")]) == "art-6a"
    assert slug_do_endereco([_art("40"), _par("4", "B")]) == "art-40-par-4b"


def test_slug_distinguishes_an_article_from_its_caput() -> None:
    """The whole article and the article's caput are different provisions."""
    assert slug_do_endereco([_art("20")]) != slug_do_endereco([_art("20"), _CAPUT])


# --- label (P4 canonical citation) --------------------------------------


def test_label_is_the_canonical_citation() -> None:
    """The citation format P4 asks for is derived here, never authored by hand."""
    assert rotulo_do_endereco([_art("40"), _par("1"), _inc("I")]) == "art. 40, § 1º, inciso I"
    assert rotulo_do_endereco([_art("1"), _inc("II"), _al("a")]) == "art. 1º, inciso II, alínea a"
    assert rotulo_do_endereco([_art("40"), _CAPUT]) == "art. 40, caput"
    assert rotulo_do_endereco([_art("3"), _PAR_UNICO]) == "art. 3º, parágrafo único"


def test_label_uses_the_ordinal_convention_of_legal_drafting() -> None:
    """1º..9º carry the ordinal marker; 10 onward are cardinal."""
    assert rotulo_do_endereco([_art("9")]) == "art. 9º"
    assert rotulo_do_endereco([_art("10")]) == "art. 10"
    assert rotulo_do_endereco([_art("40"), _par("14")]) == "art. 40, § 14"
    assert rotulo_do_endereco([_art("6", "A")]) == "art. 6º-A"


# --- ordering -----------------------------------------------------------


def _ordenado(enderecos: list[list[Componente]]) -> list[str]:
    return [slug_do_endereco(c) for c in sorted(enderecos, key=chave_de_ordem)]


def test_paragraphs_sort_numerically_not_as_strings() -> None:
    """§ 2º before § 14 — the exact failure the old path-order index shipped with."""
    assert _ordenado([[_art("20"), _par("14")], [_art("20"), _par("2")], [_art("20"), _par("9")]]) == [
        "art-20-par-2",
        "art-20-par-9",
        "art-20-par-14",
    ]


def test_articles_sort_numerically() -> None:
    """Art. 10 must not sort before art. 9º."""
    assert _ordenado([[_art("10")], [_art("9")], [_art("62")]]) == ["art-9", "art-10", "art-62"]


def test_incisos_of_the_caput_precede_the_paragraphs() -> None:
    """This is how the article reads, and what a per-level depth rank gets wrong.

    A rank-based key would place every paragraph (a shallower level) ahead of
    every inciso; the norm itself reads caput, then the caput's incisos, then
    § 1º and its incisos.
    """
    ordem = _ordenado(
        [
            [_art("40"), _par("1"), _inc("I")],
            [_art("40"), _inc("II")],
            [_art("40"), _CAPUT],
            [_art("40"), _par("1"), _CAPUT],
            [_art("40"), _inc("I")],
        ]
    )
    assert ordem == [
        "art-40-caput",
        "art-40-inc-i",
        "art-40-inc-ii",
        "art-40-par-1-caput",
        "art-40-par-1-inc-i",
    ]


def test_incisos_sort_by_roman_value() -> None:
    """IX before X — impossible on the rendered string."""
    assert _ordenado([[_art("1"), _inc("X")], [_art("1"), _inc("IX")], [_art("1"), _inc("IV")]]) == [
        "art-1-inc-iv",
        "art-1-inc-ix",
        "art-1-inc-x",
    ]


def test_suffixed_article_sorts_after_its_base() -> None:
    """Art. 6º-A follows Art. 6º and precedes Art. 7º."""
    assert _ordenado([[_art("7")], [_art("6", "A")], [_art("6")]]) == ["art-6", "art-6a", "art-7"]


def test_order_key_is_total() -> None:
    """Two distinct addresses never tie, so index order is deterministic."""
    enderecos = [[_art("20")], [_art("20"), _CAPUT]]
    assert len({chave_de_ordem(c) for c in enderecos}) == len(enderecos)


# --- roman numerals -----------------------------------------------------


@pytest.mark.parametrize(
    ("romano", "esperado"),
    [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XIV", 14), ("XL", 40), ("C", 100)],
)
def test_roman_numerals_decode(romano: str, esperado: int) -> None:
    """Subtractive forms included — incisos really are written IV and IX."""
    assert romano_para_int(romano) == esperado


def test_unreadable_roman_numeral_raises() -> None:
    """A value that isn't a numeral must fail loudly, never order as zero."""
    with pytest.raises(ComponenteInvalidoError, match="not a Roman numeral"):
        romano_para_int("ABC")
