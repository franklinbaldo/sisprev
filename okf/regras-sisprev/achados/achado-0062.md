---
type: Achado
id: achado-0062
nome: regra-0057 e regra-0058 tornam-se materialmente idênticas depois de corrigido integral em regra-0057
situacao: aberto
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0057.md
  - /regras/regra-0058.md
detectado_em: 2026-08-27
detectado_por: franklinbaldo
---

# Descrição

`achado-0061` registrou que `regra-0057` gravava `integral: N` com a mesma
`fundamentacao_integral` de `regra-0058` (`integral: S`), texto que descreve
"proventos integrais" — inconsistência de dado, não diferença de mérito.
Conferido o art. 5º, §§ 6º e 7º da ECE 146/2021 contra a transcrição oficial,
`regra-0057.integral` foi corrigido para `S`.

Com a correção, `regra-0057` e `regra-0058` ficam **materialmente idênticas**:
mesma janela (`data_adm_*`, `data_direito_*`), mesmo `tipo_calculo`, mesma
`paridade`, mesmo `integral`, mesma `fundamentacao_integral` e os mesmos
quatro `dispositivos`. Só o `sexo` diverge (`MASCULINO` × `FEMININO`), e a
grafia do nome já foi unificada (Decisão 11, posição 5) — o par entrou no
mesmo padrão que os grupos de sexo do `achado-0020`.

# Evidências

| campo                                   | `regra-0057` (corrigida) | `regra-0058`     |
| --------------------------------------- | ------------------------ | ---------------- |
| `integral`                              | S                        | S                |
| `tipo_calculo`                          | Valor Médio              | Valor Médio      |
| `paridade`                              | N                        | N                |
| `fundamentacao_integral`                | idêntica                 | idêntica         |
| `dispositivos`                          | os mesmos quatro         | os mesmos quatro |
| janela (`data_adm_*`, `data_direito_*`) | idêntica                 | idêntica         |
| `sexo`                                  | MASCULINO                | FEMININO         |

# Consequência prática

Este é um grupo `P2_IGUALDADE_MATERIAL_ATIVA` — duas regras cuja diferença
material se reduz a `sexo`, exatamente o padrão dos grupos que o
`achado-0020` já cataloga em outras famílias (ex.: `regra-0059`≡`regra-0063`
antes de diferenciadas por grau de deficiência). Por `achado-0056`,
sexo em benefício voluntário comum não costuma ser critério com lastro
específico no dispositivo citado — mas aqui os dispositivos (art. 5º, §§ 4º,
6º, II, e 7º, II, da ECE 146/2021, e art. 40, § 5º, da CF/88) fixam requisitos
"para ambos os sexos" apenas de forma implícita (o § 4º os expressa "se
mulher"/"se homem" separadamente para idade e tempo de contribuição, mas o
resultado do cálculo, aqui em disputa, não distingue sexo). Se sexo aqui é
critério com lastro (ex.: idade/tempo mínimos diferentes por sexo, já
capturados noutras colunas não expostas neste par) ou se é o mesmo padrão sem
lastro do `achado-0056` é conferência que este achado não resolve.

# Questão a investigar

Qual dos três desfechos da Decisão 3 (`docs/analysis/decisoes-de-auditoria-2026-07-30.md`)
— autonomia, consolidação N:1 ou revogação pura — resolve este grupo, e por
qual razão de mérito. Não decidido aqui: a correção de `achado-0061` só
resolveu a inconsistência de dado; a igualdade material resultante é mérito
novo, fora do escopo daquele achado.
