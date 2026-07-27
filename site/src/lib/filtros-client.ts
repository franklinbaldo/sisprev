// Cola de DOM das listagens filtráveis — mesma divisão do simulador
// (`simulador-client.ts`): nenhuma decisão de filtragem mora aqui, tudo vem
// de `filtros.ts`, que é puro e testado.
//
// Progressive enhancement, não requisito: a página sai do build com **todas**
// as fichas no HTML e a barra de filtros marcada `hidden`. Este script é o
// único que a revela — sem JS, ninguém vê um controle que não funciona, e a
// listagem continua completa (RFC 0003 §4: "zero JS no cliente por padrão").
//
// Contrato de marcação (produzido por `FilterBar.astro` + as páginas de
// índice), casado pelo nome da listagem:
//
//   <form data-filtro="regras" hidden>          controles: name="q" + uma faceta por name
//   <p data-filtro-contagem="regras" data-total="112" data-singular="regra" data-plural="regras">
//   <ul data-filtro-lista="regras">             itens: [data-filtro-item][data-busca][data-faceta-<chave>]
//   <p data-filtro-vazio="regras" hidden>
import {
  estadoFiltroDeParams,
  filtroEstaVazio,
  itemCorrespondeAoFiltro,
  paramsDeEstadoFiltro,
  PARAM_BUSCA,
  type EstadoFiltro,
} from "./filtros";

function chavesDeFaceta(form: HTMLFormElement): string[] {
  return [...new Set([...form.elements].flatMap((el) => {
    const nome = (el as HTMLInputElement).name;
    return nome && nome !== PARAM_BUSCA ? [nome] : [];
  }))];
}

function lerControles(form: HTMLFormElement, chaves: readonly string[]): EstadoFiltro {
  const dados = new FormData(form);
  const facetas: Record<string, string> = {};
  for (const chave of chaves) facetas[chave] = String(dados.get(chave) ?? "");
  return { busca: String(dados.get(PARAM_BUSCA) ?? ""), facetas };
}

function escreverControles(form: HTMLFormElement, estado: EstadoFiltro): void {
  const busca = form.elements.namedItem(PARAM_BUSCA);
  if (busca instanceof HTMLInputElement) busca.value = estado.busca;
  for (const [chave, valor] of Object.entries(estado.facetas)) {
    const controle = form.elements.namedItem(chave);
    if (controle instanceof HTMLSelectElement || controle instanceof HTMLInputElement) controle.value = valor;
  }
}

function itemFiltravel(elemento: HTMLElement, chaves: readonly string[]) {
  const facetas: Record<string, string> = {};
  for (const chave of chaves) facetas[chave] = elemento.getAttribute(`data-faceta-${chave}`) ?? "";
  return { busca: elemento.getAttribute("data-busca") ?? "", facetas };
}

function textoDaContagem(elemento: HTMLElement, visiveis: number, total: number): string {
  const singular = elemento.dataset.singular ?? "item";
  const plural = elemento.dataset.plural ?? `${singular}s`;
  const rotulo = total === 1 ? singular : plural;
  return visiveis === total
    ? `${total} ${rotulo}.`
    : `Mostrando ${visiveis} de ${total} ${rotulo}.`;
}

function ligarFiltro(form: HTMLFormElement): void {
  const nome = form.dataset.filtro;
  if (!nome) return;

  const lista = document.querySelector<HTMLElement>(`[data-filtro-lista="${nome}"]`);
  if (!lista) return;
  const itens = [...lista.querySelectorAll<HTMLElement>("[data-filtro-item]")];
  const contagem = document.querySelector<HTMLElement>(`[data-filtro-contagem="${nome}"]`);
  const vazio = document.querySelector<HTMLElement>(`[data-filtro-vazio="${nome}"]`);
  const limpar = form.querySelector<HTMLButtonElement>("[data-filtro-limpar]");
  const chaves = chavesDeFaceta(form);

  function aplicar(estado: EstadoFiltro, sincronizarUrl: boolean): void {
    let visiveis = 0;
    for (const item of itens) {
      const corresponde = itemCorrespondeAoFiltro(itemFiltravel(item, chaves), estado);
      item.hidden = !corresponde;
      if (corresponde) visiveis += 1;
    }

    if (contagem) {
      contagem.textContent = textoDaContagem(contagem, visiveis, itens.length);
    }
    if (vazio) vazio.hidden = visiveis > 0;
    if (limpar) limpar.disabled = filtroEstaVazio(estado);

    if (sincronizarUrl) {
      const params = paramsDeEstadoFiltro(estado).toString();
      // `replaceState`, não `pushState`: digitar numa busca não deve encher o
      // histórico de voltas intermediárias — mas a URL corrente continua
      // compartilhável e recarregável no mesmo recorte.
      window.history.replaceState(null, "", params ? `?${params}` : window.location.pathname);
    }
  }

  form.hidden = false;
  form.addEventListener("submit", (evento) => evento.preventDefault());
  form.addEventListener("input", () => aplicar(lerControles(form, chaves), true));
  form.addEventListener("change", () => aplicar(lerControles(form, chaves), true));
  limpar?.addEventListener("click", () => {
    const limpo: EstadoFiltro = { busca: "", facetas: Object.fromEntries(chaves.map((c) => [c, ""])) };
    escreverControles(form, limpo);
    aplicar(limpo, true);
  });

  // Estado inicial vindo da URL — é o que faz os números do painel da home
  // (`/regras/?status=revisada`) chegarem já filtrados.
  const inicial = estadoFiltroDeParams(new URLSearchParams(window.location.search), chaves);
  escreverControles(form, inicial);
  aplicar(inicial, false);
}

function init(): void {
  for (const form of document.querySelectorAll<HTMLFormElement>("form[data-filtro]")) ligarFiltro(form);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
