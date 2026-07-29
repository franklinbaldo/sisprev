---
type: Regra
id: regra-0006
row_index: 6
nome: Invalidez - Art. 40, §1º, I da CF, com redação dada pela EC nº 41/2003 e Arts. 17 e 20 da LC 432/2008
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

- [x] Critérios do cadastro percorridos um a um contra a lei — [conferência `critério → dispositivo`](../../../docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` e `fundamentacao_proporcional`, item a item: nada a acrescentar nem a remover
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado mas não funda critério representado nas colunas — o inciso III é de aposentadoria voluntária por idade. Decisão do dono do campo, não do auditor
- [ ] `data_direito_ate: 31/12/2099` discorda do prazo de 31/12/2024 do art. 4º da ECE 146/2021, que esta regra cita: ou o art. 4º não funda a janela, ou a janela está gravada errada
- [ ] Causa da incapacidade — o critério que separa esta regra da `regra-0007` não tem coluna. Depende da Q6, não decidível hoje
