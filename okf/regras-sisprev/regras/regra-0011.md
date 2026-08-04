---
type: Regra
id: regra-0011
row_index: 11
id_sisprev: '60'
nome_original: Pensão por Morte oriunda do Art. 3º da Emenda Constitucional nº 47/2005 c/c art. 4º da EC nº 146/2021
nome: Pensão · óbito a partir de 31/12/2003 e antes de 31/12/2024 · integral · Valor Efetivo mais 70% do que exceder do Teto RGPS · paridade
tipo_de_beneficio: PENSÃO POR MORTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: art. 40, § 7, I da CF/88 com redação da EC 41/2003 c/c art. 3º, § único da EC 47/2005
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-7-inc-i/ec-41-2003.md
  - /dispositivos/ec-47-2005/art-3-par-unico/original.md
---

# Estado da análise

Pensão por morte derivada da aposentadoria voluntária do art. 3º da EC 47/2005 —
a "fórmula 85/95". O instituidor tinha de ter ingressado no serviço público até
16/12/1998 e aposentado-se por aquele artigo; a pensão herda o critério de
revisão do art. 7º da EC 41/2003 por força do parágrafo único, que é o
dispositivo efetivamente vinculado.

Dois valores conferidos e corretos. `paridade: S` decorre do parágrafo único, que
manda aplicar o art. 7º da EC 41/2003 "observando-se igual critério de revisão às
pensões derivadas dos proventos de servidores falecidos que tenham se aposentado
em conformidade com este artigo". E citar **apenas** o inciso I do § 7º do art.
40 (óbito com o servidor já aposentado) é coerente com o art. 3º ser regra de
aposentadoria voluntária: o instituidor necessariamente já estava aposentado.
Pelo mesmo motivo a `fundamentacao_proporcional` vazia está certa.

O defeito está no corte de ingresso, e ele é do tipo que o catálogo mesmo
denuncia: as duas regras de aposentadoria do mesmo art. 3º (`regra-0085`,
`regra-0086`) gravam `data_adm_ate: 16/12/1998`, e esta grava a sentinela
`31/12/2099`. A pensão vizinha `regra-0010` também grava o corte do seu próprio
fundamento, o que mostra que o campo tem esse uso em pensão por morte.

- [x] `paridade: S` conferido contra o § único do art. 3º da EC 47/2005 (texto transcrito em `okf/dispositivos/ec-47-2005/art-3-par-unico/original.md`)
- [x] Citar só o inciso I do art. 40, § 7º conferido e correto — o art. 3º é aposentadoria voluntária, logo o instituidor estava aposentado ao óbito; `fundamentacao_proporcional` vazia é consequência
- [x] `dispositivos:` conferido contra `fundamentacao_integral`: os dois vínculos correspondem ao que o campo cita, nada a acrescentar nem a remover
- [ ] `data_adm_ate: 31/12/2099` não grava o corte de ingresso de 16/12/1998 que o art. 3º exige e que as três regras irmãs gravam ([`achado-0048`](../achados/achado-0048.md)). Apertar a janela retira elegibilidade hoje admitida: decisão do dono do campo
- [ ] `data_direito_ate: 31/12/2024` é o prazo do art. 4º da ECE 146/2021, citado **apenas no `nome`** — nenhum campo de fundamentação o carrega ([`achado-0047`](../achados/achado-0047.md))
- [ ] A janela `[31/12/2003, 31/12/2024)` ultrapassa em cinco anos o fim da redação citada do art. 40, § 7º, I (12/11/2019); só o resguardo do art. 4º legitima, e ele não está na fundamentação
- [ ] Se a data correta é 16/12/1998 ou 15/12/1998 — a convenção semiaberta `[apos, ate)` do catálogo exclui o próprio dia do marco, e o artigo diz "até 16 de dezembro". Depende do [`achado-0015`](../achados/achado-0015.md), que não fecha essa questão
