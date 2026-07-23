"""RFC 0004 §14 — CI gate for the audited catalog + substitution manifest.

Read-only, same posture as ``validar_regras.py``: loads the audited bundle
and the production manifest, runs every structural gate, and returns plain
``Violation``s that ``validar_regras.py`` appends to its existing payload —
never a new top-level JSON shape, never a new exit path. An audited bundle
with zero units, and a manifest with zero groups, must both pass cleanly
(RFC 0004 §14: "bundle auditado vazio deve passar").
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from detections import Violation
from manifesto_substituicao import (
    ManifestoValidationError,
    check_nenhum_grupo_ativo_em_producao,
    load_manifesto,
    validate_manifesto,
)
from okf_common import DEFAULT_BUNDLE_AUDITADO, DEFAULT_MANIFESTO_SUBSTITUICAO
from unidade_auditada_schema import load_unidades_auditadas, validate_bundle_auditado

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle


def check_catalogo_auditado(
    bundle_legado: Bundle,
    *,
    bundle_auditado_dir: Path = DEFAULT_BUNDLE_AUDITADO,
    manifesto_path: Path = DEFAULT_MANIFESTO_SUBSTITUICAO,
) -> list[Violation]:
    """Run every RFC 0004 Fase 1A structural gate against the real repo state.

    Enforces, in addition to the general manifest/unit invariants, the
    Fase-1A-specific rule that the production manifest must never declare
    an active group — activation isn't wired to any exporter yet.
    """
    unidades = load_unidades_auditadas(bundle_auditado_dir)
    violations = validate_bundle_auditado(unidades, bundle_legado)

    if not manifesto_path.exists():
        violations.append(
            Violation(
                "MANIFESTO_AUSENTE", f"{manifesto_path} not found — expected an empty/inactive-only manifest"
            )
        )
        return violations

    try:
        manifesto = load_manifesto(manifesto_path)
    except ManifestoValidationError as exc:
        violations.append(Violation("MANIFESTO_INVALIDO", str(exc)))
        return violations

    violations.extend(validate_manifesto(manifesto, unidades, bundle_legado))
    violations.extend(check_nenhum_grupo_ativo_em_producao(manifesto))
    return violations
