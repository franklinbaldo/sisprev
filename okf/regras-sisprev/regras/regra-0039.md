---
type: Regra
id: regra-0039
row_index: 39
nome: Voluntária · Magistério · ingresso após 31/12/2003, pedido a partir de 18/10/2021 · Masculino · proporcional · Valor Médio
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
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 31/12/2003 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, §1º, inciso III, alínea “a” e §5º, da Constituição Federal, com redação dada pela Emenda Constitucional nº 20/1998, quanto ao preenchimento dos requisitos de aposentadoria; artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, no que tange à fórmula de cálculo e reajuste; artigos 24, 45 e 62 da Lei Complementar Estadual nº 432/2008, e no artigo 4º da Emenda Constitucional Estadual nº 146/2021.
visivel_dtc_integral: N
sexo: MASCULINO
integral: N
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-5/ec-20-1998.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-24/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
---

# Estado da análise

Conferida contra a transcrição pesquisável da ECE 146/2021, na
[conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md) — que cobre as 24 regras que
vinculam esse dispositivo e é onde o raciocínio completo está.

Os requisitos desta regra vêm de art. 40, § 1º, III, "a" e § 5º, da CF na redação da EC 20/1998 — legislação **anterior** à ECE
146/2021. O art. 4º dessa emenda, que a regra invoca, é justamente o que
preserva aquela legislação, e preserva **com prazo**: os requisitos precisam
estar cumpridos até 31/12/2024. Sob a semântica que a Q1 fechou
(`DATA_DIREITO_ATE` é o prazo de implementação dos requisitos), a janela
deveria fechar em `31/12/2024`, e está gravada `31/12/2099`.

O `data_direito_apos: 18/10/2021` reforça a leitura: é a entrada em vigor da
ECE 146/2021, ou seja, o começo exato do período que o art. 4º garante. A
janela desta regra é esse período — e ele termina em 31/12/2024.

É o caso mais explícito do grupo: a própria fundamentação separa os eixos — cita a EC 20/1998 "quanto ao preenchimento dos requisitos" e a EC 41/2003 "no que tange à fórmula de cálculo e reajuste". Requisitos por norma anterior à EC 146, com o art. 4º invocado.

- [x] Fundamento dos requisitos identificado e conferido contra a transcrição oficial da ECE 146/2021
- [x] Art. 4º lido verbatim: o "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento dos requisitos
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
