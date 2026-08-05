---
type: TipoCalculo
id: tipo-calculo-media-proporcional-dias-teto-rgps-lce1100
nome: >-
  Média das 80% maiores remunerações contributivas, limitada ao teto do RGPS e
  proporcional ao tempo em dias — LCE 1.100/2021
base:
  tipo: media_80_maiores_remuneracoes_contributivas
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
ajustes:
  - tipo: atualizacao_monetaria_das_competencias
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24/original.md
  - tipo: proporcional_tempo_contribuicao
    ordem: 2
    dispositivos:
      - /dispositivos/lce-1100-2021/art-26/original.md
      - /dispositivos/lce-1100-2021/art-30-par-14/original.md
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24-par-10/original.md
  - tipo: teto_maximo_beneficios_rgps
    ordem: 2
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24-par-11/original.md
      - /dispositivos/lce-1100-2021/art-24-par-12/original.md
origem_legada:
  - tipo_calculo: Proporcionalidade Dias
    fidelidade: parcial
    justificativa: >-
      O rótulo legado nomeia o ajuste em dias e não diz sobre que base ele
      incide nem que limitadores a antecedem. O mesmo valor é a origem legada de
      `tipo-calculo-media-proporcional-dias-lce1100` (mesma base, **sem** o teto
      do RGPS), de `tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100`
      (base no art. 25) e de outras formas de norma diferente. O enum do Sisprev
      não distingue o teto do RGPS, e por isso o rótulo não identifica esta
      fórmula sozinho.
autorado_por: franklinbaldo
autorado_em: 2026-08-05
---

# Como calcular

A base é a mesma de
`tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100` — a média das 80%
maiores remunerações contributivas atualizadas, sujeita ao limite da
remuneração do cargo efetivo (art. 24, § 10) e ao limite máximo dos benefícios
do Regime Geral (art. 24, §§ 11 e 12), que documenta também a quem esse teto se
aplica e por quê.

O que esta forma acrescenta é a proporcionalização da causa comum: sobre o valor
já limitado incide a fração entre o tempo de contribuição e o tempo exigido para
a aposentadoria voluntária de referência, medida em dias (art. 26, para onde o
art. 30, § 14, encaminha a causa comum).

# Ordem dos limitadores e da proporcionalização

A ordem é: base → limite da remuneração do cargo (§ 10) → limite máximo do RGPS
(§§ 11 e 12) → fração em dias (art. 26).

Aqui a ordem **altera o valor**, e por isso é gravada e não deixada implícita.
Aplicar a fração antes dos tetos produziria resultado diferente de aplicá-la
depois sempre que a média bruta os exceder. A sequência adotada segue o art. 26,
§ 1º, que manda a fração incidir "sobre o valor dos proventos, calculados em
conformidade com o disposto no art. 24" — e os §§ 10 a 12 são parte do art. 24,
de modo que o valor a que a fração se aplica é o já limitado.

**Ressalva.** Essa leitura é a que o texto sustenta, mas o art. 26, § 1º, não
enuncia a sequência em face dos §§ 11 e 12, que são posteriores à redação
original da remissão. A ordem gravada é decisão desta auditoria, verificável em
homologação prática: dois servidores com a mesma média e tempos de contribuição
distintos revelam qual sequência o sistema executa.

# Fórmula

```text
media           = média das 80% maiores remunerações contributivas atualizadas
apos_teto_cargo = min(media, remuneração_do_cargo_efetivo)   # art. 24, § 10
apos_teto_rgps  = min(apos_teto_cargo, teto_rgps)            # art. 24, §§ 11-12
fração          = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento        = apos_teto_rgps × fração                    # art. 26
```

# Entradas e saídas

Entradas: histórico de remunerações de contribuição, índices de atualização,
remuneração do cargo efetivo, limite máximo dos benefícios do RGPS vigente na
concessão, tempo de contribuição em dias e tempo exigido para a aposentadoria
voluntária de referência, em dias.

Saída: provento inicial mensal proporcional, nunca superior à remuneração do
cargo efetivo nem ao teto do RGPS.

# Onde esta forma é usada

Descreve a unidade `incapacidade-lce1100-apos-2018-ou-rpc-causa-comum`. As
dezenove unidades de causa qualificada da mesma família usam
`tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100`, sem a fração.
