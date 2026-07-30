// Shared mapping from raw audit state to a StatusBadge's {tone, label} —
// one place so every page (index, detail, future search) reads the same
// wording (RFC 0003 §5: selos em todas as superfícies, consistentemente).
import type { AchadoState, RegraState } from "./site-data";

const STATUS_AUDITORIA_LABEL: Record<string, string> = {
  importada: "Importada",
  revisada: "Revisada",
  validada: "Validada",
};

/**
 * Os três valores de `status_auditoria` (P7) com o rótulo que as listagens
 * exibem — a mesma fonte de wording dos selos, para que a opção do filtro e
 * o selo do card nunca digam a mesma coisa com palavras diferentes.
 */
export const OPCOES_STATUS_AUDITORIA: ReadonlyArray<{ valor: string; rotulo: string }> = [
  "importada",
  "revisada",
  "validada",
].map((valor) => ({ valor, rotulo: STATUS_AUDITORIA_LABEL[valor] }));

/** Situação e severidade de um achado (P14), no mesmo padrão de opções das listagens. */
export const OPCOES_SITUACAO_ACHADO: ReadonlyArray<{ valor: string; rotulo: string }> = [
  { valor: "aberto", rotulo: "Aberto" },
  { valor: "resolvido", rotulo: "Resolvido" },
];

export const OPCOES_SEVERIDADE_ACHADO: ReadonlyArray<{ valor: string; rotulo: string }> = [
  { valor: "bloqueante", rotulo: "Bloqueante" },
  { valor: "informativo", rotulo: "Informativo" },
];

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
  if (state.situacao === "improcedente") {
    return { tone: "neutro", label: "Improcedente" };
  }
  return { tone: "validado", label: "Resolvido" };
}
