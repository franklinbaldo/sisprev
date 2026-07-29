// Porte do conjunto declarado das sentinelas de data (RFC 0011, P5).
//
// `scripts/sentinela.py` é a autoridade — é o Python que derruba o commit,
// mesma divisão de `dispositivo_endereco.py` / `dispositivo.ts`. Os valores
// aqui são os mesmos membros, na mesma grafia gravada, e o gate que os amarra
// à importação congelada (`tests/test_sentinela.py`) roda do lado Python.
//
// **O que este módulo diz, e o que ele não diz.** Diz que um valor pertence ao
// conjunto que a coordenação nomeou sentinela na decisão de 2026-07-17 — isto
// é, que não pretende nomear um marco. **Não diz o que ele significa**: se
// `31/12/2099` quer dizer "sem limite superior" é a pergunta 4 da §5.3 do
// levantamento das janelas temporais, e segue aberta. Nenhum consumidor daqui
// pode renderizar "sem limite": a ficha continua imprimindo a data que está
// escrita (`formato.ts`, regra 1).
import { parseDataSisprev, type DataCivil } from "./parse-sisprev";

/** Os quatro valores, na grafia exatamente gravada no frontmatter e no CSV. */
export type Sentinela = "01/01/1900 00:00" | "01/01/1910 00:00" | "01/01/1950 00:00" | "31/12/2099 00:00";

export const SENTINELAS: readonly Sentinela[] = [
  "01/01/1900 00:00",
  "01/01/1910 00:00",
  "01/01/1950 00:00",
  "31/12/2099 00:00",
];

// Indexado pela parte de data: a hora é ignorada na classificação, como é
// ignorada em todo o projeto na comparação de datas (nota de topo de
// `parse-sisprev.ts`) e como a ficha já a omite ao exibir.
const POR_DATA = new Map<string, Sentinela>(SENTINELAS.map((valor) => [valor.slice(0, 10), valor]));

function chave(data: DataCivil): string {
  const dd = String(data.dia).padStart(2, "0");
  const mm = String(data.mes).padStart(2, "0");
  return `${dd}/${mm}/${data.ano}`;
}

/**
 * A sentinela que uma data civil já parseada é, ou `null`.
 *
 * É esta a forma que o simulador usa: ele carrega `DataCivil`, não a string
 * bruta, e a parte de data é tudo o que a classificação olha.
 */
export function sentinelaDaData(data: DataCivil): Sentinela | null {
  return POR_DATA.get(chave(data)) ?? null;
}

/**
 * A sentinela que `valor` é, ou `null`. Aceita a forma gravada
 * (`DD/MM/AAAA HH:MM`) e a forma sem hora. Nunca lança.
 *
 * Espelha `sentinela_de` do lado Python. Como lá, **não existe uma
 * `limiteValido()`**: um limite não-sentinela não é um limite correto —
 * `15/12/1998` é não-sentinela e é o candidato a erro de um dia da §3.1 do
 * levantamento. O complemento de "sentinela" é "valor a conferir".
 */
export function sentinelaDe(valor: string): Sentinela | null {
  const data = parseDataSisprev(valor);
  return data === null ? null : sentinelaDaData(data);
}
