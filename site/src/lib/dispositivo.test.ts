import { describe, expect, it } from "vitest";
import {
  chaveDeOrdem,
  compararEnderecos,
  romanoParaInt,
  rotuloDaRedacao,
  rotuloDoEndereco,
  type Componente,
} from "./dispositivo";

const art = (valor: string, sufixo?: string): Componente => ({ tipo: "artigo", valor, sufixo });
const par = (valor: string, sufixo?: string): Componente => ({ tipo: "paragrafo", valor, sufixo });
const inc = (valor: string): Componente => ({ tipo: "inciso", valor });
const al = (valor: string): Componente => ({ tipo: "alinea", valor });
const CAPUT: Componente = { tipo: "caput" };
const PAR_UNICO: Componente = { tipo: "paragrafo_unico" };

describe("rotuloDoEndereco", () => {
  it("monta a citação canônica do P4", () => {
    expect(rotuloDoEndereco([art("40"), par("1"), inc("I")])).toBe("art. 40, § 1º, inciso I");
    expect(rotuloDoEndereco([art("1"), inc("II"), al("a")])).toBe("art. 1º, inciso II, alínea a");
    expect(rotuloDoEndereco([art("40"), CAPUT])).toBe("art. 40, caput");
    expect(rotuloDoEndereco([art("3"), PAR_UNICO])).toBe("art. 3º, parágrafo único");
  });

  it("usa a convenção ordinal da redação legislativa", () => {
    expect(rotuloDoEndereco([art("9")])).toBe("art. 9º");
    expect(rotuloDoEndereco([art("10")])).toBe("art. 10");
    expect(rotuloDoEndereco([art("40"), par("14")])).toBe("art. 40, § 14");
    expect(rotuloDoEndereco([art("6", "A")])).toBe("art. 6º-A");
    expect(rotuloDoEndereco([art("40"), par("4", "B")])).toBe("art. 40, § 4º-B");
  });
});

describe("ordem", () => {
  const ordenado = (enderecos: Componente[][]): string[] =>
    [...enderecos].sort(compararEnderecos).map((c) => rotuloDoEndereco(c));

  it("ordena parágrafos numericamente, não como string", () => {
    expect(ordenado([[art("20"), par("14")], [art("20"), par("2")], [art("20"), par("9")]])).toEqual([
      "art. 20, § 2º",
      "art. 20, § 9º",
      "art. 20, § 14",
    ]);
  });

  it("ordena artigos numericamente", () => {
    expect(ordenado([[art("10")], [art("9")], [art("62")]])).toEqual(["art. 9º", "art. 10", "art. 62"]);
  });

  it("põe os incisos do caput antes dos parágrafos", () => {
    expect(
      ordenado([
        [art("40"), par("1"), inc("I")],
        [art("40"), inc("II")],
        [art("40"), CAPUT],
        [art("40"), par("1"), CAPUT],
        [art("40"), inc("I")],
      ]),
    ).toEqual([
      "art. 40, caput",
      "art. 40, inciso I",
      "art. 40, inciso II",
      "art. 40, § 1º, caput",
      "art. 40, § 1º, inciso I",
    ]);
  });

  it("ordena incisos pelo valor romano", () => {
    expect(ordenado([[art("1"), inc("X")], [art("1"), inc("IX")], [art("1"), inc("IV")]])).toEqual([
      "art. 1º, inciso IV",
      "art. 1º, inciso IX",
      "art. 1º, inciso X",
    ]);
  });

  it("põe o artigo sufixado depois da sua base", () => {
    expect(ordenado([[art("7")], [art("6", "A")], [art("6")]])).toEqual([
      "art. 6º",
      "art. 6º-A",
      "art. 7º",
    ]);
  });

  it("é ordem total: endereços distintos nunca empatam", () => {
    expect(chaveDeOrdem([art("20")])).not.toEqual(chaveDeOrdem([art("20"), CAPUT]));
    expect(compararEnderecos([art("20")], [art("20"), CAPUT])).not.toBe(0);
  });

  it("é estável para o mesmo endereço", () => {
    expect(compararEnderecos([art("40"), par("1")], [art("40"), par("1")])).toBe(0);
  });
});

describe("romanoParaInt", () => {
  it.each([
    ["I", 1],
    ["IV", 4],
    ["IX", 9],
    ["XIV", 14],
    ["XL", 40],
    ["C", 100],
  ])("decodifica %s", (romano, esperado) => {
    expect(romanoParaInt(romano)).toBe(esperado);
  });
});

describe("rotuloDaRedacao", () => {
  it("nomeia a redação original", () => {
    expect(rotuloDaRedacao("original")).toBe("redação original");
  });

  it("prefere o apelido da norma alteradora", () => {
    expect(rotuloDaRedacao("ec-41-2003", "EC 41/2003")).toBe("redação dada por EC 41/2003");
  });

  it("cai na chave quando a norma alteradora não tem apelido", () => {
    expect(rotuloDaRedacao("ec-41-2003")).toBe("redação dada por ec-41-2003");
  });
});
