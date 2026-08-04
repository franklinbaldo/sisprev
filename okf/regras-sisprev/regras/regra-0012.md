---
type: Regra
id: regra-0012
row_index: 12
id_sisprev: '61'
nome_original: Pensão Morte Art. 40, §7 da EC 41/2003 e Art.28 da LC 432/2008 e alterações da LC 949/2017 e Art.4º da ECE 146/2021
nome: Pensão · óbito a partir de 31/12/2003 e antes de 31/12/2024 · integral · Valor Efetivo mais 70% do que exceder do Teto RGPS · regra-0012
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
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Pensão mensal, com fundamento nos artigos 10, I; 28, I; 30, II; 31, §§ 1º e 2º; 32, I e II, “a”, e § 1º; 33; 34, I a III, e § 2º; 38; e 62 da Lei Complementar Estadual nº 432/2008, com redação dada pela Lei Complementar Estadual nº 949/2017, bem como no artigo 4º da Emenda Constitucional Estadual nº 146/2021, artigo 40, § 7º, II, § 8º da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003 e artigo 40, § 7º da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - pensão vitalícia e temporária
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-7-inc-ii/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-7/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-8/ec-41-2003.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-10-inc-i/lce-949-2017.md
  - /dispositivos/lce-432-2008/art-32-inc-ii-al-a/lce-949-2017.md
  - /dispositivos/lce-432-2008/art-32-par-1/lce-949-2017.md
  - /dispositivos/lce-432-2008/art-33/lce-949-2017.md
  - /dispositivos/lce-432-2008/art-34-inc-i/lce-949-2017.md
  - /dispositivos/lce-432-2008/art-34-par-2/lce-949-2017.md
---

# Estado da análise

Pensão por morte sob o **art. 40, § 7º da CF/88 na redação da EC 41/2003**,
combinado com o art. 28 da LCE 432/2008 (e as alterações da LC 949/2017) e o
art. 4º da ECE 146/2021. `paridade: N` e
`tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS` são coerentes
com o regime pós-2003: o valor vai até o teto do RGPS acrescido de setenta por
cento da parcela excedente, e o reajuste segue o índice do RGPS, sem paridade. A
regra é `simulavel: N` — a indicação depende de triagem humana da fundamentação.

**Esta regra e a `regra-0013` são materialmente idênticas.** Todos os campos de
domínio coincidem, `nome` incluído, e as duas declaram o mesmo conjunto de
dispositivos. É um dos grupos `P2_IGUALDADE_MATERIAL_ATIVA` em que **nenhum campo
distingue** as duas, e a RFC 0012 §3.5 o trata como caso mínimo: como
`simulavel: N`, quem seleciona é um humano, e não há nada por que selecionar uma
em vez da outra. Diferenciar a fundamentação dissolveria o grupo **e** seria
alteração substancial, porque em `simulavel: N` a prosa *é* o critério — mas nada
autoriza fazer essa edição: qual é a distinção pretendida é pergunta ao IPERON.
Inativar uma delas também não é da auditoria, porque é campo deployável.

Verificação humana que o cadastro não expressa: conferência documental do momento
do óbito contra a vigência das normas estaduais aplicáveis, e análise probatória
do enquadramento do dependente (vitalício ou temporário), com averiguação de
impedimentos. Documentos correspondentes: certidão de óbito do instituidor,
identidade civil dos dependentes requerentes, prova de vínculo (casamento, união
estável ou nascimento) e a ficha financeira da remuneração ou proventos na data
do óbito.

- [x] `tipo_calculo` e `paridade: N` são coerentes com a fórmula do art. 40, § 7º na redação da EC 41/2003
- [ ] A identidade material com a `regra-0013` não está resolvida — pergunta ao IPERON, e a correção não é da auditoria (achados `achado-0001`/`achado-0002`, abertos)
- [ ] Os dispositivos declarados não foram conferidos um a um contra os campos de fundamentação
- [ ] `data_direito_ate: 31/12/2024` — janela do art. 4º da ECE 146/2021, cuja conferência corre em achado próprio
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
