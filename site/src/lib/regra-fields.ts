// Canonical grouping of the 27 CSV-derived domain columns (regra_schema.py
// COLUMNS, P13.2) for a regra's detail page — the RFC 0003 §3 requirement
// that the ficha show "o frontmatter como ficha estruturada", i.e. the
// deployable rule in full, not a hand-picked subset. `nome` is the page's
// own <h1> (shown separately, not repeated in a metadata row), so all 26
// *other* columns are grouped here; together with `nome` that's the full 27.
export interface FieldSpec {
  key: string;
  label: string;
}

export interface FieldGroup {
  title: string;
  fields: FieldSpec[];
}

export const REGRA_FIELD_GROUPS: FieldGroup[] = [
  {
    title: "Identidade e benefício",
    fields: [
      { key: "tipo_de_beneficio", label: "Tipo de benefício" },
      { key: "tipo", label: "Tipo" },
      { key: "atualmente_no_sistema", label: "Atualmente no sistema" },
      { key: "apos_especial", label: "Aposentadoria especial" },
      { key: "tipo_remun", label: "Tipo de remuneração" },
      { key: "simulavel", label: "Simulável" },
    ],
  },
  {
    title: "Ciclo e validação",
    fields: [
      { key: "ciclo_de_validacao", label: "Ciclo de validação" },
      { key: "validado_pge", label: "Validado PGE" },
      { key: "validado_presidencia", label: "Validado Presidência" },
    ],
  },
  {
    title: "Elegibilidade temporal",
    fields: [
      { key: "data_adm_ate", label: "Admissão até" },
      { key: "data_adm_apos", label: "Admissão após" },
      { key: "data_direito_ate", label: "Direito até" },
      { key: "data_direito_apos", label: "Direito após" },
    ],
  },
  {
    title: "Cálculo e resultado",
    fields: [
      { key: "sexo", label: "Sexo" },
      { key: "integral", label: "Integral" },
      { key: "tipo_calculo", label: "Tipo de cálculo" },
      { key: "paridade", label: "Paridade" },
      { key: "adicional_inatividade", label: "Adicional de inatividade" },
    ],
  },
  {
    title: "Fundamentação",
    fields: [
      { key: "fundamentacao", label: "Fundamentação" },
      { key: "fundamentacao_integral", label: "Fundamentação integral" },
      { key: "visivel_dtc_integral", label: "Visível DTC integral" },
      { key: "fundamentacao_proporcional", label: "Fundamentação proporcional" },
      { key: "visivel_dtc_proporcional", label: "Visível DTC proporcional" },
    ],
  },
  {
    title: "Requisitos e relatórios administrativos",
    fields: [
      { key: "tabelapontuacao", label: "Tabela de pontuação" },
      { key: "requisitos_da_in_no_5_2020", label: "Requisitos da IN nº 5/2020" },
      {
        key: "relatorio_p_reserva_remunerada_por_idade_ex_officio",
        label: "Relatório p/ reserva remunerada por idade ex officio",
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
