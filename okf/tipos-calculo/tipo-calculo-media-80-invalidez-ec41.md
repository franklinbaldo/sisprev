---
type: TipoCalculo
id: tipo-calculo-media-80-invalidez-ec41
nome: Média de 80% das remunerações de contribuição na invalidez da EC 41/2003
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/mp-167-2004/art-1/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
    - /dispositivos/lce-432-2008/art-45/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
ajustes: []
limitadores: []
origem_legada:
  tipo_calculo: Valor Médio
  fidelidade: parcial
  justificativa: >-
    `Valor Médio` identifica a base, mas não explicita o universo contributivo,
    os 80%, a atualização mensal nem o teto na remuneração do cargo previsto no
    § 10 do art. 45 durante a LCE 432/2008.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

Desde 20/02/2004, a MP 167/2004 — depois convertida na Lei 10.887/2004 — manda
considerar a média aritmética simples das maiores remunerações utilizadas como
base das contribuições, correspondentes a 80% do período contributivo desde
julho de 1994 ou desde o início da contribuição, se posterior. A LCE 432/2008
reproduziu a mesma base no art. 45, tanto na redação original quanto na redação
dada pela LCE 672/2012.

No segmento da LCE 432, os valores mensais são atualizados e submetidos aos
limites do § 9º antes da seleção das maiores remunerações; o provento final não
pode exceder a remuneração do cargo efetivo, conforme o § 10. Esses limitadores
não cabem no enum estrutural atual de `TipoCalculo`, mas são obrigatórios na
execução e estão transcritos em dispositivos próprios.

A forma descreve as causas qualificadas da regra geral da EC 41, nas quais não
há redução pelo tempo. Até 19/02/2004, aplica-se a forma da LC 228 baseada na
remuneração do cargo, não esta média.

# Fórmula

```
remunerações_atualizadas = atualizar_mês_a_mês(remunerações_contributivas)
remunerações_limitadas = aplicar_limites_mensais(remunerações_atualizadas)
base = média(das maiores remunerações_limitadas correspondentes a 80% do período)
provento = min(base, remuneração_do_cargo_efetivo)  # no segmento da LCE 432
```

# Entradas e saídas

Entradas: histórico de remunerações contributivas desde julho de 1994, índices
de atualização, limites mensais aplicáveis, quantidade de competências e
remuneração do cargo efetivo para o teto final da LCE 432.

Saída: provento inicial mensal pela média, em moeda, sem proporcionalização pelo
tempo.
