// Anotações de auditoria que uma regra carrega no frontmatter e que **não são
// campos do Sisprev**: `atos_validacao` (P7) e `precedentes` (RFC 0010 §6.1).
//
// Módulo próprio, e não parte de `relatorio.ts`, pelo mesmo motivo que levou
// `substituicao_schema.py` a sair de `conjunto_schema.py`: quem lê estas
// anotações não é só o relatório. A ficha da regra no site lê as mesmas duas
// listas, e deixá-las num módulo batizado pelo relatório faria a ficha
// importar de um lugar cujo propósito não é o dela.
//
// Puro, sem `astro:content` nem `site-data.ts` — o job `test` do CI roda
// vitest sem o emissor.
//
// **Os dois campos são deliberadamente distintos, e confundi-los é o erro que
// o segundo existe para evitar.** Um ato de validação *aprova* a regra e é a
// condição de `status_auditoria: validada`; um precedente registra que ela foi
// **usada** num caso concreto. Ter sido aplicada não é ter sido validada —
// aliás é no processo que um erro de regra se materializa, então tratar um
// precedente como ato acenderia o selo de validada justamente onde há mais
// motivo para olhar.

/** Um ato institucional que sustenta `status_auditoria: validada` (P7). */
export interface AtoDeValidacao {
  tipo: string;
  autoridade: string;
  identificador: string;
  fonte: string;
}

/**
 * Os `atos_validacao` de uma regra, lidos do frontmatter.
 *
 * É por aqui que o número do processo (SEI ou o que a Q12 vier a admitir —
 * `fonte` é texto livre de propósito, a RFC não fixou resposta) chega ao
 * relatório. O ato é **o que fecha o laço**: o relatório é o instrumento pelo
 * qual a PGE se manifesta, e o ato registrado depois de assinado é o que marca
 * a regra validada. Imprimi-lo no capítulo é o que permite ao procurador ver,
 * numa remessa seguinte, o que já foi decidido sobre aquela regra e por quem.
 *
 * A forma de cada item já é validada pelo Python (`estado_auditoria.AtoValidacao`,
 * `extra="forbid"`) e o site não constrói sobre bundle inválido — então um
 * item que não seja um objeto não tem como chegar aqui. A guarda existe para
 * que um `.md` malformado durante a edição derrube o capítulo, não a página.
 */
export function atosDeValidacao(dados: Record<string, unknown>): AtoDeValidacao[] {
  const bruto = dados.atos_validacao;
  if (!Array.isArray(bruto)) return [];
  const campo = (item: Record<string, unknown>, chave: string) =>
    item[chave] === undefined || item[chave] === null ? "" : String(item[chave]);
  return bruto
    .filter((item): item is Record<string, unknown> => typeof item === "object" && item !== null)
    .map((item) => ({
      tipo: campo(item, "tipo"),
      autoridade: campo(item, "autoridade"),
      identificador: campo(item, "identificador"),
      fonte: campo(item, "fonte"),
    }));
}

/** Um caso concreto em que a regra já foi aplicada (`precedentes`). */
export interface Precedente {
  identificador: string;
  fonte: string;
  parecer: string;
  observacao: string;
}

/**
 * Os `precedentes` de uma regra — casos em que ela foi aplicada.
 *
 * Deliberadamente separado de `atosDeValidacao`, e a separação é a razão de o
 * campo existir: um ato de validação **aprova** a regra e é a condição de
 * `status_auditoria: validada`; um precedente registra que ela foi **usada**.
 * Ter sido aplicada não é ter sido validada — e é no processo que um erro de
 * regra se materializa, então confundir os dois acenderia o selo de validada
 * exatamente onde há mais motivo para olhar.
 */
export function precedentes(dados: Record<string, unknown>): Precedente[] {
  const bruto = dados.precedentes;
  if (!Array.isArray(bruto)) return [];
  const campo = (item: Record<string, unknown>, chave: string) =>
    item[chave] === undefined || item[chave] === null ? "" : String(item[chave]);
  return bruto
    .filter((item): item is Record<string, unknown> => typeof item === "object" && item !== null)
    .map((item) => ({
      identificador: campo(item, "identificador"),
      fonte: campo(item, "fonte"),
      parecer: campo(item, "parecer"),
      observacao: campo(item, "observacao"),
    }));
}

/** A disposição que a auditoria deu a um achado numa regra específica. */
export interface DisposicaoDeAchado {
  /** Id do achado (`achado-0020`), já sem a ref de caminho. */
  achado: string;
  disposicao: string;
  justificativa: string;
  decididoEm: string;
  decididoPor: string;
}

/**
 * As `disposicao_de_achados` de uma regra — o que a auditoria decidiu sobre
 * cada achado que a alcança.
 *
 * É o campo que sustenta o quadro operativo do relatório: sem ele, o documento
 * afirma que uma regra tem defeito e não diz o que foi feito a respeito. Uma
 * regra sem disposição nenhuma **não** é uma regra sem defeito — é uma regra
 * cuja conferência não concluiu, e o relatório precisa dizer as duas coisas de
 * formas diferentes.
 *
 * A ref canônica (`/achados/achado-0020.md`) vira id aqui, uma vez, para que
 * nenhuma página refaça a mesma manipulação de string.
 */
export function disposicoesDeAchados(dados: Record<string, unknown>): DisposicaoDeAchado[] {
  const bruto = dados.disposicao_de_achados;
  if (!Array.isArray(bruto)) return [];
  const campo = (item: Record<string, unknown>, chave: string) =>
    item[chave] === undefined || item[chave] === null ? "" : String(item[chave]);
  return bruto
    .filter((item): item is Record<string, unknown> => typeof item === "object" && item !== null)
    .map((item) => ({
      achado: campo(item, "achado").replace(/^\/achados\//, "").replace(/\.md$/, ""),
      disposicao: campo(item, "disposicao"),
      justificativa: campo(item, "justificativa"),
      decididoEm: campo(item, "decidido_em"),
      decididoPor: campo(item, "decidido_por"),
    }));
}
