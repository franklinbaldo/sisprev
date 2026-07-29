# Processos SEI da planilha da PGE — inventário e mapeamento

- **Status**: mapeamento por texto exato concluído; 14 linhas pendentes de conferência humana

Nota: este documento mapeia uma aba da importação original que nunca entrou no
bundle. O mapeamento das 26 linhas da primeira tabela é **comparação de texto
exato**, conferível por qualquer um; o das 14 da segunda **não foi feito** — o
que está lá são candidatos ordenados por sobreposição de vocabulário, auxílio
de leitura e nada além disso. Nenhum destes números foi escrito em campo
nenhum de nenhuma regra, e a seção "O que esses números não são" explica um uso
que pareceria natural e corromperia o P7.

## O que existe

A planilha importada em `data/raw/regras-sisprev.xlsx` tem dez abas. A que
virou o catálogo é `regras-no-sisprev` (112 linhas, 30 colunas) — e ela **não
tem coluna de processo**. Os números estão em
`data/raw/xlsx/regras-processo-sei.csv`, 40 linhas, colunas `MODALIDADE`,
`FUNDAMENTAÇÃO`, `PROCESSO SEI`, `OBSERVAÇÃO GECAD`, `PGE CORREÇÃO`,
`PRESIDENCIA CORREÇÃO`.

Das 40 linhas, **25 trazem um número de processo**. `PGE CORREÇÃO` e
`PRESIDENCIA CORREÇÃO` estão inteiramente vazias nas 40 — o que quer que elas
fossem registrar, não foi registrado.

## O que a coluna é

**Um processo em que aquela regra foi aplicada a um caso real** (coordenação da
auditoria, 2026-07-29). É um exemplo de aplicação: a regra saiu do papel e
concedeu um benefício a alguém.

Isso a torna valiosa por um motivo que nenhuma outra fonte deste repositório
oferece. Todo o resto do catálogo é a regra *declarada* — o frontmatter, a
fundamentação, os dispositivos. O processo é a regra *executada*, e um caso
concreto é o único lugar onde se vê se a proporcionalidade foi calculada como o
art. 17 manda, se a fundamentação impressa no ato bate com a gravada no campo,
se a janela temporal foi aplicada como está no cadastro.

## O que esses números não são

**Não são `atos_validacao`.** A confusão é fácil de fazer — os dois são números
de processo do SEI ligados a uma regra — e o estrago seria silencioso.

`atos_validacao` (P7) é o ato institucional que **valida** a regra, e é a
condição de `status_auditoria: validada` (`estado_auditoria` exige a lista não
vazia). Preencher esses campos com processos de aplicação faria uma regra
alcançar `validada` pelo fato de ter sido *usada*, não de ter sido *aprovada*.
O gate continuaria verde, o selo apareceria no site e no relatório, e o
catálogo afirmaria uma validação que ninguém assinou.

Ter sido aplicada não é ter sido validada. Aliás é quase o contrário: uma regra
errada aplicada a um caso real é pior que uma regra errada parada, e o processo
é onde o erro se materializou.

## O mapeamento por texto exato

A `FUNDAMENTAÇÃO` da aba e o campo `fundamentacao*` da regra são, em muitas
linhas, **a mesma string**. Comparando-as normalizadas (NFKC, minúsculas, aspas
tipográficas unificadas, espaços colapsados, pontuação final descartada), 26
das 40 linhas casam exatamente com uma ou mais regras. Isso não é semelhança
nem inferência: é a mesma frase, e qualquer um confere com `grep`.

O que o resultado revela é a estrutura do desalinhamento. **Só 2 das 26 linhas
correspondem a uma única regra.** As outras 24 correspondem a grupos:

| regras por linha | linhas |
| ---------------- | ------ |
| 1                | 2      |
| 2                | 20     |
| 3                | 2      |
| 5                | 1      |
| 6                | 1      |

A partição da PGE é **mais grossa** que a do Sisprev, e é grossa exatamente
onde o Sisprev tem regras que compartilham fundamentação — os mesmos pares que
o `P1_NOME_REPETIDO` e o `P2_IGUALDADE_MATERIAL_ATIVA` já apontam. A PGE
enxerga "a regra"; o Sisprev tem duas linhas para ela, distintas em campos que
a fundamentação não menciona. É a decomposição 1:N da RFC 0004 vista do outro
lado.

| linha | modalidade                  | processo SEI          | regras (texto idêntico)                                                            | n   |
| ----- | --------------------------- | --------------------- | ---------------------------------------------------------------------------------- | --- |
| 0     | PENSÃO                      | `0016.004052/2023-81` | `regra-0012`, `regra-0013`                                                         | 2   |
| 1     | PENSÃO                      | `0016.001012/2025-49` | `regra-0014`, `regra-0015`, `regra-0016`, `regra-0017`, `regra-0018`               | 5   |
| 2     | INCAPACIDADE                | `0031.117501/2020-19` | `regra-0006`, `regra-0007`                                                         | 2   |
| 3     | INCAPACIDADE                | `0029.237532/2020-34` | `regra-0006`, `regra-0007`                                                         | 2   |
| 4     | INCAPACIDADE                | `0029.003981/2024-12` | `regra-0008`, `regra-0009`                                                         | 2   |
| 5     | INCAPACIDADE                | `0016.000495/2024-83` | `regra-0008`, `regra-0009`                                                         | 2   |
| 6     | INCAPACIDADE                | `0036.000147/2024-78` | `regra-0019`, `regra-0020`                                                         | 2   |
| 11    | REGRAS COMUNS - TRANSITÓRIA | `0052.070752/2022-46` | `regra-0101`, `regra-0102`                                                         | 2   |
| 15    | REGRAS COMUNS - TRANSITÓRIA | `—`                   | `regra-0055`, `regra-0056`                                                         | 2   |
| 16    | REGRAS COMUNS - TRANSITÓRIA | `—`                   | `regra-0043`, `regra-0044`                                                         | 2   |
| 17    | REGRAS COMUNS - TRANSITÓRIA | `—`                   | `regra-0047`, `regra-0048`                                                         | 2   |
| 18    | REGRA COMUM - PERMANENTE    | `—`                   | `regra-0035`, `regra-0036`                                                         | 2   |
| 19    | REGRA COMUM - PERMANENTE    | `—`                   | `regra-0037`, `regra-0038`                                                         | 2   |
| 21    | COMPULSÓRIA                 | `0029.000764/2023-81` | `regra-0032`                                                                       | 1   |
| 22    | ESPECIAL DE PROFESSOR       | `0029.002804/2024-19` | `regra-0103`, `regra-0104`                                                         | 2   |
| 25    | ESPECIAL DE PROFESSOR       | `—`                   | `regra-0045`, `regra-0046`                                                         | 2   |
| 26    | ESPECIAL DE PROFESSOR       | `—`                   | `regra-0049`, `regra-0050`                                                         | 2   |
| 27    | ESPECIAL DE PROFESSOR       | `—`                   | `regra-0053`, `regra-0054`                                                         | 2   |
| 28    | ESPECIAL DE PROFESSOR       | `—`                   | `regra-0057`, `regra-0058`                                                         | 2   |
| 29    | ESPECIAL DE POLICIAL        | `0033.016208/2023-68` | `regra-0082`, `regra-0083`                                                         | 2   |
| 30    | ESPECIAL DE POLICIAL        | `—`                   | `regra-0080`, `regra-0081`                                                         | 2   |
| 35    | PCD                         | `0030.069477/2022-76` | `regra-0059`, `regra-0060`, `regra-0061`, `regra-0062`, `regra-0063`, `regra-0064` | 6   |
| 36    | PCD                         | `0016.361607/2020-46` | `regra-0033`, `regra-0034`                                                         | 2   |
| 37    | AGENTES NOCIVOS             | `0016.102962/2020-85` | `regra-0065`, `regra-0066`, `regra-0067`                                           | 3   |
| 38    | AGENTES NOCIVOS             | `—`                   | `regra-0071`                                                                       | 1   |
| 39    | AGENTES NOCIVOS             | `—`                   | `regra-0068`, `regra-0069`, `regra-0070`                                           | 3   |

## O resíduo: 14 linhas para conferir à mão

Onde o texto não bate exatamente, ele às vezes não bate mesmo — a linha 13, por
exemplo, descreve "aposentadoria voluntária por idade e tempo de contribuição"
e seus melhores candidatos são regras de "aposentadoria especial de professor".
Um número alto de sobreposição de vocabulário não salva isso: as duas citam os
mesmos artigos.

Então esta tabela **não é um mapeamento**. É a lista de trabalho, com os três
candidatos mais próximos de cada linha para quem for conferir não começar do
zero. Onze das quatorze carregam um processo, e são elas que interessam.

| linha | modalidade                  | processo SEI          | candidatos (sobreposição)                                     |
| ----- | --------------------------- | --------------------- | ------------------------------------------------------------- |
| 7     | INCAPACIDADE                | `0029.059260/2023-78` | `regra-0022` (0.82), `regra-0021` (0.82), `regra-0020` (0.71) |
| 8     | INCAPACIDADE                | `—`                   | `regra-0022` (0.77), `regra-0021` (0.77), `regra-0020` (0.63) |
| 9     | INCAPACIDADE                | `—`                   | `regra-0022` (0.74), `regra-0021` (0.74), `regra-0020` (0.64) |
| 10    | REGRAS COMUNS - TRANSITÓRIA | `0029.038969/2024-11` | `regra-0106` (1.00), `regra-0105` (1.00), `regra-0102` (0.81) |
| 12    | REGRAS COMUNS - TRANSITÓRIA | `—`                   | `regra-0102` (1.00), `regra-0101` (1.00), `regra-0092` (0.83) |
| 13    | REGRAS COMUNS - TRANSITÓRIA | `0029.147346/2021-95` | `regra-0040` (0.60), `regra-0039` (0.60), `regra-0038` (0.50) |
| 14    | REGRAS COMUNS - TRANSITÓRIA | `0049.013838/2023-10` | `regra-0052` (1.00), `regra-0051` (1.00), `regra-0056` (0.93) |
| 20    | COMPULSÓRIA                 | `0036.068361/2022-60` | `regra-0031` (1.00), `regra-0030` (1.00), `regra-0032` (0.64) |
| 23    | ESPECIAL DE PROFESSOR       | `0029.029014/2024-72` | `regra-0108` (0.97), `regra-0107` (0.97), `regra-0042` (0.97) |
| 24    | ESPECIAL DE PROFESSOR       | `0029.021481/2025-35` | `regra-0040` (0.76), `regra-0039` (0.76), `regra-0104` (0.67) |
| 31    | ESPECIAL DE POLICIAL        | `0019.040757/2024-12` | `regra-0110` (0.97), `regra-0109` (0.97), `regra-0112` (0.92) |
| 32    | ESPECIAL DE POLICIAL        | `0033.087286/2022-66` | `regra-0112` (0.97), `regra-0111` (0.97), `regra-0077` (0.97) |
| 33    | ESPECIAL DE POLICIAL        | `0019.083472/2022-12` | `regra-0079` (0.97), `regra-0078` (0.97), `regra-0112` (0.89) |
| 34    | ESPECIAL DE POLICIAL        | `0019.376374/2020-56` | `regra-0079` (0.97), `regra-0078` (0.97), `regra-0112` (0.89) |

## O que vem depois

A coordenação pretende trazer os **pareceres** desses processos para o
repositório, com limpeza de PII. Isso muda o peso deste mapeamento: hoje ele é
um índice de casos; depois, é a espinha de um corpus de pareceres, e cada linha
resolvida passa a ligar uma regra ao texto de quem a analisou.

Três decisões ficam pendentes, e nenhuma é do auditor:

- **onde o vínculo mora.** Não é `atos_validacao`, a relação é N:N (uma linha
  aponta para até seis regras) e o parecer é um documento, não um campo — o que
  sugere um tipo próprio, não uma chave no frontmatter da regra;
- **o que sobra depois da limpeza de PII.** Um parecer sem nome, sem matrícula
  e sem número de benefício ainda é referenciado por um número de processo que
  reidentifica quem o consultar no SEI. Se o número entra no repositório
  público, isso precisa ser uma escolha feita, não um efeito colateral;
- **se e como entra no relatório da PGE.** Um caso concreto seria contexto
  forte para o procurador, mas citar um processo de terceiro num documento sobre
  regras é decisão institucional, e um caso único pode sugerir um respaldo que
  ele não dá.

## Inventário integral da aba

Transcrição das 40 linhas como importadas, para que a tabela acima possa ser
conferida contra a fonte sem abrir a planilha.

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

Duas, ambas sem número de processo na mesma linha:

- `verificar se o sistema consegue adaptar aos itens da alínea "c"`
- `Parecer 1271, item IV, a`

A segunda é a única menção a um **parecer** em toda a aba — e a única coisa
nela que se aproxima de um `atos_validacao` no sentido do P7. Ainda assim não
serve como um: falta a autoridade, falta a data e falta o processo em que foi
exarado.
