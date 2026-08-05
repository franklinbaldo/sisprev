# CLAUDE.md

Núcleo invariante do repositório — o que vale em toda sessão, inclusive para
quem nunca abre um arquivo sob `okf/`. Regras por área vivem em
`.claude/rules/` (carregadas ao trabalhar nos caminhos que declaram) e em
`site/CLAUDE.md`; o contrato de cada tipo de documento está descrito na spec
dele em `okf/spec/` — mas, quando spec e código divergem, quem vale é o
código (ver "Decisões", abaixo), e a divergência é ela própria algo a
corrigir na spec.

**Automação não autora vínculo jurídico.** Um script, gate, extrator ou
parser pode apontar *ocorrência mecânica* — um padrão, uma inconsistência,
uma citação malformada —, nunca *concluir* que um dispositivo é o certo ou
que uma redação está errada: isso é autoria humana, registrada em
`dispositivos:` ou num achado. Vale para todo código que toque `okf/`, esteja
ele em `scripts/`, `.github/workflows/` ou em qualquer lugar novo que vier a
existir — o incidente que fundamenta isto (nove atribuições erradas por um
extrator automático) está em `.claude/rules/catalogo.md`.

## O que é

`sisprev` audita as regras de aposentadoria e pensão por morte do regime
próprio de previdência de Rondônia. Três lugares:

- **`data/raw/`** — a importação congelada, linha de base conferida pelo
  manifesto `SHA256SUMS`; muda por recebimento novo da fonte, ato humano que
  aparece no diff do manifesto.
- **`okf/`** — o registro vivo, onde se edita: catálogo legado
  (`regras-sisprev/`) e propostas (`regras-propostas/`), cujo frontmatter é o
  dado que vai para o Sisprev e o corpo é a análise do auditor; dispositivos
  legais (`dispositivos/`), fórmulas (`tipos-calculo/`) e specs (`spec/`),
  cujo conteúdo — normativo ou de contrato de tipo — não é regra individual e
  não vira dado direto de nenhuma linha do Sisprev.
- **`data/regras-sisprev.csv` e `data/regras-propostas.csv`** — derivados,
  regenerados por `scripts/derivar.py` e conferidos pelo CI contra o bundle.

O trabalho é conferir regras contra a lei, e ele é humano. Diante de um
problema, a pergunta é **"que edição num `.md` resolve isto?"** — entre uma
edição e uma estrutura nova, a edição ganha. Estrutura ou guarda nova entra
com um caso concreto que já tenha acontecido; o CI
(`.github/workflows/ci.yml`) documenta, guarda a guarda, o incidente que a
motivou.

## Comandos

```bash
uv run python scripts/derivar.py             # CSVs + índices + snapshot do site
for b in okf/*/; do uv run okf-parser check "$b"; done  # conformidade OKF, todo bundle
uv run python scripts/conferir_specs_dos_tipos.py    # todo type em uso tem spec
uv run python scripts/conferir_decisoes_da_spec.py   # dado confere com a decisão
uv run python scripts/testar_conferir_achados_append_only.py  # cenários do gate de achados
uv run python scripts/testar_carga_de_implantacao_bloco_c.py  # invariante da carga do Bloco C

cd site && npm install && npm run dev        # http://localhost:4321/sisprev/
uv run python scripts/gerar_relatorio_pdf.py # roda sobre site/dist já buildado
```

## Decisões que a árvore sozinha conta mal

- `derivar.py` é o único comando que escreve artefato derivado e lê só
  frontmatter — erro de mérito o atravessa intacto; mérito é do auditor.
- A carga de implantação (`data/regras-propostas.csv`) é **derivada**:
  componentes conexos do grafo `origens_legacy`, e um componente entra quando
  todos os membros estão `estado_auditoria: concluida` e
  `estado_implantacao: confirmada` (`okf/spec/regraproposta.md`). Cada
  exclusão sai como diagnóstico com o motivo.
- `RegraProposta` tem dois eixos independentes: `estado_auditoria` afirma a
  derivação jurídica; `estado_implantacao` afirma o reconhecimento pelo
  Sisprev. Unidade concluída com implantação pendente continua concluída.
- Em `TipoCalculo`, a identidade é a fórmula — base, ajustes e limitadores,
  cada etapa com dispositivo. O rótulo legado em `origem_legada` é projeção,
  e um mesmo rótulo serve a fórmulas distintas.
- `okf-parser` preserva todo escalar como texto (`TRUE` e datas continuam
  string) — é o que dá ao CSV round-trip byte a byte com a importação.
- Quando spec e código divergirem, **o código ganha** — e a divergência se
  corrige na spec.

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

## Critério de conclusão

Reproduz o que o CI aplica — não substitui o CI, é a base local que evita
descobrir a reprovação só lá. Uma mudança está concluída quando estes
comandos passam, e o encerramento informa quais rodaram e com que resultado:

```bash
uv run ruff format --check && uv run ruff check
uv run mdformat --check --number okf docs README.md CLAUDE.md site/CLAUDE.md .claude
for b in okf/*/; do uv run okf-parser check "$b"; done
uv run python scripts/conferir_specs_dos_tipos.py
uv run python scripts/conferir_decisoes_da_spec.py
uv run python scripts/testar_conferir_achados_append_only.py
uv run python scripts/testar_carga_de_implantacao_bloco_c.py
uv run python scripts/derivar.py
git status --porcelain data/regras-sisprev.csv data/regras-propostas.csv okf/regras-sisprev/*/index.md
```

Depois de editar algo sob `okf/regras-sisprev/**` ou
`okf/regras-propostas/regras/**` — os únicos caminhos que `derivar.py` lê —,
rode-o e leve o resultado no mesmo commit: derivado divergente do bundle
parece dado bom e já ficou meses sem ser notado. Editar `dispositivos/`,
`tipos-calculo/`, `spec/` ou fora de `okf/` não move nenhum derivado. Se
mexeu no site ou no impresso, rode também (`build` e PDF só rodam no CI em
push para `main`):

```bash
bash site/scripts/emit-data.sh && cd site && npm run check && npm run test && npm run build
cd .. && uv run python scripts/gerar_relatorio_pdf.py
```

## Convenções de escrita

- **Em documentação estrutural e nesta memória de projeto, escreva a
  afirmação estrutural**, válida em qualquer commit — contagens e vocabulário
  de instante ("hoje", "a única", "ainda") vivem na árvore e saem dos
  comandos. Não vale para relatório institucional versionado
  (`docs/analysis/`, laudos, matrizes de verificação): esses registram o
  fato de uma data — "38 regras aptas, duas pendentes" — e a contagem é o
  próprio conteúdo do documento, não vocabulário a evitar.
- **Exceção de lint mora no `pyproject.toml`**: regra do ruff que atrapalha é
  desligada lá, por inteiro e com o motivo escrito. É o único lugar dela.
