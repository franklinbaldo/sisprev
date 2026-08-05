---
type: TipoCalculo
id: tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100
nome: Remuneração do cargo efetivo da LCE 1.100/2021, proporcional ao tempo em dias
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/lce-1100-2021/art-25/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-26/original.md
      - /dispositivos/lce-1100-2021/art-30-par-14/original.md
limitadores: []
origem_legada:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    `Proporcionalidade Dias` nomeia o ajuste em dias que o art. 26 aplica, sem
    dizer sobre que base ele incide. É o valor legado que `regra-0020` já
    grava, em produção, para a causa comum da coorte de ingresso até
    31/12/2003; o mesmo rótulo também é a origem legada de
    `tipo-calculo-media-proporcional-dias-lce1100` (base no art. 24, para a
    coorte de ingresso após 2003) e de `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias` (mesma base, norma diferente) — ambiguidade do
    enum do Sisprev entre fórmulas distintas, não indefinição da base desta
    forma em concreto.
autorado_por: franklinbaldo
autorado_em: 2026-08-05
---

# Como calcular

A base desta forma é a totalidade da remuneração do cargo efetivo do
art. 25, aplicável à coorte de ingresso até 31/12/2003
(`tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100`, que descreve
essa base e fundamenta por que se aplica a essa coorte). Para a causa
comum, essa base é proporcionalizada pela fração em dias do art. 26, que
o § 14 do art. 30 encaminha para essa hipótese: numerador o tempo de
contribuição, denominador o tempo exigido para a aposentadoria voluntária
de referência (art. 26, § 2º).

O art. 26, § 1º, contém remissão à média do art. 24 para compor a fração.
Essa remissão não altera a base adotada por esta forma — as razões pelas
quais ela não afasta o art. 25 para a coorte de ingresso até 31/12/2003
estão desenvolvidas em
`tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100`, que esta
forma toma por base.

# Fórmula

```text
remuneracao_cargo_efetivo = art. 25, caput e parágrafo único
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = remuneracao_cargo_efetivo × fração
```

# Entradas e saídas

Entradas: remuneração do cargo efetivo (art. 25), tempo de contribuição em
dias e tempo exigido para a aposentadoria voluntária de referência, também
em dias.

Saída: provento inicial mensal proporcional, em moeda, nunca superior à
remuneração do cargo efetivo.

# Onde esta forma é usada

Descreve a unidade de causa comum da coorte de ingresso até 31/12/2003 da
LCE 1.100/2021 (`incapacidade-lce1100-ate-2003-causa-comum`). A unidade
correspondente da coorte de ingresso após 2003 permanece descrita por
`tipo-calculo-media-proporcional-dias-lce1100`.
