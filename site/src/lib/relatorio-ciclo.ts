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
  unidade: string;
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
export function resumoDoCiclo(grupos: GrupoDeclarado[], linhas: LinhaProjetada[]): ResumoDoCiclo {
  const origens = new Set(grupos.flatMap((grupo) => grupo.origens));
  const destinos = new Set(grupos.flatMap((grupo) => grupo.destinos));
  return {
    grupos: grupos.length,
    origens: origens.size,
    destinos: destinos.size,
    gruposAtivos: grupos.filter((grupo) => grupo.estado_grupo === "ativo").length,
    linhasDeployable: linhas.filter((linha) => linha.deployable).length,
    linhasComPendencia: linhas.filter((linha) => linha.pendencias.length > 0).length,
  };
}

/** As linhas de um grupo, na ordem em que o grupo declarou os destinos. */
export function linhasDoGrupo(grupo: GrupoDeclarado, linhas: LinhaProjetada[]): LinhaProjetada[] {
  const porUnidade = new Map(linhas.map((linha) => [linha.unidade, linha]));
  return grupo.destinos
    .map((destino) => porUnidade.get(destino))
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
export function colunasPreenchidas(colunas: readonly string[], linhas: Record<string, string>[]): string[] {
  return colunas.filter((coluna) => linhas.some((linha) => (linha[coluna] ?? "").trim() !== ""));
}
