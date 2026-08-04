#!/usr/bin/env bash
# Regenera site/src/data/dados-do-site.json a partir do estado atual do bundle.
# O arquivo carrega o SHA do commit que está sendo publicado, então comitá-lo
# seria autorreferencial: ele é .gitignore e nasce de novo a cada dev/build.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"
uv run python scripts/derivar.py --somente-snapshot

# A planilha de homologação é servida ao lado do relatório que a promete. Ela é
# derivada e comitada, então aqui só se copia — quem a escreve é `derivar.py`,
# o único comando que escreve artefato derivado.
mkdir -p site/public/downloads
cp data/regras-propostas.csv site/public/downloads/regras-propostas.csv
