---
type: Regra
id: regra-0073
row_index: 73
nome: Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021
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
data_adm_ate: 13/11/2019 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória homem - idade + tempo + pedágio | Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória mulher - idade + tempo + pedágio
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Artigo 7º, §§ 2º e 3º, da Emenda Constitucional Estadual nº 146/2021
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
---

# Estado da análise

Gêmea feminina da `regra-0072`, na mesma via do art. 7º, § 2º da ECE 146/2021 —
para a mulher a idade do § 2º é **52** anos, e o tempo que a LC 51/1985 exige é o
da alínea "b": 25 anos de contribuição e 15 de exercício policial. O par é
legitimamente distinto, porque o critério aferido diverge por sexo, e é esse
mesmo motivo que faz esta regra **não** entrar no grupo de igualdade material das
cinco masculinas ([`achado-0041`](../achados/achado-0041.md)).

**A pergunta da alínea se responde bem aqui, no `dispositivos:`**: `sexo: FEMININO` e o vínculo é `lc-51-1985/art-1-inc-ii-al-b`, a alínea feminina.
Conferido na publicação oficial compilada do Planalto arquivada em
`fontes-oficiais/`. É a mesma combinação que a `regra-0079` acerta e que a
`regra-0078` erra (`achado-0017`).

O defeito está no texto, e nesta regra ele tem uma agravante: a
`fundamentacao_integral` traz as duas alíneas numa célula só e a que **não** é
dela — a masculina, 30/20 — é a que aparece **primeiro**
([`achado-0037`](../achados/achado-0037.md)). Quem lê a célula de cima para baixo
lê primeiro o requisito errado.

- [x] `sexo` × alínea: FEMININO ↔ `al-b` (25/15, "se mulher"), conferido na fonte oficial (`planalto-lcp51.htm`, cp1252)
- [x] Cada item de `dispositivos:` resolve, e o dispositivo apontado é citado por um campo de fundamentação desta regra
- [x] `integral: S`, `tipo_calculo: Remuneração de Contribuição` e `paridade: S` fundados no art. 7º, § 3º da ECE 146/2021
- [x] `data_adm_ate: 13/11/2019` é o corte de ingresso do *caput* do art. 7º, conferido na publicação oficial da Emenda (`sapl-emenda_146.pdf`, p. 8)
- [x] `data_direito_ate: 31/12/2099` coerente com o art. 7º não ter prazo (conferido: *caput* e §§ 1º a 3º, e mais nada). Sentinela não interpretada (P5)
- [x] O par com a `regra-0072` é fundado: o § 2º dá 52 anos à mulher e 53 ao homem, e as alíneas da LC 51/1985 exigem tempos diferentes — a divergência de `sexo` tem dispositivo, ao contrário do que ocorre em `regra-0080`–`0083` (`achado-0040`)
- [ ] `fundamentacao_integral` traz também a articulação masculina (alínea "a", 30/20), e antes da sua — `achado-0037`. Campo deployável
- [ ] `dispositivos:` declara uma alínea e a fundamentação cita duas — `achado-0037`, item 3
- [ ] `data_direito_apos: 14/09/2021` casa com o `vigencia_inicio` declarado da ECE 146/2021, mas não foi conferido contra fonte: a publicação em Diário Oficial não está arquivada e o PDF oficial traz 09/09/2021, data da Assembleia
- [ ] Idade mínima (52 anos), tempo de contribuição (25) e tempo de exercício policial (15) não têm coluna, e a regra é `simulavel: S` (Q5)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado e não fixa critério gravado em coluna alguma — norma de competência e remissão à emenda estadual (§5.2 de [`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md))
