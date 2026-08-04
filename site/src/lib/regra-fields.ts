// Canonical grouping of the 27 CSV-derived domain columns (regra_schema.py
// COLUMNS, P13.2) for a regra's detail page — the RFC 0003 §3 requirement
// that the ficha show "o frontmatter como ficha estruturada", i.e. the
// deployable rule in full, not a hand-picked subset. `nome` is the page's
// own <h1> (shown separately, not repeated in a metadata row), so all 26
// *other* columns are grouped here; together with `nome` that's the full 27.
//
// Cada campo declara **como é lido** (`formato`) — a conversão mora em
// `formato.ts`, que preserva o valor bruto do catálogo ao lado da leitura
// amigável e nunca interpreta sentinela (ver o topo daquele módulo). Um
// campo sem `formato` sai verbatim, que é o padrão seguro: só se declara
// formato para a coluna cujo vocabulário o projeto já fixou.
import { formatarValor, type FormatoCampo, type ValorFormatado } from "./formato";
import { sentinelaDe } from "./sentinela";

/**
 * O que a ficha e o relatório dizem ao lado de um limite sentinela.
 *
 * Uma sentinela é ausência de limite naquele eixo — `31/12/2099` não é uma
 * fronteira em 2099, e `01/01/1900` não exige ingresso depois de 1900. A nota
 * diz isso, porque o silêncio anterior tinha o efeito contrário do pretendido:
 * quem lê `31/12/2099` numa tabela sem ressalva entende uma data real, e essa
 * leitura errada é justamente a que a nota existe para impedir.
 *
 * O valor exibido continua sendo o que está gravado: a nota acompanha, nunca
 * substitui, para que quem audita compare a ficha com o repositório.
 */
export const NOTA_DE_SENTINELA = "sentinela: sem limite neste eixo — a data não é uma fronteira real";

export interface FieldSpec {
  key: string;
  label: string;
  formato?: FormatoCampo;
  /**
   * Campo de texto longo (as três `fundamentacao*`) — ocupa a linha inteira
   * da grade em vez de uma célula de coluna. Uma fundamentação de 60 palavras
   * espremida numa célula de 14rem é ilegível, e ela é justamente o campo que
   * quem confere a própria regra mais precisa ler.
   */
  largo?: boolean;
}

export interface FieldGroup {
  title: string;
  /** Âncora estável da seção, usada pelo índice lateral da ficha. */
  id: string;
  fields: FieldSpec[];
}

export const REGRA_FIELD_GROUPS: FieldGroup[] = [
  {
    title: "Identidade e benefício",
    id: "identidade",
    fields: [
      { key: "tipo_de_beneficio", label: "Tipo de benefício" },
      { key: "tipo", label: "Tipo" },
      { key: "atualmente_no_sistema", label: "Atualmente no sistema", formato: "booleano" },
      { key: "apos_especial", label: "Aposentadoria especial", formato: "sn" },
      { key: "tipo_remun", label: "Tipo de remuneração" },
      { key: "simulavel", label: "Simulável", formato: "sn" },
    ],
  },
  {
    title: "Ciclo e validação",
    id: "ciclo-e-validacao",
    fields: [
      { key: "ciclo_de_validacao", label: "Ciclo de validação" },
      { key: "validado_pge", label: "Validado PGE", formato: "booleano" },
      { key: "validado_presidencia", label: "Validado Presidência", formato: "booleano" },
    ],
  },
  {
    title: "Elegibilidade temporal",
    id: "elegibilidade-temporal",
    fields: [
      { key: "data_adm_ate", label: "Admissão até", formato: "data" },
      { key: "data_adm_apos", label: "Admissão após", formato: "data" },
      { key: "data_direito_ate", label: "Direito até", formato: "data" },
      { key: "data_direito_apos", label: "Direito após", formato: "data" },
    ],
  },
  {
    title: "Cálculo e resultado",
    id: "calculo-e-resultado",
    fields: [
      { key: "sexo", label: "Sexo" },
      { key: "integral", label: "Integral", formato: "sn" },
      { key: "tipo_calculo", label: "Tipo de cálculo" },
      { key: "paridade", label: "Paridade", formato: "sn" },
      { key: "adicional_inatividade", label: "Adicional de inatividade", formato: "sn" },
    ],
  },
  {
    title: "Fundamentação",
    id: "fundamentacao",
    fields: [
      { key: "fundamentacao", label: "Fundamentação", largo: true },
      { key: "fundamentacao_integral", label: "Fundamentação integral", largo: true },
      { key: "visivel_dtc_integral", label: "Visível DTC integral", formato: "sn" },
      { key: "fundamentacao_proporcional", label: "Fundamentação proporcional", largo: true },
      { key: "visivel_dtc_proporcional", label: "Visível DTC proporcional", formato: "sn" },
    ],
  },
  {
    title: "Requisitos e relatórios administrativos",
    id: "requisitos-administrativos",
    fields: [
      { key: "tabelapontuacao", label: "Tabela de pontuação", formato: "sn" },
      { key: "requisitos_da_in_no_5_2020", label: "Requisitos da IN nº 5/2020", formato: "sn" },
      {
        key: "relatorio_p_reserva_remunerada_por_idade_ex_officio",
        label: "Relatório p/ reserva remunerada por idade ex officio",
        formato: "sn",
      },
    ],
  },
];

/** Total domain columns covered by REGRA_FIELD_GROUPS, excluding `nome` (shown as the page title). */
export const GROUPED_FIELD_COUNT = REGRA_FIELD_GROUPS.reduce((total, group) => total + group.fields.length, 0);

// Keys deliberately excluded from "Outros campos" — not domain data: shown
// elsewhere (title, badges, backlinks) or P7/P11/P2.1/identity machinery the
// JSON bridge (site-data.ts) already covers, never a raw content-collection
// read for these specific keys.
const NON_DOMAIN_KEYS = new Set([
  "id",
  "type",
  "row_index",
  "nome",
  "dispositivos",
  "status_regra",
  "status_auditoria",
  "motivo_inativacao",
  "auditado_por",
  "auditado_em",
  "atos_validacao",
  "precedentes",
]);

const GROUPED_KEYS = new Set(REGRA_FIELD_GROUPS.flatMap((group) => group.fields.map((field) => field.key)));

/**
 * Any frontmatter key present on a regra that isn't in a known group and
 * isn't a non-domain field — a future domain field this list hasn't caught
 * up with yet, surfaced instead of silently hidden (RFC 0003 review).
 */
export function otherFields(data: Record<string, unknown>): FieldSpec[] {
  return Object.keys(data)
    .filter((key) => !GROUPED_KEYS.has(key) && !NON_DOMAIN_KEYS.has(key))
    .sort()
    .map((key) => ({ key, label: key }));
}

/** Render one frontmatter value as display text — dates as YYYY-MM-DD, everything else via String(). */
export function fieldValue(data: Record<string, unknown>, key: string): string {
  const value = data[key];
  if (value === null || value === undefined) return "";
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  return String(value);
}

/** Um campo da ficha: a leitura, o bruto quando houve conversão, e a nota quando o valor é sentinela. */
export interface CampoDaFicha extends ValorFormatado {
  /** `NOTA_DE_SENTINELA` quando o valor é um limite sentinela; `null` no resto. */
  nota: string | null;
}

/**
 * O valor do campo pronto para exibição, com o bruto preservado quando houve
 * conversão de formato e a nota de sentinela quando é o caso.
 *
 * A nota mora aqui, e não em `formato.ts`: aquele módulo converte **formato**, e
 * "este valor é uma fronteira convencional" é semântica da regra, não da string.
 * Todo campo `formato: "data"` é uma das quatro colunas de limite temporal — há
 * teste amarrando isso —, então marcar por formato não alcança nenhuma data que
 * não seja limite.
 */
export function campoFormatado(data: Record<string, unknown>, field: FieldSpec): CampoDaFicha {
  const valor = formatarValor(fieldValue(data, field.key), field.formato);
  const eLimiteSentinela = field.formato === "data" && sentinelaDe(fieldValue(data, field.key)) !== null;
  return { ...valor, nota: eLimiteSentinela ? NOTA_DE_SENTINELA : null };
}
