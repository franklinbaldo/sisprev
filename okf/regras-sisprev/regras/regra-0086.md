---
type: Regra
id: regra-0086
row_index: 86
nome: Voluntária por Idade e Temp. de Contrib.- Art. 3º da EC 47/05 - FÓRMULA 85/95 e art. 4º da EC nº 146/21
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
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-47-2005/art-3/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

"Fórmula 85/95" no masculino: a transição do **art. 3º da EC 47/2005**,
preservada em Rondônia pelo **art. 4º da ECE 146/2021**. Quem ingressou no
serviço público até 16/12/1998 aposenta-se com proventos integrais e paridade
quando somar 35 anos de contribuição, 25 de efetivo exercício no serviço público,
15 de carreira e 5 no cargo, e atingir a idade de 60 anos **reduzida em um ano por
cada ano de contribuição que exceder os 35** — é essa redução que trava a soma
idade + contribuição em **95** para o homem (85 para a mulher, `regra-0085`).
`sexo` é a única coluna em que as duas diferem.

Armadilha de leitura, a mesma anotada na gêmea: nas oito regras vizinhas do art.
5º da ECE 146/2021 o índice ímpar é o masculino; **aqui é o contrário** —
`regra-0086` é MASCULINO. É o defeito de `nome` do
[`achado-0020`](../achados/achado-0020.md) (dimensão D2) numa forma que induz erro
em vez de apenas omitir.

O par gêmeo desta regra no 4º ciclo é `regra-0105`/`0106`: mesma fundamentação,
mesmos três vínculos, mesmos `integral`, `tipo_calculo`, `paridade` e
`data_adm_ate`, e janelas de direito incompatíveis — o
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
- [x] "FÓRMULA 85/95" do `nome` **conferida na fonte**: o inciso I exige 35 anos de contribuição se homem e 30 se mulher; o inciso III reduz a idade mínima da alínea "a" (60/55) "de um ano de idade para cada ano de contribuição que exceder a condição prevista no inciso I", o que trava a soma em 95/85
- [x] `sexo: MASCULINO` é critério que o dispositivo funda, nos incisos I (35 × 30 anos de contribuição) e III (redução sobre 60 × 55 anos)
- [x] `paridade: S` fundada no parágrafo único do art. 3º, que manda aplicar o art. 7º da EC 41/2003, autorado no corpus (`ec-41-2003/art-7/original`)
- [x] `tabelapontuacao: N` coerente: a soma 95 do art. 3º é fixa e resulta de redução de idade, não de tabela progressiva — ao contrário do art. 5º, V da ECE 146/2021, cujo somatório de pontos cresce 1 por ano e onde as regras gravam `S`
- [ ] [`achado-0035`](../achados/achado-0035.md): `data_direito_ate: 31/12/2099` e `data_direito_apos: 01/01/1950` são as duas sentinelas, contra o prazo de 31/12/2024 do art. 4º da ECE 146/2021 (que esta regra cita e vincula) e contra o art. 6º da EC 47/2005, que limita a retroatividade à vigência da EC 41/2003 (31/12/2003) — valor gravado por `regra-0105`/`0106`
- [ ] [`achado-0036`](../achados/achado-0036.md): o art. 12, II da ECE 146/2021 referenda expressamente a revogação do art. 3º da EC 47/2005 pelo art. 35, IV da EC 103/2019. Se o referendo satisfaz o art. 36, II da EC 103/2019 — conclusão jurídica sobre norma estadual, que esta auditoria não toma —, o fundamento primário desta regra caiu em 14/09/2021
- [ ] `tipo_calculo: Remuneração de Contribuição`: o art. 3º diz "proventos integrais" sem definir a base de cálculo, e o art. 7º da EC 41/2003 trata de reajuste, não de base. A base fecha por leitura sistemática, não por texto de dispositivo citado
- [ ] granularidade do vínculo: `ec-47-2005/art-3-par-unico` está autorado e é o texto que funda a `paridade: S`, mas a regra cita "artigo 3º" sem estreitar e o vínculo declarado é ao artigo. Convenção aberta desde o §7 da [conferência das doze](../../../docs/analysis/conferencia-criterio-dispositivo-transicao-ec41-ec47.md)
- [ ] `ec-47-2005/art-3/original` transcreve **só o *caput*** embora enderece o artigo inteiro: quem clica no vínculo lê um documento chamado "art. 3º" sem os três incisos que decidem o caso. Os incisos estão conferidos acima contra a fonte; transcrevê-los é ato próprio, não feito nesta rodada
- [ ] `ec-47-2005/norma.md` não tem `vigencia_inicio`. A fonte arquivada dá "Este texto não substitui o publicado no **DOU 6.7.2005**" e o art. 6º ("entra em vigor na data de sua publicação") — data conferida aqui, não autorada no documento da norma (item 5.1 da [semântica das janelas](../../../docs/analysis/semantica-das-janelas-temporais.md))
- [ ] 25 anos de efetivo exercício no serviço público, 15 de carreira e 5 no cargo (inciso II) **não têm coluna** no Sisprev — aferição manual, e criar coluna é alterar o sistema
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda competência, não critério de coluna. E a redação vinculada (EC 103/2019) **não tem a alínea "a"** a que o art. 3º da EC 47/2005 remete: essa alínea existe no corpus nas redações da EC 20/1998 e da EC 41/2003, e nenhum campo desta regra a cita — logo nada a propor, apenas a registrar
- [ ] **Divergência de conclusão** sobre `data_direito_ate`: a conferência da janela do art. 4º a tem por correta (direito adquirido), esta por errada (transição com prazo). Ver a seção "Divergência entre duas conferências" acima — a decisão precede qualquer edição do campo
