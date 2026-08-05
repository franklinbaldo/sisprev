---
type: TipoCalculo
id: tipo-calculo-totalidade-remuneracao-cargo-efetivo-ec20
nome: Totalidade da remuneração do cargo efetivo — CF, redação da EC 20/1998
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
ajustes: []
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O rótulo sugere uma base ligada ao cargo efetivo, mas não declara que o
    valor corresponde à totalidade da remuneração nem identifica a redação
    constitucional aplicável.
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

O art. 40, § 3º, na redação da EC 20/1998, determina que os proventos sejam
calculados com base na remuneração do servidor no cargo efetivo e correspondam à
totalidade dessa remuneração. Não há média, fração, redutor ou limitador nesta
forma isolada.

# Fórmula

```text
provento = totalidade_remuneracao_cargo_efetivo
```

# Entradas e saídas

Entrada: `remuneracao_cargo_efetivo`, valor monetário formado pelas parcelas que
a legislação aplicável inclua na remuneração do cargo.

Saída: `provento_inicial`, igual à entrada.

A composição concreta das rubricas remuneratórias não é deduzida do rótulo
`Valor Efetivo`; deve ser apurada segundo a norma remuneratória do cargo e o
marco temporal do caso.
