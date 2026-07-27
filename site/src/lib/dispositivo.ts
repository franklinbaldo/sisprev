// Endereço estrutural de um dispositivo, do lado do site (P3/P4).
//
// Porte fiel de `scripts/dispositivo_endereco.py`: as mesmas regras de
// rótulo e de ordem, para que a página e o `index.md` gerado pelo Python
// digam exatamente a mesma coisa. Mantido **puro** — sem import de
// `site-data.ts`, sem `astro:content` — pela mesma razão de `painel.ts` e
// `filtros.ts`: o job `test` do CI roda vitest sem o emissor, então um
// módulo testável que alcance `dados-do-site.json` quebra o CI mesmo
// passando localmente.
//
// Não é duplicação de regra de negócio: a fonte de verdade continua sendo o
// Python (é ele que valida e que recusa o commit). Aqui só se **exibe** o
// que já foi validado lá — e os testes deste arquivo travam as duas
// implementações no mesmo comportamento observável.

export type TipoComponente =
  | "artigo"
  | "caput"
  | "paragrafo"
  | "paragrafo_unico"
  | "inciso"
  | "alinea"
  | "item";

export interface Componente {
  tipo: TipoComponente;
  valor?: string;
  sufixo?: string;
}

// Até onde os incisos deste corpus chegam; forma subtrativa incluída
// porque eles são mesmo escritos IV e IX.
const ROMANOS: ReadonlyArray<readonly [string, number]> = [
  ["C", 100],
  ["XC", 90],
  ["L", 50],
  ["XL", 40],
  ["X", 10],
  ["IX", 9],
  ["V", 5],
  ["IV", 4],
  ["I", 1],
];

const ULTIMO_ORDINAL = 9;

export function romanoParaInt(romano: string): number {
  let total = 0;
  let resto = romano;
  for (const [simbolo, valor] of ROMANOS) {
    while (resto.startsWith(simbolo)) {
      total += valor;
      resto = resto.slice(simbolo.length);
    }
  }
  return resto === "" ? total : 0;
}

/** 1º..9º levam o marcador ordinal; de 10 em diante são cardinais. */
function ordinal(numero: number): string {
  return numero <= ULTIMO_ORDINAL ? `${numero}º` : String(numero);
}

function numeroDe(componente: Componente): number {
  if (componente.tipo === "inciso") return romanoParaInt(componente.valor ?? "");
  if (componente.tipo === "alinea") {
    return (componente.valor ?? "a").charCodeAt(0) - "a".charCodeAt(0) + 1;
  }
  // caput / parágrafo único: singulares por definição, a posição vem do nível.
  return componente.valor === undefined ? 1 : Number.parseInt(componente.valor, 10);
}

/** Fragmento canônico de citação de um nível (P4). */
export function rotuloDoComponente(componente: Componente): string {
  switch (componente.tipo) {
    case "caput":
      return "caput";
    case "paragrafo_unico":
      return "parágrafo único";
    case "inciso":
      return `inciso ${componente.valor}`;
    case "alinea":
      return `alínea ${componente.valor}`;
    case "item":
      return `item ${componente.valor}`;
    default: {
      let numero = ordinal(Number.parseInt(componente.valor ?? "0", 10));
      if (componente.sufixo !== undefined) numero = `${numero}-${componente.sufixo}`;
      return componente.tipo === "artigo" ? `art. ${numero}` : `§ ${numero}`;
    }
  }
}

/** Citação canônica do endereço inteiro — `art. 40, § 1º, inciso I`. */
export function rotuloDoEndereco(componentes: readonly Componente[]): string {
  return componentes.map(rotuloDoComponente).join(", ");
}

const SLOT: Record<TipoComponente, number> = {
  artigo: 0,
  paragrafo: 1,
  paragrafo_unico: 1,
  caput: 2,
  inciso: 3,
  alinea: 4,
  item: 5,
};

/**
 * Chave de ordem: uma casa fixa por nível, com `0` querendo dizer "este
 * nível não faz parte do endereço". É esse zero que torna a ordem *legal*
 * em vez de meramente lexicográfica — um inciso do caput (casa do parágrafo
 * em `0`) vem antes do § 1º, que é como o artigo se lê.
 *
 * Devolve um array comparável elemento a elemento por `compararEnderecos`.
 */
export function chaveDeOrdem(componentes: readonly Componente[]): Array<number | string> {
  const porSlot = new Map<number, Componente>();
  for (const componente of componentes) {
    if (!porSlot.has(SLOT[componente.tipo])) porSlot.set(SLOT[componente.tipo], componente);
  }
  const numero = (slot: number): number => {
    const componente = porSlot.get(slot);
    return componente === undefined ? 0 : numeroDe(componente);
  };
  const sufixo = (slot: number): string => porSlot.get(slot)?.sufixo ?? "";

  return [
    numero(SLOT.artigo),
    sufixo(SLOT.artigo),
    numero(SLOT.paragrafo),
    sufixo(SLOT.paragrafo),
    numero(SLOT.inciso),
    numero(SLOT.alinea),
    numero(SLOT.item),
    // O caput não tem casa própria — "sem inciso" já o coloca à frente dos
    // incisos da sua unidade. Só falta distingui-lo do endereço da unidade
    // inteira, que é o papel deste último segmento.
    componentes.map((c) => `${c.tipo}${c.valor ?? ""}${c.sufixo ?? ""}`).join("-"),
  ];
}

/** Comparador para `Array.prototype.sort`, sobre `chaveDeOrdem`. */
export function compararEnderecos(a: readonly Componente[], b: readonly Componente[]): number {
  const chaveA = chaveDeOrdem(a);
  const chaveB = chaveDeOrdem(b);
  for (let i = 0; i < chaveA.length; i += 1) {
    const x = chaveA[i];
    const y = chaveB[i];
    if (x === y) continue;
    if (typeof x === "number" && typeof y === "number") return x - y;
    return String(x) < String(y) ? -1 : 1;
  }
  return 0;
}

/**
 * Rótulo da redação, para quando duas fichas do mesmo dispositivo precisam
 * ser distinguidas numa lista. `apelido` chega do `norma.md` da norma
 * alteradora quando ela está no vocabulário; sem ele, mostra-se a chave —
 * nunca uma string vazia, que esconderia a diferença entre as redações.
 */
export function rotuloDaRedacao(redacaoId: string, apelido?: string): string {
  if (redacaoId === "original") return "redação original";
  return `redação dada por ${apelido ?? redacaoId}`;
}
