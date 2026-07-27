import { describe, expect, it } from "vitest";
import {
  PARAM_BUSCA,
  estadoFiltroDeParams,
  filtroEstaVazio,
  itemCorrespondeAoFiltro,
  normalizarBusca,
  paramsDeEstadoFiltro,
  type EstadoFiltro,
  type ItemFiltravel,
} from "./filtros";

function item(overrides: Partial<ItemFiltravel> = {}): ItemFiltravel {
  return {
    busca: "regra-0006 Invalidez - Art. 40, §1º, I da CF",
    facetas: { tipo: "APOSENTADORIA POR INVALIDEZ", ciclo: "1º", status: "importada" },
    ...overrides,
  };
}

function estado(overrides: Partial<EstadoFiltro> = {}): EstadoFiltro {
  return { busca: "", facetas: { tipo: "", ciclo: "", status: "" }, ...overrides };
}

describe("normalizarBusca", () => {
  it("tira acentos e caixa", () => {
    expect(normalizarBusca("Pensão por Morte")).toBe("pensao por morte");
    expect(normalizarBusca("VOLUNTÁRIA")).toBe("voluntaria");
  });
});

describe("itemCorrespondeAoFiltro", () => {
  it("aceita tudo quando nada está preenchido", () => {
    expect(itemCorrespondeAoFiltro(item(), estado())).toBe(true);
  });

  it("acha texto acentuado a partir de busca sem acento", () => {
    const alvo = item({ busca: "regra-0003 Pensão por Morte - com redação original da CF/88" });
    expect(itemCorrespondeAoFiltro(alvo, estado({ busca: "pensao" }))).toBe(true);
  });

  it("exige todos os termos, não qualquer um", () => {
    const alvo = item({ busca: "regra-0003 Pensão por Morte - redação da EC nº 20/1998" });
    expect(itemCorrespondeAoFiltro(alvo, estado({ busca: "pensao 1998" }))).toBe(true);
    expect(itemCorrespondeAoFiltro(alvo, estado({ busca: "pensao 2003" }))).toBe(false);
  });

  it("busca também pelo id, não só pelo nome", () => {
    expect(itemCorrespondeAoFiltro(item(), estado({ busca: "regra-0006" }))).toBe(true);
  });

  it("ignora espaços extras entre termos", () => {
    expect(itemCorrespondeAoFiltro(item(), estado({ busca: "  invalidez   art  " }))).toBe(true);
  });

  it("faceta preenchida exige igualdade exata", () => {
    const filtro = estado({ facetas: { tipo: "PENSÃO POR MORTE", ciclo: "", status: "" } });
    expect(itemCorrespondeAoFiltro(item(), filtro)).toBe(false);
    expect(
      itemCorrespondeAoFiltro(item(), estado({ facetas: { tipo: "APOSENTADORIA POR INVALIDEZ", ciclo: "", status: "" } })),
    ).toBe(true);
  });

  it("combina facetas e busca em E", () => {
    const filtro = estado({ busca: "invalidez", facetas: { tipo: "", ciclo: "3º", status: "" } });
    expect(itemCorrespondeAoFiltro(item(), filtro)).toBe(false);
  });

  it("faceta que o item não declara só passa quando o filtro não a restringe", () => {
    const alvo = item({ facetas: { tipo: "PENSÃO POR MORTE" } });
    expect(itemCorrespondeAoFiltro(alvo, estado({ facetas: { severidade: "" } }))).toBe(true);
    expect(itemCorrespondeAoFiltro(alvo, estado({ facetas: { severidade: "bloqueante" } }))).toBe(false);
  });
});

describe("estadoFiltroDeParams", () => {
  it("lê busca e facetas declaradas", () => {
    const params = new URLSearchParams("q=pensao&tipo=PENS%C3%83O+POR+MORTE&ciclo=1%C2%BA");
    expect(estadoFiltroDeParams(params, ["tipo", "ciclo"])).toEqual({
      busca: "pensao",
      facetas: { tipo: "PENSÃO POR MORTE", ciclo: "1º" },
    });
  });

  it("ignora parâmetro não declarado e preenche faceta ausente com vazio", () => {
    const params = new URLSearchParams("desconhecido=x");
    expect(estadoFiltroDeParams(params, ["tipo"])).toEqual({ busca: "", facetas: { tipo: "" } });
  });
});

describe("paramsDeEstadoFiltro", () => {
  it("omite tudo que está vazio", () => {
    expect(paramsDeEstadoFiltro(estado()).toString()).toBe("");
  });

  it("serializa só o que está preenchido", () => {
    const params = paramsDeEstadoFiltro(estado({ busca: " pensao ", facetas: { tipo: "", ciclo: "2º" } }));
    expect(params.get(PARAM_BUSCA)).toBe("pensao");
    expect(params.get("ciclo")).toBe("2º");
    expect(params.has("tipo")).toBe(false);
  });

  it("faz ida e volta com estadoFiltroDeParams", () => {
    const original = estado({ busca: "invalidez", facetas: { tipo: "APOSENTADORIA POR INVALIDEZ", ciclo: "" } });
    const voltou = estadoFiltroDeParams(paramsDeEstadoFiltro(original), ["tipo", "ciclo"]);
    expect(voltou).toEqual(original);
  });
});

describe("filtroEstaVazio", () => {
  it("distingue nenhum critério de algum critério", () => {
    expect(filtroEstaVazio(estado())).toBe(true);
    expect(filtroEstaVazio(estado({ busca: "   " }))).toBe(true);
    expect(filtroEstaVazio(estado({ busca: "x" }))).toBe(false);
    expect(filtroEstaVazio(estado({ facetas: { tipo: "PENSÃO POR MORTE" } }))).toBe(false);
  });
});
