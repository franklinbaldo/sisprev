"""P13.2 — the normative map from CSV columns to their `.md` representation.

Single source of truth for all 27 columns of ``data/raw/regras-sisprev.csv``.
``csv_to_okf.py``, ``okf_to_csv.py``, the dataset doc's "# Schema" table, and
the tests all derive from :data:`COLUMNS` — nothing else declares a column
mapping independently (RFC 0001, P13.2).

Per the RFC's "semântica adiada" principle, ``categoria`` for domain fields
records a *hypothesis* tagged with the open question that would confirm or
revise it (Q3, Q6, Q9, Q10, ...) — it is not a normative classification.
Only identity/provenance and administrative fields are confirmed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


@dataclass(frozen=True)
class ColumnSpec:
    """One row of the P13.2 normative map.

    Every original CSV column maps to a frontmatter key — the frontmatter *is*
    the deployable Sisprev rule (P13.2 refactor 2026-07). The markdown body
    holds the auditor's own analysis, never a CSV column, so there is no
    body/frontmatter split to model here anymore.
    """

    csv_name: str
    frontmatter_key: str
    tipo: str
    categoria: str
    semantica_vazio: str


# Order matches the original CSV header exactly — okf_to_csv.py rebuilds
# the derived CSV in this order (P13.2 CI invariant: ordem preservada).
COLUMNS: tuple[ColumnSpec, ...] = (
    ColumnSpec("NOME", "nome", "string", "identidade humana (P1)", "não vazio"),
    ColumnSpec(
        "TIPO DE BENEFICIO",
        "tipo_de_beneficio",
        "string (enum)",
        "candidato a predicado de seleção (Q3)",
        "a definir",
    ),
    ColumnSpec(
        "ATUALMENTE NO SISTEMA",
        "atualmente_no_sistema",
        "TRUE/FALSE",
        "estado no Sisprev real — não confundir com status_regra (P2.1)",
        "não vazio",
    ),
    ColumnSpec(
        "CICLO DE VALIDAÇÃO",
        "ciclo_de_validacao",
        "string (1º-4º)",
        "ordenação do processo de auditoria",
        "não vazio",
    ),
    ColumnSpec(
        "VALIDADO PGE",
        "validado_pge",
        "TRUE/FALSE",
        "legado — candidato a derivar de atos_validacao (P7)",
        "não vazio",
    ),
    ColumnSpec(
        "VALIDADO PRESIDENCIA",
        "validado_presidencia",
        "TRUE/FALSE",
        "legado — candidato a derivar de atos_validacao (P7)",
        "não vazio",
    ),
    ColumnSpec("SIMULAVEL", "simulavel", "S/N", "candidato a apresentação/interface (Q9)", "a definir"),
    ColumnSpec("TIPO", "tipo", "string", "candidato a predicado de seleção (Q3)", "a definir"),
    ColumnSpec(
        "APOS_ESPECIAL", "apos_especial", "S/N", "candidato a predicado ou apresentação (Q3, Q9)", "a definir"
    ),
    ColumnSpec("TIPO_REMUN", "tipo_remun", "string", "candidato a apresentação/interface (Q9)", "a definir"),
    ColumnSpec("PARIDADE", "paridade", "S/N", "candidato a resultado/efeito (Q6)", "a definir"),
    ColumnSpec("TabelaPontuacao", "tabelapontuacao", "S/N", "a investigar (Q9)", "a definir"),
    ColumnSpec(
        "Requisitos da IN Nº 5/2020",
        "requisitos_da_in_no_5_2020",
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "Relatório p/ Reserva Remunerada por Idade ex-officio",
        "relatorio_p_reserva_remunerada_por_idade_ex_officio",
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "ADICIONAL_INATIVIDADE",
        "adicional_inatividade",
        "S/N",
        "candidato a resultado/efeito ou apresentação (Q6, Q9)",
        "a definir",
    ),
    ColumnSpec(
        "DATA_ADM_ATE",
        "data_adm_ate",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_ADM_APOS",
        "data_adm_apos",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_DIREITO_ATE",
        "data_direito_ate",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_DIREITO_APOS",
        "data_direito_apos",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "FUNDAMENTACAO_PROPORCIONAL",
        "fundamentacao_proporcional",
        "text",
        "fundamentação (campo deployável do Sisprev)",
        "a definir (Q7 — por que uma regra pode ter as duas fundamentações?)",
    ),
    ColumnSpec(
        "VISIVEL DTC PROPORCIONAL",
        "visivel_dtc_proporcional",
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "FUNDAMENTACAO_INTEGRAL",
        "fundamentacao_integral",
        "text",
        "fundamentação (campo deployável do Sisprev)",
        "a definir (Q7 — por que uma regra pode ter as duas fundamentações?)",
    ),
    ColumnSpec(
        "VISIVEL DTC INTEGRAL",
        "visivel_dtc_integral",
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "SEXO",
        "sexo",
        "string (enum)",
        "candidato a predicado de seleção (Q3)",
        "a investigar (Q10 — AMBOS vs. vazio vs. desconhecido vs. não aplicável)",
    ),
    ColumnSpec("INTEGRAL", "integral", "S/N", "candidato a resultado/efeito (Q6)", "a definir"),
    ColumnSpec(
        "TIPO_CALCULO",
        "tipo_calculo",
        "string (enum)",
        "candidato a resultado/efeito (Q6)",
        "a investigar (Q10 — 'Não identificado' sem significado presumido)",
    ),
    ColumnSpec(
        "FUNDAMENTACAO", "fundamentacao", "text", "fundamentação (campo deployável do Sisprev)", "a definir"
    ),
)

_BY_CSV_NAME: dict[str, ColumnSpec] = {c.csv_name: c for c in COLUMNS}
if len(_BY_CSV_NAME) != len(COLUMNS):
    msg = "COLUMNS has a duplicate csv_name — every original column must appear exactly once (P13.2)"
    raise ValueError(msg)

# Every column is a frontmatter key now — FRONTMATTER_COLUMNS == CSV_COLUMN_NAMES,
# kept as a distinct name only for callers that read it semantically.
CSV_COLUMN_NAMES: tuple[str, ...] = tuple(c.csv_name for c in COLUMNS)
FRONTMATTER_COLUMNS: tuple[str, ...] = CSV_COLUMN_NAMES
FRONTMATTER_KEYS: dict[str, str] = {c.csv_name: c.frontmatter_key for c in COLUMNS}


# Administrative fields (RFC 0001, P2.1/P7/P11) — not part of the original
# CSV import, but appended to the derived CSV (P12) with explicit defaults
# so the derived export never has an "unknown" cell. Order matters: this is
# the order they're appended in the derived CSV, after the 27 original
# columns. auditado_por/auditado_em are filled on the transition to
# revisada (P11); they stay scalar strings like the rest of this dict.
ADMIN_FIELD_DEFAULTS: dict[str, str] = {
    "status_regra": "ativa",
    "motivo_inativacao": "",
    "status_auditoria": "importada",
    "auditado_por": "",
    "auditado_em": "",
}

# atos_validacao (P7) is a *list* of institutional acts (tipo/autoridade/
# identificador/fonte per item) — kept out of ADMIN_FIELD_DEFAULTS (which is
# typed as scalar strings) and handled separately wherever it's serialized
# (okf_to_csv.py JSON-encodes it into its own derived CSV column).
ATOS_VALIDACAO_KEY = "atos_validacao"

# dispositivos (P3) is a *list* of absolute OKF links to okf/dispositivos/
# concept docs (e.g. "/dispositivos/cf88/art-40-i-original.md") — same
# scalar-vs-list split as atos_validacao, same JSON-encoded CSV handling.
# Populated by a human auditor per regra, on demand — never bulk-inferred
# from free-text FUNDAMENTACAO prose (princípio da autoria humana).
DISPOSITIVOS_KEY = "dispositivos"


class RegraAdminContrato(BaseModel):
    """The P2.1/P3 administrative slice of a regra's frontmatter, validated on demand.

    Mirrors ``estado_auditoria.RegraAuditoriaContrato`` (the P7/P11 slice) —
    same reasoning, kept as a *separate* model rather than merged into it,
    since the RFC treats P2.1/P3/P7/P11 as distinct numbered proposals with
    distinct owners. ``extra="ignore"`` because this validates only a slice
    of a frontmatter dict that also carries ~27 domain fields (P2's
    extensibility requirement — a strict whole-document schema would
    contradict it, see bundle.py's Regra docstring).
    """

    model_config = ConfigDict(extra="ignore")

    status_regra: Literal["ativa", "inativa"] = "ativa"
    dispositivos: list[str] = Field(default_factory=list)


def blank_frontmatter() -> dict[str, object]:
    """Return a regra frontmatter dict with every real column present, defaulted to ``""``.

    A convenience base for building synthetic ``Regra`` fixtures (tests) or
    scaffolding a new regra doc — every caller still overrides the handful
    of fields it actually cares about.
    """
    return {FRONTMATTER_KEYS[csv_name]: "" for csv_name in FRONTMATTER_COLUMNS}


def render_schema_table() -> str:
    """Render the dataset doc's "# Schema" table — one row per COLUMNS entry."""
    lines = [
        "| Coluna | Destino | Tipo | Categoria semântica | Semântica de vazio |",
        "|---|---|---|---|---|",
    ]
    for c in COLUMNS:
        destino = f"`{c.frontmatter_key}` (frontmatter)"
        lines.append(f"| `{c.csv_name}` | {destino} | {c.tipo} | {c.categoria} | {c.semantica_vazio} |")
    return "\n".join(lines)
