---
type: FormaCalculo
id: forma-calculo-totalidade-proporcional-tempo
nome: Totalidade da remuneração do cargo efetivo, proporcional ao tempo de contribuição
base:
  tipo: totalidade_remuneracao_cargo_efetivo
ajustes:
  - tipo: proporcional_tempo_contribuicao
limitadores: []
dispositivos:
  - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md
projecao_sisprev:
  tipo_calculo: Não identificado
  fidelidade: sem_representacao
  justificativa: >-
    O enum do Sisprev não tem rótulo que combine base na totalidade da
    remuneração do cargo efetivo com proporcionalidade ao tempo de
    contribuição. `Valor Efetivo` expressa a base sem a proporção;
    `Proporcionalidade Dias` expressa a proporção sem dizer sobre que base;
    `Valor Médio` é a base da redação seguinte, da EC 41/2003. O valor gravado
    descreve corretamente o estado do catálogo, e não o estado do conhecimento
    — a fórmula é conhecida e está transcrita nos dois dispositivos acima.
autorado_por: franklinbaldo
autorado_em: 2026-07-30
---

# Como calcular

Dois dispositivos da redação da **EC 20/1998**, cada um fundamentando um
componente.

A **base** vem do art. 40, § 3º:

> § 3º - Os proventos de aposentadoria, por ocasião da sua concessão, serão
> calculados com base na **remuneração do servidor no cargo efetivo** em que se
> der a aposentadoria e, na forma da lei, corresponderão à **totalidade da
> remuneração**.

É a última remuneração do cargo efetivo, integral — não média. A média entra na
redação seguinte do mesmo parágrafo, dada pela EC 41/2003, que fala em
"remunerações utilizadas como base para as contribuições".

O **ajuste** vem do art. 40, § 1º, II:

> II - compulsoriamente, aos setenta anos de idade, com **proventos
> proporcionais ao tempo de contribuição**;

A proporção é sobre o tempo **exigido** para a aposentadoria voluntária
correspondente, não sobre um total arbitrário. Este documento **não fixa** esse
denominador: ele depende da norma que define o tempo exigido, e nas regras que
usam esta forma essa norma é a lei estadual do período — que não está conferida
aqui. É o que o item aberto de "Entradas e saídas" registra.

Não há limitador: a redação da EC 20/1998 do § 3º não submete o provento ao teto
do RGPS, e a submissão só aparece com a EC 41/2003.

# Fórmula

```
provento = totalidade_remuneracao_cargo_efetivo × (tempo_contribuicao / tempo_exigido)
```

com o produto **limitado à própria base** — a proporção reduz, nunca amplia:

```
provento = base × min(1, tempo_contribuicao / tempo_exigido)
```

# Entradas e saídas

| entrada                     | tipo           | de onde vem                                                                        |
| --------------------------- | -------------- | ---------------------------------------------------------------------------------- |
| `remuneracao_cargo_efetivo` | decimal, moeda | totalidade da remuneração do cargo em que se dá a aposentadoria                    |
| `tempo_contribuicao_dias`   | inteiro, dias  | tempo de contribuição apurado                                                      |
| `tempo_exigido_dias`        | inteiro, dias  | tempo exigido para a voluntária correspondente — **não fixado por este documento** |

Saída: `provento_mensal`, decimal em moeda, sempre `<= remuneracao_cargo_efetivo`.

Contagem **em dias**, não em anos: é a granularidade que o catálogo já usa no
rótulo `Proporcionalidade Dias`, e arredondar para anos altera o resultado de
qualquer caso que não feche exatamente em aniversário.

- [ ] `tempo_exigido_dias` não tem fonte conferida nesta forma. Depende da norma
  estadual do período, que não foi lida — e sem ela a fórmula é completa em
  estrutura e incompleta em parâmetro

# Implementação

```python
from decimal import Decimal, ROUND_HALF_UP


def provento(
    remuneracao_cargo_efetivo: Decimal,
    tempo_contribuicao_dias: int,
    tempo_exigido_dias: int,
) -> Decimal:
    """Totalidade da remuneração, proporcional ao tempo de contribuição.

    A fração é truncada em 1: a proporcionalidade do art. 40, § 1º, II reduz o
    provento de quem não completou o tempo exigido, e nunca o aumenta acima da
    base do § 3º para quem o excedeu.
    """
    if tempo_exigido_dias <= 0:
        msg = "tempo_exigido_dias tem de ser positivo"
        raise ValueError(msg)
    fracao = min(Decimal(1), Decimal(tempo_contribuicao_dias) / Decimal(tempo_exigido_dias))
    return (remuneracao_cargo_efetivo * fracao).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

`Decimal`, não `float`: valor de provento em moeda, e a diferença aparece em
centavos que alguém recebe. O arredondamento é explícito por isso mesmo — o
modo padrão do Python (`ROUND_HALF_EVEN`) não é o de arredondamento monetário
usual no Brasil.

# Onde esta forma é usada

Conferida na `regra-0025` (aposentadoria compulsória, redação da EC 20/1998),
que é o caso que motivou este bundle. **Nenhum vínculo é declarado da regra para
esta forma**: uma forma é combinação jurídica reutilizável, e a relação
forma↔regra é livre nas duas direções. Ligá-las por campo é decisão que este
bundle não toma.
