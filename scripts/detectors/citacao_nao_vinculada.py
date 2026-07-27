"""P4 detector — provisions the fundamentação cites but ``dispositivos:`` omits (camada 3).

RFC 0001's P4 makes ``dispositivos:`` the canonical, checkable statement of
what grounds a regra, and leaves ``FUNDAMENTACAO*`` as free prose for humans.
Nothing so far compared the two, so a regra could cite six provisions in
prose and declare none — which is the state all 112 are in today, invisibly.

This detector makes that gap a number. For each regra it reads the prose
(``citacoes.extrair_citacoes``), resolves each citation against the authored
dispositivos, and reports what is **cited but not linked**, split by why:

- ``nao_vinculadas`` — the provision is authored and the prose names it, but
  ``dispositivos:`` doesn't. This is the auditor's queue.
- ``sem_dispositivo`` — cited, but no such provision has been transcribed
  yet. This is the transcription queue, and it is why the linking cannot
  simply be run to completion today.
- ``redacao_ausente`` — the provision is authored, but not in the *wording*
  the prose names. Linking any other wording would ground the regra on a
  text that was not in force for it, so this is a transcription gap too —
  and one a provision-level count would miss entirely.
- ``sem_norma`` / ``endereco_invalido`` — the prose names no owning norm, or
  reads as an impossible address. These need a human reading, and saying so
  is the point: guessing the norm is what silently misattributes an article.
- ``com_qualificador`` — provisions whose citation narrows to a clause
  ("segunda parte"). They *are* linked, to the whole provision, because the
  qualifier names a clause inside one provision rather than another
  provision (see ``citacoes.Citacao.qualificador``). Counted here so the
  resolution the frontmatter does not carry stays a visible number.

Informative only (``requires_achado=False``). It reports a *reading of prose*
— strong evidence about what a regra claims, never a conclusion that the
regra is founded on it. Writing the link stays a human act (princípio da
autoria humana); this only stops the gap from being invisible.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from citacoes import Citacao, SituacaoCitacao, extrair_citacoes
from detections import Detection, canonical_json, fingerprint

if TYPE_CHECKING:
    from bundle import Bundle, Regra

DETECTOR_ID = "P4_CITACAO_NAO_VINCULADA"
VERSION = 1

TESTS = ("tests/test_detector_citacao_nao_vinculada.py",)

CAMPOS_FUNDAMENTACAO = ("fundamentacao", "fundamentacao_proporcional", "fundamentacao_integral")


def _citacoes_da_regra(regra: Regra) -> list[Citacao]:
    """Read every citation across the regra's three fundamentação fields."""
    citacoes: list[Citacao] = []
    for campo in CAMPOS_FUNDAMENTACAO:
        citacoes.extend(extrair_citacoes(str(regra.frontmatter.get(campo) or "")))
    return citacoes


def _vinculados(regra: Regra) -> set[str]:
    """Return the ``<norma>/<endereço>`` of every dispositivo the regra declares.

    Compared at *provision* granularity, not wording: a regra that links one
    wording of art. 40 § 1º I has answered the prose's citation of it. Which
    wording is right is a separate question, and P3's own checks own it.
    """
    return {
        ref.removeprefix("/dispositivos/").removesuffix(".md").rsplit("/", 1)[0] for ref in regra.dispositivos
    }


def _lacuna(
    citacoes: list[Citacao],
    declarados: set[str],
    redacoes: dict[str, set[str]],
    autorados: set[str],
) -> dict[str, object]:
    """Classify one regra's citations into the queues that describe its gap."""
    nao_vinculadas: set[str] = set()
    sem_dispositivo: set[str] = set()
    redacao_ausente: set[str] = set()
    com_qualificador: set[str] = set()
    nao_enderecaveis: dict[str, int] = {}

    for citacao in citacoes:
        if citacao.situacao is not SituacaoCitacao.ENDERECAVEL:
            chave = citacao.situacao.value
            nao_enderecaveis[chave] = nao_enderecaveis.get(chave, 0) + 1
            continue
        endereco = citacao.endereco_id
        if endereco is None:
            continue
        if citacao.qualificador is not None:
            com_qualificador.add(f"{endereco} ({citacao.qualificador})")
        if endereco not in autorados:
            sem_dispositivo.add(endereco)
        elif citacao.redacao is not None and citacao.redacao not in redacoes[endereco]:
            redacao_ausente.add(f"{endereco}/{citacao.redacao}")
        elif endereco not in declarados:
            nao_vinculadas.add(endereco)

    return {
        "nao_vinculadas": sorted(nao_vinculadas),
        "sem_dispositivo": sorted(sem_dispositivo),
        "redacao_ausente": sorted(redacao_ausente),
        "nao_enderecaveis": dict(sorted(nao_enderecaveis.items())),
        "com_qualificador": sorted(com_qualificador),
    }


def detect(bundle: Bundle) -> list[Detection]:
    """Report, per regra, the provisions its prose cites but its frontmatter omits."""
    redacoes: dict[str, set[str]] = {}
    for doc_id in bundle.dispositivo_ids():
        endereco, redacao = doc_id.rsplit("/", 1)
        redacoes.setdefault(endereco, set()).add(redacao)
    autorados = set(redacoes)
    detections: list[Detection] = []

    for regra in bundle.regras:
        citacoes = _citacoes_da_regra(regra)
        if not citacoes:
            continue

        evidencia = _lacuna(citacoes, _vinculados(regra), redacoes, autorados)
        if not any(evidencia.values()):
            continue

        # The fingerprint bakes in the gap itself, not just the regra id: once
        # the auditor links a provision, the occurrence is materially
        # different and must not keep an old achado looking "still reproduced".
        canonical = canonical_json({"regra": regra.doc_id, **evidencia})
        detections.append(
            Detection(
                detector=DETECTOR_ID,
                fingerprint=fingerprint(DETECTOR_ID, VERSION, canonical),
                regras=frozenset({regra.doc_id}),
                evidencia=evidencia,
                requires_achado=False,
            ),
        )
    return detections
