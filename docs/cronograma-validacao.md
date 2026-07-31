# Cronograma diario de validacao das regras

Objetivo: validar cinco regras por dia, agrupando por similaridade juridica sempre que possivel. A ordem prioriza familias juridicas (invalidez, pensao, idade, incapacidade, compulsoria, deficiencia, agentes nocivos e demais voluntarias), e usa o titulo juridico normalizado para desempatar. As regras de magisterio e policial permanecem nos lotes finais. Inicio sugerido: **01/08/2026**.

Cada regra deve ser revisada no arquivo `okf/regras-sisprev/regras/regra-NNNN.md`. Registre correcoes, duvidas e achados no proprio arquivo ou na unidade auditada correspondente.

## Lotes

| Dia | Data | Regras | Grupo predominante | Concluido |
|---:|:---:|:---|:---|:---:|
| 1 | 01/08/2026 | regra-0004, regra-0001, regra-0002, regra-0008, regra-0009 | invalidez | [ ] |
| 2 | 02/08/2026 | regra-0006, regra-0007, regra-0003, regra-0005, regra-0014 | pensao, invalidez | [ ] |
| 3 | 03/08/2026 | regra-0015, regra-0016, regra-0017, regra-0018, regra-0011 | pensao | [ ] |
| 4 | 04/08/2026 | regra-0012, regra-0013, regra-0010, regra-0024, regra-0026 | pensao, idade | [ ] |
| 5 | 05/08/2026 | regra-0091, regra-0087, regra-0089, regra-0033, regra-0034 | idade | [ ] |
| 6 | 06/08/2026 | regra-0028, regra-0029, regra-0085, regra-0086, regra-0105 | idade | [ ] |
| 7 | 07/08/2026 | regra-0106, regra-0043, regra-0044, regra-0051, regra-0052 | idade | [ ] |
| 8 | 08/08/2026 | regra-0035, regra-0036, regra-0101, regra-0102, regra-0022 | idade, incapacidade | [ ] |
| 9 | 09/08/2026 | regra-0021, regra-0019, regra-0020, regra-0030, regra-0031 | incapacidade, compulsoria | [ ] |
| 10 | 10/08/2026 | regra-0032, regra-0027, regra-0023, regra-0025, regra-0068 | compulsoria, agentes-nocivos | [ ] |
| 11 | 11/08/2026 | regra-0069, regra-0070, regra-0071, regra-0065, regra-0066 | agentes-nocivos | [ ] |
| 12 | 12/08/2026 | regra-0067, regra-0061, regra-0062, regra-0063, regra-0064 | voluntaria-geral, agentes-nocivos | [ ] |
| 13 | 13/08/2026 | regra-0059, regra-0060, regra-0047, regra-0048, regra-0097 | voluntaria-geral | [ ] |
| 14 | 14/08/2026 | regra-0098, regra-0093, regra-0094, regra-0055, regra-0056 | voluntaria-geral | [ ] |
| 15 | 15/08/2026 | regra-0037, regra-0038, regra-0092, regra-0088, regra-0090 | magisterio, voluntaria-geral | [ ] |
| 16 | 16/08/2026 | regra-0058, regra-0057, regra-0039, regra-0040, regra-0049 | magisterio | [ ] |
| 17 | 17/08/2026 | regra-0050, regra-0099, regra-0100, regra-0045, regra-0046 | magisterio | [ ] |
| 18 | 18/08/2026 | regra-0053, regra-0054, regra-0041, regra-0042, regra-0103 | magisterio | [ ] |
| 19 | 19/08/2026 | regra-0104, regra-0095, regra-0096, regra-0107, regra-0108 | magisterio | [ ] |
| 20 | 20/08/2026 | regra-0109, regra-0110, regra-0080, regra-0081, regra-0072 | policial | [ ] |
| 21 | 21/08/2026 | regra-0073, regra-0074, regra-0075, regra-0076, regra-0077 | policial | [ ] |
| 22 | 22/08/2026 | regra-0078, regra-0079, regra-0082, regra-0083, regra-0111 | policial | [ ] |
| 23 | 23/08/2026 | regra-0112, regra-0084 | policial | [ ] |

## Criterio de encerramento diario

- [ ] As regras foram comparadas com as fontes legais aplicaveis.
- [ ] Correcoes foram feitas somente nos arquivos OKF correspondentes.
- [ ] Duvidas e achados foram registrados.
- [ ] Os artefatos derivados foram regenerados com `uv run python scripts/gerar_indices.py`.
- [ ] Validadores e testes foram executados antes do commit.

O ultimo lote contem duas regras porque 112 nao e multiplo de cinco. Os grupos de magisterio e policial comecam no lote 15 e ocupam todos os lotes seguintes.
