import { describe, expect, it } from "vitest";
import { atosDeValidacao, precedentes } from "./anotacoes";

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
