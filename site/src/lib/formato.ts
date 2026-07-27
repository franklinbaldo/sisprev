// Camada de apresentação dos valores crus do catálogo (regra_schema.py
// COLUMNS) na ficha da regra — `TRUE`, `N`, `31/12/2099 00:00` são o formato
// de origem do Sisprev, não uma escolha de leitura.
//
// Duas regras governam este módulo:
//
// 1. **Nunca interpretar o que o projeto decidiu não interpretar.** Uma data
//    vazia é "sentinela — preservada, não interpretada (P5)" (ver o topo de
//    `parse-sisprev.ts`); `31/12/2099` **não** vira "sem limite" aqui, porque
//    isso seria inventar um fato de domínio (RFC 0003, não-objetivo). A
//    conversão feita é só de *formato*: a hora constante `00:00` sai, o dia/
//    mês/ano permanece exatamente o que está no `.md`.
// 2. **Nunca esconder o valor de origem.** Quando o texto exibido não
//    reproduz literalmente o valor do frontmatter (`S` → "Sim"), o bruto
//    volta em `bruto` para ser mostrado ao lado — quem audita precisa ver o
//    que está gravado, não só a leitura amigável dele.
//
// A conversão `S`/`N` → Sim/Não não é uma semântica nova: é a mesma que
// `parseSN` já aplica (e testa) para o simulador, reusada aqui em vez de
// reimplementada.
import { parseDataSisprev, parseSN } from "./parse-sisprev";

/**
 * Como um campo da ficha deve ser lido.
 *
 * - `texto` — verbatim, sem conversão nenhuma (o padrão).
 * - `sn` — flag `S`/`N` do catálogo.
 * - `booleano` — flag `TRUE`/`FALSE` do catálogo.
 * - `data` — `DD/MM/AAAA HH:MM` do catálogo.
 */
export type FormatoCampo = "texto" | "sn" | "booleano" | "data";

export interface ValorFormatado {
  /** Texto a exibir. Vazio quando o campo é vazio — quem renderiza decide o placeholder. */
  texto: string;
  /**
   * Valor exatamente como está no frontmatter, quando `texto` não o
   * reproduz literalmente. `null` quando não houve conversão alguma (aí
   * exibir o bruto ao lado seria só ruído duplicado).
   */
  bruto: string | null;
}

function verbatim(raw: string): ValorFormatado {
  return { texto: raw, bruto: null };
}

function doisDigitos(valor: number): string {
  return String(valor).padStart(2, "0");
}

/**
 * Formata um valor cru do catálogo para leitura, preservando o bruto quando
 * a conversão muda o texto.
 *
 * Qualquer valor que o parser correspondente não reconheça sai **verbatim**,
 * nunca coagido a um default — um `S`/`N` inesperado ou uma data malformada
 * é um fato sobre o catálogo que a ficha precisa mostrar, não corrigir.
 */
export function formatarValor(raw: string, formato: FormatoCampo = "texto"): ValorFormatado {
  const bruto = raw.trim();
  if (bruto === "") return verbatim(raw);

  switch (formato) {
    case "sn": {
      const flag = parseSN(bruto);
      return flag === null ? verbatim(raw) : { texto: flag ? "Sim" : "Não", bruto };
    }
    case "booleano": {
      const maiusculo = bruto.toUpperCase();
      if (maiusculo === "TRUE") return { texto: "Sim", bruto };
      if (maiusculo === "FALSE") return { texto: "Não", bruto };
      return verbatim(raw);
    }
    case "data": {
      const data = parseDataSisprev(bruto);
      if (data === null) return verbatim(raw);
      // Aqui, ao contrário de `sn`/`booleano`, o bruto **não** volta: a única
      // diferença entre ele e o texto exibido é a hora `00:00`, constante em
      // todas as linhas e explicitamente ignorada por este projeto na
      // comparação de datas (parse-sisprev.ts). Repetir "31/12/2099
      // 31/12/2099 00:00" ao lado do valor seria ruído, não transparência —
      // o dia/mês/ano exibido é literalmente o que está gravado.
      return { texto: `${doisDigitos(data.dia)}/${doisDigitos(data.mes)}/${data.ano}`, bruto: null };
    }
    case "texto":
      return verbatim(raw);
  }
}
