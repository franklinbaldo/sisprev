"""P1 detector — nome repetido entre TODAS as regras (RFC 0001, P1; camada 3).

Reports groups of 2+ regras sharing the same normalized ``nome`` — over
*every* regra, active or inactive. The RFC is explicit: "detecção de nome
repetido ... sobre todos os regra-*.md" and "a unicidade global de nome é
uma meta de revisada" — an inactive regra sharing a name with an active one
is exactly the collision P1 exists to catch; excluding inactive regras
would let an active regra become ``revisada`` while still colliding with
one the auditor previously set aside.

Informative only (``requires_achado=False``): a repeated name does not prove
the regras are equal (that is P2/E2) — only that the name alone does not
distinguish them. Never blocks the CI by itself; but a `revisada` regra
still part of an active P1 group *is* a P7_ESTADO_INVALIDO (estado_auditoria.py)
— the detection is global, and its blocking force is a P7 join, not a P1 property.
"""

from __future__ import annotations

import re
import unicodedata
from typing import TYPE_CHECKING

from detections import Detection, canonical_json, fingerprint

if TYPE_CHECKING:
    from bundle import Bundle

DETECTOR_ID = "P1_NOME_REPETIDO"
VERSION = 3  # v3: scans all regras (incl. inativas), not just active — global uniqueness (RFC P1)
_MIN_GROUP_SIZE = 2


def _normalize(nome: str) -> str:
    """Case/accent/whitespace-insensitive form of a nome, for grouping."""
    ascii_nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", ascii_nome).strip().lower()


def detect(bundle: Bundle) -> list[Detection]:
    """Report each group of 2+ regras (active or inactive) with the same normalized nome."""
    groups: dict[str, list[str]] = {}
    for regra in bundle.regras:
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
