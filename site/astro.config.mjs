// @ts-check
import { defineConfig } from "astro/config";

// RFC 0003 §7/§9 (Q3/Q4 decididas): GitHub Pages de projeto, público, em
// https://franklinbaldo.github.io/sisprev/ — base precisa bater com o nome
// do repositório para os links relativos funcionarem sob esse subpath.
export default defineConfig({
  site: "https://franklinbaldo.github.io",
  base: "/sisprev",
});
