"""Tests for reading the provisions a fundamentação cites (P4).

Every case here is a citation shape that **actually occurs** in the corpus,
copied from a real ``FUNDAMENTACAO*`` field. That is deliberate: the value
of this module is not that it parses some idealized citation grammar, it is
that its error rate against *this* prose is known. Two bugs found by eye
during development (a norm spelling that silently reattributed articles to
the next norm named, and an article list where only the first number was
read) are pinned below so they cannot come back unnoticed.
"""

from __future__ import annotations

import dataclasses

import pytest
from citacoes import Citacao, SituacaoCitacao, extrair_citacoes
from dispositivo_endereco import rotulo_do_endereco, slug_do_endereco


def _enderecaveis(texto: str) -> list[tuple[str, str, str | None]]:
    """Return ``(norma, slug, redacao)`` for each addressable citation."""
    return [
        (c.norma or "", slug_do_endereco(c.componentes), c.redacao)
        for c in extrair_citacoes(texto)
        if c.situacao is SituacaoCitacao.ENDERECAVEL
    ]


def _situacoes(texto: str) -> list[SituacaoCitacao]:
    return [c.situacao for c in extrair_citacoes(texto)]


def test_empty_text_cites_nothing() -> None:
    """A regra with no fundamentação claims nothing."""
    assert extrair_citacoes("") == []
    assert extrair_citacoes("   ") == []


def test_simple_citation_with_explicit_wording() -> None:
    """The base shape: address, owning norm, then the amending norm."""
    texto = (
        "com base no artigo 40, § 1º, II, da Constituição Federal, "
        "com redação dada pela Emenda Constitucional nº 88/2015."
    )
    assert _enderecaveis(texto) == [("cf88", "art-40-par-1-inc-ii", "ec-88-2015")]


def test_wording_marker_is_never_read_as_the_owning_norm() -> None:
    """A "com redação dada pela" clause names the amendment, not the owner.

    Reading it as the owner would file CF art. 40 under the amending
    Emenda — the single most likely way to attribute an article to the
    wrong norm.
    """
    texto = (
        "artigo 40, § 1º, I, da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003"
    )
    assert _enderecaveis(texto) == [("cf88", "art-40-par-1-inc-i", "ec-41-2003")]


def test_article_whose_owning_norm_is_never_named_is_reported_as_such() -> None:
    """Real corpus prose names only the amendment, leaving the CF implicit.

    The reader knows art. 40 is the CF's; the parser must not guess. It
    reports SEM_NORMA so a human decides, rather than filing the article
    under the amending Emenda.
    """
    texto = (
        "artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, "
        "no que tange à fórmula de cálculo"
    )
    assert SituacaoCitacao.SEM_NORMA in _situacoes(texto)
    assert _enderecaveis(texto) == []


def test_abbreviated_norm_spelling_is_recognised() -> None:
    """Regression: an abbreviated norm spelling was silently reattributed.

    "EC nº 146/2021" was unrecognised, so its articles were filed under the
    "Constituição Federal" named afterwards.
    """
    texto = (
        "com base no artigo 6º, § 2º, I, e § 3°, I, da EC nº 146/2021, "
        "e artigo 40, § 5°, da Constituição Federal"
    )
    normas = {norma for norma, _, _ in _enderecaveis(texto)}
    assert normas == {"ece-146-2021", "cf88"}
    assert ("cf88", "art-6", None) not in _enderecaveis(texto)


def test_article_list_reads_every_number_not_just_the_first() -> None:
    """Regression: "artigos 17, 20, caput, 45 e 62" spells "artigo" once.

    Reading only 17 made the following "caput" attach to art. 17 instead of
    art. 20 — a wrong provision that still looked plausible.
    """
    texto = "artigos 17, 20, caput, 45 e 62 da Lei Complementar Estadual nº 432/2008"
    slugs = [slug for _, slug, _ in _enderecaveis(texto)]
    assert slugs == ["art-17", "art-20-caput", "art-45", "art-62"]


def test_semicolon_separates_articles_even_after_a_paragraph() -> None:
    """Regression, from regra-0012's real prose.

    "31, §§ 1º e 2º; 32, ...; 33; ...; 62" — once a § appeared, every later
    bare number inherited "paragrafo", inventing a "§ 62 do art. 31" out of
    what is plainly article 62. In this corpus ';' separates articles while
    ',' and 'e' continue whatever is being enumerated.
    """
    texto = (
        "Pensão mensal, com fundamento nos artigos 10, I; 28, I; 30, II; 31, §§ 1º e 2º; "
        "32, I; 33; 38; e 62 da Lei Complementar Estadual nº 432/2008"
    )
    slugs = [slug for _, slug, _ in _enderecaveis(texto)]
    assert "art-31-par-1" in slugs
    assert "art-31-par-2" in slugs
    assert "art-62" in slugs
    assert "art-33" in slugs
    assert not [s for s in slugs if s.startswith("art-31-par-6")]


def test_fragment_citation_is_not_widened_to_the_enclosing_provision() -> None:
    """A citation of "segunda parte" names half an inciso, which has no unit.

    Reporting it as a fragment keeps the citation honest. Linking it to the
    whole inciso would claim more than the prose did — a judgment reserved
    to the auditor.
    """
    texto = (
        "artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, "
        "com a redação dada pela Emenda Constitucional nº 103/2019"
    )
    assert _situacoes(texto) == [SituacaoCitacao.FRAGMENTO]
    assert _enderecaveis(texto) == []


def test_several_norms_in_one_sentence_each_keep_their_own_articles() -> None:
    """The corpus routinely chains three norms in a single fundamentação."""
    texto = (
        "com base no artigo 40, § 1º, II, da Constituição Federal, com redação dada pela "
        "Emenda Constitucional nº 88/2015, artigo 2º da Lei Complementar nº 152/2015, "
        "artigos 24, 26, 27, inciso II, e 31 da Lei Complementar Estadual nº 1.100/2021."
    )
    assert _enderecaveis(texto) == [
        ("cf88", "art-40-par-1-inc-ii", "ec-88-2015"),
        ("lc-152-2015", "art-2", None),
        ("lce-1100-2021", "art-24", None),
        ("lce-1100-2021", "art-26", None),
        ("lce-1100-2021", "art-27-inc-ii", None),
        ("lce-1100-2021", "art-31", None),
    ]


def test_bare_roman_numeral_in_a_list_is_an_inciso_of_its_article() -> None:
    """In "artigos 25, 27, I; 33" the I belongs to 27, not to 25 or 33."""
    texto = "artigos 25, 27, I; 33, da Lei Complementar nº 1.100/2021"
    assert _enderecaveis(texto) == [
        ("lce-1100-2021", "art-25", None),
        ("lce-1100-2021", "art-27-inc-i", None),
        ("lce-1100-2021", "art-33", None),
    ]


def test_paragraph_range_yields_one_citation_per_paragraph() -> None:
    """A range like §§ 2º e 3º cites two provisions, stored separately."""
    texto = "artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021"
    assert _enderecaveis(texto) == [
        ("ece-146-2021", "art-7-par-2", None),
        ("ece-146-2021", "art-7-par-3", None),
    ]


def test_alinea_in_quotes_is_read() -> None:
    """The corpus quotes alíneas: 'alínea "b"'."""
    texto = 'artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985'
    assert _enderecaveis(texto) == [("lc-51-1985", "art-1-inc-ii-al-b", None)]


def test_suffixed_paragraph_is_read_with_its_suffix() -> None:
    """A suffixed paragraph keeps the suffix separate, as the schema does."""
    texto = "artigo 40, § 4°-B da Constituição Federal"
    assert _enderecaveis(texto) == [("cf88", "art-40-par-4b", None)]


def test_norm_outside_the_vocabulary_is_still_attributed_not_skipped() -> None:
    """LCE 949/2017 is cited but has no norma.md.

    It is recognised so its articles are attributed to *it* — skipping the
    spelling would make the following norm swallow them.
    """
    texto = (
        "artigo 3º da Lei Complementar Estadual nº 949/2017 "
        "e artigo 20 da Lei Complementar Estadual nº 432/2008"
    )
    assert _enderecaveis(texto) == [
        ("lce-949-2017", "art-3", None),
        ("lce-432-2008", "art-20", None),
    ]


def test_citation_carries_the_prose_it_was_read_from() -> None:
    """A human checking the reading needs the source span, not just the verdict."""
    texto = "artigo 2º da Lei Complementar nº 152/2015"
    (citacao,) = [c for c in extrair_citacoes(texto) if c.situacao is SituacaoCitacao.ENDERECAVEL]
    assert "artigo 2" in citacao.trecho


def test_endereco_id_joins_norm_and_address() -> None:
    """The join key a caller resolves against the authored bundle."""
    texto = "artigo 40, § 5°, da Constituição Federal"
    (citacao,) = [c for c in extrair_citacoes(texto) if c.situacao is SituacaoCitacao.ENDERECAVEL]
    assert citacao.endereco_id == "cf88/art-40-par-5"
    assert rotulo_do_endereco(citacao.componentes) == "art. 40, § 5º"


def test_unaddressable_citation_has_no_endereco_id() -> None:
    """A fragment resolves to nothing, and says so instead of guessing."""
    texto = "artigo 40, §1°, inciso III, segunda parte, da Constituição Federal"
    (citacao,) = extrair_citacoes(texto)
    assert citacao.endereco_id is None


def test_prose_with_no_citation_at_all_yields_nothing() -> None:
    """Descriptive text without an article citation claims no provision."""
    assert extrair_citacoes("Aposentadoria compulsória, com proventos proporcionais.") == []


def test_citacao_is_frozen() -> None:
    """Citações are evidence, not mutable state."""
    (citacao,) = extrair_citacoes("artigo 2º da Lei Complementar nº 152/2015")
    assert isinstance(citacao, Citacao)
    # Called through __setattr__ so the check is the runtime one a caller
    # would actually hit, not a static assignment the type checker rejects.
    with pytest.raises(dataclasses.FrozenInstanceError):
        citacao.__setattr__("norma", "outra")
