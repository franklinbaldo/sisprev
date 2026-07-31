import { describe, expect, it } from "vitest";
import { avaliarSolicitacao, type FatosRequerimento, type RegraSimulador } from "./simulador";
import { parseDataSisprev } from "./parse-sisprev";

type Scalar = boolean | number | string | null;
type Tabela = Record<string, Scalar>;

import feature from "./auditoria.feature?raw";

function scalar(raw: string): Scalar {
  const value = raw.trim();
  if (value === "null") return null;
  if (value === "true") return true;
  if (value === "false") return false;
  if (/^-?\d+$/.test(value)) return Number(value);
  return value;
}

function tabela(lines: string[], start: number): { values: Tabela; next: number } {
  const values: Tabela = {};
  let index = start;
  while (index < lines.length && lines[index].trim().startsWith("|")) {
    const cells = lines[index].trim().split("|").slice(1, -1).map((cell) => cell.trim());
    if (cells.length === 2) values[cells[0]] = scalar(cells[1]);
    index += 1;
  }
  return { values, next: index };
}

function cenarios(text: string): Array<{ nome: string; fatos: Tabela; esperados: Tabela }> {
  const lines = text.split(/\r?\n/);
  const result: Array<{ nome: string; fatos: Tabela; esperados: Tabela }> = [];
  for (let index = 0; index < lines.length; index += 1) {
    const match = lines[index].match(/^  Scenario: (.+)$/);
    if (!match) continue;
    const scenario = { nome: match[1], fatos: {}, esperados: {} } as {
      nome: string;
      fatos: Tabela;
      esperados: Tabela;
    };
    while (index + 1 < lines.length && !lines[index + 1].startsWith("  Scenario:")) {
      index += 1;
      if (lines[index].includes("fatos")) {
        const parsed = tabela(lines, index + 1);
        scenario.fatos = parsed.values;
        index = parsed.next - 1;
      } else if (lines[index].includes("campos devem ser observados")) {
        const parsed = tabela(lines, index + 1);
        scenario.esperados = parsed.values;
        index = parsed.next - 1;
      }
    }
    result.push(scenario);
  }
  return result;
}

function data(value: Scalar) {
  return typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) ? parseDataSisprev(value.split("-").reverse().join("/")) : null;
}

function regra(id: string, tipoDeBeneficio: string, aposEspecial: boolean, nome: string): RegraSimulador {
  return {
    id,
    nome,
    tipoDeBeneficio,
    sexo: "AMBOS",
    aposEspecial,
    simulavel: true,
    statusRegra: null,
    dataAdmApos: null,
    dataAdmAte: null,
    dataDireitoApos: null,
    dataDireitoAte: null,
    integral: null,
    tipoCalculo: "",
    paridade: null,
  };
}

const catalogo: RegraSimulador[] = [
  regra("regra-0068", "APOSENTADORIA VOLUNTÃƒÂRIA POR TEMPO DE CONTRIBUIÃƒâ€¡ÃƒÆ’O", true, "Faixa 66/15"),
  regra("regra-0069", "APOSENTADORIA VOLUNTÃƒÂRIA POR TEMPO DE CONTRIBUIÃƒâ€¡ÃƒÆ’O", true, "Faixa 76/20"),
  regra("regra-0070", "APOSENTADORIA VOLUNTÃƒÂRIA POR TEMPO DE CONTRIBUIÃƒâ€¡ÃƒÆ’O", true, "Faixa 86/25"),
  regra("regra-0001", "PENSÃƒÆ’O POR MORTE", false, "PensÃƒÂ£o"),
];

const tipos: Record<string, string> = { voluntaria: catalogo[0].tipoDeBeneficio, pensao: catalogo[3].tipoDeBeneficio };

function fatosDoCenario(fatos: Tabela): FatosRequerimento {
  return {
    tipoDeBeneficio: tipos[String(fatos.tipoDeBeneficio)] ?? String(fatos.tipoDeBeneficio ?? ""),
    sexo: fatos.sexo === "null" || fatos.sexo === null ? null : (String(fatos.sexo) as "MASCULINO" | "FEMININO"),
    aposEspecial: typeof fatos.aposEspecial === "boolean" ? fatos.aposEspecial : null,
    dataAdmissao: data(fatos.dataAdmissao),
    dataDireito: data(fatos.dataDireito),
  };
}

describe("auditoria BDD do seletor legado", () => {
  for (const scenario of cenarios(feature)) {
    it(scenario.nome, () => {
      const fatos = fatosDoCenario(scenario.fatos);
      const rastro = avaliarSolicitacao(catalogo, fatos);
      const observados = rastro.naoExcluidas.map((item) => item.regraId);
      const includes = String(scenario.esperados["legado.inclui"] ?? "").split(",").filter(Boolean);
      const excludes = String(scenario.esperados["legado.exclui"] ?? "").split(",").filter(Boolean);
      expect(observados.length).toBe(Number(scenario.esperados["legado.quantidade_observada"]));
      expect(observados).toEqual(expect.arrayContaining(includes));
      expect(rastro.excluidas.map((item) => item.regraId)).toEqual(expect.arrayContaining(excludes));
      expect(scenario.esperados["expectativa.elegivel"]).toBe(scenario.fatos["faixa_exposicao"] !== "nenhuma");
      expect(scenario.esperados["expectativa.faixa_exposicao"]).toBe(scenario.fatos["faixa_exposicao"]);
      const divergente = Number(scenario.esperados["legado.quantidade_esperada"]) !== observados.length;
      expect(scenario.esperados["legado.divergente"]).toBe(divergente);
    });
  }
});
