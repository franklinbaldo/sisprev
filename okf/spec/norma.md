---
type: Especificacao
id: norma
nome: Norma
---

# Norma

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Uma **Norma** é o vocabulário fechado das leis citáveis. Cada `norma.md` guarda
o nome canônico e as URLs oficiais contra as quais uma transcrição se confere —
uma vez, em vez do mesmo nome redigitado em cada dispositivo.

## Campos

| campo     | o que é                                                   |
| --------- | --------------------------------------------------------- |
| `id`      | o diretório da norma em `okf/dispositivos/`, `[a-z0-9-]+` |
| `nome`    | o nome canônico, por extenso                              |
| `apelido` | a forma curta usada em citação corrida                    |
| `fontes`  | URLs oficiais, ao menos uma                               |

## Por que existe separada do dispositivo

Um dispositivo é a unidade endereçada; a norma é a lei que o contém. Sem esta
separação, o nome da lei seria redigitado em cada uma das centenas de
transcrições — e divergiria na primeira correção que alcançasse só metade.
