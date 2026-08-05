import { describe, expect, it } from "vitest";
import {
  SEM_TIPO,
  aplicarTotais,
  dataCivil,
  escaparHtml,
  inlineParaHtml,
  itensNaoMarcadosDoHtml,
  janelaDeVigencia,
  nota,
  notasDeSecao,
  resumoDoRelatorio,
  type CapituloContavel,
} from "./relatorio";

describe("notasDeSecao", () => {
  const arquivo = [
    "# Notas de seção",
    "",
    "Preâmbulo que explica o arquivo e não é nota de nada.",
    "",
    "## parametros",
    "",
    "Os campos como gravados.",
    "",
    "## analise",
    "",
    "Texto do auditor,",
    "em duas linhas.",
  ].join("\n");

  it("indexa cada bloco pela chave do seu título, ignorando o preâmbulo", () => {
    const notas = notasDeSecao(arquivo);
    expect([...notas.keys()]).toEqual(["parametros", "analise"]);
    expect(notas.get("parametros")).toBe("Os campos como gravados.");
    expect(notas.get("analise")).toBe("Texto do auditor,\nem duas linhas.");
  });

  it("ignora um título sem corpo em vez de indexar nota vazia", () => {
    expect(notasDeSecao("## vazia\n\n## cheia\n\ntexto").has("vazia")).toBe(
      false,
    );
  });

  it("nota() estoura na chave ausente, para o defeito não sair impresso", () => {
    const notas = notasDeSecao(arquivo);
    expect(nota(notas, "parametros")).toBe("Os campos como gravados.");
    expect(() => nota(notas, "inexistente")).toThrowError(/## inexistente/);
  });
});

describe("aplicarTotais", () => {
  it("substitui cada marcador pelo total correspondente", () => {
    expect(
      aplicarTotais("as {{regras}} regras, {{pendencias}} pontos", {
        regras: 112,
        pendencias: 13,
      }),
    ).toBe("as 112 regras, 13 pontos");
  });

  it("substitui todas as ocorrências do mesmo marcador", () => {
    expect(aplicarTotais("{{regras}} de {{regras}}", { regras: 7 })).toBe(
      "7 de 7",
    );
  });

  it("aceita o total zero em vez de tratá-lo como ausente", () => {
    expect(aplicarTotais("{{pendencias}} pontos", { pendencias: 0 })).toBe(
      "0 pontos",
    );
  });

  it("estoura no marcador desconhecido, em vez de imprimi-lo cru", () => {
    expect(() => aplicarTotais("{{inventado}}", { regras: 1 })).toThrowError(
      /\{\{inventado\}\}/,
    );
  });

  it("deixa intacto o texto sem marcador", () => {
    expect(aplicarTotais("prosa comum", {})).toBe("prosa comum");
  });
});

describe("inlineParaHtml", () => {
  it("converte código, ênfase forte e ênfase", () => {
    expect(inlineParaHtml("o `campo` é **obrigatório** e *aberto*")).toBe(
      "o <code>campo</code> é <strong>obrigatório</strong> e <em>aberto</em>",
    );
  });

  it("reduz o link ao seu texto — o destino não existe dentro do PDF", () => {
    expect(
      inlineParaHtml("ver a [conferência](../../docs/analysis/x.md) completa"),
    ).toBe("ver a conferência completa");
  });

  it("escapa o que viria do texto autorado antes de virar HTML", () => {
    expect(inlineParaHtml('art. 40 <b>&"</b>')).toBe(
      "art. 40 &lt;b&gt;&amp;&quot;&lt;/b&gt;",
    );
  });

  it("não confunde a barra de uma data com marcação", () => {
    expect(inlineParaHtml("`data_direito_ate: 31/12/2099`")).toBe(
      "<code>data_direito_ate: 31/12/2099</code>",
    );
  });

  it("deixa literal o que está fora do subconjunto coberto", () => {
    expect(inlineParaHtml("nota[^1] e ~~risco~~")).toBe("nota[^1] e ~~risco~~");
  });
});

describe("escaparHtml", () => {
  it("neutraliza os quatro caracteres que quebrariam a marcação", () => {
    expect(escaparHtml('<a href="x">&</a>')).toBe(
      "&lt;a href=&quot;x&quot;&gt;&amp;&lt;/a&gt;",
    );
  });
});

describe("itensNaoMarcadosDoHtml", () => {
  // As fixtures abaixo são o HTML que `createSatteriMarkdownProcessor` de
  // fato emite para `- [ ]`/`- [x]` (GFM task list) — conferido rodando o
  // processador contra corpos reais do bundle. A função não reprocessa
  // Markdown: só recorta o `<li>` de cada item não marcado.

  it("preserva o item multilinha completo, como o renderer o entrega", () => {
    const html =
      '<ul class="contains-task-list">\n' +
      '<li class="task-list-item"><input type="checkbox" disabled> protocolo institucional de reconhecimento do nexo de\n' +
      "moléstia profissional ainda não definido pelo IPERON (lacuna normativa,\n" +
      "RFC 0004 §7/§14) — dependência externa.</li>\n" +
      "</ul>";
    expect(itensNaoMarcadosDoHtml(html)).toEqual([
      "protocolo institucional de reconhecimento do nexo de\n" +
        "moléstia profissional ainda não definido pelo IPERON (lacuna normativa,\n" +
        "RFC 0004 §7/§14) — dependência externa.",
    ]);
  });

  it("preserva a formatação inline do renderer, sem reconvertê-la para Markdown", () => {
    const html =
      '<ul class="contains-task-list">\n' +
      '<li class="task-list-item"><input type="checkbox" disabled> <code>data_direito_ate</code> discorda do prazo do ' +
      '<a href="/dispositivos/x">art. 4º</a>, <strong>confirmado</strong>.</li>\n' +
      "</ul>";
    expect(itensNaoMarcadosDoHtml(html)).toEqual([
      '<code>data_direito_ate</code> discorda do prazo do <a href="/dispositivos/x">art. 4º</a>, <strong>confirmado</strong>.',
    ]);
  });

  it("exclui o item marcado", () => {
    const html =
      '<ul class="contains-task-list">\n' +
      '<li class="task-list-item"><input type="checkbox" checked disabled> conferido item a item</li>\n' +
      '<li class="task-list-item"><input type="checkbox" disabled> pendência aberta</li>\n' +
      "</ul>";
    expect(itensNaoMarcadosDoHtml(html)).toEqual(["pendência aberta"]);
  });
});

function capitulo(parcial: Partial<CapituloContavel> = {}): CapituloContavel {
  return {
    tipoDeBeneficio: "APOSENTADORIA POR INVALIDEZ",
    dispositivos: 0,
    pendencias: 0,
    achadosAbertos: 0,
    achados: 0,
    ...parcial,
  };
}

describe("resumoDoRelatorio", () => {
  it("conta regras, citações e pendências separando 'quantas regras' de 'quantos itens'", () => {
    const resumo = resumoDoRelatorio([
      capitulo({
        dispositivos: 7,
        pendencias: 3,
        achados: 1,
        achadosAbertos: 1,
      }),
      capitulo({ dispositivos: 2, pendencias: 1 }),
      capitulo(),
    ]);

    expect(resumo.regras).toBe(3);
    expect(resumo.regrasComDispositivos).toBe(2);
    expect(resumo.regrasSemDispositivos).toBe(1);
    // Soma de citações, não de dispositivos distintos: o capítulo é
    // autocontido e reimprime o texto de cada citação.
    expect(resumo.dispositivosCitados).toBe(9);
    expect(resumo.regrasComPendencia).toBe(2);
    expect(resumo.pendencias).toBe(4);
    expect(resumo.regrasComAchado).toBe(1);
    expect(resumo.achadosAbertosCitados).toBe(1);
  });

  it("um achado improcedente conta como achado do capítulo, mas não como aberto", () => {
    const resumo = resumoDoRelatorio([
      capitulo({ achados: 2, achadosAbertos: 0 }),
    ]);
    expect(resumo.regrasComAchado).toBe(1);
    expect(resumo.achadosAbertosCitados).toBe(0);
  });

  it("agrupa por tipo de benefício, do mais frequente ao menos", () => {
    const resumo = resumoDoRelatorio([
      capitulo({ tipoDeBeneficio: "PENSAO POR MORTE" }),
      capitulo({ tipoDeBeneficio: "APOSENTADORIA VOLUNTARIA" }),
      capitulo({ tipoDeBeneficio: "PENSAO POR MORTE" }),
    ]);

    expect(resumo.porTipoDeBeneficio).toEqual([
      { tipo: "PENSAO POR MORTE", regras: 2 },
      { tipo: "APOSENTADORIA VOLUNTARIA", regras: 1 },
    ]);
  });

  it("rotula o tipo vazio em vez de inventar um default", () => {
    const resumo = resumoDoRelatorio([capitulo({ tipoDeBeneficio: "   " })]);
    expect(resumo.porTipoDeBeneficio).toEqual([{ tipo: SEM_TIPO, regras: 1 }]);
  });

  it("devolve zeros para um catálogo vazio, nunca NaN", () => {
    const resumo = resumoDoRelatorio([]);
    expect(resumo.regras).toBe(0);
    expect(resumo.dispositivosCitados).toBe(0);
    expect(resumo.porTipoDeBeneficio).toEqual([]);
  });
});

describe("janelaDeVigencia", () => {
  const data = (iso: string) => new Date(`${iso}T00:00:00Z`);

  it("diz as duas pontas quando as duas existem", () => {
    expect(janelaDeVigencia(data("1998-12-16"), data("2003-12-30"))).toBe(
      "de 16/12/1998 a 30/12/2003",
    );
  });

  it("diz o aberto de cada lado", () => {
    expect(janelaDeVigencia(data("2019-11-13"), undefined)).toBe(
      "a partir de 13/11/2019",
    );
    expect(janelaDeVigencia(undefined, data("2003-12-30"))).toBe(
      "até 30/12/2003",
    );
  });

  it("declara a ausência em vez de imprimir vazio", () => {
    expect(janelaDeVigencia(undefined, undefined)).toBe(
      "vigência não declarada",
    );
  });
});

describe("dataCivil", () => {
  it("diz a data como se diz numa peça", () => {
    expect(dataCivil("2026-08-04")).toBe("04/08/2026");
  });

  it("devolve verbatim o que não é data ISO, em vez de coagir a um default", () => {
    expect(dataCivil("sem data")).toBe("sem data");
    expect(dataCivil("")).toBe("");
  });
});
