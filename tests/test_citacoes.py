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


def test_comma_after_a_lone_paragraph_returns_to_the_article_level() -> None:
    """Regression, from regra-0027's real prose.

    "artigos 17, 21, § 1º, 45 e 62" is arts. 17, 21 § 1º, 45 and 62. Reading
    45 and 62 as paragraphs of art. 21 invented "§ 45" and "§ 62" — the
    articles 45 and 62 are transcribed provisions of this very norm. A lone
    "§" inside a list of articles is a detour, not a change of level; a
    range ("§§ 2º e 3º") is the case where it is not.
    """
    texto = "combinado com os artigos 17, 21, § 1º, 45 e 62 da Lei Complementar Estadual nº 432/2008"
    slugs = [slug for _, slug, _ in _enderecaveis(texto)]
    assert slugs == ["art-17", "art-21-par-1", "art-45", "art-62"]


def test_clause_qualifier_resolves_to_the_whole_provision() -> None:
    """A citation of "segunda parte" resolves to the inciso, keeping the qualifier.

    CF art. 40, § 1º, III (EC 103/2019) has no alíneas: its "segunda parte"
    is the "no âmbito dos Estados" clause of that same inciso. The provision
    the regra rests on *is* inciso III; which clause of it applies is what
    the prose says. Dropping the citation would leave the corpus' most-cited
    provision outside the P4 check entirely.
    """
    texto = (
        "artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, "
        "com a redação dada pela Emenda Constitucional nº 103/2019"
    )
    assert _enderecaveis(texto) == [("cf88", "art-40-par-1-inc-iii", "ec-103-2019")]


def test_clause_qualifier_is_kept_for_reporting() -> None:
    """The narrowing the frontmatter cannot carry stays visible, never discarded."""
    texto = "artigo 40, §1°, inciso III, segunda parte, da Constituição Federal"
    (citacao,) = extrair_citacoes(texto)
    assert citacao.qualificador == "segunda parte"


def test_citation_without_a_qualifier_has_none() -> None:
    """Most citations name the provision plainly; the field stays empty then."""
    (citacao,) = extrair_citacoes("artigo 2º da Lei Complementar nº 152/2015")
    assert citacao.qualificador is None


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


def test_last_inciso_of_a_list_is_joined_by_e_not_a_comma() -> None:
    """Regression, from regra-0014's real prose.

    "51, inciso I, II, III e VIII, alínea 'c'" — VIII is joined by "e", so it
    was missed and the alínea attached to inciso III, naming
    ``art-51-inc-iii-al-c``. Art. 51's inciso III is "com a emancipação" and
    has no alíneas at all: the address did not exist in the norm.
    """
    texto = 'artigos 51, inciso I, II, III e VIII, alínea "c", da Lei Complementar nº 1.100/2021'
    slugs = [slug for _, slug, _ in _enderecaveis(texto)]
    assert "art-51-inc-viii-al-c" in slugs
    assert "art-51-inc-iii-al-c" not in slugs
    assert "art-51-inc-iii" in slugs


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


def test_bare_quoted_letter_after_an_inciso_is_that_inciso_alinea() -> None:
    """regra-0012/0013 cite an alínea without the word: '32, I e II, "a", e § 1º'.

    Dropping it linked the whole inciso II — broader than the prose cites, the
    over-attribution mirror of the misattributions this reader exists to avoid.
    """
    texto = 'artigos 32, I e II, "a", e § 1º da Lei Complementar Estadual nº 432/2008'
    assert _enderecaveis(texto) == [
        ("lce-432-2008", "art-32-inc-i", None),
        ("lce-432-2008", "art-32-inc-ii-al-a", None),
        ("lce-432-2008", "art-32-par-1", None),
    ]


def test_quoted_letter_that_does_not_follow_an_inciso_is_not_an_alinea() -> None:
    """The rule needs an inciso right before it — otherwise it stays unread."""
    texto = 'artigo 32 da Lei Complementar Estadual nº 432/2008, na parte "a"'
    assert _enderecaveis(texto) == [("lce-432-2008", "art-32", None)]


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
    """An article with no owning norm resolves to nothing, instead of guessing."""
    texto = (
        "artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, no que tange à fórmula"
    )
    assert all(c.endereco_id is None for c in extrair_citacoes(texto))


def test_prose_with_no_citation_at_all_yields_nothing() -> None:
    """Descriptive text without an article citation claims no provision."""
    assert extrair_citacoes("Aposentadoria compulsória, com proventos proporcionais.") == []


def test_concatenated_field_tags_each_citation_with_its_segment() -> None:
    """Regra-0072's real field packs the homem and the mulher fundamentação.

    It is MASCULINO, yet the cell carries both alínea "a" (homem) and alínea
    "b" (mulher). Attributing both to the regra would ground a masculine rule
    on the provision governing the feminine one — so each citation says which
    segment it came from, and how many the field has.
    """
    texto = (
        'artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 - homem'
        ' | artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 - mulher'
    )
    citacoes = extrair_citacoes(texto)

    assert [(c.segmento, c.segmentos, c.endereco_id) for c in citacoes] == [
        (0, 2, "lc-51-1985/art-1-inc-ii-al-a"),
        (1, 2, "lc-51-1985/art-1-inc-ii-al-b"),
    ]


def test_single_fundamentacao_reports_one_segment() -> None:
    """The ordinary case: one fundamentação per field."""
    (citacao,) = extrair_citacoes("artigo 2º da Lei Complementar nº 152/2015")
    assert (citacao.segmento, citacao.segmentos) == (0, 1)


def test_citacao_is_frozen() -> None:
    """Citações are evidence, not mutable state."""
    (citacao,) = extrair_citacoes("artigo 2º da Lei Complementar nº 152/2015")
    assert isinstance(citacao, Citacao)
    # Called through __setattr__ so the check is the runtime one a caller
    # would actually hit, not a static assignment the type checker rejects.
    with pytest.raises(dataclasses.FrozenInstanceError):
        citacao.__setattr__("norma", "outra")


def test_abbreviated_article_spelling_is_read() -> None:
    """`Art. 40` is the spelling of the 17 oldest regras, and it was invisible.

    Reading only `artigo`/`artigos` made ``extrair_citacoes`` return *nothing*
    for every regra imported with the abbreviated form — so their P4 gap was
    reported as zero rather than as a gap. Each shape below is copied from a
    real ``FUNDAMENTACAO*`` field.
    """
    assert _enderecaveis("Art. 40, inciso I da Constituição Federal de 1988 em seu texto original") == [
        ("cf88", "art-40-inc-i", None)
    ]
    assert _enderecaveis("Art 40, §1º, I, da CF com redação da EC 20/98") == [
        ("cf88", "art-40-par-1-inc-i", "ec-20-1998")
    ]
    assert _enderecaveis("art. 40, § 5º da Constituição Federal") == [("cf88", "art-40-par-5", None)]


def test_abbreviation_never_starts_inside_a_word() -> None:
    """Words like "quarto" carry the letters of `art` but name no article."""
    assert extrair_citacoes("no quarto trimestre, parte final da Constituição Federal") == []


def test_amendment_cited_without_its_year_is_the_owning_norm() -> None:
    """regra-0010 writes "da EC nº 41 com redação EC nº 70/12".

    Federal amendments run in one national series, so the number alone names
    the norm. Not reading it cost two errors at once: art. 6º-A fell through
    to EC 70/2012 — which is only its *wording* — and the bare "41" was then
    read as an article of its own.
    """
    texto = "art. 6º-A § -unico da EC nº 41 com redação EC nº 70/12"
    assert _enderecaveis(texto) == [("ec-41-2003", "art-6a", "ec-70-2012")]


def test_state_amendment_without_a_number_never_falls_through_to_the_federal_one() -> None:
    """regra-0093/0094's field ends "da Emenda à Constituição Estadual - CF".

    The number was truncated away by the import. Attributing art. 4º to the
    next norm named — the federal Constitution — would put a *state*
    amendment's provision in CF/88. It has to come out unaddressable instead.
    """
    texto = (
        'artigo 40, §1º, inciso III, alínea "a", da Constituição Federal,'
        " art. 4° da Emenda à Constituição Estadual - CF"
    )
    assert ("cf88", "art-4", None) not in _enderecaveis(texto)
    assert SituacaoCitacao.SEM_NORMA in _situacoes(texto)


def test_state_amendment_with_its_number_still_reads_normally() -> None:
    """The barrier above must never swallow the spelling that *is* identified."""
    assert _enderecaveis("artigo 4º da Emenda à Constituição Estadual nº 146/2021") == [
        ("ece-146-2021", "art-4", None)
    ]


def test_roman_numeral_straight_after_a_paragraph_is_its_inciso() -> None:
    """regra-0010 writes "art. 40 § 7º II" with no punctuation between them.

    Without this the citation silently widened to the whole § 7º, which is a
    different provision from its inciso II.
    """
    assert _enderecaveis("art. 40 § 7º II da CF/88") == [("cf88", "art-40-par-7-inc-ii", None)]
