"""P10 — the RFC 0001 validator.

Implements the "semântica adiada" four-layer model (RFC 0001, top-of-doc
principle):

1. **structural invariants** (regra identity, achado schema) — bloqueante;
2. **mechanic detectors** (P2 igualdade material) — create/verify achados,
   checked bidirectionally against ``achados/`` — bloqueante only on
   *incoherence* between what's detected and what's recorded, never on the
   detected condition itself;
3. heuristic/semantic checks (P5 datas-vs-marcos, P9 co-ocorrências) — not
   yet implemented as blocking; planned as informative/híbrido achados;
4. confirmed semantic rules (post-P13.2) — not yet applicable.

Exit code != 0 iff a camada-1 or camada-2-bidirectional violation is found.
Run as ``uv run python scripts/validar_regras.py [--bundle PATH]``.
"""

from __future__ import annotations

import argparse
import datetime
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

from achado_schema import (
    build_achado_doc,
    load_achados,
    next_achado_id,
    regenerate_achados_index,
    validate_bundle_achados,
)
from okf_common import DEFAULT_BUNDLE, BundleIntegrityError
from okf_to_csv import parse_doc, validate_bundle_identity
from regra_schema import ADMIN_FIELD_DEFAULTS, BODY_COLUMNS, CSV_COLUMN_NAMES, FRONTMATTER_KEYS

DETECTOR_TOOL_ID = "scripts/validar_regras.py"

logger = logging.getLogger(__name__)

P2_DETECTOR_CODE = "P2_IGUALDADE_MATERIAL_ATIVA"
_COMPARE_COLUMNS = tuple(c for c in CSV_COLUMN_NAMES if c != "NOME")


@dataclass(frozen=True)
class Violation:
    """One validator finding — always includes a stable code (P10)."""

    code: str
    message: str

    def __str__(self) -> str:
        """Render as "CODE: message" for CLI output."""
        return f"{self.code}: {self.message}"


def _load_regras(bundle_dir: Path) -> list[tuple[str, dict, dict[str, str]]]:
    """Return (regra_id, frontmatter, body_sections) for every regra doc, in filename order."""
    regras_dir = bundle_dir / "regras"
    result = []
    for doc_path in sorted(regras_dir.glob("regra-*.md")):
        frontmatter, sections = parse_doc(doc_path.read_text(encoding="utf-8"))
        result.append((doc_path.stem, frontmatter, sections))
    return result


def check_structural(bundle_dir: Path) -> list[Violation]:
    """Camada 1: regra sequence identity + achado schema. Both bloqueante."""
    violations: list[Violation] = []

    try:
        validate_bundle_identity(bundle_dir)
    except BundleIntegrityError as exc:
        violations.append(Violation("P_ESTRUTURA_REGRAS", str(exc)))

    regra_ids = frozenset(doc_path.stem for doc_path in sorted((bundle_dir / "regras").glob("regra-*.md")))
    violations.extend(
        Violation("P14_ACHADO_INVALIDO", error)
        for error in validate_bundle_achados(bundle_dir, known_regra_ids=regra_ids)
    )

    return violations


def _material_key(frontmatter: dict, sections: dict[str, str]) -> tuple[str, ...]:
    """The tuple of values (excluding NOME) that defines "igualdade material" for P2."""
    values = []
    for col in _COMPARE_COLUMNS:
        if col in BODY_COLUMNS:
            values.append(sections.get(col, ""))
        else:
            values.append(str(frontmatter.get(FRONTMATTER_KEYS[col], "")))
    return tuple(values)


def detect_p2_groups(bundle_dir: Path) -> list[frozenset[str]]:
    """Camada 2 detector: groups of 2+ ACTIVE regras materially identical (ignoring NOME).

    Returns each group as a frozenset of regra ids — comparable directly
    against an achado's regras_afetadas set.
    """
    groups: dict[tuple[str, ...], list[str]] = {}
    for regra_id, frontmatter, sections in _load_regras(bundle_dir):
        status_regra = frontmatter.get("status_regra", ADMIN_FIELD_DEFAULTS["status_regra"])
        if status_regra != "ativa":
            continue
        key = _material_key(frontmatter, sections)
        groups.setdefault(key, []).append(regra_id)

    return [frozenset(ids) for ids in groups.values() if len(ids) > 1]


def _regra_ref_to_id(ref: str) -> str:
    return ref.rsplit("/", 1)[-1].removesuffix(".md")


def check_p2_bidirectional(bundle_dir: Path) -> list[Violation]:
    """Camada 2: detected igualdade-material groups <-> achados must agree exactly.

    - a detected group with no matching open P2 achado -> P14_DETECTOR_SEM_ACHADO
    - an open P2 achado whose regras_afetadas isn't a currently-detected group
      -> P14_ACHADO_SEM_DETECTOR
    """
    violations: list[Violation] = []
    detected_groups = detect_p2_groups(bundle_dir)

    p2_achados = [
        a
        for a in load_achados(bundle_dir)
        if a.frontmatter.get("detector") == P2_DETECTOR_CODE and a.frontmatter.get("situacao") == "aberto"
    ]
    achado_groups = {frozenset(_regra_ref_to_id(r) for r in a.regras_afetadas): a for a in p2_achados}

    violations.extend(
        Violation(
            "P14_DETECTOR_SEM_ACHADO",
            f"{P2_DETECTOR_CODE} detected an undocumented group: {sorted(group)}",
        )
        for group in detected_groups
        if group not in achado_groups
    )

    detected_set = set(detected_groups)
    violations.extend(
        Violation(
            "P14_ACHADO_SEM_DETECTOR",
            f"{achado.doc_id} (detector={P2_DETECTOR_CODE}) no longer matches any "
            "detected group — resolve it or update regras_afetadas",
        )
        for group, achado in achado_groups.items()
        if group not in detected_set
    )

    return violations


def create_missing_p2_achados(bundle_dir: Path) -> list[str]:
    """Write an achado for every currently-undocumented P2 group (P14.4).

    Neutral by construction (RFC "semântica adiada"/"detecção ≠ conclusão"):
    each achado states only the mechanical fact — which regras are
    materially identical — and asks the investigation to determine the
    cause. It does not propose inactivating anyone. Returns the created ids.
    """
    violations = check_p2_bidirectional(bundle_dir)
    undocumented = [v for v in violations if v.code == "P14_DETECTOR_SEM_ACHADO"]
    if not undocumented:
        return []

    today = datetime.datetime.now(tz=datetime.UTC).date().isoformat()
    created: list[str] = []
    (bundle_dir / "achados").mkdir(parents=True, exist_ok=True)

    for group in detect_p2_groups(bundle_dir):
        already_documented = any(
            frozenset(_regra_ref_to_id(r) for r in a.regras_afetadas) == group
            for a in load_achados(bundle_dir)
            if a.frontmatter.get("detector") == P2_DETECTOR_CODE
        )
        if already_documented:
            continue

        doc_id = next_achado_id(bundle_dir)
        regra_ids = sorted(group)
        frontmatter = {
            "type": "Achado",
            "id": doc_id,
            "nome": f"Igualdade material entre {', '.join(regra_ids)}",
            "situacao": "aberto",
            "severidade": "bloqueante",
            "verificacao": "mecanica",
            "detector": P2_DETECTOR_CODE,
            "natureza": "dados",
            "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
            "detectado_em": today,
            "detectado_por": DETECTOR_TOOL_ID,
        }
        sections = {
            "Descrição": (
                f"As regras {', '.join(regra_ids)} têm todas as colunas originais "
                "materialmente idênticas, exceto NOME (P2 ignora o nome na comparação — "
                "ver RFC 0001, P1/P2)."
            ),
            "Evidências": f"Detectado por `{P2_DETECTOR_CODE}` em {today}.",
            "Questão a investigar": (
                "A igualdade material representa redundância indevida, uma distinção não "
                "modelada nas 27 colunas, ou outro problema de origem? Ver RFC 0001, P2."
            ),
            "Resolução": "",
        }
        doc_text = build_achado_doc(frontmatter, sections)
        (bundle_dir / "achados" / f"{doc_id}.md").write_text(doc_text, encoding="utf-8")
        created.append(doc_id)

    regenerate_achados_index(bundle_dir)
    return created


def run(bundle_dir: Path) -> list[Violation]:
    """Run every implemented check. Returns all violations (empty = clean)."""
    violations = check_structural(bundle_dir)
    violations.extend(check_p2_bidirectional(bundle_dir))
    return violations


def main() -> None:
    """CLI entry point: validate --bundle, printing every violation. Exits 1 if any."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--criar-achados",
        action="store_true",
        help="Write a neutral achado for every currently-undocumented P2 group, then re-validate.",
    )
    args = parser.parse_args()

    if args.criar_achados:
        created = create_missing_p2_achados(args.bundle)
        for doc_id in created:
            logger.info("Created %s", doc_id)
    elif (args.bundle / "achados").is_dir():
        # Keep achados/index.md and the bundle-root index.md current even
        # when no achado was created this run (P14.7) — same pattern as
        # okf_to_csv.py always refreshing regras/index.md.
        regenerate_achados_index(args.bundle)

    violations = run(args.bundle)
    if not violations:
        logger.info("No violations found.")
        return

    for violation in violations:
        logger.error(str(violation))
    logger.error("%d violation(s) found.", len(violations))
    sys.exit(1)


if __name__ == "__main__":
    main()
