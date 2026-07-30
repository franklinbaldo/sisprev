---
type: Regra
id: regra-0071
row_index: 71
nome: Voluntária · Agentes nocivos · ingresso até 31/12/2003, pedido a partir de 18/10/2021 · Ambos · integral · Valor Médio
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por média) e sem paridade, com base nos artigos 24, 27, inciso II, e 41, inciso III, da Lei Complementar Estadual 1.100/2021 e artigo 40, § 1º, inciso III, segunda parte, e § 4°-C, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - regra permanente
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-24/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
---

# Estado da análise

Mesma hipótese material da `regra-0067` — art. 41, III da LCE 1.100/2021 — no
ramo **média sem paridade**: arts. 24 e 27, II da mesma lei. `tipo_calculo: Valor Médio` corresponde à média aritmética das 80% maiores remunerações do
art. 24 e `paridade: N` ao reajuste "nos termos estabelecidos para o RGPS" do
art. 27, II. `data_direito_apos: 18/10/2021` é o dia de vigência da LCE
1.100/2021 e segue a convenção do catálogo (19 regras gravam o mesmo valor).

O defeito é a **janela de admissão**, e é grave por ser exata: os arts. 24 e
27, II alcançam **apenas** quem ingressou *após* 31/12/2003, e a regra grava
`data_adm_ate: 31/12/2003` — o complemento exato. É a única regra do catálogo
que cita esses dois artigos e põe o marco no campo `ATE`; as irmãs
`regra-0080`/`0081` põem em `data_adm_apos`, que é a forma certa.

- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os cinco vínculos correspondem às cinco provisões citadas, nada a acrescentar nem a remover
- [x] Texto dos arts. 24, 27, II e 41, III conferido na compilação oficial (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`)
- [x] `paridade: N`, `integral: S` e `tipo_calculo: Valor Médio` conferidos contra os arts. 24 e 27, II: coerentes
- [x] `apos_especial: S` fundado no art. 41, III
- [x] `data_direito_apos: 18/10/2021` coincide com a vigência da LCE 1.100/2021 e com a convenção de 19 regras irmãs
- [ ] `data_adm_ate: 31/12/2003` é o complemento exato da população dos arts. 24 e 27, II: hoje a regra está fechada para quem ela deveria alcançar — `achado-0042`; campo deployável, decisão do dono
- [ ] Os 86 pontos e os 25 anos de exposição não têm coluna: mesma lacuna de schema da `regra-0067`, com `tabelapontuacao: N`
