# RFC 0003 — Site estático para publicação do catálogo auditado

- **Status**: proposta (2026-07-22; revisada 2026-07-22 após review na
  [PR #25](https://github.com/franklinbaldo/sisprev/pull/25) — Q1 decidida
  (emissor derivado dedicado), frescor de deploy reescrito como
  verificável-por-SHA, Q4 passa a bloquear a Fase B, Zod endurecido para os
  campos consumidos e contrato de URLs fixado). Não escreve código de
  aplicação nem altera regras, achados ou dispositivos; define a arquitetura
  de um site **estático** que publica o bundle OKF e os relatórios como uma
  projeção navegável, e o processo para construí-lo e implantá-lo.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md)
  (bundle OKF como registro vivo; artefatos derivados por comando, P10;
  `status_auditoria`, P7; achados, P14; dispositivos, P3) e
  [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (o `nome` como a menor
  descrição que distingue uma regra). Consome a spec
  [`docs/spec/regra.md`](../spec/regra.md).
- **Não-objetivo**: virar um lugar onde se edita regra (isso continua sendo o
  `regra-*.md`, sempre); virar uma segunda fonte de verdade; ter backend,
  banco de dados ou formulários; reimplementar a lógica normativa (P2/P7/P14)
  em JavaScript; decidir ou conceder benefício (RFC 0002); **inventar fato de
  domínio** que não exista no bundle — metadados **derivados e rastreáveis**
  (estado calculado, backlinks, detecções, SHA da fonte) são permitidos,
  desde que remontem à fonte que os origina (§4).

## 1. Problema

O registro vivo é excelente para auditoria e péssimo para leitura. Hoje o
catálogo são 112+ `regra-*.md`, mais `achados/`, mais `okf/dispositivos/`,
mais os relatórios em `docs/analysis/` e as RFCs em `docs/rfc/`. Isso dá diff
por regra, revisão em PR e histórico linha-a-linha — mas quem precisa **ler** o
catálogo (PGE, Presidência, a própria equipe, um servidor conferindo a
fundamentação da sua regra) não vai abrir 112 arquivos markdown no GitHub nem
decifrar um CSV de 27 colunas.

Falta uma superfície publicada: **navegável, pesquisável, com URL estável por
regra / achado / dispositivo, e com as ligações cruzadas já resolvidas** (a
regra aponta para os dispositivos que cita; o achado aponta para as regras que
afeta; o dispositivo aponta para as regras que o citam). O CSV derivado
(`data/regras-sisprev.csv`) resolve "quero uma tabela plana", não "quero ler".

## 2. Princípio: o site é um artefato derivado

O site é uma **função pura das fontes autoradas** — os bundles OKF (`okf/`) e
os documentos em `docs/` — exatamente como `data/regras-sisprev.csv` é (P10,
"derivar"). É uma **projeção somente-leitura**: nada se edita pelo site, nada
nasce no site. Isso preserva a regra de ouro do repo — *edite a regra no
`.md`, nunca em outro lugar* — sem exceção nova.

Uma diferença em relação ao CSV: **o site não é commitado**. O CSV derivado
vive versionado e por isso precisa do gate `derived-csv-in-sync` para não
divergir do bundle no repositório. O site não tem esse tipo de drift: o único
artefato commitado é o **código-fonte do site** (o gerador), nunca o HTML
gerado — logo **não há artefato derivado versionado que possa divergir da
fonte**.

Isso **não** significa que "o site não pode divergir". O HTML servido pelo
GitHub Pages **pode ficar obsoleto** em relação à `main`: se o deploy de um
commit novo falhar, o Pages continua servindo o commit anterior; um build
verde no PR também não prova que o que está no ar corresponde à `main`. Ou
seja: **não há drift autorado no repositório; a correspondência entre o que
está publicado e a `main` é uma propriedade a ser *verificada*, não assumida.**
A prova é por SHA (§7): o site carrega e exibe o SHA e a data do snapshot que
originou aquele build, com link para o commit-fonte, e o pipeline de deploy
constrói/publica **exatamente** o SHA da `main` sob status obrigatório e um
smoke check pós-deploy.

Consequência de desenho: se o site precisar de um dado de auditoria que hoje
só a biblioteca Python sabe calcular (o `status_auditoria` efetivo, a lista de
detecções abertas — P7/P14), esse dado é **produzido pelo Python no build** e
consumido pelo site como entrada; o site **não recomputa** P2/P7/P14 em
JavaScript (§4).

## 3. O que o site expõe

| Coleção          | Fonte                             | Página de índice                                                                     | Página de detalhe                                                                                                                                                                                  |
| ---------------- | --------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regras**       | `okf/regras-sisprev/regras/*.md`  | listagem filtrável por `tipo_de_beneficio`, `ciclo_de_validacao`, `status_auditoria` | ficha da regra: o **frontmatter** como ficha estruturada (é a regra deployável) + o **corpo** renderizado (a análise do auditor), com links para os dispositivos citados e os achados que a afetam |
| **Achados**      | `okf/regras-sisprev/achados/*.md` | listagem por `situacao` e `severidade`                                               | descrição/evidências/questão renderizadas, `deteccoes` (detector + fingerprint) e backlinks para `regras_afetadas`                                                                                 |
| **Dispositivos** | `okf/dispositivos/**/*.md`        | listagem agrupada por norma                                                          | texto legal **verbatim** + metadados (`norma`, `artigo`, `redacao_dada_por`, `fonte`) e backlinks das regras que o citam                                                                           |
| **Relatórios**   | `docs/analysis/*.md`              | listagem                                                                             | relatório renderizado                                                                                                                                                                              |
| **RFCs**         | `docs/rfc/*.md`                   | listagem                                                                             | RFC renderizada (esta inclusa)                                                                                                                                                                     |
| **Painel**       | `dados-do-site.json` (build, §4)  | —                                                                                    | uma home com o estado da auditoria: contagens por `status_auditoria`, por `validado_pge`/`validado_presidencia`, por ciclo, e achados abertos por severidade                                       |

Ligações cruzadas resolvidas em build: regra ↔ dispositivo (via
`dispositivos:` da regra) e regra ↔ achado (via `regras_afetadas` do achado —
a mesma fonte única que a P14 já usa). Não se inventa nenhuma relação nova; o
site só torna navegável o que os bundles já declaram.

## 4. Arquitetura técnica

- **Gerador**: [Astro](https://astro.build) em modo estático (SSG),
  TypeScript. Escolhido por content collections nativas sobre markdown +
  frontmatter, zero JS no cliente por padrão (páginas HTML puras, rápidas e
  acessíveis) e build reproduzível. Mora em **`site/`** no mesmo repositório
  (monorepo) — o gerador ao lado das fontes que ele projeta.

- **Leitura direta do bundle, sem re-exportar**: as content collections usam o
  *glob loader* apontando para `../okf/**` e `../docs/**`. O site lê os mesmos
  `regra-*.md`/`achado-*.md`/dispositivos que a auditoria edita — **não há uma
  segunda cópia** dos dados nem um passo de "exportar para JSON o catálogo".
  Fonte única preservada.

- **Ponte de estado de auditoria — emissor derivado dedicado (Q1 decidida)**.
  O `validar_regras.py --json` de hoje **não serve** como ponte: seu payload só
  contém `violations` e `detections` (nem regras, nem `status_auditoria`, nem
  validações institucionais, nem achados, nem contagens do painel) e é emitido
  via `logger` — sai por **stderr**, não stdout. Em vez de esticá-lo, a Fase C
  adiciona um **emissor derivado dedicado** — `dados-do-site.json`, gerado pelo
  Python sob P10 (novo alvo de `gerar_indices.py` ou script irmão), com
  **contrato versionado** (`schema_version`) contendo, no mínimo:

  - **`sha` da fonte** e data do snapshot;
  - **regras** com seus estados validados (`status_auditoria` efetivo,
    `validado_pge`/`validado_presidencia`, ciclo);
  - **achados** e suas relações (`regras_afetadas`, `deteccoes`);
  - **detecções** e **violações** (o que o payload atual já tem);
  - **contagens do painel** (por status, por validação, por ciclo, achados
    abertos por severidade).

  Assim o site **nunca reimplementa** P2/P7/P14 em JS: a lógica normativa fica,
  como manda a RFC 0001, na biblioteca Python pura, e o site consome um
  contrato explícito e testável — não um efeito colateral de log.

- **Schema Zod — estrito no que o site consome, permissivo só no resto**. Todo
  campo que alimenta **rota, filtro, selo ou relação** é validado
  estritamente: `id` (identidade imutável), `type`, `status_auditoria`,
  `validado_pge`/`validado_presidencia`, `ciclo_de_validacao`,
  `tipo_de_beneficio` (regra); `situacao`, `severidade`, `regras_afetadas`,
  `deteccoes` (achado); `norma`, `artigo`, `fonte` (dispositivo);
  `dispositivos` (referências da regra). Um array virado string por acidente,
  ou um enum fora do vocabulário, **falha o build com erro claro** em vez de
  quebrar um backlink silenciosamente. O `passthrough()` cobre **apenas** os
  ~27 campos de domínio não consumidos pelo site (espelhando o `Concept`
  shape-only do `concept.py` e a razão da P2 — todo campo de domínio é
  material, um schema estrito do documento inteiro contradiria isso). O
  contrato de verdade continua no Python (Pydantic + `validar_regras`); o Zod
  do site é só o suficiente para o build falhar cedo, nunca uma segunda
  definição do contrato.

- **Contrato de URLs — identidades imutáveis, nunca rótulos**. As rotas
  derivam **exclusivamente** do `id` estável de cada documento, nunca de
  `nome`, título ou fundamentação (que mudam — RFC 0002):

  - `/regras/regra-0006/`
  - `/achados/achado-0009/`
  - `/dispositivos/cf88/art-40-i-original/`

  O `nome` aparece no conteúdo da página, nunca na URL. Uma correção de `nome`
  numa auditoria não pode quebrar links externos já compartilhados.

- **Busca**: [Pagefind](https://pagefind.app) — índice de busca estático
  gerado sobre o HTML no fim do build, client-side, sem servidor. Os
  resultados de busca carregam o selo de estado de validação (§5).

- **Estilo**: CSS próprio, mínimo e acessível (sem framework pesado);
  responsivo; tema claro/escuro.

## 5. Governança da publicação (detecção ≠ conclusão, aplicada ao leitor)

Ponto sensível e **bloqueante da Fase B** (§8). Na baseline importada,
**nenhuma regra concluiu o ciclo de validação** (`validado_pge`/
`validado_presidencia` ambos `FALSE`) e a maioria está `importada`, não
`revisada`/`validada`. Publicar essas regras sem deixar isso à vista corre o
risco de que sejam lidas como **oficiais/validadas** — o oposto do que o repo
afirma.

O GitHub Pages e "acesso ao conteúdo pré-validação" **não são decisões
independentes**: se o Pages publica todo o catálogo, a decisão prática já é
"conteúdo público". E, como **nada está validado**, o risco **não se resolve
só com um selo por ficha**. Por isso a política de acesso (Q4, §9) precisa ser
decidida **antes** de qualquer deploy da Fase B:

- **Se público**: título global "catálogo em auditoria", aviso global
  proeminente, estado de validação também nos resultados de busca, e
  possivelmente `noindex` enquanto nenhuma regra estiver validada — para o site
  não ser indexado como fonte oficial.
- **Se restrito**: rever GitHub Pages / hosting **antes** da implementação
  (Pages de projeto é público por padrão), escolhendo um alvo com controle de
  acesso.

Em qualquer caso, o site **exibe o estado de validação de forma proeminente**
em toda ficha, listagem e resultado de busca (`status_auditoria`,
`validado_pge`, `validado_presidencia`, ciclo). É a mesma linha "detecção ≠
conclusão" da RFC 0001, agora aplicada a quem lê o site — o site publica o
**estado da auditoria**, não um veredito.

## 6. Convivência com o toolchain Python

O `site/` traz um toolchain Node isolado e **não toca** os gates existentes:

- `ruff` (`select = ["ALL"]`) e `ty` continuam só sobre Python;
  `md_format.py --check` continua sobre `okf docs README.md CLAUDE.md`. O site
  adiciona os seus próprios checks (`astro check`, formatação) num **job de CI
  separado**, sem interferir nos jobs `lint`/`typecheck`/`test`/
  `derived-csv-in-sync`/`original-raw-immutable`.
- `.gitignore` ganha `site/node_modules/` e `site/dist/` (o HTML gerado nunca
  é commitado — §2).
- Nenhuma dependência Node entra no `pyproject.toml`/`uv.lock`; o site tem seu
  próprio `package.json`/lockfile dentro de `site/`.

## 7. Deploy e prova de frescor

- **Deploy do SHA exato da `main`.** Um workflow novo (`pages.yml`, ou um job
  isolado) roda, para **o commit exato da `main`**: o emissor
  `dados-do-site.json` (§4), `astro build`, o índice Pagefind, e publica no
  GitHub Pages. Sem rebuild de conteúdo antigo, sem mistura de SHAs.
- **Frescor verificável (§2).** O site **exibe o SHA e a data do snapshot** que
  originaram o build, com **link para o commit-fonte** no GitHub. Assim
  qualquer pessoa confere, sem confiar, se o que está no ar corresponde à
  `main`.
- **Deploy como status obrigatório / ambiente protegido**, com **smoke check
  pós-deploy** (o site respondeu 200 e o SHA publicado é o esperado) — um
  deploy que falha não passa silenciosamente deixando o Pages servir o commit
  anterior; a falha é visível e acionável.
- **Build de validação em PR (não é preview navegável).** O mesmo build roda em
  PR **sem deploy**, apenas para validar: uma regra nova cujo frontmatter
  quebra o schema Zod estrito (§4), ou um dispositivo mal formado, **falha o
  build** antes do merge. É um gate de validação de schema, não um ambiente de
  preview navegável.
- **Base path**: projeto em `franklinbaldo.github.io/sisprev` exige
  `base: '/sisprev'` no `astro.config`. Domínio próprio fica para a §9 (Q3).

## 8. Fases

- **Fase A — esta RFC.** Só a proposta; nenhum código de site.
- **Fase B — esqueleto + coleções.** Projeto Astro em `site/`, coleções de
  **regras**, **achados** e **dispositivos** com índices, páginas de detalhe,
  URLs por identidade imutável (§4) e ligações cruzadas; selos de estado de
  validação (§5). **Bloqueada até Q4 (§9) ser decidida** — o modo de acesso
  determina o alvo de hosting e o tratamento de indexação/aviso global antes de
  qualquer deploy.
- **Fase C — estado + busca + textos.** Emissor derivado `dados-do-site.json`
  (§4) e o painel que o consome, busca Pagefind, e as coleções de
  **relatórios** e **RFCs**.
- **Fase D — opcional.** Filtros avançados, exportações, e o que as questões da
  §9 decidirem.

## 9. Questões em aberto

- **Q1 — ponte de estado. *Decidida* (§4).** Emissor derivado dedicado
  `dados-do-site.json`, sob P10, com contrato versionado — **não** reutilizar
  `validar_regras.py --json` (payload insuficiente e emitido por stderr).
- **Q2 — onde o site mora.** `site/` no mesmo repo (recomendado — gerador ao
  lado da fonte, um único PR muda regra e vê o efeito no build de validação)
  vs. repo separado consumindo este via submódulo/download.
- **Q3 — URL/domínio.** Pages de projeto (`/sisprev`) vs. domínio próprio.
- **Q4 — acesso ao conteúdo pré-validação (§5). *Bloqueia a Fase B*.** Público
  (com título "catálogo em auditoria", aviso global, estado nas buscas e
  possivelmente `noindex` enquanto nada validado) ou restrito (revisar
  hosting/Pages antes de implementar)? Precisa ser decidida antes de qualquer
  deploy.
- **Q5 — gerador.** Astro (proposto) vs. outra SSG. A escolha afeta só a Fase B;
  a arquitetura da §2 (projeção derivada, fonte única, ponte Python) vale para
  qualquer gerador estático.
