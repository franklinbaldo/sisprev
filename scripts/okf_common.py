"""Shared constants/helpers for the CSV <-> OKF regras-sisprev conversion."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "data" / "raw" / "regras-sisprev.csv"
DEFAULT_BUNDLE = REPO_ROOT / "okf" / "regras-sisprev"

# Concept doc holding the dataset-level frontmatter (columns, row_count,
# source_file) and the "# Schema" section — see OKF SPEC.md Appendix A,
# where a dataset doc (datasets/sales.md) sits alongside its leaf
# collection (tables/*.md), each with their own index.md.
DATASET_DOC = "regras-sisprev.md"

# Long free-text columns rendered as markdown body sections instead of
# frontmatter — OKF's own guidance: frontmatter for queryable fields, the
# body for prose.
BODY_COLUMNS = ["FUNDAMENTACAO_PROPORCIONAL", "FUNDAMENTACAO_INTEGRAL", "FUNDAMENTACAO"]
BODY_HEADINGS = {
    "FUNDAMENTACAO_PROPORCIONAL": "Fundamentação Proporcional",
    "FUNDAMENTACAO_INTEGRAL": "Fundamentação Integral",
    "FUNDAMENTACAO": "Fundamentação",
}

# (tipo, descrição) per CSV column, for the dataset doc's "# Schema" table.
# Purely descriptive — never read back by okf_to_csv.py.
COLUMN_SCHEMA: dict[str, tuple[str, str]] = {
    "NOME": ("string", "Nome da regra de aposentadoria/pensão."),
    "TIPO DE BENEFICIO": (
        "string (enum)",
        "Categoria do benefício (ex.: APOSENTADORIA POR INVALIDEZ, PENSÃO POR MORTE).",
    ),
    "ATUALMENTE NO SISTEMA": ("TRUE/FALSE", "Se a regra está atualmente implementada no Sisprev."),
    "CICLO DE VALIDAÇÃO": ("string (1º-4º)", "Ciclo de validação jurídica da regra."),
    "VALIDADO PGE": ("TRUE/FALSE", "Se a regra foi validada pela Procuradoria-Geral do Estado."),
    "VALIDADO PRESIDENCIA": (
        "TRUE/FALSE",
        "Se a regra foi validada pela Presidência do órgão previdenciário.",
    ),
    "SIMULAVEL": ("S/N", "Se a regra pode ser usada em simulações de aposentadoria."),
    "TIPO": ("string", "Categoria do servidor (ex.: CIVIL)."),
    "APOS_ESPECIAL": (
        "S/N",
        "Se é uma aposentadoria especial (ex.: magistério, policial, exposição a agentes nocivos).",
    ),
    "TIPO_REMUN": ("string", "Tipo de remuneração aplicável, quando preenchido."),
    "PARIDADE": ("S/N", "Se os proventos têm paridade com a remuneração da ativa."),
    "TabelaPontuacao": ("S/N", "Se a regra usa tabela de pontuação (idade + tempo de contribuição)."),
    "Requisitos da IN Nº 5/2020": ("S/N", "Se a regra segue os requisitos da Instrução Normativa nº 5/2020."),
    "Relatório p/ Reserva Remunerada por Idade ex-officio": (
        "S/N",
        "Se a regra gera relatório de reserva remunerada por idade de ofício.",
    ),
    "ADICIONAL_INATIVIDADE": ("S/N", "Se há adicional de inatividade aplicável."),
    "DATA_ADM_ATE": (
        "datetime (DD/MM/AAAA HH:MM)",
        "Data-limite superior de admissão para a regra se aplicar.",
    ),
    "DATA_ADM_APOS": (
        "datetime (DD/MM/AAAA HH:MM)",
        "Data-limite inferior de admissão para a regra se aplicar.",
    ),
    "DATA_DIREITO_ATE": ("datetime (DD/MM/AAAA HH:MM)", "Data-limite superior de aquisição do direito."),
    "DATA_DIREITO_APOS": ("datetime (DD/MM/AAAA HH:MM)", "Data-limite inferior de aquisição do direito."),
    "FUNDAMENTACAO_PROPORCIONAL": (
        "text",
        "Fundamentação legal do cálculo proporcional (corpo do documento da regra).",
    ),
    "VISIVEL DTC PROPORCIONAL": (
        "S/N",
        "Se a fundamentação proporcional é visível na Declaração de Tempo de Contribuição (DTC).",
    ),
    "FUNDAMENTACAO_INTEGRAL": (
        "text",
        "Fundamentação legal do cálculo integral (corpo do documento da regra).",
    ),
    "VISIVEL DTC INTEGRAL": ("S/N", "Se a fundamentação integral é visível na DTC."),
    "SEXO": ("string (enum)", "Sexo a que a regra se aplica: MASCULINO, FEMININO, AMBOS ou vazio."),
    "INTEGRAL": ("S/N", "Se os proventos são integrais."),
    "TIPO_CALCULO": (
        "string (enum)",
        "Método de cálculo dos proventos (ex.: Valor Efetivo, Valor Médio, "
        "Remuneração de Contribuição, Proporcionalidade Dias).",
    ),
    "FUNDAMENTACAO": ("text", "Fundamentação legal geral/adicional (corpo do documento da regra)."),
}


def render_schema_table(columns: list[str]) -> str:
    """Render the "# Schema" markdown table documenting every CSV column."""
    lines = ["| Coluna | Tipo | Descrição |", "|---|---|---|"]
    for col in columns:
        tipo, descricao = COLUMN_SCHEMA[col]
        lines.append(f"| `{col}` | {tipo} | {descricao} |")
    return "\n".join(lines)


def slugify_column(name: str) -> str:
    """Turn a CSV header into an ASCII snake_case frontmatter key."""
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "_", ascii_name).strip("_").lower()
