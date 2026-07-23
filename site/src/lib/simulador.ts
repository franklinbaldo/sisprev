// Simulador de requerimento (RFC 0002) — motor de avaliação trivalente.
//
// Implementa RFC 0002 §4 ao pé da letra: cada regra recebe compatível
// (todos os critérios conhecidos e satisfeitos, nenhum desconhecido capaz
// de mudar a seleção), incompatível (um critério confirmado exclui), ou
// indeterminada (há pendência — fato ou semântica — capaz de mudar o
// resultado). O desfecho agregado da solicitação segue §4 também: se
// QUALQUER regra restante é indeterminada, o conjunto inteiro é
// `indeterminado` (a pendência pode mudar única/múltiplas), nunca só as
// que sobraram "compatíveis" contam.
//
// Only the fields that actually vary in the catalog are used as match
// criteria (tipo_de_beneficio, sexo, apos_especial, the two date windows —
// `tipo` and `tipo_remun` are constant across all 112 regras today, so they
// carry no discriminating information). `integral`/`tipo_calculo`/
// `paridade` are RFC 0002 §3's "resultado candidato" fields — shown for
// context, never used to filter, since selecting between them requires the
// "causa da incapacidade" fact this catalog does not have (RFC 0002 §3,
// Q6).
import { parseDataSisprev, parseSN } from "./parse-sisprev";

export interface RegraSimulador {
  id: string;
  nome: string;
  tipoDeBeneficio: string;
  /** Raw catalog value: `""`, `"AMBOS"`, `"MASCULINO"`, or `"FEMININO"`. */
  sexo: string;
  aposEspecial: boolean | null;
  simulavel: boolean | null;
  statusRegra: string | null;
  dataAdmApos: Date | null;
  dataAdmAte: Date | null;
  dataDireitoApos: Date | null;
  dataDireitoAte: Date | null;
  /** Resultado candidato (RFC 0002 §3) — nunca usado como critério de filtro. */
  integral: boolean | null;
  tipoCalculo: string;
  paridade: boolean | null;
}

export interface FatosRequerimento {
  tipoDeBeneficio: string;
  sexo: "MASCULINO" | "FEMININO" | null;
  aposEspecial: boolean | null;
  dataAdmissao: Date | null;
  dataDireito: Date | null;
}

export type ValorTrivalente = "compativel" | "incompativel" | "indeterminada";

export interface AvaliacaoRegra {
  regraId: string;
  nome: string;
  valor: ValorTrivalente;
  criteriosSatisfeitos: string[];
  motivoExclusao: string | null;
  fatosPendentes: string[];
}

export type DesfechoAgregado = "nenhuma" | "unica" | "multiplas" | "indeterminado";

export interface RastroSolicitacao {
  desfecho: DesfechoAgregado;
  candidatas: AvaliacaoRegra[];
  eliminadas: AvaliacaoRegra[];
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
 * Reconstrói `RegraSimulador[]` a partir do payload que
 * `simulador.astro` serializa com `JSON.stringify` (datas viram string ISO
 * automaticamente; esta função é a única responsável por desfazer isso no
 * cliente).
 */
export function regrasSimuladorFromJSON(raw: unknown[]): RegraSimulador[] {
  const toDate = (v: unknown): Date | null => (typeof v === "string" ? new Date(v) : null);
  const toBool = (v: unknown): boolean | null => (typeof v === "boolean" ? v : null);
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
      dataAdmApos: toDate(r.dataAdmApos),
      dataAdmAte: toDate(r.dataAdmAte),
      dataDireitoApos: toDate(r.dataDireitoApos),
      dataDireitoAte: toDate(r.dataDireitoAte),
      integral: toBool(r.integral),
      tipoCalculo: String(r.tipoCalculo ?? ""),
      paridade: toBool(r.paridade),
    };
  });
}

type ResultadoJanela =
  | { status: "nao_avaliado" }
  | { status: "satisfeito" }
  | { status: "pendente"; motivo: string }
  | { status: "incompativel"; motivo: string };

function avaliarJanela(fato: Date | null, limiteInferior: Date | null, limiteSuperior: Date | null, label: string): ResultadoJanela {
  if (fato === null) return { status: "nao_avaliado" };

  if (limiteInferior !== null && fato.getTime() === limiteInferior.getTime()) {
    return {
      status: "pendente",
      motivo: `Data de ${label} informada coincide exatamente com o limite inferior da regra — inclusividade do limite ainda não está definida (RFC 0002, Q1/Q2).`,
    };
  }
  if (limiteSuperior !== null && fato.getTime() === limiteSuperior.getTime()) {
    return {
      status: "pendente",
      motivo: `Data de ${label} informada coincide exatamente com o limite superior da regra — inclusividade do limite ainda não está definida (RFC 0002, Q1/Q2).`,
    };
  }
  if (limiteInferior !== null && fato.getTime() < limiteInferior.getTime()) {
    return { status: "incompativel", motivo: `Data de ${label} informada é anterior ao limite inferior da regra.` };
  }
  if (limiteSuperior !== null && fato.getTime() > limiteSuperior.getTime()) {
    return { status: "incompativel", motivo: `Data de ${label} informada é posterior ao limite superior da regra.` };
  }
  if (limiteInferior === null || limiteSuperior === null) {
    return {
      status: "pendente",
      motivo: `Limite de ${label} não preenchido no catálogo para esta regra — não é possível confirmar (valor vazio é sentinela, não interpretado).`,
    };
  }
  return { status: "satisfeito" };
}

function incompativel(regra: RegraSimulador, motivo: string): AvaliacaoRegra {
  return { regraId: regra.id, nome: regra.nome, valor: "incompativel", criteriosSatisfeitos: [], motivoExclusao: motivo, fatosPendentes: [] };
}

/** Avalia uma única regra contra os fatos do requerimento (RFC 0002 §4). */
export function avaliarRegra(regra: RegraSimulador, fatos: FatosRequerimento): AvaliacaoRegra {
  const satisfeitos: string[] = [];
  const pendentes: string[] = [];

  if (regra.tipoDeBeneficio !== fatos.tipoDeBeneficio) {
    return incompativel(regra, `Tipo de benefício da regra ("${regra.tipoDeBeneficio}") diferente do informado ("${fatos.tipoDeBeneficio}").`);
  }
  satisfeitos.push("Tipo de benefício");

  if (regra.sexo === "") {
    pendentes.push("Sexo não está preenchido no catálogo para esta regra (semântica em aberto, RFC 0001 Q10).");
  } else if (regra.sexo === "AMBOS") {
    satisfeitos.push("Sexo (regra aceita ambos)");
  } else if (fatos.sexo === null) {
    pendentes.push("Sexo do requerente não informado.");
  } else if (regra.sexo !== fatos.sexo) {
    return incompativel(regra, `Sexo da regra ("${regra.sexo}") diferente do informado ("${fatos.sexo}").`);
  } else {
    satisfeitos.push("Sexo");
  }

  if (regra.aposEspecial === null) {
    pendentes.push("Aposentadoria especial não está preenchida no catálogo para esta regra.");
  } else if (fatos.aposEspecial === null) {
    pendentes.push("Aposentadoria especial do requerente não informada.");
  } else if (regra.aposEspecial !== fatos.aposEspecial) {
    return incompativel(regra, `Aposentadoria especial da regra ("${regra.aposEspecial ? "sim" : "não"}") diferente do informado.`);
  } else {
    satisfeitos.push("Aposentadoria especial");
  }

  const admissao = avaliarJanela(fatos.dataAdmissao, regra.dataAdmApos, regra.dataAdmAte, "admissão");
  if (admissao.status === "incompativel") return incompativel(regra, admissao.motivo);
  if (admissao.status === "satisfeito") satisfeitos.push("Data de admissão");
  if (admissao.status === "pendente") pendentes.push(admissao.motivo);

  const direito = avaliarJanela(fatos.dataDireito, regra.dataDireitoApos, regra.dataDireitoAte, "aquisição do direito");
  if (direito.status === "incompativel") return incompativel(regra, direito.motivo);
  if (direito.status === "satisfeito") satisfeitos.push("Data de aquisição do direito");
  if (direito.status === "pendente") pendentes.push(direito.motivo);

  if (pendentes.length > 0) {
    return { regraId: regra.id, nome: regra.nome, valor: "indeterminada", criteriosSatisfeitos: satisfeitos, motivoExclusao: null, fatosPendentes: pendentes };
  }
  return { regraId: regra.id, nome: regra.nome, valor: "compativel", criteriosSatisfeitos: satisfeitos, motivoExclusao: null, fatosPendentes: [] };
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
 * Avalia o conjunto (RFC 0002 §4, "por solicitação"). Regras fora do
 * universo (ver `estaNoUniverso`) voltam em `foraDoEscopo`, nunca somem
 * silenciosamente.
 */
export function avaliarSolicitacao(regras: RegraSimulador[], fatos: FatosRequerimento): RastroSolicitacao {
  const universo = regras.filter(estaNoUniverso);
  const foraDoEscopo = regras.filter((r) => !estaNoUniverso(r));

  const avaliacoes = universo.map((r) => avaliarRegra(r, fatos));
  const compativeis = avaliacoes.filter((a) => a.valor === "compativel");
  const indeterminadas = avaliacoes.filter((a) => a.valor === "indeterminada");
  const eliminadas = avaliacoes.filter((a) => a.valor === "incompativel").sort((a, b) => a.regraId.localeCompare(b.regraId));

  let desfecho: DesfechoAgregado;
  if (indeterminadas.length > 0) {
    desfecho = "indeterminado";
  } else if (compativeis.length === 0) {
    desfecho = "nenhuma";
  } else if (compativeis.length === 1) {
    desfecho = "unica";
  } else {
    desfecho = "multiplas";
  }

  const candidatas = [...compativeis, ...indeterminadas].sort((a, b) => a.regraId.localeCompare(b.regraId));

  return { desfecho, candidatas, eliminadas, foraDoEscopo: foraDoEscopo.sort((a, b) => a.id.localeCompare(b.id)) };
}
