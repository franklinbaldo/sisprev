import { describe, expect, it } from "vitest";
import {
  colunasPreenchidas,
  linhasDoGrupo,
  partesDoRelatorio,
  resumoDoCiclo,
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
  pendencias: [] as string[],
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

  it("conta linhas liberadas e linhas com pendência", () => {
    const linhas = [
      linha("u-a", { deployable: true }),
      linha("u-b", { pendencias: ["P_COMPILA_ESTADO_INVALIDO"] }),
      linha("u-c"),
    ];

    const resumo = resumoDoCiclo([], linhas);

    expect(resumo.linhasDeployable).toBe(1);
    expect(resumo.linhasComPendencia).toBe(1);
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
    expect(() => partesDoRelatorio(corpo.replace("<!-- notas -->", ""))).toThrow(
      /falta o delimitador/,
    );
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
