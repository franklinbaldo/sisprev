---
type: Analise
id: auditoria-juridica-ciclo-09
nome: Auditoria jurídica das propostas do Ciclo 9
data: 2026-08-07
---

# Auditoria jurídica — Ciclo 9

**Estado:** Fase 2 em execução; 24 unidades estão em
`estado_auditoria: concluida` e 1 permanece em `elaboracao`. Este documento
registra o cotejo acumulado desta rodada e não registra validação da PGE, aprovação
do IPERON, assinatura, decisão institucional ou ativação.

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
- LCE 1/1984, LCE 39/1990, LCE 68/1992, LCE 228/2000, LCE 432/2008 e LCE
  1.100/2021: róis temporalmente aplicáveis transcritos em
  `okf/dispositivos/`, com as publicações integrais preservadas em
  `fontes-oficiais/`. A transcrição integral pesquisável das digitalizações é
  evidência; os dispositivos vinculados foram cotejados nas páginas
  renderizadas.

## Resultado por família

### CF/88 original — sete propostas

A norma constitucional fornece a invalidez permanente, a exceção sem redução
proporcional para acidente em serviço, moléstia profissional e doença
qualificada, e o regime de revisão então previsto. A EC 20/1998 preserva o
direito já adquirido, mas não transforma a data do requerimento em limite da
janela.

A auditoria encontrou um discriminante material que a abertura ainda não
representava: a causa comum atravessava três estatutos, duas razões de
proporcionalização e uma diferença por sexo. Como identidade de fórmula define
TipoCalculo, manter uma única unidade ocultaria mudanças de base e método. A
decomposição em quatro unidades de causa comum é decisão de **modelagem**
fundada nessa diferença material, não a criação de quatro direitos pela norma.

| proposta                                              | fundamento decisivo                                                  | justificativa do cotejo                                                                                                                                                                                                                                | efeito                                                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| `invalidez-cf88-original-acidente-em-servico`         | CF/88 art. 40, I e § 4º; EC 20 art. 3º; estatutos estaduais vigentes | A causa qualificada afasta a redução proporcional. Na LCE 1/1984, a remuneração da atividade é adotada por interpretação sistemática dos arts. 94 e 154, § 2º; as LCE 39/1990 e 68/1992 trazem base expressa.                                          | correspondente; nexo, projeção e composição do enum são conferências operacionais        |
| `invalidez-cf88-original-doenca-catalogada`           | mesmos dispositivos constitucionais; róis e bases dos três estatutos | A doença precisa constar do rol aplicável à data do direito. Os três róis estão transcritos, e a ponte interpretativa da LCE 1/1984 está explícita.                                                                                                    | correspondente; cotejo do diagnóstico e projeção são operacionais                        |
| `invalidez-cf88-original-molestia-profissional`       | mesmos dispositivos constitucionais e estatutários                   | A exceção exige nexo profissional demonstrado. A classificação da causa é distinta da definição jurídica da base.                                                                                                                                      | correspondente; reconhecimento do nexo e projeção são operacionais                       |
| `invalidez-cf88-original-lce1-causa-comum`            | LCE 1/1984 arts. 86, 94 e 154, §§ 2º e 3º                            | A razão é 1/30 por ano para ambos os sexos; o ano tem 365 dias, e o resto superior a 182 dias arredonda para um ano. A base remuneratória resulta da interpretação sistemática registrada na própria fórmula.                                          | correspondente; cálculo juridicamente determinado                                        |
| `invalidez-cf88-original-lce39-masculino-causa-comum` | LCE 39/1990 arts. 132, 155, parágrafo único, e 156                   | Para homem, a razão é 1/35 por ano. O resto superior a 180 dias arredonda para um ano, e a base está expressa no art. 156.                                                                                                                             | correspondente; cálculo juridicamente determinado                                        |
| `invalidez-cf88-original-lce39-feminino-causa-comum`  | LCE 39/1990 arts. 132, 155, parágrafo único, e 156                   | Para mulher, a razão é 1/30 por ano, com a mesma conversão e base. A diferença por sexo exige TipoCalculo próprio.                                                                                                                                     | correspondente; cálculo juridicamente determinado                                        |
| `invalidez-cf88-original-lce68-causa-comum`           | LCE 68/1992 arts. 137, 235 e 236                                     | O art. 235 determina proporcionalidade e registra o parágrafo único como vetado; o art. 236 fixa a base e o art. 137 a conversão, mas nenhum dispositivo fixa o denominador. Importar 35/30 da voluntária preencheria por analogia uma lacuna do veto. | não fechado: exige manifestação jurídica específica antes do TipoCalculo e do mapeamento |

### EC 20/1998 — quatro propostas

A EC 20/1998 mantém a estrutura de invalidez permanente, com proventos
proporcionais como regra e exceção para acidente em serviço, moléstia
profissional e doença grave, contagiosa ou incurável especificada em lei. A
decomposição em quatro propostas é **modelagem**. O marco final de 30/12/2003
separa o período anterior à publicação da EC 41; a data do requerimento
posterior não elimina o direito adquirido.

Na causa comum, a janela atravessa duas formas de positivação da mesma fórmula.
De 16/12/1998 a 30/01/2000, os denominadores de 35/30 são adotados por
interpretação sistemática do art. 40, § 1º, I e III, “a”: o primeiro exige
proporcionalidade e o segundo fornece os tempos contributivos integrais na
mesma redação. A IN SEAP 5/1999, art. 5º, § 1º, confirma que o SIPEC federal
adotou essa leitura contemporaneamente, mas não vincula Rondônia. Desde
31/01/2000, a LCE 228, art. 43, parágrafo único, I, fornece diretamente 1/35 e
1/30. O art. 137 da LCE 68, que não foi alcançado pela revogação dos arts. 229 a
257, fecha a conversão anual durante toda a janela.

| proposta                               | vínculo já autorado                                                                                                       | justificativa do cotejo                                                                                                                                                                                                                                                                                                                  | efeito                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `invalidez-ec20-acidente-em-servico`   | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º                                                                        | A exceção constitucional conduz ao ramo integral; a preservação temporal exige direito implementado sob a legislação da época.                                                                                                                                                                                                           | correspondente; falta protocolo operacional do nexo                             |
| `invalidez-ec20-causa-comum`           | EC 20 art. 40, § 1º, I, III, “a”, § 3º, § 8º e art. 4º; LCE 68 art. 137; LCE 228 art. 43 e parágrafo único; EC 41 art. 3º | A regra proporcional é residual e a base vem do § 3º. A adoção sistemática de 35/30 no primeiro trecho está expressa e é corroborada, sem efeito vinculante estadual, pela IN SEAP 5/1999; a LCE 228 positiva diretamente a razão no segundo trecho. A conversão anual vem da LCE 68. O art. 3º da EC 41 preserva a concessão posterior. | correspondente; fórmula determinada; projeção e seleção permanecem operacionais |
| `invalidez-ec20-doenca-catalogada`     | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º; róis da LCE 68 e da LCE 228                                           | A integralidade depende de doença qualificada na lei aplicável, não apenas de diagnóstico nominal. As três versões do rol alcançadas pela janela estão transcritas, e o art. 3º da EC 41 preserva a concessão posterior pelos critérios anteriores.                                                                                      | correspondente; projeção e fluxo são operacionais                               |
| `invalidez-ec20-molestia-profissional` | EC 20 art. 40, § 1º, I e § 3º; § 8º; EC 41 art. 3º                                                                        | A exceção constitucional expressa inclui moléstia profissional e conduz ao ramo integral; separar a unidade é decisão de modelagem. O nexo e a projeção são conferências operacionais. O art. 3º da EC 41 preserva a concessão posterior pelos critérios anteriores.                                                                     | correspondente; nexo, projeção e seleção são operacionais                       |

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

| proposta                                               | vínculo já autorado                                                                          | justificativa do cotejo                                                                                                                                                                                                                              | efeito                                                   |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `invalidez-ec41-geral-pre-mp167-acidente-em-servico`   | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44                                                 | A causa qualificada afasta a proporcionalização; a base do primeiro segmento depende da legislação então vigente.                                                                                                                                    | correspondente com pendência de projeção                 |
| `invalidez-ec41-geral-pre-mp167-causa-comum`           | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e parágrafo único                                    | A causa comum permanece proporcional; o denominador e o tratamento de fração exigem demonstração jurídica e administrativa.                                                                                                                          | correspondente com pendência operacional e Q6            |
| `invalidez-ec41-geral-pre-mp167-doenca-catalogada`     | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44, § 1º                                           | A doença qualificada depende do rol temporal aplicável e conduz ao ramo sem proporcionalização; a redação da LCE 253 cobre toda a subfaixa.                                                                                                          | correspondente; projeção, cotejo e Q6 são operacionais   |
| `invalidez-ec41-geral-pre-mp167-molestia-profissional` | EC 41 art. 40, § 1º, I; LC 228 arts. 43 e 44                                                 | O nexo profissional é requisito da causa qualificada; o ramo não se presume pela ocupação.                                                                                                                                                           | correspondente com pendência de protocolo e Q6           |
| `invalidez-ec41-geral-acidente-em-servico`             | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LCE 432 arts. 20, § 6º, e 45     | A causa qualificada permanece integral; a média e o reajuste sem paridade decorrem da legislação do segmento, não do rótulo da regra.                                                                                                                | correspondente com pendência de projeção e Q6            |
| `invalidez-ec41-geral-doenca-catalogada`               | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; róis da LCE 228 e da LCE 432     | O rol da LCE 228 rege até 12/03/2008. Desde 13/03/2008, aplica-se o rol da LCE 432, inclusive no trecho posterior a 14/09/2021, porque o art. 4º da ECE 146 preserva a legislação vigente em sua entrada; a LCE 1.100 posterior não compõe a janela. | correspondente; fluxo, projeção e Q6 são operacionais    |
| `invalidez-ec41-geral-molestia-profissional`           | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LCE 432 arts. 20 e 45            | A causa qualificada depende do reconhecimento do nexo; a média é consequência normativa separada da decisão médica.                                                                                                                                  | correspondente com pendência de protocolo, projeção e Q6 |
| `invalidez-ec41-geral-media-lc228-causa-comum`         | EC 41 art. 40, § 1º, I; MP 167 art. 1º; Lei 10.887 art. 1º; LC 228 art. 43 e parágrafo único | A unidade representa o trecho em que a média é proporcionalizada pela fração anual. A separação do trecho é modelagem; o tratamento de fração de ano é pendência operacional testável.                                                               | correspondente com pendência operacional e Q6            |
| `invalidez-ec41-geral-causa-comum`                     | EC 41 art. 40, § 1º, I; LCE 432 arts. 17, 20, 45, §§ 9º e 10                                 | A causa comum exige exclusão probatória das qualificadas; a proporcionalidade em dias depende da fórmula composta dos dispositivos estaduais.                                                                                                        | correspondente com pendência de projeção e Q6            |

### Art. 6º-A da EC 41, na redação da EC 70 — cinco propostas

O art. 6º-A exige ingresso no serviço público até a publicação da EC 41,
aposentadoria por invalidez permanente fundada no art. 40, § 1º, I, base na
remuneração do cargo efetivo e aplicação do art. 7º da EC 41 por seu parágrafo
único. A ECE 146/2021 fixa o fecho histórico em 31/12/2024 para os requisitos,
representado como `data_direito_ate: 01/01/2025` exclusivo. A condição de
ingresso, a base e a paridade são **jurídicas**; separar as causas e os
segmentos de cálculo é **modelagem**.

| proposta                                      | vínculo já autorado                                                                                              | justificativa do cotejo                                                                                                                                                                                                                                 | efeito                                                    |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `invalidez-ec70-art-6a-acidente-em-servico`   | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 228 arts. 43, 44 e § 2º; LCE 432 art. 20, §§ 6º–8º | O art. 6º-A fornece ingresso, base e paridade. A LCE 228 enumera acidente em serviço sem defini-lo; a LCE 432 passa a defini-lo e enumera equiparações. O reconhecimento probatório do nexo não integra a fórmula.                                      | correspondente; enum, protocolo e Q6 são operacionais     |
| `invalidez-ec70-art-6a-doenca-catalogada`     | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; róis da LCE 228 e da LCE 432                           | A doença deve ser cotejada com o rol aplicável: LCE 228 até 12/03/2008 e LCE 432 desde 13/03/2008. O art. 4º preserva a legislação vigente na entrada da ECE 146, de modo que a LCE 1.100 posterior não compõe esta janela.                             | correspondente; enum, fluxo, cotejo e Q6 são operacionais |
| `invalidez-ec70-art-6a-molestia-profissional` | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 228 arts. 43, 44 e § 2º; LCE 432 art. 20           | As duas leis estaduais enumeram a moléstia profissional, mas não fornecem definição autônoma. O nexo profissional é requisito da causa e deve ser demonstrado na instrução; o art. 6º-A não transforma classificação médica em consequência automática. | correspondente; enum, protocolo e Q6 são operacionais     |
| `invalidez-ec70-art-6a-lc228-causa-comum`     | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; LC 228 art. 43 e parágrafo único                                        | A causa comum é proporcional, preservando a base do cargo efetivo e a paridade do art. 6º-A; o cálculo da fração anual exige comprovação.                                                                                                               | correspondente com pendência operacional e de projeção    |
| `invalidez-ec70-art-6a-causa-comum`           | EC 41 art. 40, § 1º, I; EC 70 art. 6º-A; ECE 146 art. 4º; LCE 432 arts. 17 e 20                                  | A causa comum exige exclusão das classes qualificadas; desde 13/03/2008 a fração em dias é consequência da legislação estadual, sem afastar a paridade.                                                                                                 | correspondente com pendência de projeção e Q6             |

As três causas qualificadas usam um TipoCalculo próprio da EC 70, sem ajuste.
Os tipos anual e diário permanecem nas duas unidades de causa comum. A mudança
da lei estadual da causa em 13/03/2008 não altera base, fórmula, resultado ou
projeção das causas qualificadas e, por isso, não cria nova unidade. Essa é uma
decisão de **modelagem**; o ramo sem proporcionalização é decisão **jurídica**.

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
- a base do trecho da LCE 1/1984 foi fechada por interpretação sistemática
  expressa, sem apresentá-la como literalidade do diploma. Permanece pendente o
  denominador da causa comum na LCE 68/1992, cujo parágrafo único do art. 235
  foi vetado. As causas qualificadas anteriores à LCE 432 no grupo do art.
  6º-A foram fechadas pelos arts. 43, 44 e 44, § 2º, da LCE 228, sem inferir
  definição de causa que o diploma não contém. A conferência específica da
  issue #146 retirou da regra geral EC 41 o rol da LCE 1.100: por ser posterior
  a 14/09/2021, ele não integra a legislação preservada pelo art. 4º. A
  correção não altera fórmula, representação nem estado da unidade.
  Nenhum desses pontos se resolve por regex, nome de arquivo ou analogia.

## Estado por unidade

A separação foi aplicada individualmente. `estado_auditoria: concluida` significa
somente que dispositivo, requisitos, fórmula e representação da unidade estão
determinados; não significa validação da PGE, aprovação do IPERON, homologação
ou ativação.

| unidade                                                | estado_auditoria | bloqueio jurídico ou de modelagem                                    | implantação                   |
| ------------------------------------------------------ | ---------------- | -------------------------------------------------------------------- | ----------------------------- |
| `invalidez-cf88-original-acidente-em-servico`          | `concluida`      | nenhum; ponte sistemática da LCE 1 está documentada                  | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-doenca-catalogada`            | `concluida`      | nenhum; rol e base de cada trecho estão determinados                 | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-molestia-profissional`        | `concluida`      | nenhum; reconhecimento do nexo é operacional                         | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-lce1-causa-comum`             | `concluida`      | nenhum; razão, conversão, base e representação determinadas          | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-lce39-masculino-causa-comum`  | `concluida`      | nenhum; razão, conversão, base e representação determinadas          | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-lce39-feminino-causa-comum`   | `concluida`      | nenhum; razão, conversão, base e representação determinadas          | `confirmada_com_ressalva`     |
| `invalidez-cf88-original-lce68-causa-comum`            | `elaboracao`     | denominador ausente após veto; TipoCalculo não pode ser completado   | `pendente_mapeamento_sisprev` |
| `invalidez-ec20-acidente-em-servico`                   | `concluida`      | nenhum bloqueio jurídico; protocolo é operacional                    | `confirmada_com_ressalva`     |
| `invalidez-ec20-causa-comum`                           | `concluida`      | nenhum; interpretação, razão, conversão e representação determinadas | `confirmada_com_ressalva`     |
| `invalidez-ec20-doenca-catalogada`                     | `concluida`      | nenhum bloqueio jurídico; projeção e cotejo são operacionais         | `confirmada_com_ressalva`     |
| `invalidez-ec20-molestia-profissional`                 | `concluida`      | nenhum bloqueio jurídico; nexo, projeção e seleção são operacionais  | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-pre-mp167-acidente-em-servico`   | `concluida`      | nenhum bloqueio jurídico; projeção é operacional                     | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-pre-mp167-causa-comum`           | `concluida`      | nenhum bloqueio jurídico; fração e seleção são operacionais          | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-pre-mp167-doenca-catalogada`     | `concluida`      | nenhum bloqueio jurídico; projeção, cotejo e Q6 são operacionais     | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-pre-mp167-molestia-profissional` | `concluida`      | nenhum bloqueio jurídico; protocolo é operacional                    | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-acidente-em-servico`             | `concluida`      | nenhum bloqueio jurídico; projeção e causa são operacionais          | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-causa-comum`                     | `concluida`      | nenhum bloqueio jurídico; projeção e classificação são operacionais  | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-doenca-catalogada`               | `concluida`      | nenhum bloqueio jurídico; fluxo, projeção e Q6 são operacionais      | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-media-lc228-causa-comum`         | `concluida`      | nenhum bloqueio jurídico; fração e seleção são operacionais          | `confirmada_com_ressalva`     |
| `invalidez-ec41-geral-molestia-profissional`           | `concluida`      | nenhum bloqueio jurídico; protocolo e projeção são operacionais      | `confirmada_com_ressalva`     |
| `invalidez-ec70-art-6a-acidente-em-servico`            | `concluida`      | nenhum; enum e protocolo de nexo são operacionais                    | `confirmada_com_ressalva`     |
| `invalidez-ec70-art-6a-causa-comum`                    | `concluida`      | nenhum bloqueio jurídico; projeção e seleção são operacionais        | `confirmada_com_ressalva`     |
| `invalidez-ec70-art-6a-doenca-catalogada`              | `concluida`      | nenhum; fluxo e cotejo do rol aplicável são operacionais             | `confirmada_com_ressalva`     |
| `invalidez-ec70-art-6a-lc228-causa-comum`              | `concluida`      | nenhum bloqueio jurídico; fração e projeção são operacionais         | `confirmada_com_ressalva`     |
| `invalidez-ec70-art-6a-molestia-profissional`          | `concluida`      | nenhum; reconhecimento do nexo é operacional                         | `confirmada_com_ressalva`     |

As propostas com pendência operacional conhecida agora registram
`estado_implantacao: confirmada_com_ressalva` e a ressalva específica no
frontmatter. Não há confirmação implícita sem reservas.

## Situação da auditoria

A auditoria não acopla os dois eixos. As unidades sem bloqueio jurídico ou de
modelagem foram promovidas a `estado_auditoria: concluida`, sem qualquer ato
institucional. Permanecem em `elaboracao` somente as unidades cujo próprio
fundamento, fonte normativa, fórmula ou atomicidade ainda não está determinado.

As pendências operacionais — origem do enum, protocolo de seleção, tratamento
administrativo da fração e confirmação prática da projeção — estão registradas
no eixo de implantação. Elas não impedem, por si sós, a conclusão jurídica e
não autorizam ativação.

O estado de implantação é independente e agora está explícito como
`confirmada_com_ressalva` onde há dúvida conhecida. Nenhuma dessas marcações
equivale a validação da PGE, aprovação do IPERON, homologação ou ativação.
