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

/** Uma regra com ressalva de homologação, na forma que a matriz imprime. */
export interface RegraRessalvada {
  id: string;
  /** O índice do componente de substituição a que pertence (1-based). */
  componente: number;
  classes: ClasseDeRessalva[];
}

/**
 * As regras com ressalva de homologação do ciclo, com a classe de cada uma e
 * o componente a que pertencem — a matriz que o documento imprime para que as
 * regras ressalvadas sejam identificáveis nominalmente, e não só contadas.
 *
 * A ordem é a dos componentes e, dentro de cada um, a do próprio componente:
 * a mesma em que os capítulos e o anexo as apresentam.
 */
export function regrasRessalvadas(
  componentes: ComponenteDeImplantacao[],
  propostas: PropostaDeclarada[],
): RegraRessalvada[] {
  const porId = new Map(propostas.map((p) => [p.id, p]));
  const ressalvadas: RegraRessalvada[] = [];
  componentes.forEach((componente, indice) => {
    for (const destino of componente.destinos) {
      const proposta = porId.get(destino);
      if (!proposta) continue;
      // Pela declaração, não pela classificação: ver `levaRessalva`.
      if (!levaRessalva(proposta)) continue;
      ressalvadas.push({ id: destino, componente: indice + 1, classes: classeExigida(proposta) });
    }
  });
  return ressalvadas;
}

/**
 * As regras ressalvadas que estão efetivamente na carga de homologação.
 *
 * A população de `regrasRessalvadas` continua deliberadamente abrangendo
 * todos os componentes: ela é o gate que faz uma causa ressalvada sem classe
 * conhecida derrubar o build, mesmo quando o componente está bloqueado. Só
 * depois dessa validação a relação é recortada pelos componentes prontos.
 */
export function regrasRessalvadasNaCarga(
  componentes: ComponenteDeImplantacao[],
  propostas: PropostaDeclarada[],
): RegraRessalvada[] {
  const todas = regrasRessalvadas(componentes, propostas);
  const componentesProntos = new Set(
    componentes.filter((componente) => componente.pronto).flatMap((componente) => componente.destinos),
  );
  return todas.filter((regra) => componentesProntos.has(regra.id));
}

/** O que o capítulo de um componente afirma sobre si, em números derivados. */
export interface ResumoDoComponente {
  /** Quantas regras propostas do componente levam ressalva de homologação. */
  comRessalva: number;
  /** Quantas não levam — a população que o documento também precisa reconhecer. */
  semRessalva: number;
  /** As classes que aparecem no componente, sem repetição. */
  classes: ClasseDeRessalva[];
}

/** Conta, para um componente, as regras ressalvadas e as classes presentes. */
export function resumoDoComponente(
  componente: ComponenteDeImplantacao,
  propostas: PropostaDeclarada[],
): ResumoDoComponente {
  const porId = new Map(propostas.map((p) => [p.id, p]));
  const classes = new Set<ClasseDeRessalva>();
  let comRessalva = 0;
  for (const destino of componente.destinos) {
    const proposta = porId.get(destino);
    if (!proposta) continue;
    if (!levaRessalva(proposta)) continue;
    comRessalva += 1;
    for (const classe of classeExigida(proposta)) classes.add(classe);
  }
  return {
    comRessalva,
    semRessalva: componente.destinos.length - comRessalva,
    classes: [...classes],
  };
}

/**
 * Os selos do capítulo, ditos pelo que cada número significa.
 *
 * Duas populações diferentes conviviam sob a palavra "ressalva": as regras com
 * `estado_implantacao: confirmada_com_ressalva`, que é atributo da regra, e as
 * conferências que a auditoria deixou por marcar no corpo, que são perguntas
 * em aberto. O capítulo do componente que substitui uma única regra de causa
 * comum imprimia "0 ressalvas" — verdade sobre as conferências, falsidade
 * sobre a regra, que é ressalvada. São contados e nomeados separadamente.
 */
export function selosDoComponente(
  resumo: ResumoDoComponente,
  conferenciasAbertas: number,
): string[] {
  const regras =
    resumo.comRessalva === 0
      ? "Nenhuma regra com ressalva de homologação"
      : resumo.comRessalva === 1
        ? "1 regra com ressalva de homologação"
        : `${resumo.comRessalva} regras com ressalva de homologação`;
  const conferencias =
    conferenciasAbertas === 0
      ? "Nenhuma conferência em aberto"
      : conferenciasAbertas === 1
        ? "1 conferência em aberto"
        : `${conferenciasAbertas} conferências em aberto`;
  return [regras, conferencias];
}

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
  ressalvaHomologacao?: string;
  /** `predicados.causa_incapacidade` — de onde sai a classe da proporcionalização. */
  causaIncapacidade?: string;
  /** `predicados.vinculo_rpc` — de onde sai a classe do teto do RGPS. */
  vinculoRpc?: string;
}

/**
 * As classes de ressalva de homologação em uso.
 *
 * Não são vocabulário do schema: são o agrupamento **material** das ressalvas
 * que o Ciclo 1 registrou, e é por classe que o documento impresso as
 * apresenta, porque uma ressalva sobre a base do cálculo e outra sobre o teto
 * do Regime Geral se encerram por evidências diferentes.
 */
export type ClasseDeRessalva =
  | "proporcionalizacao"
  | "rpc_teto"
  | "reconhecimento_acidente"
  | "enquadramento_rol"
  | "reconhecimento_molestia";

export const ROTULO_DA_CLASSE: Record<ClasseDeRessalva, string> = {
  proporcionalizacao: "base da proporcionalização",
  rpc_teto: "sujeição ao regime complementar e teto do RGPS",
  reconhecimento_acidente: "reconhecimento do acidente e do nexo",
  enquadramento_rol: "enquadramento no rol temporal",
  reconhecimento_molestia: "reconhecimento do nexo profissional",
};

/**
 * As classes de ressalva que incidem sobre uma regra proposta.
 *
 * Derivadas dos **predicados estruturados**, não do texto de
 * `ressalvaHomologacao`: classificar por palavra-chave na prosa é o modo de
 * falha que este repositório já conhece — uma extração por correspondência
 * textual produziu atribuições erradas que pareciam bem formadas. O predicado
 * é o que a auditoria decidiu; a prosa é como ela o explicou.
 *
 * Lista vazia quando a regra não leva ressalva: a classe qualifica a ressalva,
 * e sem ressalva não há o que qualificar. Uma causa comum `confirmada` não
 * entra na contagem da classe da proporcionalização.
 */
export function classesDeRessalva(proposta: PropostaDeclarada): ClasseDeRessalva[] {
  if (!levaRessalva(proposta)) return [];
  const classes: ClasseDeRessalva[] = [];
  if (proposta.causaIncapacidade === "causa_comum") classes.push("proporcionalizacao");
  if (proposta.vinculoRpc === "sujeito") classes.push("rpc_teto");
  if (proposta.causaIncapacidade === "acidente_em_servico") {
    classes.push("reconhecimento_acidente");
  }
  if (proposta.causaIncapacidade === "doenca_catalogada") classes.push("enquadramento_rol");
  if (proposta.causaIncapacidade === "molestia_profissional") {
    classes.push("reconhecimento_molestia");
  }
  return classes;
}

/**
 * Se a regra leva ressalva de homologação — pelo `estado_implantacao`, que é
 * onde a auditoria a declara.
 *
 * A população não pode ser derivada das classes atribuídas. Fazendo isso, uma
 * regra `confirmada_com_ressalva` sem nenhum dos predicados reconhecidos — uma
 * terceira classe que ninguém implementou, um predicado apagado por acidente —
 * some do Anexo II e das contagens **sem que nada acuse**: a comparação entre
 * "ressalvadas" e "classificadas" fecharia sempre, porque seriam o mesmo
 * conjunto. Aqui os dois lados são independentes, e `classeExigida` estoura
 * quando divergem.
 */
export function levaRessalva(proposta: PropostaDeclarada): boolean {
  return proposta.estadoImplantacao === "confirmada_com_ressalva";
}

/**
 * As classes de uma regra ressalvada, exigindo que haja ao menos uma.
 *
 * Estoura em vez de omitir: o documento circula assinado afirmando que as
 * regras com ressalva são as do Anexo II, e uma regra que sumisse da relação
 * por falta de predicado reconhecido tornaria essa afirmação falsa sem deixar
 * rastro. Falhar o build é o comportamento barato; o caro é o anexo incompleto
 * já juntado ao processo.
 */
export function classeExigida(proposta: PropostaDeclarada): ClasseDeRessalva[] {
  const classes = classesDeRessalva(proposta);
  if (classes.length === 0) {
    throw new Error(
      `${proposta.id}: estado_implantacao é confirmada_com_ressalva, mas nenhuma classe de ` +
        "ressalva é reconhecida a partir dos predicados (causa_incapacidade, vinculo_rpc). " +
        "A regra sairia das contagens e da relação de regras ressalvadas.",
    );
  }
  return classes;
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
 * homologação levando ressalva, não bloqueia a entrada do componente) — e
 * quando `ressalvaHomologacao` está consistente com esse estado em cada
 * membro: presente só em `confirmada_com_ressalva`, a mesma checagem que
 * `_carga_de_implantacao` já aplica em `scripts/derivar.py`.
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
  const ressalvaConsistente = (m: PropostaDeclarada): boolean => {
    const estado = m.estadoImplantacao ?? "confirmada";
    const temRessalva = (m.ressalvaHomologacao ?? "").trim() !== "";
    return estado === "confirmada_com_ressalva" ? temRessalva : !temRessalva;
  };
  return [...porRaiz.values()].map((membros) => ({
    origens: [...new Set(membros.flatMap((m) => m.origensLegacy))],
    destinos: membros.map((m) => m.id),
    pronto: membros.every(
      (m) =>
        m.estadoAuditoria === "concluida" &&
        ESTADOS_IMPLANTACAO_NA_CARGA.has(m.estadoImplantacao ?? "confirmada") &&
        ressalvaConsistente(m),
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
 * Quantos destinos efetivamente na carga de homologação levam ressalva
 * (`estado_implantacao: confirmada_com_ressalva`).
 *
 * "Efetivamente na carga" é o filtro que importa: uma regra
 * `confirmada_com_ressalva` cujo componente não está `pronto` — porque outro
 * destino do mesmo grafo origem↔destino tem `estado_auditoria` ou
 * `estado_implantacao` inválidos — não entra na carga de homologação, e
 * contá-la aqui infla "quantos destinos levam ressalva" além do que
 * `destinosNaCarga` (a soma dos destinos dos componentes `pronto`) afirma
 * estar dentro. A prosa do relatório fecha a conta "destinos = na carga +
 * fora da carga" com esses marcadores; um `destinosComRessalva` que conta
 * fora da carga quebraria essa soma silenciosamente.
 */
export function destinosComRessalvaDoCiclo(
  componentes: ComponenteDeImplantacao[],
  propostas: PropostaDeclarada[],
): number {
  const destinosProntos = new Set(
    componentes.filter((c) => c.pronto).flatMap((c) => c.destinos),
  );
  return propostas.filter(
    (p) => destinosProntos.has(p.id) && p.estadoImplantacao === "confirmada_com_ressalva",
  ).length;
}

/** Uma regra proposta do capítulo, na forma que a consolidação precisa. */
export interface DestinoComPontos {
  id: string;
  pontos: string[];
}

/**
 * Uma conferência em aberto do capítulo, com a relação das regras propostas
 * que ela alcança.
 */
export interface PontoConsolidado {
  /** O HTML interno do `<li>`, como a regra proposta o escreveu. */
  html: string;
  /** Os ids das regras propostas que registram esta mesma conferência. */
  regras: string[];
}

/**
 * Agrupa as conferências em aberto de um capítulo por **enunciado**, em vez de
 * concatenar as de cada regra proposta.
 *
 * Uma dependência sistêmica é escrita em todas as regras que ela alcança —
 * é assim que cada unidade fica conferível isoladamente. Concatenando, porém,
 * o capítulo derivado de `regra-0022` imprimia dezenove vezes o mesmo
 * `C1-R34`, cada ocorrência com o seu próprio campo "Providência do
 * Instituto": uma pendência única aparecia como dezenove independentes, e
 * quem recebe o documento teria de responder dezenove vezes a mesma coisa —
 * ou notar sozinho que são a mesma.
 *
 * A ordem é a da primeira aparição, para que a numeração impressa siga a
 * ordem em que os destinos entram no capítulo. A chave é o HTML exato: duas
 * redações diferentes do mesmo assunto continuam sendo dois pontos, porque
 * decidir que dizem a mesma coisa é mérito, e o gerador não o julga.
 */
export function consolidarPontos(destinos: DestinoComPontos[]): PontoConsolidado[] {
  const porEnunciado = new Map<string, PontoConsolidado>();
  for (const destino of destinos) {
    for (const html of destino.pontos) {
      const existente = porEnunciado.get(html);
      if (existente) {
        if (!existente.regras.includes(destino.id)) existente.regras.push(destino.id);
      } else {
        porEnunciado.set(html, { html, regras: [destino.id] });
      }
    }
  }
  return [...porEnunciado.values()];
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

/**
 * As partes do texto editorial do relatório, num arquivo só.
 *
 * `encaminhamento` abre o documento e responde ao destinatário o que se espera
 * dele; `abertura` traz objeto, escopo e as conclusões jurídicas;
 * `responsabilidades` distribui o que cabe a cada unidade; `notas` são as
 * notas de seção; `encerramento` fecha com a sequência de providências.
 */
export interface PartesDoRelatorio {
  encaminhamento: string;
  abertura: string;
  responsabilidades: string;
  notas: string;
  encerramento: string;
}

const DELIMITADORES = [
  "encaminhamento",
  "abertura",
  "responsabilidades",
  "notas",
  "encerramento",
] as const;

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

  // Cada parte vai do fim do seu delimitador ao início do próximo; a última,
  // até o fim do arquivo. Escrito assim para que acrescentar uma seção seja
  // acrescentar um nome em `DELIMITADORES`, e não mais um `slice` a manter.
  const recorte = (i: number) =>
    corpo.slice(posicoes[i].fim, i + 1 < posicoes.length ? posicoes[i + 1].indice : undefined).trim();

  return Object.fromEntries(
    DELIMITADORES.map((nome, i) => [nome, recorte(i)]),
  ) as unknown as PartesDoRelatorio;
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
