---
type: Especificacao
id: achado
nome: Achado
---

# Achado

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Um **Achado** é uma acusação datada sobre regras nomeadas. Ele não corrige
nada: aponta um defeito, diz quem o levantou e quando, e fica no repositório
mesmo depois de resolvido.

## Campos

| campo                           | o que é                                              |
| ------------------------------- | ---------------------------------------------------- |
| `id`                            | `achado-NNNN`, e casa com o nome do arquivo          |
| `nome`                          | o defeito dito numa linha, não um rótulo             |
| `situacao`                      | `aberto`, `resolvido` ou `improcedente`              |
| `severidade`                    | `bloqueante` ou `informativo`                        |
| `verificacao`                   | `mecanica`, `manual` ou `hibrida`                    |
| `natureza`                      | `juridica`, `dados`, `modelagem` ou `processo`       |
| `regras_afetadas`               | refs `/regras/regra-NNNN.md`, ao menos uma           |
| `detectado_em`, `detectado_por` | data e autor da acusação                             |
| `deteccoes`                     | detector e fingerprint, quando houve origem mecânica |
| `resolvido_em`, `resolvido_por` | preenchidos ao fechar                                |
| `efeito_deteccao`               | `deve_desaparecer` ou `pode_persistir`               |

## O que não acontece com um achado

**Não se apaga e não se renumera.** Outros documentos o citam pelo id, e
apagá-lo reescreve o passado da auditoria deixando citação apontando para
coisa nenhuma. Achado errado se marca `improcedente`, com justificativa. O CI
confere isso: id de achado é append-only.

**Não se fecha por inferência.** Quem dispõe de um achado é a regra que ele
nomeia, em `disposicao_de_achados`, com justificativa autorada. Um detector
que pare de acusar não fecha achado: `efeito_deteccao` existe para dizer se a
ocorrência mecânica deveria mesmo sumir.
