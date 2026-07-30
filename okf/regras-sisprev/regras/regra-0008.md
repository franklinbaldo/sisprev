---
type: Regra
id: regra-0008
row_index: 8
nome: Invalidez · ingresso até 31/12/2003, requisitos a partir de 31/12/2003 · Ambos · integral · paridade
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
integral: S
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

Regime de transição do art. 6º-A da EC 41/2003, na redação da EC 70/2012:
quem ingressou até a publicação da EC 41/2003 (`data_adm_ate: 31/12/2003`)
mantém proventos calculados sobre a remuneração do cargo efetivo
(`tipo_calculo: Remuneração de Contribuição`) e com paridade
(`paridade: S`).

Este é o caso mais limpo do que a conferência mostra e o `dispositivos:`
achatado esconde: **um único dispositivo funda três critérios de uma vez**. O
art. 6º-A dá o corte de ingresso ("que tenha ingressado no serviço público
até a data de publicação desta Emenda Constitucional"), a base de cálculo
("calculados com base na remuneração do cargo efetivo") e a paridade. Na
lista de sete entradas ele é uma linha indistinguível das demais.

A paridade merece o detalhe, porque a primeira versão desta análise a
explicava errado. O *caput* diz que não se aplicam "os §§ 3º, 8º e 17 do
art. 40" — e afastar a regra de reajuste do regime geral é norma
**negativa**: retira um critério, não fixa nenhum. Quem fixa positivamente a
paridade é o **parágrafo único** do art. 6º-A, que manda aplicar o art. 7º
da EC 41/2003, o qual determina proventos "revistos na mesma proporção e na
mesma data, sempre que se modificar a remuneração dos servidores em
atividade". Esse parágrafo não estava transcrito quando a conferência foi
feita — o documento parava no *caput*, embora `componentes` endereçasse o
artigo inteiro. Foi transcrito, e o art. 7º autorado como
`ec-41-2003/art-7/original`.

Nada disso acrescenta vínculo: o art. 7º é alcançado por **remissão**, e
nenhum campo desta regra o cita. `dispositivos:` registra o que o campo cita,
não o caminho que o raciocínio percorre.

Dois vínculos ao art. 20 da LCE 432/2008 convivem aqui de propósito, porque
os campos citam duas coisas diferentes: a `fundamentacao_proporcional` cita
"o artigo 20" sem recorte, e a `fundamentacao_integral` cita "artigo 20,
*caput*, § 9º". É também a única das quatro regras de invalidez a citar o
§ 9º — a `regra-0006` responde à mesma questão jurídica (o rol de doenças
graves) citando só o *caput*. A divergência é entre campos deployáveis de
regras vizinhas, e sair dela é decisão do dono do campo.

Sobre a "segunda parte" do art. 40, § 1º, III que a `fundamentacao_integral`
invoca: o inciso de fato se biparte, e é a segunda metade que alcança o RPPS
estadual. A leitura textual existe — mas nenhuma das duas metades funda
critério de incapacidade, então o recorte não socorre a citação.

Reconferência de 2026-07-29 contra a publicação oficial da EC 70/2012
(`fontes-oficiais/arquivos/planalto-emc70.htm`), e ela endureceu o problema da
citação do inciso III. O art. 6º-A **condiciona expressamente** o direito que
concede a que a aposentadoria tenha sido concedida "**com fundamento no inciso
I do § 1º do art. 40 da Constituição Federal**". A `fundamentacao_integral`
desta regra invoca o art. 6º-A e, no mesmo período, aponta como fundamento o
inciso **III** — e não cita o inciso I em ponto nenhum, embora a
`fundamentacao_proporcional` da mesma regra o cite. Os dois campos da regra
discordam sobre qual inciso constitucional a sustenta, e o dispositivo central
que os dois invocam exclui a leitura de um deles. Registrado em
[`achado-0022`](../achados/achado-0022.md), junto com a disjunção de vigências
das duas redações citadas.

Um defeito de **transcrição** encontrado de passagem, que não é desta regra mas
alcança quem a lê: o documento `lce-432-2008/art-20/original` — vinculado aqui
porque a `fundamentacao_proporcional` cita "o artigo 20" sem recorte — endereça
o **artigo inteiro** nos seus `componentes` e transcreve **apenas o *caput***.
O art. 20 tem quinze parágrafos, incluindo o § 9º (rol de doenças graves) e o
§ 14 (roteamento do cálculo). É o modo de falha do §5.3 da lista consolidada:
`componentes` correto, caminho correto, vínculo resolvendo, e o leitor do
capítulo desta regra no relatório da PGE não encontra os parágrafos que a
regra precisa. Corrigir é ato de transcrição, não edição de regra.

- [x] Critérios do cadastro percorridos um a um contra a lei — conferência `critério → dispositivo` de 0006–0009
- [x] `dispositivos:` conferido contra os dois campos de fundamentação, item a item: nada a acrescentar nem a remover
- [x] Os três critérios fundados pelo art. 6º-A (corte de ingresso, base de cálculo, paridade) identificados um a um
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado — inclusive com o recorte "segunda parte" — mas não funda critério representado nas colunas
- [x] Janela do art. 4º da ECE 146/2021 conferida contra a transcrição oficial ([conferência](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)): o dispositivo funda os requisitos desta regra (art. 6º-A da EC 41/2003, na redação da EC 70/2012, anterior à EC 146) e os prazeia em 31/12/2024. O "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
- [x] `data_adm_ate: 31/12/2003` conferido contra o texto oficial do art. 6º-A ("até a data de publicação desta Emenda Constitucional") e contra o marco da EC 41/2003; sob `ATE` inclusivo, o dia 31/12/2003 é coberto, o que é a leitura literal do dispositivo
- [x] `sexo: AMBOS` fecha por ausência — nem o art. 6º-A nem o art. 20 da LCE 432/2008 distinguem por sexo
- [ ] Citação do art. 40, § 1º, III (EC 103/2019), inclusive com o recorte "segunda parte": não funda critério nas colunas, é redação disjunta da do inciso I, e contraria a condição expressa do art. 6º-A — [`achado-0022`](../achados/achado-0022.md)
- [ ] Citação do rol de doenças graves diverge da `regra-0006` (aqui "art. 20, *caput*, § 9º"; lá só "art. 20, *caput*") — uniformizar é alterar campo deployável
- [ ] `lce-432-2008/art-20/original` transcreve só o *caput* embora enderece o artigo inteiro. Fila de transcrição, fora do alcance de uma edição de regra
- [ ] Causa da incapacidade — o critério que separa esta regra da `regra-0009` não tem coluna. Depende da Q6. Aqui é o caso mais extremo do catálogo: **uma única chave de frontmatter** separa as duas, e é `integral` — [`achado-0026`](../achados/achado-0026.md)
- [ ] "Moléstia profissional" não é definida em lugar nenhum da LCE 432/2008 — [`achado-0025`](../achados/achado-0025.md)
