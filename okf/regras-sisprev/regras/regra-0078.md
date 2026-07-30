---
type: Regra
id: regra-0078
row_index: 78
nome: Voluntária do Policial Civil - Art. 7º, § 3º da EC nº 146/2021
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
data_adm_ate: 13/11/2019 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória - idade + tempo de contribuição + mulher.
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Artigo 7º, §§1º e 3º da Emenda Constitucional Estadual nº 146/2021
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-1/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
disposicao_de_achados:
  - achado: /achados/achado-0017.md
    disposicao: encaminhada
    decisao_pendente_de: IPERON, como titular do produto Sisprev
    justificativa: >-
      Conferência fechada contra a fonte, e o defeito é real nesta regra. As
      duas alíneas do art. 1º, II da LC 51/1985 na redação da LC 144/2014
      estão transcritas no bundle: a **"a"** exige 30 anos de contribuição e
      20 de exercício policial, "se homem"; a **"b"**, 25 e 15, "se mulher".
      Esta regra é `sexo: MASCULINO` e o `fundamentacao_integral` cita a "b",
      terminando no descritor "mulher" — o texto entregue invoca a provisão
      que a lei reserva ao outro sexo. Não há dúvida de mérito a resolver.
      O que resta **não é da auditoria**: `FUNDAMENTACAO_INTEGRAL` é campo
      deployável, e reescrevê-lo aqui alteraria o produto sem que ninguém
      tivesse decidido alterá-lo. A correção está escrita e conferida como
      unidade auditada
      (`policial-civil-voluntaria-masculino`), que compila `deployable` e
      difere desta regra em exatamente uma coluna; ela é carregada pelo grupo
      `policial-civil-alinea-masculina` do conjunto
      `proposta-auditoria-2026-07`, que segue `proposto`. Adotá-la é ato de
      quem responde pelo produto. Duas coisas que esta disposição **não**
      afirma: que o motor afira 25/15 em vez de 30/20 (tempo de contribuição
      e tempo de exercício policial não têm coluna, e esta regra é
      `simulavel: S`, condição em que o motor não lê a fundamentação); e que
      o achado esteja resolvido — ele segue aberto, e alcança a `regra-0084`,
      cujo provimento judicial não foi localizado.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---

# Estado da análise

Aposentadoria especial de policial civil pela regra de transição do art. 7º da
**ECE 146/2021**, com integralidade e paridade pelo § 3º, para quem ingressou
até 13/11/2019 e adquiriu o direito a partir de 14/09/2021. O tempo exigido não
está na emenda: o art. 40, § 1º, III da CF, na redação da EC 103/2019, remete à
lei complementar, e é a **LC 51/1985** que o fixa — por sexo, em duas alíneas.

**A conferência do fundamento está fechada, e achou o defeito.** Esta regra é
`sexo: MASCULINO` e cita a alínea feminina. A alínea masculina é a "a", e não é
vinculada por regra nenhuma do catálogo. Está registrado no
[`achado-0017`](../achados/achado-0017.md), a correção está escrita como
unidade auditada, e a disposição no frontmatter diz de quem é a decisão que
falta.

- [x] Fundamento conferido contra a fonte transcrita — as duas alíneas do art.
  1º, II da LC 51/1985 (redação da LC 144/2014) estão no bundle, e a citada não
  é a do sexo declarado.
- [x] Defeito autorado como achado (`achado-0017`) e correção autorada como
  unidade (`policial-civil-voluntaria-masculino`), com a projeção conferida
  coluna a coluna contra esta regra.
- [x] Disposição do achado bloqueante registrada, com dono nomeado para a
  decisão que falta.
- [ ] **`nome` colide com a `regra-0079`** (`P1_NOME_REPETIDO`): as duas se
  chamam "Voluntária do Policial Civil - Art. 7º, § 3º da EC nº 146/2021", e
  nada no nome diz qual sexo cada uma afere. Resolver isso é editar as **duas**
  regras, e a gêmea não é origem do grupo desta correção — fica para a decisão
  de `nome` do [`achado-0020`](../achados/achado-0020.md).
- [ ] **Vínculo critério → dispositivo não escrito.** `dispositivos:` registra
  as quatro provisões que a fundamentação cita, mas não qual funda qual
  critério. A idade mínima, o tempo de contribuição, o tempo de exercício
  policial e a integralidade vêm de provisões diferentes, e esse mapa é
  conferência humana em prosa — ainda não feita aqui.

Estes dois itens abertos são o que impede `revisada`, e é por isso que o
`status_auditoria` não subiu nesta rodada. O achado bloqueante já não é o
obstáculo: ele está disposto, e `encaminhada` libera `revisada`. O que falta é
menos grave e mais chato — uma colisão de nome que arrasta a gêmea e um mapa de
fundamentação que ninguém escreveu.
