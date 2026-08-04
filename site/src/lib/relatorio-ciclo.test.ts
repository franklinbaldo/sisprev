import { describe, expect, it } from "vitest";
import {
  celulasDaProjecao,
  colunasPreenchidas,
  estadoDoGrupoLegivel,
  estadoLegivel,
  gruposDaCadeia,
  idDaRef,
  linhasDoGrupo,
  type ConjuntoDeclarado,
  type SubstituicaoDeclarada,
  partesDoRelatorio,
  resumoDoCiclo,
  tituloDoCapitulo,
} from "./relatorio-ciclo";

const grupo = (parcial: Partial<Parameters<typeof linhasDoGrupo>[0]> = {}) => ({
  grupo: "g1",
  origens: ["regra-0001"],
  destinos: ["u-a", "u-b"],
  estado_grupo: "inativo",
  ...parcial,
});

const linha = (proposta: string, parcial: Record<string, unknown> = {}) => ({
  proposta,
  grupo: "g1",
  deployable: false,
  colunas: {} as Record<string, string>,
  ...parcial,
});

describe("resumoDoCiclo", () => {
  it("conta origens sem repetição", () => {
    const grupos = [
      grupo({
        grupo: "g1",
        origens: ["regra-0001", "regra-0002"],
        destinos: ["u-a"],
      }),
      grupo({ grupo: "g2", origens: ["regra-0002"], destinos: ["u-b"] }),
    ];

    // Uma capa assinada que soma a mesma regra duas vezes afirma um número
    // maior de regras a desativar do que a proposta realmente atinge.
    expect(resumoDoCiclo(grupos, []).origens).toBe(2);
  });

  it("conta destinos sem repetição", () => {
    const grupos = [grupo({ destinos: ["u-a", "u-a", "u-b"] })];

    expect(resumoDoCiclo(grupos, []).destinos).toBe(2);
  });

  it("separa grupos ativos dos inativos", () => {
    const grupos = [
      grupo({ grupo: "g1", estado_grupo: "ativo" }),
      grupo({ grupo: "g2" }),
    ];

    const resumo = resumoDoCiclo(grupos, []);

    expect(resumo.grupos).toBe(2);
    expect(resumo.gruposAtivos).toBe(1);
  });

  it("conta as linhas liberadas para o sistema", () => {
    const linhas = [linha("u-a", { deployable: true }), linha("u-b")];

    expect(resumoDoCiclo([], linhas).linhasDeployable).toBe(1);
  });
});

describe("celulasDaProjecao", () => {
  it("converte a texto sem reformatar o valor autorado", () => {
    // A célula é conferida contra a tela do Sisprev: uma data reescrita ou um
    // booleano traduzido aqui é uma célula que não se coteja.
    expect(
      celulasDaProjecao({
        data_adm_ate: "31/12/2003 00:00",
        validado_pge: "FALSE",
        paridade: "S",
      }),
    ).toEqual({
      data_adm_ate: "31/12/2003 00:00",
      validado_pge: "FALSE",
      paridade: "S",
    });
  });

  it("dá célula vazia ao valor ausente, em vez de imprimir null", () => {
    expect(celulasDaProjecao({ sexo: null, tipo: undefined })).toEqual({
      sexo: "",
      tipo: "",
    });
  });
});

describe("idDaRef", () => {
  it("tira o id da ref de caminho, que o documento nunca imprime", () => {
    expect(idDaRef("/regras/regra-0019.md")).toBe("regra-0019");
    expect(idDaRef("/regras-propostas/regras/incapacidade-causa-comum.md")).toBe("incapacidade-causa-comum");
  });

  it("aceita id já sem caminho nem extensão", () => {
    expect(idDaRef("regra-0019")).toBe("regra-0019");
  });
});

describe("gruposDaCadeia", () => {
  const cadeia = (...conjuntos: ConjuntoDeclarado[]) =>
    new Map(conjuntos.map((conjunto) => [conjunto.id, conjunto]));
  const substituicao = (parcial: Partial<SubstituicaoDeclarada> = {}): SubstituicaoDeclarada => ({
    grupo: "g1",
    origens_legacy: ["/regras/regra-0001.md"],
    destinos_propostos: ["/regras-propostas/regras/u-a.md"],
    estado_grupo: "inativo",
    ...parcial,
  });

  it("colhe os grupos da base mais antiga para a mais recente", () => {
    // O conjunto de fechamento não declara delta próprio: ler só os grupos
    // dele faria o documento dizer que o ciclo não substituiu nada.
    const porId = cadeia(
      { id: "s2", substituicoes: [substituicao({ grupo: "a", estado_grupo: "ativo" })] },
      { id: "s4", base: "s2", substituicoes: [substituicao({ grupo: "c", estado_grupo: "ativo" })] },
      { id: "s6", base: "s4" },
    );

    expect(gruposDaCadeia("s6", porId).map((g) => g.grupo)).toEqual(["a", "c"]);
  });

  it("converte as refs de caminho em ids", () => {
    const porId = cadeia({
      id: "s4",
      substituicoes: [
        substituicao({
          estado_grupo: "ativo",
          origens_legacy: ["/regras/regra-0019.md", "/regras/regra-0020.md"],
          destinos_propostos: ["/regras-propostas/regras/u-a.md"],
        }),
      ],
    });

    const [grupo] = gruposDaCadeia("s4", porId);

    expect(grupo.origens).toEqual(["regra-0019", "regra-0020"]);
    expect(grupo.destinos).toEqual(["u-a"]);
  });

  it("deixa de fora o grupo que a auditoria não promoveu", () => {
    const porId = cadeia({
      id: "s6",
      substituicoes: [substituicao({ grupo: "a" }), substituicao({ grupo: "c", estado_grupo: "ativo" })],
    });

    expect(gruposDaCadeia("s6", porId).map((g) => g.grupo)).toEqual(["c"]);
  });

  it("faz valer a redeclaração mais recente, no lugar da primeira", () => {
    const porId = cadeia(
      {
        id: "s2",
        substituicoes: [
          substituicao({ grupo: "a", estado_grupo: "ativo", destinos_propostos: ["/x/u-a.md"] }),
        ],
      },
      { id: "s3", base: "s2", substituicoes: [substituicao({ grupo: "b", estado_grupo: "ativo" })] },
      {
        id: "s4",
        base: "s3",
        substituicoes: [
          substituicao({ grupo: "a", estado_grupo: "ativo", destinos_propostos: ["/x/u-a.md", "/x/u-b.md"] }),
        ],
      },
    );

    const grupos = gruposDaCadeia("s4", porId);

    expect(grupos.map((g) => g.grupo)).toEqual(["a", "b"]);
    expect(grupos[0].destinos).toEqual(["u-a", "u-b"]);
  });

  it("estoura em cadeia que volta sobre si, em vez de travar o build", () => {
    const porId = cadeia({ id: "s2", base: "s6" }, { id: "s6", base: "s2" });

    expect(() => gruposDaCadeia("s6", porId)).toThrow(/duas vezes/);
  });

  it("devolve vazio para conjunto que não existe", () => {
    expect(gruposDaCadeia("fantasma", cadeia())).toEqual([]);
  });
});

describe("linhasDoGrupo", () => {
  it("segue a ordem em que o grupo declarou os destinos", () => {
    const g = grupo({ destinos: ["u-b", "u-a"] });
    const linhas = [linha("u-a"), linha("u-b")];

    expect(linhasDoGrupo(g, linhas).map((l) => l.proposta)).toEqual([
      "u-b",
      "u-a",
    ]);
  });

  it("ignora destino sem linha projetada em vez de emitir buraco", () => {
    const g = grupo({ destinos: ["u-a", "u-fantasma"] });

    expect(linhasDoGrupo(g, [linha("u-a")]).map((l) => l.proposta)).toEqual([
      "u-a",
    ]);
  });
});

describe("colunasPreenchidas", () => {
  it("mantém só as colunas que algum destino do grupo preenche", () => {
    const colunas = ["NOME", "SEXO", "TIPO_REMUN"];
    const linhas = [
      { NOME: "a", SEXO: "AMBOS", TIPO_REMUN: "" },
      { NOME: "b", SEXO: "", TIPO_REMUN: "" },
    ];

    expect(colunasPreenchidas(colunas, linhas)).toEqual(["NOME", "SEXO"]);
  });

  it("trata célula só com espaços como vazia", () => {
    expect(colunasPreenchidas(["A"], [{ A: "   " }])).toEqual([]);
  });

  it("preserva a ordem declarada das colunas", () => {
    const colunas = ["C", "A", "B"];

    expect(colunasPreenchidas(colunas, [{ A: "x", B: "y", C: "z" }])).toEqual([
      "C",
      "A",
      "B",
    ]);
  });

  it("devolve vazio quando o grupo não projeta linha alguma", () => {
    expect(colunasPreenchidas(["A", "B"], [])).toEqual([]);
  });
});

describe("partesDoRelatorio", () => {
  const corpo = [
    "<!-- abertura -->",
    "# Objeto",
    "prosa de abertura",
    "<!-- notas -->",
    "## parametros",
    "nota de parametros",
    "<!-- encerramento -->",
    "# Providencias",
    "prosa final",
  ].join("\n\n");

  it("reparte nas tres partes, sem os delimitadores", () => {
    const partes = partesDoRelatorio(corpo);

    expect(partes.abertura).toBe("# Objeto\n\nprosa de abertura");
    expect(partes.notas).toBe("## parametros\n\nnota de parametros");
    expect(partes.encerramento).toBe("# Providencias\n\nprosa final");
  });

  it("estoura quando falta um delimitador", () => {
    // Sem a excecao, um `<!-- notas -->` esquecido faria as notas serem lidas
    // como abertura e todo o documento sair sem nota nenhuma - num relatorio
    // que ja teria sido juntado ao processo.
    expect(() =>
      partesDoRelatorio(corpo.replace("<!-- notas -->", "")),
    ).toThrow(/falta o delimitador/);
  });

  it("estoura quando os delimitadores saem de ordem", () => {
    const trocado = [
      "<!-- abertura -->",
      "a",
      "<!-- encerramento -->",
      "c",
      "<!-- notas -->",
      "b",
    ].join("\n\n");

    expect(() => partesDoRelatorio(trocado)).toThrow(/antes de/);
  });
});

describe("estadoLegivel", () => {
  it("diz em português os três estados do vocabulário", () => {
    expect(estadoLegivel("elaboracao")).toBe("em elaboração");
    expect(estadoLegivel("preview")).toBe("em conferência");
    expect(estadoLegivel("deployable")).toBe("pronta para o sistema");
  });

  it("devolve verbatim o que não conhece, em vez de traduzir por aproximação", () => {
    expect(estadoLegivel("promovida")).toBe("promovida");
    expect(estadoLegivel("")).toBe("");
  });
});

describe("tituloDoCapitulo", () => {
  it("diz a substituição em regras, não em origens e destinos", () => {
    expect(tituloDoCapitulo(2, 20)).toBe(
      "2 regras cadastradas substituídas por 20 regras propostas",
    );
  });

  it("concorda no singular, porque um grupo de uma origem existe", () => {
    expect(tituloDoCapitulo(1, 1)).toBe(
      "1 regra cadastrada substituída por 1 regra proposta",
    );
  });
});

describe("estadoDoGrupoLegivel", () => {
  it("diz o efeito do grupo sobre a proposta", () => {
    expect(estadoDoGrupoLegivel("ativo")).toBe("integra a proposta");
    expect(estadoDoGrupoLegivel("inativo")).toBe("fora da proposta");
  });

  it("devolve verbatim o que não conhece", () => {
    expect(estadoDoGrupoLegivel("suspenso")).toBe("suspenso");
  });
});
