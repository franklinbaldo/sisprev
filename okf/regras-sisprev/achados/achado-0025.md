---
type: Achado
id: achado-0025
nome: Moléstia profissional é uma das três causas que decidem a integralidade das seis regras de invalidez, e nenhum dos dois regimes estaduais a define — as outras duas são definidas no mesmo artigo
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0019.md
  - /regras/regra-0022.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Nos dois regimes estaduais de aposentadoria por incapacidade, os proventos são
proporcionais ao tempo de contribuição **exceto** se a incapacidade decorrer de
uma de três causas — e a enumeração é a mesma nos dois, palavra por palavra:

> **acidente em serviço**, **moléstia profissional** ou **doença grave,
> contagiosa ou incurável**

É essa exceção que decide o campo `integral` das seis regras deste lote. As
duas leis definem duas das três classes, no mesmo artigo:

| classe                            | LCE 432/2008        | LCE 1.100/2021            |
| --------------------------------- | ------------------- | ------------------------- |
| acidente em serviço               | art. 20, §§ 6º e 7º | art. 30, §§ 5º e 6º       |
| doença grave/contagiosa/incurável | art. 20, § 9º (rol) | art. 30, § 8º (rol de 16) |
| **moléstia profissional**         | **—**               | **—**                     |

**A terceira classe nunca é definida.** Ela aparece só dentro da própria
enumeração da exceção, nas duas leis, e em nenhum outro lugar delas.

Isso não é lacuna de citação — é lacuna **normativa** no perímetro das normas
que as seis regras citam. Nenhuma das seis pode citar um dispositivo que
defina "moléstia profissional", porque nas duas leis não há um.

# Evidências

Busca exaustiva pela expressão nos dois textos oficiais compilados,
arquivados localmente (`sha256` no `fontes-oficiais/manifesto.yaml`):

| arquivo                              | ocorrências de "moléstia profissional" | onde                                    |
| ------------------------------------ | -------------------------------------- | --------------------------------------- |
| `ditel-LC432-COMPILADA-REVOGADA.txt` | **1**                                  | art. 20, *caput* (a própria enumeração) |
| `ditel-LC1100---COMPILAÇÃO.txt`      | **3**                                  | art. 30, *caput*, § 13 e § 14           |

E as três ocorrências da LCE 1.100/2021 são a **mesma enumeração repetida**:

- art. 30, *caput* — "exceto se a incapacidade for decorrente de acidente em
  serviço, moléstia profissional ou doença grave, contagiosa ou incurável";
- § 13 — "**se** a incapacidade **for** decorrente de acidente em serviço,
  moléstia profissional ou doença grave, contagiosa ou incurável" (roteia o
  cálculo para o art. 24);
- § 14 — "**se** a incapacidade **não for** decorrente de acidente em serviço,
  moléstia profissional ou doença grave, contagiosa ou incurável" (roteia para
  o art. 26).

Nenhuma delas define; todas as três **usam** o termo como se estivesse
definido. E os §§ 13 e 14 mostram que o termo não é ornamental: é operador de
uma bifurcação de cálculo.

O contraste com as duas classes vizinhas é o que fecha a evidência, porque
mostra que a ausência não é estilo de redação. Nas duas leis o legislador
**parou para definir** as outras duas, no mesmo artigo e imediatamente
adiante:

- "**Acidente em serviço é aquele** ocorrido em exercício, que se relacione,
  direta ou indiretamente, com as atribuições do cargo, provocando lesão
  corporal ou perturbação funcional [...]" (LCE 1.100/2021, art. 30, § 5º;
  LCE 432/2008, art. 20, § 6º), seguida de um § de equiparações com quatro
  incisos;
- "**Consideram-se doenças graves, contagiosas ou incuráveis**, dentre outras
  que a lei indicar com base na medicina especializada, [...] as abaixo
  relacionadas: I - tuberculose ativa; [...]" (LCE 1.100/2021, art. 30, § 8º,
  dezesseis incisos; LCE 432/2008, art. 20, § 9º, rol em texto corrido).

Duas de três definidas, com generosidade de detalhe. A terceira, nenhuma vez.

## Como isso aparece nas seis regras

Nas três de causa empacotada por classe o termo é **usado como rótulo de
ramo**, e é aí que a lacuna deixa de ser acadêmica:

- `regra-0022` (e `regra-0021`) tem `fundamentacao_integral` com **três
  cláusulas** separadas por `|`, uma por classe de causa, e a **terceira é
  exatamente "moléstia profissional"** — a única das três cujo recorte do art.
  30 é "artigo 30" sem parágrafo, porque não há parágrafo a apontar. As outras
  duas apontam `§§ 5º e 6º` e `§ 8º`, que existem.
- `regra-0019` e as quatro de invalidez (`0006`–`0009`) carregam a enumeração
  inteira dentro do parêntese do texto de fundamentação ("acidente em serviço,
  moléstia profissional ou doença grave, contagiosa ou incurável"), sem
  recortar classe alguma.

Ou seja: onde a fundamentação **desce ao nível da classe**, a ausência de
dispositivo para "moléstia profissional" fica visível na própria estrutura do
campo — a cláusula que a invoca é a única sem parágrafo a citar.

## Limite desta conferência, declarado

Este é o ponto em que a conclusão precisa ser lida exatamente como está
escrita.

- **O que está conferido:** nas compilações oficiais da LCE 432/2008 e da LCE
  1.100/2021 — as duas leis que as seis regras citam — a expressão "moléstia
  profissional" aparece apenas dentro da enumeração da exceção, e nenhuma
  delas a define, enquanto ambas definem as outras duas classes no mesmo
  artigo.
- **O que NÃO está conferido, e não se afirma:** que não exista definição em
  norma alguma. A definição pode viver em decreto ou regulamento estadual, em
  ato do IPERON, ou alcançar o RPPS por remissão à legislação federal — a Lei
  nº 8.213/1991 define "doença profissional" e "doença do trabalho" para o
  RGPS, e nenhuma das duas leis estaduais faz essa remissão em texto no artigo
  conferido. **Nada disso foi pesquisado nesta rodada**, e nenhuma das três
  hipóteses está descartada.
- A fonte são as **compilações** da DITEL/Casa Civil, não as publicações
  originais no Diário Oficial. Nos dois artigos conferidos, os parágrafos que
  definem as outras duas classes não trazem nota de alteração (a única nota do
  art. 20 da LCE 432/2008 é a revogação do § 5º e a inclusão do § 15, ambas
  pela LC 504/2009), o que os identifica como redação original pela prática de
  anotação daqueles documentos.
- O § 8º da LCE 1.100/2021 abre o rol com "**dentre outras que a lei
  indicar**", e o § 9º da LCE 432/2008 fecha com "**e outras que a lei
  indicar**" — as duas leis, portanto, **sabem** delegar a lei posterior a
  ampliação de uma classe. Não há cláusula equivalente para moléstia
  profissional: não há nem definição nem delegação.
- **Nenhum vínculo é proposto** para acrescentar ou remover. Não há
  dispositivo que a definição justificasse vincular, e é essa a questão.

# Consequência prática

A classe é **decisiva e sozinha suficiente**: a enumeração da exceção é
disjuntiva ("acidente em serviço, moléstia profissional **ou** doença grave"),
de modo que basta a incapacidade ser decorrente de moléstia profissional para
que os proventos deixem de ser proporcionais. Nas seis regras isso é a
diferença entre `integral: S` e `integral: N` — e na LCE 1.100/2021, por força
dos §§ 13 e 14 do art. 30, é também a diferença entre calcular pelo art. 24 e
pelo art. 26.

Sem definição, quem decide o enquadramento é a perícia médica oficial do
IPERON (art. 30, § 1º da LCE 1.100/2021; art. 20, § 1º da LCE 432/2008), sem
critério normativo estadual a que se ancorar — **e sem que nenhum campo do
cadastro registre a causa**, porque a causa da incapacidade não tem coluna
(Q6). O critério mais consequente do benefício fica, portanto, duplamente
invisível ao catálogo: não é parametrizado, e o texto que o invoca não tem
dispositivo a citar.

Para o requerente o efeito é de previsibilidade: dos três caminhos que levam à
integralidade, dois vêm com definição ou rol publicados e um não vem com nada.
Dois requerimentos materialmente iguais podem ser enquadrados de formas
diferentes sem que nenhum dos dois atos possa ser conferido contra um texto.

# Questão a investigar

1. **Se existe definição fora das duas leis.** É a pergunta que decide se este
   achado é lacuna normativa ou lacuna de citação, e ela é de pesquisa, não de
   interpretação. Três lugares a olhar, na ordem: decreto/regulamento estadual
   e atos do IPERON; a legislação de pessoal do Estado (o estatuto do servidor,
   onde "moléstia profissional" costuma aparecer no regime de licenças); e a
   Lei nº 8.213/1991, art. 20, se houver remissão expressa em algum
   dispositivo estadual não conferido aqui. **Se alguma delas responder, o
   achado se resolve por transcrição e citação, não por alteração de norma.**

2. **Se a ausência é intencional.** A hipótese benigna é que "moléstia
   profissional" seja tratada como conceito técnico-médico consolidado, e a
   sua caracterização deliberadamente deixada à perícia — o que seria coerente
   com o § 1º dos dois artigos. Nesse caso o que falta não é definição, é o
   **protocolo de verificação humana** registrado como tal (o
   `requisito_verificacao_humana` da RFC 0004), e não haveria erro a corrigir
   em campo nenhum.

3. **Se a `regra-0022` deveria citar algo na terceira cláusula.** Hoje ela cita
   "artigo 30" sem recorte, e o artigo inteiro **não está autorado** em
   `okf/dispositivos/lce-1100-2021/` (existem `art-30-caput` e os §§ 1, 2, 5,
   6 e 8). Se a resposta ao item 1 for negativa, "artigo 30" sem recorte pode
   ser a citação **honesta** — a norma não oferece nível mais fino para essa
   classe — e o que falta é o *caput* ser citado explicitamente, já que é ele
   que abre a exceção.

4. **Se isto pede pedido formal ao IPERON.** As classes vizinhas mostram que a
   definição é o formato que o legislador estadual escolheu para as outras
   duas; pedi-la é pedido de **norma**, não de coluna, e portanto fora do que a
   parametrização resolve. Registrado como tal.
