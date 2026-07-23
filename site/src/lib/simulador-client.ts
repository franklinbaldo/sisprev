// Cola de DOM para /simulador/ — lê o dataset embutido pela página, ouve o
// formulário, chama o motor puro (simulador.ts) e renderiza o resultado.
// Deliberadamente fino: nenhuma regra de avaliação mora aqui.
import { avaliarSolicitacao, regrasSimuladorFromJSON, type AvaliacaoRegra, type FatosRequerimento, type RegraSimulador } from "./simulador";
import { parseIsoDateInput } from "./parse-sisprev";

// Reaproveita os tons de StatusBadge já existentes — "excluída" ~
// bloqueante, "não excluída" ~ neutro (nunca "validado"/✓: este filtro não
// confirma compatibilidade, só afasta o que um critério conhecido exclui).
const TONE_ICON: Record<string, string> = { bloqueante: "⚠", neutro: "•" };

function el<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  opts: { text?: string; className?: string } = {},
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (opts.text !== undefined) node.textContent = opts.text;
  if (opts.className !== undefined) node.className = opts.className;
  return node;
}

function badge(tone: "bloqueante" | "neutro", label: string): HTMLElement {
  const span = el("span", { className: "status-badge" });
  span.dataset.tone = tone;
  const icon = el("span", { text: TONE_ICON[tone] });
  icon.setAttribute("aria-hidden", "true");
  span.append(icon, document.createTextNode(` ${label}`));
  return span;
}

function renderRegraCard(avaliacao: AvaliacaoRegra, regra: RegraSimulador | undefined, base: string): HTMLElement {
  const article = el("article", { className: "entity-card" });
  const header = el("header");
  const heading = el("h3");
  const link = el("a", { text: avaliacao.nome });
  link.href = `${base.replace(/\/$/, "")}/regras/${avaliacao.regraId}/`;
  heading.appendChild(link);
  header.appendChild(heading);
  header.appendChild(
    avaliacao.valor === "excluida" ? badge("bloqueante", "Excluída") : badge("neutro", "Não excluída"),
  );
  article.appendChild(header);

  if (avaliacao.criteriosSatisfeitos.length > 0) {
    const p = el("p", { text: `Critérios que bateram: ${avaliacao.criteriosSatisfeitos.join(", ")}.` });
    article.appendChild(p);
  }
  if (avaliacao.motivoExclusao) {
    article.appendChild(el("p", { text: avaliacao.motivoExclusao }));
  }
  if (avaliacao.fatosPendentes.length > 0) {
    const p = el("p", { text: "Pendências — nada aqui foi confirmado:" });
    const ul = el("ul");
    for (const pendencia of avaliacao.fatosPendentes) {
      ul.appendChild(el("li", { text: pendencia }));
    }
    article.append(p, ul);
  }
  if (regra) {
    const resultado = el("p", {
      text:
        `Resultado candidato no catálogo (não verificado pelo simulador — ver RFC 0002 §3): ` +
        `integral ${regra.integral === null ? "não preenchido" : regra.integral ? "sim" : "não"}, ` +
        `tipo de cálculo "${regra.tipoCalculo || "não preenchido"}", ` +
        `paridade ${regra.paridade === null ? "não preenchida" : regra.paridade ? "sim" : "não"}.`,
    });
    resultado.className = "simulador-resultado-candidato";
    article.appendChild(resultado);
  }
  return article;
}

function init(): void {
  const dataEl = document.getElementById("simulador-regras-data");
  const form = document.getElementById("simulador-form") as HTMLFormElement | null;
  const resultado = document.getElementById("simulador-resultado");
  if (!dataEl?.textContent || !form || !resultado) return;

  const base = resultado.dataset.base ?? "";
  const regras = regrasSimuladorFromJSON(JSON.parse(dataEl.textContent) as unknown[]);
  const regrasPorId = new Map(regras.map((r) => [r.id, r]));

  function lerFatos(): FatosRequerimento | null {
    if (!form) return null;
    const tipoDeBeneficio = (form.elements.namedItem("tipoBeneficio") as HTMLSelectElement).value;
    if (!tipoDeBeneficio) return null;
    const sexoRaw = (form.elements.namedItem("sexo") as HTMLSelectElement).value;
    const aposRaw = (form.elements.namedItem("aposEspecial") as HTMLSelectElement).value;
    const dataAdmissao = parseIsoDateInput((form.elements.namedItem("dataAdmissao") as HTMLInputElement).value);
    const dataDireito = parseIsoDateInput((form.elements.namedItem("dataDireito") as HTMLInputElement).value);
    return {
      tipoDeBeneficio,
      sexo: sexoRaw === "MASCULINO" || sexoRaw === "FEMININO" ? sexoRaw : null,
      aposEspecial: aposRaw === "" ? null : aposRaw === "sim",
      dataAdmissao,
      dataDireito,
    };
  }

  function render(): void {
    if (!resultado) return;
    resultado.replaceChildren();
    const fatos = lerFatos();
    if (!fatos) {
      resultado.appendChild(el("p", { text: "Selecione o tipo de benefício para começar." }));
      return;
    }

    const rastro = avaliarSolicitacao(regras, fatos);

    const resumo =
      rastro.naoExcluidas.length === 0
        ? "Nenhuma regra restante — todas as regras simuláveis foram excluídas pelos fatos informados."
        : `${rastro.naoExcluidas.length} regra(s) não excluída(s) pelos fatos informados — isso NÃO é uma lista de regras aplicáveis, só as que os fatos informados não afastam. Veja as pendências de cada uma.`;
    resultado.appendChild(badge(rastro.naoExcluidas.length === 0 ? "bloqueante" : "neutro", resumo));

    if (rastro.naoExcluidas.length > 0) {
      resultado.appendChild(el("h3", { text: "Não excluídas" }));
      for (const candidata of rastro.naoExcluidas) {
        resultado.appendChild(renderRegraCard(candidata, regrasPorId.get(candidata.regraId), base));
      }
    }

    if (rastro.excluidas.length > 0) {
      const details = el("details");
      const summary = el("summary", { text: `Regras excluídas (${rastro.excluidas.length})` });
      details.appendChild(summary);
      for (const excluida of rastro.excluidas) {
        details.appendChild(renderRegraCard(excluida, regrasPorId.get(excluida.regraId), base));
      }
      resultado.appendChild(details);
    }
  }

  form.addEventListener("input", render);
  form.addEventListener("change", render);
  render();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
