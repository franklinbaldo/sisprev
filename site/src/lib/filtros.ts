// Lógica pura das listagens filtráveis (RFC 0003 §3: regras "filtrável por
// `tipo_de_beneficio`, `ciclo_de_validacao`, `status_auditoria`"; achados
// "listagem por `situacao` e `severidade`").
//
// Filtrar aqui é **esconder linhas já renderizadas**, nunca buscar dados: o
// site é estático e todas as fichas saem no HTML do build. Sem JavaScript a
// listagem continua inteira e legível — a barra de filtros é progressive
// enhancement, revelada pelo cliente (`filtros-client.ts`), nunca um
// controle morto para quem não executa JS.
//
// O estado do filtro é serializável para query string de propósito: é o que
// permite o painel da home linkar direto para "as 22 regras do ciclo 1º" e
// o leitor compartilhar um recorte por URL. A URL do filtro é um rótulo de
// navegação, não uma identidade — o contrato de URLs estáveis da §4 vale
// para as fichas (`/regras/regra-0006/`), que continuam intocadas.

/** Nome do parâmetro de busca livre na query string. */
export const PARAM_BUSCA = "q";

export interface ItemFiltravel {
  /** Todo o texto pesquisável do item, já concatenado (nome, id, ...). */
  busca: string;
  /** Valor de cada faceta do item, na chave do controle correspondente. */
  facetas: Readonly<Record<string, string>>;
}

export interface EstadoFiltro {
  busca: string;
  /** Valor escolhido em cada faceta; string vazia = faceta não restringe nada. */
  facetas: Readonly<Record<string, string>>;
}

/**
 * Forma canônica de comparação de texto: sem acentos e em minúsculas, para
 * que "pensao" ache "Pensão" — quem digita numa busca raramente acentua, e
 * um catálogo em português inteiro acentuado tornaria a busca inútil.
 */
export function normalizarBusca(texto: string): string {
  return texto
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase();
}

/**
 * `true` se o item satisfaz o filtro inteiro.
 *
 * Busca: **todos** os termos digitados precisam aparecer (E, não OU) — é o
 * que faz "pensao 1998" refinar em vez de alargar. Faceta vazia não
 * restringe; faceta preenchida exige igualdade exata com o valor do item
 * (as opções são geradas a partir dos próprios valores do catálogo, então
 * não há normalização a fazer entre controle e item).
 */
export function itemCorrespondeAoFiltro(item: ItemFiltravel, estado: EstadoFiltro): boolean {
  for (const [chave, valor] of Object.entries(estado.facetas)) {
    if (valor !== "" && item.facetas[chave] !== valor) return false;
  }

  const termos = normalizarBusca(estado.busca).split(/\s+/).filter(Boolean);
  if (termos.length === 0) return true;

  const alvo = normalizarBusca(item.busca);
  return termos.every((termo) => alvo.includes(termo));
}

/**
 * Lê o estado do filtro de uma query string, considerando apenas as facetas
 * declaradas pela página — um parâmetro desconhecido é ignorado, nunca vira
 * uma faceta que nenhum controle sabe exibir nem limpar.
 */
export function estadoFiltroDeParams(params: URLSearchParams, chaves: readonly string[]): EstadoFiltro {
  const facetas: Record<string, string> = {};
  for (const chave of chaves) facetas[chave] = params.get(chave) ?? "";
  return { busca: params.get(PARAM_BUSCA) ?? "", facetas };
}

/**
 * Serializa o estado do filtro, omitindo tudo que está vazio — o estado
 * "sem filtro nenhum" precisa produzir uma URL limpa, sem `?q=&tipo=`
 * pendurado, senão toda navegação suja o histórico com ruído.
 */
export function paramsDeEstadoFiltro(estado: EstadoFiltro): URLSearchParams {
  const params = new URLSearchParams();
  if (estado.busca.trim() !== "") params.set(PARAM_BUSCA, estado.busca.trim());
  for (const [chave, valor] of Object.entries(estado.facetas)) {
    if (valor !== "") params.set(chave, valor);
  }
  return params;
}

/** `true` quando nenhum critério está ativo — usado para decidir se há o que "limpar". */
export function filtroEstaVazio(estado: EstadoFiltro): boolean {
  return estado.busca.trim() === "" && Object.values(estado.facetas).every((valor) => valor === "");
}
