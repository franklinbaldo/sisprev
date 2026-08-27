---
type: Achado
id: achado-0061
nome: regra-0057 grava integral N mas fundamentacao_integral (a única preenchida) descreve proventos integrais
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0057.md
detectado_em: 2026-08-13
detectado_por: franklinbaldo
---

# Descrição

`regra-0057` grava `integral: N` (proporcional) e `paridade: N`, mas
`fundamentacao_proporcional` está **vazio** — só `fundamentacao_integral` tem
texto, e o texto começa "Aposentadoria especial de professor, **com proventos
integrais** (cálculo por média) e sem paridade". `regra-0058`, a irmã do
grupo (mesma janela, mesma `fundamentacao_integral`, `integral: S`), tem o
texto idêntico byte a byte.

Isso surgiu na conferência da Decisão 11
([`docs/analysis/decisoes-de-auditoria-2026-07-30.md`](../../../docs/analysis/decisoes-de-auditoria-2026-07-30.md)
§12): as duas regras passaram a diferir, depois de removida a faceta de sexo
do nome, **apenas** por `integral`/`proporcional`. Antes de aplicar a
unificação de nome que a mesma decisão orienta para pares assim, a conferência
achou que a fundamentação não sustenta a diferença — as duas regras citam a
mesma fundamentação integral.

# Evidências

| campo                                   | `regra-0057`                                                              | `regra-0058` |
| --------------------------------------- | ------------------------------------------------------------------------- | ------------ |
| `integral`                              | N                                                                         | S            |
| `fundamentacao_proporcional`            | `''` (vazio)                                                              | `''` (vazio) |
| `fundamentacao_integral`                | idêntica, "com proventos integrais (cálculo por média) e sem paridade..." | idêntica     |
| `tipo_calculo`                          | Valor Médio                                                               | Valor Médio  |
| `paridade`                              | N                                                                         | N            |
| janela (`data_adm_*`, `data_direito_*`) | idêntica                                                                  | idêntica     |

Não há, em nenhum dos dois registros, um texto de fundamentação proporcional
distinto que explique por que `regra-0057` seria a variante proporcional.

# Consequência prática

Duas leituras possíveis, e nenhuma das duas é gravável sem quem responde pelo
produto decidir:

1. `regra-0057.integral` está errado — deveria ser `S`, como a irmã, e as duas
   regras seriam materialmente idênticas (o que abriria, aí sim, um
   `P2_IGUALDADE_MATERIAL_ATIVA`, não coberto por este achado).
2. `regra-0057` é de fato a variante proporcional, e falta escrever
   `fundamentacao_proporcional` com o texto correto — o campo
   `fundamentacao_integral` estaria preenchido por engano.

Enquanto isso não é decidido, a unificação de nome que a Decisão 11 orienta
para pares "diferem só por integral/proporcional" **não foi aplicada** a este
par — unificar o nome esconderia a pergunta em vez de expô-la. O par segue com
`integral`/`proporcional` visível no nome até este achado ser disposto.

# Questão a investigar

Qual dos dois campos está errado — `integral` ou `fundamentacao_proporcional`
— é conferência de dispositivo (art. 5º, §§ 4º e 6º, II, e § 7º, II, da ECE
146/2021) contra o texto oficial, não decisão desta auditoria a chutar.

# Como a população respondeu

`regra-0057` respondeu `corrigida`. Conferido o art. 5º da ECE 146/2021
contra a transcrição oficial (`fontes-oficiais/transcricoes/sapl-emenda_146.md`):
o § 6º distingue **inciso I** (totalidade da remuneração) de **inciso II**
(média de 80% do período contributivo, "para o servidor público não
contemplado no inciso I") — as duas são bases de cálculo do provento
**pleno**, não uma redução proporcional por tempo incompleto; o § 7º só troca
a regra de reajuste (paridade no inciso I, RGPS no inciso II). A leitura 1 da
seção "Consequência prática" é a correta: `regra-0057.integral` estava
errado. Corrigido para `S`, igual à irmã.

**O achado permanece `aberto`.** Sob o modelo de estados do catálogo, um
defeito real não se fecha por selo no próprio achado — quem responde é a
regra, em `disposicao_de_achados`, e é ali que o tratamento fica registrado
com autor e data.

**A consequência que a seção "Consequência prática" previa se confirmou**: as
duas regras ficam materialmente idênticas em todo campo de critério aferido
exceto `sexo`, um `P2_IGUALDADE_MATERIAL_ATIVA` de fato. Este achado não o
resolve — registrado em [`achado-0062`](achado-0062.md), aberto, para quem
julgar o mérito do grupo (autonomia, consolidação N:1 ou revogação, Decisão
3). `nome` foi unificado por decorrência (Decisão 11, posição 5): a única
faceta que distinguia os dois nomes deixou de divergir.
