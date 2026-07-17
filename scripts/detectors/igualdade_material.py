"""P2 detector — material equality between active regras.

The comparison is intentionally extensible: every authored frontmatter field
and every level-one body section is material by default. Only explicit
identity, provenance and administrative/audit fields are excluded.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from detections import Detection, canonical_json, fingerprint
from regra_schema import ADMIN_FIELD_DEFAULTS

if TYPE_CHECKING:
    from bundle import Bundle, Regra

DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
VERSION = 3  # v3: fingerprint now incorporates the material content, not just regra ids
_MIN_GROUP_SIZE = 2

_IGNORED_FRONTMATTER_KEYS = frozenset(
    {
        "type",
        "id",
        "row_index",
        "nome",
        "auditado_por",
        "auditado_em",
        "atos_validacao",
        *ADMIN_FIELD_DEFAULTS,
    }
)


def _material_key(regra: Regra) -> str:
    """Canonical representation of all current and future material content."""
    frontmatter = {
        key: value for key, value in regra.frontmatter.items() if key not in _IGNORED_FRONTMATTER_KEYS
    }
    payload = {
        "frontmatter": frontmatter,
        "sections": regra.sections,
    }
    return canonical_json(payload)


def detect(bundle: Bundle) -> list[Detection]:
    """Report each group of 2+ active regras with equal material content."""
    groups: dict[str, list[str]] = {}
    for regra in bundle.active_regras():
        groups.setdefault(_material_key(regra), []).append(regra.id)

    detections: list[Detection] = []
    for material_key, regra_ids in groups.items():
        if len(regra_ids) < _MIN_GROUP_SIZE:
            continue
        sorted_ids = sorted(regra_ids)
        # The fingerprint bakes in the material content (material_key), not
        # just the ids: a group that keeps the same members but drifts to a
        # different shared value must not reuse the old fingerprint (an
        # achado documenting the old content would otherwise look "still
        # reproduced" for a premise that no longer holds).
        canonical_subject = canonical_json({"regras": sorted_ids, "material_key": material_key})
        detections.append(
            Detection(
                detector=DETECTOR_ID,
                fingerprint=fingerprint(DETECTOR_ID, VERSION, canonical_subject),
                regras=frozenset(regra_ids),
                evidencia={"grupo": sorted_ids},
            )
        )
    return detections
