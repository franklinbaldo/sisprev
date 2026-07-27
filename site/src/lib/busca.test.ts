import { describe, expect, it } from "vitest";
import { rotuloDeContagem, urlDoResultado } from "./busca";

describe("urlDoResultado", () => {
  it("põe a base na frente da URL que o índice grava sem ela", () => {
    expect(urlDoResultado("/relatorios/estado-da-auditoria/", "/sisprev")).toBe(
      "/sisprev/relatorios/estado-da-auditoria/",
    );
  });

  it("aceita base com barra final sem duplicar a barra", () => {
    expect(urlDoResultado("/regras/regra-0006/", "/sisprev/")).toBe("/sisprev/regras/regra-0006/");
  });

  it("é idempotente: não prefixa de novo uma URL que já traz a base", () => {
    expect(urlDoResultado("/sisprev/regras/regra-0006/", "/sisprev")).toBe("/sisprev/regras/regra-0006/");
  });

  it("não confunde um caminho que só começa com o mesmo texto", () => {
    expect(urlDoResultado("/sisprevidencia/x/", "/sisprev")).toBe("/sisprev/sisprevidencia/x/");
  });

  it("devolve a URL intacta quando o site é servido da raiz", () => {
    expect(urlDoResultado("/regras/regra-0006/", "")).toBe("/regras/regra-0006/");
  });
});

describe("rotuloDeContagem", () => {
  it("pede um termo enquanto a busca está vazia", () => {
    expect(rotuloDeContagem(0, "   ")).toBe("Digite um termo para buscar.");
  });

  it("conta em páginas, não em regras — a busca é por página", () => {
    expect(rotuloDeContagem(0, "zzz")).toBe("Nenhuma página encontrada para “zzz”.");
    expect(rotuloDeContagem(1, "pensão")).toBe("1 página encontrada para “pensão”.");
    expect(rotuloDeContagem(12, "invalidez")).toBe("12 páginas encontradas para “invalidez”.");
  });
});
