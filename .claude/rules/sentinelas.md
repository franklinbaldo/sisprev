---
paths:
  - "okf/regras-sisprev/**"
  - "okf/regras-propostas/**"
  - "site/src/**"
  - "scripts/**"
---

# Datas sentinela

- `01/01/1900`, `01/01/1910` e `01/01/1950` nas colunas `_APOS`, e
  `31/12/2099` nas colunas `_ATE`, significam **ausência de limite naquele
  eixo** — três convenções de digitação para a mesma coisa, declaradas em
  `site/src/lib/sentinela.ts`. Trate-as como ausência: lida como data real,
  uma regra sem piso vira exigência de ingresso depois de 1950, e num anexo
  impresso `31/12/2099` pede ressalva porque quem assina o lê como fronteira
  de verdade.
- `01/01/1969` fica **fora** do conjunto por decisão registrada
  (`regra-0003`): é suspeita de erro de digitação, e ampliar o conjunto de
  sentinelas exige ato registrado de alguém.
