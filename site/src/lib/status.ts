// Shared mapping from raw audit state to a StatusBadge's {tone, label} —
// one place so every page (index, detail, future search) reads the same
// wording (RFC 0003 §5: selos em todas as superfícies, consistentemente).
import type { AchadoState, RegraState } from "./site-data";

const STATUS_AUDITORIA_LABEL: Record<string, string> = {
  importada: "Importada",
  revisada: "Revisada",
  validada: "Validada",
};

export function regraStatusBadge(state: RegraState): { tone: "auditoria" | "validado"; label: string } {
  const label = STATUS_AUDITORIA_LABEL[state.status_auditoria];
  return state.status_auditoria === "validada" ? { tone: "validado", label } : { tone: "auditoria", label };
}

export function validadoBadgeLabel(state: RegraState): string {
  const pge = state.validado_pge ? "PGE ✓" : "PGE ✗";
  const presidencia = state.validado_presidencia ? "Presidência ✓" : "Presidência ✗";
  return `${pge} · ${presidencia}`;
}

export function achadoStatusBadge(
  state: AchadoState,
): { tone: "bloqueante" | "neutro" | "validado"; label: string } {
  if (state.situacao === "aberto" && state.severidade === "bloqueante") {
    return { tone: "bloqueante", label: "Aberto · bloqueante" };
  }
  if (state.situacao === "aberto") {
    return { tone: "neutro", label: "Aberto · informativo" };
  }
  return { tone: "validado", label: "Resolvido" };
}
