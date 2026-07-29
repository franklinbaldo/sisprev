---
type: Achado
id: achado-0018
nome: Três regras de magistério carregam a fundamentação da gêmea não especial; o dispositivo que funda a especialidade é citado, mas nunca descrito
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0092.md
  - /regras/regra-0099.md
  - /regras/regra-0100.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0092`, `regra-0099` e `regra-0100` gravam `apos_especial: S` e trazem
"(Magistério)" no `nome`. Cada uma tem uma gêmea que grava `apos_especial: N`
— `regra-0091`, `regra-0097` e `regra-0098` — e com ela partilha uma
`fundamentacao_integral` **idêntica byte a byte** e a **mesma** lista de
`dispositivos:`.

O texto que as três entregam não contém as palavras "professor" nem
"magistério". **A única coisa em todo o registro que diz que a regra é de
magistério é o `nome`.**

Este achado nasceu de um item de candidatura que dizia outra coisa: que nas
três o `apos_especial: S` **não tem dispositivo que o funde**. Conferido
contra fonte oficial, **isso é falso** — o artigo que cada uma cita tem um
§ 4º que é exatamente a regra do magistério. A refutação está em
"O que este achado não alcança"; o que sobra, e é o que aqui se registra, é
mais estreito e é sobre o texto deployável.

# Evidências

## As três duplas, conferidas campo a campo

Comparado o frontmatter inteiro de cada par (só `id` e `row_index` excluídos):

| par             | campos materiais que divergem | `fundamentacao_integral`      |
| --------------- | ----------------------------- | ----------------------------- |
| `0091` × `0092` | `apos_especial`, `simulavel`  | sha256 `ada6a9ea33f6…`, 422 c |
| `0097` × `0099` | `apos_especial`               | sha256 `02a9e757977d…`, 489 c |
| `0098` × `0100` | `apos_especial`               | sha256 `02a9e757977d…`, 489 c |

A `fundamentacao_integral` é a mesma string nas quatro regras da família da
EC 41 (`0097`, `0098`, `0099`, `0100`) e a mesma string nas duas da família da
EC 20 (`0091`, `0092`). O `dispositivos:` de cada par é idêntico item a item.

**Uma correção ao relatório de apoio, e ela é minha ao recontar.** A
[reconferência dos blocos 4 e 5](../../../docs/analysis/reconferencia-blocos-4-e-5.md)
§2.2 descreve `0091` × `0092` como distintas pelo `nome`. Não é só isso:
divergem também em `simulavel` (`S` na `0091`, `N` na `0092`). O `nome`
continua sendo o único lugar onde a **especialidade** aparece — mas o par não
é "o mesmo documento com o rótulo trocado".

## O § 4º existe, é citado, e não está transcrito

`regra-0099`/`0100` citam "artigo 2º da Emenda Constitucional nº 41/2003" e
vinculam `ec-41-2003/art-2/original`. `regra-0092` cita "artigo 8º da Emenda
Constitucional nº 20/1998" e vincula `ec-20-1998/art-8/original`. Os dois
documentos endereçam o **artigo inteiro** (`componentes: [artigo 2]`,
`[artigo 8]`) e transcrevem **só até o caput**, que termina em "quando o
servidor, cumulativamente:".

Lidos nas publicações originais (fontes ao fim desta seção), os dois artigos
têm um § 4º, e ele é a provisão do magistério:

> **EC 41/2003, art. 2º, § 4º** — O professor, servidor da União, dos
> Estados, do Distrito Federal e dos Municípios, incluídas suas autarquias e
> fundações, que, até a data de publicação da Emenda Constitucional nº 20, de
> 15 de dezembro de 1998, tenha ingressado, regularmente, em cargo efetivo de
> magistério e que opte por aposentar-se na forma do disposto no caput, terá
> o tempo de serviço exercido até a publicação daquela Emenda contado com o
> acréscimo de dezessete por cento, se homem, e de vinte por cento, se
> mulher, desde que se aposente, exclusivamente, com tempo de efetivo
> exercício nas funções de magistério, observado o disposto no § 1º.

> **EC 20/1998, art. 8º, § 4º** — O professor, servidor da União, dos
> Estados, do Distrito Federal e dos Municípios, incluídas suas autarquias e
> fundações, que, até a data da publicação desta Emenda, tenha ingressado,
> regularmente, em cargo efetivo de magistério e que opte por aposentar-se na
> forma do disposto no caput, terá o tempo de serviço exercido até a
> publicação desta Emenda contado com o acréscimo de dezessete por cento, se
> homem, e de vinte por cento, se mulher, desde que se aposente,
> exclusivamente, com tempo de efetivo exercício das funções de magistério.

Duas consequências, e elas puxam em direções opostas:

1. **O `apos_especial: S` está fundado.** O § 4º está dentro do artigo que a
   regra cita e vincula, e descreve tratamento próprio do professor —
   acréscimo de tempo de serviço, condicionado a exercício exclusivo em
   magistério. É aferição a mais, logo é regra distinta da gêmea, exatamente
   no sentido de ["o que individua uma regra"](../../../docs/spec/regra.md).
   Nenhum vínculo novo é proposto aqui, e nenhum é necessário: o § 4º já está
   no dispositivo vinculado.
2. **Nada disso chega ao texto entregue.** A `fundamentacao_integral` das
   três é a da gêmea não especial. O § 4º não é nomeado, o acréscimo de
   17%/20% não é mencionado, e a condição de exercício exclusivo — que é o
   requisito mais restritivo da hipótese — não aparece.

**De onde veio a acusação errada.** A triagem que a produziu procurou palavras
de especialidade no **texto transcrito** dos dispositivos vinculados. Como os
dois artigos param no caput, ela não achou nada e leu isso como "não há
fundamento". É o mesmo modo de falha que a §2.3 daquela reconferência já
tinha identificado nos arts. 34 e 35 da LCE 1.100/2021 e classificado como
fila `TRANSCREVER` — só que ali foi aplicado, e na primeira metade do item
não foi.

**Fontes conferidas.** EC 20/1998: cópia local
`fontes-oficiais/arquivos/camara-emendaconstitucional-20-15-dezembro-1998-356870-publicacaooriginal-1-pl.html`
(sha256 `8285869f…`, já no `manifesto.yaml`). EC 41/2003:
`https://www2.camara.leg.br/legin/fed/emecon/2003/emendaconstitucional-41-19-dezembro-2003-497025-publicacaooriginal-1-pl.html`
(sha256 `161a613e403a33a92d62e8a377ba8389890384d4c78353169c189182e03fd05e`) —
a mesma URL que `ec-41-2003/norma.md` já declara em `fontes`, **baixada nesta
sessão e não arquivada**: `fontes-oficiais/arquivos/` não a contém, e
acrescentá-la é trabalho do coletor (`scripts/arquivo_de_fontes.py`), não
deste achado. Quem reconferir deve baixar a URL de novo e comparar o hash.

As duas são **publicação original**. O texto compilado do Planalto continua
inacessível (HTTP `000`), então não confiro se esses §§ 4º sofreram alteração
posterior — ver "O que este achado não alcança".

## O catálogo sabe escrever isto, e escreve, noutro par

`regra-0103` e `regra-0104` são o par de magistério da família do art. 6º da
EC 41/2003. A `fundamentacao_integral` delas **começa** por "Aposentadoria
especial de professor", e elas vinculam três dispositivos a mais que as
gêmeas não especiais `0101`/`0102` (`lce-432-2008/art-24`, `art-46`,
`art-63`). O mesmo catálogo, a mesma norma-mãe, o mesmo tipo de par: ali a
especialidade chegou ao texto e ao vínculo. Nas três deste achado, não.

## O que os detectores veem, e não é isto

Rodados os detectores nesta árvore (79 detecções, nenhuma violação):
`regra-0092` aparece em `P9_CAMPOS_VAZIOS_PENDENTES` (`sexo` e `integral`
vazios — já coberto pelo `achado-0008`) e `regra-0099`/`0100` aparecem juntas
em `P1_NOME_REPETIDO`, por terem o mesmo `nome` entre si. **Nenhuma detecção
alcança o que este achado registra**, e por isso ele é `verificacao: manual`:
a chave material do P2 inclui `apos_especial`, então um par que difere nesse
campo é, para o detector, legitimamente distinto — que é justamente a leitura
certa. O defeito está no campo de texto, que nenhum detector lê.

# Consequência prática

`FUNDAMENTACAO_INTEGRAL` é o texto que o Sisprev entrega no documento do
servidor. Quem se aposenta pela `regra-0092`, `regra-0099` ou `regra-0100`
recebe uma fundamentação **indistinguível** da que recebe quem se aposenta
pela gêmea comum: mesma norma, mesmos artigos, mesma redação, nenhuma menção
ao magistério.

O documento, portanto, não registra que o benefício foi concedido na hipótese
especial, nem que dela decorre a condição de exercício exclusivo em funções de
magistério. Para quem confere a concessão depois — controle interno, PGE,
Tribunal de Contas — a única evidência de que a hipótese aplicada foi a do
§ 4º é o `nome` da regra, que não vai no texto.

`regra-0092` é `simulavel: N`, e aí o risco muda de natureza: a regra é
escolhida por um humano lendo a fundamentação, e a fundamentação que ele lê é
a mesma da `regra-0091`, que é `simulavel: S`. As duas hipóteses que precisam
ser distinguidas na triagem carregam o mesmo texto.

**Nada aqui afirma o que o motor faz.** `regra-0099`/`0100` são
`simulavel: S`, e em regra simulável o motor não lê a fundamentação. Se
`apos_especial` é critério aferido ou controle de apresentação é a Q9, aberta.
O acréscimo de 17%/20% e a exclusividade do exercício em magistério **não têm
coluna** no cadastro — o que se prova é sobre o registro e o documento
entregue, não sobre o cálculo.

# O que este achado não alcança

**Não alcança nenhum dos quatro subgrupos especiais do regime novo.** O item
de candidatura afirmava que em "três dos quatro" o critério definidor da
especialidade não teria dispositivo citado. Conferido subgrupo a subgrupo,
**em quatro de quatro** ele está citado nominalmente na fundamentação **e**
vinculado em `dispositivos:`:

| subgrupo        | regras                             | dispositivo citado e vinculado |
| --------------- | ---------------------------------- | ------------------------------ |
| magistério      | 0041, 0042, 0095, 0096, 0107, 0108 | `lce-1100-2021/art-33`         |
| policial        | 0080, 0081, 0082, 0083             | `lce-1100-2021/art-34`         |
| deficiência     | 0033, 0034, 0059–0064              | `lce-1100-2021/art-35`         |
| agentes nocivos | 0065, 0066, 0067, 0071             | `lce-1100-2021/art-41-inc-iii` |

Os quatro textos foram lidos no corpus e conferidos contra a compilação
oficial (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`): o art. 33
nomeia "O professor"; o art. 34, "O policial civil, o policial legislativo e o
ocupante de cargo de policial penal ou de agente de segurança socioeducativo";
o art. 35, "O servidor público com deficiência"; o art. 41, III, "efetiva
exposição a agentes nocivos". **Zero subgrupos entram neste achado.** (A
tabela acrescenta `0033`/`0034` ao subgrupo da deficiência, que a
reconferência listava só como `0059`–`0064`: as duas também vinculam o
art. 35.)

**Não se afirma que `apos_especial: S` esteja errado nas três.** O § 4º
sustenta a especialidade; a hipótese de que o campo é que sobra não está em
jogo aqui.

**Não se propõe vínculo nem transcrição.** O § 4º está dentro do dispositivo
já vinculado; transcrevê-lo é ato autoral separado, e reescrever
`FUNDAMENTACAO*` é alterar campo deployável.

**Não se confirma a vigência atual dos dois §§ 4º.** As duas leituras são de
publicação original; o texto compilado do Planalto está inacessível. Se algum
deles foi alterado ou revogado depois, este achado não sabe.

# Questão a investigar

1. **Se a fundamentação das três deve nomear o § 4º.** A leitura mais simples
   é que sim — o texto entregue deveria descrever a hipótese efetivamente
   aplicada, incluindo a condição de exercício exclusivo em magistério. Mas
   `FUNDAMENTACAO*` é campo **deployável**, e reescrevê-lo é decisão de quem
   responde pelo produto, não conclusão de auditoria. Este achado registra a
   lacuna; não propõe a redação.

2. **A vigência do art. 8º da EC 20/1998, que a `regra-0092` cita.** A
   publicação original da EC 41/2003 traz, verbatim: "Art. 10. Revogam-se o
   inciso IX do § 3º do art. 142 da Constituição Federal, bem como os arts. 8º
   e 10 da Emenda Constitucional nº 20, de 15 de dezembro de 1998", e o seu
   art. 11 a faz vigorar na data da publicação — 31/12/2003, que é o que
   `ec-41-2003/norma.md` já declara em `vigencia_inicio`. O documento
   `ec-20-1998/art-8/original` **não declara janela nenhuma**.
   **Isto não acusa a citação da `regra-0092`**: ela grava
   `data_direito_ate: 31/12/2003`, e o `ATE` é inclusivo
   ([`docs/spec/regra.md`](../../../docs/spec/regra.md), "Elegibilidade
   temporal") — a janela fecha exatamente no dia em que a norma revogadora
   entrou em vigor, que é o comportamento esperado de uma regra de transição
   preservada por direito adquirido. O que fica pendente é o **corpus**:
   datar a redação exige afirmar o fim da vigência, e para isso o texto
   compilado é a base mínima (ver `fontes-oficiais/PENDENCIAS.md`, item 3).

3. **Se `apos_especial` é critério aferido ou controle de apresentação (Q9).**
   Muda o que a divergência entre gêmeas significa: se é aferido, as três são
   regras legitimamente distintas com texto insuficiente; se é apresentação, a
   pergunta passa a ser por que existem seis regras onde poderiam existir
   três. A `regra-0092` ser `simulavel: N` enquanto a `regra-0091` é
   `simulavel: S` sugere a primeira leitura, mas sugerir não é responder.
