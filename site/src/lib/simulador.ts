// Simulador de requerimento (RFC 0002) — filtro explicável, não avaliador.
//
// Deliberadamente conservador: este motor só declara `excluida` quando um
// critério **conhecido e confirmado** exclui a regra. Tudo o mais é
// `nao_excluida` — nunca "compatível", nunca "candidata única" — porque o
// motor não tem como saber se capturou **todos** os requisitos legais de
// uma regra (idade, tempo de contribuição, causa da incapacidade, o texto
// da própria fundamentação, ...); ele só enxerga os poucos campos
// parametrizados que variam no catálogo hoje. Reivindicar "compatível"
// seria uma alegação de completude que este modelo não pode sustentar (ver
// RFC 0002 §3/§7 e a revisão do PR que motivou este desenho).
//
// Only the fields that actually vary in the catalog are used as match
// criteria (tipo_de_beneficio, sexo, apos_especial, the two date windows —
// `tipo` and `tipo_remun` are constant across all 112 regras today, so they
// carry no discriminating information). `integral`/`tipo_calculo`/
// `paridade` are RFC 0002 §3's "resultado candidato" fields — shown for
// context, never used to filter, since the RFC treats them as fields the
// requerente doesn't supply (they're an outcome, not an intake fact). When
// two `nao_excluida` regras share every known criterion but differ only in
// those resultado fields, that itself is flagged as a pendência (RFC 0002
// §4: multiplicidade que decorre só de um critério não avaliado não pode
// virar uma resposta confiante) — WITHOUT naming a specific cause (e.g.
// "causa da incapacidade"/Q6): the real discriminant could just as well be
// an unconsumed column, free-text `fundamentacao*`, an unparametrized
// manual requirement, or a catalog inconsistency, so this module never
// guesses which.
import { compararDatasCivis, parseDataSisprev, parseSN, type DataCivil } from "./parse-sisprev";

export interface RegraSimulador {
  id: string;
  nome: string;
  tipoDeBeneficio: string;
  /** Raw catalog value: `""`, `"AMBOS"`, `"MASCULINO"`, or `"FEMININO"`. */
  sexo: string;
  aposEspecial: boolean | null;
  simulavel: boolean | null;
  statusRegra: string | null;
  dataAdmApos: DataCivil | null;
  dataAdmAte: DataCivil | null;
  dataDireitoApos: DataCivil | null;
  dataDireitoAte: DataCivil | null;
  /** Resultado candidato (RFC 0002 §3) — nunca usado como critério de filtro. */
  integral: boolean | null;
  tipoCalculo: string;
  paridade: boolean | null;
}

export interface FatosRequerimento {
  tipoDeBeneficio: string;
  sexo: "MASCULINO" | "FEMININO" | null;
  aposEspecial: boolean | null;
  dataAdmissao: DataCivil | null;
  dataDireito: DataCivil | null;
}

/** Só dois valores — nunca "compatível"/"única" (ver docstring do módulo). */
export type ValorFiltro = "nao_excluida" | "excluida";

export interface AvaliacaoRegra {
  regraId: string;
  nome: string;
  valor: ValorFiltro;
  criteriosSatisfeitos: string[];
  motivoExclusao: string | null;
  /** Sempre exibidas, mesmo para `nao_excluida` — nunca uma lista vazia é lida como "sem pendência alguma". */
  fatosPendentes: string[];
}

export interface RastroSolicitacao {
  naoExcluidas: AvaliacaoRegra[];
  excluidas: AvaliacaoRegra[];
  foraDoEscopo: RegraSimulador[];
}

/** Map a content-collection entry's raw `.data` into the normalized shape the engine consumes. */
export function toRegraSimulador(data: Record<string, unknown>): RegraSimulador {
  const str = (key: string): string => (typeof data[key] === "string" ? (data[key] as string) : "");
  return {
    id: str("id"),
    nome: str("nome"),
    tipoDeBeneficio: str("tipo_de_beneficio"),
    sexo: str("sexo"),
    aposEspecial: parseSN(str("apos_especial")),
    simulavel: parseSN(str("simulavel")),
    statusRegra: str("status_regra") || null,
    dataAdmApos: parseDataSisprev(str("data_adm_apos")),
    dataAdmAte: parseDataSisprev(str("data_adm_ate")),
    dataDireitoApos: parseDataSisprev(str("data_direito_apos")),
    dataDireitoAte: parseDataSisprev(str("data_direito_ate")),
    integral: parseSN(str("integral")),
    tipoCalculo: str("tipo_calculo"),
    paridade: parseSN(str("paridade")),
  };
}

/**
 * Reconstrói `RegraSimulador[]` a partir do payload que `simulador.astro`
 * serializa com `JSON.stringify`. Datas são `DataCivil` (objeto plano
 * `{ano,mes,dia}`), então sobrevivem a um JSON.stringify/parse sem qualquer
 * conversão — nenhum `Date`/timezone envolvido em nenhum ponto do pipeline.
 */
export function regrasSimuladorFromJSON(raw: unknown[]): RegraSimulador[] {
  const toBool = (v: unknown): boolean | null => (typeof v === "boolean" ? v : null);
  const toDataCivil = (v: unknown): DataCivil | null => {
    if (v && typeof v === "object" && "ano" in v && "mes" in v && "dia" in v) {
      const r = v as Record<string, unknown>;
      return { ano: Number(r.ano), mes: Number(r.mes), dia: Number(r.dia) };
    }
    return null;
  };
  return raw.map((item) => {
    const r = item as Record<string, unknown>;
    return {
      id: String(r.id ?? ""),
      nome: String(r.nome ?? ""),
      tipoDeBeneficio: String(r.tipoDeBeneficio ?? ""),
      sexo: String(r.sexo ?? ""),
      aposEspecial: toBool(r.aposEspecial),
      simulavel: toBool(r.simulavel),
      statusRegra: typeof r.statusRegra === "string" ? r.statusRegra : null,
      dataAdmApos: toDataCivil(r.dataAdmApos),
      dataAdmAte: toDataCivil(r.dataAdmAte),
      dataDireitoApos: toDataCivil(r.dataDireitoApos),
      dataDireitoAte: toDataCivil(r.dataDireitoAte),
      integral: toBool(r.integral),
      tipoCalculo: String(r.tipoCalculo ?? ""),
      paridade: toBool(r.paridade),
    };
  });
}

type ResultadoJanela =
  | { status: "nao_modelada" }
  | { status: "satisfeito" }
  | { status: "pendente"; motivo: string }
  | { status: "excluida"; motivo: string };

function avaliarJanela(fato: DataCivil | null, limiteInferior: DataCivil | null, limiteSuperior: DataCivil | null, label: string): ResultadoJanela {
  // Regra não modela esta janela (ambos os limites vazios) — não é um
  // critério para esta regra, então a ausência do fato não pesa contra ela.
  if (limiteInferior === null && limiteSuperior === null) {
    return { status: "nao_modelada" };
  }

  // A regra TEM um limite aqui, mas o requerente não informou a data — é
  // exatamente o caso de "fato pendente capaz de mudar o resultado" (RFC
  // 0002 §4), nunca silenciosamente ignorado.
  if (fato === null) {
    return {
      status: "pendente",
      motivo: `Data de ${label} do requerente não informada — necessária para confirmar a janela de elegibilidade desta regra.`,
    };
  }

  if (limiteInferior !== null && compararDatasCivis(fato, limiteInferior) === 0) {
    return {
      status: "pendente",
      motivo: `Data de ${label} informada coincide exatamente com o limite inferior da regra — inclusividade do limite ainda não está definida (RFC 0002, Q1/Q2).`,
    };
  }
  if (limiteSuperior !== null && compararDatasCivis(fato, limiteSuperior) === 0) {
    return {
      status: "pendente",
      motivo: `Data de ${label} informada coincide exatamente com o limite superior da regra — inclusividade do limite ainda não está definida (RFC 0002, Q1/Q2).`,
    };
  }
  if (limiteInferior !== null && compararDatasCivis(fato, limiteInferior) < 0) {
    return { status: "excluida", motivo: `Data de ${label} informada é anterior ao limite inferior da regra.` };
  }
  if (limiteSuperior !== null && compararDatasCivis(fato, limiteSuperior) > 0) {
    return { status: "excluida", motivo: `Data de ${label} informada é posterior ao limite superior da regra.` };
  }
  if (limiteInferior === null || limiteSuperior === null) {
    return {
      status: "pendente",
      motivo: `Limite de ${label} não preenchido no catálogo para esta regra — não é possível confirmar (valor vazio é sentinela, não interpretado).`,
    };
  }
  return { status: "satisfeito" };
}

function excluida(regra: RegraSimulador, motivo: string): AvaliacaoRegra {
  return { regraId: regra.id, nome: regra.nome, valor: "excluida", criteriosSatisfeitos: [], motivoExclusao: motivo, fatosPendentes: [] };
}

/** Avalia uma única regra contra os fatos do requerimento — só exclui por critério confirmado (RFC 0002 §4). */
export function avaliarRegra(regra: RegraSimulador, fatos: FatosRequerimento): AvaliacaoRegra {
  const satisfeitos: string[] = [];
  const pendentes: string[] = [];

  if (regra.tipoDeBeneficio !== fatos.tipoDeBeneficio) {
    return excluida(regra, `Tipo de benefício da regra ("${regra.tipoDeBeneficio}") diferente do informado ("${fatos.tipoDeBeneficio}").`);
  }
  satisfeitos.push("Tipo de benefício");

  if (regra.sexo === "") {
    pendentes.push("Sexo não está preenchido no catálogo para esta regra (semântica em aberto, RFC 0001 Q10).");
  } else if (regra.sexo === "AMBOS") {
    satisfeitos.push("Sexo (regra aceita ambos)");
  } else if (fatos.sexo === null) {
    pendentes.push("Sexo do requerente não informado.");
  } else if (regra.sexo !== fatos.sexo) {
    return excluida(regra, `Sexo da regra ("${regra.sexo}") diferente do informado ("${fatos.sexo}").`);
  } else {
    satisfeitos.push("Sexo");
  }

  if (regra.aposEspecial === null) {
    pendentes.push("Aposentadoria especial não está preenchida no catálogo para esta regra.");
  } else if (fatos.aposEspecial === null) {
    pendentes.push("Aposentadoria especial do requerente não informada.");
  } else if (regra.aposEspecial !== fatos.aposEspecial) {
    return excluida(regra, `Aposentadoria especial da regra ("${regra.aposEspecial ? "sim" : "não"}") diferente do informado.`);
  } else {
    satisfeitos.push("Aposentadoria especial");
  }

  const admissao = avaliarJanela(fatos.dataAdmissao, regra.dataAdmApos, regra.dataAdmAte, "admissão");
  if (admissao.status === "excluida") return excluida(regra, admissao.motivo);
  if (admissao.status === "satisfeito") satisfeitos.push("Data de admissão");
  if (admissao.status === "pendente") pendentes.push(admissao.motivo);

  const direito = avaliarJanela(fatos.dataDireito, regra.dataDireitoApos, regra.dataDireitoAte, "aquisição do direito");
  if (direito.status === "excluida") return excluida(regra, direito.motivo);
  if (direito.status === "satisfeito") satisfeitos.push("Data de aquisição do direito");
  if (direito.status === "pendente") pendentes.push(direito.motivo);

  return { regraId: regra.id, nome: regra.nome, valor: "nao_excluida", criteriosSatisfeitos: satisfeitos, motivoExclusao: null, fatosPendentes: pendentes };
}

function serializarData(data: DataCivil | null): string {
  return data ? `${data.ano}-${data.mes}-${data.dia}` : "vazio";
}

/** Assinatura dos critérios conhecidos de uma regra — duas regras com a mesma assinatura são indistinguíveis pelos fatos que este modelo consegue perguntar. */
function assinaturaCriteriosConhecidos(regra: RegraSimulador): string {
  return [
    regra.tipoDeBeneficio,
    regra.sexo,
    String(regra.aposEspecial),
    serializarData(regra.dataAdmApos),
    serializarData(regra.dataAdmAte),
    serializarData(regra.dataDireitoApos),
    serializarData(regra.dataDireitoAte),
  ].join("|");
}

function assinaturaResultadoCandidato(regra: RegraSimulador): string {
  return [String(regra.integral), regra.tipoCalculo, String(regra.paridade)].join("|");
}

/**
 * Se, dentro de um grupo de regras não excluídas com a mesma assinatura de
 * critérios conhecidos, o resultado candidato (integral/tipo_calculo/
 * paridade) diverge, sinaliza uma pendência explícita em cada uma.
 *
 * Deliberadamente **não** nomeia a causa provável (ex.: "causa da
 * incapacidade"/Q6) — isso não decorre mecanicamente destes dados. O
 * discriminante real pode estar em qualquer lugar que este filtro não
 * consome: outro campo das 27 colunas, `fundamentacao*` em texto livre, um
 * requisito manual/não parametrizado, ou até uma inconsistência do próprio
 * catálogo (0006/0007, por exemplo, têm a causa descrita em texto em
 * `fundamentacao_integral`/`fundamentacao_proporcional` — não é um fato
 * ausente do catálogo, só não está estruturado como predicado). Só citar
 * uma causa específica (Q6 ou outra) quando houver metadado curado ou
 * análise explicitamente vinculada às regras — nunca inferido daqui. Isso
 * nunca gera uma regra "excluída": só adiciona pendência.
 */
function sinalizarDivergenciaEntreRegrasIndistinguiveis(naoExcluidas: AvaliacaoRegra[], regrasPorId: Map<string, RegraSimulador>): void {
  const grupos = new Map<string, AvaliacaoRegra[]>();
  for (const avaliacao of naoExcluidas) {
    const regra = regrasPorId.get(avaliacao.regraId);
    if (!regra) continue;
    const assinatura = assinaturaCriteriosConhecidos(regra);
    const grupo = grupos.get(assinatura) ?? [];
    grupo.push(avaliacao);
    grupos.set(assinatura, grupo);
  }

  for (const grupo of grupos.values()) {
    if (grupo.length < 2) continue;
    const resultados = new Set(grupo.map((a) => assinaturaResultadoCandidato(regrasPorId.get(a.regraId)!)));
    if (resultados.size < 2) continue;
    for (const avaliacao of grupo) {
      const outras = grupo.filter((a) => a.regraId !== avaliacao.regraId).map((a) => a.regraId);
      avaliacao.fatosPendentes.push(
        `Indistinguível de ${outras.join(", ")} pelos critérios estruturados avaliados por este filtro, mas com resultado candidato diferente (integral/tipo de cálculo/paridade). O discriminante pode estar em campo não avaliado, na fundamentação, em requisito manual/não parametrizado, ou decorrer de inconsistência do catálogo — exige revisão humana.`,
      );
    }
  }
}

/**
 * Se a regra participa do universo do simulador: `simulavel` (o flag do
 * próprio sistema de origem, RFC 0001 Q9) e ativa (`status_regra` ausente
 * ou `"ativa"`, mesmo default de `regra_schema.RegraAdminContrato`).
 */
export function estaNoUniverso(regra: RegraSimulador): boolean {
  return regra.simulavel === true && (regra.statusRegra === null || regra.statusRegra === "ativa");
}

/**
 * Avalia o conjunto. Regras fora do universo (ver `estaNoUniverso`) voltam
 * em `foraDoEscopo`, nunca somem silenciosamente. Não há "desfecho
 * agregado" tipo única/múltiplas — só a lista (sempre honesta sobre
 * pendências) de não excluídas.
 */
export function avaliarSolicitacao(regras: RegraSimulador[], fatos: FatosRequerimento): RastroSolicitacao {
  const universo = regras.filter(estaNoUniverso);
  const foraDoEscopo = regras.filter((r) => !estaNoUniverso(r));
  const regrasPorId = new Map(universo.map((r) => [r.id, r]));

  const avaliacoes = universo.map((r) => avaliarRegra(r, fatos));
  const naoExcluidas = avaliacoes.filter((a) => a.valor === "nao_excluida");
  const excluidas = avaliacoes.filter((a) => a.valor === "excluida").sort((a, b) => a.regraId.localeCompare(b.regraId));

  sinalizarDivergenciaEntreRegrasIndistinguiveis(naoExcluidas, regrasPorId);
  naoExcluidas.sort((a, b) => a.regraId.localeCompare(b.regraId));

  return { naoExcluidas, excluidas, foraDoEscopo: foraDoEscopo.sort((a, b) => a.id.localeCompare(b.id)) };
}
