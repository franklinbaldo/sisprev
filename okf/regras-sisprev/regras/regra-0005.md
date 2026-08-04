---
type: Regra
id: regra-0005
row_index: 5
id_sisprev: '54'
nome_original: Pensão por Morte - CF/88 com redação da EC nº 20/1998
nome: INVÁLIDA · Pensão · óbito a partir de 16/12/1998 e antes de 31/12/2003, ingresso até 31/12/2003 · paridade
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
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2003 00:00
data_direito_apos: 16/12/1998 00:00
fundamentacao_proporcional: Art. 40, §7º da CF/88 com redação dada pela EC 20/1998
visivel_dtc_proporcional: N
fundamentacao_integral: Art. 40, §7º da CF/88 com redação dada pela EC 20/1998
visivel_dtc_integral: N
sexo: ''
integral: ''
tipo_calculo: Não identificado
fundamentacao: ''
---

# Estado da análise

Pensão por morte sob o **art. 40, § 7º da CF/88 na redação da EC 20/1998**,
sucessora imediata da `regra-0003`. `paridade: S` é coerente com o regime
anterior à EC 41/2003. A regra é `simulavel: N`: a seleção depende de triagem
humana pela fundamentação, não do motor.

**A janela confere nas duas pontas.** `data_direito_apos: 16/12/1998` é
exatamente o `vigencia_inicio` que o bundle registra para a EC 20/1998
(`okf/dispositivos/ec-20-1998/norma.md`), e `data_direito_ate: 31/12/2003` é o
marco da EC 41/2003. A ponta inicial encaixa sem vão no fim da `regra-0003`
(`15/12/1998`), o que resolve, para as duas, a suspeita de divergência de um dia
levantada na rodada anterior.

Verificação humana que o cadastro não expressa: autenticação da certidão de óbito
do instituidor; validação da qualidade jurídica de dependente habilitado na data
do óbito; e verificação de não-cumulação indevida de benefícios. Documentos
correspondentes: certidão de óbito, certidão de casamento atualizada ou prova de
união estável ou certidão de nascimento dos dependentes, identidade civil e CPF
dos requerentes, e comprovante da remuneração no cargo efetivo ou dos proventos
na data do óbito.

- [x] `data_direito_apos: 16/12/1998` confere contra a vigência transcrita da EC 20/1998, e encaixa sem vão no fim da janela da `regra-0003`
- [x] `data_direito_ate: 31/12/2003` corresponde ao marco da EC 41/2003
- [ ] `dispositivos:` vazio: a redação da EC 20/1998 do art. 40, § 7º ainda não foi transcrita
- [ ] `sexo` e `integral` vazios, `tipo_calculo: Não identificado` — alcançados pelo `achado-0008`, sem disposição escrita nesta regra
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
