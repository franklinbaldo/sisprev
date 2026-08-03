---
type: FormaCalculo
id: forma-calculo-media-proporcional-lc228-lei10887
nome: Média federal proporcional pela fração anual da LC 228/2000
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/mp-167-2004/art-1/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/lce-228-2000/art-43/original.md
      - /dispositivos/lce-228-2000/art-43-par-unico-inc-i/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Médio
  fidelidade: parcial
  justificativa: >-
    `Valor Médio` nomeia a base — a média federal de 80% — e a
    proporcionalidade vai em `integral: N`. `Proporcionalidade Dias` afirmaria
    medida errada: a fração da LC 228 é anual, não diária. Fica sem coluna a
    medida da fração.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

Entre 20/02/2004 e 12/03/2008, a MP 167/2004 e, depois, a Lei 10.887/2004
substituem a remuneração do cargo pela média de 80% das maiores remunerações de
contribuição. A LC 228/2000 continua fornecendo o ramo proporcional da
invalidez e sua fração: 1/35 da base por ano para homem e 1/30 para mulher, com
piso de um salário mínimo.

A conjugação respeita a hierarquia: a norma federal posterior determina a base
exigida pelo § 3º do art. 40; a lei estadual permanece aplicável à medida da
proporcionalidade e ao piso, enquanto não substituída pela LCE 432/2008.

O piso não aparece em `limitadores` porque o vocabulário estrutural atual não
contém piso simples. Ele permanece parte obrigatória da fórmula e está
transcrito no art. 43, parágrafo único, II, da LC 228.

# Fórmula

```
base = média_atualizada(das maiores remunerações de contribuição de 80% do período)
denominador = 35, se homem; 30, se mulher
fração = min(1, anos_de_serviço / denominador)
provento_bruto = base × fração
provento = max(salário_mínimo, provento_bruto)
```

# Entradas e saídas

Entradas: histórico contributivo, índices de atualização, sexo, anos de serviço
reconhecidos e salário mínimo vigente na concessão.

Saída: provento inicial mensal pela média proporcional, em moeda. A lei estadual
fala em anos; eventual conversão de frações de ano depende do protocolo de
apuração do tempo e não é presumida por esta forma.
