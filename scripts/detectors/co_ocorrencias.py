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

from detections import Detection, fingerprint
from regra_schema import BODY_HEADINGS

if TYPE_CHECKING:
    from collections.abc import Mapping

    from bundle import Bundle

VERSION = 1
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
    """One per-regra informative occurrence."""
    return Detection(
        detector=detector,
        fingerprint=fingerprint(detector, VERSION, regra_id),
        regras=frozenset({regra_id}),
        evidencia=evidencia,
        requires_achado=False,
    )


def detect_integral_sem_fundamentacao(bundle: Bundle) -> list[Detection]:
    """E5: INTEGRAL=N com FUNDAMENTACAO_PROPORCIONAL vazia (relação depende de Q6/Q7)."""
    return [
        _occurrence(INTEGRAL_DETECTOR_ID, regra.id, {"regra": regra.id})
        for regra in bundle.active_regras()
        if regra.frontmatter.get("integral") == "N"
        and not regra.sections.get(_FUNDAMENTACAO_PROPORCIONAL_HEADING, "").strip()
    ]


def detect_campos_vazios(bundle: Bundle) -> list[Detection]:
    """E3/E4: SEXO vazio + INTEGRAL vazio + TIPO_CALCULO="Não identificado" (semântica em Q10)."""
    return [
        _occurrence(VAZIOS_DETECTOR_ID, regra.id, {"regra": regra.id})
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
            detections.append(_occurrence(SEXO_DETECTOR_ID, regra.id, {"regra": regra.id, "sexo": sexo}))
    return detections
