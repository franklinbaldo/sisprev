---
type: Regra
id: regra-0007
row_index: 7
id_sisprev: '56'
nome: Invalidez · requisitos a partir de 31/12/2003 · Ambos · proporcional · Proporcionalidade Dias
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
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: Art. 20, §14º e Art. 45 da Lei Complementar nº 432/2008
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-20-caput/original.md
  - /dispositivos/lce-432-2008/art-20-par-14/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
precedentes:
  - identificador: 0029.237532/2020-34
    fonte: SEI
    parecer: /fontes-oficiais/processos-sei/0029_237532-2020-34/informação_123__0056908055_.md
    observacao: >-
      A Informação 123/2025 registra ingresso no cargo estadual em 23/04/2009,
      incapacidade permanente atestada em 21/03/2018 e patologias não enquadradas
      no rol de doença grave do art. 20, §9º, da LCE 432/2008. A conclusão é por
      proventos proporcionais, calculados pela fração do art. 17 sobre a média do
      art. 45, e sem paridade pelo art. 62. O cotejo confirma `integral: N`,
      `Proporcionalidade Dias` e `paridade: N` desta regra. A Informação descreve
      a fração em tempo, não o nome do enum; a correspondência com
      `Proporcionalidade Dias` é, portanto, uma inferência operacional compatível,
      não uma afirmação textual do documento. Não é precedente para a regra-0006:
      o caso não teve proventos integrais nem doença qualificada.
disposicao_de_achados:
  - achado: /achados/achado-0022.md
    disposicao: encaminhada
    justificativa: >-
      A conferência está fechada e a correção é **determinada**: esta regra funda
      os requisitos em legislação anterior à ECE 146/2021, invoca o art. 4º dessa
      emenda — que é o dispositivo que preserva aquela legislação — e grava
      `data_direito_ate` sentinela, onde o próprio art. 4º exige que os requisitos
      "sejam cumpridos até 31 de dezembro de 2024". O valor devido é `31/12/2024`,
      e o catálogo já pratica essa leitura em doze das vinte e quatro regras que
      vinculam o art. 4º.
      **Por que encaminhar mesmo com a correção sabida.** `data_direito_ate` é
      **critério aferido**, não `nome` nem `FUNDAMENTACAO*`. A Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autorizou a auditoria a
      editar aqueles dois campos na regra e **explicitamente não estendeu a
      autorização a mais nenhum**: alterar critério aferido continua passando pelo
      conjunto (RFC 0006), porque editar a regra legada apaga o que o operador de
      fato viu. A distância entre "saber o valor certo" e "poder gravá-lo aqui" é
      de competência e de veículo, não de conhecimento — e é por isso que esta
      disposição não é `corrigida`.
      **Por que não é `nao_se_aplica`.** O defeito é desta regra: a janela aberta
      permite ao Sisprev conceder benefício sob requisitos cujo prazo de
      implementação o dispositivo invocado encerrou.
      Esta disposição **não** afirma que o valor sentinela seja "sem limite" — a
      RFC 0011 não fixa a leitura dele, e o que se afirma é que o dispositivo
      invocado fecha e o campo não acompanha.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto, quanto ao ato de alterar `data_direito_ate`
      — e a auditoria quanto ao veículo, que é um `Conjunto` com a regra
      substitutiva, não uma edição no documento legado.
  - achado: /achados/achado-0049.md
    disposicao: encaminhada
    justificativa: >-
      O defeito é real e a conferência foi feita contra as publicações oficiais
      arquivadas, não contra o corpus. Esta regra cita, na mesma frase, duas
      redações do art. 40, § 1º da CF que **nunca vigeram juntas** — a do inciso I
      pela EC 41/2003, que valeu até 12/11/2019, e a do inciso III pela EC
      103/2019, que começou no dia seguinte —, e o inciso III, nas duas metades e
      em qualquer redação, é de **aposentadoria voluntária por idade**. Esta regra
      concede por incapacidade e não afere idade em campo nenhum, então a leitura
      que salva a citação do inciso III noutras famílias — norma de competência
      que remete ao Estado a fixação da idade mínima — aqui não tem a que se
      ligar.
      **Por que não é `corrigida`, embora a Decisão 10 autorize o ato.** A saída
      mais simples é retirar a citação do inciso III, e a conferência não encontra
      critério que a perda desmontaria. Mas a questão 2 do achado levanta uma
      hipótese testável e não testada: que o pretendido fosse o art. 40, § 1º,
      **I** na redação da EC 103/2019 — o inciso da incapacidade no regime novo —,
      caso em que o defeito é de **inciso**, não de matéria, e apagar destruiria a
      pista em vez de corrigir o texto. Apagar e substituir são atos diferentes
      com consequências diferentes sobre o que a regra passa a afirmar, e escolher
      entre eles sem testar a hipótese é decidir por conveniência.
      **Por que não é `nao_se_aplica`.** `FUNDAMENTACAO*` é o texto que chega ao
      ato de concessão. O dano é de **justificação**, não de seleção — nenhum
      critério aferido depende do inciso III —, e num benefício concedido por
      incapacidade permanente a motivação é sindicável.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: se a citação do inciso III deve **sair** ou
      ser **substituída** pelo inciso I na redação da EC 103/2019. A auditoria tem
      competência para o ato desde a Decisão 10, e não tem o fato que decide qual
      dos dois é.
---

# Estado da análise

Mesma família da `regra-0006` — art. 40, § 1º, I na redação da EC 41/2003,
sem corte de ingresso, sem paridade —, com o resultado invertido: proventos
proporcionais (`integral: N`), fração apurada em dias
(`tipo_calculo: Proporcionalidade Dias`).

Esta é a única das quatro regras de invalidez com o campo `fundamentacao`
preenchido: "Art. 20, §14º e Art. 45 da Lei Complementar nº 432/2008". É de
lá que vem o vínculo `lce-432-2008/art-20-par-14/original`, que a
`regra-0006` não tem — a diferença no `dispositivos:` das duas é
consequência direta de uma diferença de campo, não de critério. O cálculo em
dias é fundado pelo art. 17, § 2º ("em número de dias") somado ao § 14 do
art. 20.

Vale o mesmo alerta da vizinha, na direção oposta: `integral: N` não faz
desta "a regra proporcional". Ela carrega a `fundamentacao_integral` também,
palavra por palavra igual à da `regra-0006`. O par difere apenas em campos de
resultado; o critério que o justifica — a causa da incapacidade — mora dentro
do parêntese de um texto compartilhado.

Reconferência de 2026-07-29 contra as publicações oficiais arquivadas em
`fontes-oficiais/`. Um cuidado que ela acrescentou: o campo `fundamentacao`
desta regra cita "Art. 20, **§14º** e Art. 45", e o § 14 do art. 20 diz, no
texto oficial, que "a forma de cálculo desse benefício dar-se-á na forma do
art. 45, ressalvado o disposto no art. 51" — isto é, **os dois dispositivos que
o campo cita levam à média das 80% maiores**, que é o `Valor Médio` da
`regra-0006`, não a `Proporcionalidade Dias` desta. Quem funda a fração em dias
é o art. 17, § 2º ("os períodos de tempo utilizados no cálculo previsto neste
artigo serão considerados em número de dias"), citado pela
`fundamentacao_proporcional` e vinculado. A articulação fecha — art. 17 dá a
fração, art. 45 dá o valor sobre o qual ela incide (art. 17, § 1º diz isso
expressamente) —, mas o campo `fundamentacao` sozinho aponta para o cálculo da
regra vizinha.

O art. 4º da ECE 146/2021 **passou a ser conferível** depois desta rodada: a
transcrição pesquisável foi arquivada, e a
[conferência da janela](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)
fechou o prazo de 31/12/2024 contra o texto oficial.

- [x] Critérios do cadastro percorridos um a um contra a lei — conferência `critério → dispositivo` de 0006–0009
- [x] `dispositivos:` conferido contra `fundamentacao_integral`, `fundamentacao_proporcional` e `fundamentacao`, item a item: nada a acrescentar nem a remover
- [x] O dispositivo a mais em relação à `regra-0006` (`art-20-par-14`) é citado pelo campo `fundamentacao` desta regra
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado mas não funda critério representado nas colunas — o inciso III é de aposentadoria voluntária por idade
- [x] Janela do art. 4º da ECE 146/2021 conferida contra a transcrição oficial ([conferência](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)): o dispositivo funda os requisitos desta regra (art. 40, § 1º, I, da CF na redação da EC 41/2003, anterior à EC 146) e os prazeia em 31/12/2024. O "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
- [x] `tipo_calculo: Proporcionalidade Dias` conferido na fonte oficial: art. 17, § 2º da LCE 432/2008 manda contar os períodos "em número de dias", e o § 1º manda aplicar a fração sobre o valor do art. 45
- [x] `sexo: AMBOS` fecha por ausência — nenhum dispositivo da cadeia de incapacidade citado distingue por sexo
- [ ] Citação do art. 40, § 1º, III (EC 103/2019): não funda critério representado nas colunas **e** é redação que nunca coexistiu com a do inciso I também citado — [`achado-0022`](../achados/achado-0022.md)
- [ ] O campo `fundamentacao` ("Art. 20, §14º e Art. 45") aponta, sozinho, para o cálculo por média — o da `regra-0006` —, e não para a fração em dias desta regra. Não é vínculo a mexer (o campo cita o que cita); é redação de campo deployável, decisão do dono
- [ ] Se a janela desta regra deveria fechar em 12/11/2019, último dia da redação do inciso I que ela cita
- [ ] Causa da incapacidade — o critério que separa esta regra da `regra-0006` não tem coluna. Depende da Q6. Consequência operacional em [`achado-0026`](../achados/achado-0026.md)
- [ ] "Moléstia profissional" não é definida em lugar nenhum da LCE 432/2008 — [`achado-0025`](../achados/achado-0025.md)
