---
type: FormaCalculo
id: forma-calculo-media-80-contribuicoes-lei10887
nome: Média das 80% maiores remunerações contributivas — Lei 10.887/2004
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/cf88/art-40-par-3/ec-41-2003.md
    - /dispositivos/lei-10887-2004/art-1/original.md
ajustes: []
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lei-10887-2004/art-1-par-5/original.md
projecao_sisprev:
  tipo_calculo: Valor Médio
  fidelidade: parcial
  justificativa: >-
    `Valor Médio` não informa que entram as 80% maiores remunerações desde
    julho de 1994, que os valores são bases contributivas atualizadas nem que
    o resultado se submete à remuneração do cargo efetivo.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

A base é a média aritmética simples das maiores remunerações utilizadas como
base para contribuições, selecionadas em quantidade correspondente a 80% do
período contributivo desde julho de 1994 ou desde o início da contribuição, se
posterior.

Depois da média, o § 5º do art. 1º da Lei 10.887/2004 limita o provento à
remuneração do cargo efetivo. Por isso o limitador tem `ordem: 1`.

# Fórmula

```text
n = piso(0,80 × número_de_competências_válidas)
média = soma(das n maiores remunerações atualizadas) / n
provento = min(média, remuneração_cargo_efetivo)
```

O piso no número de competências e a atualização mensal são exigências do
regime legal, embora os respectivos parágrafos ainda não estejam individualizados
em concepts próprios neste bundle.

# Entradas e saídas

| entrada                        | tipo              | uso                                      |
| ------------------------------ | ----------------- | ---------------------------------------- |
| remunerações contributivas     | série monetária   | ordenar, selecionar e calcular a média   |
| competências                   | `AAAA-MM`         | delimitar o período desde julho de 1994  |
| fatores de atualização         | série decimal     | atualizar cada remuneração               |
| remuneração do cargo efetivo   | moeda             | teto final do provento                   |

Saída: `provento_inicial`, valor monetário após a média e o teto.
