---
type: Regra
id: regra-0096
row_index: 96
id_sisprev: '146'
nome: Voluntária · Magistério · ingresso até 31/12/2024, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Feminino · integral · média
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
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
data_adm_ate: 31/12/2024 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 40, § 5°, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigos 25, 27, I; 33, da Lei Complementar nº 1.100/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra permanente da aposentadoria especial de professor.
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-33/original.md
---

# Estado da análise

Ramo feminino do par cujo masculino é a `regra-0095`; as duas divergem **apenas
em `sexo`**, e toda a conferência da `regra-0095` se aplica sem alteração —
registrada aqui de propósito, e não por remissão, porque a lição do
`achado-0016` é que um defeito indiferente ao sexo é fácil de enxergar em
metade do par e perder na outra.

O `nome` anuncia a transição da alínea "a" do art. 40, § 1º, III da CF c/c o
art. 4º da ECE 146/2021, com "(Magistério)". A `fundamentacao_integral` e os
cinco vínculos são os da **regra permanente** do professor (§§ 5º e 1º, III da
CF na redação da EC 103/2019; arts. 25, 27, I e 33 da LCE 1.100/2021), e o
texto se autodenomina "regra permanente" — o que é incompatível com
`data_direito_ate: 31/12/2024`, prazo que vem do art. 4º e que só o `nome`
cita. As quatro datas são, valor por valor, as de `regra-0093`/`0094`.

E, independentemente disso, os arts. 25 e 27, I citados e vinculados determinam
totalidade da remuneração do cargo e reajuste paritário, contra `Valor Médio` e
`paridade: N` gravados.

- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os cinco vínculos espelham exatamente as cinco provisões citadas, nada a acrescentar nem a remover
- [x] Texto dos arts. 25, 27, I e 33 conferido na compilação oficial (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`); art. 7º da EC 41/2003 conferido na publicação do Planalto arquivada
- [x] `apos_especial: S` fundado no art. 33 da LCE 1.100/2021
- [x] `sexo: FEMININO` é a única divergência material com a `regra-0095`, e a redução de idade do art. 33 incide sobre idade que difere por sexo
- [ ] `nome` e fundamentação apontam para regras diferentes, ambas existentes no catálogo — `achado-0043`
- [ ] `paridade: N` contra o art. 27, I e `tipo_calculo: Valor Médio` contra o art. 25 — `achado-0043`
- [ ] `data_adm_ate: 31/12/2024` incompatível com o corte de ingresso até 31/12/2003 dos arts. 25 e 27, I — `achado-0043`
- [ ] `data_direito_apos: 31/12/2003` anterior à vigência dos cinco dispositivos citados — `achado-0043`
- [ ] Seis regras de professor sob uma citação, com três parametrizações — `achado-0043`, item 2; granularidade é escolha do IPERON
