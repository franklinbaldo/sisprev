import { describe, expect, it } from "vitest";
import { avaliarRegra, avaliarSolicitacao, regrasSimuladorFromJSON, type FatosRequerimento, type RegraSimulador } from "./simulador";

function makeRegra(overrides: Partial<RegraSimulador> = {}): RegraSimulador {
  return {
    id: "regra-0001",
    nome: "Regra Teste",
    tipoDeBeneficio: "APOSENTADORIA POR INVALIDEZ",
    sexo: "AMBOS",
    aposEspecial: false,
    simulavel: true,
    statusRegra: null,
    dataAdmApos: new Date(1910, 0, 1),
    dataAdmAte: new Date(2003, 11, 31),
    dataDireitoApos: new Date(1910, 0, 1),
    dataDireitoAte: new Date(2003, 11, 31),
    integral: true,
    tipoCalculo: "Valor Médio",
    paridade: true,
    ...overrides,
  };
}

function makeFatos(overrides: Partial<FatosRequerimento> = {}): FatosRequerimento {
  return {
    tipoDeBeneficio: "APOSENTADORIA POR INVALIDEZ",
    sexo: null,
    // Matches makeRegra()'s default aposEspecial (false), so tests that
    // aren't specifically about this criterion don't spuriously land on
    // "indeterminada" from an unrelated unanswered fact.
    aposEspecial: false,
    dataAdmissao: null,
    dataDireito: null,
    ...overrides,
  };
}

describe("avaliarRegra — critérios individuais", () => {
  it("exclui por tipo de benefício diferente", () => {
    const resultado = avaliarRegra(makeRegra({ tipoDeBeneficio: "PENSÃO POR MORTE" }), makeFatos());
    expect(resultado.valor).toBe("incompativel");
    expect(resultado.motivoExclusao).toMatch(/tipo de benefício/i);
  });

  it("fica indeterminada quando o sexo da regra está vazio (Q10)", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "" }), makeFatos({ sexo: "FEMININO" }));
    expect(resultado.valor).toBe("indeterminada");
    expect(resultado.fatosPendentes.some((f) => /Q10/.test(f))).toBe(true);
  });

  it("é compatível quando a regra aceita AMBOS e o sexo não foi informado", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "AMBOS" }), makeFatos());
    expect(resultado.valor).toBe("compativel");
  });

  it("exclui por sexo diferente", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "MASCULINO" }), makeFatos({ sexo: "FEMININO" }));
    expect(resultado.valor).toBe("incompativel");
  });

  it("fica indeterminada quando o sexo do requerente não foi informado e a regra exige um sexo específico", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "MASCULINO" }), makeFatos({ sexo: null }));
    expect(resultado.valor).toBe("indeterminada");
  });

  it("exclui por aposentadoria especial diferente", () => {
    const resultado = avaliarRegra(makeRegra({ aposEspecial: true }), makeFatos({ aposEspecial: false }));
    expect(resultado.valor).toBe("incompativel");
  });

  it("fica indeterminada quando aposentadoria especial não foi informada", () => {
    const resultado = avaliarRegra(makeRegra({ aposEspecial: true }), makeFatos({ aposEspecial: null }));
    expect(resultado.valor).toBe("indeterminada");
  });

  it("é compatível quando a data de admissão cai estritamente dentro da janela", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: new Date(2000, 0, 1) }));
    expect(resultado.valor).toBe("compativel");
    expect(resultado.criteriosSatisfeitos).toContain("Data de admissão");
  });

  it("exclui quando a data de admissão é anterior ao limite inferior", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: new Date(1900, 0, 1) }));
    expect(resultado.valor).toBe("incompativel");
  });

  it("exclui quando a data de admissão é posterior ao limite superior", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: new Date(2020, 0, 1) }));
    expect(resultado.valor).toBe("incompativel");
  });

  it("fica indeterminada quando a data informada coincide exatamente com um limite (Q1/Q2)", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: new Date(2003, 11, 31) }));
    expect(resultado.valor).toBe("indeterminada");
    expect(resultado.fatosPendentes.some((f) => /Q1\/Q2/.test(f))).toBe(true);
  });

  it("fica indeterminada quando um limite da janela está vazio no catálogo", () => {
    const resultado = avaliarRegra(makeRegra({ dataAdmAte: null }), makeFatos({ dataAdmissao: new Date(2000, 0, 1) }));
    expect(resultado.valor).toBe("indeterminada");
  });

  it("não avalia a janela quando o requerente não informa a data (fato opcional)", () => {
    const resultado = avaliarRegra(makeRegra({ dataAdmAte: null }), makeFatos());
    expect(resultado.valor).toBe("compativel");
    expect(resultado.criteriosSatisfeitos).not.toContain("Data de admissão");
  });
});

describe("avaliarSolicitacao — desfecho agregado (RFC 0002 §4)", () => {
  it("nenhuma — todas as regras são incompatíveis", () => {
    const regras = [makeRegra({ id: "regra-0001" }), makeRegra({ id: "regra-0002" })];
    const rastro = avaliarSolicitacao(regras, makeFatos({ tipoDeBeneficio: "PENSÃO POR MORTE" }));
    expect(rastro.desfecho).toBe("nenhuma");
    expect(rastro.candidatas).toHaveLength(0);
    expect(rastro.eliminadas).toHaveLength(2);
  });

  it("única — uma regra compatível, as demais excluídas", () => {
    const regras = [makeRegra({ id: "regra-0001", sexo: "MASCULINO" }), makeRegra({ id: "regra-0002", sexo: "FEMININO" })];
    const rastro = avaliarSolicitacao(regras, makeFatos({ sexo: "MASCULINO" }));
    expect(rastro.desfecho).toBe("unica");
    expect(rastro.candidatas.map((c) => c.regraId)).toEqual(["regra-0001"]);
  });

  it("múltiplas — duas regras compatíveis pelos fatos conhecidos", () => {
    const regras = [makeRegra({ id: "regra-0001" }), makeRegra({ id: "regra-0002" })];
    const rastro = avaliarSolicitacao(regras, makeFatos());
    expect(rastro.desfecho).toBe("multiplas");
    expect(rastro.candidatas).toHaveLength(2);
  });

  it("indeterminado — uma pendência em qualquer regra derruba o conjunto inteiro", () => {
    const regras = [makeRegra({ id: "regra-0001" }), makeRegra({ id: "regra-0002", sexo: "" })];
    const rastro = avaliarSolicitacao(regras, makeFatos());
    expect(rastro.desfecho).toBe("indeterminado");
    expect(rastro.candidatas.map((c) => c.regraId)).toEqual(["regra-0001", "regra-0002"]);
  });

  it("regras simulavel=N e inativas ficam em foraDoEscopo, nunca somem", () => {
    const regras = [
      makeRegra({ id: "regra-0001", simulavel: false }),
      makeRegra({ id: "regra-0002", statusRegra: "inativa" }),
      makeRegra({ id: "regra-0003" }),
    ];
    const rastro = avaliarSolicitacao(regras, makeFatos());
    expect(rastro.foraDoEscopo.map((r) => r.id)).toEqual(["regra-0001", "regra-0002"]);
    expect(rastro.candidatas.map((c) => c.regraId)).toEqual(["regra-0003"]);
  });
});

describe("regrasSimuladorFromJSON — round-trip com o payload embutido na página", () => {
  it("reconstrói datas e booleanos depois de um JSON.stringify/JSON.parse", () => {
    const original = makeRegra({ dataAdmApos: new Date(2000, 5, 15) });
    const serializado: unknown = JSON.parse(JSON.stringify([original]));
    const [reidratada] = regrasSimuladorFromJSON(serializado as unknown[]);

    expect(reidratada.id).toBe(original.id);
    expect(reidratada.dataAdmApos?.getTime()).toBe(original.dataAdmApos?.getTime());
    expect(reidratada.aposEspecial).toBe(original.aposEspecial);
    expect(reidratada.simulavel).toBe(original.simulavel);
  });

  it("produz o mesmo resultado de avaliação antes e depois do round-trip", () => {
    const regra = makeRegra();
    const fatos = makeFatos({ dataAdmissao: new Date(2000, 0, 1) });
    const [reidratada] = regrasSimuladorFromJSON(JSON.parse(JSON.stringify([regra])) as unknown[]);

    expect(avaliarRegra(reidratada, fatos)).toEqual(avaliarRegra(regra, fatos));
  });
});
