---
type: FormaCalculo
id: forma-calculo-remuneracao-cargo-proporcional-cf88-original
nome: Vencimento do cargo e vantagens, proporcional ao tempo — CF/88 original
base:
  tipo: vencimento_cargo_acrescido_vantagens_pecuniarias
  dispositivos:
    - /dispositivos/lce-39-1990/art-156/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-inc-i/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Efetivo
  fidelidade: pendente
  justificativa: >-
    `Valor Efetivo` não representa o ajuste proporcional. A composição
    estatutária da base está identificada, mas a medida da fração e a
    conversão operacional do tempo ainda precisam ser decompostas por
    trecho; falta transcrever o dispositivo equivalente da LC 1/1984 para
    completar a cobertura documental do primeiro período.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original define
o ramo proporcional residual, mas não define a composição da base.

Nos períodos disciplinados pela LCE 39/1990 e pela LCE 68/1992, a base é o
vencimento do cargo acrescido da gratificação adicional por tempo de
serviço e de outras vantagens pecuniárias, conforme os arts. 156 e 236,
respectivamente. Sobre essa base incide a fração proporcional ao tempo.

Permanecem pendentes a medida da fração e a convenção operacional de tempo
em cada trecho, além da transcrição do dispositivo equivalente da LC
1/1984.

A paridade não integra esta fórmula; decorre do art. 40, § 4º, do texto
constitucional original e opera como regime de revisão posterior.

# Fórmula

```text
base_estatutaria = vencimento_cargo
       + gratificacao_adicional_tempo_servico
       + outras_vantagens_pecuniarias

provento_inicial = base_estatutaria × fracao_proporcional_tempo
```

# Entradas e saídas

Entradas já identificadas: vencimento do cargo, gratificação adicional por
tempo de serviço, outras vantagens pecuniárias e tempo apurado no caso.

Saída: provento inicial proporcional. O valor numérico depende do fechamento
da medida da fração e da conversão operacional do tempo.

# Implementação

A projeção atual combina `tipo_calculo: Valor Efetivo` com `integral: N`.
Essa combinação distingue o ramo no legado, mas não representa a fórmula
completa.

# Onde esta forma é usada

No Ciclo 1, na unidade `invalidez-cf88-original-causa-comum`.
