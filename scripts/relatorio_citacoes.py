"""Read-only report on the gap between cited fundamentação and linked ``dispositivos:`` (P4).

``validar_regras.py`` answers "is the bundle valid?"; this answers "how far
is the P3 linking, and what is in the way?". It writes nothing — the queues
it prints are work for a human, and printing them is the whole point:
without this, "0 of 112 regras linked" is a fact nobody can act on, because
the reason differs per provision.

Two queues come out of it, both ordered by how many regras are waiting on
each item, so the highest-leverage work is at the top:

- **transcrever** — provisions the prose cites that have no dispositivo yet.
  Each one unblocks every regra citing it.
- **vincular** — provisions already transcribed and already cited, waiting
  only for the auditor to declare the link.
- **transcrever (redação)** — the provision exists but not in the wording the
  prose names. A provision-level count calls these "linked"; they are not,
  and linking any other wording would ground the regra on a text that was
  not in force for it.

Run as ``uv run python scripts/relatorio_citacoes.py [--bundle PATH] [--json]``.
"""

from __future__ import annotations

import argparse
import collections
import json
import logging
from pathlib import Path
from typing import TypedDict

from bundle import Bundle
from detectors.citacao_nao_vinculada import DETECTOR_ID, detect
from okf_common import DEFAULT_BUNDLE

logger = logging.getLogger(__name__)


class ItemDaFila(TypedDict):
    """One provision waiting on work, and how many regras wait with it."""

    dispositivo: str
    regras: int


class ResumoDeCitacoes(TypedDict):
    """The coverage summary plus both work queues, ordered by leverage."""

    regras: int
    regras_com_lacuna: int
    regras_com_dispositivos: int
    transcrever: list[ItemDaFila]
    vincular: list[ItemDaFila]
    redacao_ausente: list[ItemDaFila]
    prosa_multipla: list[ItemDaFila]
    nao_enderecaveis: dict[str, int]
    com_qualificador: list[ItemDaFila]


def levantar(bundle: Bundle) -> ResumoDeCitacoes:
    """Return the citation-coverage summary and both work queues."""
    detections = [d for d in detect(bundle) if d.detector == DETECTOR_ID]

    transcrever: collections.Counter[str] = collections.Counter()
    vincular: collections.Counter[str] = collections.Counter()
    nao_enderecaveis: collections.Counter[str] = collections.Counter()
    com_qualificador: collections.Counter[str] = collections.Counter()
    redacao_ausente: collections.Counter[str] = collections.Counter()
    prosa_multipla: collections.Counter[str] = collections.Counter()

    # Detection.evidencia is a Mapping[str, object] by design (each detector
    # carries a different shape), so the reads below narrow it here rather
    # than making every detector share one payload type.
    for detection in detections:
        for chave, fila in (
            ("sem_dispositivo", transcrever),
            ("nao_vinculadas", vincular),
            ("com_qualificador", com_qualificador),
            ("redacao_ausente", redacao_ausente),
            ("prosa_multipla", prosa_multipla),
        ):
            enderecos = detection.evidencia.get(chave)
            if isinstance(enderecos, list):
                fila.update(str(endereco) for endereco in enderecos)
        motivos = detection.evidencia.get("nao_enderecaveis")
        if isinstance(motivos, dict):
            for motivo, quantas in motivos.items():
                if isinstance(quantas, int):
                    nao_enderecaveis[str(motivo)] += quantas

    return {
        "regras": len(bundle.regras),
        "regras_com_lacuna": len(detections),
        "regras_com_dispositivos": sum(1 for r in bundle.regras if r.dispositivos),
        "transcrever": [{"dispositivo": k, "regras": v} for k, v in transcrever.most_common()],
        "vincular": [{"dispositivo": k, "regras": v} for k, v in vincular.most_common()],
        "redacao_ausente": [{"dispositivo": k, "regras": v} for k, v in redacao_ausente.most_common()],
        "prosa_multipla": [{"dispositivo": k, "regras": v} for k, v in prosa_multipla.most_common()],
        "nao_enderecaveis": dict(nao_enderecaveis.most_common()),
        "com_qualificador": [{"dispositivo": k, "regras": v} for k, v in com_qualificador.most_common()],
    }


def _render(resumo: ResumoDeCitacoes) -> str:
    """Render the summary as plain text."""
    linhas = [
        f"Regras: {resumo['regras']}",
        f"  com dispositivos: vinculados : {resumo['regras_com_dispositivos']}",
        f"  com alguma lacuna de citação  : {resumo['regras_com_lacuna']}",
        "",
        "Fila TRANSCREVER (citado, sem dispositivo autorado) — cada item destrava N regras:",
    ]
    linhas += [f"  {i['regras']:4d}  {i['dispositivo']}" for i in resumo["transcrever"]] or ["  (vazia)"]
    linhas += ["", "Fila VINCULAR (dispositivo existe e é citado, falta declarar):"]
    linhas += [f"  {i['regras']:4d}  {i['dispositivo']}" for i in resumo["vincular"]] or ["  (vazia)"]
    linhas += [
        "",
        "Fila TRANSCREVER — REDAÇÃO (a provisão existe, a redação citada não):",
    ]
    linhas += [f"  {i['regras']:4d}  {i['dispositivo']}" for i in resumo["redacao_ausente"]] or ["  (vazia)"]
    linhas += [
        "",
        "Citadas em campo com mais de uma fundamentação (`|`) — precisam ser",
        "separadas por um humano antes de virar vínculo:",
    ]
    linhas += [f"  {i['regras']:4d}  {i['dispositivo']}" for i in resumo["prosa_multipla"]] or ["  (nenhuma)"]
    linhas += ["", "Citações que exigem leitura humana (não endereçáveis mecanicamente):"]
    linhas += [f"  {v:4d}  {k}" for k, v in resumo["nao_enderecaveis"].items()] or ["  (nenhuma)"]
    linhas += [
        "",
        "Vinculadas à provisão inteira, com a prosa estreitando a cláusula",
        "(resolução que o frontmatter não carrega — a prosa carrega):",
    ]
    linhas += [f"  {i['regras']:4d}  {i['dispositivo']}" for i in resumo["com_qualificador"]] or [
        "  (nenhuma)"
    ]
    return "\n".join(linhas)


def main() -> None:
    """CLI entry point: print the citation-coverage report for --bundle."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    resumo = levantar(Bundle.load(args.bundle))
    logger.info("%s", json.dumps(resumo, ensure_ascii=False, indent=2) if args.json else _render(resumo))


if __name__ == "__main__":
    main()
