# Achados candidatos da conferência `critério → dispositivo`

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. Consolida os sete
> relatórios de conferência que cobrem 101 das 112 regras. **Nada aqui é
> achado** — achado é documento autorado por humano em `achados/`, e a
> decisão de qual destes vira um é do auditor.

## Como ler esta lista

A ordem é de **gravidade**, e o critério é o dano que o erro causa se a regra
for aplicada a um requerimento real:

1. **A regra invoca provisão de outro benefício ou de outra pessoa** — aplica
   direito que não é o do caso.
2. **A regra funda-se em provisão que não vigia na janela dela** — aplica
   direito revogado, ou ainda não vigente.
3. **O valor gravado contradiz a lei que a própria regra cita** — o cadastro
   e a fundamentação, ambos deployáveis, dizem coisas diferentes.
4. **Critério decisivo sem dispositivo que o funde** — a regra decide por um
   critério que nenhuma provisão citada sustenta.
5. **Padrões sistêmicos** — repetem-se em lotes independentes, o que os torna
   estruturais.

Marcações: **[V]** = conferi pessoalmente o texto do dispositivo e o campo
da regra; **[V parcial]** = conferi parte do que a afirmação exige e digo
qual parte falta; **[R]** = vem do relatório do grupo, não reconferido aqui.

______________________________________________________________________

## 1. Provisão de outro benefício ou de outra pessoa

### 1.1 `regra-0078` funda-se na alínea que rege mulheres **[V]**

`sexo: MASCULINO`. O campo `fundamentacao_integral` cita — e `dispositivos:`
vincula — `lc-51-1985/art-1-inc-ii-al-b`, cujo texto é:

> **b)** após **25** anos de contribuição, desde que conte, pelo menos, **15**
> anos de exercício em cargo de natureza estritamente policial, **se mulher**.

A alínea **"a"**, imediatamente acima na mesma norma, é a masculina: **30**
anos de contribuição e **20** de exercício policial, "se homem".

**O que está comprovado:** incompatibilidade entre `sexo: MASCULINO` e a
única alínea citada e vinculada, que é a feminina.

**O que não está, e não se afirma aqui:** que o motor efetivamente afira
25/15 em vez de 30/20. Tempo de contribuição e tempo de exercício policial
**não têm coluna** no cadastro, e numa regra `simulavel: S` o motor não lê a
fundamentação. A citação errada produz justificativa jurídica errada e revela
lacuna de parametrização — mas o comportamento real do motor não é
reconstruível pelo catálogo.

O `achado-0010` já registra o `P9_SEXO_FUNDAMENTACAO` nesta regra; o detector
só enxerga a palavra "mulher" no texto, enquanto a conferência mostra qual
provisão é invocada.

### 1.2 `regra-0084`: `sexo: AMBOS` vinculando só a alínea feminina **[R]**

Mesmo padrão, sem detector nenhum apontando — o `P9_SEXO_FUNDAMENTACAO` não
dispara porque o campo `sexo` é `AMBOS`. Aqui `simulavel: N`, então a
fundamentação pode orientar a triagem humana; mas falta conhecer o provimento
judicial que define esta regra antes de dizer o que ela de fato aplica.

### 1.3 `regra-0061` e `regra-0062` citam o § único de artigo de auxílio-reclusão **[V parcial]**

Ambas são `APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`. O campo
`fundamentacao` de cada uma cita "Art. 39, **parágrafo único** da Lei
Complementar 432/2008" — e o ***caput*** desse artigo é:

> Art. 39. **O auxílio-reclusão** do segurado, servidor ativo, será concedido
> ao conjunto de seus dependentes, a contar da data em que o segurado preso
> deixa de perceber vencimentos [...]

**Verificação parcial, e a distinção importa.** O que conferi foi o *caput*.
O objeto literal da citação é o **parágrafo único**, que **não está
transcrito** no corpus (`lce-432-2008/` só tem `art-39`). É juridicamente
muito provável que permaneça no âmbito do auxílio-reclusão, por integrar o
mesmo artigo — mas isso não foi conferido.

A formulação segura hoje: *as regras citam o parágrafo único de artigo cujo
caput disciplina auxílio-reclusão; falta conferir o texto exato do parágrafo.*
Transcrevê-lo fecha a questão em qualquer direção.

**A consequência de segunda ordem importa tanto quanto a citação:** essa
diferença textual é a **única coisa** que mantém 0061/0062 fora de um grupo
`P2_IGUALDADE_MATERIAL_ATIVA`. A afirmação mecânica segura é essa —
*removê-la faria os três pares cair no mesmo grupo/fingerprint do P2*.

Não se segue daí que sejam duplicatas, por duas razões. Antes de transcrever
o parágrafo único não está provado que haja erro nenhum a remover. E, mesmo
que houvesse, o próprio [`CLAUDE.md`](../../CLAUDE.md) registra que um grupo
`P2_IGUALDADE_MATERIAL_ATIVA` pode ser **regras legitimamente distintas cuja
distinção o catálogo não expressa** — granularidade mais fina que as colunas,
não duplicação. Qual dos dois é o caso continua sendo decisão humana.

______________________________________________________________________

## 2. Provisão fora de vigência na janela da regra

### 2.1 `regra-0032` grava como marco de direito exatamente o dia em que caiu a norma que ela cita **[V parcial]**

```
data_direito_apos: 18/10/2021
  lce-432-2008/art-17         vigência → 2021-10-18
  lce-432-2008/art-21-par-1   vigência → 2021-10-18
  lce-432-2008/art-45         vigência → 2021-10-18
  lce-432-2008/art-62         vigência → 2021-10-18
```

O que está **provado**, sem depender de nenhuma interpretação de campo:

- a regra vincula quatro dispositivos da LCE 432/2008;
- os quatro encerram vigência em 18/10/2021, revogados pela LCE 1.100/2021;
- `data_direito_apos` grava exatamente esse mesmo marco;
- a regra cita o regime revogado e **não** cita os dispositivos
  correspondentes da LCE 1.100/2021;
- `0030`/`0031` apontam para a idade de 75 anos, e a fundamentação da `0032`
  aponta para a de 70.

**Verificação parcial, e a ressalva é do próprio repositório.** Uma versão
anterior desta lista dizia "revogado no *primeiro dia* da sua janela" e que a
janela "abre" em 18/10/2021. Isso pressupõe a leitura de `DATA_DIREITO_APOS`
que
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
§1.2 registra expressamente como **não confirmada** — a simetria com
`DATA_ADM_APOS` é a presumível, e a issue #39 existe exatamente para não
presumi-la. "Primeiro dia", "abre" e "coexistem por N anos" são conclusões
que dependem dessa pendência.

Sem resolvê-la, o que se sustenta é **incompatibilidade temporal altamente
provável e sobreposição candidata** — o que já basta para autorar o achado.
A conclusão fechada fica condicionada à decisão sobre `DATA_DIREITO_APOS`.

### 2.2 `regra-0030`/`0031`: perda de resolução temporal, não retroatividade **[V]**

Uma versão anterior desta lista as chamava de "espelho" da 0032 e acusava
aplicação de norma ainda não vigente. **Está retirado**: as duas citam
`lc-152-2015` **e** `lce-1100-2021`, e a LC 152/2015 passou a impor 75 anos
aos servidores estaduais em 04/12/2015 — que é exatamente onde a janela
abre. O art. 31 da LCE 1.100/2021 pode integrar a mesma fundamentação como
norma estadual superveniente, para o trecho a partir de 18/10/2021. Uma
regra só pode estar agregando dois períodos normativos sucessivos que
produzem o mesmo resultado.

O que resta, e é real: **perda de resolução temporal** — o catálogo não
informa qual norma sustenta qual trecho da janela.

A inconsistência forte permanece na **0032**, e some com ela a sobreposição:
os marcos gravados em 0030/0031 e em 0032 põem as três regras em vigor ao
mesmo tempo sob idades-limite diferentes — 70 pelo art. 21 da LCE 432/2008,
75 pela LC 152/2015 e pelo art. 31 da LCE 1.100/2021. A **extensão** dessa
coexistência (três anos, na leitura simétrica) depende da mesma pendência de
§2.1; a coexistência em si, não.

______________________________________________________________________

## 3. Valor gravado contra a fundamentação da própria regra

Este é o bloco mais numeroso. Em todos, os dois lados são **campo deployável**
— o cadastro e o texto entregue ao servidor discordam entre si.

### 3.1 `regra-0041` × `regra-0107`: string idêntica, três campos opostos **[V]**

|                          | 0041                                | 0107            |
| ------------------------ | ----------------------------------- | --------------- |
| `fundamentacao_integral` | **idêntica, caractere a caractere** | ←               |
| `sexo`                   | MASCULINO                           | MASCULINO       |
| `apos_especial`          | S                                   | S               |
| `integral`               | **S**                               | **N**           |
| `tipo_calculo`           | **Remuneração de Contribuição**     | **Valor Médio** |
| `paridade`               | **S**                               | **N**           |

O mesmo texto jurídico sustentando resultados opostos. Uma das duas está
errada, e o texto não diz qual.

### 3.2 Onze regras do regime novo gravam resultado contrário à própria fundamentação **[R]**

Relatado no grupo LCE 1.100/2021, sobre 24 regras.

### 3.3 `regra-0109`/`0110`: três campos contra o único dispositivo que os funda **[R]**

`ece-146-2021/art-7-par-3` estabelece totalidade da remuneração do cargo e
reajuste paritário. As duas gravam `integral: N`, `paridade: N`,
`tipo_calculo: Valor Médio`. A janela de admissão (2003–2024) também é
incompatível com o corte de ingresso até 13/11/2019 do próprio art. 7º.

### 3.4 `regra-0033`/`0034`: `integral: N` num texto que diz "proventos integrais" **[R]**

O único campo de fundamentação preenchido é o integral, e ele diz "com
proventos integrais".

### 3.5 `regra-0019`/`0020`: texto diz "integrais e com paridade", campos gravam `N` **[R]**

### 3.6 `regra-0032`: `tipo_calculo: Tipo Cálculo Nova Previdência` **[R]**

O texto da própria regra diz "média aritmética simples", e seus vínculos são
os arts. 17 e 45 da LCE 432/2008.

### 3.7 `regra-0057`/`0058`: integralidade dependendo do sexo, sem dispositivo que a funde **[R]**

______________________________________________________________________

## 4. Critério decisivo sem dispositivo

### 4.1 A idade-limite não é campo de regra nenhuma na compulsória **[R]**

O critério que **define** a aposentadoria compulsória — a idade em que ela
incide — não está parametrizado em nenhuma das seis regras do tipo.

### 4.2 `apos_especial: S` sem fundamento em campo nenhum **[R]**

Em `0099`/`0100` (transição) e em três dos quatro subgrupos especiais do
regime novo, o que **define** a especialidade não tem dispositivo citado.

### 4.3 `sexo` não é fundado por provisão transcrita nenhuma nas doze de transição **[R]**

E em `0030`/`0031` o `sexo` M/F é hoje a única coisa que impede o `P2` de
agrupá-las — sem dispositivo que o justifique.

### 4.4 O art. 34 diz "para ambos os sexos", e quatro regras se dividem por sexo **[R]**

### 4.5 A causa da incapacidade (Q6) **[V, já registrado]**

Distingue `0006`↔`0007` e `0008`↔`0009`, e nenhuma coluna a registra. Os
campos de 0006 e 0007 são **literalmente idênticos**; o que as separa está
dentro do parêntese de um texto compartilhado.

______________________________________________________________________

## 5. Padrões sistêmicos

Apareceram em lotes independentes, conferidos por agentes diferentes — o que
os torna estruturais, não coincidência.

### 5.1 O 31/12/2024 é padrão fortemente sugestivo — **não uma inversão comprovada**

O art. 4º da ECE 146/2021 é o **único** dispositivo do corpus inteiro que fixa
essa data. E o desencontro aparece em cinco dos seis grupos:

- regras que **o citam e vinculam** gravam `31/12/2099` ou `03/12/2015`;
- regras que **gravam 31/12/2024** não o citam em campo deployável — nas
  `0028`/`0029` e `0109`–`0112` ele aparece só no `nome`, que não é
  fundamentação;
- pares que vinculam os mesmos dispositivos gravam datas diferentes.

**Uma versão anterior desta lista chamava isso de "prazo invertido".** Está
rebaixado: o art. 4º fixa 31/12/2024 para a classe de servidores abrangida
por *aquela* regra de transição, e não transforma a data em termo universal
de toda regra que a contenha. Para afirmar inversão seria preciso demonstrar,
**regra por regra**, que:

1. a hipótese material está abrangida pelo art. 4º;
2. `data_direito_ate` exerce ali exatamente a função do prazo do art. 4º;
3. `31/12/2099` não é apenas sentinela técnica (P5 não a interpreta);
4. não há outro marco administrativo ou norma de transição explicando o
   mesmo valor.

Nada disso foi demonstrado. O que há é **coincidência sistemática entre o
marco, o `nome` e o dispositivo**, em lotes conferidos por agentes
independentes — evidência forte de fundamentação incompleta em alguns pares,
e a pista de maior alcance da conferência. As disjunções bem formuladas estão
nos relatórios de grupo; aqui fica só o padrão.

### 5.2 O art. 40, § 1º, III não fixa critério representado nas colunas — em pelo menos 29 regras

Confirmado nas 4 de invalidez, nas 13 de policial e nas 12 de transição, por
três agentes independentes. Já registrado como pendências **P-3**/**P-4** em
[`base-normativa-invalidez-incapacidade.md`](base-normativa-invalidez-incapacidade.md).

**Uma versão anterior dizia "não funda critério nenhum".** É estreito demais,
e perigoso: a segunda parte do inciso integra a **cadeia constitucional que
remete aos Estados a fixação da idade mínima**, o que é fundamento de
competência e de articulação normativa, ainda que não seja fonte imediata de
critério parametrizado. Dizer que não funda nada pode induzir achado errado —
ou, pior, a supressão da citação.

A formulação correta: **não fixa diretamente nenhum critério hoje
representado nas colunas; funciona como norma constitucional de
remissão/competência, e precisa ser articulado com a provisão estadual que
estabelece a idade.** Nas regras de invalidez a tensão é outra e permanece:
nenhuma das duas metades do inciso trata de incapacidade.

### 5.3 Transcrições que param no *caput*, e os requisitos estão nos incisos

- os três artigos de transição (art. 2º e 6º da EC 41/2003, art. 3º da EC
  47/2005) — os requisitos que as 12 regras precisam estão nos incisos;
- art. 35 da LCE 1.100/2021 — transcrito até "observadas as seguintes
  condições:", e os incisos não existem no corpus;
- **caput do art. 7º da ECE 146/2021** — funda o corte de ingresso e a idade
  de 55 anos das policiais, e não existe como dispositivo autorado.

Isso é fila `TRANSCREVER` nova, não detectada pela lista congelada.

**Um caso desta fila já se fechou, e ensina por que ela é grave.** O
`ec-41-2003/art-6a/ec-70-2012` parava no *caput*, embora seus `componentes`
endereçassem o artigo inteiro. O que faltava era o **parágrafo único** — e é
ele, mandando aplicar o art. 7º da EC 41/2003, que funda positivamente a
`paridade: S` de `0008`/`0009`. Com a omissão, a conferência fechou pelo
*caput* ("não se aplica o § 8º do art. 40"), que é norma **negativa**: retira
um critério de reajuste, não fixa nenhum. Transcrito o parágrafo e autorado o
art. 7º, o critério fecha pela norma certa.

O modo de falha é o que interessa: uma transcrição truncada faz a conferência
fechar **pela norma errada** sem nada falhar — `componentes` correto, caminho
correto, vínculo resolvendo. Nenhum gate podia pegar. Os itens acima estão
sob o mesmo risco enquanto não forem transcritos: a diferença é que ali a
lacuna é visível (o *caput* anuncia incisos que não existem), e aqui era
silenciosa.

### 5.4 Dezesseis regras da ECE 146/2021 não citam o dispositivo que estabelece seus requisitos **[R]**

______________________________________________________________________

## 6. O que nenhum grupo propôs

**Nenhum vínculo a acrescentar ou remover, nos seis grupos.** O
`dispositivos:` espelha o que as fundamentações citam, em todo o catálogo
conferido.

Todo o problema está em **valores gravados** e em **citações erradas** — e as
duas coisas são campo deployável, logo achado autorado, nunca correção de
link. Cada relatório registra também o que o agente **recusou** concluir.

## 7. Correção à lista congelada

A pendência da `regra-0025` está na fila errada em
[`pendencias-de-citacao-congeladas.md`](pendencias-de-citacao-congeladas.md):
é `TRANSCREVER`, não `REDACAO`. A redação da EC 20/1998 existe — o próprio
`achado-0013` a transcreve.
