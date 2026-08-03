---
type: FormaCalculo
id: forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original
nome: Totalidade da remuneração do cargo efetivo — CF/88, texto original
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
    O rótulo sugere base ligada ao cargo efetivo, mas não declara que o valor
    corresponde à totalidade da remuneração nem identifica a redação
    constitucional aplicável. `integral: S` na mesma linha confirma a ausência
    de redução proporcional.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original reserva
**proventos integrais** às invalidezes decorrentes de acidente em serviço,
moléstia profissional ou doença grave, contagiosa ou incurável especificada em
lei. Integrais, aqui, significa a totalidade da remuneração do cargo efetivo em
que se deu a aposentadoria, sem redução.

**Não há medida a descobrir.** É o que separa esta forma da do ramo residual do
mesmo inciso: ali a Constituição diz "proporcionais" sem denominador, e a fração
depende de lei que a auditoria ainda não identificou para esta janela; aqui o
próprio dispositivo fecha o cálculo, porque "integral" não admite fração.

A paridade fica fora desta forma. Ela decorre do art. 40, § 4º, do mesmo texto
original — revisão dos proventos na mesma proporção e data da remuneração dos
ativos —, e é regime de reajuste, não fórmula de concessão (P16).

# Fórmula

```
provento = remuneração_do_cargo_efetivo
```

# Entradas e saídas

Entrada: a remuneração do cargo efetivo em que se deu a aposentadoria.

Saída: provento inicial mensal, em moeda, igual a essa remuneração.

# Onde esta forma é usada

No Ciclo 1, as três unidades qualificadas de invalidez sob a CF/88 original —
acidente em serviço, moléstia profissional e doença grave catalogada.
