---
type: Conjunto
id: ciclo-01-s5-consistencia
nome: Ciclo 1 — S5 — consistência transversal de invalidez e incapacidade
situacao: proposto
base: ciclo-01-s4-bloco-c
---

# Função desta composição

Este conjunto não acrescenta nem retira unidades. Ele deriva de
`ciclo-01-s4-bloco-c` e registra os desempates, as formas de cálculo e as
pendências localizadas necessárias para que os três blocos possam ser lidos como
um único catálogo coerente.

A ausência de delta no frontmatter é deliberada: S5 harmoniza a composição já
produzida; não cria uma quarta família material de regras.

# Precedência entre o regime preservado e o permanente

Existe interseção cronológica entre as unidades do Bloco B e as do Bloco C:

- o art. 4º da ECE 146/2021 preserva requisitos, cálculo e reajuste da
  legislação anterior quando seus requisitos e critérios forem cumpridos até
  31/12/2024;
- a LCE 1.100/2021 vigora desde 18/10/2021.

Essa interseção não autoriza escolha livre nem representa sobreposição sem
desempate. A ordem de seleção é:

1. verificar se o caso preenche, até 31/12/2024, os requisitos e critérios da
   legislação vigente na entrada em vigor da ECE 146/2021;
2. em caso positivo, aplicar a unidade preservada do Bloco B, inclusive seu
   cálculo e reajuste;
3. somente quando a preservação não incidir, aplicar a unidade permanente do
   Bloco C, desde que preenchidos os seus próprios requisitos.

O predicado de precedência é jurídico e humano. Ele não é uma “opção pelo regime
anterior”: o art. 4º usa comando de observância e assegura o benefício a qualquer
tempo. Também não pode ser deduzido apenas da data da incapacidade; a instrução
deve conferir todos os requisitos e critérios da legislação anterior.

Depois de 31/12/2024 não nasce novo enquadramento no art. 4º. Direitos já
formados até a data continuam assegurados a qualquer tempo.

# Matriz de compatibilidade

- **Bloco A × Bloco B:** as janelas de implementação do direito são contíguas e
  não se sobrepõem: o Bloco A fecha em 31/12/2003 e o Bloco B começa nesse mesmo
  marco pela convenção inclusiva/exclusiva documentada em `docs/spec/`.
- **Bloco B × Bloco C:** a interseção de 18/10/2021 a 31/12/2024 é intencional e
  resolvida pela precedência do art. 4º, não por cardinalidade de datas.
- **Dentro de cada bloco:** as quatro classes de causa são mutuamente
  excludentes na seleção. `causa_comum` exige prova suficiente de que nenhuma
  classe qualificada incide; ausência de informação permanece indeterminada.
- **Entre coortes de ingresso:** `DATA_ADM_ATE = 31/12/2003` e
  `DATA_ADM_APOS = 01/01/2004` são limites inclusivos e contínuos, sem dia
  descoberto.

# Formas de cálculo compostas

S5 autora três formas que o enum legado não representa integralmente:

- `forma-calculo-media-proporcional-dias-lce432`: média do art. 45 seguida da
  fração em dias do art. 17, no segmento cuja redação do art. 45 está
  transcrita;
- `forma-calculo-remuneracao-cargo-proporcional-ec70`: remuneração do cargo
  efetivo do art. 6º-A seguida da proporcionalidade do ramo residual;
- `forma-calculo-media-proporcional-dias-lce1100`: média do art. 24 seguida da
  fração em dias do art. 26, aplicável às duas coortes do Bloco C.

A forma de cálculo inicial é independente do regime de reajuste. A mesma média
proporcional da LCE 1.100/2021 pode ser seguida de paridade ou de reajuste sem
paridade, conforme o art. 27; isso confirma que `paridade` não determina, por si
só, cálculo pela última remuneração.

# Pendências resolvidas

- A interseção temporal entre os Blocos B e C recebe desempate jurídico expresso.
- A combinação proporcional com paridade da antiga `regra-0020` permanece
  válida: cálculo inicial pela média proporcional e reajuste paritário são
  dimensões diferentes.
- As três fórmulas compostas conhecidas deixam de ser descritas como “não
  identificadas” no plano conceitual. A falta está na projeção do produto, não no
  conhecimento jurídico.
- Q6-R está resolvida para o catálogo auditado: a classe de causa é predicado da
  unidade, mesmo sem coluna deployável.

# Dependências localizadas

## Fórmulas anteriores ou não integralmente transcritas

Permanece faltando fonte autorada suficiente para:

- o cálculo estadual entre 31/12/2003 e a vigência da Lei 10.887/2004;
- a redação original do art. 45 da LCE 432/2008 e o segmento anterior à LCE
  672/2012;
- a fórmula estadual anterior à LCE 432/2008, inclusive sob a LC 228/2000;
- eventuais limitadores do art. 45 que precisam preceder a fração do art. 17.

Essas lacunas bloqueiam declarar completa a projeção de cálculo de toda a janela
do Bloco B, mas não reabrem a matriz de causas nem a existência dos ramos.

## Q6-S e Q6-T

O repositório não contém tela, banco, solicitação, laudo real ou contrato de API
que demonstre onde o Sisprev obtém e registra a causa do requerente. Também não
contém protocolo institucional suficiente para dizer quem caracteriza acidente
em serviço, nexo de moléstia profissional e vigência do rol de doenças.

A dependência fica atribuída ao IPERON, como titular do produto e do fluxo de
concessão, com evidência necessária claramente delimitada:

1. captura de tela ou schema do campo utilizado na solicitação/processo;
2. modelo de laudo e ato que identifica o responsável pela classificação;
3. procedimento de reconhecimento do acidente e do nexo profissional;
4. fonte versionada do rol de doenças e regra de escolha temporal; e
5. demonstração de como o valor apurado chega à seleção da regra.

Enquanto essa evidência não existir, todas as unidades do ciclo permanecem
`simulavel: N`. A dependência é operacional e de auditabilidade; não impede a
conclusão jurídica da matriz.

# Estado para S6

A consistência jurídica dos três blocos está fechada, mas S6 ainda não pode
promover o conjunto a `vigente`. Antes disso, deve:

1. decidir se as lacunas de fórmula do Bloco B exigem nova autoria ou aceitação
   institucional explícita de pendência;
2. obter ou formalmente encaminhar Q6-S/Q6-T ao IPERON;
3. conferir que cada unidade possui os dispositivos e a forma conceitual
   suficientes para sua janela;
4. registrar decisão de completude e ato institucional; e
5. executar todos os gates técnicos sobre a composição final.
