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


@dataclass(frozen=True)
class ColumnSpec:
    """One row of the P13.2 normative map."""

    csv_name: str
    frontmatter_key: str | None  # None <=> body column
    body_heading: str | None  # None <=> frontmatter column
    tipo: str
    categoria: str
    semantica_vazio: str

    def __post_init__(self) -> None:
        """Enforce exactly one of frontmatter_key/body_heading."""
        is_frontmatter = self.frontmatter_key is not None
        is_body = self.body_heading is not None
        if is_frontmatter == is_body:
            msg = f"{self.csv_name}: exactly one of frontmatter_key/body_heading must be set"
            raise ValueError(msg)


# Order matches the original CSV header exactly — okf_to_csv.py rebuilds
# the derived CSV in this order (P13.2 CI invariant: ordem preservada).
COLUMNS: tuple[ColumnSpec, ...] = (
    ColumnSpec("NOME", "nome", None, "string", "identidade humana (P1)", "não vazio"),
    ColumnSpec(
        "TIPO DE BENEFICIO",
        "tipo_de_beneficio",
        None,
        "string (enum)",
        "candidato a predicado de seleção (Q3)",
        "a definir",
    ),
    ColumnSpec(
        "ATUALMENTE NO SISTEMA",
        "atualmente_no_sistema",
        None,
        "TRUE/FALSE",
        "estado no Sisprev real — não confundir com status_regra (P2.1)",
        "não vazio",
    ),
    ColumnSpec(
        "CICLO DE VALIDAÇÃO",
        "ciclo_de_validacao",
        None,
        "string (1º-4º)",
        "ordenação do processo de auditoria",
        "não vazio",
    ),
    ColumnSpec(
        "VALIDADO PGE",
        "validado_pge",
        None,
        "TRUE/FALSE",
        "legado — candidato a derivar de atos_validacao (P7)",
        "não vazio",
    ),
    ColumnSpec(
        "VALIDADO PRESIDENCIA",
        "validado_presidencia",
        None,
        "TRUE/FALSE",
        "legado — candidato a derivar de atos_validacao (P7)",
        "não vazio",
    ),
    ColumnSpec("SIMULAVEL", "simulavel", None, "S/N", "candidato a apresentação/interface (Q9)", "a definir"),
    ColumnSpec("TIPO", "tipo", None, "string", "candidato a predicado de seleção (Q3)", "a definir"),
    ColumnSpec(
        "APOS_ESPECIAL",
        "apos_especial",
        None,
        "S/N",
        "candidato a predicado ou apresentação (Q3, Q9)",
        "a definir",
    ),
    ColumnSpec(
        "TIPO_REMUN",
        "tipo_remun",
        None,
        "string",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec("PARIDADE", "paridade", None, "S/N", "candidato a resultado/efeito (Q6)", "a definir"),
    ColumnSpec(
        "TabelaPontuacao",
        "tabelapontuacao",
        None,
        "S/N",
        "a investigar (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "Requisitos da IN Nº 5/2020",
        "requisitos_da_in_no_5_2020",
        None,
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "Relatório p/ Reserva Remunerada por Idade ex-officio",
        "relatorio_p_reserva_remunerada_por_idade_ex_officio",
        None,
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "ADICIONAL_INATIVIDADE",
        "adicional_inatividade",
        None,
        "S/N",
        "candidato a resultado/efeito ou apresentação (Q6, Q9)",
        "a definir",
    ),
    ColumnSpec(
        "DATA_ADM_ATE",
        "data_adm_ate",
        None,
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_ADM_APOS",
        "data_adm_apos",
        None,
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_DIREITO_ATE",
        "data_direito_ate",
        None,
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "DATA_DIREITO_APOS",
        "data_direito_apos",
        None,
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "sentinela — preservada, não interpretada (P5)",
    ),
    ColumnSpec(
        "FUNDAMENTACAO_PROPORCIONAL",
        None,
        "Fundamentação Proporcional",
        "text",
        "fundamentação (corpo)",
        "a definir (Q7 — por que uma regra pode ter as duas fundamentações?)",
    ),
    ColumnSpec(
        "VISIVEL DTC PROPORCIONAL",
        "visivel_dtc_proporcional",
        None,
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "FUNDAMENTACAO_INTEGRAL",
        None,
        "Fundamentação Integral",
        "text",
        "fundamentação (corpo)",
        "a definir (Q7 — por que uma regra pode ter as duas fundamentações?)",
    ),
    ColumnSpec(
        "VISIVEL DTC INTEGRAL",
        "visivel_dtc_integral",
        None,
        "S/N",
        "candidato a apresentação/interface (Q9)",
        "a definir",
    ),
    ColumnSpec(
        "SEXO",
        "sexo",
        None,
        "string (enum)",
        "candidato a predicado de seleção (Q3)",
        "a investigar (Q10 — AMBOS vs. vazio vs. desconhecido vs. não aplicável)",
    ),
    ColumnSpec("INTEGRAL", "integral", None, "S/N", "candidato a resultado/efeito (Q6)", "a definir"),
    ColumnSpec(
        "TIPO_CALCULO",
        "tipo_calculo",
        None,
        "string (enum)",
        "candidato a resultado/efeito (Q6)",
        "a investigar (Q10 — 'Não identificado' sem significado presumido)",
    ),
    ColumnSpec(
        "FUNDAMENTACAO",
        None,
        "Fundamentação",
        "text",
        "fundamentação (corpo)",
        "a definir",
    ),
)

_BY_CSV_NAME: dict[str, ColumnSpec] = {c.csv_name: c for c in COLUMNS}
if len(_BY_CSV_NAME) != len(COLUMNS):
    msg = "COLUMNS has a duplicate csv_name — every original column must appear exactly once (P13.2)"
    raise ValueError(msg)

CSV_COLUMN_NAMES: tuple[str, ...] = tuple(c.csv_name for c in COLUMNS)
BODY_COLUMNS: tuple[str, ...] = tuple(c.csv_name for c in COLUMNS if c.body_heading is not None)
FRONTMATTER_COLUMNS: tuple[str, ...] = tuple(c.csv_name for c in COLUMNS if c.frontmatter_key is not None)
BODY_HEADINGS: dict[str, str] = {c.csv_name: c.body_heading for c in COLUMNS if c.body_heading is not None}
FRONTMATTER_KEYS: dict[str, str] = {
    c.csv_name: c.frontmatter_key for c in COLUMNS if c.frontmatter_key is not None
}
HEADING_TO_CSV_NAME: dict[str, str] = {v: k for k, v in BODY_HEADINGS.items()}


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


def column(csv_name: str) -> ColumnSpec:
    """Look up a column's spec by its original CSV header."""
    return _BY_CSV_NAME[csv_name]


def render_schema_table() -> str:
    """Render the dataset doc's "# Schema" table — one row per COLUMNS entry."""
    lines = [
        "| Coluna | Destino | Tipo | Categoria semântica | Semântica de vazio |",
        "|---|---|---|---|---|",
    ]
    for c in COLUMNS:
        destino = (
            f"`{c.frontmatter_key}` (frontmatter)" if c.frontmatter_key else f"`# {c.body_heading}` (corpo)"
        )
        lines.append(f"| `{c.csv_name}` | {destino} | {c.tipo} | {c.categoria} | {c.semantica_vazio} |")
    return "\n".join(lines)
