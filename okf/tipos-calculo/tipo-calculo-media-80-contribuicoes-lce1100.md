---
type: TipoCalculo
id: tipo-calculo-media-80-contribuicoes-lce1100
nome: Média das 80% maiores remunerações contributivas — LCE 1.100/2021
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24-caput/original.md
ajustes: []
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24-par-10/original.md
origem_legada:
  tipo_calculo: Valor Médio
  fidelidade: parcial
  justificativa: >-
    O rótulo não declara a seleção das 80% maiores bases contributivas desde
    julho de 1994, a atualização das competências nem o teto da remuneração do
    cargo efetivo.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

O art. 24 da LCE 1.100/2021 determina a média aritmética simples das maiores
remunerações contributivas correspondentes a 80% do período desde julho de 1994
ou desde o início da contribuição, se posterior.

Após a média, o § 10 limita o provento à remuneração do cargo efetivo. O teto é
a primeira e única operação desta forma.

# Fórmula

```text
média = média_aritmética(das 80% maiores bases contributivas atualizadas)
provento = min(média, remuneração_cargo_efetivo)
```

# Entradas e saídas

Entradas: série de remunerações contributivas, competências, fatores de
atualização e remuneração do cargo efetivo.

Saída: `provento_inicial`, média já submetida ao teto do art. 24, § 10.
