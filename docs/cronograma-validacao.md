# Cronograma temático de validação das regras

Objetivo: validar cada unidade juridica em um ciclo manejavel, agrupando regras relacionadas mesmo quando isso produz ciclos de tamanhos diferentes. A ordem prioriza familias juridicas e marcos normativos: incapacidade, pensao, idade, deficiencia, agentes nocivos, voluntarias gerais, magisterio e policial, e fecha com as janelas historicas de invalidez. A norma sob a qual se pode requerer o beneficio hoje vem primeiro; o que so alcanca direito adquirido vem por ultimo. Inicio sugerido: **01/08/2026**.

Cada regra deve ser revisada no arquivo `okf/regras-sisprev/regras/regra-NNNN.md`. Registre correcoes, duvidas e achados no proprio arquivo ou na unidade auditada correspondente.

## Lotes

| Dia |    Data    | Regras                                                                                                                   | Grupo predominante                        | Concluido |
| --: | :--------: | :----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- | :-------: |
|   1 | 01/08/2026 | 0019–0022                                                                                                                | incapacidade permanente na norma em vigor |    [x]    |
|   2 | 02/08/2026 | 0003, 0005, 0010–0018                                                                                                    | pensão por morte                          |    [ ]    |
|   3 | 03/08/2026 | 0023–0034                                                                                                                | compulsória e idade                       |    [ ]    |
|   4 | 04/08/2026 | 0035–0038, 0043–0044, 0047–0048, 0051–0052, 0055–0056, 0085–0087, 0089, 0091, 0093–0094, 0097–0098, 0101–0102, 0105–0106 | voluntária geral e transições             |    [ ]    |
|   5 | 05/08/2026 | 0059–0064                                                                                                                | pessoa com deficiência                    |    [ ]    |
|   6 | 06/08/2026 | 0065–0071                                                                                                                | agentes nocivos                           |    [ ]    |
|   7 | 07/08/2026 | 0039–0042, 0045–0046, 0049–0050, 0053–0054, 0057–0058, 0088, 0090, 0092, 0095–0096, 0099–0100, 0103–0104, 0107–0108      | magistério                                |    [ ]    |
|   8 | 08/08/2026 | 0072–0084, 0109–0112                                                                                                     | policial                                  |    [ ]    |
|   9 | 09/08/2026 | 0001–0002, 0004, 0006–0009                                                                                               | janelas históricas de invalidez           |    [ ]    |

## Ciclos temáticos e relatório no próprio concept

Cada linha do cronograma é um ciclo operacional. O arquivo
`okf/regras-sisprev/ciclos/ciclo-NN.md` é a fonte única do ciclo:

- o frontmatter registra identidade, data, regras proprietárias e referências;
- o corpo contém o dossiê temático e o relatório preenchível da validação.

Não há relatório irmão em `docs/relatorio/ciclos/` nem modelo externo a manter em
sincronia. O campo histórico `ciclo_de_validacao` da CSV inicial continua apenas
como metadado da regra e não define estes ciclos temáticos.

O entregável de cada ciclo é o próprio
`okf/regras-sisprev/ciclos/ciclo-NN.md`.

O corpo de cada ciclo deve registrar: regras conferidas, correções, regras sem
correção, pendências abertas, achados, fontes legais, data, commit de origem,
responsável e checklist de encerramento.

## Criterio de encerramento diario

- [ ] As regras foram comparadas com as fontes legais aplicaveis.
- [ ] Correcoes foram feitas somente nos arquivos OKF correspondentes.
- [ ] Duvidas e achados foram registrados.
- [ ] Os artefatos derivados foram regenerados com `uv run scripts/gerar_indices.py`.
- [ ] Validadores e testes foram executados antes do commit.

Os ciclos são temáticos e não são partições cegas. Cada regra tem um único ciclo proprietário, no qual é completamente avaliada. Outros ciclos podem declará-la em `referencias` quando o cotejo transversal exigir, sem repetir a avaliação inteira. O primeiro instituto foi dividido em três marcos históricos para manter cada cotejo manejável.
