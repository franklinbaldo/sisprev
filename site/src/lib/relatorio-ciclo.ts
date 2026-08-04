// Núcleo puro do relatório de fechamento de ciclo — o que a página precisa
// *calcular* sobre uma proposta, sem tocar em `astro:content` nem em
// `site-data.ts`.
//
// Mesma divisão que `relatorio.ts` já segue, e pelo mesmo motivo operacional:
// o job `test` do CI roda vitest **sem** o emissor, então um módulo testado
// que alcançasse `dados-do-site.json` quebraria o CI mesmo passando
// localmente. Quem liga isto ao JSON e às coleções é a página `.astro`.

/** Uma linha projetada, na forma mínima que este módulo precisa conhecer. */
export interface LinhaProjetada {
  proposta: string;
  grupo: string;
  deployable: boolean;
  pendencias: string[];
}

/** Um grupo de substituição, na forma mínima que este módulo precisa conhecer. */
export interface GrupoDeclarado {
  grupo: string;
  origens: string[];
  destinos: string[];
  estado_grupo: string;
}

/** O resumo que a capa imprime sobre uma proposta. */
export interface ResumoDoCiclo {
  grupos: number;
  origens: number;
  destinos: number;
  gruposAtivos: number;
  linhasDeployable: number;
  linhasComPendencia: number;
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
    linhasComPendencia: linhas.filter((linha) => linha.pendencias.length > 0)
      .length,
  };
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
