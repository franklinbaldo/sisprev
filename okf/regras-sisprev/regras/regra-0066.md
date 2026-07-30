---
type: Regra
id: regra-0066
row_index: 66
nome: Voluntária · Agentes nocivos · pedido a partir de 31/12/2003 · Ambos · integral · paridade · regra-0066
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
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por integralidade) e com paridade, com base nos artigos 25, 27, inciso I, e 41, inciso III, da Lei Complementar Estadual 1.100/2021 e artigo 40, § 1º, inciso III, segunda parte, e § 4°-C, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - regra permanente
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
---

# Estado da análise

Regra permanente de aposentadoria voluntária por efetiva exposição a agentes
nocivos. O art. 40, § 1º, III da CF, na redação da EC 103/2019, remete a idade,
tempo de contribuição e demais requisitos à legislação do ente; o § 4º-C
permite idade e tempo diferenciados para a exposição efetiva. A hipótese
material vem do art. 41, III da LCE 1.100/2021: 20 anos de serviço público, 5
anos no cargo, 86 pontos e 25 anos de efetiva exposição. O art. 25 fixa a
**totalidade da remuneração no cargo efetivo** para ingresso até 31/12/2003,
sem opção pelo § 16 do art. 40 da CF; o art. 27, I fixa o reajuste por remissão
ao art. 7º da EC 41/2003 para a mesma população. O conteúdo da remissão foi
conferido no art. 7º transcrito no repositório: revisão na mesma proporção e na
mesma data da remuneração dos servidores em atividade.

O frontmatter põe a regra no motor (`simulavel: S`) e grava valores estruturados
para sexo, tipo, especialidade, pontuação, janelas e resultado. Entre os campos
de domínio, `sexo` é critério aferido confirmado; a semântica das quatro datas
também está fixada. Não há coluna para os 20 anos de serviço público, os 5 anos
no cargo, os 86 pontos, os 25 anos de exposição nem para a ausência de opção
pelo § 16. Esses requisitos dependem de verificação humana por construção. O
art. 41 exige que o servidor **comprove** a efetiva exposição, mas as provisões
transcritas não dizem quais documentos realizam essa prova.

Os campos `integral: S` e `paridade: S` são coerentes, respectivamente, com os
arts. 25 e 27, I. `tipo_calculo: Valor Médio`, porém, destoa do mesmo conjunto
sem que seja necessário converter o enum em fórmula: a `regra-0067` tem
fundamentação e dispositivos idênticos e grava `Valor Efetivo`, enquanto a
`regra-0071` reserva `Valor Médio` ao trilho dos arts. 24 e 27, II. A divergência
está no campo estruturado que orienta o valor, não no texto entregue ao servidor,
e é objeto do `achado-0057`.

As janelas também não correspondem ao fundamento. `data_adm_apos: 01/01/1950`
e `data_adm_ate: 31/12/2099` são sentinelas e, portanto, não gravam o corte de
ingresso até 31/12/2003 exigido pelos arts. 25 e 27, I.
`data_direito_apos: 31/12/2003` inclui esse próprio dia e antecede todos os
cinco dispositivos citados; nenhuma provisão transcrita funda esse marco. É o
mesmo defeito temporal já demonstrado no `achado-0042` para a `regra-0067`.

- [x] Os cinco arquivos de `dispositivos:` foram lidos integralmente, com a cadeia de ancestrais, e correspondem às cinco provisões nomeadas em `fundamentacao_integral`
- [x] A remissão do art. 27, I ao art. 7º da EC 41/2003 foi conferida no arquivo transcrito `ec-41-2003/art-7/original.md`; o dispositivo descreve revisão na mesma proporção e data da remuneração dos servidores em atividade
- [x] O vínculo critério → dispositivo foi recuperado: art. 40, § 1º, III para a remissão à legislação estadual; art. 40, § 4º-C para a diferenciação por exposição; art. 41, III para 20 anos de serviço público, 5 no cargo, 86 pontos e 25 de exposição; art. 25 para totalidade da remuneração e corte de ingresso; art. 27, I para reajuste e o mesmo corte
- [x] `sexo: AMBOS` conferido contra os dispositivos citados: o art. 41, III não divide a hipótese por sexo, e nenhuma das demais provisões estaduais vinculadas introduz essa distinção
- [x] `integral: S` e `paridade: S` conferidos contra os arts. 25 e 27, I e contra o texto objeto da remissão: coerentes
- [x] Requisitos sem coluna identificados: 20 anos de serviço público, 5 anos no cargo, 86 pontos, 25 anos de efetiva exposição e ausência de opção pelo § 16 do art. 40 da CF; a aferição depende de análise humana
- [ ] Identificar quais documentos demonstram exposição, tempos e ausência de opção pelo § 16; as provisões transcritas exigem os fatos, mas não especificam o meio documental
- [ ] Confirmar, além de `sexo` e das janelas, quais campos de domínio o motor efetivamente afere; `tipo`, `apos_especial`, `tabelapontuacao` e os demais permanecem candidatos sem evidência operacional suficiente
- [ ] Corrigir ou substituir `tipo_calculo: Valor Médio`, incompatível com o trilho citado e com a irmã de fundamentação idêntica — `achado-0057`; campo deployável, decisão do responsável pelo produto
- [ ] Estender `regras_afetadas` do `achado-0042` a esta regra e decidir o corte de admissão até 31/12/2003 e o marco de direito; o achado demonstra o mesmo defeito, mas não alcança esta ficha no frontmatter
- [ ] Resolver o significado operacional de `tabelapontuacao` antes de julgar `N`: o art. 41 contém pontos fixos, e as regras do art. 8º da ECE 146/2021 gravam `S` para estrutura equivalente — `achado-0054`
- [ ] Apurar o grupo de igualdade material com a `regra-0065`: pode ser repetição ou distinção externa não expressável pelo schema; não há critério cadastral que separe as duas — `achado-0005`
