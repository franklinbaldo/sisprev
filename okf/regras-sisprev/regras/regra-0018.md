---
type: Regra
id: regra-0018
row_index: 18
nome: Pensão por Morte - Art. 46 da Lei Complementar 1.100/2021 - Paridade
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

**O que distingue esta regra das irmãs é apenas `sexo: AMBOS`.** A
`regra-0016` grava `MASCULINO`, a `regra-0017` `FEMININO` e a `regra-0018`
`AMBOS`, e as três carregam o **mesmo `nome`** e a mesma fundamentação. É o caso
(a) da RFC 0012 §3.5: renomear para que o nome carregue o `sexo` é **não
substancial** (a regra já aferia o campo; o rótulo é que não dizia), a autoridade
para a edição in loco é da auditoria, porque `nome` é o único campo deployável com
essa autorização expressa, e o efeito é o inverso do intuitivo — **dissolve** a
detecção `P1_NOME_REPETIDO` e por isso *libera* `revisada` em vez de travá-la.
Não renomeei nesta rodada: o nome é rótulo de seleção e a correção pede uma
formulação decidida para as três de uma vez, não três edições avulsas.

**A que sexo a chave se refere permanece hipótese.** O campo pode discriminar o
sexo do **beneficiário** ou o do **instituidor**, e a diferença é material numa
pensão. Nada no cadastro resolve, e a prosa da fundamentação não distingue.

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
- [ ] A que pessoa `sexo: AMBOS` se refere — beneficiário ou instituidor — é hipótese não confirmada, e a diferença é material
- [ ] `nome` idêntico ao das irmãs que diferem só em `sexo`: detecção `P1_NOME_REPETIDO` ativa, correção autorizada mas não feita nesta rodada
- [ ] `data_direito_apos: 01/01/2024` não tem fundamento conferido perante a LCE 1.100/2021
- [ ] Os dispositivos declarados não foram conferidos um a um contra os campos de fundamentação
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
