import { describe, expect, it } from "vitest";
import { avaliarRegra, avaliarSolicitacao, regrasSimuladorFromJSON, type FatosRequerimento, type RegraSimulador } from "./simulador";
import type { DataCivil } from "./parse-sisprev";

function data(ano: number, mes: number, dia: number): DataCivil {
  return { ano, mes, dia };
}

function makeRegra(overrides: Partial<RegraSimulador> = {}): RegraSimulador {
  return {
    id: "regra-0001",
    nome: "Regra Teste",
    tipoDeBeneficio: "APOSENTADORIA POR INVALIDEZ",
    sexo: "AMBOS",
    aposEspecial: false,
    simulavel: true,
    statusRegra: null,
    // Marcos reais (vigência da EC 20/1998 e da EC 41/2003), nunca sentinela:
    // a fixture usava `01/01/1910` como piso, que é sentinela (RFC 0011) e
    // portanto **não é limite avaliável** — era o mesmo mal-entendido que o
    // motor tinha, reproduzido no fixture que devia flagrá-lo. As sentinelas
    // têm testes próprios abaixo.
    dataAdmApos: data(1998, 12, 16),
    dataAdmAte: data(2003, 12, 31),
    dataDireitoApos: data(1998, 12, 16),
    dataDireitoAte: data(2003, 12, 31),
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
    // a pendency from an unrelated unanswered fact.
    aposEspecial: false,
    dataAdmissao: null,
    dataDireito: null,
    ...overrides,
  };
}

describe("avaliarRegra — critérios individuais", () => {
  it("exclui por tipo de benefício diferente", () => {
    const resultado = avaliarRegra(makeRegra({ tipoDeBeneficio: "PENSÃO POR MORTE" }), makeFatos());
    expect(resultado.valor).toBe("excluida");
    expect(resultado.motivoExclusao).toMatch(/tipo de benefício/i);
  });

  it("não exclui quando o sexo da regra está vazio, mas registra pendência (Q10)", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "" }), makeFatos({ sexo: "FEMININO" }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.some((f) => /Q10/.test(f))).toBe(true);
  });

  it("não gera pendência de sexo quando a regra aceita AMBOS", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "AMBOS" }), makeFatos());
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.criteriosSatisfeitos).toContain("Sexo (regra aceita ambos)");
    expect(resultado.fatosPendentes.some((f) => /[Ss]exo/.test(f))).toBe(false);
  });

  it("exclui por sexo diferente", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "MASCULINO" }), makeFatos({ sexo: "FEMININO" }));
    expect(resultado.valor).toBe("excluida");
  });

  it("registra pendência quando o sexo do requerente não foi informado e a regra exige um sexo específico", () => {
    const resultado = avaliarRegra(makeRegra({ sexo: "MASCULINO" }), makeFatos({ sexo: null }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.length).toBeGreaterThan(0);
  });

  it("exclui por aposentadoria especial diferente", () => {
    const resultado = avaliarRegra(makeRegra({ aposEspecial: true }), makeFatos({ aposEspecial: false }));
    expect(resultado.valor).toBe("excluida");
  });

  it("registra pendência quando aposentadoria especial não foi informada", () => {
    const resultado = avaliarRegra(makeRegra({ aposEspecial: true }), makeFatos({ aposEspecial: null }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.length).toBeGreaterThan(0);
  });

  it("não gera pendência de janela de admissão quando a data cai estritamente dentro (e o fato foi informado)", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: data(2000, 1, 1) }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.criteriosSatisfeitos).toContain("Data de admissão");
    expect(resultado.fatosPendentes.some((f) => /admissão/.test(f))).toBe(false);
  });

  it("exclui quando a data de admissão é anterior ao limite inferior", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: data(1990, 1, 1) }));
    expect(resultado.valor).toBe("excluida");
  });

  it("exclui quando a data de admissão é posterior ao limite superior", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: data(2020, 1, 1) }));
    expect(resultado.valor).toBe("excluida");
  });

  it("registra pendência (não exclui, não confirma) quando a data informada coincide exatamente com um limite (Q1/Q2)", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: data(2003, 12, 31) }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.some((f) => /Q1\/Q2/.test(f))).toBe(true);
  });

  it("registra pendência quando um limite da janela está vazio no catálogo mas a data foi informada", () => {
    const resultado = avaliarRegra(makeRegra({ dataAdmAte: null }), makeFatos({ dataAdmissao: data(2000, 1, 1) }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.length).toBeGreaterThan(0);
  });

  it("Regressão: fato temporal não informado NUNCA vira nao_excluida sem pendência — a ausência do fato é, ela mesma, uma pendência", () => {
    const resultado = avaliarRegra(makeRegra(), makeFatos());
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.fatosPendentes.some((f) => /admissão do requerente não informada/.test(f))).toBe(true);
    expect(resultado.fatosPendentes.some((f) => /aquisição do direito do requerente não informada/.test(f))).toBe(true);
  });

  it("não gera pendência de janela quando a regra não modela nenhum limite (ambos os lados vazios) e o fato não foi informado", () => {
    const resultado = avaliarRegra(makeRegra({ dataAdmApos: null, dataAdmAte: null }), makeFatos());
    expect(resultado.fatosPendentes.some((f) => /admissão/.test(f))).toBe(false);
  });
});

describe("limite sentinela não é limite (RFC 0011)", () => {
  // A janela de admissão real das 25 regras que o levantamento contou:
  // `01/01/1950` a `31/12/2099`, os dois lados convencionais.
  const janelaToda = { dataAdmApos: data(1950, 1, 1), dataAdmAte: data(2099, 12, 31) };

  it("Regressão: janela inteiramente sentinela NUNCA credita critério satisfeito", () => {
    const resultado = avaliarRegra(makeRegra(janelaToda), makeFatos({ dataAdmissao: data(2010, 1, 1) }));
    expect(resultado.valor).toBe("nao_excluida");
    expect(resultado.criteriosSatisfeitos).not.toContain("Data de admissão");
  });

  it("janela inteiramente sentinela vira pendência escrita, não silêncio", () => {
    const resultado = avaliarRegra(makeRegra(janelaToda), makeFatos({ dataAdmissao: data(2010, 1, 1) }));
    expect(resultado.fatosPendentes.some((f) => /não foi avaliada.*sentinela/.test(f))).toBe(true);
  });

  it("não pede ao requerente uma data que não pode mudar o resultado", () => {
    const semData = avaliarRegra(makeRegra(janelaToda), makeFatos());
    expect(semData.fatosPendentes.some((f) => /admissão do requerente não informada/.test(f))).toBe(false);
  });

  it("não exclui por sentinela, nem quando o fato cai fora dela", () => {
    // `31/12/2099` como fronteira de verdade nunca excluiria nada; `01/01/1950`
    // excluiria uma admissão anterior a 1950. Nenhuma das duas exclui.
    const antes = avaliarRegra(makeRegra(janelaToda), makeFatos({ dataAdmissao: data(1949, 6, 1) }));
    expect(antes.valor).toBe("nao_excluida");
  });

  it("o lado real de uma janela meio sentinela continua excluindo", () => {
    const regra = makeRegra({ dataAdmApos: data(1950, 1, 1), dataAdmAte: data(2003, 12, 31) });
    const resultado = avaliarRegra(regra, makeFatos({ dataAdmissao: data(2010, 1, 1) }));
    expect(resultado.valor).toBe("excluida");
  });

  it("janela meio sentinela não confirma a janela inteira — pendência dizendo qual lado", () => {
    const regra = makeRegra({ dataAdmApos: data(1950, 1, 1), dataAdmAte: data(2003, 12, 31) });
    const resultado = avaliarRegra(regra, makeFatos({ dataAdmissao: data(2000, 1, 1) }));
    expect(resultado.criteriosSatisfeitos).not.toContain("Data de admissão");
    expect(resultado.fatosPendentes.some((f) => /só de um lado: o limite inferior.*sentinela/.test(f))).toBe(true);
  });

  it("distingue as duas causas de limite não avaliável — vazio não é sentinela", () => {
    const resultado = avaliarRegra(makeRegra({ dataAdmAte: null }), makeFatos({ dataAdmissao: data(2000, 1, 1) }));
    expect(resultado.fatosPendentes.some((f) => /limite superior não está preenchido no catálogo/.test(f))).toBe(true);
    expect(resultado.fatosPendentes.some((f) => /sentinela/.test(f))).toBe(false);
  });

  it("o fato do requerente nunca é classificado como sentinela — só o limite do catálogo", () => {
    // Admissão informada exatamente em `01/01/1950` contra limites reais: é um
    // fato do requerimento, e cai antes do piso real de 1998 → exclui.
    const resultado = avaliarRegra(makeRegra(), makeFatos({ dataAdmissao: data(1950, 1, 1) }));
    expect(resultado.valor).toBe("excluida");
  });

  it("duas regras que diferem só em qual sentinela usaram são indistinguíveis para o filtro", () => {
    const comMilNovecentosECinquenta = makeRegra({ id: "regra-0001", ...janelaToda, integral: true, tipoCalculo: "Valor Médio" });
    const comMilNovecentosEDez = makeRegra({
      ...comMilNovecentosECinquenta,
      id: "regra-0002",
      dataAdmApos: data(1910, 1, 1),
      integral: false,
      tipoCalculo: "Proporcionalidade Dias",
    });
    const rastro = avaliarSolicitacao([comMilNovecentosECinquenta, comMilNovecentosEDez], makeFatos({ dataAdmissao: data(2010, 1, 1), dataDireito: data(2000, 1, 1) }));
    expect(rastro.naoExcluidas).toHaveLength(2);
    for (const candidata of rastro.naoExcluidas) {
      expect(candidata.fatosPendentes.some((f) => /Indistinguível de/.test(f))).toBe(true);
    }
  });
});

describe("comparação de datas é por calendário civil, nunca por instante/timezone", () => {
  it("um limite exato é reconhecido mesmo quando dia/mês/ano vêm de fontes distintas (regressão do bug de fuso)", () => {
    // Simula exatamente o payload embutido pela página (regra) e o valor
    // lido de <input type="date"> (fato) — ambos DataCivil puro, sem Date.
    const regra = makeRegra({ dataAdmAte: { ano: 2003, mes: 12, dia: 31 } });
    const resultado = avaliarRegra(regra, makeFatos({ dataAdmissao: { ano: 2003, mes: 12, dia: 31 } }));
    expect(resultado.fatosPendentes.some((f) => /Q1\/Q2/.test(f))).toBe(true);
  });
});

describe("avaliarSolicitacao — filtro conservador", () => {
  it("nenhuma regra restante quando todas são excluídas", () => {
    const regras = [makeRegra({ id: "regra-0001" }), makeRegra({ id: "regra-0002" })];
    const rastro = avaliarSolicitacao(regras, makeFatos({ tipoDeBeneficio: "PENSÃO POR MORTE" }));
    expect(rastro.naoExcluidas).toHaveLength(0);
    expect(rastro.excluidas).toHaveLength(2);
  });

  it("mantém como não excluídas as regras que nenhum critério conhecido descarta", () => {
    const regras = [makeRegra({ id: "regra-0001", sexo: "MASCULINO" }), makeRegra({ id: "regra-0002", sexo: "FEMININO" })];
    const rastro = avaliarSolicitacao(regras, makeFatos({ sexo: "MASCULINO" }));
    expect(rastro.naoExcluidas.map((c) => c.regraId)).toEqual(["regra-0001"]);
    expect(rastro.excluidas.map((c) => c.regraId)).toEqual(["regra-0002"]);
  });

  it("regras simulavel=N e inativas ficam em foraDoEscopo, nunca somem", () => {
    const regras = [
      makeRegra({ id: "regra-0001", simulavel: false }),
      makeRegra({ id: "regra-0002", statusRegra: "inativa" }),
      makeRegra({ id: "regra-0003" }),
    ];
    const rastro = avaliarSolicitacao(regras, makeFatos());
    expect(rastro.foraDoEscopo.map((r) => r.id)).toEqual(["regra-0001", "regra-0002"]);
    expect(rastro.naoExcluidas.map((c) => c.regraId)).toEqual(["regra-0003"]);
  });

  it("Regressão (achado #2 da 1ª rodada de review): regras com os mesmos critérios conhecidos mas resultado candidato diferente (par 0006/0007) recebem pendência explícita de indistinguibilidade, nunca uma resposta silenciosamente múltipla — e sem apontar uma causa específica (achado #1 da 2ª rodada)", () => {
    const regra0006 = makeRegra({
      id: "regra-0006",
      sexo: "AMBOS",
      aposEspecial: false,
      dataAdmApos: data(1950, 1, 1),
      dataAdmAte: data(2099, 12, 31),
      dataDireitoApos: data(2003, 12, 31),
      dataDireitoAte: data(2099, 12, 31),
      integral: true,
      tipoCalculo: "Valor Médio",
      paridade: false,
    });
    const regra0007 = makeRegra({
      ...regra0006,
      id: "regra-0007",
      integral: false,
      tipoCalculo: "Proporcionalidade Dias",
    });
    const fatos = makeFatos({ aposEspecial: false, dataAdmissao: data(2010, 1, 1), dataDireito: data(2020, 1, 1) });

    const rastro = avaliarSolicitacao([regra0006, regra0007], fatos);

    expect(rastro.naoExcluidas.map((c) => c.regraId)).toEqual(["regra-0006", "regra-0007"]);
    for (const candidata of rastro.naoExcluidas) {
      expect(candidata.fatosPendentes.some((f) => /Indistinguível de/.test(f))).toBe(true);
      // A pendência não pode citar uma causa específica (nem "Q6", nem
      // "causa da incapacidade") — o filtro não tem como saber qual campo,
      // texto de fundamentação ou requisito manual é o discriminante real.
      expect(candidata.fatosPendentes.some((f) => /Q6|causa da incapacidade/i.test(f))).toBe(false);
    }
  });

  it("não sinaliza divergência entre regras indistinguíveis quando elas diferem em algum critério conhecido (não é o caso do par 0006/0007)", () => {
    const regraA = makeRegra({ id: "regra-0001", integral: true, tipoCalculo: "Valor Médio" });
    const regraB = makeRegra({ id: "regra-0002", sexo: "MASCULINO", integral: false, tipoCalculo: "Proporcionalidade Dias" });
    const rastro = avaliarSolicitacao([regraA, regraB], makeFatos({ sexo: "MASCULINO" }));
    const candidataA = rastro.naoExcluidas.find((c) => c.regraId === "regra-0001");
    expect(candidataA?.fatosPendentes.some((f) => /Indistinguível de/.test(f))).toBe(false);
  });
});

describe("regrasSimuladorFromJSON — round-trip com o payload embutido na página", () => {
  it("reconstrói datas civis e booleanos depois de um JSON.stringify/JSON.parse", () => {
    const original = makeRegra({ dataAdmApos: data(2000, 6, 15) });
    const serializado: unknown = JSON.parse(JSON.stringify([original]));
    const [reidratada] = regrasSimuladorFromJSON(serializado as unknown[]);

    expect(reidratada.id).toBe(original.id);
    expect(reidratada.dataAdmApos).toEqual(original.dataAdmApos);
    expect(reidratada.aposEspecial).toBe(original.aposEspecial);
    expect(reidratada.simulavel).toBe(original.simulavel);
  });

  it("produz o mesmo resultado de avaliação antes e depois do round-trip", () => {
    const regra = makeRegra();
    const fatos = makeFatos({ dataAdmissao: data(2000, 1, 1) });
    const [reidratada] = regrasSimuladorFromJSON(JSON.parse(JSON.stringify([regra])) as unknown[]);

    expect(avaliarRegra(reidratada, fatos)).toEqual(avaliarRegra(regra, fatos));
  });
});
