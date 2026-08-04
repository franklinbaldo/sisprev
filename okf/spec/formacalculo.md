---
type: Especificacao
id: formacalculo
nome: FormaCalculo
---

# Forma de cálculo

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Uma **FormaCalculo** é a fórmula do provento descrita juridicamente: qual é a
base, o que a proporcionaliza, que limites incidem e em que dispositivos cada
passo se funda.

## Campos

| campo  | o que é                    |
| ------ | -------------------------- |
| `id`   | casa com o nome do arquivo |
| `nome` | a fórmula dita numa linha  |

O corpo é autorado e não tem forma fixa: ele descreve a fórmula e cita os
dispositivos que a sustentam.

## O que uma forma de cálculo não é

**Não é implementação.** Ela descreve juridicamente o cálculo; fazê-lo operar
no sistema é providência técnica do Instituto, e a distância entre as duas
coisas é justamente o que a homologação confere.

**Não é o `tipo_calculo` do Sisprev.** Aquele é o rótulo que o sistema grava
na coluna — ver [tipocalculo.md](tipocalculo.md).
