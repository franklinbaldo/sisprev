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

Após a média, o § 10 limita o provento à remuneração do cargo efetivo. Esse é o
único limitador desta forma.

O limite máximo dos benefícios do RGPS **não** incide aqui: o art. 24, § 11,
alcança o segurado sujeito ao regime de previdência complementar, e o § 12,
quem ingressou a partir de 6 de novembro de 2018. Esta forma descreve a família
que exclui as duas condições — ingresso de 01/01/2004 a 05/11/2018 sem adesão.
A forma com aquele teto é
`tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100`: mesma base, mesmo § 10
e **um limitador a mais**. As duas produzem valores diferentes para o mesmo
servidor e compartilham o rótulo legado `Valor Médio`.

# Fórmula

```text
média = média_aritmética(das 80% maiores bases contributivas atualizadas)
provento = min(média, remuneração_cargo_efetivo)
```

# Entradas e saídas

Entradas: série de remunerações contributivas, competências, fatores de
atualização e remuneração do cargo efetivo.

Saída: `provento_inicial`, média já submetida ao teto do art. 24, § 10.

# Onde esta forma é usada

Descreve as dezenove unidades de causa qualificada da família
`incapacidade-lce1100-2004-ate-2018-sem-rpc-*` (exceto `causa-comum`). A
unidade de causa comum da mesma família usa
`tipo-calculo-media-proporcional-dias-lce1100`.
