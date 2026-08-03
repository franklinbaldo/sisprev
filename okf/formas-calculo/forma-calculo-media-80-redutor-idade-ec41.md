---
type: FormaCalculo
id: forma-calculo-media-80-redutor-idade-ec41
nome: Média das 80% maiores remunerações com redutor por idade — EC 41/2003
base:
  tipo: media_remuneracoes_contribuicao
  percentual_periodo: 80
  competencia_inicial: 1994-07
  dispositivos:
    - /dispositivos/cf88/art-40-par-3/ec-41-2003.md
    - /dispositivos/lei-10887-2004/art-1/original.md
ajustes:
  - tipo: redutor_idade_por_ano_antecipado
    ordem: 2
    percentual_ate_marco: 3.5
    percentual_a_partir_marco: 5
    marco_alteracao: 2006-01-01
    dispositivos:
      - /dispositivos/ec-41-2003/art-2-par-1/original.md
      - /dispositivos/ec-41-2003/art-2-par-1-inc-i/original.md
      - /dispositivos/ec-41-2003/art-2-par-1-inc-ii/original.md
      - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
      - /dispositivos/cf88/art-40-par-5/ec-20-1998.md
limitadores:
  - tipo: teto_remuneracao_cargo_efetivo
    ordem: 1
    dispositivos:
      - /dispositivos/lei-10887-2004/art-1-par-5/original.md
projecao_sisprev:
  tipo_calculo: Valor Médio com Redutor da Idade
  fidelidade: parcial
  justificativa: >-
    O rótulo identifica média e redutor, mas não informa a seleção das 80%
    maiores remunerações, o teto da remuneração, as alíquotas de 3,5% e 5%, o
    marco de 1º de janeiro de 2006 nem as idades de referência.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

Primeiro calcula-se a média contributiva da Lei 10.887/2004 e aplica-se o teto
da remuneração do cargo efetivo. Depois o art. 2º, § 1º, da EC 41/2003 reduz o
resultado por ano de antecipação em relação às idades constitucionais de
referência.

A taxa é de 3,5% para quem completou as exigências até 31 de dezembro de 2005 e
de 5% para quem as completou a partir de 1º de janeiro de 2006. Para professor,
a idade de referência vem do art. 40, § 5º; nos demais casos, do § 1º, III,
alínea “a”, ambos na redação da EC 20/1998.

# Fórmula

```text
base = min(média_das_80_por_cento_maiores, remuneração_cargo_efetivo)
taxa = 0,035, se requisitos até 31/12/2005; 0,05, se a partir de 01/01/2006
provento = base × (1 - taxa × anos_antecipados)
```

O texto constitucional fala em redução “para cada ano antecipado”. A regra de
tratamento de fração de ano não foi identificada nesta autoria e não deve ser
inventada pela implementação.

# Entradas e saídas

Entradas: série contributiva atualizada, remuneração do cargo efetivo, data de
implementação dos requisitos, idade na concessão, sexo e indicação de exercício
exclusivo de magistério.

Saída: `provento_inicial`, após média, teto e redutor, nessa ordem.
