---
type: Regra
id: regra-0067
row_index: 67
nome: Voluntária · Agentes nocivos · pedido a partir de 31/12/2003 · Ambos · integral · paridade · regra-0067
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por integralidade) e com paridade, com base nos artigos 25, 27, inciso I, e 41, inciso III, da Lei Complementar Estadual 1.100/2021 e artigo 40, § 1º, inciso III, segunda parte, e § 4°-C, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - regra permanente
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Efetivo
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
---

# Estado da análise

Regra permanente de agentes nocivos do art. 41, III da LCE 1.100/2021 (86
pontos e 25 anos de efetiva exposição), no ramo **integralidade + paridade**:
arts. 25 e 27, I da mesma lei. `paridade: S` corresponde ao reajuste do art.
27, I, que remete ao art. 7º da EC 41/2003. `Valor Médio` está descartado para
esse ramo, mas `tipo_calculo: Valor Efetivo` ainda é hipótese: o catálogo usa
também `Remuneração de Contribuição` para a totalidade da remuneração do art.
25, e as fórmulas dos dois códigos não estão documentadas.

O que não fecha são as **janelas**. Os arts. 25 e 27, I exigem ingresso *até*
31/12/2003 e a regra não grava corte de admissão nenhum; e
`data_direito_apos: 31/12/2003` é dezesseis anos anterior ao § 4º-C da CF (EC
103/2019), que é a autorização constitucional do benefício, e dezoito anterior
à lei estadual que o exerce. Detalhe: nenhum critério que decide o caso — os 86
pontos e os 25 anos de exposição — tem coluna no legado. O modelo auditado
passou a carregá-lo em `predicados.faixa_exposicao`. `tabelapontuacao: N` é
coerente com faixa fixa; o `S` das gêmeas do art. 8º da ECE 146/2021
(`0068`–`0070`) é o candidato a correção.

- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os cinco vínculos correspondem às cinco provisões citadas, nada a acrescentar nem a remover
- [x] Texto dos arts. 25, 27, I e 41, III conferido na compilação oficial (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`)
- [x] `paridade: S` e `integral: S` conferidos contra os arts. 25 e 27, I; `tipo_calculo: Valor Efetivo` permanece hipótese operacional, porque o catálogo também usa `Remuneração de Contribuição` para o mesmo comando
- [x] `apos_especial: S` fundado no art. 41, III, que é dispositivo de aposentadoria especial e nomeia a efetiva exposição a agentes nocivos
- [ ] Janela de admissão sem o corte de 31/12/2003 que os arts. 25 e 27, I exigem — `achado-0042`; campo deployável, decisão do dono
- [ ] `data_direito_apos: 31/12/2003` anterior à vigência de todos os cinco dispositivos citados — `achado-0042`
- [x] A faixa 86/25 não tem coluna no legado, mas foi explicitada como `predicados.faixa_exposicao` e completada com unidades próprias para os incisos I e II no modelo auditado
- [x] `tabelapontuacao: N` coerente com faixa fixa; o corpus reserva `S` às tabelas com progressão anual — `achado-0054`
- [ ] `Valor Efetivo` × `Remuneração de Contribuição`: seis irmãs citam o mesmo art. 25 e gravam o segundo valor. Se os dois membros do enum não são sinônimos, uma das duas famílias calcula errado (Q6)
