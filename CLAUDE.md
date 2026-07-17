# CLAUDE.md

Project guide for Claude Code. Keep this file short and actionable.

## What this repo is

`sisprev` catalogs the retirement/pension rules ("regras de aposentadoria e
pensão por morte") of a state's regime próprio de previdência (RO), and
converts that catalog losslessly between two representations:

- **`data/raw/regras-sisprev.csv`** — the source of truth, a 112-row export
  with legal basis, eligibility windows, and calculation method per rule.
- **`okf/regras-sisprev/`** — the same data as an [Open Knowledge Format
  (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  bundle: markdown files with YAML frontmatter, one concept doc per rule.

## Architecture at a glance

```
data/raw/regras-sisprev.csv          <-- source of truth
        │  scripts/csv_to_okf.py
        ▼
okf/regras-sisprev/
├── index.md                         # root listing — NO frontmatter except okf_version (SPEC.md §6, §11)
├── regras-sisprev.md                # type: Dataset — columns/row_count frontmatter + "# Schema" table
└── regras/
    ├── index.md                     # listing, no frontmatter
    └── regra-0001.md ... regra-0112.md   # type: Regra, one per CSV row
        │  scripts/okf_to_csv.py (reverse direction)
        ▼
data/raw/regras-sisprev.csv
```

- Long free-text columns (`FUNDAMENTACAO`, `FUNDAMENTACAO_PROPORCIONAL`,
  `FUNDAMENTACAO_INTEGRAL`) live in the markdown **body** as sections, not
  frontmatter — OKF's own guidance: frontmatter for queryable fields, body
  for prose. Every other column is a frontmatter key (slugified column name).
- `regras-sisprev.md`'s `columns` frontmatter field is the single source of
  truth for column order/names when rebuilding the CSV — `okf_to_csv.py`
  reads it from there, not from `index.md` (which per spec MUST NOT carry
  arbitrary frontmatter).
- The CSV's stray leading blank row (a Google Sheets export artifact) is
  reproduced explicitly by `okf_to_csv.py`, not treated as data.

## Running things

```bash
# CSV -> OKF bundle
uv run python scripts/csv_to_okf.py

# OKF bundle -> CSV (writes back to data/raw/regras-sisprev.csv by default)
uv run python scripts/okf_to_csv.py

# Tests (round-trip: CSV -> bundle -> CSV must reproduce the original DataFrame)
uv run pytest -q
```

## Rules of the road

- **CSV and bundle must always be regenerated together.** If you edit
  `data/raw/regras-sisprev.csv` by hand, run `csv_to_okf.py` before
  committing. If you edit a `regras/regra-*.md` doc by hand, run
  `okf_to_csv.py` before committing. CI's `bundle-in-sync` job fails the
  build if the two ever disagree — don't try to satisfy it by editing only
  one side.
- **`index.md` files never carry frontmatter**, except the bundle-root
  `index.md`'s `okf_version` key (the one exception the spec allows). Put
  dataset-level metadata (`columns`, `row_count`, `source_file`, `tags`) on
  the `Dataset` concept doc (`regras-sisprev.md`) instead.
- **Ruff runs with `select = ["ALL"]`** (see `pyproject.toml`). Fix
  violations for real — no `# noqa` comments anywhere in this repo. If a
  rule is fundamentally wrong for this project, add it to `[tool.ruff.lint]
  ignore` with a comment explaining why, don't suppress it inline.
- **`ty` type-checks the whole project** (`uv run ty check`). `scripts/` is
  on the module search path via `[tool.ty.environment] extra-paths`, not a
  regular installed package — keep that in sync with `[tool.pytest.ini_options]
  pythonpath` if either changes.
- Python 3.13+, `from __future__ import annotations` at the top of every
  module.

## Before committing

```bash
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest -q
```

If you touched the CSV or the bundle, also regenerate the other side and
verify no diff:

```bash
uv run python scripts/csv_to_okf.py
git status --porcelain okf/          # must be empty
```
