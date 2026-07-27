/**
 * Cola de DOM da busca (RFC 0003, Fase C). Sem lógica de negócio: quem
 * decide URL e rótulo é `lib/busca.ts`, puro e testado — mesma divisão do
 * simulador (`simulador.ts` / `simulador-client.ts`) e dos filtros.
 *
 * O índice do Pagefind só existe depois de `astro build` + `pagefind`
 * (o `postbuild` do `package.json`). Em `npm run dev` ele não existe, e o
 * import falha — por isso o formulário sai do HTML com `hidden` e **só o
 * JS o revela**, depois de confirmar que o índice carregou: sem índice,
 * ninguém vê um campo de busca que não busca. É a mesma regra da barra de
 * filtros, pelo mesmo motivo (não exibir controle morto).
 */

import { rotuloDeContagem, urlDoResultado } from "./busca";

interface ResultadoPagefind {
  url: string;
  excerpt: string;
  /** `selo` só existe para regra/achado — as fichas que têm estado de auditoria. */
  meta?: { title?: string; selo?: string };
  filters?: Record<string, string[]>;
}

interface BuscaPagefind {
  results: Array<{ data: () => Promise<ResultadoPagefind> }>;
}

interface Pagefind {
  search: (termo: string) => Promise<BuscaPagefind>;
  options?: (opcoes: Record<string, unknown>) => Promise<void>;
}

/** Quantos resultados são detalhados por vez. */
const LOTE = 20;

function comoTexto(valor: unknown, alternativa: string): string {
  return typeof valor === "string" && valor.trim() !== "" ? valor : alternativa;
}

export async function iniciarBusca(): Promise<void> {
  const form = document.querySelector<HTMLFormElement>("[data-busca]");
  const campo = document.querySelector<HTMLInputElement>("[data-busca-termo]");
  const contagem = document.querySelector<HTMLElement>("[data-busca-contagem]");
  const lista = document.querySelector<HTMLElement>("[data-busca-resultados]");
  const indisponivel = document.querySelector<HTMLElement>("[data-busca-indisponivel]");
  if (form === null || campo === null || contagem === null || lista === null) return;

  const base = form.dataset.base ?? "";

  let pagefind: Pagefind;
  try {
    // O índice só passa a existir *depois* do build (o `postbuild` roda o
    // Pagefind sobre o `dist/` já pronto), então o import tem de ficar
    // opaco ao empacotador. `/* @vite-ignore */` sozinho não basta aqui: o
    // Vite ainda envolve a chamada no seu helper de preload e deixa um
    // `__VITE_PRELOAD__` por substituir, que estoura em runtime. Construir
    // o `import` fora do alcance da análise estática é o que garante que a
    // chamada chegue ao navegador como está escrita.
    const caminho = `${base.replace(/\/$/, "")}/pagefind/pagefind.js`;
    const importarEmRuntime = new Function("caminho", "return import(caminho)") as (
      caminho: string,
    ) => Promise<Pagefind>;
    pagefind = await importarEmRuntime(caminho);
  } catch {
    // Sem índice (tipicamente `npm run dev`): o formulário continua
    // escondido e a página explica por quê, em vez de oferecer uma busca
    // que devolveria sempre zero.
    indisponivel?.removeAttribute("hidden");
    return;
  }

  form.removeAttribute("hidden");

  let geracao = 0;
  async function buscar(termo: string): Promise<void> {
    const minha = ++geracao;
    if (termo.trim() === "") {
      lista!.replaceChildren();
      contagem!.textContent = rotuloDeContagem(0, termo);
      return;
    }
    const busca = await pagefind.search(termo);
    const dados = await Promise.all(busca.results.slice(0, LOTE).map((r) => r.data()));
    // Uma busca lenta que voltasse depois de uma mais nova sobrescreveria o
    // resultado corrente — cada execução só escreve se ainda for a última.
    if (minha !== geracao) return;

    contagem!.textContent = rotuloDeContagem(busca.results.length, termo);
    lista!.replaceChildren(
      ...dados.map((resultado) => {
        const item = document.createElement("li");
        item.className = "busca-resultado";

        const titulo = document.createElement("a");
        titulo.href = urlDoResultado(resultado.url, base);
        titulo.textContent = comoTexto(resultado.meta?.title, resultado.url);
        item.append(titulo);

        const secao = resultado.filters?.["Seção"]?.[0];
        if (secao !== undefined) {
          const chip = document.createElement("span");
          chip.className = "meta-chip";
          chip.textContent = secao;
          item.append(" ", chip);
        }

        // RFC 0003 §5: o selo de estado acompanha a regra/achado em toda
        // superfície, e a lista de resultados é uma delas — um resultado não
        // pode parecer catálogo pronto.
        if (resultado.meta?.selo !== undefined) {
          const selo = document.createElement("span");
          selo.className = "meta-chip";
          selo.textContent = resultado.meta.selo;
          item.append(" ", selo);
        }

        const trecho = document.createElement("p");
        // `excerpt` vem do Pagefind com <mark> nos termos casados; é HTML
        // gerado pelo próprio índice a partir do nosso conteúdo estático,
        // não entrada de usuário.
        trecho.innerHTML = resultado.excerpt;
        item.append(trecho);
        return item;
      }),
    );
  }

  let agendado: ReturnType<typeof setTimeout> | undefined;
  campo.addEventListener("input", () => {
    if (agendado !== undefined) clearTimeout(agendado);
    agendado = setTimeout(() => void buscar(campo.value), 150);
  });
  form.addEventListener("submit", (evento) => {
    evento.preventDefault();
    if (agendado !== undefined) clearTimeout(agendado);
    void buscar(campo.value);
  });

  // Um link para `/busca/?q=termo` chega buscando, e a busca feita é
  // compartilhável — mesma decisão da query string dos filtros.
  const inicial = new URLSearchParams(window.location.search).get("q");
  if (inicial !== null && inicial !== "") {
    campo.value = inicial;
    await buscar(inicial);
  }
  campo.focus();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => void iniciarBusca());
} else {
  void iniciarBusca();
}
