---
type: FormaCalculo
id: forma-calculo-media-proporcional-dias-lce432
nome: Média contributiva da LCE 432/2008, proporcional ao tempo em dias
base:
  tipo: media_remuneracoes_contribuicao
  dispositivos:
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    dispositivos:
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    O rótulo legado expressa a fração em dias, mas não informa que ela incide
    sobre a média contributiva calculada na forma do art. 45. A fórmula completa
    depende dos dois componentes.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O art. 45 fornece a base: média aritmética simples das maiores remunerações que
serviram de base às contribuições, correspondente a 80% do período contributivo.
O art. 17 determina que os proventos proporcionais usem uma fração cujo
numerador é o tempo total de contribuição e cujo denominador é o tempo exigido
para a aposentadoria voluntária correspondente. O § 2º manda considerar os
períodos em dias.

Esta autoria está fechada para a redação do art. 45 dada pela LCE 672/2012. O
segmento anterior da LCE 432/2008 permanece dependente da transcrição da redação
do art. 45 então vigente.

# Fórmula

```
base = média_das_maiores_remunerações_de_contribuição
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base × fração
```

A proporção reduz a base e nunca a amplia. Eventuais limitadores do art. 45
precisam ser aplicados na ordem indicada pela redação temporalmente aplicável;
eles não foram autorados como componente desta forma porque o dispositivo
específico ainda não está transcrito no corpus.

# Entradas e saídas

Entradas: remunerações contributivas do período, quantidade de competências que
compõem os 80%, tempo de contribuição em dias e tempo exigido em dias para a
aposentadoria voluntária de referência.

Saída: provento mensal proporcional, em moeda, nunca superior à base média.

A forma não resolve sozinha qual regra voluntária fornece o denominador em cada
caso; essa seleção depende da situação funcional e permanece dado da instrução.

# Onde esta forma é usada

No Ciclo 1, descreve o ramo de causa comum da regra geral da EC 41 durante o
segmento em que a redação vinculada do art. 45 estava vigente. A relação com as
unidades auditadas é registrada no conjunto da S5, não em campo deployável.
