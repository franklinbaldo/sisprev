import { describe, expect, it } from "vitest";
import {
  notaDeApoio,
  numeroDaRfc,
  reescreverLinkMd,
  statusDaRfc,
  tituloDoMarkdown,
} from "./documentos";

const REPO = "https://github.com/franklinbaldo/sisprev";

describe("tituloDoMarkdown", () => {
  it("lê o primeiro # do corpo", () => {
    expect(tituloDoMarkdown("# RFC 0001 — Critérios\n\ntexto")).toBe("RFC 0001 — Critérios");
  });

  it("ignora ## e ### — só o título de nível 1 nomeia o documento", () => {
    expect(tituloDoMarkdown("## Seção\n\n# Título real\n")).toBe("Título real");
  });

  it("não confunde '#' dentro de texto com um título", () => {
    expect(tituloDoMarkdown("veja #4 do relatório\n\n# Real\n")).toBe("Real");
  });

  it("devolve null quando não há título, em vez de inventar um", () => {
    expect(tituloDoMarkdown("só corpo, sem heading")).toBeNull();
  });
});

describe("notaDeApoio", () => {
  const corpo = [
    "# Relatório de Estado da Auditoria",
    "",
    "> **Nota:** Este é um relatório gerado por IA com o objetivo de apoiar",
    "> a tomada de decisão (não é um artefato oficial de auditoria).",
    "",
    "## 1. Distribuição",
  ].join("\n");

  it("extrai a nota inteira como texto corrido, sem as marcações", () => {
    expect(notaDeApoio(corpo)).toBe(
      "Este é um relatório gerado por IA com o objetivo de apoiar a tomada de decisão (não é um artefato oficial de auditoria).",
    );
  });

  it("desmarca ênfase e código: o card mostra o texto, não a marcação crua", () => {
    const corpoComMarcacao = [
      "# Base normativa",
      "",
      "> **Nota:** Relatório gerado por IA. **Não é artefato oficial**, não",
      "> edita nenhuma `regra-*.md` nem `data/regras-sisprev.csv`.",
    ].join("\n");
    expect(notaDeApoio(corpoComMarcacao)).toBe(
      "Relatório gerado por IA. Não é artefato oficial, não edita nenhuma regra-*.md nem data/regras-sisprev.csv.",
    );
  });

  it("devolve null quando o documento não traz nota — o site não fabrica uma", () => {
    expect(notaDeApoio("# RFC 0001\n\n- **Status**: Aceita\n")).toBeNull();
  });

  it("não captura uma citação que apareça depois do corpo já ter começado", () => {
    const tardio = "# Título\n\nParágrafo normal.\n\n> citação no meio do texto\n";
    expect(notaDeApoio(tardio)).toBeNull();
  });
});

describe("statusDaRfc", () => {
  it("lê o status declarado", () => {
    expect(statusDaRfc("# RFC 0001\n\n- **Status**: Aceita (2026-07-17)\n")).toBe("Aceita (2026-07-17)");
  });

  it("corta na primeira frase, sem levar junto as ressalvas da RFC", () => {
    const corpo = [
      "# RFC 0002",
      "",
      "- **Status**: proposta (2026-07-21); o filtro explicável de §1 foi",
      "  implementado no site (`/simulador/`, §7) — o **avaliador de decisão**",
      "  segue pendente.",
      "- **Criada em**: 2026-07-21",
    ].join("\n");
    expect(statusDaRfc(corpo)).toBe("proposta (2026-07-21)");
  });

  it("não corta no ponto de uma data ISO nem de uma abreviação colada", () => {
    expect(statusDaRfc("- **Status**: proposta (2026-07-23). Especificação revisável")).toBe(
      "proposta (2026-07-23)",
    );
  });

  it("devolve null quando a RFC não declara status", () => {
    expect(statusDaRfc("# RFC 0009\n\nsem status\n")).toBeNull();
  });
});

describe("numeroDaRfc", () => {
  it("tira o número do id do arquivo", () => {
    expect(numeroDaRfc("0003-site-estatico-de-publicacao")).toBe("0003");
  });

  it("devolve null para id fora do padrão", () => {
    expect(numeroDaRfc("rascunho")).toBeNull();
  });
});

describe("reescreverLinkMd", () => {
  it("liga um relatório a outro relatório", () => {
    expect(reescreverLinkMd("reconciliacao-invalidez-incapacidade.md", "relatorios", "/sisprev", REPO)).toEqual({
      url: "/sisprev/relatorios/reconciliacao-invalidez-incapacidade/",
      interno: true,
    });
  });

  it("preserva a âncora do link original", () => {
    const alvo = reescreverLinkMd("q6-causa-incapacidade.md#10-decisao", "relatorios", "/sisprev", REPO);
    expect(alvo?.url).toBe("/sisprev/relatorios/q6-causa-incapacidade/#10-decisao");
  });

  it("atravessa ../ entre as duas coleções, nos dois sentidos", () => {
    expect(reescreverLinkMd("../rfc/0002-selecao-explicavel-pos-anamnese.md", "relatorios", "/sisprev", REPO)?.url).toBe(
      "/sisprev/rfcs/0002-selecao-explicavel-pos-anamnese/",
    );
    expect(reescreverLinkMd("../analysis/q6-causa-incapacidade.md", "rfcs", "/sisprev", REPO)?.url).toBe(
      "/sisprev/relatorios/q6-causa-incapacidade/",
    );
  });

  it("liga uma RFC a outra RFC do mesmo diretório", () => {
    expect(reescreverLinkMd("0001-criterios-de-validacao-das-regras.md", "rfcs", "/sisprev", REPO)?.url).toBe(
      "/sisprev/rfcs/0001-criterios-de-validacao-das-regras/",
    );
  });

  it("manda para o GitHub o que o site não publica, em vez de deixar link morto", () => {
    expect(reescreverLinkMd("../spec/regra.md", "rfcs", "/sisprev", REPO)).toEqual({
      url: `${REPO}/blob/main/okf/spec/regra.md`,
      interno: false,
    });
    expect(reescreverLinkMd("../../CLAUDE.md", "rfcs", "/sisprev", REPO)?.url).toBe(`${REPO}/blob/main/CLAUDE.md`);
  });

  it("não toca em referência OKF absoluta — identidade não é rótulo de navegação", () => {
    expect(reescreverLinkMd("/regras/regra-0006.md", "relatorios", "/sisprev", REPO)).toBeNull();
  });

  it("não toca em link externo, âncora pura, nem em link que não seja .md", () => {
    expect(reescreverLinkMd("https://exemplo.org/x.md", "relatorios", "/sisprev", REPO)).toBeNull();
    expect(reescreverLinkMd("#secao-3", "relatorios", "/sisprev", REPO)).toBeNull();
    expect(reescreverLinkMd("imagem.png", "relatorios", "/sisprev", REPO)).toBeNull();
  });

  it("aceita base com e sem barra final, sem duplicar a barra", () => {
    expect(reescreverLinkMd("estado-da-auditoria.md", "relatorios", "/sisprev/", REPO)?.url).toBe(
      "/sisprev/relatorios/estado-da-auditoria/",
    );
  });
});
