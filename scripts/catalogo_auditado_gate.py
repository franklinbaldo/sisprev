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

from compilador_auditado import compilar, detectar_colisoes
from detections import Violation
from manifesto_substituicao import (
    ManifestoValidationError,
    check_nenhum_grupo_ativo_em_producao,
    load_manifesto,
    validate_manifesto,
)
from okf_common import DEFAULT_BUNDLE_AUDITADO, DEFAULT_MANIFESTO_SUBSTITUICAO
from unidade_auditada_schema import (
    UnidadeAuditadaValidationError,
    load_unidades_auditadas,
    validate_bundle_auditado,
)

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle
    from unidade_auditada_schema import UnidadeAuditada


def _checar_unidades_deployable(unidades: list[UnidadeAuditada], bundle_legado: Bundle) -> list[Violation]:
    """RFC 0004 §5.3/§14 — every ``estado_unidade: deployable`` unit must actually compile clean.

    Runs independently of any manifest/grupo state: a unit that is formally
    marked ``deployable`` but carries an impossible projection (missing
    portador, invalid enum, unresolved proveniência, ...) must be caught by
    the gate even while its group is ``inativo`` — "schema válido" is never
    the same claim as "projeção deployável válida". Collisions are checked
    across every successfully-compiled unit, not per-unit.
    """
    legacy_regra_ids = bundle_legado.regra_ids()
    dispositivo_ids = bundle_legado.dispositivo_ids()
    violations: list[Violation] = []
    resultados = [
        compilar(
            unidade, modo="deployable", legacy_regra_ids=legacy_regra_ids, dispositivo_ids=dispositivo_ids
        )
        for unidade in unidades
        if unidade.estado_unidade == "deployable"
    ]
    for resultado in resultados:
        violations.extend(resultado.pendencias)
    violations.extend(detectar_colisoes(resultados))
    return violations


def check_catalogo_auditado(
    bundle_legado: Bundle,
    *,
    bundle_auditado_dir: Path = DEFAULT_BUNDLE_AUDITADO,
    manifesto_path: Path = DEFAULT_MANIFESTO_SUBSTITUICAO,
) -> list[Violation]:
    """Run every RFC 0004 Fase 1A structural gate against the real repo state.

    Enforces, in addition to the general manifest/unit invariants, the
    Fase-1A-specific rule that the production manifest must never declare
    an active group — activation isn't wired to any exporter yet. A
    malformed audited-unit document (unparseable frontmatter) is reported
    as a stable ``Violation`` rather than raising — the ``--json`` payload
    shape (``{"violations": [...], "detections": [...]}``) must survive a
    corrupt document the same way it survives any other invariant failure.
    """
    try:
        unidades = load_unidades_auditadas(bundle_auditado_dir)
    except UnidadeAuditadaValidationError as exc:
        return [Violation("AUDITADA_DOCUMENTO_INVALIDO", str(exc))]

    violations = validate_bundle_auditado(unidades, bundle_legado)
    violations.extend(_checar_unidades_deployable(unidades, bundle_legado))

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
