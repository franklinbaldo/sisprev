# Cadeia de vigência dos dispositivos — varredura do defeito "vigência que atravessa alteração de ancestral"

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial** e **não é achado**. Não edita nenhuma `regra-*.md` nem
> `achado-*.md`, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. Edita **apenas**
> `okf/dispositivos/`, e só onde o texto oficial foi conferido — três
> `vigencia_fim` corrigidos e três redações autoradas, todos listados na
> seção 3. Toda conclusão sobre citação de regra continua sendo ato humano,
> em achado próprio.

## 1. O defeito procurado

[`docs/spec/dispositivo.md`](../spec/dispositivo.md), seção "O corpo é a
cadeia legível até o dispositivo": um `type: Dispositivo` é a unidade
endereçada **com toda a cadeia que a contém**, e os níveis acima entram na
redação contemporânea a esta. A consequência é que **alterar um ancestral
cria uma redação nova do dispositivo** — o texto do inciso não mudou, mas o
dispositivo mudou —, e portanto **a vida de uma redação termina na primeira
alteração de qualquer nível da sua cadeia**, não só do nível mais interno.

Um documento cuja vigência atravessa a alteração de um ancestral está
errado, e o erro é silencioso: cada metade do corpo é verbatim, e nenhum
invariante do bundle o detecta (`check_vigencias` só proíbe duas redações do
**mesmo** dispositivo em vigor ao mesmo tempo).

O caso-gabarito já tratado fora desta varredura:
`cf88/art-40-par-1-inc-ii/ec-20-1998` declarava 1998-12-16 → 2015-05-07,
atravessando a EC 41/2003, que reescreveu o caput do § 1º ("na forma do § 3º"
→ "na forma dos §§ 3º e 17"). Foi corrigido para terminar em 2003-12-30, com
`inc-ii/ec-41-2003` autorado no intervalo restante.

## 2. Método e cobertura

Varridos **os 112 documentos `type: Dispositivo`** de `okf/dispositivos/`
(15 normas com dispositivo redigido, 17 `norma.md` no total).

Duas pistas, nesta ordem:

1. **Pista estrutural, mecânica (a).** Para cada par de documentos da mesma
   norma cujos `componentes` compartilham prefixo (logo compartilham
   ancestral) e cujas vigências declaradas se sobrepõem, comparar os
   parágrafos do corpo correspondentes aos níveis ancestrais. Texto diferente
   com vigências sobrepostas = um dos dois está errado. Rodada por script
   descartável sobre `dispositivo_schema.load_dispositivos`, não incorporada
   ao repositório — a decisão da RFC 0008 §5 é que essa conferência é humana,
   e transformá-la em detector emitiria acusação derivada.
2. **Pista documental (b).** Para as normas em que a pista (a) não podia
   acusar nada (ancestral sem irmão redigido, ou irmão na mesma janela),
   leitura direta da publicação oficial, artigo a artigo, procurando "Redação
   dada" no **caput** de cada nível ancestral.

Legenda dos marcadores: **[V]** texto conferido na fonte oficial;
**[V parcial]** conferido em parte, com a lacuna dita; **[R]** inferido da
estrutura do bundle, sem conferência de fonte.

### Fontes efetivamente abertas

- **[V]** CF/88 texto original — cópia local
  (`fontes-oficiais/arquivos/camara-constituicao-1988-...html`, Câmara/LEGIN).
- **[V]** EC 20/1998 — cópia local (Câmara/LEGIN).
- **[V]** EC 41/2003 — Câmara/LEGIN, baixada nesta sessão
  ([publicação original](https://www2.camara.leg.br/legin/fed/emecon/2003/emendaconstitucional-41-19-dezembro-2003-497025-publicacaooriginal-1-pl.html)).
- **[V]** EC 47/2005 — Câmara/LEGIN, baixada nesta sessão
  ([publicação original](https://www2.camara.leg.br/legin/fed/emecon/2005/emendaconstitucional-47-5-julho-2005-537717-publicacaooriginal-30462-pl.html)).
- **[V]** EC 88/2015 — cópia local (Câmara/LEGIN).
- **[V]** EC 103/2019 — Câmara/LEGIN, baixada nesta sessão
  ([publicação original](https://www2.camara.leg.br/legin/fed/emecon/2019/emendaconstitucional-103-12-novembro-2019-789412-publicacaooriginal-159409-pl.html)).
- **[V]** LCE 432/2008 compilada e revogada — cópia local (DITEL/Casa Civil,
  PDF + `.txt`), com a ficha SAPL da norma (`fontes-oficiais/arquivos/sapl-4011`).
- **[V]** LCE 1.100/2021 compilada — cópia local (DITEL/Casa Civil), mais
  LC 1.162/2022 e LC 1.181/2023 baixadas do SAPL/ALE-RO nesta sessão (ver
  §4.3).
- **[V parcial]** ECE 146/2021 — ficha SAPL da norma consultada nesta sessão
  (`/norma/9906`): sem "Data Fim Vigência" e com "Normas Relacionadas"
  **vazia**. O texto da emenda está em cópia local; o que não foi conferido
  é a *inexistência* de emenda posterior por outra via que não o registro do
  SAPL.
- **Planalto fora do ar** durante toda a sessão. Nenhuma conferência depende
  dele; as URLs do Planalto que já constavam em `fontes:` foram mantidas e
  acompanhadas das URLs da Câmara efetivamente abertas.

## 3. O que estava errado, e o que foi feito

Três documentos, todos em `cf88`, todos pelo mesmo motivo: a **EC 41/2003
reescreveu o caput do art. 40** ("de caráter contributivo" → "de caráter
contributivo e solidário, mediante contribuição do respectivo ente público,
dos servidores ativos e inativos e dos pensionistas") **e o caput do § 1º**,
e nenhum dos três havia quebrado em 2003-12-30/2003-12-31.

**[V]** A base da conferência é o art. 1º da EC 41/2003: ele reproduz o caput
do art. 40, o caput do § 1º e o inciso I, e usa **linha de reticências** onde
não reescreve — os incisos II e III (e as alíneas do III) e os §§ 4º, 5º e 6º
ficam sob reticências. É exatamente a técnica que a spec descreve: "este
texto não mudou", **não** "esta emenda não alcança este dispositivo".

| documento                                   | vigência declarada      | data de alteração do ancestral atravessada | ancestral alterado                          |
| ------------------------------------------- | ----------------------- | ------------------------------------------ | ------------------------------------------- |
| `cf88/art-40-par-1-inc-iii-al-a/ec-20-1998` | 1998-12-16 → 2019-11-12 | 2003-12-31                                 | art. 40 caput **e** § 1º caput (EC 41/2003) |
| `cf88/art-40-par-1-inc-iii-al-b/ec-20-1998` | 1998-12-16 → 2019-11-12 | 2003-12-31                                 | art. 40 caput **e** § 1º caput (EC 41/2003) |
| `cf88/art-40-par-5/ec-20-1998`              | 1998-12-16 → 2019-11-12 | 2003-12-31                                 | art. 40 caput (EC 41/2003)                  |

Correções aplicadas — em cada um dos três diretórios, `vigencia_fim` passou a
**2003-12-30** e foi autorada a redação `ec-41-2003.md` cobrindo
**2003-12-31 → 2019-11-12**:

- `cf88/art-40-par-1-inc-iii-al-a/ec-41-2003.md` (novo)
- `cf88/art-40-par-1-inc-iii-al-b/ec-41-2003.md` (novo)
- `cf88/art-40-par-5/ec-41-2003.md` (novo)

Composição do corpo dos três novos documentos, e a fonte de cada linha:

- caput do art. 40 e caput do § 1º na redação da **EC 41/2003** — **[V]**
  transcritos da publicação original da Câmara;
- inciso III, alíneas *a* e *b*, e § 5º na redação da **EC 20/1998** — **[V]**
  transcritos da publicação original da Câmara (cópia local), texto idêntico
  ao que os documentos `ec-20-1998` vizinhos já traziam;
- fim em **2019-11-12** — **[V]** a EC 103/2019 reescreveu o caput do art. 40,
  o caput do § 1º, o inciso I, o inciso III e o § 5º, e entrou em vigor na
  data da publicação (DOU de 13/11/2019, art. 36, III).

**[V]** Que nada mais mexeu nesses ancestrais entre 2003 e 2019: a EC 47/2005
reescreve, no art. 40, apenas o § 4º e acrescenta o § 21 (o caput e o § 1º
ficam sob reticências); a EC 88/2015 alcança só o § 1º, II.

Ressalva tipográfica, registrada por honestidade: o § 5º nos documentos
`ec-20-1998` do bundle grafa `§ 1º, III, "a"` (com aspas, como no texto
compilado do Planalto), enquanto a publicação original da Câmara imprime
`§ 1º, III, a,` sem aspas. O novo `art-40-par-5/ec-41-2003.md` repete a
grafia do documento irmão de propósito — assim as duas redações diferem
**apenas** onde a lei difere. Não é diferença normativa.

## 4. O que foi varrido e está limpo

### 4.1 `cf88` — art. 40, demais documentos — **[V]**

Verificados contra CF/88 original, EC 20/1998, EC 41/2003, EC 47/2005,
EC 88/2015 e EC 103/2019: nenhuma outra vigência declarada atravessa
alteração de ancestral.

- `art-40-inc-i/original` (1988-10-05 → 1998-12-15): o caput do art. 40 na
  redação originária ("Art. 40. O servidor será aposentado:") vigeu até a
  EC 20/1998. **[R]** quanto às emendas de 1988-1998 que não foram abertas
  (EC 3/1993 alcança o art. 40, mas no § 6º) — a fonte dessa exclusão não foi
  conferida nesta sessão.
- `art-40-par-5/original` (1988-10-05 → 1998-12-15), `art-40-par-7/ec-20-1998`
  (1998-12-16 → 2003-12-30), `art-40-par-8/ec-41-2003` (2003-12-31 →
  2019-11-12), `art-40-par-1-inc-i/*`, `art-40-par-5/ec-103-2019`,
  `art-40-par-7/ec-103-2019`, `art-40-par-1-inc-iii/ec-103-2019`: todos com
  fronteiras coincidindo com alterações do próprio nível **e** dos
  ancestrais.

### 4.2 `lce-432-2008` — 28 documentos — **[V]**

Conferidos artigo a artigo contra a compilação oficial DITEL/Casa Civil
(cópia local, `.txt` grepável), que é a `fonte:` declarada nos próprios
documentos. Os caputs que servem de ancestral aos documentos do bundle —
arts. 10, 17, 20, 21, 24, 28, 30, 31, 32, 38, 39, 45, 46, 62 e 63 — **não
receberam nova redação** de nenhuma das 14 leis alteradoras. Consequência: os
`art-20-par-*`, `art-21-par-1`, `art-28-inc-i`, `art-30-inc-ii`,
`art-31-par-*`, `art-32-*` seguem legíveis sob um único caput durante toda a
janela declarada.

Duas observações que **não** são o defeito procurado, registradas para quem
continuar:

- **Art. 34 mudou de caput duas vezes** (LC 504/2009 e LC 949/2017). Os dois
  documentos que dependem dele — `art-34-inc-i/lce-949-2017` e
  `art-34-par-2/lce-949-2017` — trazem o caput da LC 949 e portanto estão
  **coerentes**; mas ambos estão **sem `vigencia_inicio`**, então nada
  atravessa nada e nada se prova. Ver §5.
- **Divergência de data entre fontes.** O SAPL registra a LC 949 como "de 18
  de julho de 2017" e a LC 504 como "de 28 de abril de 2009"; a compilação
  DITEL imprime 17/07/2017 e 29/04/2009. Nenhum documento do bundle depende
  hoje dessas datas (todos os afetados estão sem `vigencia_inicio`), mas
  **qualquer preenchimento futuro precisa decidir a divergência contra a
  publicação no DOE**, não escolher a fonte mais à mão.

### 4.3 `lce-1100-2021` — 27 documentos — **[V]**

Todos `original`, 2021-10-18 → (em vigor). Os ancestrais em jogo são os
caputs dos arts. 27, 30, 41, 46, 47 e 51. Conferido:

- compilação DITEL/Casa Civil (cópia local), que declara no cabeçalho as
  alterações da LC 1.111/2021, da LC 1.125/2021 e do Decreto 26.859/2022 —
  nenhuma delas toca os arts. 24-51 (alcançam os arts. 8º, 61, 77, 86, 112 e
  115);
- **a compilação local está desatualizada**, e a ficha SAPL da LC 1.100
  (`/norma/9979`) registra mais duas normas: **LC 1.162/2022** e
  **LC 1.181/2023**. Ambas foram baixadas e lidas nesta sessão:
  - LC 1.162/2022 altera o **§ 11 do art. 30** e acresce §§ 11-A e 11-B e os
    arts. 112-A/112-B — o **caput do art. 30 fica sob reticências**, logo os
    seis documentos `art-30-*` do bundle não são alcançados;
  - LC 1.181/2023 acresce o art. 112-C, substitui o Anexo I e revoga o
    art. 94, XI e o Anexo II — nada nos arts. 24-51.

A base da completude aqui é a lista "Normas Relacionadas" do SAPL. Se ela
estiver incompleta, a conclusão desta subseção cai junto; não há como fechar
isso sem uma segunda fonte de compilação atualizada.

### 4.4 `ece-146-2021` — 15 documentos — **[V parcial]**

Todos `original`, 2021-09-14 → (em vigor), com ancestrais internos à própria
emenda (caputs dos arts. 5º a 8º e dos §§ 6º, 7º, 2º e 3º). A pista (a) não
acusa divergência: os 15 corpos exibem os mesmos ancestrais com o mesmo
texto. A ficha SAPL (`/norma/9906`) confirma publicação em 14/09/2021, não
registra fim de vigência e traz "Normas Relacionadas" vazia — **nenhuma
emenda posterior registrada**. O que falta para virar **[V]**: conferir a
inexistência de emenda posterior fora do registro do SAPL.

### 4.5 Documentos imunes por construção — **[R]**

`ec-41-2003/art-6a/ec-70-2012` (2012-03-30 → em vigor) endereça um artigo:
não tem ancestral, então não há cadeia que possa mudar sob ele. Mesma
situação para os demais documentos de nível `artigo` sem componentes acima.

## 5. O que ficou sem conclusão

### 5.1 `cf88/art-40-par-1-inc-ii/ec-88-2015` — o mesmo defeito, na fronteira de 2019 — **[V]**

**Não editado por instrução explícita da tarefa** (o diretório `inc-ii/` já
havia sido tratado noutra frente). Registrado aqui porque a varredura o
encontrou e a fonte o sustenta:

O documento declara `vigencia_inicio: 2015-05-08` e **nenhum
`vigencia_fim`** — isto é, afirma estar em vigor hoje. Mas a **EC 103/2019
reescreveu o caput do art. 40 e o caput do § 1º** (o inciso II fica sob
reticências, logo seu texto continua o da EC 88/2015, mas o **dispositivo**
mudou). Pela regra da spec, essa redação deveria terminar em **2019-11-12**,
com uma redação `ec-103-2019` cobrindo dali em diante.

É o único par que a pista mecânica (a) ainda acusa depois das correções da
§3: o corpo de `inc-ii/ec-88-2015` exibe o art. 40 na redação da EC 41/2003
enquanto `art-40-par-1-inc-i/ec-103-2019`, `art-40-par-1-inc-iii/ec-103-2019`,
`art-40-par-5/ec-103-2019` e `art-40-par-7/ec-103-2019` exibem o mesmo artigo
na redação da EC 103/2019, todos com vigências que se sobrepõem à dele.

### 5.2 Vigência dos artigos de emenda revogados pela EC 103/2019 — **[V]** no texto, **aberto** na conclusão

**[V]** O art. 35 da EC 103/2019 revoga expressamente "os arts. 2º, 6º e 6º-A
da Emenda Constitucional nº 41" e "o art. 3º da Emenda Constitucional nº 47".
O bundle tem os quatro documentos: `ec-41-2003/art-2/original`,
`ec-41-2003/art-6/original`, `ec-41-2003/art-6a/ec-70-2012`,
`ec-47-2005/art-3/original` (e `art-3-par-unico`).

**Por que não fechei.** O art. 36, II da EC 103/2019 condiciona essas
revogações, **para os regimes próprios dos Estados**, à "data de publicação
de lei de iniciativa privativa do respectivo Poder Executivo que as referende
integralmente". A data de fim de vigência desses artigos **em Rondônia** é,
portanto, a de uma lei estadual de referendo — qual seja, e se a LCE
1.100/2021 cumpre esse papel, é conclusão jurídica que esta varredura não
tem base para tomar e que muda o alcance de várias regras de transição.
Fica como pendência autoral.

Vale notar que três dos quatro estão **sem `vigencia_inicio` e sem
`vigencia_fim`**, então hoje nada atravessa nada — o problema não é o
defeito desta varredura, é ausência de janela.

### 5.3 Trinta e dois documentos sem janela declarada — **[R]**

A varredura **não pode acusar nem inocentar** um documento sem
`vigencia_inicio`: não há intervalo que possa conter uma data de alteração.
Onde a coerência textual pôde ser lida (art. 34 da LCE 432, §§ 7º do art. 40
da CF/88), a cadeia está correta; o que falta é a data.

Sem `vigencia_inicio` **e** sem `vigencia_fim` (16): `cf88/art-40-caput/original`,
`cf88/art-40-inc-ii/original`, `cf88/art-40-inc-iii-al-a|b|c|d/original`,
`cf88/art-40-par-1-caput/ec-103-2019`, `cf88/art-40-par-4a|4b|4c/ec-103-2019`,
`cf88/art-40-par-7-caput/ec-41-2003`, `cf88/art-40-par-7-inc-i|ii/ec-41-2003`,
`ec-20-1998/art-8/original`, `ec-41-2003/art-2|6|7/original`,
`ec-47-2005/art-3/original`, `ec-47-2005/art-3-par-unico/original`,
`lc-152-2015/art-2/original`, `lc-51-1985/art-1/lc-144-2014`,
`lc-51-1985/art-1-inc-ii/lc-144-2014`,
`lc-51-1985/art-1-inc-ii-al-a|b/lc-144-2014`,
`lei-10887-2004/art-1/original`.

Sem `vigencia_inicio`, com `vigencia_fim` (8, todos `lce-432-2008`):
`art-10-inc-i/lce-949-2017`, `art-31-par-1|2/lce-504-2009`,
`art-32-inc-ii-al-a/lce-949-2017`, `art-32-par-1/lce-949-2017`,
`art-33/lce-949-2017`, `art-34-inc-i/lce-949-2017`,
`art-34-par-2/lce-949-2017`.

Nota da spec que se aplica inteira aqui: uma redação sem data não sustenta
prova nenhuma — nem a de `historico_completo`, nem a desta varredura.

## 6. O defeito é isolado ou sistemático?

**Sistemático em origem, concentrado em alcance.** Todas as quatro
ocorrências (as três corrigidas na §3 mais a da §5.1, e a que já havia sido
corrigida antes desta varredura) são o **mesmo erro de leitura**: tratar a
linha de reticências da emenda como "esta emenda não alcança este
dispositivo", quando ela significa "este texto não mudou". Não é distração de
digitação — é a interpretação que a spec teve de explicitar, e ela erra
sempre no mesmo sentido: **estender demais** a vigência.

Concentrado, porém, em `cf88/art-40`, e por um motivo verificável: é o único
dispositivo do corpus cujos ancestrais foram reescritos **três vezes**
(EC 20/1998, EC 41/2003, EC 103/2019) enquanto níveis internos ficavam
intactos. Nas normas estaduais o padrão não se repete — as leis alteradoras
da LCE 432 e da LCE 1.100 reescrevem incisos, parágrafos e alíneas, quase
nunca o caput que os contém, e as três vezes em que o caput mudou (art. 34 da
LCE 432, duas vezes; art. 45, uma) o bundle já as tinha separadas em arquivos
distintos.

Duas consequências práticas:

1. **A varredura não fica pronta.** Enquanto 32 documentos estiverem sem
   janela declarada, o mesmo defeito pode entrar em qualquer um deles no dia
   em que a data for preenchida. O momento de conferir a cadeia é o momento
   de escrever a data.
2. **Nada disto é gate.** A pista (a) é mecânica e barata, mas o que ela
   acusa é sempre "um dos dois está errado" — dizer **qual** exige abrir a
   emenda. Transformá-la em detector emitiria, na melhor hipótese, um par de
   ids e, na pior, uma acusação derivada sobre vigência legal. É a mesma
   razão pela qual o leitor de citações por regex foi removido (RFC 0008).

## Pós-escrito — a RFC 0009 fechou a pista mecânica, e o que sobrou

Este relatório concluía que a pista mecânica não devia virar gate porque
"acusa sempre *um dos dois está errado*, e dizer qual exige abrir a emenda".
Continua verdade sobre a **pista** — comparar os corpos entre irmãos —, mas a
[RFC 0009](../rfc/0009-vigencia-por-componente.md) deu outro caminho: cada
componente passou a declarar a sua própria redação e janela, e
`check_ancestrais_divergentes` compara *declarações*, não textos. A conclusão
"o defeito não é detectável" caducou; a de que **dizer qual dos dois errou é
humano** não.

Estado após a migração: **98 documentos migrados de 116**. Os 33 da CF/88
fecharam integralmente; nas estaduais e federais 18 ficaram de fora, por
recusa e não por esquecimento — 12 porque suas normas só têm fonte no
Planalto, fora do ar durante toda a sessão, e 6 pelo motivo do item 2 abaixo.
Migrar exige afirmar também o *fim*, e "sem `vigencia_fim`" quer dizer "ainda
em vigor": afirmação que não sai de memória.
`check_ancestrais_divergentes` fica genuinamente exercitado: o nível
`cf88/art-40` é afirmado por 25 documento-níveis e `cf88/art-40-par-1` por 13,
todos concordantes.

O que a migração revelou, e que o relatório acima não podia ver: **seis
documentos são nomeados por uma emenda que não deu redação ao nível que eles
endereçam.** `art-40-par-1-inc-ii/ec-103-2019` tem o inciso da EC 88/2015;
`art-40-par-5/ec-41-2003` tem o § 5º da EC 20/1998 e só existe porque o caput
mudou; `art-40-par-8/ec-41-2003` tem um § 8º que **segue em vigor hoje** e
cujo documento termina em 2019-11-12 apenas porque o caput foi reescrito.
Nenhum desses fatos era representável antes.

### Fica pendente

1. **`cf88/art-40-par-8/ec-103-2019` não existe.** O § 8º na redação da EC
   41/2003 continua em vigor sob o caput da EC 103/2019 — a EC 103 não o
   reproduziu nem o revogou (o art. 35 revoga só o § 21). É lacuna legítima
   pela transcrição sob demanda (invariante 10), mas é uma redação que a lei
   tem e o bundle não. Autorá-la exige conferir a sobrevivência do § 8º, que
   é conclusão jurídica.
2. **Os 6 documentos da redação LCE 949/2017 exigem procedência não uniforme.**
   Em `art-10-inc-i` e nos dois de `art-32`, o caput é original e só o nível
   interno é da LC 949 — copiar a tripla do documento para todos os
   componentes gravaria cadeia falsa. Em `art-33`, `art-34-inc-i` e
   `art-34-par-2` a cadeia inteira é da LC 949. A migração deles depende de
   fechar a `vigencia_inicio` da própria LC 949/2017, hoje recusada em
   `lce-949-2017/norma.md`: SAPL e DITEL discordam sobre a data da lei
   (18/07 × 17/07/2017) e a cláusula de 180 dias admite duas contagens.
3. **Falta decidir se os campos de componente passam a ser exigidos.** Hoje
   são opcionais (RFC 0009, fase 1), para que a migração pudesse ser
   incremental. Com ela concluída, exigi-los transforma o invariante de
   "checado onde declarado" em "checado sempre".
