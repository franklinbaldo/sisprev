"""P4 detector — a regra citing a wording that never existed (camada 2).

``citacao_nao_vinculada`` already reports, as ``redacao_ausente``, that a
regra names a wording no dispositivo carries. That report cannot tell two
opposite situations apart:

- the wording exists and simply has not been transcribed yet — a queue item;
- the wording **never existed** — a false legal citation in a field the
  Sisprev deploys into the servidor's own document.

This detector separates them, using nothing but what the bundle already
records. When the authored wordings of a provision tile the owning norm's
entire life with no gap (``dispositivo_schema.historico_completo``), there is
no room left for another one, and a citation naming a wording outside that
set is provably a misattribution rather than a pending transcription.

It is **camada 2** (``requires_achado=True``): a citation that names a norm
which never gave the provision its wording is a defect in a deployable
field, and CI blocks until a human registers the achado. That is what the
achados 0011/0012/0013 are — each found by hand, by going to check why one
link would not close. This is that check, run on every commit.

The fingerprint is deliberately **narrow**: the regra, the address and the
wording it asks for, nothing else. Unlike ``citacao_nao_vinculada``, whose
fingerprint bakes in the regra's whole gap and therefore moves on every
linking batch (see achado-0011 for why that one is left unfixed), this
occurrence is a single stable fact — and an achado about it must keep
reading as "still reproduced" while the prose stays as it is.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from citacoes import SituacaoCitacao
from detections import Detection, canonical_json, fingerprint
from detectors.citacao_nao_vinculada import citacoes_da_regra
from dispositivo_schema import historico_completo

if TYPE_CHECKING:
    from bundle import Bundle
    from dispositivo_schema import Dispositivo

DETECTOR_ID = "P4_REDACAO_INEXISTENTE"
VERSION = 1

TESTS = ("tests/test_detector_redacao_inexistente.py",)


def enderecos_com_historico_completo(bundle: Bundle) -> dict[str, frozenset[str]]:
    """Return, per provision address, the wordings that exhaust its history.

    An address is absent from the result whenever the bundle cannot prove
    exhaustiveness — the owning norm has no declared window, or one of the
    wordings is missing a date, or they leave a gap. Absent means "no
    conclusion", never "incomplete": the caller must not read a missing key
    as evidence of anything.
    """
    por_endereco: dict[str, list[Dispositivo]] = {}
    for dispositivo in bundle.dispositivos:
        por_endereco.setdefault(dispositivo.endereco_id, []).append(dispositivo)

    completos: dict[str, frozenset[str]] = {}
    for endereco_id, redacoes in por_endereco.items():
        norma = bundle.normas.get(endereco_id.split("/", 1)[0])
        janela = norma.janela if norma is not None else None
        if janela is None or not historico_completo(redacoes, janela):
            continue
        completos[endereco_id] = frozenset(d.doc_id.rsplit("/", 1)[1] for d in redacoes)
    return completos


def detect(bundle: Bundle) -> list[Detection]:
    """Report each regra citing a wording that a fully transcribed provision never had."""
    completos = enderecos_com_historico_completo(bundle)
    detections: list[Detection] = []
    vistos: set[tuple[str, str, str]] = set()

    for regra in bundle.regras:
        for citacao in citacoes_da_regra(regra):
            if citacao.situacao is not SituacaoCitacao.ENDERECAVEL or citacao.redacao is None:
                continue
            endereco = citacao.endereco_id
            if endereco is None:
                continue
            autoradas = completos.get(endereco)
            if autoradas is None or citacao.redacao in autoradas:
                continue
            # The same citation can appear in more than one fundamentação
            # field of the same regra; it is one occurrence, not two.
            chave = (regra.doc_id, endereco, citacao.redacao)
            if chave in vistos:
                continue
            vistos.add(chave)
            evidencia = {
                "regra": regra.doc_id,
                "dispositivo": endereco,
                "redacao_citada": citacao.redacao,
                "redacoes_existentes": sorted(autoradas),
            }
            detections.append(
                Detection(
                    detector=DETECTOR_ID,
                    fingerprint=fingerprint(
                        DETECTOR_ID,
                        VERSION,
                        canonical_json(
                            {
                                "regra": regra.doc_id,
                                "dispositivo": endereco,
                                "redacao_citada": citacao.redacao,
                            }
                        ),
                    ),
                    regras=frozenset({regra.doc_id}),
                    evidencia=evidencia,
                    requires_achado=True,
                ),
            )
    return detections
