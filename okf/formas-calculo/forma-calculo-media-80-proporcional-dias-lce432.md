---
type: FormaCalculo
id: forma-calculo-media-80-proporcional-dias-lce432
nome: Média das 80% maiores remunerações, limitada e proporcional em dias — LCE 432/2008
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/lce-432-2008/art-45-caput/lce-672-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 2
    dispositivos:
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lce-432-2008/art-45-par-10/lce-672-2012.md
projecao_sisprev:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    O rótulo descreve a fração em dias, mas omite a base de 80% das maiores
    remunerações contributivas e o teto aplicado antes da proporcionalidade.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

Primeiro calcula-se a média do art. 45. Em seguida aplica-se o teto do § 10 à
remuneração do cargo efetivo. Só então o art. 17 manda multiplicar esse resultado
pela fração entre o tempo total de contribuição e o tempo exigido para a
aposentadoria voluntária correspondente.

A ordem não é intercambiável: o art. 17, § 1º, diz expressamente que o limite é
observado previamente, e o § 2º manda contar numerador e denominador em dias.

# Fórmula

```text
média = média_aritmética(das 80% maiores bases contributivas atualizadas)
base_limitada = min(média, remuneração_cargo_efetivo)
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base_limitada × fração
```

# Entradas e saídas

| entrada                      | tipo            |
| ---------------------------- | --------------- |
| remunerações contributivas   | série monetária |
| fatores de atualização       | série decimal   |
| remuneração do cargo efetivo | moeda           |
| tempo de contribuição        | dias            |
| tempo exigido                | dias            |

Saída: `provento_inicial`, após média, teto e proporcionalidade, nessa ordem.
