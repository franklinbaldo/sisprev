# CLAUDE.md

Mapa do repositório. Onde as coisas ficam e o que já quebrou em silêncio.

## O que este repo é

`sisprev` audita as regras de aposentadoria e pensão por morte do regime próprio
de previdência do Estado de Rondônia. O catálogo vive em três lugares:

- **`data/raw/`** — a importação congelada, a linha de base: o que foi
  recebido, como foi recebido, conferido pelo manifesto `SHA256SUMS`. O que a
  substitui é **recebimento novo da fonte**, ato humano e deliberado que
  aparece no diff do manifesto — foi assim que a coluna `ID` entrou, depois de
  a primeira remessa ter vindo sem ela.
- **`okf/`** — o registro vivo. **É aqui que se edita**: o catálogo legado
  (`regras-sisprev/`, um `regra-NNNN.md` por regra), o catálogo proposto
  (`regras-propostas/`), os dispositivos legais (`dispositivos/`), as fórmulas
  (`tipos-calculo/`) e as specs (`spec/`). O frontmatter *é* o dado que vai
  para o Sisprev; o corpo é a análise do auditor e fica no repositório.
- **`data/regras-sisprev.csv` e `data/regras-propostas.csv`** — exports
  derivados, regenerados por `scripts/derivar.py` a cada edição e conferidos
  pelo CI contra o bundle.

## O trabalho é conferir regras

Cada regra importada precisa ser lida contra a lei, ter os dispositivos
vinculados à mão, e os erros escritos como achado. É esse o trabalho, e ele é
humano. Diante de um problema, a pergunta é **"que edição num `.md` resolve
isto?"** — quando uma edição de regra e uma mudança de estrutura resolvem o
mesmo problema, a edição ganha.

Este repositório aprendeu isso do jeito caro: chegou a ter nove tipos de
documento, um compilador e uma pilha de conjuntos construídos antes de existir
demanda, e tudo foi removido. Estrutura ou guarda nova entra com um caso
concreto que já tenha acontecido.

## Como rodar

```bash
uv run python scripts/derivar.py             # CSVs + índices + snapshot do site
uv run okf-parser check okf/regras-sisprev   # um bundle por vez
uv run python scripts/conferir_specs_dos_tipos.py    # todo type em uso tem spec
uv run python scripts/conferir_decisoes_da_spec.py   # dado confere com a decisão
uv run python scripts/testar_conferir_achados_append_only.py  # cenários do gate de achados
uv run python scripts/testar_carga_de_implantacao_bloco_c.py  # invariante da carga do Bloco C

cd site && npm install
npm run dev      # http://localhost:4321/sisprev/
npm run check    # astro check
npm run test     # vitest
npm run build    # -> site/dist/

uv run python scripts/gerar_relatorio_pdf.py   # exige npm run build antes
```

## O que existe

**`scripts/derivar.py`** é o único comando que escreve artefato derivado. Lê o
frontmatter e mais nada — a competência para achar erro de mérito é do auditor,
e um erro de mérito atravessa o script intacto. Produz o CSV legado, a carga de
implantação (`data/regras-propostas.csv`), as duas listagens que carregam
`nome` e o snapshot do site.

**A carga de implantação é derivada do grafo.** Quais regras propostas sobem
juntas no Sisprev é propriedade de `origens_legacy`: `derivar.py` calcula os
componentes conexos do grafo origem↔destino, um componente entra no CSV quando
todos os seus membros estão `estado_auditoria: concluida` e
`estado_implantacao: confirmada`, e cada exclusão sai como diagnóstico com o
motivo (`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada").

**`scripts/gerar_relatorio_pdf.py`** imprime o catálogo como documento único,
para a PGE juntar ao SEI. Roda sobre o `site/dist/` já buildado, via
WeasyPrint, porque três recursos de CSS Paged Media sustentam o documento
(`string-set` no cabeçalho de folha, `target-counter` no sumário,
`bookmark-level`). O `url_fetcher` **estoura** quando um recurso deixa de
resolver: um PDF sem folha de estilo sai legível e sem quebra de página, e o
defeito só apareceria com o anexo já no processo.

**`okf-parser`** faz o parsing e a conformidade OKF. É dependência. O leitor
preserva todo escalar como texto — `2026-07-30` continua string, `TRUE`
continua string —, e é isso que dá ao CSV derivado round-trip byte a byte com a
importação original.

**O site** (`site/`, Astro estático) lê os `.md` por content collections. A
ponte com o Python é `site/src/data/dados-do-site.json`: o SHA do commit e o
estado de auditoria indexado por id, sempre regenerado e sempre fora do git —
ele carrega o SHA do próprio commit que o geraria. O estado que ele mostra é
**o que está escrito no frontmatter**: selo errado se corrige no `.md`.

**O CI** (`.github/workflows/ci.yml`) é um job de guardas, cada uma comentada
com o incidente concreto que a motivou: bundles conformes, derivados em
sincronia, importação íntegra pelo manifesto, todo type com spec, decisões
declaradas conferidas contra o dado, achados append-only (comparados ao
merge-base com `main`, com cobertura de teste própria) e o invariante da carga
do Bloco C. Guarda nova entra pelo mesmo critério que a motivou todas: caso
concreto que já aconteceu.

## Os documentos

| tipo            | onde                           | quem lê                       |
| --------------- | ------------------------------ | ----------------------------- |
| `Regra`         | `okf/regras-sisprev/regras/`   | `derivar.py`, site, relatório |
| `Achado`        | `okf/regras-sisprev/achados/`  | `derivar.py`, site            |
| `Ciclo`         | `okf/regras-sisprev/ciclos/`   | site, relatório               |
| `RegraProposta` | `okf/regras-propostas/regras/` | `derivar.py`, site            |
| `Dispositivo`   | `okf/dispositivos/`            | site, relatório               |
| `Norma`         | `okf/dispositivos/*/norma.md`  | site                          |
| `TipoCalculo`   | `okf/tipos-calculo/`           | site, regras propostas        |

**`RegraProposta` carrega dois eixos independentes.** `estado_auditoria`
(`elaboracao`/`preview`/`concluida`) afirma a derivação jurídica: `concluida`
diz que a fórmula que a lei exige está determinada e representada.
`estado_implantacao` (`confirmada`/`pendente_mapeamento_sisprev`) afirma, à
parte, se o Sisprev reconhece a projeção sem ambiguidade. Uma unidade concluída
com implantação pendente continua concluída; o que a pendência segura é a
entrada do componente dela na carga.

**`TipoCalculo` é a fórmula juridicamente fundamentada** — base, ajustes e
limitadores, cada etapa com o dispositivo que a funda. `origem_legada` registra
o(s) rótulo(s) que o Sisprev grava para ela: o rótulo é projeção, a identidade
é a fórmula, e um mesmo rótulo legado serve a fórmulas distintas.

As specs em `okf/spec/` são a autoridade de cada tipo — inclusive dos
retirados, que ficam lá como nota histórica. Quando uma spec e o código
divergirem, **o código ganha**, e a divergência é ela própria algo a corrigir
na spec.

## O que já quebrou em silêncio

Cinco lições, todas de incidentes daqui.

**A cadeia do dispositivo.** Um dispositivo é a unidade endereçada *com toda a
cadeia que a contém*, na redação contemporânea a ela. Alterar um ancestral cria
redação nova — arquivo novo, fronteira de vigência nova — ainda que o inciso
continue idêntico, porque uma vigência que atravessa a alteração de um
ancestral monta texto que jamais esteve em vigor junto. Foi assim que
`art-40-par-1-inc-ii` ficou com vigência atravessando a EC 41/2003 enquanto o
irmão `inc-i` estava certo.

**Citação é vínculo autorado.** A entrada em `dispositivos:` nasce de um humano
que lê a fundamentação, confere contra a fonte e escreve o vínculo. O leitor
automático que já existiu produziu nove atribuições erradas — `C/C` (*combinado
com*) lido como inciso, dígitos de data lidos como artigo, uma emenda estadual
doando artigos à Constituição federal — todas parecendo citação bem formada. A
saída congelada dele virou lista de trabalho em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](docs/analysis/pendencias-de-citacao-congeladas.md).

**Conclusão jurídica é achado autorado.** "Esta redação nunca existiu", "estas
duas regras são a mesma" — conclusões assim vão escritas à mão num achado, com
autor e data, porque são acusações sobre campo que vai para produção. Detector
aponta ocorrência mecânica; quem conclui é o auditor. E achado, uma vez em
`main`, é permanente: o errado se marca `improcedente`, com justificativa
(`okf/spec/achado.md`), e o CI confere.

**As datas sentinela.** `01/01/1900`, `01/01/1910` e `01/01/1950` nas colunas
`_APOS`, e `31/12/2099` nas colunas `_ATE`, significam **ausência de limite
naquele eixo** — convenções de digitação diferentes para a mesma coisa,
declaradas em `site/src/lib/sentinela.ts`. Tratá-las como data real inverte o
critério (uma regra sem piso viraria exigência de ingresso depois de 1950), e
num anexo impresso `31/12/2099` pede ressalva, porque quem assina o lê como
fronteira de verdade. `01/01/1969` fica fora do conjunto por decisão registrada
(`regra-0003`): é suspeita de erro de digitação, e entrar no conjunto exige ato
de alguém.

**Derivado anda junto com a fonte.** Depois de editar qualquer `.md`, rode
`derivar.py` e comite o resultado — um CSV comitado que diverge do bundle
parece dado bom, e já ficou meses divergente antes de alguém notar.

## Antes de commitar

```bash
uv run ruff format --check && uv run ruff check
uv run mdformat --check --number okf docs README.md CLAUDE.md
uv run python scripts/conferir_specs_dos_tipos.py
uv run python scripts/conferir_decisoes_da_spec.py
uv run python scripts/testar_conferir_achados_append_only.py
uv run python scripts/testar_carga_de_implantacao_bloco_c.py
uv run python scripts/derivar.py
git status --porcelain data/regras-sisprev.csv data/regras-propostas.csv okf/regras-sisprev/*/index.md
```

Se mexeu no site ou no impresso, rode-os também — o CI de PR cobre `check` e
`test`; `build` e PDF rodam no push para `main`:

```bash
bash site/scripts/emit-data.sh && cd site && npm run check && npm run test && npm run build
cd .. && uv run python scripts/gerar_relatorio_pdf.py
```

## Convenções de escrita

- **Escreva a afirmação estrutural**, válida em qualquer commit. Contagens,
  estados momentâneos e vocabulário de instante ("hoje", "a única", "ainda")
  vivem na árvore e saem dos comandos — prosa que os repete envelhece no commit
  seguinte.
- **Exceção de lint mora no `pyproject.toml`**: regra do ruff que atrapalha o
  projeto é desligada lá, por inteiro e com o motivo escrito, onde todo mundo a
  vê. É o único lugar dela.
