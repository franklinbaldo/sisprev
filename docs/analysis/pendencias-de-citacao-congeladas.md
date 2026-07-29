# Pendências de citação, congeladas na remoção do leitor por regex

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. É a **última
> saída** do leitor de citações (`scripts/citacoes.py`) antes de ele ser
> removido do repositório, preservada como lista de trabalho autorada.

## Por que esta lista existe

O leitor de citações lia a prosa de `FUNDAMENTACAO*` com expressão regular
para descobrir quais dispositivos cada regra afirma citar. Ele foi removido
(RFC 0008): uma citação legal derivada de parse de prosa é uma acusação
plausível e não verificada, e nove misatribuições distintas foram encontradas
e corrigidas no tempo em que ele existiu — `C/C` (combinado com) lido como
inciso, dígitos de data virando artigos, emenda estadual doando artigos para a
Constituição Federal.

O que ele sabia, porém, é real: a lista do que ainda falta vincular. Apagar a
ferramenta sem preservar a lista perderia trabalho conhecido. Esta tabela é
essa lista, **congelada** — ela não se atualiza mais sozinha.

## O que isso significa na prática

**A lista não se regenera.** Se alguém editar uma `FUNDAMENTACAO*` daqui em
diante, esta tabela fica desatualizada e nada avisa. Isso é aceitável porque o
ponto de chegada da RFC 0008 é a fundamentação passar a ser **renderizada** a
partir de `dispositivos:` — quando isso acontecer, a divergência entre prosa e
vínculo deixa de ser possível. Entre hoje e lá, esta é uma janela real e está
registrada como tal.

**Nenhum item aqui é mecanicamente fechável.** A fila `VINCULAR` — a única que
o leitor resolvia sozinho — foi zerada antes da remoção: cinco vínculos em
`regra-0008`, `regra-0009`, `regra-0012`, `regra-0013` e `regra-0026`,
conferidos um a um contra a prosa da própria regra. O que sobrou exige leitura
humana com ou sem a ferramenta.

## As filas

| fila             | itens | o que exige                                                                                                                                        |
| ---------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ESTREITADA`     | 67    | nada — a prosa recorta a cláusula ("inciso III, *segunda parte*") e o vínculo é da provisão inteira. Registro da resolução perdida, não pendência. |
| `REDACAO`        | 19    | decisão sobre a citação: a provisão existe, a redação citada não. É o território do `achado-0012`.                                                 |
| `SEGMENTAR`      | 14    | separar à mão um campo que empacota mais de uma fundamentação com `\|`.                                                                            |
| `LEITURA-HUMANA` | 5     | a prosa não identifica a norma (`sem_norma`).                                                                                                      |
| `TRANSCREVER`    | 3     | o texto legal verbatim da provisão, que ninguém transcreveu.                                                                                       |

As três de `TRANSCREVER` são as únicas que destravam vínculo novo assim que o
texto for autorado:

- `ec-41-2003/art-6a-par-unico` — citado por `regra-0010`
- `lce-432-2008/art-39-par-unico` — citado por `regra-0061` e `regra-0062`

## A lista, item a item

| regra        | fila           | item                                        |
| ------------ | -------------- | ------------------------------------------- |
| `regra-0003` | REDACAO        | `cf88/art-40-par-5/original`                |
| `regra-0005` | REDACAO        | `cf88/art-40-par-7/ec-20-1998`              |
| `regra-0008` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0009` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0010` | TRANSCREVER    | `ec-41-2003/art-6a-par-unico`               |
| `regra-0012` | REDACAO        | `lce-432-2008/art-28-inc-i/lce-949-2017`    |
| `regra-0012` | REDACAO        | `lce-432-2008/art-30-inc-ii/lce-949-2017`   |
| `regra-0012` | REDACAO        | `lce-432-2008/art-31-par-1/lce-949-2017`    |
| `regra-0012` | REDACAO        | `lce-432-2008/art-31-par-2/lce-949-2017`    |
| `regra-0012` | REDACAO        | `lce-432-2008/art-32-inc-i/lce-949-2017`    |
| `regra-0012` | REDACAO        | `lce-432-2008/art-38/lce-949-2017`          |
| `regra-0012` | REDACAO        | `lce-432-2008/art-62/lce-949-2017`          |
| `regra-0013` | REDACAO        | `lce-432-2008/art-28-inc-i/lce-949-2017`    |
| `regra-0013` | REDACAO        | `lce-432-2008/art-30-inc-ii/lce-949-2017`   |
| `regra-0013` | REDACAO        | `lce-432-2008/art-31-par-1/lce-949-2017`    |
| `regra-0013` | REDACAO        | `lce-432-2008/art-31-par-2/lce-949-2017`    |
| `regra-0013` | REDACAO        | `lce-432-2008/art-32-inc-i/lce-949-2017`    |
| `regra-0013` | REDACAO        | `lce-432-2008/art-38/lce-949-2017`          |
| `regra-0013` | REDACAO        | `lce-432-2008/art-62/lce-949-2017`          |
| `regra-0021` | SEGMENTAR      | `cf88/art-40-par-1-inc-i`                   |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-25`                      |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-27-inc-i`                |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-30`                      |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-30-par-5`                |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-30-par-6`                |
| `regra-0021` | SEGMENTAR      | `lce-1100-2021/art-30-par-8`                |
| `regra-0022` | SEGMENTAR      | `cf88/art-40-par-1-inc-i`                   |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-25`                      |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-27-inc-i`                |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-30`                      |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-30-par-5`                |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-30-par-6`                |
| `regra-0022` | SEGMENTAR      | `lce-1100-2021/art-30-par-8`                |
| `regra-0025` | REDACAO        | `cf88/art-40-par-1-inc-ii/ec-20-1998`       |
| `regra-0028` | REDACAO        | `cf88/art-40-par-1-inc-ii/ec-41-2003`       |
| `regra-0029` | REDACAO        | `cf88/art-40-par-1-inc-ii/ec-41-2003`       |
| `regra-0033` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0034` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0037` | LEITURA-HUMANA | `sem_norma (1×)`                            |
| `regra-0039` | LEITURA-HUMANA | `sem_norma (2×)`                            |
| `regra-0040` | LEITURA-HUMANA | `sem_norma (2×)`                            |
| `regra-0041` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0042` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0043` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0044` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0047` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0048` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0051` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0052` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0055` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0056` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0059` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0060` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0061` | TRANSCREVER    | `lce-432-2008/art-39-par-unico`             |
| `regra-0061` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0062` | TRANSCREVER    | `lce-432-2008/art-39-par-unico`             |
| `regra-0062` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0063` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0064` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0065` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0065` | ESTREITADA     | `cf88/art-40-par-4c (segunda parte)`        |
| `regra-0066` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0066` | ESTREITADA     | `cf88/art-40-par-4c (segunda parte)`        |
| `regra-0067` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0067` | ESTREITADA     | `cf88/art-40-par-4c (segunda parte)`        |
| `regra-0071` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0071` | ESTREITADA     | `cf88/art-40-par-4c (segunda parte)`        |
| `regra-0072` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0073` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0074` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0075` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0076` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0077` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0078` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0079` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0080` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0080` | ESTREITADA     | `cf88/art-40-par-4b (segunda parte)`        |
| `regra-0081` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0081` | ESTREITADA     | `cf88/art-40-par-4b (segunda parte)`        |
| `regra-0082` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0082` | ESTREITADA     | `cf88/art-40-par-4b (segunda parte)`        |
| `regra-0083` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0083` | ESTREITADA     | `cf88/art-40-par-4b (segunda parte)`        |
| `regra-0084` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0085` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0086` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0091` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0092` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0093` | LEITURA-HUMANA | `sem_norma (3×)`                            |
| `regra-0094` | LEITURA-HUMANA | `sem_norma (3×)`                            |
| `regra-0095` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0096` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0097` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0098` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0099` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0100` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0101` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0102` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0103` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0104` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0105` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0106` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0107` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0108` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0109` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0110` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0111` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |
| `regra-0112` | ESTREITADA     | `cf88/art-40-par-1-inc-iii (segunda parte)` |

TOTAL 108 pendências em 74 regras
