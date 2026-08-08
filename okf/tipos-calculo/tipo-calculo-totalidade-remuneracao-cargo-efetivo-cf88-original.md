---
type: TipoCalculo
id: tipo-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original
nome: Vencimento do cargo acrescido de adicional por tempo e vantagens — CF/88 original
base:
  tipo: vencimento_cargo_acrescido_vantagens_pecuniarias
  dispositivos:
    - /dispositivos/lce-1-1984/art-94/original.md
    - /dispositivos/lce-1-1984/art-154-par-2/original.md
    - /dispositivos/lce-39-1990/art-156/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
ajustes: []
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O rótulo `Valor Efetivo` não identifica a composição estatutária da
    base, a redação constitucional aplicável nem o ramo sem
    proporcionalização. No trecho da LCE 1/1984, a referência à remuneração
    resulta de interpretação sistemática dos arts. 94 e 154, § 2º.
autorado_por: openai-codex
autorado_em: 2026-08-08
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original define
a invalidez permanente e reserva o ramo sem proporcionalização às causas
qualificadas. Ele não define a composição da base.

No período da LCE 1/1984, a remuneração da atividade é a referência adotada por
interpretação sistemática: o art. 94 a define como vencimento mais vantagens
financeiras asseguradas em lei, e o art. 154, § 2º, limita os proventos a ela.
“Integrais” significa que não incide a redução de 1/30 reservada aos demais
casos pelo mesmo artigo. A norma não usa a fórmula posterior “o cálculo terá
por base”, e essa ponte interpretativa fica expressamente registrada.

Nos períodos disciplinados pela LCE 39/1990 e pela LCE 68/1992, a base é o
vencimento do cargo acrescido da gratificação adicional por tempo de
serviço e de outras vantagens pecuniárias, conforme os arts. 156 e 236,
respectivamente.

A paridade fica fora desta forma. Ela decorre do art. 40, § 4º, do texto
constitucional original e constitui regime de revisão posterior.

# Fórmula

```text
provento_inicial = vencimento_cargo
        + gratificacao_adicional_tempo_servico
        + outras_vantagens_pecuniarias
```

Não incide redução proporcional ao tempo neste ramo.

# Entradas e saídas

Entradas: vencimento do cargo, gratificação adicional por tempo
e demais vantagens pecuniárias incluídas pelo estatuto vigente na data do
direito.

Saída: provento inicial mensal sem redução proporcional ao tempo.

# Implementação

A projeção atual usa `tipo_calculo: Valor Efetivo` com `integral: S`. A
fidelidade é parcial porque o enum não explicita a composição da base nem a
redação normativa aplicável.

# Onde esta forma é usada

No Ciclo 9, nas três unidades qualificadas de invalidez sob a CF/88
original: acidente em serviço, moléstia profissional e doença grave
catalogada.
