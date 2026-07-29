# Processos SEI da planilha da PGE — inventário congelado

- **Status**: inventário, nenhum vínculo autorado

Nota: este documento **inventaria** uma coluna da importação original que
nunca entrou no bundle. Ele não conclui nada sobre nenhuma regra e não
autoriza ninguém a preencher `atos_validacao` a partir dele — a razão está
em "Por que nada foi vinculado", abaixo.

## O que existe

A planilha importada em `data/raw/regras-sisprev.xlsx` tem mais de uma aba. A
que virou o catálogo é `regras-no-sisprev` (112 linhas, 30 colunas) — e ela
**não tem coluna de processo**. Os números de processo estão numa aba
separada, `data/raw/xlsx/regras-processo-sei.csv`, com 40 linhas e as colunas:

`MODALIDADE`, `FUNDAMENTAÇÃO`, `PROCESSO SEI`, `OBSERVAÇÃO GECAD`,
`PGE CORREÇÃO`, `PRESIDENCIA CORREÇÃO`.

Das 40 linhas, **25 trazem um número de processo**. `PGE CORREÇÃO` e
`PRESIDENCIA CORREÇÃO` estão **inteiramente vazias** nas 40 — o que quer que
essas duas colunas fossem registrar, não foi registrado. `OBSERVAÇÃO GECAD`
tem duas entradas, transcritas ao fim.

## Por que nada foi vinculado

A aba endereça por **modalidade + texto de fundamentação**, não por regra. São
40 linhas para 112 regras, e uma modalidade como `INCAPACIDADE` cobre oito
linhas cujos textos de fundamentação diferem entre si. Descobrir a que
`regra-NNNN` cada processo corresponde é comparar prosa jurídica com prosa
jurídica.

Isso é exatamente o que a RFC 0008 proíbe derivar mecanicamente, e pelo mesmo
motivo: o leitor de citações por regex era cuidadoso e ainda assim produziu
nove misattributions. Aqui o erro seria pior que uma citação errada — seria
**um número de processo errado impresso num documento que vai ser juntado a um
processo**. Um procurador que lesse "SEI 0029.003981/2024-12" no capítulo de
uma regra concluiria que aquela regra já foi tratada naqueles autos.

Então o vínculo é autoral, uma linha por vez: quem confere lê a fundamentação
da linha, acha a regra correspondente e escreve o `atos_validacao` naquele
`regra-*.md`. O relatório já imprime a seção "Atos de validação registrados"
em todo capítulo que tiver o campo preenchido — hoje, nenhum.

Há também uma pergunta anterior a essa, e ela é de quem conhece o fluxo, não
do auditor: **o que esses processos são**. A coluna diz só "PROCESSO SEI".
Podem ser os autos em que a modalidade foi analisada, o pedido que a originou,
ou o processo de um requerimento concreto que a usou. `AtoValidacao` exige
`tipo` e `autoridade`, e nenhum dos dois se lê da planilha. É a Q12 da RFC
0001, ainda em aberto.

## Inventário

| modalidade                  | processo SEI        | fundamentação (início)                                                                                                                                  |
| --------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PENSÃO                      | 0016.004052/2023-81 | pensão mensal, com fundamento nos artigos 10, I; 28, I; 30, II; 31, §§ 1º e 2º; 32, I e II, “a”, e § 1º; 33; 34, I a III, e § 2º; 38; e 62 da Lei Comp… |
| PENSÃO                      | 0016.001012/2025-49 | pensão mensal, com fundamento nos artigos 27, inciso I; 46, inciso I; 47, inciso I e II; 49; 50; 51, inciso I, II, III e VIII, alínea "c", todos da Le… |
| INCAPACIDADE                | 0031.117501/2020-19 | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Const… |
| INCAPACIDADE                | 0029.237532/2020-34 | aposentadoria por incapacidade permanente, com proventos proporcionais ao tempo de contribuição e sem paridade, com base no artigo 40, § 1º, inciso I,… |
| INCAPACIDADE                | 0029.003981/2024-12 | aposentadoria por incapacidade permanente, com proventos proporcionais, calculados com base na última remuneração e com paridade, com fundamento no ar… |
| INCAPACIDADE                | 0016.000495/2024-83 | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III… |
| INCAPACIDADE                | 0036.000147/2024-78 | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1º, inciso I, … |
| INCAPACIDADE                | 0029.059260/2023-78 | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Const… |
| INCAPACIDADE                | —                   | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Const… |
| INCAPACIDADE                | —                   | aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Const… |
| REGRAS COMUNS - TRANSITÓRIA | 0029.038969/2024-11 | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 3º … |
| REGRAS COMUNS - TRANSITÓRIA | 0052.070752/2022-46 | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40,… |
| REGRAS COMUNS - TRANSITÓRIA | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40,… |
| REGRAS COMUNS - TRANSITÓRIA | 0029.147346/2021-95 | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, §1º, in… |
| REGRAS COMUNS - TRANSITÓRIA | 0049.013838/2023-10 | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 5º,… |
| REGRAS COMUNS - TRANSITÓRIA | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 5º, § 6º, I… |
| REGRAS COMUNS - TRANSITÓRIA | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º,… |
| REGRAS COMUNS - TRANSITÓRIA | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 6º, § 2º, I… |
| REGRA COMUM - PERMANENTE    | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40,… |
| REGRA COMUM - PERMANENTE    | —                   | aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1°, i… |
| COMPULSÓRIA                 | 0036.068361/2022-60 | aposentadoria compulsória, com proventos proporcionais ao tempo de contribuição, com base na média aritmética simples, e sem paridade, com base no art… |
| COMPULSÓRIA                 | 0029.000764/2023-81 | aposentadoria compulsória, com proventos proporcionais ao tempo de contribuição (média aritmética simples) e sem paridade, com base no artigo 40, § 1º… |
| ESPECIAL DE PROFESSOR       | 0029.002804/2024-19 | aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º da Emenda Constituciona… |
| ESPECIAL DE PROFESSOR       | 0029.029014/2024-72 | aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 5°, da Constituição … |
| ESPECIAL DE PROFESSOR       | 0029.021481/2025-35 | aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso III, alínea “a”, … |
| ESPECIAL DE PROFESSOR       | —                   | aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º, §§ 1° e 2°, inciso I, … |
| ESPECIAL DE PROFESSOR       | —                   | aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 6º, §§ 1° e 2°, inciso II, e § 3º,… |
| ESPECIAL DE PROFESSOR       | —                   | aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 5º, §§ 4° e 6°, inciso I, … |
| ESPECIAL DE PROFESSOR       | —                   | aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 5º, §§ 4° e 6°, inciso II, e § 7º,… |
| ESPECIAL DE POLICIAL        | 0033.016208/2023-68 | aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, §1°, inciso III, segund… |
| ESPECIAL DE POLICIAL        | —                   | aposentadoria especial de policial, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, §1°, inciso III, segunda parte,… |
| ESPECIAL DE POLICIAL        | 0019.040757/2024-12 | aposentadoria especial de policial, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constituci… |
| ESPECIAL DE POLICIAL        | 0033.087286/2022-66 | aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Co… |
| ESPECIAL DE POLICIAL        | 0019.083472/2022-12 | aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda Constitu… |
| ESPECIAL DE POLICIAL        | 0019.376374/2020-56 | aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda Constitu… |
| PCD                         | 0030.069477/2022-76 | aposentadoria voluntária de servidor com deficiência, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 4º-… |
| PCD                         | 0016.361607/2020-46 | aposentadoria voluntária de servidor com deficiência, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 4º-A, da Co… |
| AGENTES NOCIVOS             | 0016.102962/2020-85 | aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por integralidade) e com paridade, com base n… |
| AGENTES NOCIVOS             | —                   | aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por média) e sem paridade, com base nos artig… |
| AGENTES NOCIVOS             | —                   | aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por média) e sem paridade, com base no artigo… |

## Observações da GECAD

Duas, ambas sem número de processo associado na mesma linha:

- `verificar se o sistema consegue adaptar aos itens da alínea "c"`
- `Parecer 1271, item IV, a`

A segunda é a única menção a um **parecer** em toda a aba, e é a única linha
que se aproxima de um ato no sentido do `atos_validacao` — mas sem autoridade,
sem data e sem o processo em que o parecer foi exarado.
