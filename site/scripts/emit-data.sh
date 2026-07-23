#!/usr/bin/env bash
# Regenerates site/src/data/dados-do-site.json from the current bundle state
# (RFC 0003 §4/§8) — the emitter is ephemeral, never committed (.gitignore),
# so this runs as an npm pre-dev/pre-build hook, every time, deterministically
# from the exact commit being built (or the working tree, for local dev).
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
site_dir="$(dirname "$script_dir")"
repo_root="$(dirname "$site_dir")"

sha="$(git -C "$repo_root" rev-parse HEAD)"
date="$(git -C "$repo_root" log -1 --format=%cs HEAD)"
out="$site_dir/src/data/dados-do-site.json"

cd "$repo_root"
uv run python scripts/emit_site_data.py --sha "$sha" --date "$date" --out "$out"
