"""P4 camada 2 — telling "not transcribed yet" apart from "never existed".

Synthetic fixtures throughout, for the same reason as the sibling detector's
tests: what is pinned down here is the *derivation* (do the authored wordings
exhaust the norm's life?), not the reading of real corpus prose, which
``tests/test_citacoes.py`` covers.

The negative tests carry the weight. This detector's output is an accusation
that a regra cites a wording that never existed, so every path where the
bundle cannot actually prove that must stay silent — a false accusation here
is worse than the invisible gap it replaces.
"""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

import yaml
from bundle import Bundle, Regra
from detectors.redacao_inexistente import DETECTOR_ID, detect
from dispositivo_schema import Dispositivo, historico_completo
from regra_schema import blank_frontmatter

if TYPE_CHECKING:
    from pathlib import Path

# "com redação dada pela LCE 949/2017" is what makes the citation name a
# wording at all — without the clause there is nothing to prove absent.
_FUNDAMENTACAO = (
    "com fundamento no artigo 62 da Lei Complementar Estadual nº 432/2008, "
    "com redação dada pela Lei Complementar Estadual nº 949/2017."
)

_VIDA_DA_NORMA = (datetime.date(2008, 3, 13), datetime.date(2021, 10, 18))


def _regra(regra_id: str = "regra-0001", *, fundamentacao: str = _FUNDAMENTACAO) -> Regra:
    fm = blank_frontmatter()
    fm["nome"] = f"Regra {regra_id}"
    fm["fundamentacao_integral"] = fundamentacao
    return Regra(doc_id=regra_id, frontmatter=fm)


def _write_norma(
    dispositivos_dir: Path,
    norma: str = "lce-432-2008",
    *,
    inicio: str | None = "2008-03-13",
    fim: str | None = "2021-10-18",
) -> None:
    fm: dict[str, object] = {
        "type": "Norma",
        "id": norma,
        "nome": f"Norma {norma}",
        "apelido": norma,
    }
    if inicio is not None:
        fm["vigencia_inicio"] = inicio
    if fim is not None:
        fm["vigencia_fim"] = fim
    fm["fontes"] = ["https://example.invalid/x"]
    caminho = dispositivos_dir / norma / "norma.md"
    caminho.parent.mkdir(parents=True, exist_ok=True)
    texto = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    caminho.write_text(f"---\n{texto}---\n\n# {norma}\n", encoding="utf-8")


def _write_dispositivo(
    dispositivos_dir: Path,
    doc_id: str = "lce-432-2008/art-62/original",
    *,
    inicio: str | None = "2008-03-13",
    fim: str | None = "2021-10-18",
) -> None:
    norma, endereco, redacao = doc_id.split("/")
    fm: dict[str, object] = {
        "type": "Dispositivo",
        "id": doc_id,
        "norma": norma,
        "componentes": [{"tipo": "artigo", "valor": "62"}],
    }
    if redacao != "original":
        fm["redacao_dada_por"] = redacao
    if inicio is not None:
        fm["vigencia_inicio"] = inicio
    if fim is not None:
        fm["vigencia_fim"] = fim
    fm["fontes"] = ["https://example.invalid/x"]
    caminho = dispositivos_dir / norma / endereco / f"{redacao}.md"
    caminho.parent.mkdir(parents=True, exist_ok=True)
    texto = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    caminho.write_text(f"---\n{texto}---\n\nTexto de teste.\n", encoding="utf-8")


def _bundle(dispositivos_dir: Path, *, regras: list[Regra] | None = None) -> Bundle:
    return Bundle(
        regras=tuple(regras if regras is not None else [_regra()]), dispositivos_dir=dispositivos_dir
    )


def test_wording_outside_a_complete_history_is_reported(tmp_path: Path) -> None:
    """The one wording on file covers the norm's whole life — no room for another."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path)

    (detection,) = detect(_bundle(tmp_path))

    assert detection.detector == DETECTOR_ID
    assert detection.requires_achado
    assert detection.evidencia["dispositivo"] == "lce-432-2008/art-62"
    assert detection.evidencia["redacao_citada"] == "lce-949-2017"
    assert detection.evidencia["redacoes_existentes"] == ["original"]


def test_the_cited_wording_itself_is_never_reported(tmp_path: Path) -> None:
    """If the wording is on file, there is nothing to prove absent."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path, inicio="2008-03-13", fim="2017-07-16")
    _write_dispositivo(
        tmp_path,
        "lce-432-2008/art-62/lce-949-2017",
        inicio="2017-07-17",
        fim="2021-10-18",
    )

    assert detect(_bundle(tmp_path)) == []


def test_norm_without_a_declared_window_never_concludes(tmp_path: Path) -> None:
    """No norm life, no tiling — the absence stays a transcription queue item."""
    _write_norma(tmp_path, inicio=None, fim=None)
    _write_dispositivo(tmp_path)

    assert detect(_bundle(tmp_path)) == []


def test_wording_missing_a_date_never_concludes(tmp_path: Path) -> None:
    """One undated wording and the tiling is fiction — declining is the safe answer."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path, inicio=None, fim=None)

    assert detect(_bundle(tmp_path)) == []


def test_history_that_starts_after_the_norm_never_concludes(tmp_path: Path) -> None:
    """A hole before the first authored wording is exactly where the cited one could live."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path, inicio="2012-08-09", fim="2021-10-18")

    assert detect(_bundle(tmp_path)) == []


def test_citation_with_no_wording_clause_is_not_this_detector_business(tmp_path: Path) -> None:
    """Prose that names no wording makes no claim this detector can refute."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path)
    regra = _regra(fundamentacao="com fundamento no artigo 62 da Lei Complementar Estadual nº 432/2008.")

    assert detect(_bundle(tmp_path, regras=[regra])) == []


def test_one_occurrence_per_regra_even_when_two_fields_cite_it(tmp_path: Path) -> None:
    """The same false citation in two fundamentação fields is one fact, not two."""
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path)
    regra = _regra()
    regra.frontmatter["fundamentacao_proporcional"] = _FUNDAMENTACAO

    assert len(detect(_bundle(tmp_path, regras=[regra]))) == 1


def test_fingerprint_survives_transcribing_an_unrelated_provision(tmp_path: Path) -> None:
    """The fingerprint is the fact itself, so an achado keeps reading as reproduced.

    This is the deliberate difference from P4_CITACAO_NAO_VINCULADA, whose
    fingerprint bakes in the regra's whole gap and therefore moves on every
    linking batch (achado-0011 explains why that one is left as is).
    """
    _write_norma(tmp_path)
    _write_dispositivo(tmp_path)
    (antes,) = detect(_bundle(tmp_path))

    _write_dispositivo(tmp_path, "lce-432-2008/art-17/original")
    (depois,) = detect(_bundle(tmp_path))

    assert antes.fingerprint == depois.fingerprint


def test_historico_completo_rejects_a_one_day_gap() -> None:
    """Contiguity is exact: a single uncovered day is somewhere a wording could be."""
    completo = [
        _janela("2008-03-13", "2017-07-16"),
        _janela("2017-07-17", "2021-10-18", redacao="lce-949-2017"),
    ]
    com_buraco = [
        _janela("2008-03-13", "2017-07-16"),
        _janela("2017-07-18", "2021-10-18", redacao="lce-949-2017"),
    ]
    assert historico_completo(completo, _VIDA_DA_NORMA)
    assert not historico_completo(com_buraco, _VIDA_DA_NORMA)


def test_historico_completo_requires_an_open_last_wording_for_a_living_norm() -> None:
    """A norm still in force cannot have its last wording already ended."""
    fechada = [_janela("1988-10-05", "2019-11-12")]
    aberta = [_janela("1988-10-05", None)]
    viva = (datetime.date(1988, 10, 5), None)
    assert not historico_completo(fechada, viva)
    assert historico_completo(aberta, viva)


def test_historico_completo_is_false_for_no_wordings_at_all() -> None:
    """Nothing transcribed proves nothing — the empty set is not a complete history."""
    assert not historico_completo([], _VIDA_DA_NORMA)


def _janela(inicio: str | None, fim: str | None, *, redacao: str = "original") -> Dispositivo:
    """A real Dispositivo carrying only the window — the function reads its contract."""
    doc_id = f"lce-432-2008/art-62/{redacao}"
    fm: dict[str, object] = {
        "type": "Dispositivo",
        "id": doc_id,
        "norma": "lce-432-2008",
        "componentes": [{"tipo": "artigo", "valor": "62"}],
    }
    if redacao != "original":
        fm["redacao_dada_por"] = redacao
    if inicio is not None:
        fm["vigencia_inicio"] = inicio
    if fim is not None:
        fm["vigencia_fim"] = fim
    fm["fontes"] = ["https://example.invalid/x"]
    return Dispositivo(doc_id=doc_id, frontmatter=fm, body="Texto de teste.")
