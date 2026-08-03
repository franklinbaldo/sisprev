---
type: FormaCalculo
id: forma-calculo-pensao-ec41-servidor-aposentado
nome: Pensão sobre proventos do servidor aposentado — teto do RGPS e 70% do excedente
base:
  tipo: totalidade_proventos_servidor_falecido
  dispositivos:
    - /dispositivos/cf88/art-40-par-7-inc-i/ec-41-2003.md
ajustes: []
limitadores:
  - tipo: teto_rgps_mais_percentual_do_excedente
    ordem: 1
    percentual_excedente: 70
    dispositivos:
      - /dispositivos/cf88/art-40-par-7-inc-i/ec-41-2003.md
projecao_sisprev:
  tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS
  fidelidade: parcial
  justificativa: >-
    O rótulo reproduz a operação sobre o excedente, mas não distingue a base
    constituída pelos proventos do aposentado da base remuneratória aplicável
    quando o servidor falece em atividade.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

A base é a totalidade dos proventos do servidor aposentado na data do óbito. O
art. 40, § 7º, I, na redação da EC 41/2003, preserva integralmente a parcela até
o teto do RGPS e acrescenta 70% da parcela que o exceder.

# Fórmula

```text
até_teto = min(proventos, teto_rgps)
excedente = max(0, proventos - teto_rgps)
pensão = até_teto + 0,70 × excedente
```

# Entradas e saídas

Entradas: `proventos_servidor_falecido` e `teto_rgps` vigente na competência
aplicável.

Saída: `valor_total_pensao`, antes de eventual rateio entre beneficiários.
