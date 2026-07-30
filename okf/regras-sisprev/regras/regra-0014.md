---
type: Regra
id: regra-0014
row_index: 14
nome: Pensão · óbito a partir de 01/01/2024, ingresso após 01/01/2004 · Ambos · regra-0014
tipo_de_beneficio: PENSÃO POR MORTE
atualmente_no_sistema: 'TRUE'
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

# Estado da análise

Pensão por morte sob o **art. 46 da LCE 1.100/2021**, o regime de cotas: cota
familiar de cinquenta por cento mais dez por cento por dependente, até cem por
cento, calculada sobre os proventos ou sobre a aposentadoria por incapacidade a
que o servidor teria direito, com cotas extintas não reversíveis e reajuste sem
paridade — coerente com `paridade: N`, `integral: N` e
`tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte`. A regra é
`simulavel: N`.

**Esta regra e a `regra-0015` são materialmente idênticas** em todos os campos
de domínio, `nome` incluído, e declaram o mesmo conjunto de dispositivos — outro
grupo `P2_IGUALDADE_MATERIAL_ATIVA` sem campo distintivo, com a mesma leitura da
RFC 0012 §3.5: a distinção pretendida é pergunta ao IPERON, e nem diferenciar a
fundamentação nem inativar uma delas é decisão da auditoria.

**`data_direito_apos: 01/01/2024` não tem fundamento conferido.** A LCE 1.100/2021
é de 2021, e por que o direito só se abre em 2024 não decorre de nada que esteja
transcrito. O mesmo marco aparece nas cinco regras do art. 46
(`regra-0014` a `regra-0018`), o que sugere decisão de cadastro comum a elas e não
lapso isolado — mas sugerir não é conferir.

Verificação humana que o cadastro não expressa: validação da data do óbito e da
qualidade de segurado do instituidor; apuração do número de dependentes
concorrentes, que é o que fixa a cota familiar e as cotas individuais; e aplicação
da tabela de duração do benefício para cônjuge ou companheiro conforme a idade na
data do óbito. Documentos correspondentes: certidão de óbito, prova de dependência
(casamento, união estável ou nascimento), laudo pericial oficial quando houver
dependente inválido ou com deficiência, e o extrato da remuneração do cargo
efetivo ou dos proventos do instituidor.

- [x] O regime de cotas descrito é coerente com `paridade: N`, `integral: N` e o `tipo_calculo` gravado
- [ ] `data_direito_apos: 01/01/2024` não tem fundamento conferido perante a LCE 1.100/2021
- [ ] A identidade material com a `regra-0015` não está resolvida — pergunta ao IPERON (achados `achado-0001`/`achado-0002`, abertos)
- [ ] Os dispositivos declarados não foram conferidos um a um contra os campos de fundamentação
- [ ] A tabela de duração por idade do art. 46 não foi transcrita, logo não há a que conferir a aplicação
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
