---
type: TipoCalculo
id: tipo-calculo-remuneracao-cargo-ec70-proporcional-dias
nome: Remuneração do cargo efetivo sob a EC 70/2012, proporcional em dias
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores: []
origem_legada:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    `Proporcionalidade Dias` nomeia o ajuste exatamente como ele é: razão entre
    o tempo de contribuição e o tempo exigido, contada em dias. É o sentido que
    o rótulo já tem no catálogo, onde toda regra que o usa mede a fração em
    dias. Fica sem coluna a **base** — a remuneração do cargo efetivo, e não a
    média —, que é a perda desta projeção; `integral: N` confirma o ramo
    proporcional mas não diz sobre que valor a fração incide.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 6º-A da EC 41/2003, incluído pela EC 70/2012, substitui a base
contributiva por proventos calculados sobre a remuneração do cargo efetivo. O
inciso I do § 1º do art. 40 mantém o ramo proporcional para as causas comuns.

Esta forma cobre o segmento em que a medida da proporção é **em dias**: desde
13/03/2008, o art. 17 da LCE 432/2008 fornece a razão entre o tempo total de
contribuição e o tempo exigido para a aposentadoria voluntária correspondente.

A leitura é conforme à hierarquia normativa: a lei estadual fornece a fração,
mas a sua remissão ordinária à própria base não afasta a base constitucional
especial posterior do art. 6º-A. A remuneração do cargo vem da EC 70; só o
ajuste proporcional varia conforme a legislação aplicável à data do direito.

# Fórmula

```
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = remuneração_do_cargo_efetivo × fração
```

A paridade do art. 6º-A é regime de reajuste e fica fora da fórmula de
concessão.

# Entradas e saídas

Entradas: remuneração do cargo efetivo, tempo de contribuição em dias e tempo
exigido para a aposentadoria voluntária correspondente, também em dias.

Saída: provento inicial proporcional, em moeda, nunca superior à remuneração do
cargo efetivo.

# Onde esta forma é usada

No Ciclo 1, descreve a unidade de causa comum do art. 6º-A/EC 70 desde a LCE
432/2008. O segmento anterior, com fração anual da LC 228/2000, é
[tipo próprio](tipo-calculo-remuneracao-cargo-ec70-proporcional-anos.md) — a
medida do ajuste é o que distingue as duas, e uma forma que abrigasse as duas
não teria projeção única no enum do Sisprev.
