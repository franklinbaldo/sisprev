"""Fase B site data emitter (RFC 0003 §4/§8) — the minimal audit-state bridge.

``validar_regras.py --json`` does not serve as this bridge: its payload only
carries ``violations``/``detections`` (RFC 0003 §4), nothing about regras,
achados, or their effective audit state, and it is emitted via ``logger``
(stderr), not stdout. This script is a *different*, dedicated emitter, run as
a build step by the Astro site (never by ``gerar_indices.py`` — its output is
never committed, see the module docstring below for the ephemeral contract).

It emits exactly the subset the site's selos (status seals) need, computed by
this repo's own domain library — never recomputed in JavaScript (RFC 0001):
per regra the *effective* ``status_auditoria`` (re-verified by
``validate_bundle``, the same P7/P14 join ``validar_regras.py`` runs — this
refuses to emit anything if the bundle currently has any outstanding
violation, so the site can never serve a state Python itself considers
broken) plus ``validado_pge``/``validado_presidencia``/``ciclo_de_validacao``;
per achado ``situacao``/``severidade``/``regras_afetadas``. Every other domain
field (``nome``, ``fundamentacao*``, ``dispositivos``, ...) is read by Astro
directly from the ``.md`` frontmatter via its own content collections — this
emitter does not duplicate them.

Ephemeral contract (RFC 0003 §4, §7): the output JSON carries the exact
source ``--sha`` the caller passes in (normally the commit being built), so
committing the file would be self-referential — the commit that adds it
would produce a new SHA, immediately stale. The output is therefore never
committed (see ``.gitignore``); ``site/scripts/emit-data.sh`` regenerates it
on every local dev/build/CI run, and it is excluded from the
``derived-csv-in-sync`` gate, which only covers artifacts committed to this
repository.

Run as ``uv run python scripts/emit_site_data.py --sha <sha> --date <iso-date> --out <path>``.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict

from bundle import Bundle, collect_detections, validate_bundle
from okf_common import DEFAULT_BUNDLE

if TYPE_CHECKING:
    from achado_schema import Achado
    from bundle import Regra

logger = logging.getLogger(__name__)

SCHEMA_VERSION = 1


class RegraPayload(TypedDict):
    """The audit-state subset a regra's selo needs — never the ~27 domain fields."""

    status_auditoria: str
    validado_pge: bool
    validado_presidencia: bool
    ciclo_de_validacao: str


class AchadoPayload(TypedDict):
    """The audit-state subset an achado's selo/backlink needs."""

    situacao: str
    severidade: str
    regras_afetadas: list[str]


class SitePayload(TypedDict):
    """The full emitter payload — schema_version gates any future breaking change."""

    schema_version: int
    sha: str
    generated_at: str
    regras: dict[str, RegraPayload]
    achados: dict[str, AchadoPayload]


class SiteDataBundleInvalidError(Exception):
    """Raised when the bundle has an outstanding violation the emitter refuses to serve.

    A silent emit over a broken bundle would let the site quietly diverge
    from what ``validar_regras.py`` (and CI) already consider invalid —
    "detecção ≠ conclusão" applies to this reader too: the build must fail
    loudly, the same way CI's ``validar-regras`` job would.
    """


def _regra_payload(regra: Regra) -> RegraPayload:
    frontmatter = regra.frontmatter
    return {
        "status_auditoria": str(frontmatter.get("status_auditoria") or "importada"),
        "validado_pge": str(frontmatter.get("validado_pge") or "").strip().upper() == "TRUE",
        "validado_presidencia": str(frontmatter.get("validado_presidencia") or "").strip().upper() == "TRUE",
        "ciclo_de_validacao": str(frontmatter.get("ciclo_de_validacao") or ""),
    }


def _achado_payload(achado: Achado) -> AchadoPayload:
    return {
        "situacao": achado.situacao,
        "severidade": str(achado.frontmatter.get("severidade") or ""),
        "regras_afetadas": [ref.rsplit("/", 1)[-1].removesuffix(".md") for ref in achado.regras_afetadas],
    }


def build_payload(bundle: Bundle, *, sha: str, generated_at: str) -> SitePayload:
    """Build the emitter's JSON payload, refusing if the bundle has any outstanding violation."""
    detections = collect_detections(bundle)
    violations = validate_bundle(bundle, detections)
    if violations:
        lines = "\n".join(f"- {v.code}: {v.message}" for v in violations)
        msg = (
            f"refusing to emit site data: bundle has {len(violations)} outstanding "
            f"violation(s) (run `uv run python scripts/validar_regras.py` for detail):\n{lines}"
        )
        raise SiteDataBundleInvalidError(msg)

    return {
        "schema_version": SCHEMA_VERSION,
        "sha": sha,
        "generated_at": generated_at,
        "regras": {regra.doc_id: _regra_payload(regra) for regra in bundle.regras},
        "achados": {achado.doc_id: _achado_payload(achado) for achado in bundle.achados},
    }


def render_payload(payload: SitePayload) -> str:
    """Render ``payload`` deterministically — stable key order, one trailing newline.

    ``sort_keys=True`` makes dict key order a pure function of the keys
    themselves (regra/achado ids sort lexicographically, and zero-padded
    ``NNNN`` ids sort in numeric order too); list order is already
    deterministic (``bundle.regras``/``bundle.achados`` are loaded in sorted
    filename order by ``Bundle.load``). Nothing here depends on wall-clock
    time or dict insertion order, so the same bundle + ``--sha``/``--date``
    always serializes byte-for-byte identically.
    """
    return json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: emit ``--out`` from ``--bundle``, or exit 1 if the bundle is invalid."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--sha", required=True, help="exact source commit SHA being built")
    parser.add_argument("--date", required=True, help="ISO date (YYYY-MM-DD) of the source snapshot")
    parser.add_argument("--out", type=Path, required=True, help="output path for dados-do-site.json")
    args = parser.parse_args(argv)

    bundle = Bundle.load(args.bundle)
    try:
        payload = build_payload(bundle, sha=args.sha, generated_at=args.date)
    except SiteDataBundleInvalidError:
        logger.exception("cannot emit site data")
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render_payload(payload), encoding="utf-8")
    logger.info(
        "Wrote %s (%d regra(s), %d achado(s)).",
        args.out,
        len(payload["regras"]),
        len(payload["achados"]),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
