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

O § 14 do art. 30 da LCE 1.100/2021 encaminha a incapacidade por causa comum
ao art. 26, "ressalvado o direito adquirido a outra fórmula". Para o servidor
alcançado pelo trilho de ingresso até 31 de dezembro de 2003, essa ressalva
é a mesma que os arts. 25 e 27, I já nomeiam, com a mesma grafia, para as
causas qualificadas da mesma coorte (§ 13 do art. 30): "que tenha ingressado
no serviço público em cargo efetivo até 31 de dezembro de 2003". A base desta
forma é, portanto, a totalidade da remuneração do cargo efetivo do art. 25 —
e não a média do art. 24, que o próprio art. 24, *caput*, restringe
expressamente a quem ingressou **após** 31/12/2003 — proporcionalizada pela
fração em dias do art. 26: numerador o tempo de contribuição, denominador o
tempo exigido para a aposentadoria voluntária de referência (art. 26, § 2º).

Esta forma preserva, para a causa comum, a mesma coerência de regime que
`tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100` preserva para as
causas qualificadas da mesma coorte: quem ingressou até 2003 calcula sobre a
remuneração do cargo, com paridade; quem ingressou depois calcula pela média,
sem paridade (`tipo-calculo-media-proporcional-dias-lce1100`).

# Tensão interpretativa registrada, não resolvida

O art. 26, § 1º, é textualmente expresso: a fração "será aplicada sobre o
valor dos proventos, calculados em conformidade com o disposto no art. 24" —
isto é, sobre a média, não sobre a remuneração do cargo. Essa remissão
interna faz a mesma tensão que atinge o § 13 (art. 25 × art. 30, § 13 →
art. 24) recair também sobre o § 14, por via do próprio art. 26 que ele
encaminha. Esta forma adota a leitura conservadora — regime coerente pela
coorte, base no art. 25 — por decisão da coordenação registrada nas regras
propostas que a usam, e não porque a literalidade do art. 26, § 1º, a
resolva sozinha. A questão permanece aberta a revisão diante de manifestação
jurídica específica, precedente ou decisão institucional posterior; nenhuma
das duas leituras está descartada.

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

No Ciclo 1, descreve a unidade de causa comum da coorte de ingresso até
31/12/2003 da LCE 1.100/2021 (`incapacidade-lce1100-ate-2003-causa-comum`).
A unidade correspondente da coorte de ingresso após 2003 permanece descrita
por `tipo-calculo-media-proporcional-dias-lce1100`.
