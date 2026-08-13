---
type: Regra
id: regra-0102
row_index: 102
id_sisprev: '152'
nome_original: Voluntária por Tempo de Contribuição - Art. 6º da EC 41/03 c/c art. 4º da EC nº 146/21
nome: Voluntária · ingresso até 31/12/2003, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · integral · paridade
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
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
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 6º da Emenda Constitucional nº 41/2003 - fundamento - regra de transição - EC 41/03 - CF
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-6/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
precedentes:
  - identificador: 0052.070752/2022-46
    fonte: SEI
    parecer: /fontes-oficiais/processos-sei/0052_070752-2022-46/informação_1357__0055677294_.md
    observacao: >-
      A Informação 1357/2024/PGE-IPERON examina requerimento de aposentadoria
      voluntária de servidora (sexo feminino) que ingressou no serviço público
      em 13/05/2003. O cotejo direto confirma a transição do art. 6º da EC
      41/2003: requisitos cumpridos em 09/05/2013, opção expressa pela regra,
      proventos integrais calculados pela integralidade da última remuneração e
      paridade, com preservação pelo art. 4º da ECE 146/2021. Isso corresponde
      a `sexo: FEMININO`, `data_adm_ate`, `integral: S`, `paridade: S` e às
      janelas de direito desta regra. Não é precedente para a `regra-0101`,
      porque ela é o ramo masculino e os incisos I e II do art. 6º exigem
      limites de idade e contribuição distintos; o parecer trata de mulher e
      aplica o ramo feminino. A expressão "integralidade da última remuneração"
      confirma a natureza jurídica da totalidade do cargo efetivo, mas não
      demonstra qual enum `tipo_calculo` o motor Sisprev executa; a regra mantém
      `Remuneração de Contribuição` sem que este processo resolva a semântica do
      campo.
---

# Estado da análise

Ramo feminino da transição do art. 6º da EC 41/2003, divergindo da
`regra-0101` **apenas em `sexo`**. Os números que o sexo comanda estão nos
incisos I e II do próprio artigo: 55 anos de idade (contra 60) e 30 anos de
contribuição (contra 35); os incisos III e IV — 20 anos de efetivo exercício no
serviço público, 10 de carreira e 5 no cargo — não distinguem sexo.

Janelas e campos de resultado conferem contra o texto do art. 6º:
`data_adm_ate: 31/12/2003` é o corte de ingresso do *caput* (data de publicação
da emenda), `integral: S` e `tipo_calculo: Remuneração de Contribuição`
correspondem a "proventos integrais [...] totalidade da remuneração do servidor
no cargo efetivo", `data_direito_apos: 31/12/2003` é a vigência da emenda e
`data_direito_ate: 31/12/2024` o prazo verbatim do art. 4º da ECE 146/2021.
`apos_especial: N` é correto: a redução do magistério ressalvada pelo *caput* é
o que individua `regra-0103`/`0104`.

`paridade: S` está certo e sem dispositivo que o funde **nesta** fundamentação —
o parágrafo único do art. 6º foi revogado pelo art. 5º da EC 47/2005, e quem
manda aplicar o art. 7º da EC 41/2003 é o art. 2º da EC 47/2005, não citado e
não autorado. Registrado aqui, e não por remissão à `regra-0101`, porque a
lacuna é indiferente ao sexo e é assim que se perde metade de um par.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da EC 41/2003, lido na publicação do Planalto arquivada localmente (`planalto-emc41.htm`, sha256 `af74d433…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os três vínculos correspondem às três provisões citadas, nada a acrescentar nem a remover
- [x] `sexo: FEMININO` fundado nos incisos I e II do art. 6º: 55 anos e 30 de contribuição, contra 60 e 35 do ramo masculino
- [x] `data_adm_ate: 31/12/2003`, `data_direito_apos: 31/12/2003` e `data_direito_ate: 31/12/2024` conferidos, um a um, contra datas escritas nos dispositivos citados
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra o *caput* do art. 6º
- [x] `apos_especial: N` correto: a redução do magistério individua `regra-0103`/`0104`
- [ ] `paridade: S` sem dispositivo citado que o funde positivamente: depende do **art. 2º da EC 47/2005**, não citado e não autorado no bundle (o parágrafo único do art. 6º foi revogado pelo art. 5º da EC 47/2005)
- [ ] O "na forma da lei" do art. 6º não é preenchido: o art. 46 da LCE 432/2008, que as gêmeas de magistério citam, não aparece aqui
- [ ] Idade, tempo de contribuição, tempo de serviço público, carreira e cargo não têm coluna: a diferença por sexo que a lei manda não é conferível contra o cadastro (Q5)
- [ ] Vigência do art. 6º da EC 41/2003 depois de 13/11/2019 em aberto (art. 36, II da EC 103/2019); `ec-41-2003/art-6/original` sem janela declarada
- [ ] `ec-41-2003/art-6/original` transcreve só o *caput*: os quatro incisos estão fora do corpus
- [ ] `data_adm_apos: 01/01/1910` é sentinela inferior sem correspondência normativa, divergindo do 01/01/1950 usado em 79 regras
