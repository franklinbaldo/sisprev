---
type: TipoCalculo
id: tipo-calculo-media-proporcional-dias-lce1100
nome: Média contributiva da LCE 1.100/2021, limitada e proporcional ao tempo em dias
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 2
    dispositivos:
      - /dispositivos/lce-1100-2021/art-26/original.md
      - /dispositivos/lce-1100-2021/art-30-par-14/original.md
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24-par-10/original.md
origem_legada:
  - tipo_calculo: Proporcionalidade Dias
    fidelidade: parcial
    justificativa: >-
      A fórmula está integralmente determinada acima: média do art. 24
      limitada pelo teto do § 10, proporcionalizada pela fração do art. 26 —
      é o que `nome`, no frontmatter, já nomeia sem ambiguidade,
      independentemente do rótulo do Sisprev. `Proporcionalidade Dias` é o
      valor legado observado — o único que o Sisprev já grava para esta
      hipótese — e nomeia corretamente o ajuste, mas não a base nem o
      limite. O mesmo valor também é gravado, no catálogo legado, pela
      origem legada de `tipo-calculo-media-proporcional-dias-lce432`,
      `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias` — que nem
      incide sobre uma média — e, dentro da própria LCE 1.100/2021, por
      `tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100` — que
      descreve a mesma hipótese jurídica (causa comum, art. 26) para a
      coorte de ingresso até 31/12/2003, com base diferente (remuneração do
      cargo, não média; revisão de 2026-08-05, abaixo). Isso não reabre a
      derivação jurídica desta forma. A origem legada desta forma
      (`regra-0021`) já grava, em produção, essa mesma combinação para a
      causa comum da coorte de ingresso após 2003 da LCE 1.100/2021 —
      evidência concreta de que o Sisprev já executa algum mecanismo para
      ela. O que falta é confirmação, em homologação prática, de que a
      execução aplica a base composta (média limitada pelo teto, então
      proporcionalizada) e não uma proporcionalidade nua — ressalva de
      homologação, registrada como `estado_implantacao: confirmada_com_ressalva` e `ressalva_homologacao` na regra proposta que usa
      esta forma (issue #122). Não bloqueia a entrada dela na carga de
      homologação; condiciona a ativação em produção.
  - tipo_calculo: Tipo Cálculo Nova Previdência
    fidelidade: parcial
    justificativa: >-
      Absorvido de `tipo-calculo-media-80-proporcional-dias-lce1100`
      (consolidado aqui): a mesma base (`media_remuneracoes_contribuicao`,
      80%, competência inicial 1994-07), o mesmo limitador
      (`teto_remuneracao_cargo_efetivo`, art. 24, § 10) e o mesmo ajuste
      (`proporcional_tempo_contribuicao`, art. 26) que este documento já
      descrevia sob o rótulo `Proporcionalidade Dias` — a única diferença
      material era a ausência do limitador na decomposição anterior deste
      documento, agora corrigida. Nenhuma regra proposta viva projeta este
      rótulo; preservado porque documenta uma proveniência legada distinta
      observada no catálogo.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O § 14 do art. 30 encaminha a incapacidade decorrente de causa comum ao art. 26.
Esse artigo manda aplicar uma fração sobre os proventos previamente calculados
na forma do art. 24, **observando-se, previamente, a aplicação do limite de
que trata o § 10** do art. 24 — é o próprio § 1º do art. 26 que fixa essa
precedência, não uma leitura desta auditoria. A base é, portanto, a média das
maiores remunerações de contribuição correspondente a 80% do período
contributivo, limitada pela remuneração do cargo efetivo; o ajuste é a razão,
em dias, entre o tempo total de contribuição e o tempo exigido para a
aposentadoria voluntária de referência, aplicada sobre a base já limitada.

A remissão especial do § 14 alcança a incapacidade; o art. 27 trata somente do
reajuste posterior e não muda esta fórmula de concessão. Assim, a mesma forma
pode conviver com paridade ou sem paridade, conforme a coorte de ingresso.

# Fórmula

```
média = média_das_maiores_remunerações_de_contribuição
base_limitada = min(média, remuneração_cargo_efetivo)  # art. 24, § 10; precedência fixada pelo art. 26, § 1º
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base_limitada × fração
```

Os períodos são considerados em dias. A proporção é limitada a 1 porque reduz o
provento e não cria valor superior à base limitada.

# Entradas e saídas

Entradas: remunerações contributivas, período contributivo, remuneração do
cargo efetivo, tempo de contribuição em dias e tempo exigido em dias para a
aposentadoria voluntária de referência.

Saída: provento inicial mensal proporcional, em moeda, nunca superior à base
limitada. Paridade ou reajuste sem paridade não são saída desta forma;
pertencem ao regime de manutenção do benefício.

# Onde esta forma é usada

Descreve a unidade de causa comum da família de ingresso de 01/01/2004 a
05/11/2018 **sem adesão ao regime de previdência complementar**
(`incapacidade-lce1100-2004-ate-2018-sem-rpc-causa-comum`), sem paridade.

Esta forma **não** carrega o limite máximo dos benefícios do RGPS: o art. 24,
§ 11, alcança o segurado sujeito ao regime de previdência complementar, e o
§ 12, quem ingressou a partir de 6 de novembro de 2018 — duas condições que
esta família exclui. A unidade de causa comum sujeita àquele teto é descrita
por `tipo-calculo-media-proporcional-dias-teto-rgps-lce1100`, que tem a mesma
base e **um limitador a mais**.

**Revisão de 2026-08-05 (revisão jurídica adicional da coordenação).** Até
esta data, este documento também descrevia a unidade de causa comum da
coorte de ingresso até 31/12/2003, com paridade. A coordenação apontou que
essa leitura — base no art. 24 (média) combinada com paridade do art. 27, I
— altera a fórmula que `regra-0020` já grava em produção para a mesma
hipótese (`tipo_calculo: Proporcionalidade Dias`, sem indicar média), conflita
com o art. 25 (que rege expressamente essa coorte) e carece de jurisprudência
específica. A unidade daquela coorte passa a ser descrita por
`tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100`, que preserva a
coerência de regime com as causas qualificadas da mesma coorte (base na
remuneração do cargo, com paridade). Esta forma continua correta e em uso
para a coorte após 2003, cuja base no art. 24 nunca esteve em disputa.

# Consolidação

Este documento absorveu `tipo-calculo-media-80-proporcional-dias-lce1100`
(retirado): os dois descreviam, dentro da LCE 1.100/2021, a mesma base, o
mesmo limitador e o mesmo ajuste, na mesma ordem, para o mesmo resultado
jurídico — a diferença entre eles era que este documento, antes desta
correção, omitia o limitador do § 10 na decomposição estruturada
(`limitadores: []`), embora o § 1º do art. 26 o exigisse. Corrigida essa
omissão, os dois eram o mesmo `TipoCalculo` sob rótulos legados diferentes
(`origem_legada`, acima) — não duas fórmulas distintas. O documento
absorvido não tinha regra proposta viva.
