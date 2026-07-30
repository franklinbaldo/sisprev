---
type: Regra
id: regra-0009
row_index: 9
nome: Invalidez · ingresso até 31/12/2003, requisitos a partir de 31/12/2003 · Ambos · regra-0009
tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
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
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: Aposentadoria por incapacidade permanente, com proventos proporcionais, calculados com base na última remuneração e com paridade, com fundamento no artigo 40, §1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 41/2003, combinado com o artigo 20 da Lei Complementar n. 432/2008, no artigo 6º-A da Emenda Constitucional n. 41/03, com redação dada pela Emenda Constitucional n. 70/2012, bem como no artigo 4º da Emenda à Constituição Estadual nº 146/2021 - fundamento incapacidade - 6-A EC 41/03 (sem acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável com ingresso antes de 2004)
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição Estadual nº 146/2021, artigo 6º-A da Emenda Constitucional nº 41/2003, com redação dada pela Emenda Constitucional nº 70/2012 e artigo 20, caput, § 9º, da Lei Complementar Estadual nº 432/2008. (com acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável com ingresso antes de 2004)
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-20-caput/original.md
  - /dispositivos/lce-432-2008/art-20-par-9/original.md
  - /dispositivos/lce-432-2008/art-20/original.md
---

# Estado da análise

Mesmo regime de transição da `regra-0008` — art. 6º-A da EC 41/2003 na
redação da EC 70/2012, ingresso até 31/12/2003, paridade, base na remuneração
do cargo —, com proventos proporcionais em vez de integrais.

O par 0008/0009 é o caso mais apertado das quatro: o frontmatter das duas é
**idêntico em todos os campos exceto `integral`**. Diferente do par
0006/0007, aqui nem o `tipo_calculo` muda — as duas gravam
`Remuneração de Contribuição` —, e os dois campos de fundamentação são os
mesmos texto por texto, o parêntese "com acidente em serviço, moléstia
profissional ou doença grave" incluído. Uma única letra separa as duas
regras, e o critério que essa letra representa não está registrado em lugar
nenhum do cadastro.

Isso torna a Q6 mais visível aqui do que em qualquer outro ponto do catálogo:
`integral` é o **resultado**, e o critério que o determina — a causa da
incapacidade — não tem coluna. Enquanto assim for, um requerimento que case
com esta regra casa igualmente com a `regra-0008`, e nada nos campos decide
entre elas.

Reconferência de 2026-07-29 contra a publicação oficial da EC 70/2012. O
agravante da `regra-0008` é integralmente desta também, porque os dois campos
de fundamentação são byte-idênticos entre as duas: a `fundamentacao_integral`
invoca o art. 6º-A — que exige, em texto, fundamento "no inciso I do § 1º do
art. 40" — e aponta como fundamento o inciso **III**, sem citar o inciso I em
ponto nenhum. Ver [`achado-0022`](../achados/achado-0022.md).

Nesta regra, porém, há uma assimetria que vale nomear: `integral: N` significa
proventos **proporcionais**, e o texto que a regra carrega para o caso
proporcional — a `fundamentacao_proporcional` — cita o inciso I e o art. 20 da
LCE 432/2008 corretamente. É o campo `_integral`, que esta regra carrega sem
conceder o benefício que ele descreve, que traz a citação defeituosa. Isso não
a torna inócua: `FUNDAMENTACAO_INTEGRAL` é coluna deployável, e a Q7 (qual dos
dois campos vale, e quando) segue aberta.

- [x] Critérios do cadastro percorridos um a um contra a lei — conferência `critério → dispositivo` de 0006–0009
- [x] `dispositivos:` conferido contra os dois campos de fundamentação, item a item: nada a acrescentar nem a remover
- [x] Diferença material em relação à `regra-0008` isolada: um único campo, `integral`
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado — inclusive com o recorte "segunda parte" — mas não funda critério representado nas colunas
- [x] Janela do art. 4º da ECE 146/2021 conferida contra a transcrição oficial ([conferência](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)): o dispositivo funda os requisitos desta regra (art. 6º-A da EC 41/2003, na redação da EC 70/2012, anterior à EC 146) e os prazeia em 31/12/2024. O "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
- [x] `data_adm_ate: 31/12/2003` conferido contra o texto oficial do art. 6º-A ("até a data de publicação desta Emenda Constitucional") e contra o marco da EC 41/2003
- [x] `sexo: AMBOS` fecha por ausência — nem o art. 6º-A nem o art. 20 da LCE 432/2008 distinguem por sexo
- [ ] Citação do art. 40, § 1º, III (EC 103/2019), inclusive com o recorte "segunda parte": não funda critério nas colunas, é redação disjunta da do inciso I, e contraria a condição expressa do art. 6º-A — [`achado-0022`](../achados/achado-0022.md)
- [ ] Qual dos dois campos de fundamentação vale nesta regra, que grava `integral: N` e carrega os dois textos byte-idênticos aos da `regra-0008`. É a **Q7**, aberta, e sem ela não se diz qual lado cede
- [ ] `lce-432-2008/art-20/original`, vinculado aqui, transcreve só o *caput* embora enderece o artigo inteiro. Fila de transcrição
- [ ] Causa da incapacidade — único critério que separa esta regra da `regra-0008`, e sem coluna que o registre. Depende da Q6; com `simulavel: S` nas duas, o motor não tem predicado que decida — [`achado-0026`](../achados/achado-0026.md)
- [ ] "Moléstia profissional" não é definida em lugar nenhum da LCE 432/2008 — [`achado-0025`](../achados/achado-0025.md)
