"""P2 detector — igualdade material entre regras ativas (RFC 0001, P2).

Reports groups of 2+ **active** regras whose 26 non-``NOME`` columns are
byte-identical in the frozen import. It only reports the occurrence; the
auditor writes the achado. The comparison deliberately ignores ``NOME``
(P1/P2), ``id``/``row_index`` (identity/provenance) and the administrative
fields (P2.1/P7) — so renaming a regra or flipping an admin field never
changes a detection, while a new domain field or body section that actually
distinguishes two regras splits the group (both proved by unit tests).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from detections import Detection, fingerprint
from regra_schema import BODY_COLUMNS, CSV_COLUMN_NAMES, FRONTMATTER_KEYS

if TYPE_CHECKING:
    from bundle import Bundle, Regra

DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
VERSION = 1

# A material-equality group needs at least two members.
_MIN_GROUP_SIZE = 2

# Every original column except NOME defines "igualdade material" (P1/P2).
_COMPARE_COLUMNS = tuple(c for c in CSV_COLUMN_NAMES if c != "NOME")


def _material_key(regra: Regra) -> tuple[str, ...]:
    """The tuple of values (excluding NOME) that defines material equality."""
    values = []
    for col in _COMPARE_COLUMNS:
        if col in BODY_COLUMNS:
            values.append(regra.sections.get(col, ""))
        else:
            values.append(str(regra.frontmatter.get(FRONTMATTER_KEYS[col], "")))
    return tuple(values)


def detect(bundle: Bundle) -> list[Detection]:
    """Report each group of 2+ active regras that are materially identical."""
    groups: dict[tuple[str, ...], list[str]] = {}
    for regra in bundle.active_regras():
        groups.setdefault(_material_key(regra), []).append(regra.id)

    detections: list[Detection] = []
    for regra_ids in groups.values():
        if len(regra_ids) < _MIN_GROUP_SIZE:
            continue
        canonical = "\n".join(sorted(regra_ids))
        detections.append(
            Detection(
                detector=DETECTOR_ID,
                fingerprint=fingerprint(DETECTOR_ID, VERSION, canonical),
                regras=frozenset(regra_ids),
                evidencia={"grupo": sorted(regra_ids)},
            ),
        )
    return detections
