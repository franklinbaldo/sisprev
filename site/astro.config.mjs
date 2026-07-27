// @ts-check
import { defineConfig } from "astro/config";
import { satteri } from "@astrojs/markdown-satteri";
import { pluginDeLinksDeDocumentos } from "./src/plugins/links-de-documentos";
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
    // aqui só serve para pendurar o plugin de links, sem trocar o pipeline de
    // markdown do site.
    //
    // A base entra por opção, e não por `import.meta.env.BASE_URL`: o plugin
    // roda no processo de build (contexto Node), fora do módulo Astro onde
    // essa variável existe.
    processor: satteri({
      mdastPlugins: [pluginDeLinksDeDocumentos({ base, repoUrl: REPO_URL })],
    }),
  },
});
