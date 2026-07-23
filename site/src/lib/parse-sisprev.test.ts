import { describe, expect, it } from "vitest";
import { parseDataSisprev, parseIsoDateInput, parseSN } from "./parse-sisprev";

describe("parseDataSisprev", () => {
  it("parses a DD/MM/AAAA HH:MM value", () => {
    const parsed = parseDataSisprev("15/12/1998 00:00");
    expect(parsed).not.toBeNull();
    expect(parsed?.getFullYear()).toBe(1998);
    expect(parsed?.getMonth()).toBe(11);
    expect(parsed?.getDate()).toBe(15);
  });

  it("parses a bare DD/MM/AAAA value", () => {
    const parsed = parseDataSisprev("01/01/1910");
    expect(parsed?.getFullYear()).toBe(1910);
  });

  it("returns null for an empty string (sentinela não interpretada)", () => {
    expect(parseDataSisprev("")).toBeNull();
    expect(parseDataSisprev("   ")).toBeNull();
  });

  it("returns null for an unrecognized shape", () => {
    expect(parseDataSisprev("not a date")).toBeNull();
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
    const parsed = parseIsoDateInput("2010-06-01");
    expect(parsed?.getFullYear()).toBe(2010);
    expect(parsed?.getMonth()).toBe(5);
    expect(parsed?.getDate()).toBe(1);
  });

  it("returns null for an empty value", () => {
    expect(parseIsoDateInput("")).toBeNull();
  });
});
