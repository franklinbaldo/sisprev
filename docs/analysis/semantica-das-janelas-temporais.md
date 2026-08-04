# Varredura das datas do catálogo — 2026-08-01

> **Documento histórico.** Registra a medição feita nesta data e a fila de
> perguntas que ela abriu. **Não é fonte normativa**: a semântica das quatro
> fronteiras `DATA_*` está em
> [`okf/spec/janelas-temporais-regra.md`](../../okf/spec/janelas-temporais-regra.md),
> que é a autoridade do assunto. Se as duas divergirem, vale a spec, e a
> divergência é ela própria defeito a corrigir aqui.
>
> A versão anterior deste documento repetia a regra vigente e declarava
> superar leituras anteriores. Isso saiu: cada cópia de uma decisão é uma
> cópia sujeita a divergir, e a cláusula "este documento prevalece" é sinal de
> autoridade que não está representada — ver
> [`okf/spec/especificacao.md`](../../okf/spec/especificacao.md).

## O que foi medido

A varredura anterior encontrou os seguintes valores não coincidentes com os
marcos então autorados no bundle:

| valor        | ocorrências | onde                                                    |
| ------------ | ----------- | ------------------------------------------------------- |
| `31/12/2024` | 34          | `data_adm_ate` de 6 regras; `data_direito_ate` de 28    |
| `15/12/1998` | 6           | `data_adm_ate` e `data_direito_ate` de 0001, 0002, 0003 |
| `01/01/2004` | 6           | `data_adm_apos` de 0014, 0015, 0021, 0022, 0057, 0058   |
| `01/01/2024` | 5           | `data_direito_apos` de 0014–0018                        |
| `23/10/2021` | 4           | `data_direito_apos` de 0019–0022                        |
| `04/12/2015` | 2           | `data_direito_apos` de 0030, 0031                       |
| `14/06/2021` | 2           | `data_adm_ate` de 0049, 0050                            |
| `09/09/2021` | 2           | `data_adm_ate` de 0057, 0058                            |
| `01/01/1969` | 1           | `data_direito_apos` de 0003                             |
| `01/12/2002` | 1           | `data_direito_ate` de 0087                              |
| `03/12/2015` | 1           | `data_direito_ate` de 0027                              |

## Fila de conferência jurídica

As perguntas legítimas agora são concretas:

- qual dispositivo sustenta `23/10/2021` nas regras 0019–0022, se a LCE
  1.100/2021 começou a vigorar em 18/10/2021?;
- qual norma sustenta `01/01/2024` nas regras 0014–0018?;
- o que institui o prazo `31/12/2024`?;
- `15/12/1998`, `14/06/2021` e `09/09/2021` são erros de digitação ou marcos
  próprios?;
- `01/01/1969` é sentinela não catalogada ou data real?; e
- qual fonte explica `01/12/2002` na `regra-0087`?

Essas perguntas não reabrem a semântica de `APOS`. Elas pedem o fundamento de
um valor específico.

## O que esta varredura não decide

Nada sobre a semântica dos campos. Ela mede **valores gravados** e pergunta
pelo lastro de cada um; qual é a fronteira que cada coluna representa é
decisão da coordenação, e vive na spec.
