---
type: Especificacao
id: dataset
nome: Dataset
---

# Dataset

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Um **Dataset** é a declaração de identidade de um bundle importado: quantas
linhas a importação tinha, e portanto quantos documentos o bundle deve ter.

## Campos

| campo       | o que é                                       |
| ----------- | --------------------------------------------- |
| `id`        | casa com o nome do arquivo, na raiz do bundle |
| `row_count` | quantas linhas a importação trouxe            |

## Para que serve

`derivar.py` confere a identidade dos documentos contra ele: o `id` e o
`row_index` de cada documento têm de casar com o nome do arquivo, e o conjunto
dos `row_index` tem de ser exatamente `1..row_count`, sem buraco nem repetido.

Contar documentos não bastaria — dois arquivos podem somar o número certo e
apontar para a mesma linha da importação.
