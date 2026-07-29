---
type: Achado
id: achado-0046
nome: Quatro regras de transição calculam idade por redução sobre a alínea "a" do art. 40, § 1º, III da CF, e nenhuma a cita nem a vincula — as quatro citam, no lugar dela, a redação da EC 103/2019 que a extinguiu
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0097.md
  - /regras/regra-0098.md
  - /regras/regra-0105.md
  - /regras/regra-0106.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0097`/`0098` implementam o art. 2º da EC 41/2003 e `regra-0105`/`0106` o
art. 3º da EC 47/2005. As duas transições têm em comum o mecanismo que as
define: **a idade de aposentadoria não é um número fixo, é o resultado de uma
redução aplicada sobre outro dispositivo** — a alínea "a" do art. 40, § 1º, III
da Constituição Federal, que fixa 60 anos se homem e 55 se mulher.

Nas quatro regras, essa alínea:

- **não é citada** em `fundamentacao_integral`;
- **não está** em `dispositivos:`;
- não aparece no `nome`.

O que as quatro citam no lugar dela é "artigo 40, § 1°, inciso III, **segunda
parte**, da Constituição Federal, com a redação dada pela Emenda Constitucional
nº 103/2019" — e vinculam
`cf88/art-40-par-1-inc-iii/ec-103-2019`, que é a redação **que extinguiu a
alínea**: o inciso III da EC 103/2019 não tem alíneas.

Não é o mesmo defeito das §§4.2/5.2 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md),
que registram que o art. 40, § 1º, III não funda critério representado nas
colunas. Aqui há um dispositivo que **funda um critério gravado** —
`tipo_calculo: Valor Médio com Redutor da Idade` nas duas primeiras, a "fórmula
85/95" do `nome` nas duas últimas —, ele existe, está transcrito no bundle, e
nenhuma das quatro o alcança.

# Evidências

## As duas transições remetem à alínea nominalmente, e o texto é verbatim

Conferido em `fontes-oficiais/arquivos/planalto-emc41.htm` (sha256
`af74d4331bb95caacbfffd2293e784e4365761c646f900c2a08b12bcb5bb518f`) e
`fontes-oficiais/arquivos/planalto-emc47.htm` (sha256
`408a9df87e4f7a196f0892d39962ac0c5e908d343af1e12e985bba38cbda41e5`), ambos no
`manifesto.yaml`. Os dois arquivos são **cp1252**, não UTF-8 — decodificados
como UTF-8, a busca por "alínea" retorna zero sem levantar erro.

> **EC 41/2003, art. 2º, § 1º** — O servidor de que trata este artigo que
> cumprir as exigências para aposentadoria na forma do caput terá os seus
> proventos de inatividade **reduzidos para cada ano antecipado em relação aos
> limites de idade estabelecidos pelo art. 40, § 1º, III, a, e § 5º da
> Constituição Federal**, na seguinte proporção: I - três inteiros e cinco
> décimos por cento, para aquele que completar as exigências [...] até 31 de
> dezembro de 2005; II - cinco por cento, [...] a partir de 1º de janeiro de
> 2006\.

> **EC 47/2005, art. 3º, III** — **idade mínima resultante da redução,
> relativamente aos limites do art. 40, § 1º, inciso III, alínea "a", da
> Constituição Federal**, de um ano de idade para cada ano de contribuição que
> exceder a condição prevista no inciso I do caput deste artigo.

Nos dois casos a alínea "a" não é contexto: é o **minuendo**. Sem ela o
percentual de redução do art. 2º, § 1º não tem sobre o que incidir, e a idade
mínima do art. 3º, III não tem valor.

Os documentos que o bundle tem dos dois artigos de transição
(`ec-41-2003/art-2/original` e `ec-47-2005/art-3/original`) **param no
*caput***, e é por isso que a remissão não é visível no corpus — é o modo de
falha nomeado em §5.3 daquela lista, e é o mesmo que produziu a conclusão
errada corrigida no `achado-0018`.

## Os números da alínea, e a diferença por sexo que o catálogo não carrega

Transcrita no bundle em `cf88/art-40-par-1-inc-iii-al-a/`, nas duas redações:

> a) sessenta anos de idade e trinta e cinco de contribuição, se homem, e
> cinqüenta e cinco anos de idade e trinta de contribuição, se mulher;

Combinando com os requisitos próprios de cada transição, lidos nas publicações
acima:

| regra      | transição     | idade do caput | referência da redução (alínea "a")             | efeito                             |
| ---------- | ------------- | -------------- | ---------------------------------------------- | ---------------------------------- |
| `0097` (M) | art. 2º EC 41 | 53 anos        | 60 anos                                        | até 7 anos antecipados × 5% ao ano |
| `0098` (F) | art. 2º EC 41 | 48 anos        | 55 anos                                        | até 7 anos antecipados × 5% ao ano |
| `0105` (M) | art. 3º EC 47 | —              | 60 anos, −1 por ano de contribuição além de 35 | 60+35 = **95**                     |
| `0106` (F) | art. 3º EC 47 | —              | 55 anos, −1 por ano de contribuição além de 30 | 55+30 = **85**                     |

O `nome` de `0105`/`0106` — "FÓRMULA 85/95" — é literalmente a soma dos
números da alínea "a" com os do inciso I do art. 3º. **A regra nomeia-se pelo
resultado de um dispositivo que ela não cita.**

Nenhum desses números tem coluna no catálogo: idade, tempo de contribuição,
tempo de serviço público, tempo de carreira, tempo no cargo e percentual de
redutor estão todos fora das 27 colunas. A diferença masculino/feminino que a
lei manda — 60/55, 35/30, 53/48 — não é conferível contra o cadastro, porque o
cadastro só grava `sexo`. É a hipótese de trabalho da Q5, e aqui ela se
confirma em quatro regras: o único campo que registra o mecanismo é
`tipo_calculo: Valor Médio com Redutor da Idade`, que o nomeia sem
parametrizá-lo.

## A redação vinculada é a que extinguiu a alínea

`cf88/art-40-par-1-inc-iii/ec-103-2019` (vigência a partir de 2019-11-13)
transcreve:

> III - no âmbito da União, aos 62 (sessenta e dois) anos de idade, se mulher,
> e aos 65 (sessenta e cinco) anos de idade, se homem, e, no âmbito dos
> Estados, do Distrito Federal e dos Municípios, na idade mínima estabelecida
> mediante emenda às respectivas Constituições e Leis Orgânicas [...]

Conferido no art. 1º da EC 103/2019
(`fontes-oficiais/arquivos/planalto-emc103.htm`, sha256
`73dd6248d146e0faaea2a1cf8b15f729084898367fd993ab1e293ae10b12170b`): o novo
inciso III **não tem alíneas**, e as alíneas *a* e *b* da redação anterior
cessaram com ele. Os documentos do bundle registram a mesma coisa pelas datas —
`al-a/ec-41-2003` termina em 2019-11-12.

O efeito é que, das duas metades do inciso III da EC 103/2019, a que as quatro
regras invocam ("segunda parte", a que remete aos Estados) é norma de
**competência** — ela manda a emenda estadual fixar a idade —, não fonte da
idade. É a formulação que §5.2 daquela lista fixou como a correta, e ela vale
aqui: o vínculo não é falso, é insuficiente para o critério em causa.

Também não é a emenda estadual que supre: `ece-146-2021/art-4`, que as quatro
citam e vinculam, preserva "os requisitos e os critérios exigidos pela
legislação vigente até a data de entrada em vigor desta Emenda" — ou seja,
**remete de volta** à alínea "a", sem repetir número nenhum.

## O documento de destino existe

`cf88/art-40-par-1-inc-iii-al-a/ec-41-2003`, vigência **2003-12-31 →
2019-11-12**, é a redação contemporânea à abertura da janela das quatro regras
(`data_direito_apos: 31/12/2003` em todas). Foi autorada na
[varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md)
§3 e ainda **não é vinculada por regra nenhuma** do catálogo.

# Consequência prática

Estas quatro regras existem para conceder uma idade **menor** que a do regime
geral, e a medida dessa redução vem de fora do que elas declaram. Quem confere
uma concessão — controle interno, PGE, Tribunal de Contas — lendo a ficha ou o
capítulo do relatório encontra três dispositivos em cada uma das quatro, e em
nenhum deles o número 60, o 55 ou o percentual de 3,5%/5%.
O art. 2º e o art. 3º vinculados param no *caput*, então o texto reimpresso no
relatório termina em "quando o servidor, cumulativamente:" e em "desde que
preencha, cumulativamente, as seguintes condições:" — a lista de condições não
aparece.

`FUNDAMENTACAO_INTEGRAL` é o texto entregue ao servidor. Nas quatro ele afirma
"com Aplicação do redutor de idade (se houver antecipação)" (`0097`/`0098`) ou
nomeia a "FÓRMULA 85/95" no `nome` (`0105`/`0106`) sem citar a norma que fixa a
idade de referência. Quem quiser recalcular o próprio provento a partir do
documento não consegue.

Nada aqui afirma que o motor calcule errado. As quatro são `simulavel: S`, e o
redutor não é parametrizado em coluna nenhuma — ele está em código, em tabela
externa ou em análise manual, que é justamente a Q5. O que se prova é sobre o
registro: **o dispositivo que dá a medida do critério não está declarado**.

# Questão a investigar

1. **Se a fundamentação deve nomear a alínea "a".** É a leitura mais simples —
   e há precedente no próprio catálogo: `regra-0039`/`0040`, `0089`/`0090`,
   `0093`/`0094` citam a alínea nominalmente e a vinculam. Mas `FUNDAMENTACAO*`
   é campo **deployável**, e reescrevê-lo é alteração de produto. **Nenhum
   vínculo é proposto aqui**, e não poderia ser: a fundamentação atual não cita
   a alínea, e declarar o vínculo afirmaria que ela cita (RFC 0008). O vínculo
   só se torna possível **depois** de a fundamentação mudar — nesta ordem, não
   na inversa.

2. **Qual redação da alínea cada regra invocaria.** Se a fundamentação passar a
   citá-la, a escolha não é livre: a janela das quatro é
   `[31/12/2003 , 31/12/2024]`, e `al-a/ec-41-2003` cobre 2003-12-31 →
   2019-11-12, deixando de 2019 a 2024 sem redação da alínea (ela não existe
   mais no plano federal). Fechar esse trecho depende do item 3.

3. **O alcance das transições depois de 13/11/2019 — conclusão jurídica que
   este achado não toma.** O art. 35 da EC 103/2019 revoga os arts. 2º e 6º da
   EC 41/2003 e o art. 3º da EC 47/2005; o art. 36, II condiciona essas
   revogações, **para os regimes próprios dos Estados**, à "data de publicação
   de lei de iniciativa privativa do respectivo Poder Executivo que as
   referende integralmente", sem efeito retroativo. Qual lei estadual cumpre
   esse papel em Rondônia — e se a LCE 1.100/2021 o cumpre — é a pendência
   registrada na §5.2 e nas "quatro recusas" da
   [varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md),
   e é por isso que `ec-41-2003/art-2/original`, `ec-41-2003/art-6/original` e
   `ec-47-2005/art-3/original` seguem **sem `vigencia_inicio` e sem
   `vigencia_fim`** no corpus. Enquanto isso não se decide, nada se conclui
   sobre a vigência das quatro regras — e note-se que datar errado aqui poria
   "fora de vigência" exatamente a fundamentação de quem tem direito adquirido.

4. **A transcrição dos incisos dos dois artigos de transição.** É a fila
   `TRANSCREVER` de §5.3 daquela lista, e é o que tornaria a remissão à alínea
   "a" visível no corpus sem tocar campo deployável nenhum. Não fecha este
   achado — a lacuna é na fundamentação da regra, não no bundle —, mas remove a
   condição que fez a conferência anterior não ver o problema.
