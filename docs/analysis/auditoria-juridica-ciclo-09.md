---
type: Analise
id: auditoria-juridica-ciclo-09
nome: Auditoria jurídica das propostas do Ciclo 9
data: 2026-08-07
---

# Auditoria jurídica — Ciclo 9

**Estado:** Fase 2 em execução; as 22 unidades permanecem em
`estado_auditoria: elaboracao`. Este documento registra a primeira rodada de
cotejo e não registra validação da PGE, aprovação do IPERON, assinatura,
decisão institucional ou ativação.

## Método

O cotejo foi feito a partir de três elementos separados:

1. o texto normativo transcrito em `okf/dispositivos/`, conferido contra as
   publicações oficiais correspondentes;
2. o fundamento que a proposta invoca em sua `taxonomias:`;
3. a consequência representada em `predicados`, `aplicabilidade_temporal` e
   `projecao`.

A referência encontrada por extração ou por correspondência textual é apenas
evidência de pesquisa. O vínculo estrutural de uma regra legada fica em
`dispositivos:`; a RegraProposta mantém seus vínculos articulados em
`taxonomias:`, conforme o contrato de `RegraProposta`. Não foi criado um
campo adicional fora da spec.

As conclusões abaixo distinguem:

- **jurídica:** o requisito, a exceção, a base, a proporcionalidade ou o
  reajuste que a norma impõe;
- **modelagem:** a decisão de separar uma família por causa, subfaixa ou
  fórmula;
- **operacional:** a prova, o fluxo administrativo e a confirmação do enum no
  Sisprev.

## Fundamentos normativos de referência

- CF/88 original, art. 40, I e § 4º:
  [texto constitucional no Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm);
- EC 20/1998, art. 40, § 1º, I, e art. 3º:
  [Emenda Constitucional nº 20/1998](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc20.htm);
- EC 41/2003, art. 40, § 1º, I, e art. 3º:
  [Emenda Constitucional nº 41/2003](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc41.htm);
- EC 70/2012, art. 6º-A e parágrafo único:
  [Emenda Constitucional nº 70/2012](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc70.htm);
- ECE 146/2021, art. 4º: transcrição oficial arquivada em
  `okf/dispositivos/ece-146-2021/art-4/original.md`, com conferência própria
  registrada em `docs/analysis/conferencia-janela-art-4-ece-146.md`;
- LC 228/2000, LCE 39/1990, LCE 68/1992 e LCE 432/2008: referências
  transcritas em `okf/dispositivos/`; a transcrição faltante ou incompleta
  continua sendo pendência jurídica, não é suprida por inferência.

## Resultado por família

### CF/88 original — quatro propostas

A norma constitucional fornece a invalidez permanente, a exceção integral para
acidente em serviço, moléstia profissional e doença qualificada, e o regime de
revisão então previsto. A EC 20/1998 preserva o direito já adquirido, mas não
transforma a data do requerimento em limite da janela. A decomposição em quatro
propostas é **modelagem**: representa três causas qualificadas e a causa comum
residual.

A base remuneratória e a fração dependem do estatuto estadual vigente quando os
requisitos foram implementados. Isso é uma conclusão jurídica sobre a lei
intertemporal; confirmar o denominador da fração e a composição operacional da
base é pendência distinta.

| proposta | vínculo já autorado | justificativa do cotejo | efeito |
|---|---|---|---|
| `invalidez-cf88-original-acidente-em-servico` | CF/88 art. 40, I; § 4º; EC 20 art. 3º; LCE 39 art. 156; LCE 68 art. 236 | O ramo integral decorre da causa qualificada e a revisão decorre do regime constitucional então vigente. A base estadual é temporalmente condicionada. | correspondente; pendem a fonte estadual anterior, a projeção e o fluxo de nexo |
| `invalidez-cf88-original-causa-comum` | mesmos dispositivos, com a fração estadual indicada na proposta | A causa comum é residual: exige exclusão documentada das causas qualificadas. A proporcionalidade não pode ser substituída por um enum sem denominador juridicamente definido. A variação entre LC 1/1984, LC 39/1990 e LC 68/1992 atravessa a unidade; a atomicidade de uma única proposta ainda não está demonstrada. | não fechado: pendência jurídica e decisão de modelagem; a implantação só será avaliada depois |
| `invalidez-cf88-original-doenca-catalogada` | CF/88 art. 40, I; § 4º; EC 20 art. 3º; legislação estadual temporal | A exceção depende de doença prevista no rol aplicável ao momento de implementação do direito; o nome da doença não substitui o cotejo com a versão do rol. | correspondente com pendência de rol e fonte estadual |
| `invalidez-cf88-original-molestia-profissional` | CF/88 art. 40, I; § 4º; EC 20 art. 3º; legislação estadual temporal | A causa qualificada exige nexo profissional demonstrado. A regra de modelagem é distinta da causa comum, mas o reconhecimento do nexo é operacional. | correspondente com pendência de fonte, cálculo e protocolo |

### EC 20/1998 — quatro propostas

A EC 20/1998 mantém a estrutura de invalidez permanente, com proventos
proporcionais como regra e exceção para acidente em serviço, moléstia
profissional e doença grave, contagiosa ou incurável especificada em lei. A
decomposição em quatro propostas é **modelagem**. O marco final de 30/12/2003
separa o período anterior à publicação da EC 41; a data do requerimento
posterior não elimina o direito adquirido.

| proposta | vínculo já autorado | justificativa do cotejo | efeito |
|---|---|---|---|
| `invalidez-ec20-acidente-em-servico` | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º | A exceção constitucional conduz ao ramo integral; a preservação temporal exige direito implementado sob a legislação da época. | correspondente; falta protocolo operacional do nexo |
| `invalidez-ec20-causa-comum` | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º | A regra proporcional é residual e depende da forma estadual de medir o tempo. O art. 3º da EC 41 preserva a concessão posterior pelos critérios anteriores. | correspondente com pendência de parâmetros e projeção |
| `invalidez-ec20-doenca-catalogada` | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º | A integralidade depende de doença qualificada na lei aplicável, não apenas de diagnóstico nominal. O art. 3º da EC 41 preserva a concessão posterior pelos critérios anteriores. | correspondente com pendência de rol, projeção e fluxo |
| `invalidez-ec20-molestia-profissional` | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º | A exceção depende de moléstia profissional e nexo reconhecido; separar a unidade é decisão de modelagem. O art. 3º da EC 41 preserva a concessão posterior pelos critérios anteriores. | correspondente com pendência de fonte estadual, projeção e fluxo |

### EC 41 — regra geral — nove propostas

A EC 41/2003 dá a regra constitucional de invalidez permanente; a composição
da base e da proporcionalidade passa pelas normas posteriores e pela legislação
estadual aplicável. A divisão em três causas qualificadas e causa comum, além
das três subfaixas de cálculo, é **modelagem**. As subfaixas são:

- 31/12/2003 a 19/02/2004;
- 20/02/2004 a 12/03/2008;
- desde 13/03/2008 até 31/12/2024, antes do fecho exclusivo de 01/01/2025.

As datas do direito são conclusão jurídica sobre implementação dos requisitos;
a comprovação do tratamento administrativo da fração é operacional.

| proposta | vínculo já autorado | justificativa do cotejo | efeito |
|---|---|---|---|
| `invalidez-ec41-geral-pre-mp167-acidente-em-servico` | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44 | A causa qualificada afasta a proporcionalização; a base do primeiro segmento depende da legislação então vigente. | correspondente com pendência de projeção |
| `invalidez-ec41-geral-pre-mp167-causa-comum` | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e parágrafo único | A causa comum permanece proporcional; o denominador e o tratamento de fração exigem demonstração jurídica e administrativa. | correspondente com pendência operacional e Q6 |
| `invalidez-ec41-geral-pre-mp167-doenca-catalogada` | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44 | A doença qualificada depende do rol temporal aplicável e conduz ao ramo sem proporcionalização. | correspondente com pendência do rol completo e Q6 |
| `invalidez-ec41-geral-pre-mp167-molestia-profissional` | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44 | O nexo profissional é requisito da causa qualificada; o ramo não se presume pela ocupação. | correspondente com pendência de protocolo e Q6 |
| `invalidez-ec41-geral-acidente-em-servico` | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LCE 432 arts. 20, § 6º, e 45 | A causa qualificada permanece integral; a média e o reajuste sem paridade decorrem da legislação do segmento, não do rótulo da regra. | correspondente com pendência de projeção e Q6 |
| `invalidez-ec41-geral-doenca-catalogada` | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LCE 432 arts. 20, § 9º, e 45 | O enquadramento depende da versão do rol, e o ramo integral não autoriza inventar a taxonomia ausente. | correspondente com pendência de rol, fluxo e Q6 |
| `invalidez-ec41-geral-molestia-profissional` | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LCE 432 arts. 20 e 45 | A causa qualificada depende do reconhecimento do nexo; a média é consequência normativa separada da decisão médica. | correspondente com pendência de protocolo, projeção e Q6 |
| `invalidez-ec41-geral-media-lc228-causa-comum` | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LC 228 art. 43 e parágrafo único | A unidade representa o trecho em que a média é proporcionalizada pela fração anual. A separação do trecho é modelagem; o tratamento de fração de ano é pendência operacional testável. | correspondente com pendência operacional e Q6 |
| `invalidez-ec41-geral-causa-comum` | EC 41 art. 40, § 1º, I; LCE 432 arts. 17, 20, 45, §§ 9º e 10 | A causa comum exige exclusão probatória das qualificadas; a proporcionalidade em dias depende da fórmula composta dos dispositivos estaduais. | correspondente com pendência de projeção e Q6 |

### Art. 6º-A da EC 41, na redação da EC 70 — cinco propostas

O art. 6º-A exige ingresso no serviço público até a publicação da EC 41,
aposentadoria por invalidez permanente fundada no art. 40, § 1º, I, base na
remuneração do cargo efetivo e aplicação do art. 7º da EC 41 por seu parágrafo
único. A ECE 146/2021 fixa o fecho histórico em 31/12/2024 para os requisitos,
representado como `data_direito_ate: 01/01/2025` exclusivo. A condição de
ingresso, a base e a paridade são **jurídicas**; separar as causas e os
segmentos de cálculo é **modelagem**.

| proposta | vínculo já autorado | justificativa do cotejo | efeito |
|---|---|---|---|
| `invalidez-ec70-art-6a-acidente-em-servico` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 432 art. 20, § 6º | O art. 6º-A fornece ingresso, base e paridade; a causa qualificada elimina a proporcionalização segundo a lei aplicável. | correspondente com pendência de base, fonte estadual e Q6 |
| `invalidez-ec70-art-6a-doenca-catalogada` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 432 art. 20, § 9º | A doença deve ser cotejada com o rol vigente na data do direito; a paridade vem do parágrafo único do art. 6º-A e do art. 7º da EC 41. | correspondente com pendência de rol, base, fluxo e Q6 |
| `invalidez-ec70-art-6a-molestia-profissional` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 432 art. 20 | O nexo profissional é requisito da exceção; o art. 6º-A não transforma a classificação médica em consequência automática. | correspondente com pendência de fonte, base, protocolo e Q6 |
| `invalidez-ec70-art-6a-lc228-causa-comum` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; LC 228 art. 43 e parágrafo único | A causa comum é proporcional, preservando a base do cargo efetivo e a paridade do art. 6º-A; o cálculo da fração anual exige comprovação. | correspondente com pendência operacional e de projeção |
| `invalidez-ec70-art-6a-causa-comum` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 432 arts. 17 e 20 | A causa comum exige exclusão das classes qualificadas; desde 13/03/2008 a fração em dias é consequência da legislação estadual, sem afastar a paridade. | correspondente com pendência de projeção e Q6 |

## Vínculos estruturais e achados

Os vínculos estruturais existentes nas sete origens do ciclo foram conferidos
contra as referências normativas do catálogo. A presença de um caminho em
`dispositivos:` registra a fonte invocada pelo cadastro; não transforma uma
citação errada em fundamento jurídico correto.

A conferência encontrou, e mantém documentados para decisão própria, os
seguintes pontos:

- o achado `achado-0049` registra a citação incompatível nas regras `0006`–`0009`.
  Nas `0008`–`0009`, o próprio art. 6º-A exige fundamento no inciso I do § 1º do
  art. 40. Nas `0006`–`0007`, a incompatibilidade decorre do enquadramento da
  aposentadoria por incapacidade no inciso I, sem participação do art. 6º-A.
  O vínculo existente é evidência da citação do cadastro, não validação dela;
- a divergência entre os campos proporcional e integral dessas origens exige
  decisão **jurídica** sobre o fundamento invocado e, quando houver mais de uma
  representação possível, decisão de modelagem sobre a forma de registrá-la;
  ela não deve ser corrigida automaticamente;
- a taxonomia das propostas usa os dispositivos que efetivamente sustentam as
  famílias históricas e não copia essa citação incompatível como fundamento do
  art. 6º-A;
- os dispositivos estaduais faltantes ou transcritos apenas parcialmente
  permanecem pendência jurídica. Não são preenchidos por regex, nome de arquivo
  ou analogia.

## Situação da auditoria

A auditoria não acopla os dois eixos. Uma pendência operacional — por exemplo,
origem do enum, protocolo de seleção ou tratamento administrativo da fração —
não impede, por si só, a promoção de `estado_auditoria`. Ela deve ser registrada
como pendência de implantação, com `confirmada_com_ressalva` quando houver base
suficiente para a homologação, ou como `pendente_mapeamento_sisprev` quando nem
sequer houver hipótese operacional testável.

Nesta rodada, a promoção jurídica ainda não está autorizada para as unidades
abaixo porque permanecem pendências especificamente jurídicas ou de modelagem:

- CF/88 original: fonte estadual da base e da fração, e atomicidade da proposta
  de causa comum, que atravessa fórmulas e denominadores distintos;
- EC 20/1998: rol e legislação estadual temporalmente aplicáveis;
- EC 41: conteúdo normativo das bases e frações históricas e versão dos rols;
- art. 6º-A: fontes estaduais, rol e delimitação jurídica da causa comum.

As pendências de protocolo, origem do enum e tratamento administrativo foram
separadas no relatório como operacionais ou externas. Elas não são usadas como
bloqueio jurídico automático. Quando as pendências jurídicas estiverem fechadas,
o eixo de implantação será conferido independentemente, sem promover qualquer
ato institucional ou ativação.

O estado de implantação continua independente e presumido `confirmada` onde
ausente; isso não promove a auditoria nem autoriza carga pronta para ativação.
