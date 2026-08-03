---
type: FormaCalculo
id: forma-calculo-media-proporcional-dias-lce432
nome: Média contributiva da LCE 432/2008, proporcional ao tempo em dias
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/lce-432-2008/art-45/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Proporcionalidade Dias
  fidelidade: parcial
  justificativa: >-
    O rótulo legado expressa a fração em dias, mas não informa que ela incide
    sobre a média contributiva do art. 45 nem os limites dos §§ 9º e 10. A
    fórmula completa depende de todos esses componentes.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O art. 45 fornece a base durante toda a vigência da LCE 432/2008: média
aritmética simples das maiores remunerações que serviram de base às
contribuições, correspondente a 80% do período contributivo. A redação original
e a dada pela LCE 672/2012 têm a mesma estrutura material para este ciclo.

O art. 17 determina que os proventos proporcionais usem uma fração cujo
numerador é o tempo total de contribuição e cujo denominador é o tempo exigido
para a aposentadoria voluntária correspondente. O § 2º manda considerar os
períodos em dias.

A ordem é juridicamente relevante. Primeiro atualizam-se e limitam-se as
remunerações mês a mês conforme o art. 45, § 9º; depois calcula-se a média; o
resultado fica sujeito ao teto da remuneração do cargo efetivo do § 10; somente
então o art. 17 manda aplicar a fração proporcional. O próprio art. 17, § 1º,
remete ao valor do art. 45 “após a aplicação do limite do § 10”.

Os limites simples dos §§ 9º e 10 não aparecem em `limitadores` porque o
vocabulário estrutural atual só contém o redutor de pensão acima do teto do
RGPS. Eles estão transcritos e permanecem obrigatórios na execução; a limitação
é do schema, não da fórmula conhecida.

# Fórmula

```
remunerações_atualizadas = atualizar_mês_a_mês(remunerações_contributivas)
remunerações_limitadas = aplicar_limites_mensais_do_§9(remunerações_atualizadas)
media = média(das maiores remunerações_limitadas correspondentes a 80% do período)
base_limitada = min(media, remuneração_do_cargo_efetivo)  # § 10
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base_limitada × fração
```

# Entradas e saídas

Entradas: remunerações contributivas do período, índices de atualização,
limites mensais, quantidade de competências que compõem os 80%, remuneração do
cargo efetivo, tempo de contribuição em dias e tempo exigido em dias para a
aposentadoria voluntária de referência.

Saída: provento mensal proporcional, em moeda, nunca superior à base limitada.

A forma não resolve sozinha qual aposentadoria voluntária fornece o denominador
em cada caso; essa seleção depende da situação funcional e deve ser registrada
na instrução.

# Onde esta forma é usada

No Ciclo 1, descreve o ramo de causa comum da regra geral da EC 41 desde
13/03/2008 e também os direitos preservados sob a LCE 432/2008 até o fecho do
art. 4º da ECE 146/2021.
