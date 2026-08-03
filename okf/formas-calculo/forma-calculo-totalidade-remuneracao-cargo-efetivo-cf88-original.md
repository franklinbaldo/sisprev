---
type: FormaCalculo
id: forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original
nome: Proventos integrais sobre a base remuneratória aplicável — CF/88, texto original
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-inc-i/original.md
ajustes: []
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O rótulo `Valor Efetivo` não identifica a redação constitucional aplicável,
    não explicita que o ramo é integral e não descreve a composição concreta da
    base remuneratória, que depende da legislação vigente na data do direito.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original reserva
**proventos integrais** às invalidezes decorrentes de acidente em serviço,
moléstia profissional ou doença grave, contagiosa ou incurável especificada em
lei.

Para o Ciclo 1, esta forma fecha a distinção juridicamente necessária: o ramo
não sofre redução proporcional ao tempo. A base é a remuneração do cargo
efetivo juridicamente aplicável ao caso, mas a composição concreta de suas
rubricas continua submetida à legislação estadual vigente quando o direito foi
implementado.

Não há fração proporcional a descobrir neste ramo. Isso não significa que toda
a operação esteja parametrizada: composição da base, rubricas incluídas e
projeção fiel no Sisprev permanecem matérias de integração e detalhamento.

A paridade fica fora desta forma. Ela decorre do art. 40, § 4º, do mesmo texto
original e constitui regime de revisão posterior, não componente do cálculo
inicial.

# Fórmula

```text
provento_inicial = base_remuneratoria_integral_aplicavel
```

A expressão identifica a ausência de proporcionalização. A composição de
`base_remuneratoria_integral_aplicavel` deve ser apurada segundo a legislação
vigente na data do direito e não é inferida do rótulo `Valor Efetivo`.

# Entradas e saídas

Entrada: base remuneratória do cargo efetivo apurada segundo a legislação
aplicável ao marco temporal do caso.

Saída: provento inicial mensal sem redução proporcional ao tempo.

# Implementação

A projeção atual usa `tipo_calculo: Valor Efetivo` em conjunto com
`integral: S`. A fidelidade é parcial até que o Sisprev represente de modo
explícito a redação normativa e a composição da base.

# Onde esta forma é usada

No Ciclo 1, nas três unidades qualificadas de invalidez sob a CF/88 original:
acidente em serviço, moléstia profissional e doença grave catalogada.
