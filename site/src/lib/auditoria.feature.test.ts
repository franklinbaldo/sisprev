import { describe, expect, it } from "vitest";
import { generateMessages } from "@cucumber/gherkin";
import { SourceMediaType, type GherkinDocument, type TableRow } from "@cucumber/messages";
import { load } from "js-yaml";
import feature from "./auditoria.feature?raw";
import { avaliarSolicitacao, toRegraSimulador, type FatosRequerimento, type RegraSimulador } from "./simulador";
import { parseDataSisprev } from "./parse-sisprev";

type Scalar = boolean | number | string | null;
type Tabela = Record<string, Scalar>;
type Cenario = { nome: string; fatos: Tabela; esperados: Tabela };

function scalar(raw: string): Scalar {
  const value = raw.trim();
  if (value === "null") return null;
  if (value === "true") return true;
  if (value === "false") return false;
  if (/^-?\d+$/.test(value)) return Number(value);
  return value;
}
function tabela(rows: readonly TableRow[]): Tabela {
  const result: Tabela = {};
  for (const row of rows) {
    const cells = row.cells.map((cell) => cell.value.trim());
    if (cells.length !== 2) throw new Error("As tabelas BDD devem ter exatamente duas colunas");
    result[cells[0]] = scalar(cells[1]);
  }
  return result;
}
function cenarios(text: string): Cenario[] {
  const envelopes = generateMessages(text, "auditoria.feature", SourceMediaType.TEXT_X_CUCUMBER_GHERKIN_PLAIN, { includeGherkinDocument: true, includePickles: false, newId: () => crypto.randomUUID() });
  const document = envelopes.find((envelope) => envelope.gherkinDocument)?.gherkinDocument as GherkinDocument | undefined;
  if (!document?.feature) throw new Error("O documento Gherkin não contém uma Feature");
  const result: Cenario[] = [];
  for (const child of document.feature.children) {
    if (!child.scenario) continue;
    let fatos: Tabela | undefined;
    let esperados: Tabela | undefined;
    for (const step of child.scenario.steps) {
      const table = step.dataTable?.rows;
      if (step.keyword.trim() === "Given" && step.text === "the legacy catalog") continue;
      if (step.keyword.trim() === "And" && step.text === "a request with the following facts:") fatos = tabela(table ?? []);
      else if (step.keyword.trim() === "When" && step.text === "the legacy filter is executed") continue;
      else if (step.keyword.trim() === "Then" && step.text === "the following fields are observed:") esperados = tabela(table ?? []);
      else throw new Error(`Step Gherkin não registrado: ${step.keyword}${step.text}`);
    }
    if (!fatos || !esperados) throw new Error(`Cenário incompleto: ${child.scenario.name}`);
    result.push({ nome: child.scenario.name, fatos, esperados });
  }
  return result;
}

const fontes = import.meta.glob("../../../okf/regras-sisprev/regras/regra-*.md", { eager: true, query: "?raw", import: "default" }) as Record<string, string>;
const catalogo: RegraSimulador[] = Object.values(fontes).map((raw) => {
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) throw new Error("Regra sem frontmatter YAML");
  return toRegraSimulador(load(match[1]) as Record<string, unknown>);
});
const tipos: Record<string, string> = {
  voluntaria: catalogo.find((regra) => regra.id === "regra-0068")?.tipoDeBeneficio ?? "",
  pensao: catalogo.find((regra) => regra.id === "regra-0003")?.tipoDeBeneficio ?? "",
};
function data(value: Scalar) {
  return typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) ? parseDataSisprev(value.split("-").reverse().join("/")) : null;
}
function fatosDoCenario(fatos: Tabela): FatosRequerimento {
  return { tipoDeBeneficio: tipos[String(fatos.tipoDeBeneficio)] ?? String(fatos.tipoDeBeneficio ?? ""), sexo: fatos.sexo === null ? null : (String(fatos.sexo) as "MASCULINO" | "FEMININO"), aposEspecial: typeof fatos.aposEspecial === "boolean" ? fatos.aposEspecial : null, dataAdmissao: data(fatos.dataAdmissao), dataDireito: data(fatos.dataDireito) };
}
describe("auditoria BDD do seletor legado", () => {
  for (const scenario of cenarios(feature)) {
    it(scenario.nome, () => {
      const rastro = avaliarSolicitacao(catalogo, fatosDoCenario(scenario.fatos));
      const observados = rastro.naoExcluidas.map((item) => item.regraId);
      const includes = String(scenario.esperados["legado.inclui"] ?? "").split(",").filter((value) => value && value !== "nenhum");
      const excludes = String(scenario.esperados["legado.exclui"] ?? "").split(",").filter((value) => value && value !== "nenhum");
      expect(observados.length).toBe(Number(scenario.esperados["legado.quantidade_observada"]));
      expect(observados).toEqual(expect.arrayContaining(includes));
      expect(rastro.excluidas.map((item) => item.regraId)).toEqual(expect.arrayContaining(excludes));
      const foraDoEscopo = String(scenario.esperados["legado.fora_escopo"] ?? "").split(",").filter((value) => value && value !== "nenhum");
      expect(rastro.foraDoEscopo.map((item) => item.id)).toEqual(expect.arrayContaining(foraDoEscopo));
      const quantidadeEsperada = Number(scenario.esperados["legado.quantidade_esperada"]);
      expect(scenario.esperados["expectativa.elegivel"]).toBe(quantidadeEsperada > 0);
      const divergente = quantidadeEsperada !== observados.length;
      expect(scenario.esperados["legado.divergente"]).toBe(divergente);
    });
  }
});
