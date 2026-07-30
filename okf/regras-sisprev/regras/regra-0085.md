---
type: Regra
id: regra-0085
row_index: 85
nome: Voluntária · ingresso até 16/12/1998 · Feminino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_ate: 16/12/1998 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/1950 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 3º da Emenda Constitucional nº 47/2005, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-47-2005/art-3/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

"Fórmula 85/95": a transição do **art. 3º da EC 47/2005**, preservada em Rondônia
pelo **art. 4º da ECE 146/2021**. Quem ingressou no serviço público até
16/12/1998 aposenta-se com proventos integrais e paridade quando somar 30 anos de
contribuição (mulher), 25 de efetivo exercício no serviço público, 15 de carreira
e 5 no cargo, e atingir a idade de 55 anos **reduzida em um ano por cada ano de
contribuição que exceder os 30** — é essa redução que mantém a soma idade +
contribuição constante em **85** para a mulher (95 para o homem, `regra-0086`).

Uma armadilha de leitura, registrada porque o `nome` não a desfaz: nas oito
regras vizinhas do art. 5º da ECE 146/2021 o índice ímpar é o masculino; **aqui é
o contrário** — `regra-0085` é FEMININO e `regra-0086` é MASCULINO. É o defeito
de `nome` do [`achado-0020`](../achados/achado-0020.md) (dimensão D2: o sexo
nunca aparece no nome) numa forma que induz erro em vez de apenas omitir.

O par gêmeo desta regra no 4º ciclo é `regra-0105`/`0106`: mesma fundamentação,
mesmos três vínculos, mesmo `integral`, `tipo_calculo`, `paridade` e
`data_adm_ate`. Divergem nas janelas de direito, e essa divergência é o
[`achado-0035`](../achados/achado-0035.md).

## Divergência entre duas conferências, registrada em vez de resolvida

Duas conferências independentes alcançaram esta regra na mesma semana e
**concluíram o oposto** sobre `data_direito_ate: 31/12/2099`. A divergência fica
registrada porque ela é, ela própria, o achado — resolver por escolha silenciosa
apagaria o argumento do lado preterido.

A [conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)
conclui que a sentinela **está correta**: trata esta regra como *direito
adquirido puro*, cujos requisitos se completaram antes da EC 20/1998, e um
direito já adquirido não é alcançado por prazo criado em 2021.

A conferência de mérito desta regra conclui que a sentinela **está errada**, e o
[`achado-0035`](../achados/achado-0035.md) a registra.

O argumento que separa as duas é o significado de `data_adm_ate: 16/12/1998`.
Ele é o corte de **ingresso** — "que tenha ingressado no serviço público até 16
de dezembro de 1998", literal no *caput* do art. 3º —, e não a data em que os
requisitos se completam. Quem ingressou em 1998 soma os 30 anos de contribuição
do inciso I muito depois: em 2028, se começou a contribuir naquele ano. O art.
3º da EC 47/2005 é **regra de transição**, não direito adquirido.

E é a própria conferência da janela que fornece essa distinção, ao separar
`regra-0097`–`0100` — mesmo `data_adm_ate: 16/12/1998`, mas fechando em
31/12/2024 — dizendo que aquelas "são regra de *transição* (art. 2º da EC
41/2003), não direito adquirido". O art. 3º da EC 47/2005 é transição da mesma
espécie: corte de ingresso, requisitos escalonados, pontuação 85/95. Aplicada
consistentemente, a distinção da conferência da janela leva à conclusão oposta à
que ela tirou aqui.

Não é decisão desta seção. Fica como item aberto, e quem decidir precisa olhar
`regra-0105`/`0106` no mesmo ato: elas têm a mesma fundamentação e os mesmos
vínculos, e gravam `data_direito_apos: 31/12/2003` onde esta grava a sentinela
`01/01/1950`.

- [x] Critérios do cadastro percorridos um a um contra o art. 3º da EC 47/2005, na publicação oficial arquivada (`fontes-oficiais/arquivos/planalto-emc47.htm` — arquivo **cp1252**, não UTF-8; decodificar como UTF-8 devolve zero resultados sem erro)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: as três provisões citadas estão vinculadas, nada a acrescentar nem a remover
- [x] `data_adm_ate: 16/12/1998` é literal no *caput* do art. 3º ("que tenha ingressado no serviço público até 16 de dezembro de 1998")
- [x] `integral: S` fundado no *caput* ("poderá aposentar-se com proventos integrais")
- [x] "FÓRMULA 85/95" do `nome` **conferida na fonte**: o inciso I exige 30 anos de contribuição se mulher e 35 se homem; o inciso III reduz a idade mínima da alínea "a" (55/60) "de um ano de idade para cada ano de contribuição que exceder a condição prevista no inciso I", o que trava a soma em 85/95. A [conferência das doze de transição](../../../docs/analysis/conferencia-criterio-dispositivo-transicao-ec41-ec47.md) §5 registrava o nome como não sustentado por nada transcrito; está sustentado
- [x] `sexo: FEMININO` é critério que o dispositivo funda, nos incisos I (30 × 35 anos de contribuição) e III (redução sobre 55 × 60 anos). O §3 daquela conferência registrava `sexo` sem fundamento nas doze — era verdade sobre a transcrição do corpus, não sobre a norma
- [x] `paridade: S` fundada no parágrafo único do art. 3º, que manda aplicar o art. 7º da EC 41/2003, autorado no corpus (`ec-41-2003/art-7/original`)
- [x] `tabelapontuacao: N` coerente: a soma 85/95 do art. 3º é fixa e resulta de redução de idade, não de tabela progressiva. O contraste fecha contra o art. 5º da ECE 146/2021, cujo inciso V institui pontuação com acréscimo anual — e onde as regras gravam `S`
- [ ] [`achado-0035`](../achados/achado-0035.md): `data_direito_ate: 31/12/2099` e `data_direito_apos: 01/01/1950` são as duas sentinelas, contra o prazo de 31/12/2024 do art. 4º da ECE 146/2021 (que esta regra cita e vincula) e contra o art. 6º da EC 47/2005, que limita a retroatividade da Emenda à vigência da EC 41/2003 (31/12/2003) — que é o valor gravado por `regra-0105`/`0106`
- [ ] [`achado-0036`](../achados/achado-0036.md): o art. 12, II da ECE 146/2021 referenda expressamente a revogação do art. 3º da EC 47/2005 pelo art. 35, IV da EC 103/2019. Se o referendo satisfaz o art. 36, II da EC 103/2019 — conclusão jurídica sobre norma estadual, que esta auditoria não toma —, o fundamento primário desta regra caiu em 14/09/2021 e o que resta é a sobrevida do art. 4º, limitada a 31/12/2024
- [ ] `tipo_calculo: Remuneração de Contribuição`: o art. 3º diz "proventos integrais" sem definir a base de cálculo, e o art. 7º da EC 41/2003 trata de reajuste, não de base. A base fecha por leitura sistemática, não por texto de dispositivo citado
- [ ] granularidade do vínculo: `ec-47-2005/art-3-par-unico` está autorado no corpus e é o texto que funda a `paridade: S`, mas a regra cita "artigo 3º da Emenda Constitucional nº 47/2005" sem estreitar, e o vínculo declarado é ao artigo. Se uma citação ao artigo alcança o parágrafo único é decisão de convenção, aberta desde o §7 da conferência das doze
- [ ] `ec-47-2005/art-3/original` transcreve **só o *caput*** embora seus `componentes` enderecem o artigo inteiro: quem clica no vínculo desta regra lê um documento chamado "art. 3º" sem os três incisos que decidem o caso. Os incisos estão conferidos acima contra a fonte; transcrevê-los é ato próprio, não feito nesta rodada
- [ ] `ec-47-2005/norma.md` não tem `vigencia_inicio`. A fonte oficial arquivada dá "Este texto não substitui o publicado no **DOU 6.7.2005**" e o art. 6º ("entra em vigor na data de sua publicação") — data conferida aqui, não autorada no documento da norma. É o item 5.1 da [semântica das janelas](../../../docs/analysis/semantica-das-janelas-temporais.md)
- [ ] 25 anos de efetivo exercício no serviço público, 15 de carreira e 5 no cargo (inciso II) **não têm coluna** no Sisprev — a aferição é manual, e criar coluna é alterar o sistema
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte": funda a competência estadual para fixar idade mínima por emenda, não critério representado em coluna. Aqui o elo é mais frouxo que nas regras da ECE 146/2021, porque a idade desta regra vem do art. 3º da EC 47/2005 e da alínea "a" do inciso III **na redação da EC 20/1998**, não da redação de 2019 que a regra vincula
- [ ] **Divergência de conclusão** sobre `data_direito_ate`: a conferência da janela do art. 4º a tem por correta (direito adquirido), esta por errada (transição com prazo). Ver a seção "Divergência entre duas conferências" acima — a decisão precede qualquer edição do campo
