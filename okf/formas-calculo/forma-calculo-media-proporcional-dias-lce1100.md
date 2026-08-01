---
type: FormaCalculo
id: forma-calculo-media-proporcional-dias-lce1100
nome: Média contributiva da LCE 1.100/2021, proporcional ao tempo em dias
base:
  tipo: media_remuneracoes_contribuicao
  dispositivos:
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    dispositivos:
      - /dispositivos/lce-1100-2021/art-26/original.md
      - /dispositivos/lce-1100-2021/art-30-par-14/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    O rótulo legado representa o ajuste em dias, mas omite a base média do art.
    24 que o art. 26 manda proporcionalizar. A combinação completa não possui
    rótulo próprio no enum atual.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O § 14 do art. 30 encaminha a incapacidade decorrente de causa comum ao art. 26.
Esse artigo manda aplicar uma fração sobre os proventos previamente calculados
na forma do art. 24. A base é, portanto, a média das maiores remunerações de
contribuição correspondente a 80% do período contributivo; o ajuste é a razão,
em dias, entre o tempo total de contribuição e o tempo exigido para a
aposentadoria voluntária de referência.

A remissão especial do § 14 alcança a incapacidade; o art. 27 trata somente do
reajuste posterior e não muda esta fórmula de concessão. Assim, a mesma forma
pode conviver com paridade ou sem paridade, conforme a coorte de ingresso.

# Fórmula

```
base = média_das_maiores_remunerações_de_contribuição
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base × fração
```

Os períodos são considerados em dias. A proporção é limitada a 1 porque reduz o
provento e não cria valor superior à base média.

# Entradas e saídas

Entradas: remunerações contributivas, período contributivo, tempo de
contribuição em dias e tempo exigido em dias para a aposentadoria voluntária de
referência.

Saída: provento inicial mensal proporcional, em moeda. Paridade ou reajuste sem
paridade não são saída desta forma; pertencem ao regime de manutenção do
benefício.

# Onde esta forma é usada

No Ciclo 1, descreve as unidades de causa comum das duas coortes da LCE
1.100/2021: com paridade para ingresso até 31/12/2003 e sem paridade para
ingresso a partir de 01/01/2004.
