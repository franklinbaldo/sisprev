---
type: TipoCalculo
id: tipo-calculo-remuneracao-lce1-proporcional-anos
nome: Remuneração, 1/30 por ano de serviço — LCE 1/1984
base:
  tipo: remuneracao_atividade
  dispositivos:
    - /dispositivos/lce-1-1984/art-94/original.md
    - /dispositivos/lce-1-1984/art-154-par-2/original.md
ajustes:
  - tipo: proporcional_tempo_servico
    ordem: 1
    dispositivos:
      - /dispositivos/lce-1-1984/art-154-par-3/original.md
      - /dispositivos/lce-1-1984/art-86/original.md
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    O enum não informa a razão de 1/30, a apuração anual, o arredondamento nem
    a composição da remuneração que serve de referência.
autorado_por: openai-codex
autorado_em: 2026-08-08
---

# Como calcular

Esta fórmula vale para o direito implementado entre 05/10/1988 e 30/07/1990.
A LCE 1/1984 chama de remuneração o vencimento acrescido das vantagens
financeiras asseguradas por lei (art. 94), limita os proventos à remuneração da
atividade (art. 154, § 2º) e manda calcular a proporcionalidade à razão de 1/30
por ano de serviço (art. 154, § 3º).

A adoção da remuneração da atividade como referência da proporcionalização é
uma **interpretação sistemática**: o diploma não contém a fórmula posterior
“o cálculo terá por base”. Ela resulta da conjugação entre a definição de
remuneração, o limite expresso e os ramos integral/proporcional do art. 154.

O art. 86 determina apuração em dias, conversão por ano de 365 dias e
arredondamento: até 182 dias restantes não contam; acima disso, contam como um
ano.

# Fórmula

```text
anos = inteiros(dias / 365) + (1 se resto > 182; senão 0)
fracao = min(1, anos / 30)
provento_inicial = remuneracao_atividade × fracao
```

# Onde esta forma é usada

Na unidade `invalidez-cf88-original-lce1-causa-comum` do Ciclo 9.
