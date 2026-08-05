---
type: Especificacao
id: conjunto
nome: Conjunto
---

# Conjunto

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Um **Conjunto** é uma composição do catálogo: que regras valem juntas. É a
unidade que responde "o que iria para o sistema se isto fosse ativado".

## Campos

| campo           | o que é                                                                            |
| --------------- | ---------------------------------------------------------------------------------- |
| `id`            | casa com o nome do arquivo                                                         |
| `nome`          | a composição dita a quem decide sobre ela                                          |
| `situacao`      | `vigente` ou `proposto`                                                            |
| `base`          | o conjunto de que este deriva, se houver                                           |
| `substituicoes` | os grupos de substituição declarados, cada um com sua `decisao_completude` própria |

## O grupo de substituição

Cada item de `substituicoes` traz `grupo`, `origens_legacy`,
`destinos_propostos`, `decisao_completude` e `estado_grupo` (`ativo` ou
`inativo`). Origens e destinos são **refs de caminho**, e quem as lê
converte em id — o documento que circula nunca imprime a ref.

O grupo é a unidade de decisão: **ativa e reverte inteiro**. Aprovar metade
deixaria hipótese sem representação ou representada duas vezes.

## Decisão jurídica e prontidão operacional são campos distintos

`decisao_completude` (`decidido_por`/`decidido_em`/`justificativa`/`fonte`)
é a decisão da auditoria de que a substituição — quais regras cadastradas
saem, quais regras propostas entram — está correta e completa. É
independente de `estado_grupo`: fica preenchida sempre que essa decisão
existir, e não é zerada só porque o grupo está `inativo`. Só é retirada
(com o registro do motivo) quando a própria decisão jurídica é revista —
não quando falta mapeamento de implantação num dos destinos.

`estado_grupo` não é decidido à parte: é **computado** a partir de
`decisao_completude` e do estado dos destinos. `ativo` se e somente se
`decisao_completude` está preenchida **e** todos os destinos estão
`estado_proposta: deployable` **e** todos têm `estado_implantacao: confirmada` (ver `okf/spec/regraproposta.md`) — porque trocar a fonte
operacional do grupo antes de todos os destinos estarem implantáveis
reproduz o mesmo risco de cobertura parcial que a atomicidade do grupo
existe para evitar. Em qualquer outro caso, `inativo` — e a presença ou
ausência de `decisao_completude` é o que distingue, sem precisar de prosa,
"juridicamente não decidido" de "juridicamente decidido, implantação
pendente".

## A cadeia de bases

Um conjunto de fechamento tipicamente não declara delta próprio: ele
consolida o que as sessões anteriores decidiram, e quem quer os grupos dele
percorre a cadeia de `base`. Ler só o delta devolve zero e se lê como "este
ciclo não substituiu nada".

## O que uma composição não faz

Não desativa regra por marca gravada nela. Uma regra de origem sai do
catálogo pela **ativação do grupo** que a substitui; o frontmatter dela não
muda, e é por isso que introduzir um conjunto é no-op demonstrável.
