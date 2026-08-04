# CLAUDE.md

Mapa do repositório. Onde as coisas ficam e o que quebra sem avisar.

## O que este repo é

`sisprev` audita as regras de aposentadoria e pensão por morte do regime próprio
de previdência do Estado de Rondônia. O catálogo vive em três lugares:

- **`data/raw/`** — a importação congelada, read-only para o repositório: nada
  aqui deriva de nada, e `derivar.py` estoura se pedirem que a reescreva. É a
  linha de base: o que foi recebido, como foi recebido. O que a substitui é
  **recebimento novo da fonte**, ato humano e raro — foi assim que a coluna
  `ID` entrou, depois de a primeira remessa ter vindo sem ela. Substituir por
  conveniência de código é que não acontece.
- **`okf/regras-sisprev/`** — o registro vivo, um `regra-NNNN.md` por regra.
  **É aqui que se edita.** O frontmatter *é* a regra que vai para o Sisprev; o
  corpo é a análise do auditor e nunca é deployado.
- **`data/regras-sisprev.csv`** — export derivado, regenerado por script. Nunca
  se edita.

## O trabalho é conferir regras, não construir sistema

Cada regra importada precisa ser lida contra a lei, ter os dispositivos
vinculados à mão, e os erros escritos como achado. É esse o trabalho, e ele é
humano.

Diante de um problema, a pergunta é **"que edição num `.md` resolve isto?"** —
não "que campo, gate ou detector eu crio?". Quando uma edição de regra e uma
mudança de estrutura resolvem o mesmo problema, a edição ganha.

Este repositório aprendeu isso do jeito caro. Chegou a ter nove tipos de
documento, dezessete famílias de código de violação, um compilador, um bundle de
catálogo proposto e uma pilha de conjuntos — tudo construído antes de existir
demanda, enquanto a conferência de mérito mal tinha começado. Foi removido. O
que sobrou cabe nesta página, e é isso que se quer manter.

## Como rodar

```bash
uv run python scripts/derivar.py             # CSV + índices + snapshot do site
uv run okf-parser check okf/regras-sisprev   # um bundle por vez

cd site && npm install
npm run dev      # http://localhost:4321/sisprev/
npm run check    # astro check
npm run test     # vitest
npm run build    # -> site/dist/

uv run python scripts/gerar_relatorio_pdf.py   # exige npm run build antes
```

## O que existe

**`scripts/derivar.py`** é o único comando que escreve artefato derivado. Lê o
frontmatter e mais nada — sem regra de domínio, sem julgamento, sem gate. Um
erro de mérito atravessa ele intacto, porque não é ele quem tem competência para
achar erro de mérito. Produz o CSV, as duas listagens que carregam `nome`, e o
snapshot do site.

**`scripts/gerar_relatorio_pdf.py`** imprime o catálogo inteiro como documento
único, para a PGE juntar ao SEI. Roda sobre o `site/dist/` já buildado, via
WeasyPrint — não é navegador headless porque três recursos de CSS Paged Media
sustentam o documento (`string-set` no cabeçalho de folha, `target-counter` no
sumário, `bookmark-level`) e nenhum motor de navegador os implementa. O
`url_fetcher` **estoura** se um recurso não resolver: um PDF sem folha de estilo
sai legível e sem nenhuma quebra de página, e o defeito só apareceria depois de
o anexo já estar no processo.

**`okf-parser`** faz o parsing e a conformidade OKF. É dependência, não código
daqui. O leitor dele preserva todo escalar como texto — `2026-07-30` não vira
`date`, `TRUE` não vira `bool` —, e é isso que faz o CSV derivado dar round-trip
byte a byte com a importação original.

**O site** (`site/`, Astro estático) lê os `.md` direto por content collections.
A única ponte com o Python é `dados-do-site.json`: o SHA do commit publicado e o
estado de auditoria já indexado por id. Nunca comitado — ele carrega o SHA do
próprio commit que o geraria. O estado que ele carrega é **o que está escrito no
frontmatter**, sem recálculo: se um selo está errado, o erro está no `.md`.

**O CI** são quatro comandos num job só, comentados um a um em
`.github/workflows/ci.yml` com o que cada um protege. Guarda nova ali exige um
caso concreto que já tenha acontecido — foi a ausência dessa exigência que
produziu a infraestrutura que ele substituiu.

## Os documentos

| tipo          | onde                          | quem lê                       |
| ------------- | ----------------------------- | ----------------------------- |
| `Regra`       | `okf/regras-sisprev/regras/`  | `derivar.py`, site, relatório |
| `Achado`      | `okf/regras-sisprev/achados/` | `derivar.py`, site            |
| `Dispositivo` | `okf/dispositivos/`           | site, relatório               |
| `Norma`       | `okf/dispositivos/*/norma.md` | site                          |

Quatro outros bundles — `conjuntos/`, `regras-propostas/`, `formas-calculo/`,
`tipos-calculo/` — são **markdown inerte**. O código que os lia e validava foi
removido; os documentos ficaram porque são trabalho humano. Nada os confere.
Material de consulta, não parte viva do catálogo.

As specs em `docs/spec/` e as RFCs em `docs/rfc/` descrevem decisões, muitas
sobre estrutura que não existe mais. **Quando uma spec e o código divergirem, o
código ganha** — e a divergência é ela própria algo a corrigir na spec.

## O que quebra em silêncio

Cinco coisas. Todas já aconteceram aqui.

**A cadeia do dispositivo.** Um dispositivo é a unidade endereçada *com toda a
cadeia que a contém*, na redação contemporânea a ela. Alterar um ancestral cria
redação nova — arquivo novo, fronteira de vigência nova — ainda que o inciso não
mude uma vírgula. Uma vigência que atravessa a alteração de um ancestral monta
texto que nunca esteve em vigor junto. Cada parágrafo confere, o caminho
confere, e nada acusa. Foi assim que `art-40-par-1-inc-ii` ficou com vigência
atravessando a EC 41/2003 enquanto o irmão `inc-i` estava certo.

**Ler citação por regex.** Já existiu um leitor que extraía dispositivos da
`FUNDAMENTACAO` automaticamente. Foi feito com cuidado e produziu **nove
atribuições erradas**: `C/C` (*combinado com*) lido como inciso, dígitos de data
lidos como número de artigo, uma emenda estadual doando seus artigos à
Constituição federal. Todas pareciam citação bem formada. Foi removido, e sua
saída congelada virou lista de trabalho em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](docs/analysis/pendencias-de-citacao-congeladas.md).
A entrada em `dispositivos:` é **autorada**: um humano lê a fundamentação,
confere contra a fonte, escreve o vínculo. Nada lê aqueles campos mecanicamente,
e nada pode.

**Concluir sobre a lei em código.** "Esta redação nunca existiu", "esta
fundamentação cita o dispositivo errado", "estas duas regras são a mesma" — são
conclusões jurídicas, e a saída delas é **acusação** sobre campo que vai para
produção. Vão escritas à mão num achado, com autor e data, nunca emitidas por
uma função. Detector aponta ocorrência mecânica; quem conclui é o auditor.

**As datas sentinela.** `01/01/1900`, `01/01/1910` e `01/01/1950` nas colunas
`_APOS`, e `31/12/2099` nas colunas `_ATE`, são sentinelas: **significam
ausência de limite naquele eixo**, não uma fronteira em 1900 ou em 2099. Os três
valores de piso são convenções de digitação diferentes para a mesma coisa.
Tratá-los como data real inverte o sentido do critério — uma regra sem piso vira
uma regra que exige ingresso depois de 1950 —, e num anexo impresso `31/12/2099`
sem ressalva é lido como limite de verdade por quem assina. `site/src/lib/sentinela.ts`
é a declaração do conjunto.

`01/01/1969` fica **fora** do conjunto (`regra-0003`): é suspeita de erro de
digitação, não convenção conhecida, e uma suspeita que entra sem ato de ninguém
vira decisão de que aquele limite não é critério.

**O derivado fora de sincronia.** Um CSV comitado que não é o que o bundle
produz parece dado bom. Depois de editar qualquer `.md`, rode `derivar.py` e
comite o resultado.

## Antes de commitar

```bash
uv run ruff format --check && uv run ruff check
uv run mdformat --check --number okf docs README.md CLAUDE.md
uv run python scripts/derivar.py
git status --porcelain data/regras-sisprev.csv okf/regras-sisprev/*/index.md
```

Se mexeu no site ou no impresso, rode-os à mão — o CI do site roda `check` e
`test` em PR, mas o `build`, que inclui o PDF, só roda em push para `main`:

```bash
bash site/scripts/emit-data.sh && cd site && npm run check && npm run test && npm run build
cd .. && uv run python scripts/gerar_relatorio_pdf.py
```

## Convenções de escrita

- **Não escreva contagem em prosa.** Quantos testes passam, quantas regras estão
  num estado, quantas páginas o relatório tem: a árvore já responde, e o número
  envelhece a cada commit. Quem quer o número roda o comando.
- **Nem vocabulário que só é verdade num instante**: "hoje", "atualmente", "a
  única", "ainda não". Escreva a afirmação estrutural.
- **Sem `# noqa`.** Regra do ruff que não serve ao projeto é desligada no
  `pyproject.toml`, com o motivo escrito.
