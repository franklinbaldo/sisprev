---
type: Achado
id: achado-0057
nome: regra-0065 e regra-0066 gravam Valor Médio citando o art. 25 da LCE 1.100/2021, que manda calcular pela totalidade da remuneração
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0065.md
  - /regras/regra-0066.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

A LCE 1.100/2021 põe base de cálculo e reajuste em **dois trilhos excludentes**,
separados pelo ingresso até ou após 31/12/2003:

> **Art. 24.** No cálculo dos proventos de aposentadoria dos servidores titulares
> de cargo efetivo que tenham ingressado no serviço público em cargo efetivo
> **após 31 de dezembro de 2003** [...] será considerada a **média aritmética
> simples** das maiores remunerações [...] correspondentes a 80% (oitenta por
> cento) de todo o período contributivo [...]

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**
> [...] corresponderá à **totalidade da remuneração no cargo efetivo** em que se
> der a aposentadoria.

O art. 27 espelha a mesma partição no reajuste: o **inciso I** assegura o
tratamento do art. 7º da EC 41/2003 — paridade — a quem ingressou até
31/12/2003; o **inciso II** manda reajustar nos termos do RGPS quem ingressou
depois.

Base e reajuste andam juntos **por construção da lei estadual**: art. 25 com art.
27, I é totalidade da remuneração com paridade; art. 24 com art. 27, II é média
sem paridade.

`regra-0065` e `regra-0066` citam **arts. 25 e 27, I** e gravam
`tipo_calculo: Valor Médio`, que é o regime do art. 24 — o artigo que elas não
citam.

# Evidências

**A contradição é tripla dentro de cada regra.** Os `dispositivos:` vinculam
`lce-1100-2021/art-25` e `lce-1100-2021/art-27-inc-i`; a
`fundamentacao_integral` escreve por extenso o que eles determinam —

> Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com
> proventos integrais (**cálculo por integralidade**) e **com paridade**, com
> base nos artigos **25, 27, inciso I**, e 41, inciso III, da Lei Complementar
> Estadual 1.100/2021 [...]

— e os campos `integral: S` e `paridade: S` confirmam. Só o `tipo_calculo`
destoa.

**A irmã idêntica é o controle, e é o que fecha o argumento.** A `regra-0067` tem
`fundamentacao_integral` **idêntica caractere a caractere** e `dispositivos:`
**idênticos item a item**:

| campo                   | `regra-0065` / `regra-0066` | `regra-0067`                | `regra-0071`              |
| ----------------------- | --------------------------- | --------------------------- | ------------------------- |
| dispositivos de cálculo | arts. **25** e **27, I**    | arts. **25** e **27, I**    | arts. **24** e **27, II** |
| texto da fundamentação  | integralidade, com paridade | integralidade, com paridade | média, sem paridade       |
| `integral`              | `S`                         | `S`                         | `S`                       |
| `paridade`              | `S`                         | `S`                         | `N`                       |
| `tipo_calculo`          | **`Valor Médio`**           | `Valor Efetivo`             | `Valor Médio`             |

`regra-0071` é a versão do outro trilho e é **inteiramente coerente**: cita o
artigo da média, diz média no texto, grava `paridade: N` e `Valor Médio`.
`regra-0067` é a versão deste trilho e também é coerente. `regra-0065` e
`regra-0066` têm o cabeçalho de `0067` e o `tipo_calculo` de `0071`.

**A divergência não decorre de as regras alcançarem populações diferentes.** As
três — `0065`, `0066`, `0067` — gravam exatamente a mesma janela
(`data_adm_apos`, `data_adm_ate`, `data_direito_apos`, `data_direito_ate`
iguais), o mesmo `sexo: AMBOS`, o mesmo `apos_especial: S` e o mesmo
`simulavel: S`. Não há critério aferido que as separe e explique cálculos
diferentes.

## O que sustenta cada candidato do enum

### Evidência a favor de `Valor Efetivo`

- `regra-0067` é a irmã materialmente idêntica de `0065`/`0066` no mesmo
  trilho dos arts. 25 e 27, I, mas grava `Valor Efetivo` em vez de `Valor Médio`;
- `regra-0019` também usa `Valor Efetivo` com o art. 25 e descreve o valor como
  totalidade da remuneração do cargo efetivo;
- o termo “efetivo” é semanticamente próximo da expressão legal “cargo
  efetivo”.

Essa evidência é apenas indiciária. A própria análise da `regra-0019` registra
que o art. 30, § 13, ainda deixa uma questão de encaminhamento do cálculo em
aberto. O catálogo não contém definição técnica de que `Valor Efetivo` seja a
última remuneração.

### Evidência a favor de `Remuneração de Contribuição`

- seis regras do ramo de integralidade com art. 25 — `0035`, `0036`, `0041`,
  `0042`, `0082` e `0083` — gravam `Remuneração de Contribuição` junto com
  `integral: S` e `paridade: S`;
- as análises das regras `0035`, `0082` e `0083` tratam esse código como a
  projeção da totalidade da remuneração do art. 25;
- a frequência do código no catálogo é muito maior: 34 ocorrências contra 4
  de `Valor Efetivo`.

Essa evidência é de padrão do catálogo, não de documentação do motor. O nome
“Remuneração de Contribuição” também é literalmente próximo da base contributiva
do art. 24, que é o regime de média; portanto, o rótulo pode ser enganoso.

### Limite comum da evidência

O documento P16 sobre formas de cálculo registra que o enum legado mistura base,
ajuste e limitador e **não identifica fórmulas**. A forma jurídica
“totalidade da remuneração do cargo efetivo” chega a ser projetada como
`Não identificado` quando não há correspondência segura. Não foi localizada
documentação pública do fornecedor, código do produto, ajuda de tela ou exemplo
de cálculo que resolva a semântica desses dois membros.

### Busca na documentação pública da Agenda Assessoria

A busca foi estendida ao domínio da própria desenvolvedora, incluindo páginas
do produto, catálogo de serviços, notícias de implantação e PDFs públicos. A
página do [Sisprev Web](https://www.agendaassessoria.com.br/page/sisprev-web)
confirma que o produto possui simulador parametrizável, apuração de cálculo e
regras de reajuste, mas não publica o dicionário do enum nem define
`Valor Efetivo` ou `Remuneração de Contribuição`. O [catálogo de produtos e
serviços](https://www.agendaassessoria.com.br/produtos-servicos) confirma a
Agenda como fornecedora do Sisprev Web, sem manual funcional público. A notícia
da [apresentação do Sisprev à Amazonprev](https://www.agendaassessoria.com.br/post/fundacao-amazonprev-manausam-apresenta-novo-sistema-previdenciario-com-recursos-para-simulacao-de-concessao-de-aposentadoria-e-pensao-em-ambiente-virtual)
registra apresentação técnica, capacitação e painel de dúvidas, o que indica
que esse tipo de semântica pode estar em material de implantação ou na área do
cliente, não no site aberto. Os PDFs encontrados no domínio são políticas de
segurança e proteção de dados, não manuais de cálculo.

### Evidência adicional dos manuais de procedimento

Foi localizada, no material de manuais consultado no NotebookLM, uma distinção
operacional que não estava disponível no repositório. No aplicativo Meu RPPS
(volume 2, p. 87), **Remuneração Efetiva** é descrita como o valor da
remuneração do segurado. No cadastro do segurado (volume 1, p. 152),
**Remuneração do Cargo Efetivo** é apresentada separadamente. Já no módulo de
arrecadação (volume 1, pp. 77–78), **Remuneração de Contribuição** é o valor que
serve de base para calcular as contribuições do segurado e do ente; no cadastro
de gratificações (p. 140), ela aparece distinta da remuneração do cargo efetivo
e pode incluir verbas com incidência previdenciária.

Essa distinção reforça `Valor Efetivo` como candidato semântico para o trilho do
art. 25 e enfraquece a leitura de que `Remuneração de Contribuição` seja apenas
outro nome para a remuneração do cargo efetivo. Ainda não é prova conclusiva:
os trechos identificam campos da interface, não demonstram que o enum
`tipo_calculo` aponta exatamente para um deles nem mostram o resultado de um
cálculo com cada código. A referência precisa ser conferida nos PDFs originais
e nas páginas indicadas antes de promover a parametrização.

Assim, a evidência de catálogo favorece provisoriamente
`Remuneração de Contribuição`, enquanto a evidência dos manuais e a evidência
lexical favorecem `Valor Efetivo`. O balanço agora favorece provisoriamente
`Valor Efetivo`, mas nenhum dos dois lados alcança, sozinho, o grau necessário
para alterar a parametrização com segurança.

# Consequência prática

**A divergência é de valor concedido, não de documento.** Estas regras são
`simulavel: S`, e `tipo_calculo` é o campo que orienta o cálculo — ao contrário
da fundamentação, que o motor não lê. Média das maiores remunerações
correspondentes a 80% do período contributivo e totalidade da remuneração no
cargo efetivo produzem valores diferentes, e a diferença é permanente, porque se
projeta em todo o benefício.

A direção do desvio: `Valor Médio` sob o trilho do art. 25 tende a conceder
**menos** do que o dispositivo citado determina.

**Severidade `bloqueante`**, pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md): campo deployável que
contradiz o dispositivo que a própria regra vincula, alcançando o valor do
benefício.

# O que este achado não afirma

**Não afirma que `Valor Efetivo` seja comprovadamente o código executado** para
a totalidade da remuneração do art. 25. Os manuais distinguem remuneração
efetiva, remuneração do cargo efetivo e remuneração de contribuição, mas não
documentam a ligação desses campos ao enum legado. O
`CLAUDE.md`, o P16 e `tests/test_forma_calculo_schema.py` registram que o enum
legado não identifica fórmulas — seus valores misturam base, ajuste e
limitador. O que se afirma é apenas que `Valor Médio` é incompatível com o
trilho do art. 25, que os manuais favorecem semanticamente `Valor Efetivo` e que
a correspondência técnica ainda precisa ser confirmada.

**Não afirma que alguma concessão tenha saído a menor.** Depende de caso
concreto, e o catálogo não registra caso concreto.

**Não presume que a proposta de consolidação já foi adotada.** A planilha da
PGE e o parecer não revelam critério que separe as três linhas, e a unidade
auditada propõe consolidá-las. O grupo continua inativo e as origens continuam
operacionais até decisão do IPERON.

# Por que não é duplicata de achado existente

O [`achado-0042`](achado-0042.md) adverte que um segundo achado sobre estas
regras "não deve nascer duplicado" dele e que "quem estender a população estende
esta lista, não o raciocínio". A advertência é sobre o **defeito de janela** —
`data_adm_ate` sentinela sob os arts. 25 e 27, I —, que estas regras de fato
partilham com a `regra-0067` e que **continua sendo daquele achado**. Este aqui
não o toca.

O [`achado-0016`](achado-0016.md) registra a forma "fundamentação afirma
integralidade e paridade e os campos dizem o contrário", em `regra-0107` e
`regra-0108`. **A forma é parecida e a estrutura probatória não é**, e a
diferença decide o que se pode concluir:

- em `0107`/`0108` os **três** campos (`integral`, `paridade`, `tipo_calculo`)
  contradizem o texto **de forma coerente entre si** — descrevem o regime novo
  inteiro. Não se sabe qual lado corrigir, e o `achado-0016` deixa isso como
  questão aberta;
- aqui `integral` e `paridade` **concordam** com o texto e com os dispositivos
  citados, e só o `tipo_calculo` destoa. O defeito **isola num campo**, e a
  `regra-0067` fornece o valor que o trilho usa.

Um achado que juntasse os dois casos teria de abandonar a conclusão mais forte
deste — qual campo está errado — para caber na indeterminação daquele.

# Questão a investigar

1. **Adotar ou rejeitar a solução temporal proposta.** O
   [`achado-0042`](achado-0042.md) agora alcança as três regras. A unidade
   auditada propõe o trilho dos arts. 25 e 27, I, com
   `data_adm_ate: 31/12/2003` e
   `data_direito_apos: 18/10/2021`. A evidência sustenta esses limites, mas a
   mudança de campos deployáveis ainda exige decisão do IPERON.

2. **Confirmar a consolidação 3:1.** `0065`, `0066` e `0067` partilham janela,
   sexo e fundamentação; a planilha da PGE vincula o mesmo texto e o mesmo
   processo às três. O
   [`achado-0005`](achado-0005.md) registra a igualdade e a unidade auditada
   materializa a consolidação, ainda em `preview`.

3. **Se a mesma incompatibilidade alcança as regras de pensão.** `regra-0016`,
   `regra-0017` e `regra-0018` gravam `paridade: S` com
   `tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte`. Se "Nova
   Previdência" designar base por média, é a mesma contradição noutra família —
   mas é leitura de rótulo, que este achado deliberadamente não faz, e exige
   conferência própria contra os dispositivos daquelas regras.

4. **Qual membro do enum executa a totalidade da remuneração do art. 25.** A
   resposta exige evidência do produto: descrição da tela, código/configuração
   do fornecedor ou exemplo de cálculo comparativo. Até lá, a divergência entre
   `Valor Efetivo` e `Remuneração de Contribuição` permanece aberta e bloqueia a
   promoção das unidades pré-2004.
