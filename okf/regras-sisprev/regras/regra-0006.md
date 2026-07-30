---
type: Regra
id: regra-0006
row_index: 6
nome: Invalidez · requisitos a partir de 31/12/2003 · Ambos · integral · Valor Médio
tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
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
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: Aposentadoria por incapacidade permanente, com proventos proporcionais ao tempo de contribuição e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003, artigos 17, 20, caput, 45 e 62 da Lei Complementar Estadual nº 432/2008, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - fundamento incapacidade - LCE 432/08 (doença não catalogada com ingresso após 2003)
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003, artigos 20, caput, 45 e 62 da Lei Complementar Estadual nº 432/2008, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - fundamento incapacidade - LCE 432/08 (acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável com ingresso após 2003).
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-20-caput/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
---

# Estado da análise

Regime geral do art. 40, § 1º, I, na redação da EC 41/2003: incapacidade
permanente, sem corte de ingresso (`data_adm_ate: 31/12/2099`), sem paridade,
proventos integrais calculados por média (`tipo_calculo: Valor Médio`).

O que a separa da vizinha é só o resultado. O frontmatter de `regra-0007` é
igual ao desta em tudo, exceto `integral`, `tipo_calculo`, o campo
`fundamentacao` e um dispositivo a mais — **os dois campos de fundamentação
são literalmente idênticos nas duas**. Cada uma carrega as duas: a integral,
cujo parêntese diz "acidente em serviço, moléstia profissional ou doença
grave", e a proporcional, cujo parêntese diz "doença não catalogada". O
critério que de fato separa 0006 de 0007 é a **causa da incapacidade**, e ela
não está em coluna nenhuma — está dentro daquele parêntese, num texto que as
duas compartilham. Por isso o `P1_NOME_REPETIDO` do par não se resolve
renomeando: o nome repetido é sintoma, e a lacuna é de representação (Q6).

Um cuidado que esta regra em particular exige, registrado porque a primeira
versão da conferência errou nele: `integral: S` **não** faz desta "a regra
integral". Ela carrega também a `fundamentacao_proporcional`, e é lá que o
art. 17 da LCE 432/2008 é citado — o vínculo `lce-432-2008/art-17/original`
está correto. Pelo mesmo motivo o § 9º do art. 20 **não** entra aqui: nenhum
campo desta regra o cita. Quem o cita é a `regra-0008`.

Reconferência de 2026-07-29, agora contra as **publicações oficiais
arquivadas** em `fontes-oficiais/` e não só contra a transcrição do corpus. Ela
fechou três coisas e abriu uma. Fechou: o texto do art. 20 da LCE 432/2008
(*caput* e § 14, que roteia o cálculo ao art. 45 — a média das 80% maiores, que
é o `Valor Médio` gravado), o texto do art. 45 na redação da LCE 672/2012, e o
texto do art. 40, § 1º, I na redação da EC 41/2003, que é o dispositivo que
traz o discriminante integral × proporcional desta regra. Abriu: as duas
redações do art. 40, § 1º que esta regra cita — inciso I pela EC 41/2003 e
inciso III pela EC 103/2019 — **nunca vigeram ao mesmo tempo**, e o *caput* do
§ 1º que cada uma exige é texto diferente. Está em
[`achado-0022`](../achados/achado-0022.md).

O art. 4º da ECE 146/2021 **passou a ser conferível** depois desta rodada: a
transcrição pesquisável foi arquivada, e a
[conferência da janela](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)
fechou o prazo de 31/12/2024 contra o texto oficial. O item que estava aberto
por falta de fonte foi substituído pelo item conferido.

- [x] Critérios do cadastro percorridos um a um contra a lei — [conferência `critério → dispositivo`](../../../docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` e `fundamentacao_proporcional`, item a item: nada a acrescentar nem a remover
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado mas não funda critério representado nas colunas — o inciso III é de aposentadoria voluntária por idade. Decisão do dono do campo, não do auditor
- [x] Janela do art. 4º da ECE 146/2021 conferida contra a transcrição oficial ([conferência](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)): o dispositivo funda os requisitos desta regra (art. 40, § 1º, I, da CF na redação da EC 41/2003, anterior à EC 146) e os prazeia em 31/12/2024. O "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
- [x] `tipo_calculo: Valor Médio` conferido contra a fonte oficial: art. 20, § 14 da LCE 432/2008 roteia ao art. 45, e o art. 45 é a média aritmética simples das 80% maiores remunerações
- [x] `sexo: AMBOS` fecha por ausência — nenhum dispositivo da cadeia de incapacidade citado distingue por sexo (o único que distingue é o art. 40, § 1º, III, cuja matéria não é a desta regra)
- [x] `data_direito_apos: 31/12/2003` coincide com o marco da EC 41/2003, a norma que dá a redação citada
- [ ] Citação do art. 40, § 1º, III (EC 103/2019): não funda critério representado nas colunas **e** é redação que nunca coexistiu com a do inciso I também citado — [`achado-0022`](../achados/achado-0022.md). Decisão do dono do campo, não do auditor
- [ ] Se a janela desta regra deveria fechar em 12/11/2019, último dia da redação do inciso I que ela cita — mesmo formato do [`achado-0014`](../achados/achado-0014.md), e agora com uma família de regras (`0019`–`0022`) existindo para o período seguinte
- [ ] Causa da incapacidade — o critério que separa esta regra da `regra-0007` não tem coluna. Depende da Q6, não decidível hoje. Consequência operacional em [`achado-0026`](../achados/achado-0026.md): com `simulavel: S`, o motor não tem predicado que decida entre as duas
- [ ] "Moléstia profissional", uma das três causas que produzem `integral: S` aqui, não é definida em lugar nenhum da LCE 432/2008 — [`achado-0025`](../achados/achado-0025.md). Falta pesquisar decreto/regulamento estadual e eventual remissão à legislação federal
