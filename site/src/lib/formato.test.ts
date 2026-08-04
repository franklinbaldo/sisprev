import { describe, expect, it } from "vitest";
import { formatarValor } from "./formato";

describe("formatarValor", () => {
  it("deixa texto comum verbatim, sem bruto duplicado", () => {
    expect(formatarValor("Valor Médio")).toEqual({ texto: "Valor Médio", bruto: null });
    expect(formatarValor("AMBOS", "texto")).toEqual({ texto: "AMBOS", bruto: null });
  });

  it("lê S/N como Sim/Não preservando o valor gravado", () => {
    expect(formatarValor("S", "sn")).toEqual({ texto: "Sim", bruto: "S" });
    expect(formatarValor("N", "sn")).toEqual({ texto: "Não", bruto: "N" });
  });

  it("lê TRUE/FALSE como Sim/Não preservando o valor gravado", () => {
    expect(formatarValor("TRUE", "booleano")).toEqual({ texto: "Sim", bruto: "TRUE" });
    expect(formatarValor("FALSE", "booleano")).toEqual({ texto: "Não", bruto: "FALSE" });
  });

  it("tira a hora constante da data, mantendo o dia/mês/ano exatos e sem repetir o bruto", () => {
    expect(formatarValor("31/12/2099 00:00", "data")).toEqual({ texto: "31/12/2099", bruto: null });
  });

  it("não muda nada quando a data já vem sem hora", () => {
    expect(formatarValor("13/11/2019", "data")).toEqual({ texto: "13/11/2019", bruto: null });
  });

  it("não substitui a sentinela: 31/12/2099 sai como a data gravada, e quem explica é a nota", () => {
    expect(formatarValor("31/12/2099 00:00", "data").texto).toBe("31/12/2099");
  });

  it("devolve valor vazio como vazio, sem inventar placeholder", () => {
    expect(formatarValor("", "data")).toEqual({ texto: "", bruto: null });
    expect(formatarValor("", "sn")).toEqual({ texto: "", bruto: null });
  });

  it("sai verbatim quando o valor não casa com o formato declarado", () => {
    expect(formatarValor("TALVEZ", "sn")).toEqual({ texto: "TALVEZ", bruto: null });
    expect(formatarValor("SIM", "booleano")).toEqual({ texto: "SIM", bruto: null });
    expect(formatarValor("31/02/2020", "data")).toEqual({ texto: "31/02/2020", bruto: null });
    expect(formatarValor("a definir", "data")).toEqual({ texto: "a definir", bruto: null });
  });
});
