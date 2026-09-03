import { defineHastPlugin } from "satteri";

/**
 * Dá nome acessível aos checkboxes gerados por listas de tarefas Markdown.
 *
 * O Sätteri materializa `- [ ] texto` como um `<input type="checkbox"
 * disabled>` seguido do texto do item. Visualmente isso comunica estado, mas
 * um controle sem nome faz o leitor de tela encontrar centenas de caixas
 * indistinguíveis no relatório. O plugin preserva o HTML e a aparência
 * locais; ele só torna explícito o que a própria lista já diz.
 */
export const pluginDeRotulosDeChecklist = defineHastPlugin({
  name: "sisprev-rotulos-de-checklist",
  element: {
    filter: ["input"],
    visit(node, ctx) {
      if (node.properties.type !== "checkbox" || node.properties.disabled !== true) return;
      if (typeof node.properties.ariaLabel === "string" && node.properties.ariaLabel.trim()) return;

      const pai = ctx.parent(node);
      const texto = pai ? ctx.textContent(pai).trim().replace(/\s+/g, " ") : "";
      const estado = node.properties.checked === true ? "Concluído" : "Pendente";
      ctx.setProperty(node, "ariaLabel", texto ? `${estado}: ${texto}` : estado);
    },
  },
});
