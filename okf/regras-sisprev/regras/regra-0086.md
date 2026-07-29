---
type: Regra
id: regra-0086
row_index: 86
nome: Voluntária por Idade e Temp. de Contrib.- Art. 3º da EC 47/05 - FÓRMULA 85/95 e art. 4º da EC nº 146/21
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_ate: 16/12/1998 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/1950 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 3º da Emenda Constitucional nº 47/2005, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-47-2005/art-3/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Conferida contra a transcrição pesquisável da ECE 146/2021, na
[conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md) — que cobre as 24 regras que
vinculam esse dispositivo e é onde o raciocínio completo está.

**Direito adquirido puro, e a janela está certa.** `data_adm_ate: 16/12/1998`:
os requisitos foram completados sob a redação original da CF/88, antes da EC
20/1998. Um direito já adquirido em 1998 não é alcançado por prazo criado em
2021 — satisfaz trivialmente o "até 31/12/2024" do art. 4º da ECE 146/2021 e
não depende dele. A sentinela `31/12/2099` em `data_direito_ate` está adequada.

O que sobra é a **citação do art. 4º, que não funda critério algum aqui**. Vale
registrar a distinção, porque ela é fina: `regra-0097`–`0100` também têm
`data_adm_ate: 16/12/1998` e **fecham** em 31/12/2024 — mas são regra de
*transição* (art. 2º da EC 41/2003), não direito adquirido. Transição depende
do prazo; direito adquirido, não.

- [x] Janela conferida contra o art. 4º da ECE 146/2021: `31/12/2099` está correto, por ser direito adquirido anterior à EC 20/1998
- [x] Distinção com as regras de transição da EC 41/2003 (`0097`–`0100`), que fecham em 31/12/2024, verificada
- [ ] O art. 4º da ECE 146/2021 é citado sem fundar critério representado nas colunas. Decisão do dono do campo, não do auditor
