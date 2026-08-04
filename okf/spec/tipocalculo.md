---
type: Especificacao
id: tipocalculo
nome: TipoCalculo
---

# Tipo de cálculo

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Um **TipoCalculo** é um rótulo do domínio da coluna `TIPO_CALCULO` do Sisprev,
com o que ele designa.

## Campos

| campo  | o que é                         |
| ------ | ------------------------------- |
| `id`   | casa com o nome do arquivo      |
| `nome` | o rótulo como o sistema o grava |

## A premissa que atravessa o tipo

Que fórmula o sistema **implanta** para cada rótulo é comportamento do
programa, não do catálogo: a auditoria descreve a fórmula que entende
aplicável e declara a premissa de que o rótulo gravado é aquele pelo qual o
sistema a executa. Confirmar isso é providência do Instituto, e enquanto não
confirmada a premissa acompanha toda conclusão que dela dependa.
