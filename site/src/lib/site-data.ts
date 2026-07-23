// Typed access to dados-do-site.json (RFC 0003 §4) — the emitter's minimal
// audit-state bridge. This file is the *only* place that trusts the JSON's
// shape; every page reads through the typed getters below, never the raw
// import, and never a content collection's raw frontmatter for anything
// this bridge covers (status_auditoria, validado_*, situacao, severidade,
// regras_afetadas) — that field is the whole point of the bridge (RFC 0003
// §4): the *effective*, P7-joined value, not whatever happens to be
// written in the .md. Validated with Zod (not just cast, and not with
// loose types) so a malformed/stale emitter output fails the build loudly
// instead of rendering a wrong or blank seal.
import { z } from "zod";
import raw from "../data/dados-do-site.json";

// scripts/emit_site_data.py::SCHEMA_VERSION — a literal, not a bare number:
// a version bump is a breaking contract change the site must consciously
// migrate to, never silently accept because "some number" was present.
const SCHEMA_VERSION = 1;

const RegraStateSchema = z.object({
  status_auditoria: z.enum(["importada", "revisada", "validada"]),
  validado_pge: z.boolean(),
  validado_presidencia: z.boolean(),
  ciclo_de_validacao: z.string().min(1),
});

const AchadoStateSchema = z.object({
  situacao: z.enum(["aberto", "resolvido"]),
  severidade: z.enum(["bloqueante", "informativo"]),
  regras_afetadas: z.array(z.string()),
});

const SiteDataSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION),
  sha: z.string().regex(/^[0-9a-f]{40}$/, "sha must be a 40-character lowercase hex commit SHA"),
  generated_at: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "generated_at must be an ISO date (YYYY-MM-DD)"),
  regras: z.record(z.string(), RegraStateSchema),
  achados: z.record(z.string(), AchadoStateSchema),
});

export type RegraState = z.infer<typeof RegraStateSchema>;
export type AchadoState = z.infer<typeof AchadoStateSchema>;

const siteData = SiteDataSchema.parse(raw);

/** Exact source commit SHA this build's dados-do-site.json was generated from. */
export const sha = siteData.sha;

/** Short (9-char) form of `sha`, for compact display. */
export const shortSha = sha.slice(0, 9);

/** ISO date (YYYY-MM-DD) of the source commit — the snapshot's freshness date. */
export const generatedAt = siteData.generated_at;

/**
 * The regra's effective audit state (status_auditoria, validado_*, ciclo).
 *
 * Throws if `regraId` is unknown to dados-do-site.json — a regra the
 * content collection can see but the emitter can't means the emitter ran
 * against a different, stale bundle state. That must fail the build loudly
 * (RFC 0003 §2: "não há como divergir silenciosamente"), never fall back to
 * a guessed default like "importada" for a regra the emitter never actually
 * looked at.
 */
export function getRegraState(regraId: string): RegraState {
  const state = siteData.regras[regraId];
  if (!state) {
    throw new Error(
      `dados-do-site.json has no entry for regra "${regraId}" — the emitter ` +
        "(scripts/emit_site_data.py) ran against a bundle state that doesn't " +
        "match what Astro's content collection sees. Re-run site/scripts/emit-data.sh.",
    );
  }
  return state;
}

/**
 * The achado's effective state (situacao, severidade, regras_afetadas).
 *
 * Throws if `achadoId` is unknown, for the same reason `getRegraState` does.
 */
export function getAchadoState(achadoId: string): AchadoState {
  const state = siteData.achados[achadoId];
  if (!state) {
    throw new Error(
      `dados-do-site.json has no entry for achado "${achadoId}" — the emitter ` +
        "(scripts/emit_site_data.py) ran against a bundle state that doesn't " +
        "match what Astro's content collection sees. Re-run site/scripts/emit-data.sh.",
    );
  }
  return state;
}

/** Every achado id currently affecting a given regra id (reverse of regras_afetadas). */
export function achadosAffectingRegra(regraId: string): string[] {
  return Object.entries(siteData.achados)
    .filter(([, state]) => state.regras_afetadas.includes(regraId))
    .map(([achadoId]) => achadoId)
    .sort();
}

/**
 * Whether any regra has completed the audit cycle (status_auditoria "validada").
 *
 * Drives noindex and the audit banner's wording (RFC 0003 §5) as a live
 * computation, not a flag a human could forget to flip back — the
 * directive stops applying automatically the moment it stops being true.
 */
export const hasAnyValidatedRegra = Object.values(siteData.regras).some(
  (regra) => regra.status_auditoria === "validada",
);
