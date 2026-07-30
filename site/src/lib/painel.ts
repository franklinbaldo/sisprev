// Contagens do painel da home (RFC 0003 §3, linha "Painel": "uma home com o
// estado da auditoria: contagens por `status_auditoria`, por `validado_pge`/
// `validado_presidencia`, por ciclo, e achados abertos por severidade").
//
// Funções puras sobre arrays simples, de propósito: o job `test` do CI roda
// vitest **sem** o emissor (`dados-do-site.json` não existe lá), então nada
// aqui pode importar `site-data.ts`. Quem liga uma coisa na outra é a
// própria `site-data.ts`, o único módulo que confia no formato do JSON.
//
// Isto **não** recomputa P7/P14 em JavaScript (RFC 0003 §2): os estados
// contados aqui já vêm calculados pela biblioteca Python; este módulo só
// soma o que o emissor emitiu.

/** O recorte de `RegraState` que o painel conta — estrutural, não o tipo Zod (ver nota de topo). */
export interface EstadoRegraContavel {
  status_auditoria: "importada" | "revisada" | "validada";
  validado_pge: boolean;
  validado_presidencia: boolean;
  ciclo_de_validacao: string;
}

/** O recorte de `AchadoState` que o painel conta. */
export interface EstadoAchadoContavel {
  situacao: "aberto" | "improcedente";
  severidade: "bloqueante" | "informativo";
}

export interface ContagemPorCiclo {
  ciclo: string;
  total: number;
}

export interface ResumoRegras {
  total: number;
  importadas: number;
  revisadas: number;
  validadas: number;
  validadoPge: number;
  validadoPresidencia: number;
  /** Regras com PGE **e** Presidência — o ciclo institucional completo. */
  validadoAmbos: number;
  porCiclo: ContagemPorCiclo[];
}

export interface ResumoAchados {
  total: number;
  abertos: number;
  abertosBloqueantes: number;
  abertosInformativos: number;
  /**
   * Achados cuja acusação não procedia. É o **único** fechamento do próprio
   * achado: um defeito real deixa de pender pela disposição de cada regra
   * alcançada, e não por selo aqui, então não existe contagem de "resolvidos".
   */
  improcedentes: number;
}

/**
 * Ordena rótulos de ciclo (`1º`, `2º`, ...) pelo número que os inicia, caindo
 * para ordem alfabética quando o rótulo não começa por dígito — o campo é
 * `z.string()` no schema justamente para não travar num vocabulário fechado,
 * então um valor futuro fora do padrão precisa ordenar de forma estável em
 * vez de quebrar.
 */
function compararCiclos(a: string, b: string): number {
  const numeroA = Number.parseInt(a, 10);
  const numeroB = Number.parseInt(b, 10);
  const aEhNumero = Number.isFinite(numeroA);
  const bEhNumero = Number.isFinite(numeroB);
  if (aEhNumero && bEhNumero && numeroA !== numeroB) return numeroA - numeroB;
  if (aEhNumero !== bEhNumero) return aEhNumero ? -1 : 1;
  return a.localeCompare(b, "pt-BR");
}

export function resumirRegras(estados: readonly EstadoRegraContavel[]): ResumoRegras {
  const porCiclo = new Map<string, number>();
  const resumo: ResumoRegras = {
    total: estados.length,
    importadas: 0,
    revisadas: 0,
    validadas: 0,
    validadoPge: 0,
    validadoPresidencia: 0,
    validadoAmbos: 0,
    porCiclo: [],
  };

  for (const estado of estados) {
    if (estado.status_auditoria === "importada") resumo.importadas += 1;
    if (estado.status_auditoria === "revisada") resumo.revisadas += 1;
    if (estado.status_auditoria === "validada") resumo.validadas += 1;
    if (estado.validado_pge) resumo.validadoPge += 1;
    if (estado.validado_presidencia) resumo.validadoPresidencia += 1;
    if (estado.validado_pge && estado.validado_presidencia) resumo.validadoAmbos += 1;
    porCiclo.set(estado.ciclo_de_validacao, (porCiclo.get(estado.ciclo_de_validacao) ?? 0) + 1);
  }

  resumo.porCiclo = [...porCiclo.entries()]
    .map(([ciclo, total]) => ({ ciclo, total }))
    .sort((a, b) => compararCiclos(a.ciclo, b.ciclo));

  return resumo;
}

export function resumirAchados(estados: readonly EstadoAchadoContavel[]): ResumoAchados {
  const resumo: ResumoAchados = {
    total: estados.length,
    abertos: 0,
    abertosBloqueantes: 0,
    abertosInformativos: 0,
    improcedentes: 0,
  };

  for (const estado of estados) {
    // Encerrado, e por isso fora da contagem de abertos — mas contado à parte,
    // porque juntá-lo aos abertos afirmaria pendência que não existe.
    if (estado.situacao === "improcedente") {
      resumo.improcedentes += 1;
      continue;
    }
    resumo.abertos += 1;
    if (estado.severidade === "bloqueante") resumo.abertosBloqueantes += 1;
    else resumo.abertosInformativos += 1;
  }

  return resumo;
}
