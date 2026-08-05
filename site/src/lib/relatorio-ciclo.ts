// Núcleo puro do relatório de fechamento de ciclo — o que a página precisa
// *calcular* sobre uma proposta, sem tocar em `astro:content`.
//
// Mesma divisão que `relatorio.ts` já segue, e pelo mesmo motivo operacional:
// o job `test` do CI roda vitest sem o emissor, então um módulo testado que
// alcançasse `dados-do-site.json` quebraria o CI mesmo passando localmente.
// Quem liga isto às coleções é a página `.astro`.
//
// A projeção que este módulo organiza é **autorada**, não compilada: cada
// regra proposta escreve no seu `projecao:` os valores que entrariam no
// cadastro. Nada aqui conclui sobre a regra — ordena, conta e rotula.
//
// Não existe mais um `Conjunto` declarando grupos de substituição à parte
// (RFC 0004, round 11: retirado). A atomicidade do lote de implantação é
// **derivada** do grafo origem↔destino entre as `RegraProposta` do mesmo
// ciclo — o mesmo cálculo que `scripts/derivar.py` faz para
// `data/regras-propostas.csv` — e este módulo replica em TypeScript para o
// relatório de fechamento agrupar seus capítulos.

/** Uma linha projetada, na forma mínima que este módulo precisa conhecer. */
export interface LinhaProjetada {
  proposta: string;
  colunas: Record<string, string>;
}

/** Uma regra proposta, na forma mínima que o cálculo de componentes precisa. */
export interface PropostaDeclarada {
  id: string;
  ciclo: string;
  origensLegacy: string[];
  estadoAuditoria: string;
  estadoImplantacao?: string;
}

/**
 * Um componente conexo do grafo origem↔destino: o conjunto de regras
 * propostas que compartilham, direta ou transitivamente, ao menos uma
 * origem legada — a unidade atômica de implantação
 * (`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada").
 */
export interface ComponenteDeImplantacao {
  origens: string[];
  destinos: string[];
  pronto: boolean;
}

/**
 * Computa os componentes conexos do grafo origem↔destino para as
 * `RegraProposta` de um ciclo — o mesmo cálculo que
 * `scripts/derivar.py::_componentes_conexos` faz em Python.
 *
 * Duas propostas entram no mesmo componente quando compartilham, direta ou
 * transitivamente, ao menos uma origem legada. Um componente está `pronto`
 * quando **todos** os seus membros têm `estadoAuditoria === "concluida"` e
 * `estadoImplantacao` ausente, `"confirmada"` ou `"confirmada_com_ressalva"`
 * (RFC 0004, round 12 — `confirmada_com_ressalva` entra na carga de
 * homologação levando ressalva, não bloqueia a entrada do componente).
 */
export function componentesDoCiclo(
  ciclo: string,
  propostas: PropostaDeclarada[],
): ComponenteDeImplantacao[] {
  const doCiclo = propostas.filter((proposta) => proposta.ciclo === ciclo);

  const pai = new Map<string, string>();
  const achar = (x: string): string => {
    let raiz = x;
    while (pai.get(raiz) !== raiz) {
      const proximo = pai.get(raiz);
      if (proximo === undefined) break;
      raiz = proximo;
    }
    return raiz;
  };
  const unir = (a: string, b: string) => {
    const ra = achar(a);
    const rb = achar(b);
    if (ra !== rb) pai.set(ra, rb);
  };

  for (const proposta of doCiclo) {
    pai.set(proposta.id, proposta.id);
  }
  const porOrigem = new Map<string, string[]>();
  for (const proposta of doCiclo) {
    for (const origem of proposta.origensLegacy) {
      const lista = porOrigem.get(origem) ?? [];
      lista.push(proposta.id);
      porOrigem.set(origem, lista);
    }
  }
  for (const mesmaOrigem of porOrigem.values()) {
    for (const outro of mesmaOrigem.slice(1)) {
      unir(mesmaOrigem[0], outro);
    }
  }

  const porRaiz = new Map<string, PropostaDeclarada[]>();
  for (const proposta of doCiclo) {
    const raiz = achar(proposta.id);
    const lista = porRaiz.get(raiz) ?? [];
    lista.push(proposta);
    porRaiz.set(raiz, lista);
  }

  const ESTADOS_IMPLANTACAO_NA_CARGA = new Set(["confirmada", "confirmada_com_ressalva"]);
  return [...porRaiz.values()].map((membros) => ({
    origens: [...new Set(membros.flatMap((m) => m.origensLegacy))],
    destinos: membros.map((m) => m.id),
    pronto: membros.every(
      (m) =>
        m.estadoAuditoria === "concluida" &&
        ESTADOS_IMPLANTACAO_NA_CARGA.has(m.estadoImplantacao ?? "confirmada"),
    ),
  }));
}

/** O resumo que a capa imprime sobre uma proposta. */
export interface ResumoDoCiclo {
  componentes: number;
  origens: number;
  destinos: number;
  componentesProntos: number;
  linhasConcluidas: number;
}

/**
 * Conta o que a capa afirma sobre a proposta.
 *
 * As origens são contadas **sem repetição**: a mesma regra legada não aparece
 * em dois componentes, mas contar por componente faria a capa somar errado
 * se algum dia aparecesse, e um número inflado numa capa assinada é pior que
 * nenhum.
 */
export function resumoDoCiclo(
  componentes: ComponenteDeImplantacao[],
  propostas: PropostaDeclarada[],
): ResumoDoCiclo {
  const origens = new Set(componentes.flatMap((c) => c.origens));
  const destinos = new Set(componentes.flatMap((c) => c.destinos));
  return {
    componentes: componentes.length,
    origens: origens.size,
    destinos: destinos.size,
    componentesProntos: componentes.filter((c) => c.pronto).length,
    linhasConcluidas: propostas.filter(
      (p) => destinos.has(p.id) && p.estadoAuditoria === "concluida",
    ).length,
  };
}

/**
 * Achata o `projecao:` de uma regra proposta em células de texto.
 *
 * Cada valor sai como está escrito, convertido a texto e nada mais: o quadro
 * impresso é o cotejo entre o que a auditoria propõe e o que o Sisprev
 * receberia, e uma célula "melhorada" na impressão é uma célula que não se
 * confere contra o sistema. Chave ausente vira célula vazia — que é o que
 * `colunasPreenchidas` usa para decidir se a coluna vale a folha.
 */
export function celulasDaProjecao(
  projecao: Record<string, unknown>,
): Record<string, string> {
  return Object.fromEntries(
    Object.entries(projecao).map(([chave, valor]) => [
      chave,
      valor === null || valor === undefined ? "" : String(valor),
    ]),
  );
}

/** As linhas de um componente, na ordem em que ele declarou os destinos. */
export function linhasDoComponente(
  componente: ComponenteDeImplantacao,
  linhas: LinhaProjetada[],
): LinhaProjetada[] {
  const porProposta = new Map(linhas.map((linha) => [linha.proposta, linha]));
  return componente.destinos
    .map((destino) => porProposta.get(destino))
    .filter((linha): linha is LinhaProjetada => linha !== undefined);
}

/**
 * As colunas que valem a pena imprimir para uma unidade: as que algum destino
 * do componente preenche.
 *
 * O Sisprev tem 27 colunas e uma unidade típica preenche menos da metade;
 * imprimir todas daria um quadro em que a informação some no meio de células
 * vazias. O critério é por **componente**, não por linha, para que as
 * unidades de um mesmo componente saiam com o mesmo cabeçalho e possam ser
 * lidas em paralelo — que é como se confere decomposição de uma regra em
 * várias.
 */
export function colunasPreenchidas(
  colunas: readonly string[],
  linhas: Record<string, string>[],
): string[] {
  return colunas.filter((coluna) =>
    linhas.some((linha) => (linha[coluna] ?? "").trim() !== ""),
  );
}

/** As três partes do texto editorial do relatório, num arquivo só. */
export interface PartesDoRelatorio {
  abertura: string;
  notas: string;
  encerramento: string;
}

const DELIMITADORES = ["abertura", "notas", "encerramento"] as const;

/**
 * Reparte o corpo do `relatorio.md` nas três partes que a página consome.
 *
 * O texto editorial vive num arquivo só porque quem redige documento que
 * circula assinado não deve pular entre arquivos para mover um parágrafo de
 * seção. As fronteiras são **comentários HTML** — `<!-- abertura -->` — e não
 * títulos: um título é editorial e pode ser reescrito, e o gerador não pode
 * quebrar porque alguém renomeou uma seção.
 *
 * Estoura em delimitador ausente ou fora de ordem. O modo de falha que isso
 * evita é silencioso: sem a exceção, um `<!-- notas -->` esquecido faria as
 * notas serem lidas como parte da abertura e todas as seções do documento
 * saírem sem nota, num relatório que já foi juntado ao processo.
 */
export function partesDoRelatorio(corpo: string): PartesDoRelatorio {
  const posicoes = DELIMITADORES.map((nome) => {
    const marca = `<!-- ${nome} -->`;
    const indice = corpo.indexOf(marca);
    if (indice === -1) {
      throw new Error(`relatorio.md: falta o delimitador ${marca}`);
    }
    return { nome, indice, fim: indice + marca.length };
  });

  for (let i = 1; i < posicoes.length; i += 1) {
    if (posicoes[i].indice <= posicoes[i - 1].indice) {
      throw new Error(
        `relatorio.md: ${DELIMITADORES[i]} aparece antes de ${DELIMITADORES[i - 1]}`,
      );
    }
  }

  return {
    abertura: corpo.slice(posicoes[0].fim, posicoes[1].indice).trim(),
    notas: corpo.slice(posicoes[1].fim, posicoes[2].indice).trim(),
    encerramento: corpo.slice(posicoes[2].fim).trim(),
  };
}

/**
 * O `estado_auditoria` de uma regra proposta, dito em português corrente.
 *
 * O documento circula assinado, fora do repositório: quem se manifesta sobre
 * ele não tem como saber o que `concluida` afirma, e um rótulo opaco numa
 * coluna chamada "Estado" é lido como carimbo de aprovação. O rótulo
 * descreve só a auditoria jurídica — nunca aptidão operacional, que é
 * questão de `estado_implantacao` e não deste campo: uma regra com
 * `estado_auditoria: concluida` e `estado_implantacao:
 * confirmada_com_ressalva` está tão pronta para a carga de homologação
 * quanto o selo do componente diz, e não mais.
 *
 * Valor fora do vocabulário sai verbatim, nunca traduzido por aproximação.
 */
export function estadoLegivel(estado: string): string {
  const rotulos: Record<string, string> = {
    elaboracao: "em elaboração",
    preview: "em conferência",
    concluida: "auditoria jurídica concluída",
  };
  return rotulos[estado] ?? estado;
}

/**
 * O título de um capítulo, dito como quem recebe o documento o lê: quantas
 * regras cadastradas saem e quantas propostas entram no lugar.
 *
 * O par "origem → destino" descreve a relação para quem a construiu, não para
 * quem decide sobre ela — e a abreviação de plural entre parênteses é de tela,
 * não de documento assinado.
 */
export function tituloDoCapitulo(origens: number, destinos: number): string {
  const regras = (n: number) => (n === 1 ? "1 regra" : `${n} regras`);
  return `${regras(origens)} cadastrada${origens === 1 ? "" : "s"} substituída${
    origens === 1 ? "" : "s"
  } por ${regras(destinos)} proposta${destinos === 1 ? "" : "s"}`;
}

/**
 * O estado de um componente de implantação, dito pelo efeito que ele tem
 * sobre a carga — que é o que interessa a quem se manifesta. "Pronto" nomeia
 * o resultado do cálculo derivado (`componentesDoCiclo`), não um campo
 * decidido à parte.
 */
export function estadoDoComponenteLegivel(pronto: boolean): string {
  return pronto ? "integra a carga de homologação" : "fora da carga de homologação";
}
