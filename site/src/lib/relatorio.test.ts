import { describe, expect, it } from "vitest";
import {
  SEM_TIPO,
  aplicarTotais,
  atosDeValidacao,
  escaparHtml,
  inlineParaHtml,
  nota,
  notasDeSecao,
  pendenciasDoCorpo,
  precedentes,
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
    expect(notasDeSecao("## vazia\n\n## cheia\n\ntexto").has("vazia")).toBe(false);
  });

  it("nota() estoura na chave ausente, para o defeito não sair impresso", () => {
    const notas = notasDeSecao(arquivo);
    expect(nota(notas, "parametros")).toBe("Os campos como gravados.");
    expect(() => nota(notas, "inexistente")).toThrowError(/## inexistente/);
  });
});

describe("aplicarTotais", () => {
  it("substitui cada marcador pelo total correspondente", () => {
    expect(aplicarTotais("as {{regras}} regras, {{pendencias}} pontos", { regras: 112, pendencias: 13 })).toBe(
      "as 112 regras, 13 pontos",
    );
  });

  it("substitui todas as ocorrências do mesmo marcador", () => {
    expect(aplicarTotais("{{regras}} de {{regras}}", { regras: 7 })).toBe("7 de 7");
  });

  it("aceita o total zero em vez de tratá-lo como ausente", () => {
    expect(aplicarTotais("{{pendencias}} pontos", { pendencias: 0 })).toBe("0 pontos");
  });

  it("estoura no marcador desconhecido, em vez de imprimi-lo cru", () => {
    expect(() => aplicarTotais("{{inventado}}", { regras: 1 })).toThrowError(/\{\{inventado\}\}/);
  });

  it("deixa intacto o texto sem marcador", () => {
    expect(aplicarTotais("prosa comum", {})).toBe("prosa comum");
  });
});

describe("atosDeValidacao", () => {
  const ato = {
    tipo: "parecer",
    autoridade: "PGE/RO",
    identificador: "Parecer nº 123/2026",
    fonte: "SEI 0028.123456/2026-11",
  };

  it("lê os quatro campos de cada ato, na ordem gravada", () => {
    expect(atosDeValidacao({ atos_validacao: [ato, { ...ato, identificador: "Parecer nº 124/2026" }] })).toEqual([
      ato,
      { ...ato, identificador: "Parecer nº 124/2026" },
    ]);
  });

  it("devolve lista vazia quando a regra ainda não foi validada", () => {
    expect(atosDeValidacao({})).toEqual([]);
    expect(atosDeValidacao({ atos_validacao: [] })).toEqual([]);
  });

  it("não estoura com um campo ausente — o capítulo sai com a lacuna à vista", () => {
    expect(atosDeValidacao({ atos_validacao: [{ tipo: "parecer" }] })).toEqual([
      { tipo: "parecer", autoridade: "", identificador: "", fonte: "" },
    ]);
  });

  it("ignora valor que não é lista, em vez de tratá-lo como um ato", () => {
    expect(atosDeValidacao({ atos_validacao: "SEI 0028.1/2026" })).toEqual([]);
  });
});

describe("precedentes", () => {
  it("lê os campos de cada caso em que a regra foi aplicada", () => {
    const caso = {
      identificador: "0031.117501/2020-19",
      fonte: "SEI",
      parecer: "/pareceres/parecer-0001.md",
      observacao: "concessão deferida",
    };
    expect(precedentes({ precedentes: [caso] })).toEqual([caso]);
  });

  it("não confunde precedente com ato de validação — são campos distintos", () => {
    const dados = {
      precedentes: [{ identificador: "0031.117501/2020-19", fonte: "SEI" }],
      atos_validacao: [],
    };
    expect(precedentes(dados)).toHaveLength(1);
    expect(atosDeValidacao(dados)).toEqual([]);
  });

  it("devolve lista vazia quando a regra não tem precedente anotado", () => {
    expect(precedentes({})).toEqual([]);
  });

  it("completa campo opcional ausente em vez de estourar", () => {
    expect(precedentes({ precedentes: [{ identificador: "x", fonte: "SEI" }] })).toEqual([
      { identificador: "x", fonte: "SEI", parecer: "", observacao: "" },
    ]);
  });
});

describe("inlineParaHtml", () => {
  it("converte código, ênfase forte e ênfase", () => {
    expect(inlineParaHtml("o `campo` é **obrigatório** e *aberto*")).toBe(
      "o <code>campo</code> é <strong>obrigatório</strong> e <em>aberto</em>",
    );
  });

  it("reduz o link ao seu texto — o destino não existe dentro do PDF", () => {
    expect(inlineParaHtml("ver a [conferência](../../docs/analysis/x.md) completa")).toBe(
      "ver a conferência completa",
    );
  });

  it("escapa o que viria do texto autorado antes de virar HTML", () => {
    expect(inlineParaHtml('art. 40 <b>&"</b>')).toBe("art. 40 &lt;b&gt;&amp;&quot;&lt;/b&gt;");
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
    expect(escaparHtml('<a href="x">&</a>')).toBe("&lt;a href=&quot;x&quot;&gt;&amp;&lt;/a&gt;");
  });
});

describe("pendenciasDoCorpo", () => {
  it("extrai apenas os itens não marcados, na ordem do corpo", () => {
    const corpo = [
      "# Estado da análise",
      "",
      "Prosa qualquer.",
      "",
      "- [x] conferido item a item",
      "- [ ] primeira pendência",
      "- [ ] segunda pendência",
    ].join("\n");

    expect(pendenciasDoCorpo(corpo)).toEqual(["primeira pendência", "segunda pendência"]);
  });

  it("preserva o markdown do item verbatim, sem interpretar nem encurtar", () => {
    const corpo = "- [ ] `data_direito_ate: 31/12/2099` discorda do prazo do [art. 4º](../x.md)";
    expect(pendenciasDoCorpo(corpo)).toEqual([
      "`data_direito_ate: 31/12/2099` discorda do prazo do [art. 4º](../x.md)",
    ]);
  });

  it("aceita as duas grafias de marcador e o item indentado", () => {
    expect(pendenciasDoCorpo("* [ ] com asterisco\n  - [ ] indentado")).toEqual([
      "com asterisco",
      "indentado",
    ]);
  });

  it("ignora o item marcado em maiúscula e o texto que só parece checklist", () => {
    const corpo = ["- [X] marcado", "- [ ]", "o texto - [ ] no meio da linha", "- [ ] real"].join("\n");
    expect(pendenciasDoCorpo(corpo)).toEqual(["real"]);
  });

  it("devolve lista vazia para um corpo sem checklist", () => {
    expect(pendenciasDoCorpo("# Estado da análise\n\nsó prosa.\n")).toEqual([]);
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
      capitulo({ dispositivos: 7, pendencias: 3, achados: 1, achadosAbertos: 1 }),
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

  it("um achado resolvido conta como achado do capítulo, mas não como aberto", () => {
    const resumo = resumoDoRelatorio([capitulo({ achados: 2, achadosAbertos: 0 })]);
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
