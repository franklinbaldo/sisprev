---
type: Regra
id: regra-0032
row_index: 32
nome: Compulsória - Art. 40, §1º, II da CF com redaçao da EC 103/19 c/c art. 31 da Lc nº 1.100/2021
tipo_de_beneficio: APOSENTADORIA COMPULSÓRIA
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 2º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: Aposentadoria compulsória, com proventos proporcionais ao tempo de contribuição (média aritmética simples) e sem paridade, com base no artigo 40, § 1º, inciso II, da Constituição Federal, com redação dada pela Emenda Constitucional nº 88/2015; em conformidade com a Lei Complementar nº 152/2015, combinado com os artigos 17, 21, § 1º, 45 e 62 da Lei Complementar Estadual nº 432/2008, e com o artigo 4º da Emenda Constitucional Estadual nº 146/2021.
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Tipo Cálculo Nova Previdência
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-ii/ec-88-2015.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-21-par-1/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
---

# Estado da análise

Conferida contra a transcrição pesquisável da ECE 146/2021, na
[conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md) — que cobre as 24 regras que
vinculam esse dispositivo e é onde o raciocínio completo está.

Os requisitos desta regra vêm de art. 40, § 1º, II, da CF na redação da EC 88/2015, combinado com a LC 152/2015 — legislação **anterior** à ECE
146/2021. O art. 4º dessa emenda, que a regra invoca, é justamente o que
preserva aquela legislação, e preserva **com prazo**: os requisitos precisam
estar cumpridos até 31/12/2024. Sob a semântica que a Q1 fechou
(`DATA_DIREITO_ATE` é o prazo de implementação dos requisitos), a janela
deveria fechar em `31/12/2024`, e está gravada `31/12/2099`.

O `data_direito_apos: 18/10/2021` reforça a leitura: é a entrada em vigor da
ECE 146/2021, ou seja, o começo exato do período que o art. 4º garante. A
janela desta regra é esse período — e ele termina em 31/12/2024.

Tem, antes da janela, uma divergência interna: o `nome` a funda na EC 103/2019 e na LC 1.100/2021, a fundamentação na EC 88/2015 e na LC 152/2015 ([`achado-0023`](../achados/achado-0023.md)). Qual das duas vale decide se o problema é a janela ou a citação do art. 4º.

- [x] Fundamento dos requisitos identificado e conferido contra a transcrição oficial da ECE 146/2021
- [x] Art. 4º lido verbatim: o "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento dos requisitos
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
