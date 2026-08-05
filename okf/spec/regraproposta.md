---
type: Especificacao
id: regraproposta
nome: RegraProposta
---

# Regra proposta

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Uma **RegraProposta** é a regra corrigida: uma regra inteira, com nome,
parâmetros e fundamentação próprios, pronta para ocupar uma linha do Sisprev.

Ela vive num espaço de identidade próprio, fora da numeração do catálogo
recebido, porque o `regra-NNNN` é a linha que o sistema tem hoje — e corrigir
frequentemente **muda o número de regras**.

## Campos

| campo                                   | o que é                                                     |
| --------------------------------------- | ----------------------------------------------------------- |
| `id`                                    | casa com o nome do arquivo                                  |
| `estado_proposta`                       | `elaboracao`, `preview` ou `deployable`                     |
| `estado_implantacao`                    | opcional; `confirmada` ou `pendente_mapeamento_sisprev`     |
| `origens_legacy`                        | de que regras cadastradas ela descende                      |
| `predicados`                            | o que a unidade afirma sobre o caso, em vocabulário fechado |
| `requisitos_verificacao_humana`         | o que se afere, por quem, com que prova                     |
| `aplicabilidade_temporal.datas_legadas` | as quatro colunas de data                                   |
| `taxonomias`                            | os dispositivos articulados, com o papel de cada um         |
| `projecao`                              | as demais colunas do Sisprev, do jeito que entrariam        |
| `proveniencia`                          | fontes consultadas e notas                                  |
| `decisoes`                              | o registro datado de cada escolha, com autor                |
| `confianca`                             | o quanto a autoria se compromete com a unidade              |

## Por que as colunas moram em dois lugares

`projecao` traz a maioria e `aplicabilidade_temporal.datas_legadas` traz as de
data. Quem lê as colunas do Sisprev tem de reunir as duas: uma projeção sem as
janelas não permite conferir qual regra alcança um requerimento.

## `estado_proposta` não é o mesmo que pronto para o Sisprev

`deployable` afirma que a **derivação é a que a lei exige**: dispositivo,
requisitos, fórmula e representação estão determinados, e a unidade está
pronta para o catálogo auditado. Não afirma, por si só, que a coluna
`projecao.tipo_calculo` (ou outra coluna de vocabulário fechado) já identifica
univocamente essa fórmula no Sisprev em produção — essa é uma afirmação
diferente, sobre o sistema, não sobre a lei.

`estado_implantacao` carrega essa segunda afirmação, só quando ela precisa
ser feita separadamente da primeira. Ausente, presume-se `confirmada` — o caso
comum, em que o valor gravado já é aceito pelo Sisprev sem dúvida material.
`pendente_mapeamento_sisprev` diz que a fórmula está determinada, mas o valor
ou mecanismo que a identifica univocamente no Sisprev ainda depende de
confirmação do IPERON/fornecedor — sem reabrir a derivação jurídica.

Uma unidade `deployable` com `estado_implantacao: pendente_mapeamento_sisprev`
**não** ativa sozinha o grupo de substituição a que pertence para fins de
exportação: a seleção de origem única do exportador (RFC 0004 §1.5) substitui
as origens legadas **por inteiro**, e as origens legadas de um grupo tipicamente
cobrem, juntas, mais de uma hipótese — não há, em geral, como substituir
parcialmente sem deixar hipótese sem representação ou representada duas
vezes. Por isso `estado_grupo: ativo`, para o efeito de troca operacional de
fonte, continua exigindo `estado_implantacao: confirmada` em todos os
destinos, além de `deployable`. Isso não impede a auditoria de considerar a
regra concluída, nem o ciclo de considerar a derivação encerrada — impede
apenas a troca da fonte operacional de exportação.

## O que a unidade não decide

**Não se ativa sozinha.** `deployable` diz que a auditoria a considera pronta;
quem a põe no catálogo é o grupo de substituição, quando ativado.

**Não inventa valor de domínio fechado.** Onde a coluna do Sisprev tem
vocabulário do produto, a unidade grava o que o sistema já admite — tipicamente
o que a regra de origem grava. `estado_implantacao: pendente_mapeamento_sisprev`
existe exatamente para os casos em que esse "o que o sistema já admite" não
identifica, sozinho, a fórmula com precisão suficiente.
