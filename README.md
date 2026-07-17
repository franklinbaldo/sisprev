# sisprev

Auditoria e validação das regras de aposentadoria e pensão por morte do
Sisprev — o sistema de regime próprio de previdência de Rondônia — para que
cada regra possa ser aplicada no sistema com segurança jurídica.

## Objetivo

O Sisprev decide qual regra de aposentadoria ou pensão por morte se aplica a
cada servidor com base em uma tabela de 112 regras: cada uma define
elegibilidade (datas de admissão e de aquisição do direito, sexo), forma de
cálculo dos proventos (integral, por média, proporcional) e a fundamentação
legal correspondente.

Hoje, **as 112 regras já estão ativas no sistema** (`ATUALMENTE NO SISTEMA =
TRUE` em todas), mas **nenhuma delas concluiu o ciclo de validação jurídica**:
`VALIDADO PGE` e `VALIDADO PRESIDENCIA` são `FALSE` em 100% das linhas. As
regras estão organizadas em 4 ciclos de validação (`CICLO DE VALIDAÇÃO`,
coluna `1º` a `4º`) que definem a ordem de revisão.

Este repositório existe para fechar essa lacuna: transformar a planilha de
regras em algo que dê para **revisar regra por regra** — conferir se a
fundamentação legal citada está correta e atualizada, se a janela de
elegibilidade bate com a legislação, se o método de cálculo é o exigido —
e registrar o resultado dessa revisão de forma auditável (quem revisou, o
quê mudou, quando), até que cada regra tenha sido de fato validada pela PGE
e pela Presidência.

## Por que um bundle OKF, e não só a planilha

A planilha original (`data/raw/regras-sisprev.csv`) é a fonte de verdade, mas
não é um bom formato para auditoria: 112 linhas × 27 colunas em uma única
tabela larga, sem histórico linha-a-linha, sem como comentar uma regra
específica.

Este repo mantém a mesma informação também como um bundle [Open Knowledge
Format (OKF) v0.1][okf-spec] — um arquivo markdown por regra, com
metadados estruturados no frontmatter e a fundamentação legal em prosa no
corpo do documento. Isso dá:

- **Diff e histórico por regra**: cada alteração numa regra (e cada
  validação) vira um commit em `okf/regras-sisprev/regras/regra-NNNN.md`,
  revisável em Pull Request.
- **Revisão em paralelo**: cada regra é um arquivo — dá para distribuir a
  revisão das 112 regras entre pessoas/ciclos sem conflito.
- **Comentário e citação por regra**: PRs comentam a fundamentação de uma
  regra específica, linkam para o texto legal, sem afetar as outras 111.

A planilha e o bundle são **sempre mantidos em sincronia** pelos scripts de
conversão — nenhum dos dois é editado "à mão" sem regenerar o outro (ver
`CLAUDE.md`).

[okf-spec]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md

## Estrutura

```
data/raw/regras-sisprev.csv     # fonte de verdade (planilha original)
okf/regras-sisprev/
├── index.md                    # listagem raiz do bundle
├── regras-sisprev.md           # doc "Dataset": schema das 27 colunas + metadados
└── regras/
    ├── index.md                # listagem das 112 regras
    └── regra-0001.md ...       # uma regra por arquivo (frontmatter + fundamentação)
scripts/
├── csv_to_okf.py                # CSV -> bundle OKF
└── okf_to_csv.py                # bundle OKF -> CSV
```

Cada `regra-NNNN.md` traz no frontmatter: tipo de benefício, ciclo de
validação, status de validação (PGE/Presidência), elegibilidade (datas,
sexo), paridade, forma de cálculo etc. — e no corpo, a fundamentação legal
proporcional, integral e geral, prontas para conferência linha a linha
contra a legislação citada.

## Fluxo de trabalho de auditoria

1. Abra as regras de um ciclo (`CICLO DE VALIDAÇÃO`) em
   `okf/regras-sisprev/regras/` — comece pelo `1º`.
2. Para cada regra: confira a fundamentação legal citada contra o texto
   vigente da lei/emenda, confira se as datas de elegibilidade e o método
   de cálculo (`TIPO_CALCULO`) fazem sentido com essa fundamentação.
3. Registre o resultado da revisão (correções na fundamentação, ajuste de
   datas, ou confirmação) como uma alteração no `regra-NNNN.md`
   correspondente, em um PR.
4. Rode `uv run python scripts/okf_to_csv.py` para propagar a alteração de
   volta à planilha antes de commitar — CI falha se as duas ficarem
   dessincronizadas.
5. Quando uma regra estiver de fato aprovada pela PGE/Presidência fora
   deste repo, atualize `validado_pge` / `validado_presidencia` para
   `'TRUE'` na regra correspondente.

## Comandos

```bash
# planilha -> bundle OKF
uv run python scripts/csv_to_okf.py

# bundle OKF -> planilha
uv run python scripts/okf_to_csv.py

# testes (round-trip: CSV -> bundle -> CSV deve reproduzir os dados originais)
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
