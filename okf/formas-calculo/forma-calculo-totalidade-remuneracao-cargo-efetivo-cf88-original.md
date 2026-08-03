---
type: FormaCalculo
id: forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original
nome: Vencimento do cargo acrescido de adicional por tempo e vantagens — CF/88 original
base:
  tipo: vencimento_cargo_acrescido_vantagens_pecuniarias
  dispositivos:
    - /dispositivos/lce-39-1990/art-156/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
ajustes: []
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O rótulo `Valor Efetivo` não identifica a composição estatutária da
    base, a redação constitucional aplicável nem o ramo sem
    proporcionalização. Falta transcrever o dispositivo equivalente da LC
    1/1984 para completar a cobertura documental do primeiro trecho.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original define
a invalidez permanente e reserva o ramo sem proporcionalização às causas
qualificadas. Ele não define a composição da base.

Nos períodos disciplinados pela LCE 39/1990 e pela LCE 68/1992, a base é o
vencimento do cargo acrescido da gratificação adicional por tempo de
serviço e de outras vantagens pecuniárias, conforme os arts. 156 e 236,
respectivamente. O dispositivo equivalente da LC 1/1984 ainda deve ser
transcrito para completar a cobertura documental do primeiro trecho da
janela.

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

Entradas: vencimento do cargo, gratificação adicional por tempo de serviço
e demais vantagens pecuniárias incluídas pelo estatuto vigente na data do
direito.

Saída: provento inicial mensal sem redução proporcional ao tempo.

# Implementação

A projeção atual usa `tipo_calculo: Valor Efetivo` com `integral: S`. A
fidelidade é parcial porque o enum não explicita a composição da base nem a
redação normativa aplicável.

# Onde esta forma é usada

No Ciclo 1, nas três unidades qualificadas de invalidez sob a CF/88
original: acidente em serviço, moléstia profissional e doença grave
catalogada.
