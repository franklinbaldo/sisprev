# RFC 0014 — Como preencher o campo `FUNDAMENTACAO*`: três partes, em prosa, para o documento de concessão

- **Status**: proposta (2026-08-03). **Regra de autoria, não de geração.** Não cria campo, não cria gate, não altera o schema do Sisprev. Fixa o que o texto de fundamentação deve conter, em que ordem e em que tempo verbal, e para quem ele é escrito.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P3/P13.1), [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (papel do `nome`), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) (`requisitos_verificacao_humana`, papéis de projeção), [RFC 0008](0008-remocao-do-leitor-de-citacoes.md) (a fundamentação é articulação, não lista) e a spec da regra ([`docs/spec/regra.md`](../spec/regra.md)).
- **Alcança os Achados**: [`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md) (integral sem fundamentação proporcional), [`achado-0020`](../../okf/regras-sisprev/achados/achado-0020.md) (ausência de padrão), [`achado-0059`](../../okf/regras-sisprev/achados/achado-0059.md) (fundamentação que contradiz os campos).

______________________________________________________________________

## 0. Resumo

O campo de fundamentação passa a ter uma função declarada: **transcrever em prosa tudo que a regra exige para ser aplicada e o resultado da aplicação**, para servir de texto ao modelo que gera o **documento de concessão do benefício**. Tudo o mais decorre disso.

**Isto é decisão de produto, não constatação.** Declarada por franklinbaldo em 03/08/2026, nestes termos: "é assim que o sistema funcionará; essa será a utilidade do campo". Não há, nesta data, modelo, ofício ou tela arquivada no repositório que comprove o campo sendo consumido assim — e por isso esta RFC **não supersede** a questão aberta de [`leituras-provaveis-das-questoes-abertas.md`](../analysis/leituras-provaveis-das-questoes-abertas.md) §11, que pergunta *onde os textos de fundamentação são apresentados ou consumidos*. Aquela pergunta é sobre o presente e segue sem resposta; esta RFC institui um uso futuro.

A consequência é que o formato aqui fixado é **revogável pela evidência**: se a apuração institucional mostrar que o campo é consumido de outro modo, ou por outro consumidor, o tempo verbal, o sujeito e a estrutura de três partes caem junto, porque todos derivam desta decisão.

O texto tem **três partes, nesta ordem**, todas em prosa corrida:

1. **o que ficou demonstrado** — em prosa, o conjunto dos requisitos que a parte demonstrou ter satisfeito no curso do processo, com a indicação de quem apurou e mediante que prova;
2. **de onde os requisitos se extraem** — a articulação dos dispositivos, dizendo o que cada um funda, e não uma lista de artigos;
3. **qual o cálculo resultante e o seu fundamento** — o modo de apuração dos proventos, descrito por extenso, e o dispositivo que o determina.

O tempo verbal é o **afirmativo passado** ("No curso do processo administrativo, ficou demonstrado que..."), porque o texto será lido dentro de um ato de concessão já praticado.

## 1. Por que o destinatário decide o formato

O campo tinha três leitores possíveis e nenhum declarado, e é por isso que ele tem hoje três estilos incompatíveis: da citação abreviada de 45 caracteres à célula de 1.085 com três articulações separadas por `|`.

Os três leitores pedem coisas opostas:

- o **procurador que confere** quer a articulação e considera ruído tudo que repete as colunas;
- o **operador que escolhe a regra na tela** quer o que **distingue** esta regra das vizinhas;
- o **servidor que recebe a concessão** quer um texto **autocontido**, que diga o que ele provou, com que base e o que vai receber.

Esta RFC decide pelo terceiro, e a decisão tem uma consequência de arrumação: **o segundo leitor já é atendido por outro campo.** O `nome` existe exatamente para distinguir a regra depois da anamnese (RFC 0002), e não precisa ser socorrido pela fundamentação. O primeiro leitor é atendido pela parte 2, que é obrigatória — a conferência jurídica é servida como subproduto, não como objetivo.

## 2. As três partes

### 2.1 O que ficou demonstrado

Prosa que enumera os requisitos satisfeitos. Não é lista com marcadores: é uma frase que encadeia as aferições, porque o texto vai para um documento e não para uma tela de conferência.

Deve conter, quando aplicável ao caso da regra:

- a **qualidade** do interessado (titular de cargo efetivo, dependente, e afins);
- cada **critério aferido** que a regra exige — a mesma lista que individua a regra (spec da regra, "o que individua uma regra");
- a **janela temporal** em que o direito foi implementado, quando ela é condição da regra;
- **quem apurou** cada requisito não documental, **mediante que prova** e **que evidência foi exigida**.

Quando o **predicado e o protocolo estruturados da regra exigirem** a exclusão de hipóteses qualificadas, essa demonstração negativa entra no texto como requisito, com a ressalva que a própria regra tiver modelado.

Esta RFC **não fixa ônus probatório**. Se um ramo residual opera por não se ter demonstrado a exceção, ou se exige exclusão positiva, é decisão de mérito de cada regra — declarada em `requisitos_verificacao_humana` e no `protocolo_verificacao` —, e a redação apenas transcreve o que ali estiver. Uma convenção de escrita que decidisse isso genericamente alteraria em silêncio o mérito de regras futuras.

### 2.2 De onde os requisitos se extraem

A articulação. Não a lista dos dispositivos citados, mas **o que cada um funda**: qual requisito ou qual efeito se retira de qual provisão, e como eles se combinam para que a hipótese fique completa.

Esta é a parte que a RFC 0008 §5 descreveu e deixou em prosa por não ter schema — a relação `critério → dispositivo`. Ela continua em prosa, e esta RFC apenas fixa que **ela é obrigatória** e que tem lugar próprio no texto.

**Afirmar exaustividade é a armadilha desta parte.** Escrever que "nenhuma outra norma precisa ser invocada" é afirmação forte, conferível, e falsa com facilidade: o primeiro texto autorado sob esta RFC a fez, e estava errado duas vezes — a paridade vinha do art. 40, § 4º, do texto original, não do inciso I, e a própria aplicabilidade do texto revogado dependia do art. 3º da EC 20/1998. Nenhum dos dois dispositivos existia no bundle.

Daí a regra: **um efeito gravado em coluna precisa de dispositivo que o funde**, e o teste é percorrer os campos deployáveis um a um perguntando de onde cada um vem. `PARIDADE: S` sem dispositivo de paridade articulado é o defeito, e ele não se anuncia — o texto continua legível e plausível.

A conferência tem um lado mecânico que vale usar: **todo dispositivo articulado no texto tem de estar em `taxonomias`**, e o `papel` declarado ali é a mesma afirmação que a prosa faz. Divergência entre os dois é sinal de que um dos lados não foi conferido.

### 2.3 Qual o cálculo resultante e o seu fundamento

O modo de apuração dos proventos **descrito por extenso** — sobre que valor incide, que ajustes sofre, que limitadores se aplicam, e qual o regime de reajuste —, seguido do dispositivo que o determina.

**Não se escreve o rótulo do enum.** `Valor Efetivo` é o nome que o Sisprev dá à coluna; o documento de concessão descreve o cálculo. Escrever "pela totalidade da remuneração do cargo efetivo, sem redução proporcional ao tempo de contribuição" é o que informa o servidor; escrever `Valor Efetivo` não é.

Quando a projeção no enum é **parcial** — e ela quase sempre é (P16) —, é esta parte que carrega o que a coluna perde. É aqui, e não numa nota, que a medida da fração ou o piso sem coluna própria ficam ditos.

**Pré-requisito de autoria: a regra tem de vincular uma `FormaCalculo` sem pendência aberta sobre a fórmula.** Sem ela não se escreve a fundamentação — nem a parte 3 isoladamente, nem as outras duas. A parte 3 é constitutiva: um texto que descreve os requisitos e cala sobre o resultado não é fundamentação incompleta, é outra coisa, e a função declarada em §0 inclui "o resultado da aplicação".

`TIPO_CALCULO` **não** satisfaz este pré-requisito. O rótulo do enum não descreve a fórmula sozinho — é decisão registrada do projeto (P16), e é por isso que a `FormaCalculo` existe como documento próprio, com base, ajustes e limitadores vinculados aos seus dispositivos.

Esta RFC **não define fórmula alguma**, e não é o veículo para isso: fechar a fórmula aplicável a uma janela é trabalho de mérito, autorado em `okf/formas-calculo/`.

## 3. Tempo verbal e sujeito

**Afirmativo, no passado**: *"No curso do processo administrativo, ficou demonstrado que o interessado era servidor titular de cargo efetivo..."*.

Isto é uma mudança em relação ao template projetado da RFC 0004 §6, que escreve `Aplicável quando <predicado>` justamente para não afirmar constatação de caso concreto. A razão da mudança é o destinatário: no documento de concessão o servidor **existe** e o ato **já foi praticado**; um texto condicional ali estaria fora de lugar.

A consequência tem de ser assumida com clareza: **a ficha da regra no site passa a exibir um texto que afirma fato sobre um caso que não existe.** Isso é aceitável porque o campo declara-se, desde esta RFC, como *texto-modelo do documento de concessão*, e não como descrição da regra — quem quer a descrição tem o `nome` e a análise do corpo. Onde o texto for exibido fora do documento, cabe à superfície dizer o que ele é.

O sujeito é **"o interessado"**, nunca um nome próprio nem um número de processo: o texto é molde, e a identificação vem do modelo que o consome. Isto também mantém o campo fora do alcance da questão de PII da RFC 0010 §4.3.

## 4. O que não entra

- **O rótulo do enum** (§2.3);
- **jargão do repositório**. O `momento` do `protocolo_verificacao` — "instrução e seleção da regra" — descreve onde a verificação entra no fluxo da auditoria e não tem referente para quem lê a concessão. O protocolo entra pelo **responsável**, pelo **meio de prova** e pela **evidência exigida**; o momento já está dito na abertura ("no curso do processo administrativo");
- **várias hipóteses numa célula**. O `|` que hoje separa três articulações na `regra-0022` é sintoma de uma regra que deveria ser três, e a decomposição 1:N (RFC 0004 §1.2) é o remédio. Uma fundamentação, uma hipótese;
- **referência a outras regras do catálogo**. O documento de concessão não menciona o catálogo.

## 5. Qual dos três campos recebe o texto

O sufixo segue o **ramo que a regra aplica**, não a existência dos dois ramos na lei:

- regra cujo resultado é integral escreve em `FUNDAMENTACAO_INTEGRAL` e deixa `FUNDAMENTACAO_PROPORCIONAL` vazia;
- regra cujo resultado é proporcional escreve em `FUNDAMENTACAO_PROPORCIONAL` e deixa `FUNDAMENTACAO_INTEGRAL` vazia.

Isto contraria o preenchimento observado no catálogo recebido, em que `FUNDAMENTACAO_INTEGRAL` aparece em regras de resultado proporcional — o que o `achado-0009` já registra por outro ângulo. A correspondência entre o sufixo do campo e o valor de `INTEGRAL` passa a ser exigência de autoria.

`FUNDAMENTACAO` sem sufixo permanece como está: esta RFC não lhe atribui papel, e nenhuma regra proposta o preenche.

## 6. Relação com os campos estruturados

As três partes têm insumo estruturado no repositório, e é dele que o autor parte:

| parte | insumo                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------- |
| 1     | `requisitos_verificacao_humana[]` (predicado + protocolo) e `aplicabilidade_temporal`                     |
| 2     | `taxonomias[]`, cujo `papel` é a articulação já declarada                                                 |
| 3     | a `type: FormaCalculo` vinculada, com `base`/`ajustes`/`limitadores` e os dispositivos de cada componente |

**Isto não autoriza gerar o texto.** A decisão desta RFC é que a fundamentação é **autorada**, com os campos estruturados servindo de insumo e de conferência — pela mesma razão que derrubou o leitor de citações por regex (RFC 0008): um texto montado por template produz prosa plausível cuja fidelidade ninguém conferiu, e este texto vai assinado num ato de concessão.

O caminho inverso, porém, é legítimo e desejável: **os campos estruturados servem para conferir o texto**. Um requisito que está no texto e não em `requisitos_verificacao_humana`, ou um dispositivo articulado na parte 2 e ausente de `taxonomias`, é divergência a investigar.

## 7. Coerência com as colunas, e o gate que esta RFC não cria

A parte 3 diz por extenso o que `INTEGRAL`, `PARIDADE` e `TIPO_CALCULO` gravam em código. **A redundância é deliberada** — o documento de concessão precisa ser autocontido —, e por isso ela cria a possibilidade de divergência que o `achado-0059` já encontrou à mão em quatro regras: fundamentação afirmando integralidade e paridade enquanto os campos gravavam média e sem paridade.

Esta RFC **não cria o detector** correspondente, e a omissão é escolha, não esquecimento. Um detector que lesse o texto em busca de "integral" ou "paridade" seria um leitor por padrão sobre prosa jurídica — exatamente a máquina que a RFC 0008 removeu depois de ela produzir nove atribuições erradas. A coerência entre a parte 3 e as colunas fica **conferência humana**, como a articulação da parte 2.

Se um gate vier a existir, ele deve nascer do caminho estruturado — comparar a `FormaCalculo` vinculada com `TIPO_CALCULO`, que são dois dados declarados —, nunca da leitura do texto.

## 8. Alcance

Esta RFC vale para **as regras propostas autoradas daqui em diante**. Ela **não** converte o catálogo recebido em população de achados: as 112 regras importadas seguem como estão, e o desvio de cada uma em relação a este formato já está registrado pelo `achado-0020`, que descreve a ausência de padrão sem propor um.

Quando uma regra legada for substituída, a sua sucessora nasce neste formato. É esse o mecanismo de adoção — substituição, não reescrita em massa.

## 9. Exemplo trabalhado

`invalidez-cf88-original-acidente-em-servico`, em `FUNDAMENTACAO_INTEGRAL`. A unidade proporcional do mesmo grupo, `invalidez-cf88-original-causa-comum`, **não** tem exemplo aqui: a medida da proporção na janela da CF/88 original não tem fonte identificada — a Constituição diz "proporcionais" sem denominador e a LC 228/2000 é posterior —, então não há `FormaCalculo` a vincular e a fundamentação não pode ser autorada (§2.3).

> No curso do processo administrativo, ficou demonstrado que o interessado era servidor titular de cargo efetivo, que se encontra em estado de invalidez permanente e que essa invalidez decorreu de acidente em serviço, com nexo causal reconhecido; a incapacidade permanente e o nexo foram apurados por junta médica oficial e pela instrução previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente, prontuários e assentamentos funcionais, tendo sido exigidas conclusão médica de incapacidade permanente e ato ou conjunto probatório que reconhecesse o nexo com o serviço. Ficou igualmente demonstrado que os requisitos foram integralmente cumpridos até 15/12/1998, véspera da publicação da Emenda Constitucional nº 20/1998.
>
> Esses requisitos se extraem da conjugação de três dispositivos, cada um fundando uma parte da hipótese. O art. 40, inciso I, da Constituição Federal em seu texto original determina a aposentadoria do servidor por invalidez permanente e, no mesmo inciso, distingue os ramos do cálculo: reserva os proventos integrais às invalidezes decorrentes de acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável especificada em lei, e atribui proventos proporcionais nos demais casos — dele se retiram, portanto, o requisito da permanência da invalidez, a exigência do nexo com o serviço e o efeito de integralidade. O art. 40, § 4º, do mesmo texto original assegura que os proventos serão revistos na mesma proporção e na mesma data em que se modificar a remuneração dos servidores em atividade, e é dele — e não do inciso I — que decorre a paridade. E o art. 3º da Emenda Constitucional nº 20/1998 assegura a concessão, a qualquer tempo, a quem tenha cumprido os requisitos até a data de sua publicação, pelos critérios da legislação então vigente, sendo esse o dispositivo que permite aplicar o texto original depois de sua revogação.
>
> Do reconhecimento do acidente em serviço resulta o cálculo dos proventos pela totalidade da remuneração do cargo efetivo em que se deu a aposentadoria, sem qualquer redução proporcional ao tempo de contribuição, com fundamento no art. 40, inciso I, da Constituição Federal em sua redação original, na parte em que qualifica como integrais os proventos das invalidezes decorrentes de acidente em serviço. Os proventos assim apurados são revistos na mesma proporção e na mesma data da remuneração dos servidores em atividade, na forma do art. 40, § 4º, do mesmo texto. proveniencia:

## 10. Questões que esta RFC deixa abertas

- **O modelo do documento de concessão não está no repositório.** Esta RFC declara o destinatário do texto sem conhecer o formulário que o consome. Se o modelo esperar as três partes em campos separados, ou com marcador entre elas, a decisão de mantê-las como três parágrafos de um único campo terá de ser revista.
- **O comprimento cresce muito.** O formato produz cerca de 2.000 caracteres por regra, contra a mediana de 356 do catálogo recebido. Não há limite conhecido no Sisprev para essas colunas, e isso precisa ser confirmado antes da homologação.
- **A marca de regime** — "regra permanente", "regra de transição" — aparece hoje ao fim de várias fundamentações e não tem coluna própria. Esta RFC não a inclui nas três partes nem lhe dá lugar; segue como pendência de modelagem.
