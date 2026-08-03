# RFC 0014 — Como preencher o campo `FUNDAMENTACAO*`: três partes, em prosa, para o documento de concessão

- **Status**: proposta (2026-08-03). **Regra de autoria, não de geração.** Não cria campo, não cria gate, não altera o schema do Sisprev. Fixa o que o texto de fundamentação deve conter, em que ordem e em que tempo verbal, e para quem ele é escrito.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P3/P13.1), [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (papel do `nome`), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) (`requisitos_verificacao_humana`, papéis de projeção), [RFC 0008](0008-remocao-do-leitor-de-citacoes.md) (a fundamentação é articulação, não lista) e a spec da regra ([`docs/spec/regra.md`](../spec/regra.md)).
- **Alcança os Achados**: [`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md) (integral sem fundamentação proporcional), [`achado-0020`](../../okf/regras-sisprev/achados/achado-0020.md) (ausência de padrão), [`achado-0059`](../../okf/regras-sisprev/achados/achado-0059.md) (fundamentação que contradiz os campos).

______________________________________________________________________

## 0. Resumo

O campo de fundamentação passa a ter **destinatário declarado**: ele é o texto que preenche o campo correspondente no modelo que gera o **documento de concessão do benefício**. Tudo o mais decorre disso.

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

Quando o ramo é **residual** — definido pela ausência de hipóteses qualificadas —, a demonstração **negativa** é requisito e entra no texto como tal, com a ressalva de que silêncio ou prova insuficiente não bastam para o enquadramento.

### 2.2 De onde os requisitos se extraem

A articulação. Não a lista dos dispositivos citados, mas **o que cada um funda**: qual requisito ou qual efeito se retira de qual provisão, e como eles se combinam para que a hipótese fique completa.

Esta é a parte que a RFC 0008 §5 descreveu e deixou em prosa por não ter schema — a relação `critério → dispositivo`. Ela continua em prosa, e esta RFC apenas fixa que **ela é obrigatória** e que tem lugar próprio no texto.

Quando um único dispositivo funda toda a hipótese, dizer isso é a articulação: *"sem que outra norma precise ser invocada para completar a hipótese"* é afirmação verificável e útil a quem confere.

### 2.3 Qual o cálculo resultante e o seu fundamento

O modo de apuração dos proventos **descrito por extenso** — sobre que valor incide, que ajustes sofre, que limitadores se aplicam, e qual o regime de reajuste —, seguido do dispositivo que o determina.

**Não se escreve o rótulo do enum.** `Valor Efetivo` é o nome que o Sisprev dá à coluna; o documento de concessão descreve o cálculo. Escrever "pela totalidade da remuneração do cargo efetivo, sem redução proporcional ao tempo de contribuição" é o que informa o servidor; escrever `Valor Efetivo` não é.

Quando a projeção no enum é **parcial** — e ela quase sempre é (P16) —, é esta parte que carrega o que a coluna perde. É aqui, e não numa nota, que a medida da fração ou o piso sem coluna própria ficam ditos.

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

`invalidez-cf88-original-acidente-em-servico`, em `FUNDAMENTACAO_INTEGRAL`:

> No curso do processo administrativo, ficou demonstrado que o interessado era servidor titular de cargo efetivo, que se encontra em estado de invalidez permanente e que essa invalidez decorreu de acidente em serviço, com nexo causal reconhecido; a incapacidade permanente e o nexo foram apurados por junta médica oficial e pela instrução previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente, prontuários e assentamentos funcionais, tendo sido exigidas conclusão médica de incapacidade permanente e ato ou conjunto probatório que reconhecesse o nexo com o serviço. Ficou igualmente demonstrado que o direito foi implementado antes de 16/12/1998, data em que entrou em vigor a Emenda Constitucional nº 20/1998, de modo que a concessão se rege pelo texto original do art. 40 da Constituição Federal, por direito adquirido.
>
> Todos esses requisitos se extraem do art. 40, inciso I, da Constituição Federal em seu texto original, que determina a aposentadoria do servidor por invalidez permanente e, no mesmo inciso, distingue os ramos do cálculo: reserva os proventos integrais às invalidezes decorrentes de acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável especificada em lei, e atribui proventos proporcionais nos demais casos. É desse mesmo dispositivo que se retira o requisito da permanência da invalidez, a exigência do nexo com o serviço e o efeito de integralidade aqui reconhecido, sem que outra norma precise ser invocada para completar a hipótese.
>
> Do reconhecimento do acidente em serviço resulta o cálculo dos proventos pela totalidade da remuneração do cargo efetivo em que se deu a aposentadoria, sem qualquer redução proporcional ao tempo de contribuição, e com paridade em relação aos servidores em atividade. O fundamento desse cálculo é o próprio art. 40, inciso I, da Constituição Federal em sua redação original, na parte em que qualifica como integrais os proventos das invalidezes decorrentes de acidente em serviço.

## 10. Questões que esta RFC deixa abertas

- **O modelo do documento de concessão não está no repositório.** Esta RFC declara o destinatário do texto sem conhecer o formulário que o consome. Se o modelo esperar as três partes em campos separados, ou com marcador entre elas, a decisão de mantê-las como três parágrafos de um único campo terá de ser revista.
- **O comprimento cresce muito.** O formato produz cerca de 2.000 caracteres por regra, contra a mediana de 356 do catálogo recebido. Não há limite conhecido no Sisprev para essas colunas, e isso precisa ser confirmado antes da homologação.
- **A marca de regime** — "regra permanente", "regra de transição" — aparece hoje ao fim de várias fundamentações e não tem coluna própria. Esta RFC não a inclui nas três partes nem lhe dá lugar; segue como pendência de modelagem.
