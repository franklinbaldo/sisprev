---
type: TipoCalculo
id: tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100
nome: >-
  Média das 80% maiores remunerações contributivas, limitada ao teto do RGPS —
  LCE 1.100/2021
base:
  tipo: media_80_maiores_remuneracoes_contributivas
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24/original.md
ajustes:
  - tipo: atualizacao_monetaria_das_competencias
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1100-2021/art-24/original.md
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
  - tipo_calculo: Valor Médio
    fidelidade: parcial
    justificativa: >-
      O rótulo legado nomeia a base — a média — e não diz nada sobre
      limitadores. Ele é o mesmo valor que
      `tipo-calculo-media-80-contribuicoes-lce1100` projeta para a família sem
      sujeição ao regime de previdência complementar, que tem a mesma base e
      **um limitador a menos**. Duas fórmulas materialmente diferentes, que
      produzem valores diferentes para o mesmo servidor, compartilham o único
      rótulo disponível: o enum do Sisprev não distingue o teto do RGPS. A
      fidelidade é parcial por ausência de vocabulário, não por dúvida sobre a
      fórmula.
autorado_por: franklinbaldo
autorado_em: 2026-08-05
---

# Como calcular

Base: a média aritmética simples das maiores remunerações utilizadas como base
para as contribuições do servidor aos regimes de previdência a que esteve
vinculado, correspondentes a 80% de todo o período contributivo desde a
competência de julho de 1994 ou desde a do início da contribuição, se posterior
àquela competência (art. 24, caput).

As remunerações consideradas são atualizadas mês a mês pela variação do índice
fixado para a atualização dos salários de contribuição do RGPS (art. 24, § 7º),
observados, em cada mês, os pisos e tetos do § 9º.

Sobre o valor assim apurado incidem dois limitadores, nesta ordem:

1. o provento não pode exceder a remuneração do servidor no cargo efetivo em
   que se deu a aposentadoria (art. 24, § 10);
2. o provento não pode ser superior ao limite máximo estabelecido para os
   benefícios do Regime Geral de Previdência Social (art. 24, §§ 11 e 12).

Não há proporcionalização pelo tempo de contribuição: esta forma descreve as
causas qualificadas, que o art. 30, caput, excetua da fração.

# A quem se aplica o teto do RGPS

O art. 24 sujeita ao limite máximo dos benefícios do Regime Geral duas
situações, por vias distintas e com o mesmo resultado:

- **§ 11** — o segurado sujeito ao Regime de Previdência Complementar, nos
  termos dos §§ 14 a 16 do art. 40 da Constituição Federal. Alcança quem fez a
  opção prévia e expressa, qualquer que tenha sido a data de ingresso;
- **§ 12** — todo servidor ocupante de cargo efetivo que tenha ingressado no
  serviço público a partir da implementação do regime de previdência
  complementar estadual, ocorrida em 6 de novembro de 2018.

Por isso a família é **uma só**, alcançada por disjunção: ingresso a partir de
06/11/2018 **ou** opção expressa. Não há hipótese material que justifique
separar o optante anterior num ramo próprio — o limitador que ele recebe é o
mesmo, pelo mesmo artigo.

# Ordem dos limitadores

A ordem gravada (remuneração do cargo, depois teto do RGPS) é a que decorre da
sequência do próprio art. 24: o § 10 fecha o cálculo do caput, e os §§ 11 e 12
incidem sobre o provento já apurado. Como o resultado de dois tetos aplicados
em sequência é o menor dos dois, a ordem entre eles não altera o valor final
desta forma — ela importa na forma proporcional
(`tipo-calculo-media-proporcional-dias-teto-rgps-lce1100`), onde a fração entra
depois dos dois.

O teto do RGPS **compõe o valor inicial do benefício**, e não é informação
posterior à concessão nem regra de reajustamento.

# Fórmula

```text
media           = média das 80% maiores remunerações contributivas atualizadas
apos_teto_cargo = min(media, remuneração_do_cargo_efetivo)        # art. 24, § 10
provento        = min(apos_teto_cargo, teto_rgps)                 # art. 24, §§ 11-12
```

# Entradas e saídas

Entradas: histórico de remunerações de contribuição desde 07/1994 (ou desde o
início da contribuição), índices de atualização, remuneração do cargo efetivo na
data da aposentadoria e o limite máximo dos benefícios do RGPS vigente na
concessão.

Saída: `provento_inicial`, nunca superior à remuneração do cargo efetivo nem ao
teto do RGPS.

# Onde esta forma é usada

Descreve as dezenove unidades de causa qualificada da família
`incapacidade-lce1100-apos-2018-ou-rpc-*` (exceto `causa-comum`). A unidade de
causa comum da mesma família usa
`tipo-calculo-media-proporcional-dias-teto-rgps-lce1100`, que acrescenta a
fração do art. 26.
