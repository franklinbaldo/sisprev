// Parsing helpers for the raw Sisprev value shapes (regra_schema.py COLUMNS)
// that the simulador (RFC 0002) needs to compare against user input. Kept
// separate from simulador.ts so the fiddly string-format parsing has its own
// focused unit tests, independent of the trivalent matching logic.
//
// `okf/regras-sisprev/regras-sisprev.md`'s schema table is explicit that an
// empty date value is "sentinela — preservada, não interpretada (P5)" — an
// empty DATA_ADM_*/DATA_DIREITO_* is NOT the same as "no limit", it is a
// value this project has deliberately chosen not to interpret. `null` here
// means exactly that: no comparable value, never "unbounded".

/**
 * Parse a Sisprev `DD/MM/AAAA HH:MM` (or bare `DD/MM/AAAA`) date string.
 *
 * Returns `null` for an empty string (the sentinel case above) or anything
 * that doesn't match the expected shape — never throws, since this reads
 * frontmatter values the domain library itself only guarantees are strings
 * (`regra_schema.py`'s COLUMNS types are documented, not enforced).
 */
export function parseDataSisprev(raw: string): Date | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;

  const match = /^(\d{2})\/(\d{2})\/(\d{4})(?:\s+(\d{2}):(\d{2}))?$/.exec(trimmed);
  if (!match) return null;

  const [, day, month, year, hour, minute] = match;
  const date = new Date(
    Number(year),
    Number(month) - 1,
    Number(day),
    hour ? Number(hour) : 0,
    minute ? Number(minute) : 0,
  );
  if (Number.isNaN(date.getTime())) return null;
  return date;
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

/** Parse an `<input type="date">` value (`YYYY-MM-DD`) into a local `Date`, or `null` if blank. */
export function parseIsoDateInput(raw: string): Date | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(trimmed);
  if (!match) return null;
  const [, year, month, day] = match;
  const date = new Date(Number(year), Number(month) - 1, Number(day));
  return Number.isNaN(date.getTime()) ? null : date;
}
