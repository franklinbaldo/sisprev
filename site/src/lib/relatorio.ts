// Núcleo puro do relatório de validação da PGE — as duas coisas que a página
// precisa *calcular* sobre o catálogo, sem tocar em `astro:content` nem em
// `site-data.ts`.
//
// Mesma divisão que `painel.ts`/`filtros.ts` já seguem, e pelo mesmo motivo
// operacional: o job `test` do CI roda vitest **sem** o emissor, então um
// módulo testado que alcançasse `dados-do-site.json` quebraria o CI mesmo
// passando localmente. Quem liga isto às coleções é a página `.astro`.
//
// Duas notas sobre o que este módulo deliberadamente não faz:
//
// - **não conclui nada sobre a regra.** As pendências que ele extrai são os
//   itens de checklist que o auditor deixou por marcar, transcritos como
//   estão. Contar `- [ ]` é forma, nunca mérito — é exatamente o mesmo
//   critério que o P7 usa para admitir uma regra em `revisada`, e nem lá nem
//   aqui o código julga se os itens são os certos;
// - **não lê `validado_pge`.** Esse campo é *consequência* do relatório, não
//   insumo dele: a regra chega `revisada`, o relatório é o instrumento pelo
//   qual a PGE se manifesta, e só o ato registrado em `atos_validacao` depois
//   de assinado é que o vira `TRUE`. Filtrar por ele aqui inverteria o laço.

/** Um item de checklist ainda não marcado no corpo autorado de uma regra. */
const PENDENCIA_RE = /^[ \t]*[-*][ \t]+\[ \][ \t]+(.*)$/;

/**
 * Os itens de checklist não marcados do corpo de uma regra, na ordem em que
 * aparecem e com o texto exatamente como foi escrito (ainda em Markdown — a
 * página os renderiza com o mesmo pipeline do resto do corpo).
 *
 * Um item marcado (`- [x]`) não entra: ele é conferência concluída, não
 * pergunta aberta. O que entra vai numerado para a seção de manifestação,
 * porque é o que a PGE tem de responder.
 */
export function pendenciasDoCorpo(corpo: string): string[] {
  return corpo
    .split("\n")
    .map((linha) => PENDENCIA_RE.exec(linha))
    .filter((match): match is RegExpExecArray => match !== null)
    .map((match) => match[1].trim())
    .filter((texto) => texto.length > 0);
}

/**
 * As notas de seção autoradas em `docs/relatorio/notas.md`, indexadas pela
 * chave do seu `## título`.
 *
 * O texto editorial do relatório é fonte autorada, não código: quem redige um
 * documento que circula assinado precisa poder reescrever uma frase sem tocar
 * num `.astro`. O que fica no código é só onde cada nota entra.
 *
 * O primeiro bloco do arquivo (antes do primeiro `##`) é o preâmbulo que
 * explica o próprio arquivo, e não entra no índice.
 */
export function notasDeSecao(markdown: string): Map<string, string> {
  const notas = new Map<string, string>();
  const blocos = markdown.split(/^## +/m).slice(1);
  for (const bloco of blocos) {
    const quebra = bloco.indexOf("\n");
    if (quebra === -1) continue;
    const chave = bloco.slice(0, quebra).trim();
    const texto = bloco.slice(quebra).trim();
    if (chave && texto) notas.set(chave, texto);
  }
  return notas;
}

/**
 * Lê uma nota pela chave, ou **estoura**.
 *
 * Falhar o build é deliberado: uma seção sem nota sairia sem aviso nenhum, e o
 * defeito só apareceria depois de o anexo estar juntado ao processo. Um
 * documento assinado não é lugar de degradação silenciosa.
 */
export function nota(notas: Map<string, string>, chave: string): string {
  const texto = notas.get(chave);
  if (texto === undefined) {
    throw new Error(
      `docs/relatorio/notas.md não tem a seção "## ${chave}", exigida pelo relatório`,
    );
  }
  return texto;
}

const ESCAPES: Record<string, string> = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
};

/**
 * Substitui os marcadores `{{chave}}` do texto autorado pelos totais do
 * catálogo, e **estoura** num marcador que não conheça.
 *
 * Existe para que a prosa da abertura possa dizer "as 112 regras submetidas"
 * sem que esse número vire literal no `.md` — ele muda a cada remessa — nem
 * migre para o código, o que devolveria o texto ao lugar de onde ele saiu. Um
 * marcador desconhecido é erro de build, nunca um `{{regras}}` impresso cru no
 * meio de um documento assinado.
 */
export function aplicarTotais(
  texto: string,
  totais: Record<string, number>,
): string {
  return texto.replace(/\{\{(\w+)\}\}/g, (_, chave: string) => {
    const valor = totais[chave];
    if (valor === undefined) {
      throw new Error(
        `marcador {{${chave}}} não corresponde a nenhum total do relatório`,
      );
    }
    return String(valor);
  });
}

/** Escapa um trecho literal antes de ele entrar no HTML da página. */
export function escaparHtml(texto: string): string {
  return texto.replace(/[&<>"]/g, (caractere) => ESCAPES[caractere]);
}

/**
 * Converte a marcação **inline** de um item de checklist em HTML.
 *
 * Existe por um motivo estreito: as pendências são reimpressas, numeradas, na
 * seção de manifestação, fora do corpo que o pipeline de Markdown do Astro
 * renderiza. Cobre exatamente as quatro construções que ocorrem nesses itens
 * — código, ênfase forte, ênfase e link — levantadas contando os corpos de
 * `okf/`, não estimadas. Qualquer outra coisa sai literal, escapada: perder
 * um trecho de uma pendência em silêncio seria pior que exibi-lo cru.
 *
 * O link vira só o seu texto. O destino desses links é sempre um arquivo do
 * repositório (`../../docs/analysis/...`), que não existe dentro do PDF; um
 * link morto num anexo de processo é pior que nenhum link, e a referência
 * continua legível no capítulo, que transcreve o corpo inteiro.
 */
export function inlineParaHtml(markdown: string): string {
  return escaparHtml(markdown)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\[([^\]]+)\]\([^)\s]*\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, "$1<em>$2</em>");
}

/** O recorte de um capítulo que o quadro-resumo precisa contar. */
export interface CapituloContavel {
  tipoDeBeneficio: string;
  dispositivos: number;
  pendencias: number;
  achadosAbertos: number;
  achados: number;
}

/** Os totais do quadro de abertura — cada um conferível somando os capítulos. */
export interface ResumoDoRelatorio {
  regras: number;
  regrasComDispositivos: number;
  regrasSemDispositivos: number;
  dispositivosCitados: number;
  regrasComPendencia: number;
  pendencias: number;
  regrasComAchado: number;
  achadosAbertosCitados: number;
  porTipoDeBeneficio: { tipo: string; regras: number }[];
}

/** Rótulo usado quando a coluna `TIPO DE BENEFICIO` está vazia — nunca um default inventado. */
export const SEM_TIPO = "(sem tipo declarado)";

/**
 * Conta o catálogo para o quadro de abertura.
 *
 * `dispositivosCitados` soma as citações, não os dispositivos distintos: o
 * mesmo artigo citado por trinta regras conta trinta vezes, porque é isso
 * que o volume do relatório reflete e é isso que o leitor confere folheando.
 */
export function resumoDoRelatorio(
  capitulos: CapituloContavel[],
): ResumoDoRelatorio {
  const porTipo = new Map<string, number>();
  for (const capitulo of capitulos) {
    const tipo = capitulo.tipoDeBeneficio.trim() || SEM_TIPO;
    porTipo.set(tipo, (porTipo.get(tipo) ?? 0) + 1);
  }

  return {
    regras: capitulos.length,
    regrasComDispositivos: capitulos.filter((c) => c.dispositivos > 0).length,
    regrasSemDispositivos: capitulos.filter((c) => c.dispositivos === 0).length,
    dispositivosCitados: capitulos.reduce(
      (total, c) => total + c.dispositivos,
      0,
    ),
    regrasComPendencia: capitulos.filter((c) => c.pendencias > 0).length,
    pendencias: capitulos.reduce((total, c) => total + c.pendencias, 0),
    regrasComAchado: capitulos.filter((c) => c.achados > 0).length,
    achadosAbertosCitados: capitulos.reduce(
      (total, c) => total + c.achadosAbertos,
      0,
    ),
    porTipoDeBeneficio: [...porTipo.entries()]
      .map(([tipo, regras]) => ({ tipo, regras }))
      .sort(
        (a, b) => b.regras - a.regras || a.tipo.localeCompare(b.tipo, "pt-BR"),
      ),
  };
}

/**
 * A janela de vigência de um dispositivo, em uma linha.
 *
 * Mora aqui porque dois documentos a imprimem — o relatório de validação e o
 * de fechamento de ciclo — e duas cópias da mesma frase divergiriam na
 * primeira vez que uma delas fosse ajustada. "Vigência não declarada" é dito,
 * nunca omitido: um dispositivo sem data é fato a mostrar, não a esconder.
 *
 * A data sai em dd/mm/aaaa, como em qualquer peça: estes documentos circulam
 * assinados, e a ordem ano-mês-dia é convenção de máquina. `UTC` porque a data
 * de vigência é uma data civil, e ler o fuso do servidor de geração faria a
 * mesma norma começar num dia aqui e noutro ali.
 */
export function janelaDeVigencia(inicio?: Date, fim?: Date): string {
  const br = (data: Date) =>
    [data.getUTCDate(), data.getUTCMonth() + 1]
      .map((n) => String(n).padStart(2, "0"))
      .join("/") + `/${data.getUTCFullYear()}`;
  if (!inicio && !fim) return "vigência não declarada";
  if (!fim) return `a partir de ${br(inicio!)}`;
  if (!inicio) return `até ${br(fim)}`;
  return `de ${br(inicio)} a ${br(fim)}`;
}

/**
 * Uma data ISO dita como data civil, dd/mm/aaaa — a mesma razão da janela de
 * vigência: o documento circula assinado, e ano-mês-dia é ordem de máquina.
 *
 * O que não casar com o formato sai verbatim: valor inesperado é fato a
 * mostrar, nunca a coagir a um default.
 */
export function dataCivil(iso: string): string {
  const partes = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso);
  return partes ? `${partes[3]}/${partes[2]}/${partes[1]}` : iso;
}

/** Uma regra, no recorte que o quadro de alcance conta. */
export interface RegraNoAlcance {
  /** `status_auditoria` como está gravado; ausente conta como não concluída. */
  statusAuditoria: string;
  /** Quantas disposições de achado a regra registra. */
  disposicoes: number;
  /** Quantos itens de checklist a auditoria deixou por marcar no corpo. */
  ressalvas: number;
}

/** Um achado, no recorte que o quadro de alcance conta. */
export interface AchadoNoAlcance {
  situacao: string;
  severidade: string;
}

/**
 * O alcance real da remessa — quantas regras o documento efetivamente conclui.
 *
 * Existe porque a abertura afirmava submeter o catálogo inteiro à manifestação
 * enquanto a conferência de mérito tinha concluído sobre um punhado de regras.
 * Um documento assinado que apresenta 112 capítulos sem dizer sobre quantos
 * conclui é lido como aprovação de 112, e o silêncio faz o trabalho da
 * afirmação.
 *
 * **`revisadas` é o único número que afirma conferência concluída.** Uma regra
 * com disposição registrada teve *algum* achado disposto; não é o mesmo que ter
 * a análise fechada, e juntar as duas contagens diria mais do que o catálogo
 * diz.
 */
export interface AlcanceDaRemessa {
  regras: number;
  revisadas: number;
  comDisposicao: number;
  comRessalva: number;
  tesesAbertas: number;
  tesesBloqueantes: number;
}

export function alcanceDaRemessa(
  regras: readonly RegraNoAlcance[],
  achados: readonly AchadoNoAlcance[],
): AlcanceDaRemessa {
  const abertos = achados.filter((a) => a.situacao === "aberto");
  return {
    regras: regras.length,
    revisadas: regras.filter((r) => r.statusAuditoria === "revisada").length,
    comDisposicao: regras.filter((r) => r.disposicoes > 0).length,
    comRessalva: regras.filter((r) => r.ressalvas > 0).length,
    tesesAbertas: abertos.length,
    tesesBloqueantes: abertos.filter((a) => a.severidade === "bloqueante").length,
  };
}

/** Uma tese: o achado, as regras que ele alcança e o que se decidiu em cada uma. */
export interface Tese<A, D> {
  achado: A;
  /** Ids das regras alcançadas, na ordem em que o catálogo as apresenta. */
  regras: string[];
  /** As disposições já decididas, por regra. */
  disposicoes: { regra: string; disposicao: D }[];
}

/**
 * Agrupa o catálogo por tese — o achado como unidade, e não a regra.
 *
 * A troca é de conteúdo, não de forma: um mesmo defeito alcança dezenas de
 * linhas do cadastro, e concluí-lo uma vez por linha imprimia a mesma
 * conclusão dezenas de vezes, sem que o documento dissesse em lugar nenhum
 * quantas regras aquele defeito alcança de fato.
 *
 * A ordem é a do próprio achado (severidade antes de id), e as regras de cada
 * tese saem na ordem em que `regrasNaOrdem` as entrega — a do catálogo, para
 * que o leitor confira as duas listas em paralelo.
 */
export function tesesDoCatalogo<A extends { id: string; regras_afetadas: string[] }, D>(
  achados: readonly A[],
  regrasNaOrdem: readonly string[],
  disposicoesPorRegra: ReadonlyMap<string, { achado: string; disposicao: D }[]>,
): Tese<A, D>[] {
  return achados.map((achado) => {
    const alcancadas = new Set(achado.regras_afetadas);
    const regras = regrasNaOrdem.filter((id) => alcancadas.has(id));
    const disposicoes = regras.flatMap((regra) =>
      (disposicoesPorRegra.get(regra) ?? [])
        .filter((d) => d.achado === achado.id)
        .map((d) => ({ regra, disposicao: d.disposicao })),
    );
    return { achado, regras, disposicoes };
  });
}
