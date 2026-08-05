# RFC 0014 — Como preencher o campo `FUNDAMENTACAO*`: três partes, em prosa, para o documento de concessão

- **Status**: adotada em 2026-08-03 para as regras propostas do Ciclo 1 e seguintes. **Regra de autoria, não de geração.** Não cria campo, não altera o schema do Sisprev e não autoriza inferir mérito jurídico por leitura automática da prosa.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P3/P13.1), [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (papel do `nome`), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) (`requisitos_verificacao_humana`, papéis de projeção), [RFC 0008](0008-remocao-do-leitor-de-citacoes.md) (a fundamentação é articulação, não lista) e a spec da regra ([`okf/spec/regra.md`](../../okf/spec/regra.md)).
- **Alcança os Achados**: [`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md), [`achado-0020`](../../okf/regras-sisprev/achados/achado-0020.md) e [`achado-0059`](../../okf/regras-sisprev/achados/achado-0059.md).

______________________________________________________________________

## 0. Decisão

O campo de fundamentação passa a ter uma função declarada: **transcrever em prosa o que a regra exige para ser aplicada, de onde esses requisitos se extraem e qual resultado jurídico decorre da aplicação**, para servir de texto ao modelo que gera o documento de concessão do benefício.

Isto é decisão de produto, não constatação sobre o uso atual do Sisprev. A questão histórica sobre onde o campo é hoje apresentado ou consumido permanece registrada em [`leituras-provaveis-das-questoes-abertas.md`](../analysis/leituras-provaveis-das-questoes-abertas.md). Esta RFC institui o uso futuro do campo no modelo auditado.

A estrutura abaixo é **obrigatória** para toda regra proposta autorada a partir desta RFC. A regra que não a observa não está pronta para validação no modelo auditado.

A adoção desta RFC substitui, para as regras propostas, o uso do template condicional `Aplicável quando <predicado>` como conteúdo final de `FUNDAMENTACAO*`.

## 1. As três partes

O texto tem três partes, nesta ordem, em prosa corrida.

### 1.1 O que ficou demonstrado

A primeira parte registra, no afirmativo passado, os requisitos satisfeitos no processo administrativo. Deve conter, quando aplicável:

- a qualidade do interessado;
- cada critério que individua a regra;
- a janela temporal relevante;
- quem apurou os requisitos não documentais;
- os meios de prova e a evidência exigida.

Quando o predicado e o protocolo estruturados exigirem a exclusão de hipóteses qualificadas, essa demonstração negativa entra no texto. Esta RFC **não fixa ônus probatório**: a redação apenas transcreve a decisão material já declarada em `requisitos_verificacao_humana` e `protocolo_verificacao`.

### 1.2 De onde os requisitos se extraem

A segunda parte articula os dispositivos: não basta enumerar artigos; é preciso dizer **o que cada dispositivo funda** e como eles se combinam.

Um efeito gravado em coluna precisa de dispositivo que o sustente. O teste de autoria é percorrer os campos deployáveis — inclusive `INTEGRAL`, `PARIDADE` e a forma de cálculo — e identificar de onde cada resultado vem.

Todo dispositivo articulado na fundamentação deve aparecer em `taxonomias`, com `papel` coerente com a afirmação feita na prosa. O direito adquirido que permite aplicar redação revogada também precisa de fundamento próprio.

### 1.3 Qual o cálculo resultante e o seu fundamento

A terceira parte identifica a **forma de cálculo aplicável**, descreve por extenso a sua estrutura jurídica conhecida e aponta os dispositivos que a definem.

A obrigação da regra é, desde já:

1. diferenciar qual forma de cálculo se aplica;
2. vincular a `TipoCalculo` correspondente em `proveniencia.fontes_consultadas`;
3. indicar os dispositivos que fundam a base, os ajustes, os limitadores e o regime de reajuste que já estiverem juridicamente identificados;
4. manter a prosa coerente com `INTEGRAL`, `PARIDADE` e `TIPO_CALCULO`.

**Não é necessário que todos os parâmetros operacionais da fórmula estejam fechados para autorar a fundamentação.** A `TipoCalculo` pode registrar componentes ou medidas ainda pendentes — por exemplo, denominador, conversão em dias ou composição concreta da base — desde que:

- a estrutura jurídica já identificada esteja correta;
- a pendência esteja declarada no documento da `TipoCalculo` e nas pendências da regra;
- a fundamentação não invente nem antecipe o parâmetro ainda não apurado.

Assim, uma regra proporcional pode afirmar que os proventos são calculados sobre determinada base com redução proporcional ao tempo, indicando o dispositivo que institui esse ramo, ainda que a medida exata da fração permaneça pendente de legislação temporalmente aplicável.

`TIPO_CALCULO` sozinho não satisfaz essa obrigação. O enum é uma projeção legada e não descreve a fórmula completa.

A paridade é tratada separadamente: ela é regime de revisão posterior e deve ser fundada no dispositivo próprio, não atribuída ao dispositivo que define apenas o cálculo inicial.

## 2. Tempo verbal e sujeito

O texto é escrito no **afirmativo passado**: “No curso do processo administrativo, ficou demonstrado que...”.

O sujeito é “o interessado”, nunca nome próprio ou número de processo. O campo é texto-modelo; a identificação concreta vem do documento que o consome.

A ficha da regra no site pode exibir esse texto fora de um caso real. A superfície deve deixar claro que se trata de modelo de fundamentação, não de constatação sobre pessoa determinada.

## 3. O que não entra

- o rótulo do enum como substituto da descrição jurídica do cálculo;
- jargão interno do repositório, como o `momento` do protocolo de verificação;
- várias hipóteses materiais na mesma célula;
- referência a outras regras do catálogo;
- fórmula ou parâmetro não sustentado pelos dispositivos e pela `TipoCalculo` vinculada.

## 4. Qual campo recebe o texto

O sufixo acompanha o ramo aplicado:

- resultado integral: `FUNDAMENTACAO_INTEGRAL` preenchida e `FUNDAMENTACAO_PROPORCIONAL` vazia;
- resultado proporcional: `FUNDAMENTACAO_PROPORCIONAL` preenchida e `FUNDAMENTACAO_INTEGRAL` vazia.

`FUNDAMENTACAO` sem sufixo permanece sem papel atribuído nesta RFC.

## 5. Relação com os campos estruturados

| parte | insumo                                                        |
| ----- | ------------------------------------------------------------- |
| 1     | `requisitos_verificacao_humana[]` e `aplicabilidade_temporal` |
| 2     | `taxonomias[]`, com a relação `critério/efeito → dispositivo` |
| 3     | `TipoCalculo`, projeção e dispositivos de seus componentes    |

O texto é autorado, nunca gerado automaticamente. Os dados estruturados servem de insumo e de conferência.

O caminho inverso é obrigatório como revisão humana: requisito, efeito ou dispositivo presente na prosa e ausente do estruturado é divergência a investigar.

## 6. Coerência e automação

A parte 3 repete por extenso resultados que também aparecem em colunas estruturadas. A redundância é deliberada porque o documento precisa ser autocontido.

Esta RFC não cria leitor de prosa por palavras-chave. Se houver gate, ele deve comparar dados estruturados — por exemplo, a projeção da `TipoCalculo` com `TIPO_CALCULO` — e nunca inferir mérito da redação livre.

## 7. Aplicação obrigatória

Esta RFC vale para todas as regras propostas autoradas daqui em diante, inclusive as unidades do Ciclo 1. A sucessora de regra legada nasce neste formato; o catálogo importado não é reescrito em massa.

Para uma regra ser considerada autorada quanto à fundamentação, devem estar presentes:

- o texto nas três partes;
- todos os dispositivos articulados em `taxonomias`;
- a `TipoCalculo` correspondente em `proveniencia.fontes_consultadas`;
- a indicação explícita das pendências que ainda impeçam detalhamento completo da fórmula;
- coerência entre prosa, forma de cálculo e campos de projeção.

Pendência de detalhamento **não impede** a fundamentação quando a forma jurídica aplicável já está identificada. Impede apenas que o texto afirme o detalhe ainda desconhecido.

## 8. Exemplos de aplicação

### 8.1 Ramo integral

> Do reconhecimento do acidente em serviço resulta a concessão de proventos integrais, sem redução proporcional ao tempo, segundo a forma de cálculo fundada no art. 40, inciso I, da Constituição Federal em sua redação original. A composição concreta da base remuneratória observa a legislação vigente na data de implementação do direito e permanece vinculada à `TipoCalculo` correspondente. A paridade decorre do art. 40, § 4º, da mesma redação e opera como regime de revisão posterior.

### 8.2 Ramo proporcional com medida ainda pendente

> Do enquadramento nas demais causas resulta a concessão de proventos proporcionais, mediante aplicação de fração relacionada ao tempo sobre a base remuneratória juridicamente aplicável, nos termos do art. 40, inciso I, da Constituição Federal em sua redação original. A forma de cálculo vinculada identifica o ramo e o ajuste proporcional; a medida concreta da fração será apurada segundo a legislação estadual vigente na data do direito, sem que esta fundamentação antecipe denominador ainda não identificado. A paridade decorre do art. 40, § 4º, da mesma redação.

## 9. Questões externas que permanecem abertas

- o formato concreto do documento que consumirá o campo;
- o limite técnico de comprimento das colunas do Sisprev;
- a localização de marca de regime (“permanente”, “transição”);
- parâmetros operacionais de formas de cálculo ainda não completamente decompostas.

Essas questões não reabrem a decisão de autoria: enquanto forem resolvidas, a regra deve apontar a forma e os dispositivos corretos e declarar precisamente o que ainda falta.
