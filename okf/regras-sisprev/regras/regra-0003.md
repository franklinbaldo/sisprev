---
type: Regra
id: regra-0003
row_index: 3
id_sisprev: '52'
nome: INVÁLIDA · Pensão · óbito a partir de 01/01/1969 e antes de 15/12/1998, ingresso até 15/12/1998 · paridade
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
data_adm_ate: 15/12/1998 00:00
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 15/12/1998 00:00
data_direito_apos: 01/01/1969 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Art. 40, §5º da Constituição Federal de 1988 em seu texto original
visivel_dtc_integral: N
sexo: ''
integral: ''
tipo_calculo: Não identificado
fundamentacao: ''
---

# Estado da análise

Pensão por morte sob a **redação original do art. 40, § 5º da CF/88**: o
benefício correspondia à totalidade dos vencimentos ou proventos do servidor
falecido, com paridade de reajuste — o que é coerente com `paridade: S`. A regra
é `simulavel: N`, então quem a seleciona é um humano lendo a fundamentação, e não
o motor; nada aqui é aferido automaticamente.

**A janela fecha onde a EC 20/1998 começa, e isso confere.** `data_adm_ate` e
`data_direito_ate` são ambas `15/12/1998`, véspera da vigência da EC 20/1998, que
o bundle registra em `okf/dispositivos/ec-20-1998/norma.md`
(`vigencia_inicio: 1998-12-16`) — e a `regra-0005`, sucessora sob aquela emenda,
abre exatamente em `16/12/1998`. O par pavimenta sem vão nem sobreposição, logo
`15/12/1998` é o fim fechado do período da redação original, **não** um erro de um
dia na migração. A rodada anterior desta análise registrou o ponto como suspeita;
com a norma transcrita, ele fecha.

**`data_direito_apos: 01/01/1969` continua sem explicação.** É anterior à própria
CF/88, e a RFC 0011 deliberadamente o deixou **fora** do conjunto de sentinelas
justamente para que incluí-lo exigisse conferir o fundamento e autorar — uma
suspeita que entrasse no conjunto sem ato de ninguém viraria a decisão de que
aquele limite não é critério.

O que o requerimento exige de verificação humana, e que nenhum campo do cadastro
expressa: autenticação da certidão de óbito do instituidor; comprovação da
qualidade de segurado (ativo ou inativo) na data do óbito; e prova do vínculo de
dependência previdenciária, com verificação de impedimento legal. Os documentos
correspondentes são a certidão de óbito, identificação civil do instituidor e dos
dependentes, prova de vínculo (casamento, união estável ou nascimento) e o
demonstrativo de proventos ou vencimentos integrais do instituidor.

- [x] A fronteira `15/12/1998` confere contra a vigência da EC 20/1998 transcrita, e o par com a `regra-0005` pavimenta sem vão
- [ ] `data_direito_apos: 01/01/1969` não tem fundamento conferido — anterior à CF/88, e fora do conjunto de sentinelas por decisão da RFC 0011
- [ ] `dispositivos:` vazio: a redação original do art. 40, § 5º ainda não foi transcrita, então não há a que vincular
- [ ] `sexo` e `integral` vazios, `tipo_calculo: Não identificado` — alcançados pelo `achado-0008`, sem disposição escrita nesta regra
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
