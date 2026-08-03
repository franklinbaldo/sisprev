"""Derive command (RFC 0001, P10 "derivar") — generates only derivable artifacts.

Regenerates everything that is a pure function of the authored sources:

- ``regras/index.md`` and ``data/regras-sisprev.csv`` (via ``okf_to_csv``);
- ``achados/index.md`` and the bundle-root ``index.md`` (via ``achado_schema``);
- ``okf/dispositivos/``'s per-norma and root ``index.md`` (via
  ``dispositivo_schema``, P3) — a no-op until the first dispositivo exists;
- ``data/homologacao/<conjunto>.csv`` (via ``homologacao_csv``) — a projeção,
  em colunas do Sisprev, do que cada proposta viva levaria ao sistema;
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
from bundle import Bundle
from conjunto_schema import regenerate_conjuntos_index
from dispositivo_schema import regenerate_dispositivos_index
from homologacao_csv import regenerate_homologacao
from okf_common import (
    DEFAULT_BUNDLE,
    DEFAULT_BUNDLE_PROPOSTO,
    DEFAULT_DISPOSITIVOS_BUNDLE,
    DEFAULT_HOMOLOGACAO_DIR,
    DEFAULT_REBUILT_CSV,
    default_conjuntos_dir,
    default_dispositivos_dir,
)
from okf_to_csv import convert
from regras_log import regenerate_regras_log

logger = logging.getLogger(__name__)


def derive(
    bundle_dir: Path,
    csv_out: Path,
    dispositivos_dir: Path | None = None,
    auditadas_dir: Path | None = None,
    homologacao_dir: Path | None = None,
) -> int:
    """Regenerate every derived artifact for ``bundle_dir``. Returns the CSV row count.

    ``dispositivos_dir`` defaults to the conventional sibling
    ``okf/dispositivos/`` (P3, matching ``Bundle.load``'s convention) — pass
    it explicitly in tests that use a ``bundle_dir`` with no such sibling, so
    a temp-dir test run never touches the real bundle.
    """
    # O export consome a composição vigente (P15), não o que está em disco —
    # hoje as duas coincidem por construção, e é convert() que prova isso a
    # cada execução em vez de assumir (RFC 0006 §4).
    rows = convert(bundle_dir, csv_out, pertinencia=Bundle.load(bundle_dir).catalogo_vigente)
    # regenerate_achados_index() also rewrites the bundle-root index.md, which
    # requires the dataset doc (regras-sisprev.md) to exist — every bundle
    # convert() just succeeded on has one.
    if (bundle_dir / "regras-sisprev.md").exists():
        regenerate_achados_index(bundle_dir)  # achados/index.md + root index.md
    if dispositivos_dir is None:
        dispositivos_dir = default_dispositivos_dir(bundle_dir)
    regenerate_dispositivos_index(dispositivos_dir)  # okf/dispositivos/ indexes (P3)
    regenerate_conjuntos_index(default_conjuntos_dir(bundle_dir))  # okf/conjuntos/index.md (P15)
    if auditadas_dir is None:
        auditadas_dir = DEFAULT_BUNDLE_PROPOSTO
    if homologacao_dir is None:
        homologacao_dir = DEFAULT_HOMOLOGACAO_DIR
    # data/homologacao/*.csv (RFC 0004 §5) — a projeção do que cada proposta
    # viva levaria ao Sisprev. Depende do bundle auditado, que pode não existir
    # ao lado de um bundle_dir de teste; regenerate_homologacao devolve () ali.
    regenerate_homologacao(Bundle.load(bundle_dir), auditadas_dir, homologacao_dir)
    regenerate_regras_log(bundle_dir)  # regras/log.md — best-effort, not CI-gated
    return rows


def main() -> None:
    """CLI entry point: regenerate derived artifacts for --bundle."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--out", type=Path, default=DEFAULT_REBUILT_CSV)
    parser.add_argument("--dispositivos", type=Path, default=DEFAULT_DISPOSITIVOS_BUNDLE)
    parser.add_argument("--auditadas", type=Path, default=DEFAULT_BUNDLE_PROPOSTO)
    parser.add_argument("--homologacao", type=Path, default=DEFAULT_HOMOLOGACAO_DIR)
    args = parser.parse_args()

    rows = derive(args.bundle, args.out, args.dispositivos, args.auditadas, args.homologacao)
    logger.info("Regenerated derived artifacts (%d rows) for %s", rows, args.bundle)


if __name__ == "__main__":
    main()
