"""P10 CLI — thin, read-only presentation of the domain library (RFC 0001).

All normative logic lives in ``bundle.py`` (pure, side-effect free). This
script only loads the bundle, calls ``validate_bundle``, prints the
violations (text or JSON) and exits 0/1. It **never** writes ``achado-*.md``,
regenerates indices, or authors any content — derived artifacts are the job
of ``gerar_indices.py`` (the "derivar" step), and achados are written by
hand (princípio da autoria humana).

Run as ``uv run python scripts/validar_regras.py [--bundle PATH] [--json]``.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from bundle import Bundle, collect_detections, validate_bundle
from okf_common import DEFAULT_BUNDLE

logger = logging.getLogger(__name__)


def main() -> None:
    """Validate --bundle and exit non-zero if any violation is found."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit violations (and detections) as JSON instead of text.",
    )
    args = parser.parse_args()

    bundle = Bundle.load(args.bundle)
    violations = validate_bundle(bundle)

    if args.json:
        detections = collect_detections(bundle)
        payload = {
            "violations": [{"code": v.code, "message": v.message} for v in violations],
            "detections": [
                {"detector": d.detector, "fingerprint": d.fingerprint, "regras": sorted(d.regras)}
                for d in detections
            ],
        }
        logger.info("%s", json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for violation in violations:
            logger.error("%s", violation)
        if violations:
            logger.info("%d violation(s) found.", len(violations))
        else:
            logger.info("No violations found.")

    if violations:
        sys.exit(1)


if __name__ == "__main__":
    main()
