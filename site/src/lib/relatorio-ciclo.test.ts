import { describe, expect, it } from "vitest";
import {
  celulasDaProjecao,
  colunasPreenchidas,
  componentesDoCiclo,
  estadoDoComponenteLegivel,
  estadoLegivel,
  linhasDoComponente,
  type ComponenteDeImplantacao,
  type PropostaDeclarada,
  partesDoRelatorio,
  resumoDoCiclo,
  tituloDoCapitulo,
} from "./relatorio-ciclo";

const componente = (parcial: Partial<ComponenteDeImplantacao> = {}): ComponenteDeImplantacao => ({
  origens: ["regra-0001"],
  destinos: ["u-a", "u-b"],
  pronto: false,
  ...parcial,
});

const proposta = (id: string, parcial: Partial<PropostaDeclarada> = {}): PropostaDeclarada => ({
  id,
  ciclo: "ciclo-01",
  origensLegacy: ["regra-0001"],
  estadoAuditoria: "elaboracao",
  ...parcial,
});

const linha = (proposta: string, parcial: Record<string, unknown> = {}) => ({
  proposta,
  colunas: {} as Record<string, string>,
  ...parcial,
});

describe("componentesDoCiclo", () => {
  it("junta propostas que compartilham origem no mesmo componente", () => {
    const propostas = [
      proposta("u-a", { origensLegacy: ["regra-0019"] }),
      proposta("u-b", { origensLegacy: ["regra-0019"] }),
      proposta("u-c", { origensLegacy: ["regra-0020"] }),
    ];

    const componentes = componentesDoCiclo("ciclo-01", propostas);

    expect(componentes).toHaveLength(2);
    const porOrigens = componentes.map((c) => [...c.destinos].sort());
    expect(porOrigens).toContainEqual(["u-a", "u-b"]);
    expect(porOrigens).toContainEqual(["u-c"]);
  });

  it("une transitivamente quando destinos diferentes compartilham origens diferentes", () => {
    // u-a e u-b compartilham regra-0001; u-b e u-c compartilham regra-0002 —
    // as três entram no mesmo componente, mesmo sem par comum a todas.
    const propostas = [
      proposta("u-a", { origensLegacy: ["regra-0001"] }),
      proposta("u-b", { origensLegacy: ["regra-0001", "regra-0002"] }),
      proposta("u-c", { origensLegacy: ["regra-0002"] }),
    ];

    const componentes = componentesDoCiclo("ciclo-01", propostas);

    expect(componentes).toHaveLength(1);
    expect([...componentes[0].destinos].sort()).toEqual(["u-a", "u-b", "u-c"]);
  });

  it("ignora propostas de outro ciclo", () => {
    const propostas = [
      proposta("u-a", { ciclo: "ciclo-01" }),
      proposta("u-b", { ciclo: "ciclo-02" }),
    ];

    expect(componentesDoCiclo("ciclo-01", propostas).flatMap((c) => c.destinos)).toEqual(["u-a"]);
  });

  it("marca pronto só quando todos os membros estão concluídos e confirmados", () => {
    const propostas = [
      proposta("u-a", { origensLegacy: ["regra-0019"], estadoAuditoria: "concluida" }),
      proposta("u-b", {
        origensLegacy: ["regra-0019"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "pendente_mapeamento_sisprev",
      }),
    ];

    expect(componentesDoCiclo("ciclo-01", propostas)[0].pronto).toBe(false);
  });

  it("trata estado_implantacao ausente como confirmada", () => {
    const propostas = [proposta("u-a", { origensLegacy: ["regra-0019"], estadoAuditoria: "concluida" })];

    expect(componentesDoCiclo("ciclo-01", propostas)[0].pronto).toBe(true);
  });

  it("não deixa a pendência de um componente bloquear outro sem origem compartilhada", () => {
    // O achado real do Ciclo 1: dezenove destinos de uma origem e um destino
    // de causa comum de outra não se misturam só por pertencerem à mesma
    // coorte — só entram no mesmo componente se compartilharem origem.
    const propostas = [
      proposta("qualificada-1", { origensLegacy: ["regra-0019"], estadoAuditoria: "concluida" }),
      proposta("qualificada-2", { origensLegacy: ["regra-0019"], estadoAuditoria: "concluida" }),
      proposta("causa-comum", {
        origensLegacy: ["regra-0020"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "pendente_mapeamento_sisprev",
      }),
    ];

    const componentes = componentesDoCiclo("ciclo-01", propostas);

    expect(componentes).toHaveLength(2);
    const qualificadas = componentes.find((c) => c.destinos.includes("qualificada-1"));
    const causaComum = componentes.find((c) => c.destinos.includes("causa-comum"));
    expect(qualificadas?.pronto).toBe(true);
    expect(causaComum?.pronto).toBe(false);
  });
});

describe("resumoDoCiclo", () => {
  it("conta origens sem repetição", () => {
    const componentes = [
      componente({ origens: ["regra-0001", "regra-0002"], destinos: ["u-a"] }),
      componente({ origens: ["regra-0002"], destinos: ["u-b"] }),
    ];

    // Uma capa assinada que soma a mesma regra duas vezes afirma um número
    // maior de regras a desativar do que a proposta realmente atinge.
    expect(resumoDoCiclo(componentes, []).origens).toBe(2);
  });

  it("conta destinos sem repetição", () => {
    const componentes = [componente({ destinos: ["u-a", "u-a", "u-b"] })];

    expect(resumoDoCiclo(componentes, []).destinos).toBe(2);
  });

  it("separa componentes prontos dos que não estão", () => {
    const componentes = [componente({ pronto: true }), componente({ pronto: false })];

    const resumo = resumoDoCiclo(componentes, []);

    expect(resumo.componentes).toBe(2);
    expect(resumo.componentesProntos).toBe(1);
  });

  it("conta só as linhas concluídas cujo destino está nos componentes", () => {
    const componentes = [componente({ destinos: ["u-a", "u-b"] })];
    const propostas = [
      proposta("u-a", { estadoAuditoria: "concluida" }),
      proposta("u-b", { estadoAuditoria: "elaboracao" }),
      proposta("u-fora", { estadoAuditoria: "concluida" }),
    ];

    expect(resumoDoCiclo(componentes, propostas).linhasConcluidas).toBe(1);
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

describe("linhasDoComponente", () => {
  it("segue a ordem em que o componente declarou os destinos", () => {
    const c = componente({ destinos: ["u-b", "u-a"] });
    const linhas = [linha("u-a"), linha("u-b")];

    expect(linhasDoComponente(c, linhas).map((l) => l.proposta)).toEqual(["u-b", "u-a"]);
  });

  it("ignora destino sem linha projetada em vez de emitir buraco", () => {
    const c = componente({ destinos: ["u-a", "u-fantasma"] });

    expect(linhasDoComponente(c, [linha("u-a")]).map((l) => l.proposta)).toEqual(["u-a"]);
  });
});

describe("colunasPreenchidas", () => {
  it("mantém só as colunas que algum destino do componente preenche", () => {
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

    expect(colunasPreenchidas(colunas, [{ A: "x", B: "y", C: "z" }])).toEqual(["C", "A", "B"]);
  });

  it("devolve vazio quando o componente não projeta linha alguma", () => {
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
    expect(estadoLegivel("concluida")).toBe("auditoria jurídica concluída");
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

  it("concorda no singular, porque um componente de uma origem existe", () => {
    expect(tituloDoCapitulo(1, 1)).toBe(
      "1 regra cadastrada substituída por 1 regra proposta",
    );
  });
});

describe("estadoDoComponenteLegivel", () => {
  it("diz o efeito do componente sobre a carga de implantação", () => {
    expect(estadoDoComponenteLegivel(true)).toBe("integra a carga de implantação");
    expect(estadoDoComponenteLegivel(false)).toBe("fora da carga de implantação");
  });
});
