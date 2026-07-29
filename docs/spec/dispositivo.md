# Spec — `type: Dispositivo` e `type: Norma` (RFC 0001, P3/P4)

- **Status**: vigente desde 2026-07-27. Substitui o schema plano original
  (`artigo`/`paragrafo`/`inciso`/`alinea` + `fonte`), que foi migrado por
  inteiro — os 55 dispositivos existentes foram reescritos e nenhum texto de
  dispositivo mudou. As questões em aberto estão na última seção; elas não
  bloqueiam nada do que está descrito aqui.
- **Parte de**: [RFC 0001](../rfc/0001-criterios-de-validacao-das-regras.md),
  P3 (bundle de dispositivos legais) e P4 (formato canônico de citação).
- **Implementação**: `scripts/dispositivo_endereco.py` (núcleo puro),
  `scripts/dispositivo_schema.py` (contrato e I/O),
  `scripts/norma_schema.py` (P4), `site/src/lib/dispositivo.ts` (porte de
  exibição). Testes: `tests/test_dispositivo_endereco.py`,
  `tests/test_dispositivo_schema.py`, `tests/test_norma_schema.py`,
  `site/src/lib/dispositivo.test.ts`.

## Por que o schema anterior foi substituído

O schema original guardava o endereço do dispositivo em quatro campos
planos e opcionais. Isso falhava em cinco frentes, todas verificáveis no
próprio repositório antes da migração:

1. **Estados que o domínio proíbe passavam.** Nada impedia
   `{artigo, alinea}` sem inciso — uma alínea órfã.
2. **Os campos guardavam tipografia, não dados.** `artigo: "Art. 40"`,
   `paragrafo: "§ 1º"`, `inciso: "I"` — três convenções num registro só, e
   `paragrafo` guardava ora um número (`§ 14`), ora um nome
   (`Parágrafo único`), ora um número com sufixo (`§ 4º-A`). Havia, nos
   dados, duas grafias do mesmo símbolo ordinal (`§ 1º` e `§ 1°`).
3. **`caput` não era representável.** `cf88/art-40-caput-original.md` tinha
   frontmatter `artigo: Art. 40` e nada mais — indistinguível, no
   frontmatter, de um documento do artigo inteiro. O `caput` existia apenas
   no slug.
4. **Não havia ordem.** O índice gerado de `lce-432-2008` listava sete
   provisões do art. 20 todas rotuladas "Art. 20", na ordem
   `p1, p14, p2, p6, p7, p9` — ordem de string de caminho. O gerador não
   tinha nem rótulo completo nem chave comparável para usar, porque o
   schema não os tinha.
5. **A identidade era composta à mão e derivava.** O slug fundia dispositivo
   e redação (`art-40-p1-i-ec41-2003`), e o sufixo de redação aparecia em
   alguns documentos e não em outros — `lc-51-1985/art-1-ii-a` tinha
   `redacao_dada_por` e nenhum sufixo. Nada verificava a correspondência
   entre slug e frontmatter: trocar o frontmatter de dois arquivos passava
   na validação.

## `type: Norma` — o vocabulário fechado (P4)

Uma norma citável é um documento próprio, em
`okf/dispositivos/<chave>/norma.md`:

```yaml
---
type: Norma
id: ec-41-2003
nome: Emenda Constitucional nº 41/2003
apelido: EC 41/2003
fontes:
  - https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc41.htm
---
```

- `id` **é o nome do diretório**, conferido contra ele.
- `nome` é a forma canônica por extenso; `apelido` é a forma curta usada em
  listagens e rótulos. Ficam num lugar só, em vez de a mesma prosa ser
  redigitada em cada dispositivo da norma.
- `fontes` é uma lista **não vazia de URLs http(s)** — publicação oficial
  (Planalto, SAPL/ALE-RO, Diário Oficial). É o que o site publica como link
  clicável, e o que um auditor abre para conferir a transcrição.

Uma norma entra no corpus **sendo redigida**, nunca sendo digitada num
campo. É isso que impede o E6 do RFC 0001 (a mesma norma sob três grafias)
de se reproduzir aqui.

Normas **alteradoras** também são documentadas, mesmo sem contribuir
dispositivo próprio: é a norma alteradora que verifica uma redação, então
ela precisa de uma chave resolvível e de uma URL oficial.

## `type: Dispositivo`

Um dispositivo vive em `<norma>/<endereço>/<redação>.md`:

```
okf/dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
```

```yaml
---
type: Dispositivo
id: cf88/art-40-par-1-inc-i/ec-41-2003
norma: cf88
componentes:
  - tipo: artigo
    valor: '40'
  - tipo: paragrafo
    valor: '1'
  - tipo: inciso
    valor: I
redacao_dada_por: ec-41-2003
vigencia_inicio: 2003-12-31
vigencia_fim: 2019-11-12
fontes:
  - https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc41.htm
---

Art. 40. Aos servidores titulares de cargos efetivos [...]

§ 1º Os servidores abrangidos pelo regime de previdência de que trata este artigo serão aposentados [...]:

I - por invalidez permanente, [...]
```

### O corpo é a cadeia legível até o dispositivo

**O corpo é o texto exato do dispositivo, precedido do texto exato de cada
nível acima dele**, transcrito de publicação oficial — sem paráfrase, sem
resumo, sem seções nomeadas, um parágrafo por nível, na ordem em que a norma
os apresenta.

O corpo de um inciso de parágrafo traz, portanto, o caput do artigo, o caput
do parágrafo e o inciso. Isoladamente, `I - por invalidez permanente, sendo os proventos proporcionais [...]` não diz de que é inciso, e para lê-lo era
preciso abrir outro documento — e adivinhar **qual redação** dele. A cadeia
existe para que o documento que a auditoria cita seja o documento que a
auditoria consegue ler.

**Os níveis acima entram na redação contemporânea a esta.** O documento de
`art-40-par-1-inc-i/ec-41-2003` (vigência 2003-12-31 → 2019-11-12) traz o
caput do art. 40 **e** o caput do § 1º na redação da EC 41/2003 — "na forma
dos §§ 3º e 17" —, porque foi essa a combinação em vigor enquanto esse inciso
vigorou; o documento vizinho, `art-40-par-1-inc-i/ec-20-1998` (1998-12-16 →
2003-12-30), traz os mesmos dois níveis na redação da EC 20/1998 — "na forma
do § 3º". Exibir o caput da EC 103/2019 em qualquer um dos dois montaria um
texto que nunca esteve em vigor junto — e o erro seria invisível, porque cada
metade é verbatim.

**Consequência que é fácil não tirar: alterar um ancestral cria uma redação
nova do dispositivo.** O dispositivo é a unidade endereçada **com toda a
cadeia que a contém**, não apenas o componente mais granular — um inciso é
oração subordinada ao caput e não se lê sem ele. Logo, quando uma emenda
altera só o caput do parágrafo, cada inciso daquele parágrafo passa a ser lido
sob um caput novo: o texto do inciso não mudou, mas **o dispositivo mudou**, e
isso é um arquivo novo no diretório dele, com o nome da emenda que alterou o
ancestral.

É o que faz `art-40-par-1-inc-i/ec-41-2003` existir mesmo que a EC 41/2003
tivesse alterado apenas o caput do § 1º. E é a leitura correta da técnica
legislativa: a emenda reproduz só o que reescreve, e a linha de reticências
sobre um inciso significa "este texto não mudou", **não** "esta emenda não
alcança este inciso" — confundir as duas é confundir texto com norma.

Na prática isso fixa as fronteiras de vigência: **a vida de uma redação
termina na primeira alteração de qualquer nível da sua cadeia**, não só do
nível mais interno.

Isso deixou de ser recomendação e passou a ser contrato (RFC 0009). Cada
entrada de `componentes` declara a sua própria procedência — `redacao_dada_por`,
`vigencia_inicio`, `vigencia_fim` — e os campos do documento são **conferidos
contra a derivação**:

| campo do documento | derivação                        |
| ------------------ | -------------------------------- |
| `vigencia_inicio`  | **máximo** dos componentes       |
| `vigencia_fim`     | **mínimo** dos componentes       |
| `redacao_dada_por` | do componente que fixou o máximo |

A combinação passa a existir quando o **último** nível muda e deixa de existir
quando o **primeiro** deles muda de novo. Ou todos os componentes declaram, ou
nenhum: com metade deles datada, o máximo e o mínimo percorreriam subconjunto
arbitrário e a conferência não significaria nada.

Os campos do documento **não** foram substituídos pela derivação, de
propósito: um campo só derivado nunca discorda de nada, logo nunca acusa
ninguém. É o mesmo idioma do `_check_caminho` — recomputar e comparar.

E daí sai o invariante que fecha o buraco: **o mesmo nível não pode ter duas
redações vigentes na mesma data em todo o corpus** (`check_ancestrais_divergentes`).
Se um documento afirma que o caput do art. 40 é da EC 41/2003 desde
2003-12-31 e outro o dá como da EC 20/1998 naquela data, um dos dois
transcreve cadeia que nunca esteve em vigor junta. A checagem lê só os
`componentes` dos documentos existentes — **não exige ancestral autorado**, o
que importa porque fragmentar a norma preventivamente é justamente o que esta
spec proíbe.

**Isso é curadoria manual, e é assim de propósito.** Nada monta a cadeia
sozinho: escolher a redação contemporânea de cada ancestral é leitura
jurídica, o mesmo princípio da autoria humana que vale para achados e para as
seções P13.1. O validador exige que o corpo exista e não seja vazio; que a
cadeia esteja certa é responsabilidade de quem a transcreveu, conferível
contra as `fontes` do próprio documento.

Um efeito prático: **decompor deixa de ser necessário para tornar legível.**
Um caput só vira documento próprio quando é ele que uma regra cita — não mais
para servir de contexto a um documento vizinho.

### O diretório é o dispositivo; os arquivos são as suas redações

```
cf88/art-40-par-1-inc-i/
├── ec-20-1998.md     # vigência 1998-12-16 → 2003-12-30
├── ec-41-2003.md     # vigência 2003-12-31 → 2019-11-12
└── ec-103-2019.md    # vigência 2019-11-13 → (em vigor)
```

Isso torna estrutural o que antes era convenção de nome: "todas as redações
deste dispositivo" é uma listagem de diretório, e acrescentar uma redação
posterior nunca renomeia a anterior.

O segmento de redação é **a chave da norma alteradora**, ou literalmente
`original`. Logo `redacao_dada_por` e o nome do arquivo são o mesmo dado,
conferido — não há como uma redação original declarar norma alteradora, nem
o contrário.

### `componentes` — o endereço estrutural

Lista **ordenada**, do nível mais externo para o mais interno. Cada entrada
tem `tipo` (enum fechado) e, quando o nível é numerado, `valor`; artigos e
parágrafos aceitam ainda `sufixo` (o `A` de "Art. 6º-A").

| `tipo`            | `valor`          | Exemplo | Slug        | Rótulo            |
| ----------------- | ---------------- | ------- | ----------- | ----------------- |
| `artigo`          | inteiro          | `40`    | `art-40`    | `art. 40`         |
| `caput`           | —                |         | `caput`     | `caput`           |
| `paragrafo`       | inteiro          | `1`     | `par-1`     | `§ 1º`            |
| `paragrafo_unico` | —                |         | `par-unico` | `parágrafo único` |
| `inciso`          | romano maiúsculo | `III`   | `inc-iii`   | `inciso III`      |
| `alinea`          | letra minúscula  | `a`     | `al-a`      | `alínea a`        |
| `item`            | inteiro          | `1`     | `item-1`    | `item 1`          |

O valor é **dado, não exibição**: `40`, nunca `"Art. 40"`. O sufixo é campo
separado, para que `6º-A` continue ordenável como `(6, "A")`.

**Todo nível carrega seu prefixo no slug** (`art-`/`par-`/`inc-`/`al-`/
`item-`), de modo que nenhuma leitura dependa de posição:
`art-1-inc-ii-al-a` diz o que cada parte é.

#### Aninhamento

Os níveis ocupam casas fixas: `artigo` (0), `paragrafo`/`paragrafo_unico`
(1), `caput` (2), `inciso` (3), `alinea` (4), `item` (5). Os componentes
devem aparecer em ordem **estritamente crescente** de casa; saltos são
permitidos e significativos:

- `art. 40, inciso I` → casas 0, 3 — um inciso **do caput**;
- `art. 40, § 1º, inciso I` → casas 0, 1, 3;
- `art. 40, § 1º, caput` → casas 0, 1, 2.

`caput` fica **abaixo** de `paragrafo`, não ao lado: "caput" nomeia o texto
de abertura da unidade que o contém, e este bundle tem tanto caput de artigo
quanto caput de parágrafo. Nada aninha dentro de um `caput`. Uma `alinea`
exige `inciso`; um `item` exige `alinea`.

#### Ordem

A chave de ordem tem **uma casa fixa por nível** — artigo, sufixo,
parágrafo, sufixo, inciso, alínea, item — com `0` significando "este nível
não faz parte do endereço". É esse zero que torna a ordem *legal* e não
apenas lexicográfica: um inciso do caput (casa do parágrafo em `0`) vem
antes do § 1º, que é como o artigo se lê. Uma chave por "profundidade"
colocaria, erradamente, todo parágrafo antes de todo inciso.

A comparação é numérica em toda parte, então § 2º precede § 14.

### `fontes`

Lista **não vazia de URLs http(s)**. Guardada exatamente como escrita — sem
normalização, sem coerção por tipo `HttpUrl` (que reescreveria a string e
quebraria o round-trip byte a byte do bundle). Um dispositivo pode ter mais
de uma fonte quando é conferível contra mais de uma publicação.

## Invariantes verificados

Estruturais, por documento (`validate_dispositivo`):

1. O caminho tem exatamente três segmentos, `<norma>/<endereço>/<redação>`.
2. `id` do frontmatter == caminho do arquivo.
3. Corpo não vazio (o texto exato do dispositivo).
4. Contrato Pydantic fechado — campo desconhecido é erro. Isso rejeita
   também os campos do schema antigo, então um documento não migrado falha
   alto em vez de validar com endereço vazio.
5. Aninhamento legal válido.
6. **Caminho ≡ f(frontmatter)**: `norma`, `slug_do_endereco(componentes)` e
   `redacao_dada_por` são recomputados e comparados com os três segmentos.
   O id não tem como divergir do documento que nomeia.
7. `vigencia_fim` não precede `vigencia_inicio`.

De vocabulário (P4), quando o registro de normas é passado:

8. `norma` resolve para um `norma.md` redigido.
9. `redacao_dada_por` idem, quando a redação não é a original.

Entre documentos (`check_vigencias`, código `P3_VIGENCIA_SOBREPOSTA`):

10. Duas redações do mesmo dispositivo **não podem estar em vigor ao mesmo
    tempo**. Um *buraco* entre redações **não** é violação: o P3 transcreve
    sob demanda, então um dispositivo pode legitimamente ter a redação da
    EC 41 e a da EC 103 sem a da EC 20 no meio.

## Histórico completo — quando o buraco vira prova

O buraco entre redações não é violação (invariante 10), mas ele é o que
impede afirmar que uma redação **não existe**. Falta a peça que fecha isso: a
vigência da **norma**, declarada no seu `norma.md`
(`vigencia_inicio`/`vigencia_fim`, ambos opcionais).

Com ela, `dispositivo_schema.historico_completo` deriva — não declara — se as
redações redigidas de um dispositivo **ladrilham** a vida inteira da norma:
começam com ela, se encadeiam sem buraco (fim de uma, dia seguinte é o início
da próxima) e terminam com ela. Se ladrilham, não sobra espaço para outra
redação, e uma citação que nomeia uma redação fora desse conjunto é
**provadamente falsa**, não pendente de transcrição.

É o que separa "ainda não transcrevi" de "nunca existiu" — situações que
pedem ações opostas. A distinção é **conclusão humana**, registrada em
achado (RFC 0008): nenhum detector a deriva, porque a segunda metade é uma
acusação de citação legal falsa, e acusação é ato de autoria.

O critério é intransigente na direção **segura**: uma redação sem data, uma
norma sem janela declarada ou um único dia de buraco e não há o que
concluir. Recusar-se a concluir é sempre a resposta certa aqui; concluir
errado põe uma acusação falsa no registro de uma regra. Por isso as cinco
redações da LCE 949/2017 redigidas sem `vigencia_inicio` — a lei entra em
vigor 180 dias após uma publicação cuja data não foi conferida — não
sustentam prova nenhuma até que essa data exista.

De ligação com as regras (`check_p3_dispositivos`, inalterado quanto ao
propósito): toda referência `dispositivos:` de uma regra resolve para um
dispositivo redigido, na forma canônica de link OKF
`/dispositivos/<norma>/<endereço>/<redação>.md`. A referência nomeia a
**redação**, não só o dispositivo — uma regra se funda no texto vigente para
a sua janela.

## O que um vínculo `dispositivos:` afirma

**"A fundamentação desta regra cita este dispositivo"** — não "esta regra se
funda juridicamente nele" (decisão 2026-07-27).

A afirmação fraca é a que a fonte sustenta e a que um check consegue
verificar. A forte é conclusão jurídica, alcançada regra a regra quando um
humano a move para `revisada`; não é derivável de prosa, e tratá-la como se
fosse poria no registro um rastro de auditoria falso — com aparência de
conferido.

Duas consequências práticas:

- **A granularidade do vínculo é a provisão, não a cláusula.** Quando a
  prosa estreita ("art. 40, § 1º, III, **segunda parte**"), o vínculo aponta
  para o inciso inteiro e a prosa continua carregando qual cláusula se
  aplica — é a divisão de trabalho do próprio P4. O que motiva: aquele
  inciso não tem alíneas, sua "segunda parte" é a cláusula "no âmbito dos
  Estados" do mesmo inciso, e transcrevê-la em separado inventaria uma
  unidade que a norma não tem. A resolução que o frontmatter deixa de
  carregar é **contada e exibida** (`com_qualificador`), nunca descartada
  em silêncio.
- **`dispositivos` não é material para o P2.** É anotação de auditoria, como
  `atos_validacao`: duas regras com a mesma fundamentação citam as mesmas
  provisões, então a única forma de divergirem é uma ter sido vinculada
  antes da outra. Tratá-la como material faria a igualdade material seguir o
  *progresso da auditoria* — um grupo P2 se desfaria no meio de um lote e se
  refaria no fim, invalidando os achados que o documentam sem que regra
  nenhuma tivesse mudado.

## O que continua não sendo verificado

- **Que uma regra tenha `dispositivos:` preenchido.** Continua sendo a
  quinta pergunta do P13.1, adiada no P7. A infraestrutura resolve qualquer
  referência declarada, mas `revisada` não exige que exista alguma.
- **Que o texto transcrito corresponda à fonte.** É ato humano de
  transcrição; o código verifica o contrato, nunca decide o texto ou o
  alcance de um dispositivo.
- **Que a cadeia de redações de um dispositivo seja completa.** Por desenho
  — ver o invariante 10.
- **Que a redação declarada para um nível seja a verdadeira.** O esquema
  garante coerência interna do corpus — os documentos não se contradizem
  sobre qual redação um nível tinha numa data —, nunca correspondência com a
  lei. Dizer que o caput do art. 40 é redação da EC 41/2003 desde 2003-12-31
  continua sendo conferência humana contra as `fontes`.
- **Que o corpo exiba o texto daquelas redações.** O validador não lê o
  corpo: um documento pode declarar componentes coerentes e transcrever outra
  coisa.

## Questões em aberto

1. **URN LexML como âncora de interoperabilidade.** Existe identificador
   nacional para dispositivo (LexML Brasil), e as normas deste corpus estão
   lá — p.ex.
   `urn:lex:br;rondonia:estadual:lei.complementar:2012-08-09;672`. Um campo
   opcional `lexml:` ancoraria cada norma no mesmo identificador que a fonte
   oficial usa. Não adotado nesta versão: só foi possível confirmar a URN de
   parte das normas, e um campo semipreenchido informa menos do que nenhum.
   A adoção deve vir com as 15 URNs conferidas de uma vez.
2. **Qual publicação é a fonte preferencial** quando há mais de uma (texto
   compilado vs. publicação original). Hoje ambas podem constar e a ordem da
   lista não significa precedência.
