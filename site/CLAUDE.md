# site/

Astro estático; lê os `.md` do repositório por content collections.

- A ponte com o Python é `src/data/dados-do-site.json`, gerado por
  `bash site/scripts/emit-data.sh` (ou `derivar.py --somente-snapshot`). Ele
  carrega o SHA do próprio commit que o geraria, e por isso vive fora do git
  — regenere, sempre.
- O estado que o site mostra é **o que está escrito no frontmatter**, sem
  recálculo: selo errado se corrige no `.md`.
- Os módulos testados em `src/lib/` são puros — sem `astro:content` nem
  `site-data` — porque o job `test` do CI roda vitest sem o emissor. Quem
  liga um módulo às coleções é a página `.astro`.
- `scripts/gerar_relatorio_pdf.py` imprime o catálogo para a PGE sobre o
  `site/dist/` já buildado, via WeasyPrint: três recursos de CSS Paged Media
  sustentam o documento (`string-set`, `target-counter`, `bookmark-level`) e
  motor de navegador nenhum os implementa. O `url_fetcher` **estoura** quando
  um recurso deixa de resolver — um PDF sem folha de estilo sai legível, e o
  defeito só apareceria com o anexo já no processo.
- Comandos: `npm run dev` / `check` / `test` / `build`; o `build` exige o
  emit-data antes.
