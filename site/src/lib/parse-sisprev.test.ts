import { describe, expect, it } from "vitest";
import { compararDatasCivis, parseDataSisprev, parseIsoDateInput, parseSN } from "./parse-sisprev";

describe("parseDataSisprev", () => {
  it("parses a DD/MM/AAAA HH:MM value into a calendar date (hour ignored)", () => {
    expect(parseDataSisprev("15/12/1998 00:00")).toEqual({ ano: 1998, mes: 12, dia: 15 });
  });

  it("parses a bare DD/MM/AAAA value", () => {
    expect(parseDataSisprev("01/01/1910")).toEqual({ ano: 1910, mes: 1, dia: 1 });
  });

  it("returns null for an empty string (sentinela não interpretada)", () => {
    expect(parseDataSisprev("")).toBeNull();
    expect(parseDataSisprev("   ")).toBeNull();
  });

  it("returns null for an unrecognized shape", () => {
    expect(parseDataSisprev("not a date")).toBeNull();
  });

  it("rejeita datas de calendário impossíveis em vez de normalizar silenciosamente", () => {
    expect(parseDataSisprev("31/02/2024")).toBeNull(); // fevereiro não tem dia 31
    expect(parseDataSisprev("31/04/2024")).toBeNull(); // abril tem 30 dias
    expect(parseDataSisprev("00/01/2024")).toBeNull();
    expect(parseDataSisprev("15/13/2024")).toBeNull(); // mês 13
    expect(parseDataSisprev("15/00/2024")).toBeNull();
  });

  it("aceita 29 de fevereiro em ano bissexto e rejeita em ano comum", () => {
    expect(parseDataSisprev("29/02/2024")).toEqual({ ano: 2024, mes: 2, dia: 29 });
    expect(parseDataSisprev("29/02/2023")).toBeNull();
  });
});

describe("parseSN", () => {
  it("parses S and N", () => {
    expect(parseSN("S")).toBe(true);
    expect(parseSN("N")).toBe(false);
  });

  it("is case-insensitive and trims whitespace", () => {
    expect(parseSN(" s ")).toBe(true);
    expect(parseSN("n")).toBe(false);
  });

  it("returns null for empty or unrecognized values", () => {
    expect(parseSN("")).toBeNull();
    expect(parseSN("TALVEZ")).toBeNull();
  });
});

describe("parseIsoDateInput", () => {
  it("parses a YYYY-MM-DD value from a date input", () => {
    expect(parseIsoDateInput("2010-06-01")).toEqual({ ano: 2010, mes: 6, dia: 1 });
  });

  it("returns null for an empty value", () => {
    expect(parseIsoDateInput("")).toBeNull();
  });

  it("rejeita datas de calendário impossíveis", () => {
    expect(parseIsoDateInput("2024-02-31")).toBeNull();
  });
});

describe("compararDatasCivis", () => {
  it("compara por ano, depois mês, depois dia — nunca por instante/timezone", () => {
    expect(compararDatasCivis({ ano: 2003, mes: 12, dia: 31 }, { ano: 2003, mes: 12, dia: 31 })).toBe(0);
    expect(compararDatasCivis({ ano: 2003, mes: 12, dia: 30 }, { ano: 2003, mes: 12, dia: 31 })).toBeLessThan(0);
    expect(compararDatasCivis({ ano: 2004, mes: 1, dia: 1 }, { ano: 2003, mes: 12, dia: 31 })).toBeGreaterThan(0);
    expect(compararDatasCivis({ ano: 2003, mes: 1, dia: 1 }, { ano: 2003, mes: 2, dia: 1 })).toBeLessThan(0);
  });
});
