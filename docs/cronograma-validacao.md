# Cronograma temático de validação das regras

Objetivo: validar cada unidade juridica em um ciclo manejavel, agrupando regras relacionadas mesmo quando isso produz ciclos de tamanhos diferentes. A ordem prioriza familias juridicas e marcos normativos: invalidez/incapacidade, pensao, idade, deficiencia, agentes nocivos, voluntarias gerais, magisterio e policial. Inicio sugerido: **01/08/2026**.

Cada regra deve ser revisada no arquivo `okf/regras-sisprev/regras/regra-NNNN.md`. Registre correcoes, duvidas e achados no proprio arquivo ou na unidade auditada correspondente.

## Lotes

| Dia |    Data    | Regras                                                                                                                   | Grupo predominante                                  | Concluido |
| --: | :--------: | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- | :-------: |
|   1 | 01/08/2026 | 0001–0002, 0004, 0006–0009, 0019–0022                                                                                    | invalidez/incapacidade; 0003 e 0005 são referências |    [ ]    |
|   2 | 02/08/2026 | 0003, 0005, 0010–0018                                                                                                    | pensão por morte                                    |    [ ]    |
|   3 | 03/08/2026 | 0023–0034                                                                                                                | compulsória e idade                                 |    [ ]    |
|   4 | 04/08/2026 | 0035–0038, 0043–0044, 0047–0048, 0051–0052, 0055–0056, 0085–0087, 0089, 0091, 0093–0094, 0097–0098, 0101–0102, 0105–0106 | voluntária geral e transições                       |    [ ]    |
|   5 | 05/08/2026 | 0059–0064                                                                                                                | pessoa com deficiência                              |    [ ]    |
|   6 | 06/08/2026 | 0065–0071                                                                                                                | agentes nocivos                                     |    [ ]    |
|   7 | 07/08/2026 | 0039–0042, 0045–0046, 0049–0050, 0053–0054, 0057–0058, 0088, 0090, 0092, 0095–0096, 0099–0100, 0103–0104, 0107–0108      | magistério                                          |    [ ]    |
|   8 | 08/08/2026 | 0072–0084, 0109–0112                                                                                                     | policial                                            |    [ ]    |

## Ciclos temáticos e relatórios obrigatórios

Cada linha do cronograma é um ciclo operacional e gera seu próprio relatório ao final da validação. O campo histórico ciclo_de_validacao da CSV inicial continua apenas como metadado da regra; ele não define estes ciclos temáticos. O relatório não substitui os registros nos arquivos das regras: ele consolida o resultado, as pendências e os achados do ciclo.

| Ciclo |         Data          |                Regras | Entregavel                        |
| ----: | :-------------------: | --------------------: | :-------------------------------- |
|   1–8 | 01/08/2026–08/08/2026 | conforme tabela acima | docs/relatorio/ciclos/ciclo-NN.md |

O modelo de cada documento esta em docs/relatorio/modelo-ciclo.md. Um relatorio deve conter: regras conferidas, correcoes, regras sem correcao, pendencias abertas, achados, fontes legais, data, commit de origem e responsavel.

## Criterio de encerramento diario

- [ ] As regras foram comparadas com as fontes legais aplicaveis.
- [ ] Correcoes foram feitas somente nos arquivos OKF correspondentes.
- [ ] Duvidas e achados foram registrados.
- [ ] Os artefatos derivados foram regenerados com `uv run python scripts/gerar_indices.py`.
- [ ] Validadores e testes foram executados antes do commit.

Os ciclos são temáticos e não são partições cegas. Cada regra tem um único ciclo proprietário, no qual é completamente avaliada. Outros ciclos podem declará-la em `referencias` quando o cotejo transversal exigir, sem repetir a avaliação inteira. O primeiro instituto foi dividido em três marcos históricos para manter cada cotejo manejável.
