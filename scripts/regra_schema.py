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

import datetime
from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


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
        "não ocorre — o valor pode ser sentinela (RFC 0011, `sentinela.py`), nunca vazio",
    ),
    ColumnSpec(
        "DATA_ADM_APOS",
        "data_adm_apos",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1)",
        "não ocorre — o valor pode ser sentinela (RFC 0011, `sentinela.py`), nunca vazio",
    ),
    ColumnSpec(
        "DATA_DIREITO_ATE",
        "data_direito_ate",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "não ocorre — o valor pode ser sentinela (RFC 0011, `sentinela.py`), nunca vazio",
    ),
    ColumnSpec(
        "DATA_DIREITO_APOS",
        "data_direito_apos",
        "datetime (DD/MM/AAAA HH:MM)",
        "elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2)",
        "não ocorre — o valor pode ser sentinela (RFC 0011, `sentinela.py`), nunca vazio",
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
# concept docs (e.g. "/dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md")
# — same scalar-vs-list split as atos_validacao, same JSON-encoded CSV
# handling.
#
# **What an entry asserts** (decision 2026-07-27): "this regra's own
# FUNDAMENTACAO names this provision", not "this regra is legally founded on
# it". The weaker claim is the one the source sustains and the one a check
# can verify; the stronger one is a legal conclusion, reached per regra when
# a human moves it to `revisada` — never derivable from prose.
#
# Entries are therefore **authored**, one at a time, by a human reading the
# regra's own fundamentação and conferring the provision against its source
# — never derived by parsing that prose (RFC 0008: a citation extracted by
# regular expression is a plausible, unverified legal accusation, and nine
# distinct misattributions were found in the reader that used to do it).
# They are never inferred from anything outside the regra and never widened
# past what the prose named; when the owning norm is only implied or the
# cited wording was never transcribed, nothing is linked.
DISPOSITIVOS_KEY = "dispositivos"

# precedentes é uma *lista* de casos concretos em que a regra foi aplicada —
# mesma divisão escalar-vs-lista de atos_validacao e dispositivos, mesmo
# tratamento JSON no CSV derivado.
#
# **Não é `atos_validacao`, e a distinção é a razão de o campo existir.** Um
# ato de validação é a manifestação institucional que *aprova* a regra, e é a
# condição de `status_auditoria: validada` (estado_auditoria exige a lista não
# vazia). Um precedente é o oposto do lado da prova: registra que a regra foi
# **usada** num caso real. Ter sido aplicada não é ter sido validada — aliás é
# no processo que um erro de regra se materializa. Sem um campo próprio, quem
# tem em mãos um número de processo é empurrado para o único campo que existe,
# e uma regra vira `validada` por ter sido usada, com o gate verde e o selo
# aceso no site e no relatório.
#
# Para que serve: o resto do catálogo é a regra *declarada*; o precedente é a
# regra *executada*. É onde se confere se a proporcionalidade foi calculada
# como o art. 17 manda, se a fundamentação impressa no ato bate com a gravada
# no campo, se a janela temporal foi aplicada como está no cadastro.
PRECEDENTES_KEY = "precedentes"


class Precedente(BaseModel):
    """Um caso concreto em que a regra foi aplicada — nunca um ato que a valide.

    ``fonte`` é texto livre pelo mesmo motivo de ``AtoValidacao.fonte``: a Q12
    da RFC 0001 (o SEI é a única origem válida?) segue em aberto, e fixar um
    enum aqui responderia por decreto uma pergunta institucional.

    ``identificador`` costuma ser um número de processo, e **um número de
    processo reidentifica**: com ele, quem tem acesso ao sistema de origem
    chega ao requerimento inteiro, com todo o dado pessoal que uma
    despersonalização removeria. Se isso deve entrar num repositório público é
    decisão de quem coordena a auditoria, registrada na RFC 0010 §4.3 — não do
    schema, que só oferece o lugar.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    identificador: str = Field(min_length=1)
    fonte: str = Field(min_length=1)
    parecer: str | None = None
    observacao: str | None = None


# disposicao_de_achados é a resposta da regra a um achado que **já** a nomeia
# em `regras_afetadas` — nunca a declaração de que o achado existe, e nunca o
# conteúdo dele.
#
# **Uma ponta declara, a outra dispõe.** A spec do corpo já proíbe uma seção
# `# Achados` num `regra-*.md`, e a proibição continua valendo: o achado é o
# dono de *qual é o problema* e de *quais regras alcança*. O que a regra ganha
# é só *como esta regra em particular responde*. Sem essa divisão o campo
# seria a segunda ponta declarando a mesma relação — duas verdades sem gate
# que as reconcilie, exatamente o que a convenção de `dispositivos:` e de
# `precedentes` evita. Aqui existe gate: cada entrada tem de apontar para um
# achado real que nomeie esta regra, senão é disposição de relação que ninguém
# declarou.
#
# **Por que o campo é necessário.** `situacao` é um campo só para toda a
# população do achado, e a população é heterogênea por construção: 43 dos 50
# achados abertos alcançam mais de uma regra, e o `achado-0048` alcança 16 em
# três causas com três consertos diferentes. Ele será resolvido para duas
# delas (basta numerar a emenda) muito antes das quatro que não citam a norma
# em campo algum, e hoje não há como dizer isso — o achado é aberto ou
# resolvido para todas de uma vez.
#
# **Por que não afrouxa o gate.** `revisada` hoje só olha achado
# `bloqueante`, e não existe nenhum: os 50 achados abertos impõem zero ao
# estado da auditoria. Com este campo, toda regra `revisada` passa a precisar
# de disposição escrita para **cada** achado aberto que a nomeie — 195
# obrigações que não existiam. E um achado novo sobre uma regra já `revisada`
# a invalida até que ela disponha dele especificamente, que é a mesma
# semântica de rebaixamento não automático do P7.
#
# **Em achado `bloqueante`, o que a disposição libera depende de qual é ela**
# (decisão 2026-07-30, revendo a proibição categórica anterior). A proibição
# original valia para as três, e o custo apareceu no próprio documento que a
# descrevia: a spec exibia como exemplo canônico uma `nao_impede` para o
# `achado-0022`, que é bloqueante — exemplo reprovado pelo gate que ela
# documentava três parágrafos abaixo.
#
# A preocupação que a originou é real, mas alcança **uma** das disposições:
#
# - `nao_se_aplica` segue **proibida** em bloqueante. É autoabsolvição: a
#   regra acusada afirmando que o defeito não existe nela contradiz
#   diretamente quem a nomeou. Quando a população de um bloqueante estiver
#   errada, quem a corrige é o autor do achado — a regra não encolhe o achado
#   por procuração;
# - `corrigida` é **liberada**, e proibi-la era o caso mais indefensável: a
#   regra consertou o defeito e ficava travada até o autor do achado notar. É
#   afirmação de fato, conferível no diff, não juízo sobre a acusação. Exige
#   `decidido_em >= detectado_em` do achado — não se corrige antes de existir
#   o que corrigir;
# - `encaminhada` (antes `nao_impede`) **libera `revisada` e nunca
#   `validada`**, e é aí que a severidade recupera o dente. `revisada`
#   significa que a auditoria terminou, identificou o defeito e registrou o
#   encaminhamento; `validada` significa que a regra pode receber validação
#   institucional, e isso não deve acontecer com defeito bloqueante ainda
#   reconhecido como real. Em bloqueante ela exige `decisao_pendente_de`.
#
# O nome mudou junto com a semântica, e agora ele a declara: `nao_impede` era
# verdade pela metade — não impede a *revisão*, mas segue impedindo a
# *validação*. Nenhuma das 112 regras usava o campo, então este era o momento
# de acertar o vocabulário sem migração de dado.
DISPOSICAO_ACHADOS_KEY = "disposicao_de_achados"

ACHADO_REF_RE = r"^/achados/achado-\d{4}\.md$"


class DisposicaoDeAchado(BaseModel):
    """Como *esta* regra responde a um achado aberto que a nomeia.

    ``justificativa`` é obrigatória e não vazia de propósito: um achado
    posto de lado sem razão escrita é precisamente o modo de falha que este
    campo existe para impedir. "Ignorado" não é disposição — é omissão com
    um lugar para morar.

    ``decidido_por``/``decidido_em`` são a mesma trilha que o P11 exige de
    ``auditado_por``/``auditado_em``, e pelo mesmo motivo: dispensar um
    achado é decisão, e decisão sem autor nem data é um estado que se
    flipou.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    achado: str = Field(pattern=ACHADO_REF_RE)
    # nao_se_aplica: o defeito descrito não se materializa nesta regra — a
    #   população do achado alcançou além do que devia.
    # encaminhada: o defeito é real aqui, e o que resta não é da auditoria
    #   (decisão do dono do campo, questão de domínio aberta, fluxo
    #   institucional). É a única que faz uma regra avançar carregando um
    #   defeito conhecido, e é por isso que a justificativa é obrigatória — e,
    #   em achado bloqueante, também `decisao_pendente_de`. Libera `revisada`
    #   e nunca `validada`.
    # corrigida: esta regra foi editada e o achado não vale mais para ela,
    #   embora siga aberto para as outras da população.
    disposicao: Literal["nao_se_aplica", "encaminhada", "corrigida"]
    justificativa: str = Field(min_length=1)
    decidido_por: str = Field(min_length=1)
    decidido_em: datetime.date
    # A quem pertence a decisão que falta. Obrigatório quando `encaminhada`
    # dispõe de um achado bloqueante (checado em `estado_auditoria`, que é
    # quem conhece a severidade): "não é da auditoria" sem dizer de quem é
    # deixa o defeito sem dono, e um defeito sem dono não é encaminhamento —
    # é arquivamento com outro nome.
    decisao_pendente_de: str | None = None

    @field_validator("justificativa", "decidido_por", "decisao_pendente_de")
    @classmethod
    def _texto_real(cls, value: str | None) -> str | None:
        if value is not None and not value.strip():
            msg = "exige texto não vazio"
            raise ValueError(msg)
        return value


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
    precedentes: list[Precedente] = Field(default_factory=list)
    disposicao_de_achados: list[DisposicaoDeAchado] = Field(default_factory=list)


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
