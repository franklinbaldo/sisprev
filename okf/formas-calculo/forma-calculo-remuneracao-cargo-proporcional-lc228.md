---
type: FormaCalculo
id: forma-calculo-remuneracao-cargo-proporcional-lc228
nome: Remuneração do cargo efetivo proporcional por anos na LC 228/2000
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/lce-228-2000/art-43/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/lce-228-2000/art-43-par-unico-inc-i/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Não identificado
  fidelidade: sem_representacao
  justificativa: >-
    O enum não combina remuneração do cargo, fração anual de 1/35 ou 1/30 e piso
    de um salário mínimo. `Valor Efetivo` omite a proporção e
    `Proporcionalidade Dias` ainda altera a granularidade textual da LC 228,
    que calcula por ano de serviço.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O art. 43, parágrafo único, I, da LC 228/2000 fixa a base na remuneração do cargo
efetivo e atribui, por ano de serviço, um trinta e cinco avos ao homem e um
trinta avos à mulher. O inciso II estabelece piso de um salário mínimo.

No Ciclo 1, esta forma governa a causa comum no segmento de 31/12/2003 a
19/02/2004. A unidade continua aplicável a ambos os sexos porque o sexo não
seleciona outra hipótese jurídica; ele é entrada do cálculo e determina o
denominador.

O piso não aparece em `limitadores` porque o vocabulário estrutural atual só
modela o redutor de pensão acima do teto do RGPS. A obrigação está explicitada
na fórmula e vinculada ao inciso II; isso é limitação do schema, não dúvida
jurídica.

# Fórmula

```
denominador = 35, se homem; 30, se mulher
fração = min(1, anos_de_serviço / denominador)
provento_bruto = remuneração_do_cargo_efetivo × fração
provento = max(salário_mínimo, provento_bruto)
```

A lei fala em anos de serviço. Não se converte silenciosamente a fração para
dias; eventual regra de contagem de frações de ano precisa ser demonstrada pelo
procedimento de apuração do tempo.

# Entradas e saídas

Entradas: remuneração do cargo efetivo, sexo, anos de serviço reconhecidos e
salário mínimo vigente na concessão.

Saída: provento mensal proporcional, em moeda, limitado à própria base pela
fração máxima igual a 1 e nunca inferior ao salário mínimo.
