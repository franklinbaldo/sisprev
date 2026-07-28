---
type: Regra
id: regra-0017
row_index: 17
nome: Pensão por Morte (LC 1.100/2021) - SEXO=FEMININO
tipo_de_beneficio: PENSÃO POR MORTE
status_operacional: 'TRUE'
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/2024 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Pensão mensal, com fundamento nos artigos 27, inciso I; 46, inciso I; 47, inciso I e II; 49; 50; 51, inciso I, II, III e VIII, alínea "c", todos da Lei Complementar Estadual nº 1.100/2021 e artigo 40, § 7º, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - pensão vitalícia e temporária
visivel_dtc_integral: N
sexo: FEMININO
integral: N
tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-7/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-46-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-47-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-47-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-49/original.md
  - /dispositivos/lce-1100-2021/art-50/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-iii/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-viii-al-c/original.md
---

# Pensão por Morte (LC 1.100/2021) - SEXO=FEMININO

# Critérios avaliados pelo Sisprev

- Parâmetro cadastral `status_operacional: 'TRUE'`.
- Parâmetro cadastral `simulavel: 'N'` (seleção não automatizada pelo motor).
- Parâmetro cadastral `sexo: 'FEMININO'` (predicado cadastral do sistema; a vinculação desta chave ao sexo do beneficiário vs. instituidor constitui hipótese a confirmar).
- Parâmetro cadastral `data_direito_apos: 01/01/2024` (dado cadastral importado; a razão do marco de 2024 perante a LCE nº 1.100/2021 permanece como questão investigativa pendente).

# Requisitos de verificação manual

- Exame probatório da portaria de aposentadoria do instituidor comprovando a manutenção da paridade constitucional.
- Validação documental da relação de dependência previdenciária e averiguação dos requisitos de enquadramento da requerente.
- Apuração do número de dependentes para cálculo da cota familiar e verificação da tabela de duração do benefício.

# Documentos ou evidências necessários

- Certidão de óbito do instituidor.
- Ato formal de concessão de aposentadoria do instituidor com paridade.
- Documento de identidade civil (RG e CPF) da beneficiária.
- Certidão de casamento, união estável ou nascimento comprovando o vínculo.

# Resultado após a seleção

- Concessão da pensão por morte calculada em cotas (50% de cota familiar + 10% por dependente) sobre a remuneração ou proventos do instituidor, assegurada a paridade constitucional de reajuste.
