---
type: Regra
id: regra-0083
row_index: 83
nome: Voluntária · Policial civil · ingresso até 31/12/2003, pedido a partir de 18/10/2021 · Feminino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, §1°, inciso III, segunda parte, e § 4°-B da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigos 25, 27, inciso I, e 34 da Lei Complementar nº 1.100/2021 - regra permanente.
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4b/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-34/original.md
---

# Estado da análise

Gêmea feminina da `regra-0082`, na mesma regra permanente do art. 34 da LCE
1.100/2021, variante de quem ingressou **até** 31/12/2003 — totalidade da
remuneração pelo art. 25 e paridade pelo art. 27, I.

**A pergunta da alínea não se aplica**: o `achado-0017` é sobre a alínea errada
do art. 1º, II da LC 51/1985, e esta regra não cita a LC 51/1985 em campo algum.

E, como na `regra-0081`, a divisão por sexo é o próprio defeito: o art. 34 fixa
os requisitos "para ambos os sexos", e nada distingue esta regra da `regra-0082`
além do campo `sexo` ([`achado-0040`](../achados/achado-0040.md)). Não há alínea
feminina a conferir, porque a lei citada não tem uma.

A lista congelada de citações atribui a esta regra o qualificador "segunda parte"
também ao § 4º-B ([`pendencias-de-citacao-congeladas.md`](../../../docs/analysis/pendencias-de-citacao-congeladas.md)).
A prosa da fundamentação qualifica só o inciso III — "artigo 40, §1°, inciso III,
segunda parte, e § 4°-B" —, e o deslize é do leitor por expressão regular que a
RFC 0008 aposentou. Nada a corrigir na regra.

- [x] `data_adm_ate: 31/12/2003` é, sob a convenção confirmada (`ATE` inclusivo), o "ingressado [...] até 31 de dezembro de 2003" do art. 25, conferido no texto compilado oficial (`ditel-LC1100---COMPILAÇÃO.txt`)
- [x] `tipo_calculo: Remuneração de Contribuição` e `integral: S` ← art. 25; `paridade: S` ← art. 27, I
- [x] A janela de admissão fecha exatamente onde a da `regra-0081` abre — a divisão **por marco de ingresso** tem dispositivo, ao contrário da divisão por sexo
- [x] A LC 51/1985 **não** é citada em campo nenhum desta regra: o defeito da alínea (`achado-0017`) não tem como ocorrer aqui, porque os requisitos vêm do art. 34 da LCE 1.100/2021, que é expressamente unissexual
- [x] `data_direito_apos: 18/10/2021` é o início de vigência da LCE 1.100/2021, a norma que institui a modalidade
- [x] `data_direito_ate: 31/12/2099` coerente com regra permanente: conferido no texto compilado oficial que nem o art. 34 nem a Seção V fixam termo. Sentinela não interpretada (P5)
- [x] Cada item de `dispositivos:` resolve e é citado pela `fundamentacao_integral`; nada a acrescentar nem a remover
- [ ] O desdobramento por `sexo` não tem dispositivo: o art. 34 fixa os requisitos "para ambos os sexos" — [`achado-0040`](../achados/achado-0040.md)
- [ ] Os quatro requisitos do art. 34 (55 anos de idade, 30 de contribuição, 25 de exercício policial, 5 na carreira) não têm coluna no cadastro, e a regra é `simulavel: S` — o motor seleciona sem aferir nenhum deles (Q5)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado e a metade aplicável ao Estado remete à idade mínima da emenda estadual, sem fixar critério gravado em coluna (§5.2 de [`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md))
