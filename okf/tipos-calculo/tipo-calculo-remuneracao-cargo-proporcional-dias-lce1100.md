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

O art. 24, no próprio *caput*, disciplina expressamente a base de cálculo
dos servidores que ingressaram **após** 31 de dezembro de 2003, enquanto o
art. 25 disciplina, também de forma expressa, a base dos que ingressaram
**até** aquela data. Os dois integram o regime permanente vigente da LCE
1.100/2021 e se compreendem como normas complementares de distribuição
das bases de cálculo por coorte de ingresso — não como regra e exceção
temporal. O servidor alcançado pelo trilho de ingresso até 31/12/2003 não
está obrigado a requerer o benefício com fundamento em legislação
revogada ou em direito adquirido: pode requerê-lo segundo a legislação
atual, hipótese em que se aplica a disciplina que a própria lei vigente
destinou à sua coorte — os arts. 25 e 27, I, que nomeiam essa faixa com a
mesma grafia ("que tenha ingressado no serviço público em cargo efetivo
até 31 de dezembro de 2003"). Nessa leitura, a base desta forma é a
totalidade da remuneração do cargo efetivo do art. 25 — e não a média do
art. 24 — proporcionalizada pela fração em dias do art. 26, que o § 14 do
art. 30 encaminha para a causa comum: numerador o tempo de contribuição,
denominador o tempo exigido para a aposentadoria voluntária de referência
(art. 26, § 2º). O § 14 também ressalva "o direito adquirido a outra
fórmula" — proteção adicional e independente, que não é o fundamento
desta forma: a base no art. 25 decorre da coorte de ingresso dentro do
regime vigente, não de direito adquirido a regime anterior. Os
fundamentos da leitura adotada, e por que a leitura contrária (média do
art. 24 combinada com paridade) é considerada equivocada, estão em "Por
que a leitura pelo art. 24 é equivocada", abaixo.

Esta forma preserva, para a causa comum, a mesma coerência de regime que
`tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100` preserva para as
causas qualificadas da mesma coorte: quem ingressou até 2003 calcula sobre a
remuneração do cargo, com paridade; quem ingressou depois calcula pela média,
sem paridade (`tipo-calculo-media-proporcional-dias-lce1100`).

# Por que a leitura pelo art. 24 é equivocada

*Data venia*, considera-se equivocada a interpretação segundo a qual as
remissões dos arts. 30, §§ 13 e 14, e 26, § 1º, fariam incidir a média
contributiva do art. 24 também sobre os servidores que ingressaram até
31 de dezembro de 2003.

O art. 26, § 1º, é textualmente expresso — a fração "será aplicada sobre
o valor dos proventos, calculados em conformidade com o disposto no
art. 24" —, e essa remissão literal é registrada porque pode ser invocada
para sustentar entendimento diverso. Isso não significa que as duas
interpretações sejam consideradas igualmente corretas. Interpretar a
remissão como afastamento integral do art. 25 exigiria admitir que,
precisamente na aposentadoria por incapacidade, a lei teria criado a
combinação entre média contributiva e paridade — regime que a LCE
1.100/2021 não institui em nenhuma outra hipótese (a coorte que calcula
pela média, na voluntária e na causa comum das demais idades, é sempre a
sem paridade). Cálculo inicial e forma de reajustamento são categorias
juridicamente distintas, e essa combinação não é impossível em abstrato,
mas não há disposição inequívoca instituindo esse regime híbrido, nem
precedente jurisprudencial ou administrativo interno seguro que autorize
sua criação por inferência. A leitura pelo art. 24 também reduziria o
alcance do art. 25 sem que os §§ 13 e 14 do art. 30 tenham declarado
expressamente sua inaplicabilidade à aposentadoria por incapacidade — o
silêncio não equivale à revogação.

A remissão aos arts. 24 e 26 deve, portanto, ser compreendida em harmonia
com a divisão de coortes estabelecida pelos arts. 24 e 25, preservando-se,
para os ingressos até 31/12/2003, a remuneração do cargo como base do
provento — integral nas causas qualificadas, proporcionalizada em dias na
causa comum —, com paridade na forma do art. 27, I. Para a carga atual, a
coordenação considera juridicamente adequada a aplicação do art. 25 e,
*data venia*, equivocada a interpretação que cria, por via indireta, a
combinação média contributiva com paridade. A fórmula poderá ser revista
caso manifestação jurídica institucional, precedente vinculante ou
decisão judicial estabeleça entendimento contrário — o que não transforma
a homologação prática em instância de escolha entre as duas leituras: a
homologação verifica se o sistema executa a fórmula adotada (art. 25); a
execução de outra base é falha de homologação, a devolver para decisão
jurídica e institucional, não confirmação de que a leitura pelo art. 24
estivesse certa.

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
