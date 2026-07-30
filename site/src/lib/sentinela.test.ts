import { describe, expect, it } from "vitest";
import { SENTINELAS, sentinelaDaData, sentinelaDe } from "./sentinela";

describe("sentinelaDe — o conjunto declarado (RFC 0011)", () => {
  it("classifica a forma gravada e a forma sem hora", () => {
    expect(sentinelaDe("31/12/2099 00:00")).toBe("31/12/2099 00:00");
    expect(sentinelaDe("31/12/2099")).toBe("31/12/2099 00:00");
    expect(sentinelaDe("01/01/1910 00:00")).toBe("01/01/1910 00:00");
  });

  it("os quatro membros são exatamente os do lado Python (autoridade)", () => {
    expect([...SENTINELAS]).toEqual(["01/01/1900 00:00", "01/01/1910 00:00", "01/01/1950 00:00", "31/12/2099 00:00"]);
    for (const valor of SENTINELAS) expect(sentinelaDe(valor)).toBe(valor);
  });

  it("devolve null para o que não é sentinela, incluindo o que parece", () => {
    expect(sentinelaDe("31/12/2003 00:00")).toBeNull();
    expect(sentinelaDe("15/12/1998 00:00")).toBeNull();
    expect(sentinelaDe("")).toBeNull();
    expect(sentinelaDe("banana")).toBeNull();
  });

  it("`01/01/1969` fica fora — suspeita registrada não é membro", () => {
    // `regra-0003`, `data_direito_apos`: item 9 da fila de conferência do
    // levantamento. Entra por edição autorada, com achado, nunca por
    // parecer-se com preenchimento (RFC 0008).
    expect(sentinelaDe("01/01/1969 00:00")).toBeNull();
  });

  it("classifica data civil já parseada, que é a forma que o simulador usa", () => {
    expect(sentinelaDaData({ ano: 1950, mes: 1, dia: 1 })).toBe("01/01/1950 00:00");
    expect(sentinelaDaData({ ano: 2003, mes: 12, dia: 31 })).toBeNull();
  });
});
