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

## O que a unidade não decide

**Não se ativa sozinha.** `deployable` diz que a auditoria a considera pronta;
quem a põe no catálogo é o grupo de substituição, quando ativado.

**Não inventa valor de domínio fechado.** Onde a coluna do Sisprev tem
vocabulário do produto, a unidade grava o que o sistema já admite — tipicamente
o que a regra de origem grava.
