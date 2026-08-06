#!/usr/bin/env bash
# Regenera site/src/data/dados-do-site.json a partir do estado atual do bundle.
# O arquivo carrega o SHA do commit que está sendo publicado, então comitá-lo
# seria autorreferencial: ele é .gitignore e nasce de novo a cada dev/build.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"
uv run python scripts/derivar.py --somente-snapshot

# As planilhas de homologação são servidas ao lado dos relatórios que as
# prometem. São derivadas e comitadas, então aqui só se copia — quem as escreve
# é `derivar.py`, o único comando que escreve artefato derivado.
#
# O glob pega a carga global e as recortadas por ciclo de uma vez. Cada
# relatório de ciclo identifica e anexa a sua: a global reúne toda proposta
# pronta do repositório, de qualquer ciclo, e servi-la como anexo de uma
# manifestação de ciclo levaria à homologação regra sobre a qual aquele
# relatório não concluiu.
mkdir -p site/public/downloads
cp data/regras-propostas*.csv site/public/downloads/
