---
type: Achado
id: achado-0049
nome: As quatro regras de invalidez fundamentam-se em duas redações do art. 40, § 1º da CF que nunca vigeram juntas, e a segunda é de aposentadoria voluntária por idade
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As quatro regras de `APOSENTADORIA POR INVALIDEZ` do regime EC 41/2003
(`regra-0006`, `0007`, `0008`, `0009`) citam, em campo deployável, **duas
redações do mesmo art. 40, § 1º da Constituição Federal**:

- `artigo 40, § 1º, inciso I, [...] com redação dada pela Emenda Constitucional nº 41/2003`;
- `artigo 40, § 1°, inciso III, [...] com a redação dada pela Emenda Constitucional nº 103/2019` — em `0008`/`0009`, com o recorte "segunda
  parte".

Duas coisas estão erradas nessa articulação, e são independentes uma da
outra.

**Primeira: as duas redações nunca estiveram em vigor ao mesmo tempo.** Não
há data em que um requerimento pudesse invocar as duas.

**Segunda: o inciso III, nas duas metades e em qualquer redação, é de
aposentadoria voluntária por idade.** Ele não fixa nenhum critério de
incapacidade, e nenhuma das quatro regras parametriza idade mínima — de modo
que a leitura "norma de competência/remissão", que salva a citação do inciso
III em outras famílias do catálogo, aqui não tem a que se ligar.

# Evidências

## O texto do inciso III, conferido na fonte oficial

Conferido no texto do Planalto da própria EC 103/2019, arquivado localmente
(`fontes-oficiais/arquivos/planalto-emc103.htm`, `sha256` no
`fontes-oficiais/manifesto.yaml`) — **não** apenas na transcrição do corpus:

> III - no âmbito da União, aos 62 (sessenta e dois) anos de idade, se
> mulher, e aos 65 (sessenta e cinco) anos de idade, se homem, e, no âmbito
> dos Estados, do Distrito Federal e dos Municípios, na idade mínima
> estabelecida mediante emenda às respectivas Constituições e Leis Orgânicas,
> observados o tempo de contribuição e os demais requisitos estabelecidos em
> lei complementar do respectivo ente federativo.

O inciso **de fato se biparte**, e a bipartição é a que a
`fundamentacao_integral` de `0008`/`0009` invoca ao dizer "segunda parte": a
primeira metade é o corte federal de 62/65 anos, a segunda remete aos Estados
a fixação da idade mínima. A leitura textual existe. Mas **as duas metades
tratam de idade**, e o que elas variam é *quem fixa o número*, não a matéria.

Percorridos os critérios das quatro regras — tipo de benefício, `sexo`,
janelas de admissão e de direito, `integral`, `tipo_calculo`, `paridade` —
nenhum é fixado por esse inciso. As quatro concedem
`APOSENTADORIA POR INVALIDEZ`, e nenhuma das quatro grava idade em campo
algum: não há coluna de idade no cadastro, e não há valor de idade em nenhum
dos campos delas.

Observação lateral que reforça a incongruência: o inciso III é **o único
dispositivo citado pelas quatro que distingue por sexo** ("se mulher"/"se
homem"), e as quatro gravam `sexo: AMBOS`. O `sexo: AMBOS` está correto —
funda-se por ausência, porque nenhum dispositivo da cadeia de incapacidade
distingue —, mas isso significa que a única distinção de sexo entre as
provisões citadas vem justamente da provisão cuja matéria não é a das regras.

## As duas redações são disjuntas, e o § 1º que cada uma exige é outro

Um dispositivo é a unidade endereçada **com toda a cadeia que a contém** (ver
[`docs/spec/dispositivo.md`](../../../docs/spec/dispositivo.md)). Citar um
inciso do § 1º é, portanto, citar também o *caput* do § 1º na redação
contemporânea a ele. Os dois *caputs* são textos diferentes, conferidos nas
publicações oficiais arquivadas:

| redação do § 1º          | *caput* conferido                                                                                                                                                                        | fonte arquivada       |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| EC 41/2003 (inciso I)    | "Os servidores abrangidos pelo regime de previdência de que trata este artigo serão aposentados, **calculados os seus proventos a partir dos valores fixados na forma dos §§ 3º e 17**:" | `planalto-emc41.htm`  |
| EC 103/2019 (inciso III) | "**O servidor abrangido por regime próprio de previdência social** será aposentado:"                                                                                                     | `planalto-emc103.htm` |

E as vigências autoradas no bundle, que a EC 103/2019 torna adjacentes e
disjuntas:

| dispositivo vinculado                   | vigência                |
| --------------------------------------- | ----------------------- |
| `cf88/art-40-par-1-inc-i/ec-41-2003`    | 2003-12-31 → 2019-11-12 |
| `cf88/art-40-par-1-inc-iii/ec-103-2019` | 2019-11-13 → em vigor   |

Um dia separa as duas. **Não existe data em que ambas vigessem**, e as quatro
regras as invocam na mesma frase, como base conjunta de um mesmo benefício.

Vale registrar o que isso **não** prova. A citação do inciso I na redação da
EC 41/2003 está **certa** para estas quatro: é o regime que elas
implementam, e é essa redação que traz o discriminante
integral × proporcional ("exceto se decorrente de acidente em serviço,
moléstia profissional ou doença grave, contagiosa ou incurável") que a
redação da EC 103/2019 **perdeu**. O defeito está do lado do inciso III.

## Por que a leitura de competência não socorre aqui

Em outras famílias do catálogo a citação do art. 40, § 1º, III é defensável
como **norma de remissão**: a segunda parte é o que autoriza a ECE 146/2021 a
fixar a idade mínima estadual, e regras cujo critério *é* uma idade mínima
articulam legitimamente a provisão constitucional com a estadual. Essa
leitura está registrada em
[`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md)
§5.2, e este achado não a contesta.

Ela não se aplica às quatro de invalidez por uma razão simples: **não há
idade nenhuma a remeter**. A remissão do inciso III é a de um número de
idade; onde a regra não afere idade, a remissão não alcança critério algum
dela. As quatro citam a ECE 146/2021 pelo **art. 4º** — a cláusula de
preservação dos requisitos da legislação anterior —, não por qualquer
dispositivo de idade mínima.

## Um agravante em `regra-0008` e `regra-0009`

Nessas duas o defeito é mais apertado, porque o inciso III aparece **em lugar
do** inciso I, e não ao lado dele. A `fundamentacao_integral` das duas funda a
integralidade em "artigo 40, § 1°, inciso III, segunda parte" e **não cita o
inciso I em nenhum ponto** — enquanto a `fundamentacao_proporcional` da mesma
regra cita o inciso I. Os dois campos da mesma regra discordam sobre qual
inciso constitucional a sustenta.

E o dispositivo central que as duas invocam **exclui essa leitura pelo próprio
texto**. Conferido na publicação oficial da EC 70/2012
(`fontes-oficiais/arquivos/planalto-emc70.htm`):

> Art. 6º-A. O servidor [...] que tenha ingressado no serviço público até a
> data de publicação desta Emenda Constitucional e que tenha se aposentado ou
> venha a se aposentar por invalidez permanente, **com fundamento no inciso I
> do § 1º do art. 40 da Constituição Federal**, tem direito a proventos de
> aposentadoria calculados com base na remuneração do cargo efetivo [...]

O art. 6º-A **condiciona expressamente** o direito que concede a que a
aposentadoria tenha fundamento no **inciso I**. A `fundamentacao_integral` de
`0008`/`0009` invoca o art. 6º-A e, no mesmo período, aponta o inciso III como
fundamento — o que a norma invocada não admite.

## Limite desta conferência, declarado

- Os **textos** do inciso III, do § 1º em cada redação e do art. 6º-A foram
  conferidos nas publicações oficiais arquivadas em `fontes-oficiais/`, com
  `sha256` no manifesto. Não são leitura do corpus nem de memória.
- As **datas** de vigência (2003-12-31, 2019-11-13) vêm dos `norma.md` e dos
  dispositivos autorados no bundle, não foram reconferidas contra a
  publicação do DOU nesta rodada. Se alguma delas estiver errada, a
  adjacência muda de forma — mas não a disjunção, porque as duas redações são
  sucessivas por construção.
- **Nenhum vínculo é proposto para acrescentar ou remover.** `dispositivos:`
  registra o que o campo cita, e o campo cita o inciso III: os quatro
  vínculos estão corretos como leitura. O defeito é do texto citado, não do
  link.

# Consequência prática

`FUNDAMENTACAO_INTEGRAL` e `FUNDAMENTACAO_PROPORCIONAL` são campos
**deployáveis**: é esse texto que chega ao ato de concessão e ao servidor. As
quatro regras entregam hoje uma fundamentação que combina duas redações
mutuamente excludentes do mesmo parágrafo constitucional e invoca, para uma
aposentadoria por incapacidade, o inciso da aposentadoria voluntária por
idade.

O dano não é de seleção: `integral`, `tipo_calculo` e `paridade` das quatro
são fundados por outras provisões (o próprio inciso I, o art. 6º-A, os arts.
20, 45 e 62 da LCE 432/2008), e nenhum critério aferido depende do inciso III.
É dano de **justificação** — a peça jurídica que sustenta o benefício cita
direito que não é o do caso, e num benefício concedido por incapacidade
permanente, cuja motivação é sindicável.

# Questão a investigar

1. **Se a citação do inciso III deve sair das quatro.** É a saída mais
   simples, e a conferência não encontra critério que a perda desmontaria.
   Mas é edição de campo deployável, logo decisão de quem responde por ele —
   não da auditoria.

2. **Se o que se pretendia citar era outra coisa.** Duas hipóteses, nenhuma
   verificada: o art. 40, § 1º, **I** na redação da EC 103/2019 (o inciso da
   incapacidade no regime novo), que faria sentido para o trecho da janela
   posterior a 13/11/2019; ou nada — herança de preenchimento de outra
   família de regras, onde a citação é legítima. A primeira hipótese é
   testável: se for ela, o defeito é de **inciso**, não de matéria.

3. **Se a janela das quatro deveria terminar em 12/11/2019.** As quatro têm
   `data_direito_ate: 31/12/2099` (sentinela, não interpretada — P5) e citam
   uma redação que morreu em 12/11/2019. Se a janela alcança 2026, ela cobre
   um período em que o inciso I citado já não vigia — que é o mesmo formato do
   [`achado-0014`](achado-0014.md), ali sobre a compulsória. A diferença é que
   aqui existe uma família de regras para o período seguinte (`0019`–`0022`),
   o que torna a hipótese de janela excessiva mais concreta.

4. **Se `0008`/`0009` são caso separado.** O agravante do art. 6º-A é
   específico dessas duas e admite correção própria (trocar inciso III por
   inciso I na `fundamentacao_integral`), independentemente do que se decida
   para as quatro. Registrado aqui, e não em achado próprio, porque a causa é
   a mesma citação.

5. **Alcance fora deste lote.** O mesmo padrão foi relatado em ao menos 29
   regras do catálogo (§5.2 da lista consolidada), por agentes independentes.
   Este achado cobre **apenas** as quatro de invalidez, e a formulação dele —
   disjunção de redações + matéria alheia — não se transfere automaticamente
   para regras que aferem idade, onde a leitura de competência vale.
