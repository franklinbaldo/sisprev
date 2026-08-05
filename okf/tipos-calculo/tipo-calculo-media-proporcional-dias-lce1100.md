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
      origem legada de `tipo-calculo-media-proporcional-dias-lce432` e
      `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias` — a última nem
      incide sobre uma média. Isso não reabre a derivação jurídica desta
      forma. O que falta é confirmação de que `Proporcionalidade Dias` (ou
      outro mecanismo do sistema) identifica esta fórmula sem ambiguidade
      material — dependência de implantação, registrada como
      `estado_implantacao: pendente_mapeamento_sisprev` nas regras propostas
      que usam esta forma (issue #122).
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

No Ciclo 1, descreve as unidades de causa comum das duas coortes da LCE
1.100/2021: com paridade para ingresso até 31/12/2003 e sem paridade para
ingresso a partir de 01/01/2004.

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
