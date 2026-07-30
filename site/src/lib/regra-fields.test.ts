import { describe, expect, it } from "vitest";
import { NOTA_DE_SENTINELA, REGRA_FIELD_GROUPS, campoFormatado } from "./regra-fields";

const CAMPOS_DE_DATA = ["data_adm_ate", "data_adm_apos", "data_direito_ate", "data_direito_apos"];

describe("campoFormatado — a nota de sentinela (RFC 0011, fase 2)", () => {
  it("marca o limite sentinela sem interpretá-lo", () => {
    const campo = campoFormatado({ data_adm_ate: "31/12/2099 00:00" }, { key: "data_adm_ate", label: "Admissão até", formato: "data" });
    // O valor exibido continua sendo a data que está escrita (P5): a nota
    // acompanha, nunca substitui.
    expect(campo.texto).toBe("31/12/2099");
    expect(campo.nota).toBe(NOTA_DE_SENTINELA);
  });

  it("a nota nunca diz o que a sentinela significa", () => {
    expect(NOTA_DE_SENTINELA).not.toMatch(/sem limite|ilimitad|aberto|infinit/i);
  });

  it("não marca limite real", () => {
    const campo = campoFormatado({ data_adm_ate: "31/12/2003 00:00" }, { key: "data_adm_ate", label: "Admissão até", formato: "data" });
    expect(campo.texto).toBe("31/12/2003");
    expect(campo.nota).toBeNull();
  });

  it("não marca `01/01/1969`, que está fora do conjunto", () => {
    const campo = campoFormatado({ data_direito_apos: "01/01/1969 00:00" }, { key: "data_direito_apos", label: "Direito após", formato: "data" });
    expect(campo.nota).toBeNull();
  });

  it("não marca um campo que não é data, mesmo se o texto casasse", () => {
    const campo = campoFormatado({ nome: "31/12/2099 00:00" }, { key: "nome", label: "Nome" });
    expect(campo.nota).toBeNull();
  });

  it("todo campo `formato: \"data\"` é uma das quatro colunas de limite temporal", () => {
    // É esta asserção que sustenta marcar por formato em vez de manter uma
    // segunda lista de chaves. Se uma data que não é limite ganhar
    // `formato: "data"`, ela passaria a receber a nota — e este teste cai antes.
    const comFormatoData = REGRA_FIELD_GROUPS.flatMap((grupo) => grupo.fields)
      .filter((campo) => campo.formato === "data")
      .map((campo) => campo.key);
    expect(comFormatoData.toSorted()).toEqual([...CAMPOS_DE_DATA].toSorted());
  });
});
