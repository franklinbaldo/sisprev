// Parsing helpers for the raw Sisprev value shapes (regra_schema.py COLUMNS)
// that the simulador (RFC 0002) needs to compare against user input. Kept
// separate from simulador.ts so the fiddly string-format parsing has its own
// focused unit tests, independent of the exclusion-filter logic.
//
// `okf/regras-sisprev/regras-sisprev.md`'s schema table is explicit that an
// empty date value is "sentinela — preservada, não interpretada (P5)" — an
// empty DATA_ADM_*/DATA_DIREITO_* is NOT the same as "no limit", it is a
// value this project has deliberately chosen not to interpret. `null` here
// means exactly that: no comparable value, never "unbounded".
//
// Dates are represented as plain calendar values (`DataCivil`), never as
// `Date`/timestamps. A DATA_ADM_*/DATA_DIREITO_* eligibility window is a
// civil-law date, not an instant — `new Date(y, m, d, ...)` is built from
// *local* time components (build-time Node's local TZ), while an
// `<input type="date">` parsed the same way uses the *browser's* local TZ;
// those two "local"s can differ by hours, so a date exactly on a legal
// boundary could compare unequal depending on the visitor's timezone. Only
// comparing plain {ano, mes, dia} integers is timezone-proof.

export interface DataCivil {
  ano: number;
  mes: number;
  dia: number;
}

const DIAS_NO_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function isAnoBissexto(ano: number): boolean {
  return (ano % 4 === 0 && ano % 100 !== 0) || ano % 400 === 0;
}

function diasNoMes(ano: number, mes1indexado: number): number {
  if (mes1indexado === 2 && isAnoBissexto(ano)) return 29;
  return DIAS_NO_MES[mes1indexado - 1];
}

/** Valida (sem construir nenhum `Date`) que ano/mês/dia formam uma data civil real — rejeita, por exemplo, 31/02. */
function validarDataCivil(ano: number, mes: number, dia: number): DataCivil | null {
  if (!Number.isInteger(ano) || !Number.isInteger(mes) || !Number.isInteger(dia)) return null;
  if (mes < 1 || mes > 12) return null;
  if (dia < 1 || dia > diasNoMes(ano, mes)) return null;
  return { ano, mes, dia };
}

/** Compara duas datas civis: negativo se `a` < `b`, zero se iguais, positivo se `a` > `b`. */
export function compararDatasCivis(a: DataCivil, b: DataCivil): number {
  if (a.ano !== b.ano) return a.ano - b.ano;
  if (a.mes !== b.mes) return a.mes - b.mes;
  return a.dia - b.dia;
}

/**
 * Parse a Sisprev `DD/MM/AAAA HH:MM` (ou `DD/MM/AAAA` sem hora) — a hora é
 * ignorada de propósito (ver nota de topo: comparação é por data civil, não
 * por instante).
 *
 * Returns `null` for an empty string (the sentinel case above) or anything
 * that doesn't match the expected shape/isn't a real calendar date — never
 * throws, since this reads frontmatter values the domain library itself
 * only guarantees are strings (`regra_schema.py`'s COLUMNS types are
 * documented, not enforced).
 */
export function parseDataSisprev(raw: string): DataCivil | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;

  const match = /^(\d{2})\/(\d{2})\/(\d{4})(?:\s+(\d{2}):(\d{2}))?$/.exec(trimmed);
  if (!match) return null;

  const [, dia, mes, ano, hora, minuto] = match;
  // A hora é ignorada na comparação (ver nota de topo), mas um valor de
  // hora/minuto impossível (ex.: 99:99) indica uma string malformada — o
  // mesmo padrão de "rejeitar em vez de normalizar silenciosamente" que
  // vale para a data também vale aqui, mesmo a hora não sendo comparada.
  if (hora !== undefined && (Number(hora) > 23 || Number(minuto) > 59)) return null;

  return validarDataCivil(Number(ano), Number(mes), Number(dia));
}

/**
 * Parse a Sisprev `S`/`N` flag. Returns `null` for an empty string (the
 * catalog's own "a definir" empty-semantics for these columns) or anything
 * else unrecognized — never coerces an unexpected value into `false`.
 */
export function parseSN(raw: string): boolean | null {
  const trimmed = raw.trim().toUpperCase();
  if (trimmed === "S") return true;
  if (trimmed === "N") return false;
  return null;
}

/** Parse an `<input type="date">` value (`YYYY-MM-DD`) into a `DataCivil`, or `null` if blank/invalid. */
export function parseIsoDateInput(raw: string): DataCivil | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(trimmed);
  if (!match) return null;
  const [, ano, mes, dia] = match;
  return validarDataCivil(Number(ano), Number(mes), Number(dia));
}
