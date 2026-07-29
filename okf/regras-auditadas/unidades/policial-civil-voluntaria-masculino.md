---
type: UnidadeAuditada
id: policial-civil-voluntaria-masculino
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0078
predicados:
  sexo: masculino
  regime: transitorio-ece-146-2021
  marco_ingresso: ate-2019-11-13
taxonomias:
  - ref: /dispositivos/ece-146-2021/art-7-par-1/original.md
    papel: regra de transição — corte de ingresso até a vigência da EC 103/2019
  - ref: /dispositivos/ece-146-2021/art-7-par-3/original.md
    papel: integralidade dos proventos e paridade no reajuste
  - ref: /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
    papel: tempo de contribuição e de exercício policial exigidos do homem (30 e 20 anos)
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: competência e remissão à lei complementar do ente
projecao:
  fundamentacao_integral: >-
    Aposentadoria especial de policial, com proventos integrais (cálculo por
    integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda
    Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da
    Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da
    Constituição Federal, com a redação dada pela Emenda Constitucional nº
    103/2019 - regra transitória - idade + tempo de contribuição + homem.
proveniencia:
  fontes_consultadas:
    - https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp51.htm
    - /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
    - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
  notas: >-
    Correção proposta a partir do achado-0017. Duas trocas em relação à
    regra-0078: a alínea citada ("b" -> "a") e o descritor final ("mulher" ->
    "homem"). Nenhum outro campo muda.
decisoes:
  - data: 2026-07-29
    quem: franklinbaldo
    o_que: >-
      Propor a fundamentação com a alínea masculina, sem alterar a regra-0078.
      A unidade fica em `elaboracao`: nada é exportado, e a decisão de corrigir
      o campo deployável é de quem responde pelo produto.
confianca: alta
---

# O que esta unidade propõe

A `regra-0078` tem `sexo: MASCULINO` e cita a alínea **"b"** do art. 1º, II da
LC 51/1985 — que exige 25 anos de contribuição e 15 de exercício policial, "se
**mulher**". A alínea masculina é a **"a"**: 30 e 20 anos, "se homem". O texto
da regra ainda termina com o descritor "idade + tempo de contribuição +
**mulher**".

Esta unidade projeta a mesma regra com as duas trocas — a alínea e o
descritor. Nada mais muda: `integral`, `paridade`, `tipo_calculo`, as janelas e
o `nome` são os da origem.

O registro do defeito é o [`achado-0017`](../../regras-sisprev/achados/achado-0017.md).
Esta unidade é a outra metade: o achado diz o que está errado, a unidade diz
qual seria o certo, e as duas coisas ficam separadas de propósito.

# Por que uma unidade auditada, e não uma edição na regra

`FUNDAMENTACAO_INTEGRAL` é campo **deployável** — o texto que o Sisprev entrega
no documento do servidor. Editá-lo em `regra-0078` seria alterar o produto sem
que ninguém tivesse decidido alterá-lo, e o catálogo perderia o estado
anterior (a RFC 0006 registra que editar uma regra é destrutivo).

O catálogo auditado existe exatamente para isto: identidade própria, bundle
separado, e a regra legada **intocada em cardinalidade e identidade**. Enquanto
`estado_unidade` for `elaboracao`, nada aqui é compilado nem exportado — a
exportação operacional segue 100% do bundle legado.

# O que esta unidade não faz

- **Não altera a `regra-0079`.** A gêmea feminina cita a alínea "b"
  corretamente; o defeito não é dela.
- **Não toca a `regra-0084`.** Ela é `sexo: AMBOS` e o § 2º do art. 7º remete à
  LC 51 sem fixar tempo — o caso pede as **duas** alíneas, e provavelmente uma
  decomposição, não uma troca de letra. Fica para unidade própria.
- **Não afirma o que o motor faz.** `regra-0078` é `simulavel: S`, e nessa
  condição o motor não lê a fundamentação: tempo de contribuição e tempo de
  exercício policial não têm coluna. A correção é do documento entregue.
- **Não propõe promoção.** Passar de `elaboracao` a `preview` ou `deployable`
  exige decisão institucional que este documento não substitui.

# Conferência da fonte

O texto das duas alíneas foi conferido nos dispositivos autorados
(`lc-51-1985/art-1-inc-ii-al-a/lc-144-2014` e `.../al-b/...`), ambos com a nota
"(Incluído pela Lei Complementar n° 144, de 2014)". A publicação oficial no
Planalto **não pôde ser aberta** nesta sessão (HTTP 000 durante toda ela) — a
pendência está registrada em
[`fontes-oficiais/PENDENCIAS.md`](../../../fontes-oficiais/PENDENCIAS.md), onde
a LC 51/1985 é o primeiro item da fila justamente por causa deste caso.
