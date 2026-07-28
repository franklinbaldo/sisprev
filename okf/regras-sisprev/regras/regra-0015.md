---
type: Regra
id: regra-0015
row_index: 15
nome: Pensão por Morte (LC 1.100/2021) - Registro Duplicado
tipo_de_beneficio: PENSÃO POR MORTE
status_operacional: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/2004 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/2024 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Pensão mensal, com fundamento nos artigos 27, inciso I; 46, inciso I; 47, inciso I e II; 49; 50; 51, inciso I, II, III e VIII, alínea "c", todos da Lei Complementar Estadual nº 1.100/2021 e artigo 40, § 7º, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - pensão vitalícia e temporária
visivel_dtc_integral: N
sexo: AMBOS
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

# Pensão por Morte (LC 1.100/2021) - Registro Duplicado

# Critérios avaliados pelo Sisprev

- Parâmetro cadastral `status_operacional: 'TRUE'`.
- Parâmetro cadastral `data_direito_apos: 01/01/2024` (preservando o parâmetro do Sisprev antigo; a semântica e a justificativa deste marco frente à vigência da LCE nº 1.100/2021 em 18/10/2021 constituem questão investigativa pendente).
- Registro de dependente habilitado cadastrado no sistema.

# Requisitos de verificação manual

- Validação documental da data do óbito e confirmação da qualidade de segurado do instituidor.
- Apuração probatória do número de dependentes concorrentes para fixação da cota familiar global e cotas individuais.
- Aplicação da tabela de duração do benefício para cônjuge/companheiro(a) de acordo com a idade na data do óbito.

# Documentos ou evidências necessários

- Certidão de óbito do instituidor.
- Documentação de comprovação de dependência (certidão de casamento, união estável ou nascimento).
- Laudo pericial médico oficial em caso de dependentes inválidos ou com deficiência.
- Extrato da remuneração do cargo efetivo ou dos proventos de aposentadoria do instituidor.

# Resultado após a seleção

- Concessão de pensão por morte calculada em cotas (50% de cota familiar + 10% por dependente, até 100%) sobre os proventos ou aposentadoria por incapacidade que o servidor teria direito, com não-reversibilidade das cotas extintas e reajuste sem paridade.
