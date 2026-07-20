# sisprev

Auditoria e validação das regras de aposentadoria e pensão por morte do
Sisprev — o sistema de regime próprio de previdência de Rondônia — para que
cada regra possa ser aplicada no sistema com segurança jurídica.

## Objetivo

O Sisprev decide qual regra de aposentadoria ou pensão por morte se aplica a
cada servidor com base numa tabela de regras: cada uma define elegibilidade
(datas de admissão e de aquisição do direito, sexo), forma de cálculo dos
proventos (integral, por média, proporcional) e a fundamentação legal
correspondente. O número de regras não é fixo — cresce e muda conforme
legislação nova é editada e regras antigas são revistas; o que é estrutural
é o próprio modelo: cada regra tem um `TIPO DE BENEFICIO`, um
`CICLO DE VALIDAÇÃO` (a ordem em que deve ser revisada) e dois sinalizadores
de validação jurídica, `VALIDADO PGE` e `VALIDADO PRESIDENCIA`.

Na última atualização da planilha (`data/raw/regras-sisprev.csv`), todas as
regras então cadastradas já estavam ativas no sistema
(`ATUALMENTE NO SISTEMA = TRUE`) mas nenhuma tinha concluído o ciclo de
validação jurídica (`VALIDADO PGE` e `VALIDADO PRESIDENCIA` ambos `FALSE`
em toda a tabela). Isso é o estado de um momento específico, não uma
característica do sistema — a proporção validada deve mudar à medida que
regras forem revisadas; **não assuma esses números sem reconferir a
planilha atual.**

Este repositório existe para fechar essa lacuna de validação: transformar a
planilha de regras em algo que dê para **revisar regra por regra** —
conferir se a fundamentação legal citada está correta e atualizada, se a
janela de elegibilidade bate com a legislação, se o método de cálculo é o
exigido — e registrar o resultado dessa revisão de forma auditável (quem
revisou, o quê mudou, quando), até que cada regra tenha sido de fato
validada pela PGE e pela Presidência.

## Por que um bundle OKF, e não só a planilha

A planilha original (`data/raw/regras-sisprev.csv`) é a fonte de verdade, mas
não é um bom formato para auditoria: dezenas de linhas × 27 colunas em uma
única tabela larga, sem histórico linha-a-linha, sem como comentar uma
regra específica.

Este repo mantém a mesma informação também como um bundle [Open Knowledge
Format (OKF) v0.1][okf-spec] — um arquivo markdown por regra. Toda a regra
(as 27 colunas do Sisprev, fundamentação legal inclusa) vive no **frontmatter**
— o frontmatter *é* a regra deployável, só com os campos que o Sisprev já tem.
O **corpo do markdown fica livre para a nossa análise da regra** (reconciliação,
dúvidas, notas de auditoria), nunca uma coluna do CSV. Isso dá:

- **Diff e histórico por regra**: cada alteração numa regra (e cada
  validação) vira um commit em `okf/regras-sisprev/regras/regra-NNNN.md`,
  revisável em Pull Request.
- **Revisão em paralelo**: cada regra é um arquivo — dá para distribuir a
  revisão entre pessoas/ciclos sem conflito, não importa quantas regras
  existam no momento.
- **Comentário e citação por regra**: PRs comentam a fundamentação de uma
  regra específica, linkam para o texto legal, sem afetar as demais.

**`data/raw/regras-sisprev.csv` é a importação original, congelada — nunca é
sobrescrita.** `csv_to_okf.py` só a lê, nunca escreve nela; nenhum script
tem permissão de gravar nesse caminho (`okf_to_csv.py` recusa com erro se
alguém tentar apontar `--out` para lá — ver `scripts/okf_common.py`). Ela
existe como a linha de base para auditoria: o estado exato em que as regras
foram recebidas, preservado para sempre.

A partir da importação inicial, **o bundle OKF é o registro vivo**: correções
de auditoria (fundamentação, datas, status de validação) são feitas
diretamente nos `regra-NNNN.md`, não na planilha. Se algum dia for preciso um
export plano (CSV) do estado atual do bundle — já revisado — para consumo
por outro sistema, `okf_to_csv.py` gera isso em `data/regras-sisprev.csv`
(fora de `data/raw/`), nunca substituindo o original.

## Estrutura

```
data/raw/regras-sisprev.csv     # importação original — SOMENTE LEITURA, nunca sobrescrita
data/regras-sisprev.csv         # export plano do estado ATUAL do bundle — commitado, conferido pelo CI a cada mudança
okf/regras-sisprev/
├── index.md                    # listagem raiz do bundle
├── regras-sisprev.md           # doc "Dataset": schema das 27 colunas + metadados
└── regras/
    ├── index.md                # listagem de todas as regras
    └── regra-0001.md ...       # uma regra por arquivo (frontmatter = a regra; corpo = análise) — registro vivo, editado durante a auditoria
scripts/
├── csv_to_okf.py                # data/raw/regras-sisprev.csv (só leitura) -> bundle OKF
└── okf_to_csv.py                # bundle OKF -> data/regras-sisprev.csv (nunca para data/raw/)
```

Cada `regra-NNNN.md` traz no frontmatter **todas** as colunas do Sisprev:
tipo de benefício, ciclo de validação, status de validação (PGE/Presidência),
elegibilidade (datas, sexo), paridade, forma de cálculo e a fundamentação
legal proporcional, integral e geral — o frontmatter é a regra deployável. O
corpo do markdown fica livre para a análise da regra durante a auditoria
(conferência da fundamentação contra a legislação, notas, dúvidas).

## Fluxo de trabalho de auditoria

**Mudanças são sempre feitas no `.md` da regra — nunca editando um CSV à
mão.** O CSV derivado (`data/regras-sisprev.csv`) é gerado por script a
partir do bundle, nunca o contrário.

1. Abra as regras de um ciclo (`CICLO DE VALIDAÇÃO`) em
   `okf/regras-sisprev/regras/` — comece pelo `1º`.
2. Para cada regra: confira a fundamentação legal citada contra o texto
   vigente da lei/emenda, confira se as datas de elegibilidade e o método
   de cálculo (`TIPO_CALCULO`) fazem sentido com essa fundamentação.
3. Registre o resultado da revisão (correções na fundamentação, ajuste de
   datas, ou confirmação) como uma alteração direta no `regra-NNNN.md`
   correspondente.
4. Rode `uv run python scripts/okf_to_csv.py` — isso regenera
   `data/regras-sisprev.csv` a partir do bundle atualizado. Commite o
   `.md` alterado **junto com** o `data/regras-sisprev.csv` regenerado no
   mesmo PR. Um teste (`tests/test_bundle_sync.py`) e o CI (`derived-csv-in-sync`)
   conferem que esse CSV bate exatamente com o conteúdo atual das regras —
   falham se alguém commitar só o `.md` e esquecer de regenerar o CSV, ou
   vice-versa.
5. Quando uma regra estiver de fato aprovada pela PGE/Presidência fora
   deste repo, atualize `validado_pge` / `validado_presidencia` para
   `'TRUE'` no `regra-NNNN.md` correspondente (e regenere o CSV, passo 4).

## Comandos

```bash
# bootstrap único (já feito) — planilha original -> bundle OKF
# NUNCA rode de novo depois que auditorias começarem: isso reescreve todo
# regra-*.md a partir do CSV congelado, descartando correções feitas desde então.
uv run python scripts/csv_to_okf.py

# fluxo normal, a cada edição de regra: bundle OKF -> data/regras-sisprev.csv
uv run python scripts/okf_to_csv.py

# testes (inclui: round-trip CSV->bundle->CSV, e bundle atual == CSV commitado)
uv run pytest -q
```

## Antes de commitar

```bash
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest -q
```

Veja `CLAUDE.md` para detalhes de arquitetura e as regras de manter CSV e
bundle sincronizados.

[okf-spec]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
