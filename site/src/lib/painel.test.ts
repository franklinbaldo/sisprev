import { describe, expect, it } from "vitest";
import {
  resumirAchados,
  resumirRegras,
  type EstadoAchadoContavel,
  type EstadoRegraContavel,
} from "./painel";

function regra(overrides: Partial<EstadoRegraContavel> = {}): EstadoRegraContavel {
  return {
    status_auditoria: "importada",
    validado_pge: false,
    validado_presidencia: false,
    ciclo_de_validacao: "1º",
    ...overrides,
  };
}

function achado(overrides: Partial<EstadoAchadoContavel> = {}): EstadoAchadoContavel {
  return { situacao: "aberto", severidade: "informativo", ...overrides };
}

describe("resumirRegras", () => {
  it("conta por status_auditoria", () => {
    const resumo = resumirRegras([
      regra(),
      regra({ status_auditoria: "revisada" }),
      regra({ status_auditoria: "revisada" }),
      regra({ status_auditoria: "validada" }),
    ]);
    expect(resumo.total).toBe(4);
    expect(resumo.importadas).toBe(1);
    expect(resumo.revisadas).toBe(2);
    expect(resumo.validadas).toBe(1);
  });

  it("conta PGE e Presidência separadamente e a interseção", () => {
    const resumo = resumirRegras([
      regra({ validado_pge: true }),
      regra({ validado_presidencia: true }),
      regra({ validado_pge: true, validado_presidencia: true }),
      regra(),
    ]);
    expect(resumo.validadoPge).toBe(2);
    expect(resumo.validadoPresidencia).toBe(2);
    expect(resumo.validadoAmbos).toBe(1);
  });

  it("agrupa por ciclo em ordem numérica, não alfabética", () => {
    const resumo = resumirRegras([
      regra({ ciclo_de_validacao: "10º" }),
      regra({ ciclo_de_validacao: "2º" }),
      regra({ ciclo_de_validacao: "2º" }),
      regra({ ciclo_de_validacao: "1º" }),
    ]);
    expect(resumo.porCiclo).toEqual([
      { ciclo: "1º", total: 1 },
      { ciclo: "2º", total: 2 },
      { ciclo: "10º", total: 1 },
    ]);
  });

  it("ordena um rótulo de ciclo não numérico depois dos numéricos, de forma estável", () => {
    const resumo = resumirRegras([
      regra({ ciclo_de_validacao: "extraordinário" }),
      regra({ ciclo_de_validacao: "3º" }),
    ]);
    expect(resumo.porCiclo.map((c) => c.ciclo)).toEqual(["3º", "extraordinário"]);
  });

  it("resume uma lista vazia sem quebrar", () => {
    expect(resumirRegras([])).toEqual({
      total: 0,
      importadas: 0,
      revisadas: 0,
      validadas: 0,
      validadoPge: 0,
      validadoPresidencia: 0,
      validadoAmbos: 0,
      porCiclo: [],
    });
  });
});

describe("resumirAchados", () => {
  it("separa abertos por severidade e conta improcedentes à parte", () => {
    const resumo = resumirAchados([
      achado({ severidade: "bloqueante" }),
      achado({ severidade: "bloqueante" }),
      achado(),
      achado({ situacao: "improcedente", severidade: "bloqueante" }),
    ]);
    expect(resumo).toEqual({
      total: 4,
      abertos: 3,
      abertosBloqueantes: 2,
      abertosInformativos: 1,
      improcedentes: 1,
    });
  });

  it("não conta severidade de achado improcedente como aberto", () => {
    const resumo = resumirAchados([achado({ situacao: "improcedente", severidade: "bloqueante" })]);
    expect(resumo.abertosBloqueantes).toBe(0);
    expect(resumo.improcedentes).toBe(1);
  });

  it("um defeito tratado segue aberto no painel, porque quem o fecha é a disposição", () => {
    // Não há estado no achado que declare "tratado": a resposta mora em
    // `disposicao_de_achados`, na regra. O painel conta pendência, e enquanto
    // o achado não for improcedente ele é pendência.
    const resumo = resumirAchados([achado({ severidade: "bloqueante" })]);
    expect(resumo.abertos).toBe(1);
    expect(resumo.improcedentes).toBe(0);
  });
});
