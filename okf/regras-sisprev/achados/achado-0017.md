---
type: Achado
id: achado-0017
nome: Três regras de policial citam só a alínea feminina da LC 51/1985; em duas delas o sexo declarado não é o dela
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0078.md
  - /regras/regra-0079.md
  - /regras/regra-0084.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O art. 1º, II da LC 51/1985, na redação da LC 144/2014, tem duas alíneas —
uma por sexo:

> **a)** após **30** (trinta) anos de contribuição, desde que conte, pelo
> menos, **20** (vinte) anos de exercício em cargo de natureza estritamente
> policial, **se homem**;
>
> **b)** após **25** (vinte e cinco) anos de contribuição, desde que conte,
> pelo menos, **15** (quinze) anos de exercício em cargo de natureza
> estritamente policial, **se mulher**.

Três regras citam essa provisão, e **as três nomeiam apenas a alínea "b"**, a
feminina. A alínea "a" não é citada por regra nenhuma do catálogo.

| regra        | `sexo`    | alínea citada   | compatível?          |
| ------------ | --------- | --------------- | -------------------- |
| `regra-0078` | MASCULINO | "b" (se mulher) | **não**              |
| `regra-0079` | FEMININO  | "b" (se mulher) | sim                  |
| `regra-0084` | AMBOS     | "b" (se mulher) | **não, para metade** |

# Evidências

**`regra-0078` e `regra-0079` são o mesmo documento com um campo trocado.**
Têm `dispositivos:` idêntico item a item, `nome` idêntico, e os mesmos
`integral: S`, `paridade: S`, `tipo_calculo`, `data_adm_ate: 13/11/2019`. A
única diferença material é `sexo` — MASCULINO numa, FEMININO na outra.

O par foi desdobrado por sexo e a fundamentação **não acompanhou**: escreveu-se
a versão feminina e ela ficou nas duas. É a mesma forma do `achado-0016`, onde
quatro regras de professor partilham um texto que só descreve uma delas — e a
recorrência da forma é ela própria informação.

**Na `regra-0084` a incompatibilidade é localizada e mais forte.** Ela é
`sexo: AMBOS`, e dois dos seus quatro vínculos alcançam os dois sexos: o
*caput* do art. 7º da ECE 146/2021 ("idade mínima de 55 anos **para ambos os
sexos**") e o § 2º ("aos 52 anos, **se mulher**, e aos 53 anos, **se homem**").
Só o vínculo da LC 51/1985 é unissexual.

E é justamente esse que decide, porque o § 2º **remete a ele**:

> desde que cumprido o período adicional de contribuição correspondente ao
> tempo que [...] faltaria para atingir **o tempo de contribuição previsto na
> Lei Complementar n° 51, de 20 de dezembro de 1985**.

O § 2º não fixa tempo de contribuição: manda buscá-lo na LC 51. O único que a
regra nomeia é **25 anos, o feminino**. Para o requerente homem, a única
provisão que a regra invoca para o cálculo do período adicional é a que não se
aplica a ele.

# Consequência prática

O que está comprovado é **incompatibilidade entre o `sexo` gravado e a única
alínea citada**, com risco de fundamentação errada no documento entregue.

O que **não** se afirma, e a distinção é a mesma do `achado-0010`: que o motor
afira 25/15 em vez de 30/20. Tempo de contribuição e tempo de exercício
policial **não têm coluna** no cadastro. Em `regra-0078`, que é `simulavel: S`,
o motor não lê a fundamentação; em `regra-0084`, que é `simulavel: N`, a
indicação depende de triagem humana — e aí a fundamentação **é** o que a
pessoa lê para decidir, o que torna o risco maior, não menor.

`regra-0084` chama-se "Aposentadoria por Mandado de Injunção". O provimento
judicial que a define não foi localizado, então o que ela de fato aplica não é
reconstruível pelo catálogo.

**Severidade `bloqueante`**, pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md) ("Quando um achado é
`bloqueante`"): em `regra-0078` e `regra-0084` o campo deployável invoca a
alínea que a LC 51/1985 reserva ao outro sexo daquele que a regra declara — a
fundamentação entregue contradiz o critério que a própria regra afere. Que o
motor não afira 25/15 é o que este achado deixa de afirmar; o que ele afirma,
e basta ao critério, é que o texto que sai no ato cita norma que não é a do
caso. `regra-0079` fica na população pela citação truncada, sem a
incompatibilidade de sexo — a severidade é do achado, e a disposição de cada
regra é onde essa diferença se escreve.

# Relação com o que já está registrado

O `achado-0010` registra, desde 2026-07-18, a divergência entre `sexo` e o
texto da fundamentação **na `regra-0078`**, a partir da detecção
`P9_SEXO_FUNDAMENTACAO`. Este achado não o substitui: acrescenta o que o
detector não enxerga — **qual provisão é invocada e o que ela exige** — e
alcança duas regras que o `0010` não cobre.

`regra-0084` não aparece em **nenhuma** das detecções ativas nem em achado
algum até aqui. O `P9_SEXO_FUNDAMENTACAO` não dispara nela porque o campo
`sexo` é `AMBOS`, e a palavra "mulher" no texto deixa de ser divergência
aparente. É o ponto cego exato do detector.

# Questão a investigar

1. **Se a alínea "a" deveria ser citada, e por quem.** A leitura mais simples
   é que `regra-0078` deveria citar a masculina e `regra-0084` as duas. Mas
   `FUNDAMENTACAO*` é campo **deployável**: reescrevê-lo é alterar o produto,
   não auditar o catálogo. Nenhum vínculo é proposto aqui — vincular a alínea
   "a" a uma regra que não a cita seria inventar citação, não corrigi-la.

2. **Se `regra-0078` e `regra-0079` deveriam existir como par.** Os requisitos
   diferem por sexo (30/20 × 25/15), então o desdobramento é legítimo e é o que
   a spec chama de critério aferido distinto. O defeito não é o par existir; é
   ele não ter chegado à fundamentação.

3. **Um candidato provável ao provimento da `regra-0084`, que não explica nem
   sana a citação.** O levantamento em
   [`docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md`](../../../docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md)
   localiza o **Mandado de Injunção nº 1.545/DF** (STF, Rel. Min. Joaquim
   Barbosa, decisão monocrática, DJ de 04/03/2010), impetrado pelo Sindicato dos
   Agentes Penitenciários do Estado de Rondônia — SINGEPERON. O dispositivo
   determina que a Administração analise a situação fática dos substituídos
   **"à luz do art. 57 da lei 8.213/1991"**, sem mencionar a LC 51/1985.

   **O vínculo entre esse provimento e a `regra-0084` permanece inferencial.**
   Falta o ato, parecer ou nota técnica do IPERON que ligue o cadastro àquele
   MI. Ele é candidato provável — a categoria e o Estado coincidem, e o nome da
   regra é do mesmo instituto —, não identificação fechada.

   O que a fonte permite afirmar é estreito e vale registrar assim: **o
   precedente não explica nem sana a citação da alínea "b"**. Ele não fornece
   justificativa para ela, porque não tratou daquela norma. Disso **não** se
   segue que a citação atual seja lapso de cópia — a própria hipótese registrada
   é de reparametrização posterior sob a ECE 146/2021, e a causa do erro
   continua sem demonstração.

   A conclusão deste achado não depende disso: ela se sustenta na
   **incompatibilidade interna** entre `sexo: AMBOS` e a alínea que a LC 51/1985
   reserva a um sexo, que é legível no próprio documento.

   Ressalva de método: o dispositivo foi lido em **transcrição** num documento do
   TCE-SC, não no inteiro teor do STF, que respondeu HTTP 503 às tentativas.

4. **Se a categoria da `regra-0084` é policial penal.** A origem documentada é a
   dos agentes penitenciários de Rondônia, categoria que hoje corresponde ao
   policial penal. Mas a fundamentação **gravada** é a do art. 7º da ECE
   146/2021, que alcança policial civil, policial legislativo, policial penal e
   agente de segurança socioeducativo sem distinguir entre eles. Origem histórica
   e conteúdo cadastrado apontam para recortes diferentes, e a decisão sobre qual
   deles o `nome` da regra deve descrever é de mérito.

5. **Questão condicional — a conjugação dos dois regimes.** O MI nº 4.528 AgR
   (Tribunal Pleno, j. 13/06/2012, DJE de 01/08/2012), transcrito na mesma fonte,
   afasta a conjugação da LC 51/1985 com o art. 57 da Lei 8.213/91 **"para com
   isso cogitar-se de idade mínima para aposentação"** — é vedação a um uso
   determinado, não proibição abstrata de qualquer convivência histórica entre os
   regimes.

   A `regra-0084` não cita nem parametriza o art. 57; ela conserva um nome
   genérico cujo vínculo ao MI 1.545 ainda não foi documentado. A questão só se
   coloca **se** duas coisas forem demonstradas: o elo entre a regra e aquele MI,
   e aplicação simultânea dos dois regimes num mesmo cálculo. Enquanto nenhuma
   delas estiver de pé, não há o que concluir daqui.
