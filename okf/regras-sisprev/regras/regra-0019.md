---
type: Regra
id: regra-0019
row_index: 19
nome: Incapacidade · ingresso até 31/12/2003, requisitos a partir de 23/10/2021 · Ambos · integral · paridade
tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 23/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §8°, da Lei Complementar Estadual nº 1.100/2021 - fundamento - incapacidade - LCE 1.100/2021 (acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável, com ingresso antes de 2004)
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Efetivo
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-30-par-8/original.md
disposicao_de_achados:
  - achado: /achados/achado-0025.md
    disposicao: substituida
    substituida_por: incapacidade-lce1100-ingresso-ate-2003
    justificativa: >-
      O defeito é real e a substituição não o resolve, o que é exatamente o que
      `substituida` afirma: esta regra não continua, sem alegar que o problema
      desapareceu. A LCE 1.100/2021 define acidente em serviço no art. 30, § 5º, e
      relaciona as doenças graves no § 8º, mas não define moléstia profissional — a lacuna
      que o achado descreve permanece na lei e, portanto, nas substitutivas. O que a
      decomposição muda é a superfície: a moléstia profissional deixa de ser parte de uma
      célula de texto e passa a ser predicado próprio, com `protocolo_verificacao` que
      declara o que se afere e mediante que prova, e com fundamentação que diz
      expressamente que o nexo entre a doença e as condições de exercício do cargo é o que
      caracteriza a causa. A ausência de definição legal continua sendo questão para o
      legislador, não para a auditoria.
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
      No eixo de admissão esta regra grava `data_adm_ate: 31/12/2003`, que é o
      marco literal da lei e está correto; o defeito de `01/01/2004` é das duas
      regras do outro ramo.
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
---

# Estado da análise

Regime vigente da incapacidade permanente — art. 40, § 1º, I da CF na redação
da EC 103/2019 com a LCE 1.100/2021 —, na faixa de quem **ingressou até
31/12/2003** (`data_adm_ate: 31/12/2003`). Proventos integrais
(`integral: S`), calculados sobre a totalidade da remuneração do cargo
(`tipo_calculo: Valor Efetivo`) e reajustados com paridade (`paridade: S`).
`simulavel: N`: a seleção é humana, lendo a fundamentação.

**Esta é a regra do lote cujos artigos citados são os certos**, e vale dizê-lo
porque é o contraste que torna demonstrável o defeito da vizinha `regra-0022`.
Os arts. 25 e 27, I da LCE 1.100/2021 nomeiam no próprio corpo, e com a mesma
grafia, a classe "que tenha ingressado no serviço público em cargo efetivo
**até 31 de dezembro de 2003**" — que é exatamente a faixa desta regra. O art.
25 dá o `Valor Efetivo` ("corresponderá à totalidade da remuneração no cargo
efetivo") e o art. 27, I dá a `paridade: S` (reajuste "de acordo com o disposto
no art. 7° da Emenda Constitucional n° 41"). Três critérios fechados por dois
dispositivos, conferidos na compilação oficial arquivada em
`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`.

Duas coisas não fecham, e são de naturezas diferentes.

**A primeira é uma citação que falta.** A EC 103/2019 **retirou** do art. 40,
§ 1º, I o discriminante integral × proporcional que as redações de 1988, de
1998 e de 2003 tinham no próprio inciso — hoje o inciso só define a hipótese
("por incapacidade permanente para o trabalho, no cargo em que estiver
investido, quando insuscetível de readaptação"). Nesse regime quem discrimina é
o **art. 30, *caput*** da LCE 1.100/2021: proventos proporcionais "exceto se a
incapacidade for decorrente de acidente em serviço, moléstia profissional ou
doença grave, contagiosa ou incurável". É a exceção desse *caput* que produz o
`integral: S` desta regra — e ela cita apenas o **§ 8º** (o rol de dezesseis
doenças graves), que é uma das três classes da exceção, não a exceção. O
`art-30-caput` existe autorado no bundle e nenhuma das quatro regras do regime
vigente o cita.

**A segunda é uma tensão de cálculo que não se resolve com o que está
transcrito.** O § 13 do art. 30 — conferido na fonte oficial, e **sem
dispositivo autorado** em `okf/dispositivos/` — manda que o cálculo deste
benefício, quando a incapacidade decorre de uma das três causas, se dê "**na
forma do art. 24** desta Lei Complementar, ressalvado o direito adquirido a
outra fórmula". O art. 24 é a média das 80% maiores, isto é, `Valor Médio` — não
o `Valor Efetivo` que esta regra grava. Duas leituras são defensáveis: ou o art.
25 é a "outra fórmula" ressalvada, e então `Valor Efetivo` está certo; ou o § 13
prevalece, e está errado. **Não decido**, e não decidiria com honestidade sem os
§§ 13 e 14 transcritos e sem saber se o art. 25 conta como direito adquirido no
sentido do § 13.

O par com a `regra-0020` merece uma nota. As duas compartilham o
`fundamentacao_integral` **byte a byte**, e esta é a regra que aquele texto
descreve: "proventos integrais (cálculo por integralidade) e com paridade" casa
com `integral: S`/`paridade: S`. É a `regra-0020` que grava `integral: N`
carregando o texto do irmão, com a `fundamentacao_proporcional` vazia —
`achado-0009`, e problema dela, não desta.

- [x] Critérios do cadastro percorridos um a um contra a lei — [conferência `critério → dispositivo`](../../../docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md) §2.3, reconferida em 2026-07-29 contra a compilação oficial da LCE 1.100/2021
- [x] `dispositivos:` conferido contra o único campo de fundamentação preenchido, item a item: os quatro vínculos são exatamente as quatro provisões citadas — nada a acrescentar nem a remover
- [x] `data_adm_ate: 31/12/2003` fundado literalmente pelos arts. 25 e 27, I ("até 31 de dezembro de 2003"), e o `ATE` inclusivo cobre o próprio dia, que é a leitura do dispositivo
- [x] `paridade: S` fundada pelo art. 27, I (reajuste na forma do art. 7º da EC 41/2003)
- [x] `sexo: AMBOS` fecha por ausência — percorridos o art. 40, § 1º, I (EC 103/2019) e os arts. 25, 27 e 30 inteiros, nenhum distingue por sexo
- [x] `simulavel: N` é coerente com o que a regra pede: o discriminante desta faixa (causa da incapacidade) não está em coluna nenhuma, e com seleção humana o texto basta — por isso esta regra **não** entra no [`achado-0026`](../achados/achado-0026.md), que é sobre os pares `simulavel: S`
- [ ] `tipo_calculo: Valor Efetivo` × art. 30, § 13, que roteia o cálculo desta hipótese ao art. 24 (média). Depende de decidir se o art. 25 é a "outra fórmula" ressalvada, e de transcrever os §§ 13 e 14
- [ ] `integral: S` decorre da exceção do art. 30, *caput* — dispositivo que existe no bundle e que **nenhuma** das quatro regras do regime vigente cita, embora todas citem as suas exceções. Citação a decidir, campo deployável
- [ ] `data_direito_apos: 23/10/2021` não corresponde a marco nenhum: "23 de outubro" não aparece no texto oficial da LCE 1.100/2021 — [`achado-0024`](../achados/achado-0024.md). O lado do erro **deixou de ser indeterminado**: a publicação está identificada na ficha oficial do SAPL como DOE/RO nº 207, de 18/10/2021, logo o valor está cinco dias deslocado e é desta regra que ele sai. Quais datas concretas ficam de fora depende da semântica de `DATA_DIREITO_APOS` (Q2)
- [ ] `data_direito_ate: 31/12/2099` é sentinela e segue não interpretada (P5); `data_adm_apos: 01/01/1950` idem
- [ ] "Moléstia profissional", uma das três causas que produzem o `integral: S` desta regra, não é definida em lugar nenhum da LCE 1.100/2021, embora as outras duas classes o sejam no mesmo artigo — [`achado-0025`](../achados/achado-0025.md)
- [ ] §§ 13 e 14 do art. 30 a transcrever: são o roteador do cálculo do benefício nos dois ramos e não existem como dispositivo autorado. Ato de transcrição, não edição de regra
