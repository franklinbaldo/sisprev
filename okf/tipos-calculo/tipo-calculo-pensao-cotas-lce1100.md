---
type: TipoCalculo
id: tipo-calculo-pensao-cotas-lce1100
nome: Pensão por cotas familiares e rateio igual — LCE 1.100/2021
base:
  tipo: proventos_aposentadoria_ou_incapacidade_hipotetica
  dispositivos:
    - /dispositivos/lce-1100-2021/art-49/original.md
ajustes:
  - tipo: cota_familiar_por_dependente
    ordem: 1
    percentual_base: 50
    percentual_por_dependente: 10
    percentual_maximo: 100
    dispositivos:
      - /dispositivos/lce-1100-2021/art-49/original.md
  - tipo: rateio_igual_dependentes
    ordem: 2
    dispositivos:
      - /dispositivos/lce-1100-2021/art-50/original.md
limitadores: []
origem_legada:
  tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte
  fidelidade: parcial
  justificativa: >-
    O rótulo identifica o pacote da pensão, mas não expõe a base alternativa,
    a cota de 50%, o acréscimo de 10 pontos por dependente, o máximo de 100%
    nem o rateio igual entre pensionistas.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

A base é o valor dos proventos que o servidor recebia ou, se estava em atividade,
o valor a que teria direito se fosse aposentado por incapacidade permanente na
data do óbito.

Aplica-se uma cota familiar de 50%, acrescida de 10 pontos percentuais por
dependente, até 100%. Havendo mais de um pensionista, o valor total é dividido em
partes iguais. O art. 50 também determina que a contribuição previdenciária seja
calculada sobre o benefício total, não isoladamente sobre cada cota.

# Fórmula

```text
percentual = min(100%, 50% + 10% × número_de_dependentes)
pensão_total = base × percentual
cota_individual = pensão_total / número_de_pensionistas
```

# Entradas e saídas

| entrada                            | tipo                       |
| ---------------------------------- | -------------------------- |
| proventos recebidos                | moeda, quando aposentado   |
| incapacidade hipotética            | moeda, quando em atividade |
| número de dependentes              | inteiro não negativo       |
| número de pensionistas habilitados | inteiro positivo           |

Saídas: `pensao_total` e `cota_individual`.

A fórmula não modela duração, reversão ou extinção das cotas, porque esses efeitos
pertencem à manutenção do benefício e a outros dispositivos.
