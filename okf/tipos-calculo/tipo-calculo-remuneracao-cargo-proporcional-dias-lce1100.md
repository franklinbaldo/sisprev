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

Dentro do regime vigente da LCE 1.100/2021, o servidor alcançado pelo
trilho de ingresso até 31 de dezembro de 2003 requer a aposentadoria por
incapacidade pela regra permanente atual da lei, e é o art. 25 que
disciplina diretamente a base de cálculo dessa coorte — a mesma faixa que
o art. 27, I, já nomeia, com a mesma grafia, para o reajustamento com
paridade: "que tenha ingressado no serviço público em cargo efetivo até
31 de dezembro de 2003". A base desta forma é, portanto, a totalidade da
remuneração do cargo efetivo do art. 25 — e não a média do art. 24, que o
próprio art. 24, *caput*, restringe expressamente a quem ingressou
**após** 31/12/2003 — proporcionalizada pela fração em dias do art. 26,
que o § 14 do art. 30 encaminha para a causa comum: numerador o tempo de
contribuição, denominador o tempo exigido para a aposentadoria voluntária
de referência (art. 26, § 2º). O § 14 também ressalva "o direito adquirido
a outra fórmula" — proteção adicional e independente, que não é o
fundamento desta forma: a base no art. 25 decorre da coorte de ingresso
dentro do regime vigente, não de direito adquirido a regime anterior.

Esta forma preserva, para a causa comum, a mesma coerência de regime que
`tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100` preserva para as
causas qualificadas da mesma coorte: quem ingressou até 2003 calcula sobre a
remuneração do cargo, com paridade; quem ingressou depois calcula pela média,
sem paridade (`tipo-calculo-media-proporcional-dias-lce1100`).

# Risco interpretativo registrado, não decidido em definitivo

O art. 26, § 1º, é textualmente expresso: a fração "será aplicada sobre o
valor dos proventos, calculados em conformidade com o disposto no art. 24" —
isto é, sobre a média, não sobre a remuneração do cargo. Essa remissão
interna faz o mesmo risco que atinge o § 13 (a remissão literal ao art. 24)
recair também sobre o § 14, por via do próprio art. 26 que ele encaminha.
Esta forma adota a base do art. 25 — que disciplina diretamente, dentro do
regime vigente da LCE 1.100/2021, o cálculo da coorte de ingresso até
31/12/2003 — como **a fórmula adotada para a carga**, harmonizando os
arts. 24 e 25 como divisão vigente de coortes (decisão da coordenação de
2026-08-05, registrada nas regras propostas que usam esta forma). A tensão
com a literalidade do art. 26, § 1º, permanece registrada como risco
interpretativo, revisável diante de manifestação jurídica específica,
precedente ou decisão institucional posterior — mas não torna a base do
art. 24 uma alternativa igualmente válida para a carga atual, nem
transforma a homologação prática em instância de escolha entre as duas
leituras: a homologação verifica se o sistema executa a fórmula adotada
(art. 25); a execução de outra base é falha de homologação, a devolver
para decisão jurídica e institucional.

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
