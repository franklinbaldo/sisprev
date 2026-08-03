---
type: FormaCalculo
id: forma-calculo-remuneracao-cargo-proporcional-cf88-original
nome: Base remuneratória com proporcionalização pelo tempo — CF/88, texto original
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-inc-i/original.md
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
    `Valor Efetivo` não representa sozinho o ajuste proporcional. A estrutura
    base remuneratória vezes fração de tempo está identificada, mas a medida da
    fração e a composição concreta da base dependem da legislação estadual
    vigente na data do direito e ainda não foram decompostas.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original determina
proventos proporcionais nos casos de invalidez que não decorram de acidente em
serviço, moléstia profissional ou doença grave, contagiosa ou incurável
especificada em lei.

A estrutura jurídica identificada para o Ciclo 1 é suficiente para distinguir
esta forma da integral: parte-se da base remuneratória aplicável e incide uma
fração relacionada ao tempo. O dispositivo constitucional define o ramo
proporcional, mas não traz a medida da fração nem resolve a composição concreta
da base.

Esses parâmetros devem ser apurados na legislação estadual vigente quando o
direito foi implementado. A pendência não impede vincular a forma correta à
regra; impede apenas preencher denominador, conversão em dias ou rubricas sem
fonte.

A paridade não integra esta fórmula. Ela decorre do art. 40, § 4º, do texto
original e opera como regime de revisão posterior.

# Fórmula

```text
provento_inicial = base_remuneratoria_aplicavel × fracao_proporcional_tempo
```

A estrutura está identificada. Permanecem pendentes:

- a composição de `base_remuneratoria_aplicavel` em cada trecho temporal;
- o denominador e a medida de `fracao_proporcional_tempo`;
- a convenção de conversão do tempo em unidade operacional.

# Entradas e saídas

Entradas já identificadas:

- base remuneratória juridicamente aplicável;
- tempo apurado no caso;
- parâmetros temporais definidos pela legislação estadual aplicável.

Saída: provento inicial proporcional. O valor numérico somente pode ser obtido
após o fechamento dos parâmetros pendentes.

# Implementação

A projeção atual combina `tipo_calculo: Valor Efetivo` com `integral: N`. Essa
combinação diferencia o ramo no legado, mas não representa integralmente a
fórmula. A forma permanece com fidelidade `pendente` até o cotejo das normas
estaduais da janela de 05/10/1988 a 15/12/1998.

# Onde esta forma é usada

No Ciclo 1, na unidade `invalidez-cf88-original-causa-comum`.
