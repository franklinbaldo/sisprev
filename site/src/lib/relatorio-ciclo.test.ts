import { describe, expect, it } from "vitest";
import {
  celulasDaProjecao,
  colunasPreenchidas,
  classesDeRessalva,
  componentesDoCiclo,
  consolidarPontos,
  destinosComRessalvaDoCiclo,
  estadoDoComponenteLegivel,
  estadoLegivel,
  linhasDoComponente,
  type ComponenteDeImplantacao,
  type PropostaDeclarada,
  partesDoRelatorio,
  regrasRessalvadas,
  resumoDoCiclo,
  resumoDoComponente,
  selosDoComponente,
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

  it("marca pronto quando estado_implantacao é confirmada_com_ressalva com ressalva preenchida (RFC 0004, round 12)", () => {
    // regra-0020/regra-0021 já produzem, em produção, a mesma combinação para
    // a mesma hipótese: a ressalva de homologação não bloqueia a carga.
    const propostas = [
      proposta("causa-comum", {
        origensLegacy: ["regra-0020"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "confirmada_com_ressalva",
        ressalvaHomologacao: "confirmar em homologação prática",
      }),
    ];

    expect(componentesDoCiclo("ciclo-01", propostas)[0].pronto).toBe(true);
  });

  it("marca não pronto quando confirmada_com_ressalva não tem ressalva_homologacao", () => {
    // Mesma checagem que `_carga_de_implantacao` já aplica em
    // `scripts/derivar.py`: o rótulo promete uma ressalva registrada, e sem
    // ela o estado não se sustenta.
    const propostas = [
      proposta("causa-comum", {
        origensLegacy: ["regra-0020"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "confirmada_com_ressalva",
      }),
    ];

    expect(componentesDoCiclo("ciclo-01", propostas)[0].pronto).toBe(false);
  });

  it("marca não pronto quando ressalva_homologacao está preenchida fora de confirmada_com_ressalva", () => {
    // Ressalva residual num estado comum é tão enganosa quanto a ausência
    // dela em confirmada_com_ressalva.
    const propostas = [
      proposta("u-a", {
        origensLegacy: ["regra-0019"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "confirmada",
        ressalvaHomologacao: "ressalva residual indevida",
      }),
    ];

    expect(componentesDoCiclo("ciclo-01", propostas)[0].pronto).toBe(false);
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

describe("destinosComRessalvaDoCiclo", () => {
  it("conta destino com ressalva cujo componente está pronto", () => {
    const componentes = [componente({ destinos: ["u-a"], pronto: true })];
    const propostas = [proposta("u-a", { estadoImplantacao: "confirmada_com_ressalva" })];

    expect(destinosComRessalvaDoCiclo(componentes, propostas)).toBe(1);
  });

  it("não conta destino com ressalva cujo componente não está pronto", () => {
    // Um componente com dois destinos: u-a leva ressalva, mas u-b bloqueia o
    // componente inteiro (estado_auditoria inválido) — nenhum dos dois entra
    // na carga de homologação, então nenhum deve ser contado como "com
    // ressalva na carga".
    const componentes = [componente({ destinos: ["u-a", "u-b"], pronto: false })];
    const propostas = [
      proposta("u-a", { estadoImplantacao: "confirmada_com_ressalva" }),
      proposta("u-b", { estadoAuditoria: "preview" }),
    ];

    expect(destinosComRessalvaDoCiclo(componentes, propostas)).toBe(0);
  });

  it("não conta destino confirmado sem ressalva", () => {
    const componentes = [componente({ destinos: ["u-a"], pronto: true })];
    const propostas = [proposta("u-a", { estadoAuditoria: "concluida", estadoImplantacao: "confirmada" })];

    expect(destinosComRessalvaDoCiclo(componentes, propostas)).toBe(0);
  });

  it("soma destinos com ressalva de componentes prontos distintos", () => {
    const componentes = [
      componente({ destinos: ["u-a"], pronto: true }),
      componente({ destinos: ["u-b"], pronto: true }),
      componente({ destinos: ["u-c"], pronto: false }),
    ];
    const propostas = [
      proposta("u-a", { estadoImplantacao: "confirmada_com_ressalva" }),
      proposta("u-b", { estadoImplantacao: "confirmada_com_ressalva" }),
      proposta("u-c", { estadoImplantacao: "confirmada_com_ressalva" }),
    ];

    expect(destinosComRessalvaDoCiclo(componentes, propostas)).toBe(2);
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
  it("diz o efeito do componente sobre a carga de homologação", () => {
    expect(estadoDoComponenteLegivel(true)).toBe("integra a carga de homologação");
    expect(estadoDoComponenteLegivel(false)).toBe("fora da carga de homologação");
  });
});

describe("consolidarPontos", () => {
  it("junta num ponto só a pendência que várias regras repetem, e diz quais alcança", () => {
    const pontos = consolidarPontos([
      { id: "u-a", pontos: ["<code>C1-R34</code> — falta o teto do RGPS"] },
      { id: "u-b", pontos: ["<code>C1-R34</code> — falta o teto do RGPS"] },
      { id: "u-c", pontos: ["<code>C1-R34</code> — falta o teto do RGPS"] },
    ]);

    expect(pontos).toHaveLength(1);
    expect(pontos[0].regras).toEqual(["u-a", "u-b", "u-c"]);
  });

  it("preserva a ordem de primeira aparição, que é a numeração impressa", () => {
    const pontos = consolidarPontos([
      { id: "u-a", pontos: ["primeira", "segunda"] },
      { id: "u-b", pontos: ["segunda", "terceira"] },
    ]);

    expect(pontos.map((p) => p.html)).toEqual(["primeira", "segunda", "terceira"]);
    expect(pontos.map((p) => p.regras)).toEqual([["u-a"], ["u-a", "u-b"], ["u-b"]]);
  });

  it("não funde enunciados diferentes, porque dizer que tratam do mesmo é mérito", () => {
    const pontos = consolidarPontos([
      { id: "u-a", pontos: ["falta o teto do RGPS"] },
      { id: "u-b", pontos: ["falta o limite máximo dos benefícios do RGPS"] },
    ]);

    expect(pontos).toHaveLength(2);
  });

  it("não repete a mesma regra quando ela escreve a pendência duas vezes", () => {
    const pontos = consolidarPontos([{ id: "u-a", pontos: ["mesma", "mesma"] }]);

    expect(pontos).toHaveLength(1);
    expect(pontos[0].regras).toEqual(["u-a"]);
  });

  it("devolve lista vazia quando nenhum destino deixou conferência em aberto", () => {
    expect(consolidarPontos([{ id: "u-a", pontos: [] }])).toEqual([]);
  });
});

describe("classesDeRessalva", () => {
  const ressalvada = (parcial: Partial<PropostaDeclarada>) =>
    proposta("u", {
      estadoAuditoria: "concluida",
      estadoImplantacao: "confirmada_com_ressalva",
      ressalvaHomologacao: "confirmar",
      ...parcial,
    });

  it("deriva a classe do predicado, não do texto da ressalva", () => {
    // O texto fala de uma coisa e o predicado de outra: vale o predicado.
    // Classificar prosa por palavra-chave é o modo de falha que este
    // repositório já conheceu.
    const p = ressalvada({
      causaIncapacidade: "causa_comum",
      ressalvaHomologacao: "nada aqui menciona proporcionalização",
    });
    expect(classesDeRessalva(p)).toEqual(["proporcionalizacao"]);
  });

  it("dá as duas classes à regra que acumula causa comum e sujeição ao RPC", () => {
    const p = ressalvada({ causaIncapacidade: "causa_comum", vinculoRpc: "sujeito" });
    expect(classesDeRessalva(p)).toEqual(["proporcionalizacao", "rpc_teto"]);
  });

  it("não classifica regra sem ressalva, ainda que o predicado combine", () => {
    // Uma causa comum `confirmada` não entra na contagem da classe: a classe
    // qualifica a ressalva, e sem ressalva não há o que qualificar.
    const p = proposta("u", {
      estadoAuditoria: "concluida",
      estadoImplantacao: "confirmada",
      causaIncapacidade: "causa_comum",
    });
    expect(classesDeRessalva(p)).toEqual([]);
  });

  it("não classifica quando o estado é pendente_mapeamento_sisprev", () => {
    const p = proposta("u", {
      estadoImplantacao: "pendente_mapeamento_sisprev",
      vinculoRpc: "sujeito",
    });
    expect(classesDeRessalva(p)).toEqual([]);
  });
});

describe("resumoDoComponente e selosDoComponente", () => {
  const comRessalva = (id: string, parcial: Partial<PropostaDeclarada> = {}) =>
    proposta(id, {
      estadoAuditoria: "concluida",
      estadoImplantacao: "confirmada_com_ressalva",
      ressalvaHomologacao: "confirmar",
      ...parcial,
    });

  it("conta as ressalvadas e as não ressalvadas do componente", () => {
    const propostas = [
      comRessalva("u-a", { vinculoRpc: "sujeito" }),
      proposta("u-b", { estadoAuditoria: "concluida" }),
      proposta("u-c", { estadoAuditoria: "concluida" }),
    ];
    const resumo = resumoDoComponente(componente({ destinos: ["u-a", "u-b", "u-c"] }), propostas);

    expect(resumo.comRessalva).toBe(1);
    expect(resumo.semRessalva).toBe(2);
    expect(resumo.classes).toEqual(["rpc_teto"]);
  });

  it("nomeia as duas populações separadamente, e não confunde uma com a outra", () => {
    // O defeito concreto: o componente de uma única causa comum ressalvada
    // imprimia "0 ressalvas", porque o selo contava conferências abertas.
    const propostas = [comRessalva("causa-comum", { causaIncapacidade: "causa_comum" })];
    const resumo = resumoDoComponente(componente({ destinos: ["causa-comum"] }), propostas);

    expect(selosDoComponente(resumo, 0)).toEqual([
      "1 regra com ressalva de homologação",
      "Nenhuma conferência em aberto",
    ]);
  });

  it("admite componente sem regra ressalvada e com conferência aberta", () => {
    const propostas = [proposta("u-a", { estadoAuditoria: "concluida" })];
    const resumo = resumoDoComponente(componente({ destinos: ["u-a"] }), propostas);

    expect(selosDoComponente(resumo, 1)).toEqual([
      "Nenhuma regra com ressalva de homologação",
      "1 conferência em aberto",
    ]);
  });
});

describe("regrasRessalvadas", () => {
  it("identifica cada regra ressalvada com o seu componente e as suas classes", () => {
    const propostas = [
      proposta("cc-1", {
        origensLegacy: ["regra-0020"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "confirmada_com_ressalva",
        ressalvaHomologacao: "confirmar",
        causaIncapacidade: "causa_comum",
      }),
      proposta("rpc-1", {
        origensLegacy: ["regra-0022"],
        estadoAuditoria: "concluida",
        estadoImplantacao: "confirmada_com_ressalva",
        ressalvaHomologacao: "confirmar",
        vinculoRpc: "sujeito",
      }),
      proposta("limpa", { origensLegacy: ["regra-0022"], estadoAuditoria: "concluida" }),
    ];
    const componentes = componentesDoCiclo("ciclo-01", propostas);

    const ressalvadas = regrasRessalvadas(componentes, propostas);

    expect(ressalvadas.map((r) => r.id).sort()).toEqual(["cc-1", "rpc-1"]);
    expect(ressalvadas.find((r) => r.id === "cc-1")?.classes).toEqual(["proporcionalizacao"]);
    expect(ressalvadas.find((r) => r.id === "rpc-1")?.classes).toEqual(["rpc_teto"]);
    // A regra sem ressalva não entra na matriz — mas continua no componente.
    expect(ressalvadas.some((r) => r.id === "limpa")).toBe(false);
  });
});
