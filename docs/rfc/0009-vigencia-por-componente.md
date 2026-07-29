# RFC 0009 — Vigência e redação como propriedades do componente

- **Status**: proposta (2026-07-29). Nada implementado. O esquema atual de
  `type: Dispositivo` continua valendo até que esta RFC seja aceita e
  aplicada.
- **Parte de / depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P3/P4) e a spec
  [`docs/spec/dispositivo.md`](../spec/dispositivo.md), cuja regra "os níveis
  acima entram na redação contemporânea a esta" esta RFC não altera — apenas
  torna **verificável** o que hoje é conferência humana silenciosa.
- **Não-objetivo**: alterar o corpo dos documentos (transcrição é ato
  humano); exigir decomposição preventiva de ancestrais; enforçar
  continuidade entre redações irmãs (a lacuna continua legítima, RFC 0001
  P3); tocar em `regra-*.md`, no CSV derivado ou em qualquer coluna do
  Sisprev.

## 1. O problema, com o caso que o revelou

Um `type: Dispositivo` é a unidade endereçada **com toda a cadeia que a
contém**: o corpo de um inciso traz o caput do artigo, o caput do parágrafo e
o inciso, todos na redação vigente **junto**. Disso decorre que alterar um
ancestral cria uma redação nova do dispositivo, ainda que o texto do nível
mais interno não mude uma vírgula.

O esquema atual não consegue registrar isso. Ele tem **um** `redacao_dada_por`
e **uma** vigência por documento, para um corpo que contém vários níveis, cada
um com sua própria história. Veja um documento real:

```yaml
id: cf88/art-40-par-1-inc-ii/ec-103-2019
redacao_dada_por: ec-103-2019
vigencia_inicio: 2019-11-13
fontes:
  - https://...emc103.htm
  - https://...emendaconstitucional-88-2015...
```

Três coisas erradas, e nenhuma detectável:

1. **`redacao_dada_por: ec-103-2019` é meia verdade.** A EC 103/2019 deu
   redação ao caput do art. 40 e ao caput do § 1º. O **inciso II** — o nível
   que o documento endereça — é redação da EC 88/2015.
2. **`vigencia_inicio: 2019-11-13` é uma interseção calculada à mão**, gravada
   como número nu. O raciocínio que a produziu não sobrevive no documento.
3. **`fontes` com duas URLs é o esquema vazando.** São duas porque os níveis
   vêm de normas diferentes; o campo não consegue dizer qual comprova qual.
   Quinze dos 115 documentos do bundle têm essa marca.

### O custo não é estético

Em 2026-07 uma varredura encontrou **quatro documentos** cuja vigência
atravessava a alteração de um ancestral — `art-40-par-1-inc-ii/ec-20-1998`,
`inc-iii-al-a/ec-20-1998`, `inc-iii-al-b/ec-20-1998` e `par-5/ec-20-1998`,
todos ignorando a EC 41/2003, mais `inc-ii/ec-88-2015` ignorando a EC
103/2019. Cada um monta um texto **que nunca esteve em vigor junto**.

E nada acusou: cada parágrafo do corpo é verbatim, o caminho confere,
`_check_caminho` passa, o vínculo resolve, e `check_vigencias` só compara
datas *dentro* de um diretório. O erro só apareceu porque um humano leu a lei.
Está registrado na spec, hoje, como limitação assumida.

**Os quatro erraram o `vigencia_fim`, nunca o `inicio`, e sempre no mesmo
sentido: estender demais.** É a assinatura de um erro de leitura específico —
tomar a linha de reticências da emenda por "esta emenda não alcança este
dispositivo" — e é o que esta RFC quer tornar inexprimível.

## 2. A proposta

Cada entrada de `componentes` passa a carregar a sua própria procedência:

```yaml
componentes:
  - tipo: artigo
    valor: '40'
    redacao_dada_por: ec-103-2019
    vigencia_inicio: 2019-11-13
  - tipo: paragrafo
    valor: '1'
    redacao_dada_por: ec-103-2019
    vigencia_inicio: 2019-11-13
  - tipo: inciso
    valor: II
    redacao_dada_por: ec-88-2015
    vigencia_inicio: 2015-05-08
    vigencia_fim: 2019-11-12
redacao_dada_por: ec-103-2019
vigencia_inicio: 2019-11-13
```

E o documento **mantém** os seus `redacao_dada_por`/`vigencia_inicio`/
`vigencia_fim`, autorados, agora conferidos contra a derivação:

| campo do documento | derivação                                                               |
| ------------------ | ----------------------------------------------------------------------- |
| `vigencia_inicio`  | **máximo** dos `vigencia_inicio` dos componentes                        |
| `vigencia_fim`     | **mínimo** dos `vigencia_fim` dos componentes (`None` = ainda em vigor) |
| `redacao_dada_por` | do componente que fixou o máximo                                        |

A leitura é direta: a combinação passa a existir quando o **último** nível
muda, e deixa de existir quando o **primeiro** deles muda de novo.

### Por que manter os campos no documento, e não só derivar

Porque **um campo derivado nunca discorda de nada, logo nunca acusa
ninguém**. A redundância só se paga quando é conferida — e é exatamente o
idioma que o bundle já usa: `_check_caminho` recomputa `norma`, o slug do
endereço e `redacao_dada_por` e os compara com os três segmentos do caminho,
"para que o id não tenha como divergir do documento que nomeia". Aqui vale o
mesmo: quem escreve a vigência do documento está declarando uma conclusão, e
quem escreve os componentes está declarando as premissas. Divergência é
achado, não detalhe de serialização.

Há ainda o leitor humano e o site, que passam a ver a janela efetiva sem ter
de calcular `max`/`min` de cabeça.

### O que isso torna impossível de escrever

`inc-ii/ec-20-1998` declarava `vigencia_fim: 2015-05-07`. Sob esta proposta o
componente `artigo 40` daquele documento declararia `vigencia_fim: 2003-12-30` — porque a EC 41/2003 reescreveu o caput — e o mínimo
contradiria o valor do documento. **O bug de 2026-07 deixa de compilar.**

## 3. Um invariante novo, e ele não exige ancestral autorado

> O mesmo componente não pode ter duas `redacao_dada_por` distintas vigentes
> na mesma data, em todo o corpus.

`P3_ANCESTRAL_DIVERGENTE`. Se `art-40-par-1-inc-i/ec-41-2003` afirma que o
caput do art. 40 é redação da EC 41/2003 desde 2003-12-31, nenhum outro
documento pode afirmar que o mesmo caput era redação da EC 20/1998 naquela
data. Os quatro casos de 2026-07 cairiam aqui, mecanicamente.

O ponto decisivo é que a checagem lê **só os `componentes`** dos documentos
que já existem. Não precisa que o caput do art. 40 seja um documento próprio —
o que importa, porque a decomposição é sob demanda e preventivamente
fragmentar a norma é justamente o que a spec proíbe. Uma tentativa anterior de
derivar a vigência a partir de *documentos ancestrais* foi descartada por
isso: nos 32 documentos da CF/88, **todos** têm ao menos um ancestral sem
documento próprio.

## 4. O que continua não verificado

- **Que a redação declarada para um componente seja a verdadeira.** Continua
  conferência humana contra a fonte. O esquema garante coerência interna do
  corpus, nunca correspondência com a lei.
- **Que o corpo exiba o texto daquelas redações.** O validador não lê o corpo;
  um documento pode declarar componentes coerentes e transcrever outra coisa.
- **Lacuna entre redações irmãs.** Continua legítima e não checada — `max`/
  `min` valem *dentro* de um documento, nunca entre vizinhos.

## 5. Migração

115 documentos. Duas populações bem distintas:

- **~100 de norma estadual**, com componente único ou cadeia que nunca teve
  ancestral alterado: migram **mecanicamente**, copiando os valores do
  documento para o único componente que os justifica.
- **~15 com cadeia mista** (os de `cf88/art-40`, mais os que hoje têm mais de
  uma fonte): exigem **conferência**, porque é neles que a informação hoje
  não existe — dizer qual norma deu redação a qual nível é precisamente o dado
  que o esquema atual perdeu.

Sugere-se aplicar em duas fases, com o esquema aceitando os campos de
componente como opcionais na primeira, para que a migração mecânica não fique
bloqueada pela conferência dos 15.

Código afetado: `dispositivo_schema.py`, `dispositivo_endereco.py`
(`Componente`, `_check_caminho`), `check_vigencias`, o port
`site/src/lib/dispositivo.ts`, `site/src/content.config.ts` e os testes de
`tests/test_dispositivo_schema.py`.

## 6. Alternativas descartadas

- **Só derivar, sem campo no documento.** Elimina a possibilidade de
  divergência, e com ela a possibilidade de detecção. Ver §2.
- **Derivar da vigência de documentos ancestrais.** Exigiria que todo
  ancestral fosse autorado — decomposição preventiva, contra a spec. Medido:
  0 dos 32 documentos da CF/88 satisfazem a condição hoje.
- **Um detector que compara os corpos** entre documentos irmãos procurando
  parágrafos ancestrais divergentes. Foi a heurística que *encontrou* os
  quatro casos, e funciona — mas depende de o ancestral aparecer em dois
  documentos irmãos com vigências sobrepostas, o que é acidente de cobertura,
  não invariante.
- **Fazer de `vigencia_fim` um derivado do irmão seguinte.** Mataria a lacuna
  legítima (RFC 0001 P3): a ausência de uma redação intermediária é
  informação, não erro.

## 7. Questão em aberto

**Se `fontes` deve descer para o componente.** O sintoma que a motivou é real
— 15 documentos com múltiplas fontes, uma por nível, sem dizer qual comprova
qual. Mas descer o campo obriga a repetir a mesma URL em vários componentes
quando uma só emenda alterou vários níveis, que é o caso comum. Uma
possibilidade é um `fonte:` **opcional** por componente, com a lista do
documento continuando a valer como união. Não decidido nesta RFC.
