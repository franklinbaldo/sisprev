/**
 * Lógica pura da busca (RFC 0003, Fase C — "busca Pagefind").
 *
 * O índice é construído pelo Pagefind sobre `dist/`, que é a raiz do site
 * publicado *sem* o prefixo `/sisprev` — o prefixo só existe nos links que
 * o Astro escreve, não na árvore de arquivos. Logo a URL que volta de um
 * resultado (`/relatorios/x/`) não é navegável como está: precisa da base
 * na frente. Isso vive aqui, puro e testado, em vez de virar uma
 * concatenação solta no meio do código de DOM.
 *
 * Sem nenhum import de `site-data.ts`: o job `test` do CI roda vitest
 * **sem** o emissor.
 */

/**
 * URL navegável de um resultado do Pagefind.
 *
 * Idempotente de propósito: se um dia o índice passar a gravar a URL já
 * com a base (mudança de configuração do Pagefind, ou um build servido de
 * outra raiz), o resultado continua correto em vez de virar
 * `/sisprev/sisprev/...`.
 */
export function urlDoResultado(url: string, base: string): string {
  const prefixo = base.replace(/\/$/, "");
  if (prefixo === "" || url.startsWith(`${prefixo}/`)) return url;
  return `${prefixo}${url.startsWith("/") ? "" : "/"}${url}`;
}

/**
 * Texto do contador de resultados.
 *
 * A busca do Pagefind é por página, não por documento OKF: uma listagem e
 * uma ficha são dois resultados. O rótulo diz "página(s)" por isso — dizer
 * "regra(s)" faria a contagem parecer uma contagem de catálogo, que ela
 * não é.
 */
export function rotuloDeContagem(total: number, termo: string): string {
  if (termo.trim() === "") return "Digite um termo para buscar.";
  if (total === 0) return `Nenhuma página encontrada para “${termo}”.`;
  if (total === 1) return `1 página encontrada para “${termo}”.`;
  return `${total} páginas encontradas para “${termo}”.`;
}
