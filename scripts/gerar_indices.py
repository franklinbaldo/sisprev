"""Derive command (RFC 0001, P10 "derivar") — generates only derivable artifacts.

Regenerates everything that is a pure function of the authored sources:

- ``regras/index.md`` and ``data/regras-sisprev.csv`` (via ``okf_to_csv``);
- ``achados/index.md`` and the bundle-root ``index.md`` (via ``achado_schema``);
- ``regras/log.md`` (via ``regras_log``) — best-effort, see that module: it
  is **not** part of the CI-gated set below (a commit can't include its own
  hash/message in advance), so it's fine for it to lag until refreshed.

It writes **only** these derived artifacts — never ``regra-*.md`` or
``achado-*.md`` (the authored sources). The CI runs this and then checks
``git diff --exit-code`` on the gated subset: if anything changed, a source
was edited without regenerating the derived artifacts.

Run as ``uv run python scripts/gerar_indices.py [--bundle PATH] [--out CSV]``.
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

from achado_schema import regenerate_achados_index
from okf_common import DEFAULT_BUNDLE, DEFAULT_REBUILT_CSV
from okf_to_csv import convert
from regras_log import regenerate_regras_log

logger = logging.getLogger(__name__)


def derive(bundle_dir: Path, csv_out: Path) -> int:
    """Regenerate every derived artifact for ``bundle_dir``. Returns the CSV row count."""
    rows = convert(bundle_dir, csv_out)  # regras/index.md + derived CSV
    # regenerate_achados_index() also rewrites the bundle-root index.md, which
    # requires the dataset doc (regras-sisprev.md) to exist — every bundle
    # convert() just succeeded on has one.
    if (bundle_dir / "regras-sisprev.md").exists():
        regenerate_achados_index(bundle_dir)  # achados/index.md + root index.md
    regenerate_regras_log(bundle_dir)  # regras/log.md — best-effort, not CI-gated
    return rows


def main() -> None:
    """CLI entry point: regenerate derived artifacts for --bundle."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--out", type=Path, default=DEFAULT_REBUILT_CSV)
    args = parser.parse_args()

    rows = derive(args.bundle, args.out)
    logger.info("Regenerated derived artifacts (%d rows) for %s", rows, args.bundle)


if __name__ == "__main__":
    main()
