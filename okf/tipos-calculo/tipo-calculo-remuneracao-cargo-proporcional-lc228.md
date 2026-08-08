---
type: TipoCalculo
id: tipo-calculo-remuneracao-cargo-proporcional-lc228
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
      - /dispositivos/ec-20-1998/art-4/original.md
      - /dispositivos/lce-68-1992/art-137/original.md
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    `Valor Efetivo` nomeia a base — remuneração do cargo efetivo — e a
    proporcionalidade vai em `integral: N`. `Proporcionalidade Dias` seria
    pior que omissão: no uso do Sisprev esse rótulo designa a média
    proporcionalizada em dias do art. 17 da LCE 432, e aqui a base não é média
    e a fração é anual (1/35 ou 1/30). Ficam sem coluna a medida da fração e o
    piso de um salário mínimo.
autorado_por: openai-codex
autorado_em: 2026-08-08
---

# Como calcular

O art. 43, parágrafo único, I, da LC 228/2000 fixa a base na remuneração do cargo
efetivo e atribui, por ano de serviço, um trinta e cinco avos ao homem e um
trinta avos à mulher. O inciso II estabelece piso de um salário mínimo. O art.
4º da EC 20 permite contar como contribuição o tempo de serviço reconhecido, e
o art. 137 da LCE 68/1992 — não alcançado pela revogação dos arts. 229 a 257 —
disciplina a conversão anual.

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
anos_inteiros = piso(tempo_de_serviço_dias / 365)
resto = tempo_de_serviço_dias mod 365
anos_convertidos = anos_inteiros + (1 se resto > 180; 0 se resto <= 180)
denominador = 35, se homem; 30, se mulher
fração = min(1, anos_convertidos / denominador)
provento_bruto = remuneração_do_cargo_efetivo × fração
provento = max(salário_mínimo, provento_bruto)
```

A lei fala em anos de serviço. A conversão acima é jurídica: até 180 dias
restantes não contam e mais de 180 arredondam para um ano. Não se substitui essa
regra por proporcionalização diária sem fundamento.

# Entradas e saídas

Entradas: remuneração do cargo efetivo, sexo, dias de serviço reconhecidos e
salário mínimo vigente na concessão.

Saída: provento mensal proporcional, em moeda, limitado à própria base pela
fração máxima igual a 1 e nunca inferior ao salário mínimo.
