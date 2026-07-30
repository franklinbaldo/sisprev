---
type: Regra
id: regra-0111
row_index: 111
nome: Voluntária · Policial civil · ingresso até 31/12/2003, requisitos antes de 31/12/2024 · Masculino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
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
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 01/01/1910 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória homem- idade + tempo + pedágio | Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória mulher - idade + tempo + pedágio
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
---

# Estado da análise

Esta regra tem duas metades que descrevem regimes diferentes, e a conferência não
consegue fechar por causa disso. O `nome` e as **quatro** janelas são a via do
art. 4º da ECE 146/2021 — requisitos da legislação anterior à Emenda, cumpridos
até 31/12/2024, assegurados a qualquer tempo, sem idade mínima. A
`fundamentacao_integral`, único campo de fundamentação preenchido, é a via do
art. 7º, §§ 2º e 3º — idade mínima com pedágio, corte de ingresso em 13/11/2019,
sem prazo — e é literalmente o mesmo texto de `regra-0072` a `regra-0077`, com um
espaço de diferença. Registrado em
[`achado-0039`](../achados/achado-0039.md).

**A pergunta da alínea se responde bem no `dispositivos:`**: `sexo: MASCULINO` e o
vínculo é `lc-51-1985/art-1-inc-ii-al-a`, a alínea masculina (30/20, "se homem"),
conferida na publicação oficial compilada do Planalto arquivada em
`fontes-oficiais/`. O `nome` também nomeia a alínea "a", e para **esta** regra
isso está certo — o problema é a gêmea `regra-0112`, que é `FEMININO` e tem o
mesmo `nome` ([`achado-0038`](../achados/achado-0038.md)).

No texto, o defeito é o do empacotamento: a célula traz as duas alíneas
([`achado-0037`](../achados/achado-0037.md)).

- [x] `sexo` × alínea em `dispositivos:`: MASCULINO ↔ `al-a`, conferido na fonte oficial (`planalto-lcp51.htm`, cp1252)
- [x] `sexo` × alínea no `nome`: a alínea "a" nomeada é a masculina, e esta regra é MASCULINO — correta aqui, e só aqui no par (`achado-0038`)
- [x] Cada item de `dispositivos:` resolve, e o dispositivo apontado é citado pela `fundamentacao_integral`
- [ ] A janela é a do art. 4º e a fundamentação é a do art. 7º: duas vias de transição incompatíveis na mesma regra — `achado-0039`. Ambos os lados são campo deployável; a escolha não é do auditor
- [ ] `ece-146-2021/art-4/original` é o único dispositivo do corpus que fixa o `31/12/2024` gravado aqui, está autorado, e **não** é vinculado: nenhum campo de fundamentação o cita (só o `nome`), e vincular seria falsificar o vínculo para consertar o dado — `achado-0039`
- [ ] `data_adm_ate: 31/12/2003` não é o corte de nenhuma das duas vias; a hipótese de vir do regime de integralidade e paridade preservado pelo art. 4º, parágrafo único, não foi conferida e nenhum campo a declara
- [ ] `fundamentacao_integral` traz também a articulação feminina (alínea "b", 25/15) — `achado-0037`
- [ ] `dispositivos:` declara uma alínea e a fundamentação cita duas — `achado-0037`, item 3
- [ ] Idade mínima, tempo de contribuição e tempo de exercício policial não têm coluna, e a regra é `simulavel: S` (Q5) — aqui o efeito é composto: o motor não afere requisito nenhum **e** as duas vias exigem requisitos diferentes
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado e não fixa critério gravado em coluna alguma — norma de competência e remissão à emenda estadual (§5.2 de [`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md))
