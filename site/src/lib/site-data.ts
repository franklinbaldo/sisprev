// Typed access to dados-do-site.json (RFC 0003 §4) — the emitter's minimal
// audit-state bridge. This file is the *only* place that trusts the JSON's
// shape; every page reads through the typed getters below, never the raw
// import. Validated with Zod (not just cast) so a malformed/stale emitter
// output fails the build loudly instead of rendering a blank seal.
import { z } from "zod";
import raw from "../data/dados-do-site.json";

const RegraStateSchema = z.object({
  status_auditoria: z.string(),
  validado_pge: z.boolean(),
  validado_presidencia: z.boolean(),
  ciclo_de_validacao: z.string(),
});

const AchadoStateSchema = z.object({
  situacao: z.enum(["aberto", "resolvido"]),
  severidade: z.enum(["bloqueante", "informativo"]),
  regras_afetadas: z.array(z.string()),
});

const SiteDataSchema = z.object({
  schema_version: z.number(),
  sha: z.string().min(1),
  generated_at: z.string().min(1),
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

/** The regra's effective audit state (status_auditoria, validado_*, ciclo), or undefined if unknown. */
export function getRegraState(regraId: string): RegraState | undefined {
  return siteData.regras[regraId];
}

/** The achado's effective state (situacao, severidade, regras_afetadas), or undefined if unknown. */
export function getAchadoState(achadoId: string): AchadoState | undefined {
  return siteData.achados[achadoId];
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
 * Drives noindex (RFC 0003 §5: "enquanto nenhuma regra estiver validada") as
 * a live computation, not a flag a human could forget to flip back — the
 * directive stops applying automatically the moment it stops being true.
 */
export const hasAnyValidatedRegra = Object.values(siteData.regras).some(
  (regra) => regra.status_auditoria === "validada",
);
