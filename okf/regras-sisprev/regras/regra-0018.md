---
type: Regra
id: regra-0018
row_index: 18
id_sisprev: '67'
nome_original: Pensão por Morte - Art. 46 da Lei Complementar 1.100/2021 - Paridade
nome: Pensão · óbito a partir de 01/01/2024, ingresso até 31/12/2003 · proporcional · Tipo Cálculo Nova Previdência Pensão por morte · paridade
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
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

# Estado da análise

Pensão por morte sob o **art. 46 da LCE 1.100/2021 com paridade** (`paridade: S`),
no regime de cotas: cota familiar de cinquenta por cento mais dez por cento por
dependente, sobre a remuneração ou proventos do instituidor. A regra é
`simulavel: N`, então a seleção depende de triagem humana pela fundamentação.

**Atualização de 2026-08-13: `regra-0016` e `regra-0017` foram corrigidas
para `sexo: AMBOS`**, igual a esta regra (`achado-0056`: nenhum dos onze
dispositivos citados diferencia por sexo). As três agora são materialmente
idênticas — mesmo `nome` (sem faceta de sexo), mesma fundamentação, mesmos
dispositivos, mesmo `sexo`. A questão sobre a que pessoa o campo `sexo` se
referia (beneficiário ou instituidor) deixa de importar pelo mesmo motivo.
O grupo é `P2_IGUALDADE_MATERIAL_ATIVA` de três candidatas idênticas, e o
desfecho já decidido é revogar `regra-0016`/`regra-0017` e manter esta —
ver os blocos `revogada` delas.

**`data_direito_apos: 01/01/2024` não tem fundamento conferido**, como nas outras
regras do art. 46.

Verificação humana que o cadastro não expressa: exame da portaria de aposentadoria
do instituidor comprovando a manutenção da paridade; validação da relação de
dependência previdenciária e do enquadramento do requerente; e apuração do número
de dependentes para a cota familiar, com a tabela de duração do benefício.
Documentos correspondentes: certidão de óbito, ato formal de concessão da
aposentadoria do instituidor com paridade, identidade civil do beneficiário e
prova de vínculo.

- [x] `paridade: S` é coerente com a hipótese de instituidor já aposentado com paridade, que é o que a fundamentação descreve
- [x] `regra-0016`/`regra-0017` corrigidas para `sexo: AMBOS`; as três agora idênticas em critério aferido — grupo `P2` resolvido por revogação das duas, não por esta regra
- [x] `nome` idêntico ao das irmãs, sem faceta de sexo — correto: nenhum critério aferido as distingue
- [ ] `data_direito_apos: 01/01/2024` não tem fundamento conferido perante a LCE 1.100/2021
- [ ] Os dispositivos declarados não foram conferidos um a um contra os campos de fundamentação
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
