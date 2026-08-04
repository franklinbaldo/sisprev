#!/usr/bin/env bash
# Regenera site/src/data/dados-do-site.json a partir do estado atual do bundle.
# O arquivo carrega o SHA do commit que está sendo publicado, então comitá-lo
# seria autorreferencial: ele é .gitignore e nasce de novo a cada dev/build.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"
uv run python scripts/derivar.py --somente-snapshot
