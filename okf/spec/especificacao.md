---
type: Especificacao
id: especificacao
nome: Especificação
---

# Especificação

Uma **Especificação** é a autoridade única sobre um assunto do catálogo: o que
um campo significa, como se preenche, que decisão da coordenação vale sobre
ele. Cada uma ocupa um arquivo, e o caminho do arquivo é a sua identidade.

Este documento é a especificação das especificações, e por isso se refere a si
mesmo no `type`. A raiz fecha em si em vez de precisar de um caso especial.

## Uma autoridade por assunto

O assunto pertence a **um** documento. Os demais — análise em
`docs/analysis/`, achado, RFC, comentário de PR — registram o que foi pensado,
observado ou decidido **naquela data**, e não repetem a regra vigente.

A diferença é de tempo verbal, e ela é o ponto todo:

- a especificação diz **o que vale**;
- o documento histórico diz **o que se pensou**, e quando.

Documento histórico não precisa ser reescrito quando a decisão muda. É por
isso que ele não pode carregar a regra: cada cópia é uma cópia sujeita a
divergir, e quem divergisse teria dois documentos vigentes com igual apoio.

## Cláusula de precedência é cheiro de estrutura faltando

Um documento que precisa **declarar em prosa** que prevalece sobre outro está
compensando uma autoridade que não está representada. Enquanto a autoridade
for uma frase, ela depende de quem a lê primeiro — e foi assim que a leitura
de `DATA_ADM_APOS` chegou a existir em quatro documentos ao mesmo tempo, cada
um se dizendo posterior aos outros.

A representação estrutural é a referência: um documento aponta para a
especificação do seu assunto, e a autoridade deixa de ser afirmada para ser
**seguida**.

## Revisão

Reabrir um ponto fechado exige proposta expressa de revisão, com evidência
nova e identificação do que cai junto. A revisão se escreve **na própria
especificação**, datada, com o que ela substitui e o que ela deliberadamente
não alcança — nunca num documento paralelo que passe a concorrer com ela.

## O que uma especificação não é

Não é ato do IPERON, não interpreta lei e não conclui sobre regra alguma. Ela
fixa o significado do campo e o modo de preenchê-lo; se o valor gravado numa
regra específica está correto é conferência de auditoria, e essa é humana.
