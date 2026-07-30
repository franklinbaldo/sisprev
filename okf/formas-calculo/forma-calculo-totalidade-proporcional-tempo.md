---
type: FormaCalculo
id: forma-calculo-totalidade-proporcional-tempo
nome: Totalidade da remuneração do cargo efetivo, proporcional ao tempo de contribuição
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md
      - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
limitadores: []
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
    — a fórmula é conhecida e está transcrita nos dispositivos vinculados a
    cada componente.
autorado_por: franklinbaldo
autorado_em: 2026-07-30
---

# Como calcular

Três dispositivos da redação da **EC 20/1998**, cada um vinculado ao componente
que ele funda — a base a um, o ajuste a dois.

A **base** vem do art. 40, § 3º:

> § 3º - Os proventos de aposentadoria, por ocasião da sua concessão, serão
> calculados com base na **remuneração do servidor no cargo efetivo** em que se
> der a aposentadoria e, na forma da lei, corresponderão à **totalidade da
> remuneração**.

É a última remuneração do cargo efetivo, integral — não média. A média entra na
redação seguinte do mesmo parágrafo, dada pela EC 41/2003, que fala em
"remunerações utilizadas como base para as contribuições".

O **ajuste** é determinado pelo art. 40, § 1º, II:

> II - compulsoriamente, aos setenta anos de idade, com **proventos
> proporcionais ao tempo de contribuição**;

## O denominador da proporção é constitucional, e depende do sexo

O inciso II manda reduzir "proporcionalmente ao tempo de contribuição" e não diz
proporcional a quanto. Quem fixa o termo de comparação é o **art. 40, § 1º, III,
"a"**, na mesma redação — o tempo de contribuição exigido para a voluntária com
proventos integrais:

> a) sessenta anos de idade e trinta e cinco de contribuição, **se homem**, e
> cinqüenta e cinco anos de idade e trinta de contribuição, **se mulher**;

Logo o denominador é **35 anos para homem e 30 para mulher**, e por isso a alínea
"a" está vinculada ao ajuste junto com o inciso II: o inciso ordena a redução, a
alínea dá a medida dela.

Duas consequências que convém deixar escritas:

- **A dependência de sexo é do cálculo, não do critério de elegibilidade.** A
  compulsória do inciso II incide sobre ambos os sexos aos setenta anos — é o que
  sustenta `sexo: AMBOS` na `regra-0025`. O que varia por sexo é o denominador,
  que é dado do caso concreto, não campo da regra.
- **Nenhuma norma estadual é pressuposta aqui.** A `fundamentacao_proporcional`
  da regra que usa esta forma cita só a Constituição, e nenhum dispositivo
  estadual foi conferido alterando este denominador. Se existir, é ele que tem de
  ser identificado e vinculado — não presumido, como esta forma presumia na sua
  primeira versão.

Não há limitador: a redação da EC 20/1998 do § 3º não submete o provento ao teto
do RGPS, e a submissão só aparece com a EC 41/2003.

# Fórmula

```
tempo_exigido = 35 anos, se homem;  30 anos, se mulher     (§ 1º, III, "a")

provento = totalidade_remuneracao_cargo_efetivo × (tempo_contribuicao / tempo_exigido)
```

com o produto **limitado à própria base** — a proporção reduz, nunca amplia:

```
provento = base × min(1, tempo_contribuicao / tempo_exigido)
```

# Entradas e saídas

| entrada                     | tipo                   | de onde vem                                                     |
| --------------------------- | ---------------------- | --------------------------------------------------------------- |
| `remuneracao_cargo_efetivo` | decimal, moeda         | totalidade da remuneração do cargo em que se dá a aposentadoria |
| `tempo_contribuicao_dias`   | inteiro, dias          | tempo de contribuição apurado                                   |
| `sexo`                      | `MASCULINO`/`FEMININO` | dado do caso — decide o denominador (35 ou 30 anos)             |
| `dias_por_ano`              | inteiro, dias          | conversão de "anos de contribuição" em dias — **não conferida** |

Saída: `provento_mensal`, decimal em moeda, sempre `<= remuneracao_cargo_efetivo`.

Contagem **em dias**, não em anos: é a granularidade que o catálogo já usa no
rótulo `Proporcionalidade Dias`, e arredondar para anos altera o resultado de
qualquer caso que não feche exatamente em aniversário. É essa granularidade que
cria a única entrada sem fonte conferida — o dispositivo fixa **anos**, e a
conversão para dias é convenção de apuração, não texto de norma.

- [ ] `dias_por_ano` não tem fonte conferida. Os **anos** exigidos são
  constitucionais (35/30, art. 40, § 1º, III, "a"); a regra que os converte em
  dias — inclusive o tratamento de anos bissextos — está em norma de apuração de
  tempo de contribuição que não foi lida nesta rodada. A estrutura da fórmula
  está completa; falta este parâmetro

# Implementação

```python
from decimal import Decimal, ROUND_HALF_UP
from typing import Literal

# art. 40, § 1º, III, "a", CF, red. EC 20/1998 — anos de contribuição exigidos
# para a voluntária integral, que é o denominador da proporcionalidade do
# inciso II. Transcrito em okf/dispositivos/cf88/art-40-par-1-inc-iii-al-a/.
ANOS_EXIGIDOS = {"MASCULINO": 35, "FEMININO": 30}


def provento(
    remuneracao_cargo_efetivo: Decimal,
    tempo_contribuicao_dias: int,
    sexo: Literal["MASCULINO", "FEMININO"],
    dias_por_ano: int,
) -> Decimal:
    """Totalidade da remuneração, proporcional ao tempo de contribuição.

    `sexo` é dado do caso concreto, não o campo `sexo` da regra: a compulsória
    incide sobre ambos os sexos, e o que varia por sexo é o denominador.

    `dias_por_ano` é parâmetro explícito porque o dispositivo fixa anos, não
    dias — quem o passa está declarando a convenção de apuração que usou.

    A fração é truncada em 1: a proporcionalidade do art. 40, § 1º, II reduz o
    provento de quem não completou o tempo exigido, e nunca o aumenta acima da
    base do § 3º para quem o excedeu.
    """
    if dias_por_ano <= 0:
        msg = "dias_por_ano tem de ser positivo"
        raise ValueError(msg)
    tempo_exigido_dias = ANOS_EXIGIDOS[sexo] * dias_por_ano
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
