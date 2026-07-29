---
type: Achado
id: achado-0019
nome: Sexo é a única divergência material entre regra-0030 e regra-0031, e nenhuma das seis provisões que elas citam distingue por sexo
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0030.md
  - /regras/regra-0031.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0030` (`sexo: MASCULINO`) e `regra-0031` (`sexo: FEMININO`) são duas
regras de aposentadoria compulsória. Comparado o frontmatter inteiro,
divergem em **exatamente um campo material: `sexo`**. Têm o mesmo `nome`, a
mesma `fundamentacao_proporcional` (byte a byte), a mesma lista de seis
`dispositivos:`, as mesmas janelas e os mesmos campos de resultado.

Lidas em texto **integral** as seis provisões que as duas citam e vinculam,
nenhuma delas contém as palavras "homem", "mulher" ou "sexo".

Este achado foi autorado a partir de um item de candidatura mais largo — o de
que o critério `sexo` não teria dispositivo que o fundasse nas **doze** regras
de transição do catálogo. Conferido contra fonte oficial, **esse item é falso
nas doze**, e a seção "O que este achado não alcança" nomeia todas elas. O que
se sustenta é este caso, que não é de transição e cuja conferência agora fecha
nas duas pontas.

# Evidências

## A ponta mecânica

Aplicada a chave material do `P2_IGUALDADE_MATERIAL_ATIVA` (frontmatter menos
identidade, `nome`, `dispositivos` e campos administrativos), `regra-0030` e
`regra-0031` divergem em `sexo` e em mais nada. Os detectores as reportam hoje
**só** em `P1_NOME_REPETIDO` — as duas se chamam "Compulsória - Art. 40, §1º,
II da CF e LC nº 152/15, c/c art. 31 da Lei Complementar nº 1.100 /2021".

Se o `sexo` das duas fosse igualado, o par passaria a ser materialmente
idêntico e o `P2` passaria a agrupá-lo. Isso é uma consequência mecânica
prevista, não um argumento de que deva ser igualado.

## A ponta jurídica, agora fechada nas seis

A `fundamentacao_proporcional` das duas, idêntica, é:

> Aposentadoria compulsória com proventos proporcionais ao tempo de
> contribuição, com base na média aritmética simples, e sem paridade, com base
> no artigo 40, § 1º, II, da Constituição Federal, com redação dada pela
> Emenda Constitucional nº 88/2015, artigo 2º da Lei Complementar nº 152/2015,
> artigos 24, 26, 27, inciso II, e 31 da Lei Complementar Estadual nº
> 1.100/2021.

| provisão vinculada                     | lida em                                         | distingue por sexo? |
| -------------------------------------- | ----------------------------------------------- | ------------------- |
| `cf88/art-40-par-1-inc-ii/ec-88-2015`  | publicação original da EC 88/2015 (cópia local) | não                 |
| `lc-152-2015/art-2/original`           | publicação original da LC 152/2015              | não                 |
| `lce-1100-2021/art-24/original`        | compilação oficial, artigo inteiro              | não                 |
| `lce-1100-2021/art-26/original`        | compilação oficial, artigo inteiro              | não                 |
| `lce-1100-2021/art-27-inc-ii/original` | compilação oficial, artigo inteiro              | não                 |
| `lce-1100-2021/art-31/original`        | compilação oficial, artigo inteiro              | não                 |

**O que esta conferência acrescenta à que a precedeu.** A
[reconferência dos blocos 4 e 5](../../../docs/analysis/reconferencia-blocos-4-e-5.md)
§3.4 chegou ao mesmo veredito lendo o **texto transcrito no corpus**. Mas dois
desses documentos transcrevem menos do que endereçam: `lc-152-2015/art-2`
endereça o artigo inteiro e para no caput ("aos 75 (setenta e cinco) anos de
idade:"), e `lce-1100-2021/art-24` e `art-31` idem, parando antes dos seus
§§. Numa conferência sobre "nenhuma provisão distingue por sexo", incisos não
transcritos são exatamente onde a distinção costuma estar — é o modo de falha
que o [`achado-0018`](achado-0018.md) documenta.

As três lacunas foram fechadas:

- **LC 152/2015, art. 2º**, incisos I a V, na publicação original: "I - os
  servidores titulares de cargos efetivos da União, dos Estados, do Distrito
  Federal e dos Municípios, incluídas suas autarquias e fundações; II - os
  membros do Poder Judiciário; III - os membros do Ministério Público; IV - os
  membros das Defensorias Públicas; V - os membros dos Tribunais e dos
  Conselhos de Contas." O parágrafo único trata do Serviço Exterior
  Brasileiro. A palavra "homem", "mulher" ou "sexo" **não ocorre em lugar
  nenhum da lei**.
- **LCE 1.100/2021, arts. 24, 26, 27 e 31**, lidos por extenso na compilação
  oficial já arquivada
  (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`): nenhuma das três
  palavras ocorre em nenhum dos quatro artigos, caput e §§ incluídos.
- **CF/88, art. 40, § 1º, II, na redação da EC 88/2015**, conferido contra a
  cópia local da publicação original da Emenda: "compulsoriamente, com
  proventos proporcionais ao tempo de contribuição, aos 70 (setenta) anos de
  idade, ou aos 75 (setenta e cinco) anos de idade, na forma de lei
  complementar". Sem distinção.

**Fontes.** EC 88/2015 e a compilação da LCE 1.100/2021 estão em
`fontes-oficiais/arquivos/` e no `manifesto.yaml`. A LC 152/2015 foi lida em
`https://www2.camara.leg.br/legin/fed/leicom/2015/leicomplementar-152-3-dezembro-2015-781987-publicacaooriginal-148807-pl.html`
(sha256 `8cd6587cf7610a788fe7bff855cb7d2e91d73a36dc30dfc99ec9622e5e5ba9b8`),
baixada nesta sessão e **não arquivada** — o `manifesto.yaml` lista a LC
152/2015 em `faltando:`, com o Planalto devolvendo HTTP `000`, e arquivá-la é
trabalho do coletor (`scripts/arquivo_de_fontes.py`). É **publicação
original**, não texto compilado: se o art. 2º foi alterado depois de
04/12/2015, esta leitura não sabe.

# Consequência prática

O par existe e é operado. Um requerente do sexo masculino é dirigido à
`regra-0030` e um do feminino à `regra-0031`, e o registro não mostra
diferença alguma no que decorre disso: mesmo cálculo, mesmas janelas, mesmo
texto de fundamentação — que, sendo o mesmo, também não explica por que há
duas.

O desdobramento tem custo concreto: as duas têm o **mesmo `nome`**, então a
pessoa que seleciona a regra numa tela vê duas entradas indistinguíveis, e o
`P1_NOME_REPETIDO` as reporta por isso. Segundo
[`docs/spec/regra.md`](../../../docs/spec/regra.md), `sexo` é critério
aferido confirmado — logo duas regras que divergem nele são legitimamente
duas, e o que falha é o rótulo. Só que aqui a aferição não tem consequência
visível em campo nenhum nem apoio em provisão citada nenhuma.

**Nada aqui afirma o que o motor faz.** As duas são `simulavel: S`, e `sexo`
é coluna, então é lido; mas a idade-limite — o critério que de fato decide uma
compulsória — **não tem coluna em regra nenhuma**, e o motor não lê
fundamentação. O que se prova é uma divergência entre o registro e as leis que
ele cita, não um comportamento.

**Não se conclui que o `sexo` esteja errado.** Corrigi-lo é alterar campo
deployável, e há duas saídas opostas: consolidar as duas numa (mudança de
granularidade, dentro do escopo de parametrização) ou manter o par e mostrar,
no texto, o que o justifica. Escolher é de quem responde pelo produto.

# O que este achado não alcança

**Não alcança nenhuma das doze regras de transição.** O item de candidatura
afirmava que nelas o `sexo` não seria fundado por provisão transcrita alguma,
e a reconferência que o revisou reduziu a acusação a dez, excluindo
`regra-0103` e `regra-0104`. Conferido contra as publicações originais das
emendas, o `sexo` está fundado **nas doze**:

| família                 | regras                 | provisão citada, vinculada e fundante  |
| ----------------------- | ---------------------- | -------------------------------------- |
| art. 2º da EC 41/2003   | 0097, 0098, 0099, 0100 | `ec-41-2003/art-2`, incisos I e III, a |
| art. 6º da EC 41/2003   | 0101, 0102, 0103, 0104 | `ec-41-2003/art-6`, incisos I e II     |
| art. 3º da EC 47/2005   | 0085, 0086, 0105, 0106 | `ec-47-2005/art-3`, inciso I           |
| art. 46 da LCE 432/2008 | 0103, 0104 (também)    | `lce-432-2008/art-46`, incisos I e II  |

Os textos, verbatim:

> **EC 41/2003, art. 2º** — I - tiver cinqüenta e três anos de idade, se
> homem, e quarenta e oito anos de idade, se mulher; [...] III - contar tempo
> de contribuição igual, no mínimo, à soma de: a) trinta e cinco anos, se
> homem, e trinta anos, se mulher;

> **EC 41/2003, art. 6º** — I - sessenta anos de idade, se homem, e cinqüenta
> e cinco anos de idade, se mulher; II - trinta e cinco anos de contribuição,
> se homem, e trinta anos de contribuição, se mulher;

> **EC 47/2005, art. 3º** — I - trinta e cinco anos de contribuição, se homem,
> e trinta anos de contribuição, se mulher;

Cada uma das doze cita nominalmente o seu artigo na `fundamentacao_integral`
e o vincula em `dispositivos:`, e os três documentos endereçam o **artigo
inteiro** (`componentes: [artigo 2]`, `[artigo 6]`, `[artigo 3]`) — os
incisos acima estão, portanto, dentro da provisão vinculada.

**O que separava `0103`/`0104` das outras dez não era o direito, era o
corpus.** Elas vinculam também `lce-432-2008/art-46/original`, que está
transcrito por inteiro (caput, incisos I a IV e §§) e cujos incisos I e II
dizem "se homem"/"se mulher" — conferidos contra
`fontes-oficiais/arquivos/ditel-LC432-COMPILADA-REVOGADA.txt`. Os três
documentos das emendas param no caput. A diferença é de **transcrição
disponível**, não de fundamento: a conferência das dez precisa sair do
repositório, a das duas não.

Fontes: EC 41/2003 e EC 47/2005 nas publicações originais da Câmara
(`…emendaconstitucional-41-19-dezembro-2003-497025-publicacaooriginal-1-pl.html`,
sha256 `161a613e…`; `…emendaconstitucional-47-5-julho-2005-537717-publicacaooriginal-30462-pl.html`,
sha256 `d7e3a62d3954b46ef636783df194fb75fbf9c0cb5c6689922b795ced078eb8d8`),
baixadas nesta sessão e não arquivadas. São publicações originais; o texto
compilado do Planalto segue inacessível, então eventual alteração posterior
desses incisos não foi verificada — e a pergunta de **se e quando** os arts.
2º e 6º da EC 41 e o art. 3º da EC 47 deixaram de valer em Rondônia continua
aberta, nos termos de `fontes-oficiais/PENDENCIAS.md`.

**Não se afirma nada sobre a `regra-0032`**, que é da mesma família da
compulsória e cuja anomalia de `tipo_calculo` está fora deste achado.

# Questão a investigar

1. **Se o desdobramento por sexo da compulsória tem decisão institucional por
   trás.** O paralelo mais próximo já está registrado: a
   [reconciliação policial](../../../docs/analysis/reconciliacao-policial.md)
   §1 mostra a matriz to-be da PGE-RO mantendo o desdobramento por sexo em
   hipóteses cuja base legal é a mesma nas duas linhas. Se houver decisão
   equivalente aqui, o par é escolha e não erro — e é pergunta ao IPERON/PGE,
   não conferência de catálogo. É a pendência que mais muda a leitura deste
   achado.

2. **Se o que distingue as duas é a idade-limite, que não tem coluna.** As
   compulsórias do catálogo se dividem entre 70 e 75 anos, e **nenhum campo de
   nenhuma das seis regras compulsórias grava esse número** — nem `nome`, nem
   fundamentação. Se a distinção real entre `0030` e `0031` fosse etária, o
   catálogo não teria como expressá-la, e `sexo` estaria carregando a
   diferença que falta representar. É hipótese, e a saída dentro do escopo de
   parametrização não é criar coluna: é pedido ao IPERON, registrado como tal.

3. **Se a leitura vale contra o texto compilado.** Tudo o que este achado lê
   de norma federal vem de publicação original. Reaberto o Planalto, a
   primeira coisa a reconferir é o art. 2º da LC 152/2015 — o único dos seis
   vínculos cuja transcrição no corpus para no caput e cujo texto integral
   não está arquivado localmente.
