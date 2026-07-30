---
type: Regra
id: regra-0112
row_index: 112
nome: Voluntária · Policial civil · ingresso até 31/12/2003, requisitos antes de 31/12/2024 · Feminino · integral · paridade · Remuneração de Contribuição
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
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
---

# Estado da análise

Gêmea feminina da `regra-0111`, e herda dela as duas metades que descrevem
regimes diferentes: `nome` e as quatro janelas são a via do art. 4º da ECE
146/2021 (requisitos da legislação anterior, cumpridos até 31/12/2024, sem idade
mínima), e a `fundamentacao_integral` é a via do art. 7º, §§ 2º e 3º (idade
mínima com pedágio, corte de ingresso em 13/11/2019, sem prazo) —
[`achado-0039`](../achados/achado-0039.md).

**A pergunta da alínea se responde de dois modos opostos nesta regra, e é o
achado do dia.** Em `dispositivos:` está certo: `sexo: FEMININO` ↔
`lc-51-1985/art-1-inc-ii-al-b`, a alínea feminina (25 anos de contribuição, 15 de
exercício policial, "se mulher"), conferida na publicação oficial compilada do
Planalto arquivada em `fontes-oficiais/`. No **`nome`** está errado: o rótulo
desta regra é o mesmo da `regra-0111`, caractere a caractere, e nomeia a alínea
**"a"** — a masculina, 30/20, "se homem"
([`achado-0038`](../achados/achado-0038.md)). É o defeito do `achado-0017` num
campo que ele não alcança: lá a alínea do outro sexo está na fundamentação, aqui
está no rótulo que o usuário lê para escolher a regra.

E, como nas outras três do lote, `fundamentacao_integral` empacota as duas
alíneas — com a masculina em primeiro lugar
([`achado-0037`](../achados/achado-0037.md)).

- [x] `sexo` × alínea em `dispositivos:`: FEMININO ↔ `al-b` (25/15, "se mulher"), conferido na fonte oficial (`planalto-lcp51.htm`, cp1252)
- [x] Cada item de `dispositivos:` resolve, e o dispositivo apontado é citado pela `fundamentacao_integral`
- [ ] O `nome` nomeia a alínea masculina numa regra `sexo: FEMININO`, e é o mesmo rótulo da `regra-0111` — `achado-0038`. `NOME` é campo deployável
- [ ] A janela é a do art. 4º e a fundamentação é a do art. 7º: duas vias de transição incompatíveis na mesma regra — `achado-0039`
- [ ] `ece-146-2021/art-4/original` fixa o `31/12/2024` gravado aqui, está autorado e **não** é vinculado: nenhum campo de fundamentação o cita (só o `nome`) — `achado-0039`
- [ ] `data_adm_ate: 31/12/2003` não é o corte de nenhuma das duas vias, e nenhum campo desta regra declara norma que o funde
- [ ] `fundamentacao_integral` traz também a articulação masculina (alínea "a", 30/20), e antes da sua — `achado-0037`
- [ ] `dispositivos:` declara uma alínea e a fundamentação cita duas — `achado-0037`, item 3
- [ ] Idade mínima, tempo de contribuição e tempo de exercício policial não têm coluna, e a regra é `simulavel: S` (Q5)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado e não fixa critério gravado em coluna alguma — norma de competência e remissão à emenda estadual (§5.2 de [`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md))
