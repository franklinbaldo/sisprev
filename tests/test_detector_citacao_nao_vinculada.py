"""P4 detector — the gap between what a regra cites in prose and what it links.

Synthetic fixtures throughout: the detector's job is to *compare* two sides,
and that comparison is what these tests pin down. The reading of real corpus
prose is covered by ``tests/test_citacoes.py``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import yaml
from bundle import Bundle, Regra
from detectors.citacao_nao_vinculada import DETECTOR_ID, detect
from regra_schema import blank_frontmatter

if TYPE_CHECKING:
    from pathlib import Path

_FUNDAMENTACAO = "com base no artigo 2º da Lei Complementar nº 152/2015."

# Fixtures need the componentes to match the address in the path, since the
# path is derived from them (P3). Only the shapes these tests exercise.
_COMPONENTES: dict[str, list[dict[str, str]]] = {
    "art-40-par-1-inc-iii": [
        {"tipo": "artigo", "valor": "40"},
        {"tipo": "paragrafo", "valor": "1"},
        {"tipo": "inciso", "valor": "III"},
    ],
}


def _regra(regra_id: str, *, fundamentacao: str = "", dispositivos: list[str] | None = None) -> Regra:
    fm = blank_frontmatter()
    fm["nome"] = f"Regra {regra_id}"
    fm["fundamentacao_integral"] = fundamentacao
    if dispositivos is not None:
        fm["dispositivos"] = dispositivos
    return Regra(doc_id=regra_id, frontmatter=fm)


def _write_dispositivo(dispositivos_dir: Path, doc_id: str) -> None:
    norma, endereco, redacao = doc_id.split("/")
    fm = {
        "type": "Dispositivo",
        "id": doc_id,
        "norma": norma,
        "componentes": _COMPONENTES.get(endereco, [{"tipo": "artigo", "valor": "2"}]),
        "fontes": ["https://example.invalid/x"],
    }
    if redacao != "original":
        fm["redacao_dada_por"] = redacao
    caminho = dispositivos_dir / norma / endereco / f"{redacao}.md"
    caminho.parent.mkdir(parents=True, exist_ok=True)
    texto = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    caminho.write_text(f"---\n{texto}---\n\nTexto de teste.\n", encoding="utf-8")


def _bundle(regras: list[Regra], dispositivos_dir: Path) -> Bundle:
    return Bundle(regras=tuple(regras), dispositivos_dir=dispositivos_dir)


def test_regra_with_no_fundamentacao_reports_nothing(tmp_path: Path) -> None:
    """No prose means no claim to compare against."""
    assert detect(_bundle([_regra("regra-0001")], tmp_path)) == []


def test_cited_and_authored_but_unlinked_is_the_auditor_queue(tmp_path: Path) -> None:
    """The provision exists and the prose names it — only the link is missing."""
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/original")
    bundle = _bundle([_regra("regra-0001", fundamentacao=_FUNDAMENTACAO)], tmp_path)

    (detection,) = detect(bundle)

    assert detection.detector == DETECTOR_ID
    assert detection.evidencia["nao_vinculadas"] == ["lc-152-2015/art-2"]
    assert detection.evidencia["sem_dispositivo"] == []


def test_cited_but_never_transcribed_is_the_transcription_queue(tmp_path: Path) -> None:
    """Nothing to link to yet — the reason the linking cannot just be run to completion."""
    bundle = _bundle([_regra("regra-0001", fundamentacao=_FUNDAMENTACAO)], tmp_path)

    (detection,) = detect(bundle)

    assert detection.evidencia["sem_dispositivo"] == ["lc-152-2015/art-2"]
    assert detection.evidencia["nao_vinculadas"] == []


def test_linked_provision_closes_the_gap(tmp_path: Path) -> None:
    """Once the auditor declares the link, the detection stops reporting it."""
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/original")
    bundle = _bundle(
        [
            _regra(
                "regra-0001",
                fundamentacao=_FUNDAMENTACAO,
                dispositivos=["/dispositivos/lc-152-2015/art-2/original.md"],
            )
        ],
        tmp_path,
    )

    assert detect(bundle) == []


def test_any_wording_of_the_cited_provision_answers_the_citation(tmp_path: Path) -> None:
    """The comparison is at provision granularity, not wording.

    Which wording grounds the regra is P3's question; this detector only asks
    whether the provision the prose names was declared at all.
    """
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/original")
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/lei-outra")
    bundle = _bundle(
        [
            _regra(
                "regra-0001",
                fundamentacao=_FUNDAMENTACAO,
                dispositivos=["/dispositivos/lc-152-2015/art-2/lei-outra.md"],
            )
        ],
        tmp_path,
    )

    assert detect(bundle) == []


def test_clause_qualifier_is_linked_and_still_counted(tmp_path: Path) -> None:
    """A narrowed citation links to the whole provision, and the narrowing stays visible.

    Two things have to be true at once: the provision enters the linking
    queue like any other, and the clause the prose singled out is reported —
    the resolution `dispositivos:` cannot carry is a stated cost, not a
    silent one.
    """
    _write_dispositivo(tmp_path, "cf88/art-40-par-1-inc-iii/ec-103-2019")
    texto = (
        "artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, "
        "com a redação dada pela Emenda Constitucional nº 103/2019"
    )
    bundle = _bundle([_regra("regra-0001", fundamentacao=texto)], tmp_path)

    (detection,) = detect(bundle)

    assert detection.evidencia["nao_vinculadas"] == ["cf88/art-40-par-1-inc-iii"]
    assert detection.evidencia["com_qualificador"] == ["cf88/art-40-par-1-inc-iii (segunda parte)"]
    assert detection.evidencia["nao_enderecaveis"] == {}


def test_cited_wording_that_was_never_transcribed_is_its_own_queue(tmp_path: Path) -> None:
    """The provision exists, the wording the prose names does not.

    Linking the wording that *does* exist would ground the regra on a text
    that was not in force for it — so this is a transcription gap, and one a
    provision-level comparison reports as "already linked".
    """
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/original")
    texto = (
        "artigo 2º da Lei Complementar nº 152/2015, com redação dada pela Emenda Constitucional nº 103/2019"
    )
    bundle = _bundle([_regra("regra-0001", fundamentacao=texto)], tmp_path)

    (detection,) = detect(bundle)

    assert detection.evidencia["redacao_ausente"] == ["lc-152-2015/art-2/ec-103-2019"]
    assert detection.evidencia["nao_vinculadas"] == []


def test_detection_never_forces_an_achado(tmp_path: Path) -> None:
    """Camada 3: reading prose is evidence, never a conclusion that blocks the CI."""
    bundle = _bundle([_regra("regra-0001", fundamentacao=_FUNDAMENTACAO)], tmp_path)
    (detection,) = detect(bundle)
    assert detection.requires_achado is False


def test_fingerprint_changes_when_the_gap_changes(tmp_path: Path) -> None:
    """Linking one provision must not leave an old achado looking still-reproduced."""
    _write_dispositivo(tmp_path, "lc-152-2015/art-2/original")
    texto = "artigo 2º da Lei Complementar nº 152/2015 e artigo 40 da Constituição Federal"
    antes = detect(_bundle([_regra("regra-0001", fundamentacao=texto)], tmp_path))
    depois = detect(
        _bundle(
            [
                _regra(
                    "regra-0001",
                    fundamentacao=texto,
                    dispositivos=["/dispositivos/lc-152-2015/art-2/original.md"],
                )
            ],
            tmp_path,
        )
    )

    assert antes[0].fingerprint != depois[0].fingerprint


def test_each_regra_gets_its_own_detection(tmp_path: Path) -> None:
    """The gap is per regra, so the auditor can work through them one at a time."""
    bundle = _bundle(
        [
            _regra("regra-0001", fundamentacao=_FUNDAMENTACAO),
            _regra("regra-0002", fundamentacao=_FUNDAMENTACAO),
        ],
        tmp_path,
    )

    detections = detect(bundle)

    assert {next(iter(d.regras)) for d in detections} == {"regra-0001", "regra-0002"}
