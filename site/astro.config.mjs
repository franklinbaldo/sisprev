// @ts-check
import { defineConfig } from "astro/config";
import { satteri } from "@astrojs/markdown-satteri";
import { pluginDeLinksDeDocumentos } from "./src/plugins/links-de-documentos";
import { pluginDeRotulosDeChecklist } from "./src/plugins/rotulos-de-checklist";
import { REPO_URL } from "./src/consts";

// RFC 0003 §7/§9 (Q3/Q4 decididas): GitHub Pages de projeto, público, em
// https://franklinbaldo.github.io/sisprev/ — base precisa bater com o nome
// do repositório para os links relativos funcionarem sob esse subpath.
const base = "/sisprev";

export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base,
  markdown: {
    // `satteri()` é o processador que o Astro 7 já usa por padrão; declará-lo
    // aqui só serve para pendurar os plugins locais, sem trocar o pipeline de
    // markdown do site.
    //
    // A base entra por opção, e não por `import.meta.env.BASE_URL`: o plugin
    // de links roda no processo de build (contexto Node), fora do módulo Astro
    // onde essa variável existe. O plugin HAST de checklist age depois da
    // conversão para HTML e nomeia os checkboxes gerados pelo Markdown.
    processor: satteri({
      mdastPlugins: [pluginDeLinksDeDocumentos({ base, repoUrl: REPO_URL })],
      hastPlugins: [pluginDeRotulosDeChecklist],
    }),
  },
});
