# Auditoria legal regra a regra — 30/07/2026

## Método

As regras `0001`–`0112` foram cotejadas com os dispositivos indicados em seu
frontmatter e com os textos correspondentes em `okf/dispositivos/`. A pergunta
primária foi se a lei cobre os parâmetros da regra: benefício, população,
marcos temporais, requisitos, cálculo, reajuste, sexo e prova. Planilha da PGE e
precedentes não foram usados como fundamento. Precedente só deve ser anexado
quando a lei não resolver a questão ou quando um caso concreto acrescentar uma
interpretação aplicada.

Nenhuma regra foi editada nesta rodada. Os resultados abaixo são diagnóstico
para orientar achados e decisões, não autorização automática para alterar
campos deployáveis.

## Resultado por bloco

| Regras    | Resultado do cotejo                                                                                                                                            | Pendência principal                                             |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| 0001–0002 | Base de invalidez histórica cobre integralidade/proporcionalidade por causa; paridade e base do enum não estão demonstradas.                                   | Causa, paridade e cálculo sem parâmetros suficientes.           |
| 0003–0005 | Não auditáveis integralmente: dispositivos constitucionais não estão transcritos ou há campos vazios.                                                          | Transcrever fontes antes de preencher campos.                   |
| 0006–0009 | Cadeia LCE 432/2008 cobre incapacidade, média, fração e RGPS; persistem janela até 31/12/2024, causa sem coluna e conflitos entre ramos integral/proporcional. | Achados 0022, 0025, 0026 e decisão sobre a separação dos ramos. |
| 0010      | Fórmula do art. 40, § 7º, EC 41 é reconhecível; população, paridade e extensão temporal não estão fechadas.                                                    | Instituidor aposentado versus ativo e prazo da ECE 146.         |
| 0011      | Base de pensão coerente, mas corte de ingresso, prazo e art. 4º da ECE 146 não fecham.                                                                         | Achados 0047–0048.                                              |
| 0012–0013 | Cotas e regime pós-2003 têm base legal; faltam dispositivos citados e as duas regras são materialmente idênticas.                                              | Achados 0001–0002 e cotejo item a item.                         |
| 0014–0018 | Regime de cotas da LCE 1.100 é reconhecível; prazo `01/01/2024`, duração e sexo do instituidor/beneficiário não estão resolvidos.                              | Achados 0001, 0002, 0056 e tabela do art. 46.                   |
| 0019–0020 | 0019 tem cadeia normativa relevante, mas cálculo/causa permanecem abertos; 0020 contradiz o próprio texto ao gravar proporcionalidade.                         | Achados 0009, 0024–0026 e decisão sobre os ramos.               |
| 0021–0022 | Fundamentação empacota acidente, doença grave e moléstia; 0021/0022 misturam ramo pós-2003 com arts. 25/27-I.                                                  | Decomposição por causa e transcrição dos arts. 30, §§ 13–14.    |
| 0023–0026 | Dispositivos históricos cobrem benefício e proporcionalidade, mas sexo, integralidade, paridade e enum ficam vazios ou sem fundamento.                         | Achado 0008 e preenchimento somente após decisão.               |
| 0027      | Cobertura legal substancialmente coerente: compulsória, média, fração e RGPS.                                                                                  | Marco `03/12/2015` versus `04/12/2015`.                         |
| 0028–0029 | Fundamentação cita inciso constitucional errado; sexo e prazo final não estão sustentados pelos dispositivos.                                                  | Achado 0013 e conferência da janela.                            |
| 0030–0032 | Compulsória e cálculo têm base; 0032 mistura cadeia LCE 432 com regime novo e 0030/31 não fundam sexo.                                                         | Janela, sexo e escolha da norma-base.                           |
| 0033–0034 | LCE 1.100 art. 35 cobre deficiência, sexo e média; fundamentação integral contradiz `integral: N`.                                                             | Grau, rota por idade e conflito de campos.                      |
| 0035–0038 | Arts. 24/25/27/32 cobrem os dois trilhos; requisitos não têm colunas e `Remuneração de Contribuição` não é equivalência literal demonstrada do art. 25.        | Achados 0028–0031 e semântica do enum.                          |
| 0039–0040 | Cadeia EC 20/LCE 432 não sustenta regras pós-2021; fundamentação integral contradiz campos proporcionais.                                                      | Achados 0051 e 0052; decidir norma-base.                        |
| 0041–0050 | Regras de professor/transição têm base geral coerente, mas requisitos, prova exclusiva de magistério, pontuação, sexo e vigência não estão modelados.          | Vigência da ECE 146 e requisitos sem colunas.                   |
| 0051–0058 | Arts. 5º/6º da ECE 146 sustentam os trilhos, mas caput/incisos de requisitos não estão vinculados; 0057/58 ainda contradizem `integral`.                       | Pontuação, pedágio, sexo e datas.                               |
| 0059–0064 | Arts. 35/25/27 são incompatíveis com `paridade: N` e `Valor Médio` gravados nas regras de deficiência.                                                         | Achados 0003, 0004, 0020 e 0059.                                |
| 0065–0067 | Art. 41 exige pontuação e art. 25 exige ingresso até 31/12/2003; janela e `tabelapontuacao` estão erradas, e o enum permanece inconclusivo.                    | Achados 0042, 0054, 0057.                                       |
| 0068–0070 | Regra transitória é parcialmente sustentada, mas a transcrição do art. 8º termina antes dos limiares; as três regras não têm critério jurídico diferenciador.  | Transcrever limiares e abrir achado de duplicidade.             |
| 0071      | Arts. 24/27-II/41 cobrem média e ausência de paridade; a origem tem marco de admissão invertido.                                                               | Unidade corrigida em `preview`; decisão sobre adoção.           |
| 0072–0080 | Regras policiais têm bases legais reconhecíveis, mas há alíneas sexuais empacotadas, requisitos não modelados e sexo sem apoio no art. 34.                     | Achados 0037, 0040, 0041 e data da ECE 146.                     |
| 0081–0084 | 0081–83 têm base de cálculo, mas sexo não é fundado; 0084 conflita frontalmente entre integralidade/paridade legal e média/sem paridade nos campos.            | Achados 0040 e 0084.                                            |
| 0085–0090 | Normas históricas cobrem hipóteses gerais, mas incisos não transcritos, paridade sem fundamento, campos vazios e citações erradas impedem fechamento.          | Achado 0008 e conferências históricas.                          |
| 0091–0094 | EC 20/EC 41/ECE 146 estão misturadas ou incompletas; várias janelas não intersectam a norma citada.                                                            | Achados 0044–0046 e decisão de norma-base.                      |
| 0095–0100 | Professor e transições têm conflitos entre art. 25, média, paridade e janelas; 0099/0100 não têm dispositivo que os diferencie como magistério.                | Achados 0043, 0018 e 0046.                                      |
| 0101–0106 | Transições EC 41/EC 47 têm resultado plausível, mas paridade, incisos, requisitos e vigência pós-EC 103 não estão completamente autorados.                     | Transcrever art. 2º EC 47, art. 3º e decidir referendo.         |
| 0107–0108 | Fundamentação é do ramo integral/paritário até 2003, enquanto campos são pós-2003, média e sem paridade.                                                       | Achados 0009, 0020 e 0050.                                      |
| 0109–0112 | Regras policiais misturam art. 4º da ECE 146 com art. 7º, alíneas e janelas incompatíveis; 0112 tem nome masculino em regra feminina.                          | Achados 0027, 0037, 0038 e 0041.                                |

## Conclusão operacional

O catálogo não precisa de precedente para a maioria das regras em que a lei já
fecha o regime. Os próximos trabalhos devem ser, nesta ordem:

1. transcrever os dispositivos faltantes;
2. resolver conflitos entre fundamentação e campos deployáveis;
3. decidir as janelas cuja vigência depende da ECE 146/2021 ou da EC 103/2019;
4. criar campos ou protocolo para requisitos que a lei exige mas o legado não
   representa;
5. somente então usar precedentes para as dúvidas residuais de aplicação.

Até essas decisões, a ação segura é manter as regras originais e registrar os
achados; não preencher lacunas por analogia com outra regra ou com a planilha da
PGE.
