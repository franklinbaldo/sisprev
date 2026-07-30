"""O único parâmetro numérico da gramática de ``nome`` (decisão de 2026-07-30).

A gramática em si é **prosa**, e mora em
[`docs/spec/regra.md`](../docs/spec/regra.md) — seis posições ordenadas, cada
uma entrando só quando discrimina. Deliberadamente não há aqui validador,
gerador ou enum de posições: a decisão que fixou a gramática também registrou
que "se as posições não distinguem, não se desempata pelo número do artigo, é
lacuna do modelo" — julgamento que nenhuma função faz, e um validador de forma
daria luz verde justamente ao nome único e inútil que a gramática existe para
evitar.

O que precisa de fonte única é só o teto, porque é um **número**, e a
convenção do repositório é ancorar número que sustenta argumento em teste
contra a importação imutável (``tests/test_nome_gramatica.py``).
"""

from __future__ import annotations

# O comprimento do maior NOME da importação original — logo, um comprimento que
# o Sisprev comprovadamente aceita. Não é o limite da tela: esse segue não
# conferido, e a decisão foi fixar a gramática apesar disso, o que faz deste o
# único teto com prova por trás.
TETO_DE_COMPRIMENTO = 115
