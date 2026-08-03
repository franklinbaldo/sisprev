---
type: Regra
id: regra-0021
row_index: 21
nome: Incapacidade · ingresso após 01/01/2004, requisitos a partir de 23/10/2021 · Ambos · proporcional · Proporcionalidade Dias
tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE
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
data_adm_apos: 01/01/2004 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 23/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §§ 5° e 6º, da Lei Complementar Estadual nº 1.100/2021 (acidente em serviço com ingresso após 2003) | Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §8°, da Lei Complementar Estadual nº 1.100/2021 (doença grave, contagiosa ou incurável, com ingresso após 2003) | Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, da Lei Complementar Estadual nº 1.100/2021 (moléstia profissional com ingresso após 2003)
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: ''
disposicao_de_achados:
  - achado: /achados/achado-0009.md
    disposicao: substituida
    substituida_por: incapacidade-lce1100-ingresso-apos-2003
    justificativa: >-
      O defeito é real nesta regra: ela grava `integral: N` e deixa
      `FUNDAMENTACAO_PROPORCIONAL` vazia, de modo que o cálculo proporcional é aplicado
      sem que nenhum texto diga de onde ele vem. A regra não continua no catálogo: no
      lugar dela entram as substitutivas do grupo, que preenchem o campo correspondente ao
      ramo efetivamente aplicado — a unidade de causa comum traz
      `FUNDAMENTACAO_PROPORCIONAL` articulando o art. 30, § 14, e o art. 26 da LCE
      1.100/2021, e as unidades de causa qualificada trazem `FUNDAMENTACAO_INTEGRAL` pelo
      § 13. A alternativa entre as duas hipóteses que o achado levanta — lapso de
      preenchimento ou `integral` marcado errado — fica respondida pela decomposição: eram
      as duas coisas ao mesmo tempo, porque uma única regra cobria ramos com resultados
      opostos.
    decidido_por: franklinbaldo
    decidido_em: 2026-08-03
  - achado: /achados/achado-0026.md
    disposicao: substituida
    substituida_por: incapacidade-lce1100-ingresso-apos-2003
    justificativa: >-
      O defeito é real nesta regra e a substituição o dispõe por duas vias. A primeira é o
      que o achado pede: a causa da incapacidade deixa de ser critério sem coluna e passa
      a individuar cada substitutiva — acidente em serviço, moléstia profissional, causa
      comum e uma unidade por moléstia do rol do art. 30, § 8º —, de modo que os pares que
      só se distinguiam por campo de resultado deixam de existir. A segunda é a
      consequência imediata para o motor: as substitutivas gravam `simulavel: N`, e por
      isso nenhuma delas é oferecida à seleção automática sem que o critério que as separa
      esteja disponível. O problema que o achado descreve — o motor não ter como escolher
      entre regras cuja distinção não é predicado — não se reproduz, porque não há escolha
      automática a fazer.
    decidido_por: franklinbaldo
    decidido_em: 2026-08-03
  - achado: /achados/achado-0024.md
    disposicao: encaminhada
    justificativa: >-
      As duas conferências do achado estão fechadas contra fonte oficial
      arquivada, e nenhuma delas depende de hipótese sobre convenção de
      fronteira. `data_direito_apos: 23/10/2021` **não corresponde a marco nenhum**
      da LCE 1.100/2021: a publicação foi no DOE/RO nº 207, de **18/10/2021**,
      identificada na ficha da norma no SAPL/ALE-RO, e o texto da lei não contém a
      expressão "23 de outubro". O valor está cinco dias deslocado, e vinte e duas
      das vinte e seis regras que gravam um marco desta norma gravam 18/10/2021.
      `data_adm_apos: 01/01/2004` está errado pela mesma ordem de razão, e com
      consequência aritmética imediata. Os arts. 24, 25 e 27 da mesma lei nomeiam
      a fronteira no próprio corpo — "até" e "após **31 de dezembro de 2003**" —,
      e `DATA_ADM_APOS` é a coluna de marco **exclusivo**: gravar `31/12/2003` é
      que significa "admitido a partir de 01/01/2004". Gravando `01/01/2004` a
      cobertura desloca um dia, e **o dia 01/01/2004 não é alcançado por nenhuma
      das quatro regras** — nem pelas que fecham em 31/12/2003, nem por estas, que
      passam a abrir em 02/01/2004.
      **Por que não é `corrigida`, mesmo com os valores certos conhecidos.** As
      quatro colunas de data são **critério aferido**, não `nome` nem
      `FUNDAMENTACAO*`. A Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autorizou a auditoria a
      editar aqueles dois campos na regra e deliberadamente não estendeu a
      autorização — alterar critério continua passando pelo conjunto (RFC 0006),
      porque editar a regra legada apaga o que o operador de fato viu. Aqui a
      distância entre saber e poder é inteira: os dois valores certos estão
      escritos na norma, e nenhum deles pode ser gravado neste documento.
      **Por que não é `nao_se_aplica`.** O defeito é desta regra e está em campo
      que decide seleção — é a coluna de data que determina qual regra alcança um
      requerimento.
      Esta disposição **não** lê `data_direito_ate: 31/12/2099` como "sem limite":
      é sentinela, e a RFC 0011 não fixa a leitura dela. E **não** afirma qual dia
      concreto a janela corrigida passa a cobrir — isso depende da semântica de
      `DATA_DIREITO_APOS`, que segue aberta (Q2), enquanto o deslocamento de cinco
      dias vale sob qualquer convenção.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto, quanto ao ato de alterar as colunas de data
      — e a auditoria quanto ao veículo, que é um `Conjunto` com a regra
      substitutiva, não uma edição no documento legado. Fica registrado que a
      questão 3 do achado estreitou-se: a empresa responsável pelo Sisprev
      confirmou que `DATA_ADM_*` é data de admissão
      (`docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`), o que fixa o
      gênero do marco. Fontes oficiais posteriores fecharam a espécie jurídica:
      ingresso em cargo efetivo corresponde à posse; permanece sem teste apenas
      a coluna física lida pelo motor.
  - achado: /achados/achado-0050.md
    disposicao: encaminhada
    justificativa: >-
      A contradição está demonstrada contra a compilação oficial e alcança **três
      critérios independentes**. Esta regra é a do ingresso **após** 31/12/2003, e
      as três cláusulas do seu `fundamentacao_integral` citam, todas, os arts. **25
      e 27, I** da LCE 1.100/2021 — que o próprio texto reserva a quem ingressou
      **até** 31/12/2003. Os artigos do ramo desta regra, o 24 e o 27, II, não
      aparecem em nenhuma das três. O § 13 do art. 30 fecha por outra via: as três
      classes de causa que as cláusulas recortam são exatamente as três hipóteses
      dele, e ele manda calcular "na forma do art. 24".
      **Nesta regra há um agravante próprio.** Ela grava `integral: N` e
      `Proporcionalidade Dias`, e para incapacidade **não** decorrente das
      hipóteses do § 13 o roteador é o § 14, que manda calcular na forma do art.
      **26** — artigo que a regra também não cita. O achado registra que a
      investigação item a item desse agravante é limite do lote conferido, não
      conclusão fechada.
      **Por que não é `corrigida`, e a razão aqui é de método, não só de
      competência.** Há duas saídas opostas: ou a fundamentação troca os artigos,
      ou `tipo_calculo`, `paridade` e `data_adm_apos` é que estão errados. A
      Decisão 10 de `docs/analysis/decisoes-de-auditoria-2026-07-30.md` dá à
      auditoria competência para **exatamente uma** delas — a de `FUNDAMENTACAO*`
      —, e nenhuma para a outra, que é critério aferido. Executar a que se pode
      executar decidiria a questão 1 do achado **pela capacidade de quem edita, e
      não pelo mérito**, gravando no catálogo a aparência de que a direção foi
      escolhida. É o mesmo vício de fundo da RFC 0008 noutra forma.
      **Ordem, que a questão 4 registra.** A direção A da Q6 decompõe esta regra em
      uma linha por classe de causa. Corrigir antes de decompor conserta um texto;
      decompor antes replica a citação errada três vezes. A correção vem primeiro,
      e é mais um motivo para que ela não seja improvisada aqui.
      **Por que não é `nao_se_aplica`.** O texto entregue promete o regime mais
      vantajoso — base na última remuneração e reajuste paritário — enquanto o
      cadastro executa o outro, e nada no ato contradiz o texto para quem só lê o
      ato. É a combinação que produz litígio.
      Esta disposição **não** afirma qual lado cede, nem que a citação tenha sido
      herdada da irmã do outro ramo — a questão 2 registra a hipótese e não a
      verifica.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: qual lado cede — a fundamentação ou os
      campos de cálculo e janela. A auditoria só tem competência para um dos dois
      lados, e por isso não pode ser ela a decidir qual é. Fica registrado como
      trabalho de auditoria anterior à correção: transcrever os §§ 13 e 14 do art.
      30, que roteiam o cálculo deste benefício e não têm dispositivo autorado no
      bundle.
---

# Estado da análise

Regime vigente — art. 40, § 1º, I da CF na redação da EC 103/2019 combinado
com a LCE 1.100/2021 —, para quem ingressou **após** 31/12/2003
(`data_adm_apos: 01/01/2004`), sem paridade (`paridade: N`), com proventos
proporcionais apurados em dias (`integral: N`,
`tipo_calculo: Proporcionalidade Dias`).

Esta regra e a `regra-0022` são o único par do catálogo cujo
`fundamentacao_integral` empacota **três fundamentações numa célula só**,
separadas por `|`. As três compartilham o mesmo tronco — o art. 40, § 1º, I
na redação da EC 103/2019 e os arts. 25 e 27, inciso I da LCE 1.100/2021 — e
divergem **apenas** no recorte do art. 30, conforme a classe de causa da
incapacidade:

| cláusula | classe de causa                       | recorte do art. 30 citado               |
| -------- | ------------------------------------- | --------------------------------------- |
| 1        | acidente em serviço                   | `§§ 5º e 6º` (definição e equiparações) |
| 2        | doença grave, contagiosa ou incurável | `§ 8º` (rol de 16 doenças)              |
| 3        | moléstia profissional                 | "artigo 30", sem recorte                |

Conferido contra o texto transcrito em `okf/dispositivos/lce-1100-2021/`, as
três cláusulas são **ramos alternativos, não cumulativos**. O *caput* do
art. 30 manda proventos proporcionais "exceto se a incapacidade for
decorrente de acidente em serviço, moléstia profissional ou doença grave,
contagiosa ou incurável": a lista é uma **enumeração disjuntiva**, e cada
classe basta sozinha para afastar a regra geral. Os §§ 5º/6º e o § 8º não se
somam — o § 5º define "acidente em serviço" e o § 6º lista o que a ele se
equipara; o § 8º arrola as dezesseis doenças graves. Definem **duas das três
classes da mesma exceção**, e um requerimento concreto entra por uma delas,
apurada em perícia. Não são condições que se acumulem para conceder o
benefício.

Daí o `dispositivos:` vazio, e ele é deliberado. A união achatada das três
cláusulas — sete provisões — não é a citação de nenhuma delas: seria uma
lista em que `§§ 5º/6º` e `§ 8º` aparecem lado a lado como se a regra se
fundasse nos dois ao mesmo tempo, quando cada um pertence a um ramo que o
outro exclui. O que resolve isso não é um vínculo mais fino, é a
**decomposição em uma linha por classe de causa material** (Q6, direção A
já decidida em [`q6-causa-incapacidade.md`](../../../docs/analysis/q6-causa-incapacidade.md)
§10) — ato humano ainda não praticado, e o único momento em que faz sentido
falar em `dispositivos:` aqui.

Um segundo obstáculo, independente da Q6 e mais estreito: a cláusula 3 cita
"artigo 30" **sem recorte**, e o artigo inteiro não está autorado. O bundle
tem `art-30-caput` e os §§ 1º, 2º, 5º, 6º e 8º, nunca `lce-1100-2021/art-30`.
Vincular o *caput* no lugar seria **estreitar** uma citação que a prosa
deixou larga — o inverso da convenção `ESTREITADA` (a prosa estreita, o
vínculo aponta a provisão inteira). O precedente contrário está na
`regra-0008`, cuja `fundamentacao_proporcional` cita "o artigo 20" sem
recorte e vincula `lce-432-2008/art-20/original`, documento do artigo
inteiro, que existe.

A conferência `critério → dispositivo` das sete regras restantes de
incapacidade está em
[`conferencia-criterio-dispositivo-incapacidade-restantes.md`](../../../docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md)
§2.4; o que segue registra o que ela apurou para esta regra.

- [x] As três cláusulas do `fundamentacao_integral` separadas pelo `|` e conferidas uma a uma contra o texto em `okf/dispositivos/lce-1100-2021/`
- [x] Ramos **alternativos**, não cumulativos: as três classes são a exceção disjuntiva do art. 30, *caput*, e cada uma basta sozinha
- [x] Tronco comum às três cláusulas isolado (art. 40, § 1º, I/EC 103/2019 + arts. 25 e 27, I); só o recorte do art. 30 varia
- [ ] `dispositivos:` mantido vazio — a união achatada das três cláusulas não é a citação de nenhuma delas. Depende da decomposição em linha por classe de causa (Q6, direção A)
- [ ] "artigo 30" sem recorte (cláusula 3) não tem dispositivo autorado: existem `art-30-caput` e os §§, não o artigo inteiro
- [ ] Nenhum dispositivo, em nenhum dos dois regimes estaduais, define "moléstia profissional" — a classe da cláusula 3 fica sem base transcrita (P-6)
- [ ] O único texto de fundamentação que esta regra carrega afirma "proventos integrais (cálculo por média)", e ela grava `integral: N` / `Proporcionalidade Dias`; `fundamentacao_proporcional` está vazia (`achado-0009`, aberto). Qual lado cede depende da Q7
- [ ] Os arts. 25 e 27, I citados pelas três cláusulas são, no próprio texto, do ramo "até 31 de dezembro de 2003"; esta regra é do ramo "após" (P-5). Os artigos do ramo correto — 24, 26 e 27, II — existem no bundle e não são citados
- [ ] `data_direito_apos: 23/10/2021` não é fundado por nenhum dispositivo citado: a LCE 1.100/2021 vige desde 18/10/2021 — publicação identificada na ficha oficial do SAPL como DOE/RO nº 207, de 18/10/2021 — e a EC 103/2019 desde 13/11/2019. O valor está cinco dias deslocado e é desta regra que ele sai; quais datas concretas ficam de fora depende da Q2. Ver [`achado-0024`](../achados/achado-0024.md)
- [ ] `nome` idêntico ao da `regra-0022` (`P1_NOME_REPETIDO`); o que separa as duas é só o resultado (`integral`, `tipo_calculo`), e o critério que o determina — a causa — não tem coluna. Q6
