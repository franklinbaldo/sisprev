"""P1 detector — nome repetido entre regras ativas (RFC 0001, P1; camada 3).

Reports groups of 2+ active regras sharing the same normalized ``nome``.
Informative only (``requires_achado=False``): a repeated name does not prove
the regras are equal (that is P2/E2) — only that the name alone does not
distinguish them. Never blocks the CI; the auditor decides whether to open
an achado.
"""

from __future__ import annotations

import re
import unicodedata
from typing import TYPE_CHECKING

from detections import Detection, canonical_json, fingerprint

if TYPE_CHECKING:
    from bundle import Bundle

DETECTOR_ID = "P1_NOME_REPETIDO"
VERSION = 2  # v2: fingerprint now incorporates nome_normalizado, not just ids
_MIN_GROUP_SIZE = 2


def _normalize(nome: str) -> str:
    """Case/accent/whitespace-insensitive form of a nome, for grouping."""
    ascii_nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", ascii_nome).strip().lower()


def detect(bundle: Bundle) -> list[Detection]:
    """Report each group of 2+ active regras with the same normalized nome."""
    groups: dict[str, list[str]] = {}
    for regra in bundle.active_regras():
        key = _normalize(str(regra.frontmatter.get("nome", "")))
        groups.setdefault(key, []).append(regra.id)

    detections: list[Detection] = []
    for nome_normalizado, regra_ids in groups.items():
        if len(regra_ids) < _MIN_GROUP_SIZE:
            continue
        sorted_ids = sorted(regra_ids)
        # The fingerprint bakes in nome_normalizado, not just the ids: two
        # regras keeping the same ids but drifting to a different shared
        # name must not reuse the old fingerprint (an achado documenting
        # the old name would otherwise look "still reproduced").
        canonical_subject = canonical_json({"regras": sorted_ids, "nome_normalizado": nome_normalizado})
        detections.append(
            Detection(
                detector=DETECTOR_ID,
                fingerprint=fingerprint(DETECTOR_ID, VERSION, canonical_subject),
                regras=frozenset(regra_ids),
                evidencia={"grupo": sorted_ids, "nome_normalizado": nome_normalizado},
                requires_achado=False,
            ),
        )
    return detections
