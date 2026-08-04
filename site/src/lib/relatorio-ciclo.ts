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

/** Uma linha projetada, na forma mínima que este módulo precisa conhecer. */
export interface LinhaProjetada {
  proposta: string;
  grupo: string;
  deployable: boolean;
  /** Os valores projetados, indexados pela chave de frontmatter da coluna. */
  colunas: Record<string, string>;
}

/** Um grupo de substituição, na forma mínima que este módulo precisa conhecer. */
export interface GrupoDeclarado {
  grupo: string;
  origens: string[];
  destinos: string[];
  estado_grupo: string;
}

/** Um grupo como o conjunto o declara: por ref de caminho, não por id. */
export interface SubstituicaoDeclarada {
  grupo: string;
  origens_legacy: string[];
  destinos_propostos: string[];
  estado_grupo: string;
}

/** Um conjunto, na forma mínima que a cadeia de bases precisa conhecer. */
export interface ConjuntoDeclarado {
  id: string;
  base?: string;
  substituicoes?: SubstituicaoDeclarada[];
}

/**
 * O id de um documento a partir da ref de caminho com que o conjunto o
 * endereça — `/regras/regra-0019.md` é `regra-0019`.
 *
 * O documento impresso nunca mostra a ref: ela é endereço dentro do
 * repositório, e quem recebe o relatório não tem o repositório. O que ele
 * mostra é o id, que é como a regra é chamada no cadastro e na conversa.
 */
export function idDaRef(ref: string): string {
  return ref.slice(ref.lastIndexOf("/") + 1).replace(/\.md$/, "");
}

/**
 * Colhe os grupos de substituição do conjunto e de toda a sua cadeia de bases,
 * da base mais antiga para a mais recente — a ordem em que a auditoria os
 * decidiu, e a ordem dos capítulos.
 *
 * Um conjunto de fechamento tipicamente não declara delta próprio: ele
 * consolida o que as sessões anteriores decidiram. Ler só os grupos dele
 * devolveria zero e sairia um documento que diz "este ciclo não substituiu
 * nada" sobre um ciclo que substituiu quarenta regras.
 *
 * **Só grupos ativos entram.** O documento pergunta a quem o recebe se pode
 * substituir estas regras por aquelas, e um grupo inativo não está sendo
 * submetido: ele está autorado e conferido, mas a auditoria não o promoveu.
 * Imprimi-lo apresentaria a quem decide uma proposta maior que a submetida —
 * e faria a abertura afirmar que nenhuma das regras de origem permanece na
 * composição, quando as origens dos grupos inativos permanecem.
 *
 * A cadeia é percorrida com registro do já visitado: um `base` que aponte de
 * volta para um ancestral é erro de autoria, e sem essa guarda ele viraria
 * laço infinito na hora do build, não mensagem.
 */
export function gruposDaCadeia(
  id: string,
  porId: Map<string, ConjuntoDeclarado>,
): GrupoDeclarado[] {
  const cadeia: ConjuntoDeclarado[] = [];
  const vistos = new Set<string>();
  let atual = porId.get(id);
  while (atual) {
    if (vistos.has(atual.id)) {
      throw new Error(
        `conjunto ${atual.id} aparece duas vezes na própria cadeia de bases`,
      );
    }
    vistos.add(atual.id);
    cadeia.unshift(atual);
    atual = atual.base ? porId.get(atual.base) : undefined;
  }

  const porGrupo = new Map<string, GrupoDeclarado>();
  for (const conjunto of cadeia) {
    for (const substituicao of conjunto.substituicoes ?? []) {
      // Redeclaração vale a mais recente, mas mantém o lugar da primeira: uma
      // sessão posterior que revise um grupo revisa o capítulo, não o move.
      porGrupo.set(substituicao.grupo, {
        grupo: substituicao.grupo,
        origens: substituicao.origens_legacy.map(idDaRef),
        destinos: substituicao.destinos_propostos.map(idDaRef),
        estado_grupo: substituicao.estado_grupo,
      });
    }
  }
  return [...porGrupo.values()].filter(
    (grupo) => grupo.estado_grupo === "ativo",
  );
}

/** O resumo que a capa imprime sobre uma proposta. */
export interface ResumoDoCiclo {
  grupos: number;
  origens: number;
  destinos: number;
  gruposAtivos: number;
  linhasDeployable: number;
}

/**
 * Conta o que a capa afirma sobre a proposta.
 *
 * As origens são contadas **sem repetição**: a mesma regra legada não aparece
 * em dois grupos, mas contar por grupo faria a capa somar errado se algum dia
 * aparecesse, e um número inflado numa capa assinada é pior que nenhum.
 */
export function resumoDoCiclo(
  grupos: GrupoDeclarado[],
  linhas: LinhaProjetada[],
): ResumoDoCiclo {
  const origens = new Set(grupos.flatMap((grupo) => grupo.origens));
  const destinos = new Set(grupos.flatMap((grupo) => grupo.destinos));
  return {
    grupos: grupos.length,
    origens: origens.size,
    destinos: destinos.size,
    gruposAtivos: grupos.filter((grupo) => grupo.estado_grupo === "ativo")
      .length,
    linhasDeployable: linhas.filter((linha) => linha.deployable).length,
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

/** As linhas de um grupo, na ordem em que o grupo declarou os destinos. */
export function linhasDoGrupo(
  grupo: GrupoDeclarado,
  linhas: LinhaProjetada[],
): LinhaProjetada[] {
  const porProposta = new Map(linhas.map((linha) => [linha.proposta, linha]));
  return grupo.destinos
    .map((destino) => porProposta.get(destino))
    .filter((linha): linha is LinhaProjetada => linha !== undefined);
}

/**
 * As colunas que valem a pena imprimir para uma unidade: as que algum destino
 * do grupo preenche.
 *
 * O Sisprev tem 27 colunas e uma unidade típica preenche menos da metade;
 * imprimir todas daria um quadro em que a informação some no meio de células
 * vazias. O critério é por **grupo**, não por linha, para que as unidades de
 * um mesmo grupo saiam com o mesmo cabeçalho e possam ser lidas em paralelo —
 * que é como se confere decomposição de uma regra em várias.
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
 * O estado de uma regra proposta, dito em português corrente.
 *
 * O documento circula assinado, fora do repositório: quem se manifesta sobre
 * ele não tem como saber o que `deployable` afirma, e um rótulo opaco numa
 * coluna chamada "Estado" é lido como carimbo de aprovação. O valor gravado
 * continua impresso ao lado, para que a leitura não esconda o dado — mesma
 * regra que a ficha do site segue.
 *
 * Valor fora do vocabulário sai verbatim, nunca traduzido por aproximação.
 */
export function estadoLegivel(estado: string): string {
  const rotulos: Record<string, string> = {
    elaboracao: "em elaboração",
    preview: "em conferência",
    deployable: "pronta para o sistema",
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
 * O estado de um grupo de substituição, dito pelo efeito que ele tem sobre a
 * proposta — que é o que interessa a quem se manifesta. "Ativo" e "inativo"
 * nomeiam o estado interno do grupo e não dizem, a quem lê de fora, se aquelas
 * regras entram ou não na composição proposta.
 */
export function estadoDoGrupoLegivel(estado: string): string {
  const rotulos: Record<string, string> = {
    ativo: "integra a proposta",
    inativo: "fora da proposta",
  };
  return rotulos[estado] ?? estado;
}
