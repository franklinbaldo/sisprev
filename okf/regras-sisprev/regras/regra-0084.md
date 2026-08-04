---
type: Regra
id: regra-0084
row_index: 84
id_sisprev: '134'
nome_original: Aposentadoria por Mandado de Injunção
nome: Voluntária · Policial penal · por mandado de injunção · Ambos · integral · média
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/1950 00:00
fundamentacao_proporcional: Artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigo 7º, § 2º e § 3º, da Emenda à Constituição Estadual nº 146/2021 e artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985.
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigo 7º, § 2º e § 3º, da Emenda à Constituição Estadual nº 146/2021 e artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985.
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
status_auditoria: revisada
auditado_por: franklinbaldo
auditado_em: 2026-07-30
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
disposicao_de_achados:
  - achado: /achados/achado-0020.md
    disposicao: corrigida
    justificativa: >-
      Corrigida pela renomeação do catálogo inteiro. Esta regra recebeu
      `nome` pelo padrão de facetas em ordem de anamnese — benefício, categoria
      especial, regime, e sexo quando gravado —, que é a resposta à questão 1 do
      achado ("qual padrão adotar"). A questão 4 dele — se a correção pertencia ao
      catálogo auditado da RFC 0004 em vez de a uma edição em `regra-*.md` — foi
      respondida pela coordenação em 2026-07-30: a auditoria está autorizada a alterar
      `nome`, e o registro está na Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`. Duas coisas que esta
      disposição **não** afirma: que o `P2_IGUALDADE_MATERIAL_ATIVA` sobre esta regra
      tenha sido tocado, se houver — `nome` está fora da chave material, então
      renomear é incapaz de criar ou dissolver grupo de igualdade material, e o
      baseline de `tests/test_achados_bundle.py` assevera isso; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0017.md
    disposicao: encaminhada
    justificativa: >-
      O defeito é real nesta regra e a conferência está fechada: as duas
      `FUNDAMENTACAO*` e o `dispositivos:` invocam a alínea "b" do art. 1º, II da
      LC 51/1985, que a lei reserva à mulher, enquanto a regra é `sexo: AMBOS`. O
      § 2º do art. 7º da ECE 146/2021 não fixa tempo de contribuição e manda
      buscá-lo naquela lei complementar, então, para o requerente homem, a única
      provisão que a regra invoca para o período adicional é a que não se aplica
      a ele.
      **Por que não é `corrigida`, ao contrário da `regra-0078`.** A Decisão 10
      de `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autoriza a auditoria
      a alterar `FUNDAMENTACAO*`, mas autorização para reescrever não é
      conhecimento do que escrever. Na `regra-0078` o texto correto era
      determinado — regra de um sexo só, alínea daquele sexo. Aqui não é:
      acrescentar a alínea "a" pressupõe que a regra alcance os dois sexos pelo
      regime da LC 51/1985, e o que esta regra aplica depende do provimento
      judicial que lhe dá nome, que não foi localizado. O levantamento em
      `docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md`
      chega a um candidato provável — o MI nº 1.545/DF —, e o próprio documento
      registra que o vínculo permanece inferencial e que aquele provimento
      determina análise à luz do art. 57 da Lei 8.213/1991, sem mencionar a LC
      51/1985. Corrigir sob essa incerteza seria inventar citação.
      **Por que não é `nao_se_aplica`.** O defeito se materializa aqui, e é nesta
      regra que ele é mais grave: `simulavel: N`, logo a triagem é humana e a
      fundamentação é justamente o que a pessoa lê para decidir.
      Duas coisas que esta disposição **não** afirma: que o motor afira 25/15 em
      vez de 30/20 — tempo de contribuição e tempo de exercício policial não têm
      coluna, e esta regra sequer é simulável; e que o achado esteja fechado —
      ele segue aberto, e esta é a única regra da população que ainda carrega o
      defeito.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: localizar o ato, parecer ou nota técnica
      que liga este cadastro ao provimento judicial que lhe dá nome. Sem ele não
      se sabe qual regime a regra aplica, e portanto nem qual citação a corrige.
  - achado: /achados/achado-0055.md
    disposicao: encaminhada
    justificativa: >-
      A divergência é fato do catálogo e está conferida: das treze regras que
      vinculam o § 1º, § 2º ou § 3º do art. 7º da ECE 146/2021, esta é a única
      que grava sentinela em `data_adm_ate`; oito gravam `13/11/2019`, que é a
      data que o *caput* nomeia, e quatro gravam outros dois valores. Sob a
      hipótese de trabalho declarada no achado — `DATA_ADM_*` é data de admissão,
      confirmado pela empresa responsável pelo Sisprev —, esta regra não recorta
      por entrada onde o dispositivo que ela vincula recorta, e o desvio é
      ampliativo: uma regra de transição sem a fronteira que a define deixa de
      ser transição.
      **Por que não é `corrigida`.** Gravar `13/11/2019` aqui seria a leitura mais
      simples e é justamente o que o achado se recusa a afirmar: quatro valores
      distintos convivem entre regras que declaram o mesmo vínculo, e enquanto
      não se souber por que `regra-0109`–`regra-0112` gravam `31/12/2024` e
      `31/12/2003` não se sabe se `13/11/2019` é o valor certo ou apenas o mais
      frequente. Escolher pela frequência é o modo de falha da RFC 0008 — leitura
      plausível gravada em campo deployável sem conferência que a sustente. Some-
      se a isso que o levantamento sobre o mandado de injunção registra a
      hipótese de esta regra ser cadastro antigo reparametrizado, caso em que a
      ausência de recorte teria causa própria e não seria lapso.
      **Por que não é `nao_se_aplica`.** O campo é deployável e a divergência é
      material — `data_adm_ate` integra a chave do `P2_IGUALDADE_MATERIAL_ATIVA`.
      Que a regra seja `simulavel: N` não afasta o defeito: desloca-o para o que
      o operador entende ao ver o campo, que é a questão 4 do achado.
      Esta disposição **não** afirma que alguma concessão tenha ocorrido fora do
      recorte — depende de caso concreto, que o catálogo não registra —, nem que
      `13/11/2019` seja o valor a gravar.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto, em duas frentes que a auditoria não fecha
      sozinha: por que `regra-0109`–`regra-0112` gravam datas diferentes com o
      mesmo vínculo de dispositivo, que é anterior a propor valor para esta
      regra; e se "admissão" e "ingresso na respectiva carreira" coincidem no
      Sisprev, já que o *caput* recorta pelo segundo e o campo marca o primeiro.
  - achado: /achados/achado-0058.md
    disposicao: encaminhada
    justificativa: >-
      Esta regra vincula o § 3º do art. 7º da ECE 146/2021 — totalidade da
      remuneração no cargo efetivo, com reajuste vinculado ao servidor em
      atividade — e grava `paridade: N` com `tipo_calculo: Valor Médio`, contra
      as dez regras do mesmo vínculo que gravam `paridade: S` com `Remuneração de
      Contribuição`.
      **Aqui a contradição é também interna, e é ela que impede corrigir.** A
      regra grava `integral: S` **e** `Valor Médio` no mesmo documento. Se a base
      é a média das maiores remunerações de 80% do período contributivo, não é a
      totalidade da remuneração do cargo efetivo, e `integral: S` deixa de
      descrever o que a regra faz. A combinação não corresponde a nenhum dos dois
      regimes do art. 7º, nem à hipótese do optante do § 16 que o achado registra
      para as outras duas regras da população. Enquanto não se souber o que ela
      pretendia afirmar, corrigir um dos dois campos é escolher por conveniência
      qual metade do documento é a verdadeira.
      **Some-se o que já está encaminhado nesta regra.** O `achado-0017` e o
      `achado-0055` também dependem de saber qual regime esta regra aplica, e a
      causa comum é a mesma: o provimento judicial que lhe dá nome não foi
      localizado. Três defeitos distintos convergindo no mesmo documento faltante
      é razão para encaminhar, não para arbitrar cada um deles em separado.
      **Por que não é `nao_se_aplica`.** Os campos são deployáveis e a
      incompatibilidade é legível no próprio documento. Que a regra seja
      `simulavel: N` desloca o efeito para a triagem humana, não o afasta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: o ato, parecer ou nota técnica que
      reconstrói o regime aplicado por esta regra. É o mesmo documento que o
      `achado-0017` e o `achado-0055` aguardam, e sem ele não se sabe se o que
      está errado é `paridade`, `integral`, `tipo_calculo` ou o vínculo com o
      § 3º.
---

# Estado da análise

Regra de aposentadoria especial de policial pela via de transição do art. 7º da
**ECE 146/2021**, com idade reduzida pelo § 2º (52 anos se mulher, 53 se homem)
mediante pedágio, e proventos pelo § 3º. Ao contrário das irmãs do mesmo artigo,
ela não recorta janela nenhuma: as quatro colunas de data são sentinela.

**A conferência do fundamento está fechada e achou três defeitos.** Nenhum deles
se corrige daqui, e a causa é comum: o `nome` da regra invoca um provimento
judicial que não foi localizado, e sem ele não se sabe qual regime ela aplica.

## Critério → dispositivo

A relação que `dispositivos:` achata. Quatro provisões vinculadas, e o que cada
uma funda:

| critério aferido                             | provisão                                                                                |
| -------------------------------------------- | --------------------------------------------------------------------------------------- |
| direito à aposentadoria especial de policial | CF, art. 40, § 1º, III, 2ª parte (EC 103/2019) — remete à lei complementar              |
| idade mínima reduzida                        | ECE 146/2021, art. 7º, § 2º                                                             |
| tempo de contribuição e pedágio              | LC 51/1985, art. 1º, II — por remissão do § 2º                                          |
| base de cálculo e reajuste                   | ECE 146/2021, art. 7º, § 3º                                                             |
| janela de ingresso                           | **nenhuma** — o *caput* recorta em 13/11/2019 e a regra não o vincula nem o parametriza |

As duas últimas linhas são os defeitos: o § 3º manda pagar a totalidade da
remuneração com paridade e a regra grava `paridade: N` com `Valor Médio`
([`achado-0058`](../achados/achado-0058.md)); o recorte do *caput* não aparece em
campo nenhum ([`achado-0055`](../achados/achado-0055.md)). A terceira linha
carrega o defeito do [`achado-0017`](../achados/achado-0017.md): a remissão do
§ 2º busca o tempo na LC 51/1985, e a única alínea que a regra nomeia é a
feminina, numa regra `sexo: AMBOS`.

- [x] Fundamento conferido provisão a provisão contra o texto transcrito no
  bundle, e o mapa `critério → dispositivo` escrito acima.
- [x] Os três defeitos autorados como achados bloqueantes e dispostos como
  `encaminhada`, cada um com o dono da decisão que falta nomeado.
- [x] `achado-0020` (padrão de `nome`) disposto como `corrigida`.
- [x] Nenhuma detecção mecânica ativa alcança esta regra — o
  `P9_SEXO_FUNDAMENTACAO` não dispara porque `sexo` é `AMBOS`, e é o ponto cego
  que o `achado-0017` registra por escrito.

`revisada` afirma que a auditoria terminou o que lhe cabia e registrou os
encaminhamentos, não que a regra esteja correta. Ela **não** pode receber
`validada`: são três bloqueantes `encaminhada` com pendência real, e
`encaminhada` nunca libera validação institucional. Todos os três aguardam o
mesmo documento do IPERON.
