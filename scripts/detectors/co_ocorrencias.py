"""P9 detectors — co-ocorrências entre campos (RFC 0001, P9; camada 3).

Each detector reports a **co-occurrence of values**, one Detection per regra,
always informative (``requires_achado=False``): the *obligatory* relation
between the fields only exists once P13.2 confirms each field's meaning
(Q6/Q7/Q10). Until then the detector points at the pattern; it never asserts
incoherence, never forces an achado, and never blocks the CI.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from detections import Detection, canonical_json, fingerprint
from regra_schema import BODY_HEADINGS

if TYPE_CHECKING:
    from collections.abc import Mapping

    from bundle import Bundle

VERSION = 2  # v2: fingerprint now incorporates the mechanical evidencia, not just regra_id
INTEGRAL_DETECTOR_ID = "P9_INTEGRAL_SEM_FUNDAMENTACAO"
VAZIOS_DETECTOR_ID = "P9_CAMPOS_VAZIOS_PENDENTES"
SEXO_DETECTOR_ID = "P9_SEXO_FUNDAMENTACAO"

# bundle.Regra.sections is keyed by the raw "# Heading" text, not the CSV
# column name — BODY_HEADINGS (P13.2) is the single source for that mapping.
_FUNDAMENTACAO_PROPORCIONAL_HEADING = BODY_HEADINGS["FUNDAMENTACAO_PROPORCIONAL"]
_FUNDAMENTACAO_HEADINGS = (
    BODY_HEADINGS["FUNDAMENTACAO_PROPORCIONAL"],
    BODY_HEADINGS["FUNDAMENTACAO_INTEGRAL"],
    BODY_HEADINGS["FUNDAMENTACAO"],
)
_MULHER_RE = re.compile(r"\bmulher\b", re.IGNORECASE)
_HOMEM_RE = re.compile(r"\bhomem\b", re.IGNORECASE)


def _occurrence(detector: str, regra_id: str, evidencia: Mapping[str, object]) -> Detection:
    """One per-regra informative occurrence.

    The fingerprint bakes in ``evidencia``, not just ``regra_id`` — if the
    regra changes such that the same detector fires again but for a
    materially different reason (e.g. E7's SEXO/mention direction flipping),
    the fingerprint must change too, or the CI would treat the new
    occurrence as "still reproduced" by a stale achado.
    """
    canonical_subject = canonical_json({"regra": regra_id, "evidencia": dict(evidencia)})
    return Detection(
        detector=detector,
        fingerprint=fingerprint(detector, VERSION, canonical_subject),
        regras=frozenset({regra_id}),
        evidencia=evidencia,
        requires_achado=False,
    )


def detect_integral_sem_fundamentacao(bundle: Bundle) -> list[Detection]:
    """E5: INTEGRAL=N com FUNDAMENTACAO_PROPORCIONAL vazia (relação depende de Q6/Q7)."""
    detections: list[Detection] = []
    for regra in bundle.active_regras():
        fundamentacao = regra.sections.get(_FUNDAMENTACAO_PROPORCIONAL_HEADING, "")
        if regra.frontmatter.get("integral") == "N" and not fundamentacao.strip():
            evidencia = {
                "integral": regra.frontmatter.get("integral"),
                "fundamentacao_proporcional": fundamentacao,
            }
            detections.append(_occurrence(INTEGRAL_DETECTOR_ID, regra.id, evidencia))
    return detections


def detect_campos_vazios(bundle: Bundle) -> list[Detection]:
    """E3/E4: SEXO vazio + INTEGRAL vazio + TIPO_CALCULO="Não identificado" (semântica em Q10)."""
    return [
        _occurrence(
            VAZIOS_DETECTOR_ID,
            regra.id,
            {
                "sexo": regra.frontmatter.get("sexo"),
                "integral": regra.frontmatter.get("integral"),
                "tipo_calculo": regra.frontmatter.get("tipo_calculo"),
            },
        )
        for regra in bundle.active_regras()
        if not regra.frontmatter.get("sexo")
        and not regra.frontmatter.get("integral")
        and regra.frontmatter.get("tipo_calculo") == "Não identificado"
    ]


def detect_sexo_fundamentacao(bundle: Bundle) -> list[Detection]:
    """E7 (híbrido): SEXO de um único gênero cuja fundamentação só menciona o outro."""
    detections: list[Detection] = []
    for regra in bundle.active_regras():
        sexo = regra.frontmatter.get("sexo")
        text = " ".join(regra.sections.get(heading, "") for heading in _FUNDAMENTACAO_HEADINGS)
        has_mulher = bool(_MULHER_RE.search(text))
        has_homem = bool(_HOMEM_RE.search(text))
        if (sexo == "MASCULINO" and has_mulher and not has_homem) or (
            sexo == "FEMININO" and has_homem and not has_mulher
        ):
            evidencia = {"sexo": sexo, "has_mulher": has_mulher, "has_homem": has_homem}
            detections.append(_occurrence(SEXO_DETECTOR_ID, regra.id, evidencia))
    return detections
