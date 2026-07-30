---
okf_version: '0.1'
---

# Formas de cálculo de benefício

Uma fórmula por documento, decomposta em `base`, `ajustes` e `limitadores`, com
os dispositivos que fundamentam cada componente e a explicação de como calcular.

O `tipo_calculo` do Sisprev entra em `projecao_sisprev`, como **projeção legada
da fórmula** — não como a identidade dela. O motivo está em
`scripts/forma_calculo_schema.py`: o enum mistura base, ajuste e limitador no
mesmo rótulo, e a `regra-0025` é a prova de que existe combinação jurídica
conhecida sem rótulo que a represente.
