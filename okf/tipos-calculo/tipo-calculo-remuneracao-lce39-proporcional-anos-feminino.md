---
type: TipoCalculo
id: tipo-calculo-remuneracao-lce39-proporcional-anos-feminino
nome: Vencimento e vantagens, 1/30 por ano — LCE 39/1990, mulher
base:
  tipo: vencimento_cargo_acrescido_vantagens_pecuniarias
  dispositivos:
    - /dispositivos/lce-39-1990/art-156/original.md
ajustes:
  - tipo: proporcional_tempo_servico
    ordem: 1
    dispositivos:
      - /dispositivos/lce-39-1990/art-155-par-unico/original.md
      - /dispositivos/lce-39-1990/art-132/original.md
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O enum não informa a razão feminina de 1/30 nem a conversão anual com
    arredondamento.
autorado_por: openai-codex
autorado_em: 2026-08-08
---

# Fórmula

```text
anos = inteiros(dias / 365) + (1 se resto > 180; senão 0)
fracao = min(1, anos / 30)
provento_inicial = (vencimento + adicional_tempo + outras_vantagens) × fracao
```

A fórmula vale de 31/07/1990 a 08/12/1992 e somente para mulher. A diferença de
denominador em relação ao homem é textual e cria tipo de cálculo distinto.

# Onde esta forma é usada

Na unidade `invalidez-cf88-original-lce39-feminino-causa-comum` do Ciclo 9.
