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
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md
      - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    `Valor Efetivo` nomeia a base — a totalidade da remuneração do cargo
    efetivo — e é o rótulo que a `regra-0002`, origem desta hipótese, já
    gravava. A proporcionalidade não se perde: ela é carregada por
    `integral: N` na mesma linha, e o par recupera o que nenhum dos dois
    campos diz sozinho. O que fica sem coluna é a **medida** da fração, e isso
    é limitação do Sisprev, não indefinição da auditoria.
autorado_por: franklinbaldo
autorado_em: 2026-07-30
---

# Como calcular

A **base** vem do art. 40, § 3º, na redação da EC 20/1998: a totalidade da
remuneração do cargo efetivo em que ocorre a aposentadoria.

O **ajuste** vem do art. 40, § 1º, II: redução proporcional ao tempo de
contribuição. O denominador é dado pelo § 1º, III, alínea “a”, na mesma redação:
35 anos para homem e 30 anos para mulher. A operação está em `ordem: 1`, pois
não há limitador anterior ou posterior nesta combinação.

# Fórmula

```text
exigido = 35 anos, se homem; 30 anos, se mulher
fração = min(1, tempo_contribuição / exigido)
provento = remuneração_cargo_efetivo × fração
```

# Entradas e saídas

| entrada                     | tipo                  | origem                                                    |
| --------------------------- | --------------------- | --------------------------------------------------------- |
| `remuneracao_cargo_efetivo` | moeda                 | totalidade da remuneração no cargo efetivo                |
| `tempo_contribuicao_dias`   | inteiro, dias         | tempo apurado no caso                                     |
| `sexo`                      | masculino ou feminino | define o denominador constitucional de 35 ou 30 anos      |
| `dias_por_ano`              | inteiro positivo      | convenção de conversão ainda sem dispositivo identificado |

Saída: `provento_mensal`, limitado à própria base.

A estrutura jurídica da fórmula está fechada. Permanece pendente apenas a fonte
da conversão dos anos constitucionais em dias, inclusive quanto a anos
bissextos.
