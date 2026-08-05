---
type: TipoCalculo
id: tipo-calculo-media-80-proporcional-dias-lce1100
nome: Média das 80% maiores remunerações, limitada e proporcional em dias — LCE 1.100/2021
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24-caput/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 2
    dispositivos:
      - /dispositivos/lce-1100-2021/art-26/original.md
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24-par-10/original.md
origem_legada:
  tipo_calculo: Tipo Cálculo Nova Previdência
  fidelidade: parcial
  justificativa: >-
    O rótulo identifica um pacote operacional, mas não expõe a média das 80%
    maiores bases contributivas, o teto da remuneração nem a fração em dias.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

Calcula-se a média do art. 24 e aplica-se o teto do § 10. Depois, e não antes,
o art. 26 manda multiplicar o valor limitado pela fração entre o tempo total de
contribuição e o tempo necessário para a aposentadoria voluntária por idade e
tempo de contribuição.

O § 1º do art. 26 determina expressamente a precedência do teto; o § 2º manda
considerar os períodos em número de dias.

# Fórmula

```text
média = média_aritmética(das 80% maiores bases contributivas atualizadas)
base_limitada = min(média, remuneração_cargo_efetivo)
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base_limitada × fração
```

# Entradas e saídas

Entradas: remunerações contributivas e suas competências, fatores de atualização,
remuneração do cargo efetivo, tempo de contribuição em dias e tempo exigido em
dias.

Saída: `provento_inicial`, após média, teto e proporcionalidade, nessa ordem.
