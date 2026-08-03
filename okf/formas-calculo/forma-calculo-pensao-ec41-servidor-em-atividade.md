---
type: FormaCalculo
id: forma-calculo-pensao-ec41-servidor-em-atividade
nome: Pensão sobre remuneração do servidor em atividade — teto do RGPS e 70% do excedente
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-par-7-inc-ii/ec-41-2003.md
ajustes: []
limitadores:
  - tipo: teto_rgps_mais_percentual_do_excedente
    ordem: 1
    percentual_excedente: 70
    dispositivos:
      - /dispositivos/cf88/art-40-par-7-inc-ii/ec-41-2003.md
projecao_sisprev:
  tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS
  fidelidade: parcial
  justificativa: >-
    O rótulo reproduz a operação sobre o excedente, mas não distingue a base
    remuneratória do servidor em atividade da base formada pelos proventos do
    servidor já aposentado.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

A base é a totalidade da remuneração do servidor no cargo efetivo na data do
óbito. O art. 40, § 7º, II, na redação da EC 41/2003, preserva integralmente a
parcela até o teto do RGPS e acrescenta 70% da parcela excedente.

# Fórmula

```text
até_teto = min(remuneração_cargo_efetivo, teto_rgps)
excedente = max(0, remuneração_cargo_efetivo - teto_rgps)
pensão = até_teto + 0,70 × excedente
```

# Entradas e saídas

Entradas: `remuneracao_cargo_efetivo` e `teto_rgps` vigente na competência
aplicável.

Saída: `valor_total_pensao`, antes de eventual rateio entre beneficiários.
