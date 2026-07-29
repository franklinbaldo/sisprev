# RFC 0010 — Corpus de pareceres da PGE: extração do SEI, despersonalização e vínculo com as regras

- **Status**: proposta (2026-07-29), **com as duas decisões de coordenação
  respondidas no mesmo dia** (§2 e §4.3). A única coisa implementada é o campo
  `precedentes` (§6.1), vazio em todas as regras. Nenhum arquivo de `okf/` é
  criado por esta RFC; ela existe para que uma sessão **com acesso ao SEI**
  possa executar o trabalho sem ter de decidir, sozinha e no meio do caminho,
  coisas que não são dela.
- **Depende de**:
  [`docs/analysis/processos-sei-da-planilha-da-pge.md`](../analysis/processos-sei-da-planilha-da-pge.md)
  (o inventário das 40 linhas e o mapeamento por texto exato) e da
  [RFC 0008](0008-traducao-sem-perdas-entre-os-dois-esquemas.md) (por que uma
  relação jurídica não se deriva de prosa).
- **Não-objetivo**: alterar `regra-*.md`, o schema deployável, o CSV derivado
  ou o relatório da PGE. Preencher `atos_validacao` — ver §7.

## Quem executa isto

Uma sessão distinta, com acesso autenticado ao SEI. Esta RFC é o contrato
dela. Três coisas valem antes de qualquer download:

1. **Você está entrando num sistema com dados pessoais de servidores reais.**
   Cada processo da lista é o requerimento de aposentadoria ou pensão de uma
   pessoa. Nos processos de incapacidade há **dado pessoal sensível** (saúde).
   O objetivo não é trazer o processo para o repositório: é trazer *o que a
   PGE disse sobre a regra*.
2. **Baixe só o que está na lista de §3.** Não navegue lateralmente, não siga
   processos relacionados, não use pesquisa livre para "achar mais". A lista é
   fechada e tem 25 itens.
3. **Duas decisões estão tomadas e não são suas para rediscutir** — §2 (extrai
   o parecer **integral**) e §4.3 (o número do processo **é gravado**). Ambas
   ampliam o que entra no repositório em relação à alternativa mais restrita, e
   é por isso que §4 ganhou controles próprios. Qualquer coisa fora do que elas
   autorizam, **pare e pergunte**: um repositório público com dado pessoal
   dentro não se desfaz com um commit de correção, porque o histórico do git
   guarda.

## 1. O que este corpus é, e para que serve

Todo o resto do repositório é a regra **declarada** — o frontmatter, a
fundamentação, os dispositivos. O parecer é a regra **lida por um jurista**,
aplicada a um caso concreto. É a única fonte que responde a perguntas como
"a PGE já se manifestou sobre a janela temporal desta regra?" ou "que leitura
o procurador deu ao art. 17 quando o aplicou?".

Isso serve à auditoria de duas maneiras: fecha pendências que hoje estão
abertas no corpo P13.1 de várias regras, e dá ao relatório de validação um
histórico — o procurador que recebe o documento passa a ver o que a própria
PGE já disse sobre aquela regra antes.

## 2. Decidido: extrai-se o parecer integral, despersonalizado

**Decisão da coordenação da auditoria, 2026-07-29.** Mantém-se o documento
inteiro — relatório, fundamentação e conclusão — e removem-se os
identificadores conforme §4.

A alternativa considerada era extrair só o trecho de fundamentação jurídica.
Ela foi recusada, e o registro da razão pela qual **não** foi escolhida importa
tanto quanto a escolha: o trecho isolado é mais fácil de garantir limpo, mas
perde o encadeamento entre o que o procurador constatou e o que ele concluiu —
e é justamente esse encadeamento que permite conferir se a regra foi aplicada
como está escrita.

O custo assumido, e ele é real:

- **o erro é silencioso.** Num parecer de incapacidade, tirar nome, CPF e
  matrícula não basta: doença + data de ingresso + regra aplicada + órgão de
  lotação reidentifica uma pessoa dentro do universo de servidores estaduais.
  Um documento que "parece limpo" e reidentifica é o modo de falha que ninguém
  percebe na conferência;
- **a afirmação exigida é mais forte.** No trecho isolado, bastava ler e dizer
  "isto não fala de ninguém". No documento integral, é preciso sustentar que
  *nada* nele identifica — uma negativa universal sobre dezenas de páginas.

Por isso a escolha de (B) **acopla dois controles obrigatórios**, sem os quais
ela não vale:

1. **duas leituras humanas independentes** por documento, de pessoas
   diferentes, cada uma registrada em `despersonalizacao.revisado_por`. A
   segunda leitura não é conferência da primeira: é uma leitura do zero;
2. **a combinação é examinada, não só os campos.** Depois de substituir os
   identificadores, releia perguntando "quem lê isto e conhece o quadro
   funcional do Estado consegue dizer de quem se trata?". Se a resposta for
   talvez, generalize também o atributo combinatório — a doença específica
   vira `[MOLÉSTIA]`, a lotação vira `[ÓRGÃO]`, a data exata vira o ano.

## 3. Quais pareceres, e como achá-los

A lista fechada está em
[`docs/analysis/processos-sei-da-planilha-da-pge.md`](../analysis/processos-sei-da-planilha-da-pge.md),
extraída de `data/raw/xlsx/regras-processo-sei.csv` — uma aba da planilha
original da PGE, com 40 linhas, das quais **25 trazem um número de processo**.

O que a coluna `PROCESSO SEI` registra: **um processo em que aquela regra foi
aplicada a um caso real**. Não é o processo em que a regra foi aprovada.

Dentro de cada processo, o que interessa é **o parecer da PGE** — não o
requerimento, não os documentos pessoais anexados, não o laudo médico, não a
certidão de tempo de contribuição. Se o processo tiver mais de um parecer,
traga todos, cada um como documento próprio.

Registre, para cada processo acessado: número, data do acesso, quais
documentos foram abertos e quais foram baixados. Esse registro entra no
repositório (§5), e é ele que torna o acesso auditável.

Se um processo da lista não existir, estiver sigiloso ou não contiver parecer,
**registre isso** como resultado — a ausência é informação, e um item que
simplesmente sumir da lista vira dúvida depois.

## 4. Despersonalização

### 4.1 Onde a PII se esconde num documento do SEI

Esta lista é o mínimo a conferir. Ela não é exaustiva por construção — o
propósito dela é impedir que a conferência pare cedo demais.

- **Corpo do texto**: nome do servidor, do cônjuge, dos dependentes, do
  procurador que assina, de servidores citados; CPF, RG, PIS/PASEP, matrícula
  funcional, número do benefício, número do processo administrativo e
  judicial; datas de nascimento, admissão e óbito; cargo, lotação e órgão;
  valores de remuneração e de provento; **diagnóstico, CID, descrição de
  moléstia, resultado de perícia**.
- **Cabeçalho e rodapé de cada página** — o SEI costuma repetir o número do
  processo e o do documento em toda folha. Uma limpeza que trate só o "texto"
  passa por cima disso.
- **Bloco de assinatura eletrônica**, com nome, cargo e código de verificação.
  O código de verificação **é um identificador**: com ele, qualquer um recupera
  o documento no portal público do SEI.
- **Metadados do arquivo**: autor, título, produtor, assunto, palavras-chave
  do PDF. Sobrevivem a qualquer edição do texto e ninguém olha.
- **Camada de texto sob a imagem**: um PDF digitalizado pode ter OCR embutido.
  Tarjar visualmente a imagem **não remove** o texto por baixo. Extraia o
  texto e confira o que sai, nunca confie na aparência da página.
- **Nome do arquivo** que você salvar.

### 4.2 Procedimento

O passo mecânico existe para **aumentar o recall**, não para dar o veredito:

1. converta o documento para texto e trabalhe sobre o texto extraído, nunca
   sobre a aparência da página;
2. rode um passo mecânico de marcação (regex para CPF/RG/matrícula/CNJ/datas,
   e um reconhecedor de entidades para nomes de pessoa — Presidio ou
   equivalente) **calibrado para marcar demais**. Falso positivo custa uma
   leitura; falso negativo custa um vazamento;
3. **leia o texto inteiro à mão.** Este passo não é opcional e não é
   substituível. O passo 2 não encontra "a servidora, professora da rede
   estadual em Ji-Paraná, afastada desde 2019 por moléstia especificada em
   lei" — que não tem uma única entidade nomeada e identifica uma pessoa;
4. substitua cada ocorrência por um marcador estável e legível
   (`[NOME]`, `[CPF]`, `[MATRÍCULA]`, `[DATA]`, `[CID]`), nunca por remoção
   silenciosa: quem revisa precisa ver *que havia* algo ali;
5. **repita os passos 3 e 4 com outra pessoa**, do zero — a segunda leitura
   não é conferência da primeira. É o controle que a decisão de §2 exige, e
   sem ele o parecer integral não pode ser commitado;
6. registre no próprio documento **quantas substituições de cada tipo** foram
   feitas, e **as duas pessoas** que revisaram.

**"O regex não achou nada" nunca é conclusão de que não há PII.** Esse é o
mesmo erro que a RFC 0008 documenta no leitor de citações, com o sinal
invertido: lá o mecanismo afirmava demais; aqui ele deixaria de afirmar, e o
silêncio seria lido como limpeza.

### 4.3 Decidido: o número do processo é gravado

**Decisão da coordenação da auditoria, 2026-07-29.** O `identificador` de um
`precedente` e o vínculo de um parecer com os seus autos são gravados no
repositório público, com o número do processo.

A rastreabilidade de volta ao processo é o que torna cada precedente
verificável — sem ela, "esta regra já foi aplicada" é uma afirmação que
ninguém consegue conferir, e o corpus perde a única propriedade que o
distingue do resto do catálogo.

**A consequência precisa estar escrita, porque ela muda o que o corpus é.**
Para quem tem acesso ao SEI, o número anula a despersonalização: partindo dele
chega-se ao processo inteiro, com tudo que §4 removeu. Então:

- **este corpus é pseudonimizado, não anônimo.** Nenhum documento, README ou
  página do site pode descrevê-lo como anônimo, e ninguém deve tratá-lo como
  se fosse;
- **a despersonalização continua valendo, e protege quem não tem esse acesso**
  — que é a maioria de quem lê um repositório público. Ela deixa de ser
  suficiente; não deixa de ser necessária;
- **o modelo de ameaça está declarado**: leitor sem acesso ao SEI, protegido
  pela despersonalização; leitor com acesso ao SEI, não protegido, e que já
  poderia chegar aos mesmos autos por outros caminhos.

Isto foi decidido sabendo que os 25 números **já estão no repositório público**
desde a importação, em `data/raw/xlsx/regras-processo-sei.csv`. Gravá-los de
novo amplifica uma exposição existente em vez de criar uma — e a coordenação
decidiu, junto, reabrir a questão daquela primeira exposição (§10).

## 5. O bundle

Um terceiro bundle OKF, com identidade própria — nunca um `regra-NNNN`, nunca
um `achado-NNNN`, pela mesma razão da RFC 0004 §1.2.

```
okf/pareceres/
├── index.md                  # listagem, sem frontmatter
├── pareceres.md              # type: Dataset
└── pareceres/
    ├── index.md
    └── parecer-0001.md ...   # type: Parecer
```

Frontmatter proposto:

```yaml
type: Parecer
id: parecer-0001
identificador: Parecer nº 1271/2023 — PGE/RO
autoridade: Procuradoria-Geral do Estado de Rondônia
data: 2023-08-14
escopo: integral                 # decidido em §2
acesso:                          # o registro que §3 exige
  em: 2026-08-05
  por: <quem acessou o SEI>
  documentos_abertos: 4
  documentos_baixados: 1
despersonalizacao:
  escopo_decidido_em: 2026-07-29        # §2: parecer integral
  revisado_por:                          # duas leituras independentes (§4.2)
    - <quem leu o texto inteiro>
    - <quem leu de novo, do zero>
  revisado_em: 2026-08-05
  substituicoes:                 # contagem por tipo, nunca os valores
    NOME: 7
    CPF: 1
    MATRICULA: 2
    DATA: 4
processo: 0031.117501/2020-19    # gravado por decisão de §4.3
```

**O parecer não declara a que regras se refere.** O vínculo mora na regra
(§6), e ter as duas pontas declarando a mesma relação criaria duas verdades
para manter em sincronia, sem gate que as reconcilie. É a convenção que
`dispositivos:` já segue: a regra aponta para fora, e o backlink na ficha do
destino é derivado.

O corpo é o texto despersonalizado, **verbatim no que sobrou** — a
despersonalização substitui, não reescreve, não resume e não corrige o
português do procurador. Se o parecer disser algo que a auditoria considere
errado, isso vira um achado; não vira uma edição do parecer.

Notas de forma, para o documento passar nos gates que já existem:

- `index.md` **nunca** leva frontmatter (a exceção do `okf_version` vale só
  para o `index.md` da raiz do bundle);
- todo `.md` autorado passa por
  `uv run python scripts/md_format.py okf docs README.md CLAUDE.md`;
- comece **sem** schema Python. Autore dois ou três documentos primeiro e só
  então escreva `scripts/parecer_schema.py` no molde de `achado_schema.py`
  (subclasse de `Concept`, contrato validado uma vez por `cached_property`).
  Escrever o schema antes de existir corpo real é desenhar contra a
  imaginação.

## 6. O vínculo mora na regra, em `precedentes`

**Decisão da coordenação, 2026-07-29: a vinculação é feita nos `regra-*.md`,
não na planilha.** Uma entrada de `precedentes` (§6.1) no frontmatter da regra
é o vínculo — e é a única representação dele.

Três consequências, e a terceira é a que evita retrabalho:

- **a planilha não é editada, nunca.** `data/raw/xlsx/regras-processo-sei.csv`
  é entrada congelada, sob o gate `original-raw-immutable`. Ela é a origem dos
  números e mais nada; nenhum resultado deste trabalho volta para lá;
- **o parecer também não declara o vínculo** (§5). Uma ponta só, na regra;
- **o mapeamento por texto exato é auxílio de leitura, não fonte.** A tabela em
  [`processos-sei-da-planilha-da-pge.md`](../analysis/processos-sei-da-planilha-da-pge.md)
  diz por onde começar; quem autora confere e escreve a entrada no
  `regra-*.md`. Nada no repositório lê aquela tabela, e nada deve.

O vínculo é **autorado**, uma entrada por vez, pela mesma razão da RFC 0008
que rege `dispositivos:`: uma relação jurídica extraída por semelhança de texto
é uma afirmação plausível e não verificada.

Duas propriedades da relação que mudam o trabalho na prática:

- **é N:N, e quase nunca 1:1.** Das 26 linhas que casam por texto idêntico, só
  2 correspondem a uma única regra; 20 correspondem a duas, e uma corresponde a
  seis. Um processo da linha 35 vira uma entrada de `precedentes` em **cada**
  uma das seis regras `regra-0059`…`regra-0064`. Isso não é imprecisão: é a
  partição da PGE sendo mais grossa que a do Sisprev, e é o assunto da
  RFC 0004;
- **as 14 linhas sem correspondência exata não estão mapeadas.** Os candidatos
  por sobreposição de vocabulário naquele documento não são mapeamento — a
  linha 13 é o contraexemplo: descreve voluntária por idade e tempo de
  contribuição, e seus melhores candidatos são regras de especial de professor,
  porque citam os mesmos artigos.

Onde o parecer não permitir dizer com segurança a que regra se refere, **não
vincule** e registre por quê — no corpo P13.1 da regra, se houver uma
candidata, ou na análise do próprio parecer. Uma lacuna registrada é
conferível; um vínculo errado é uma afirmação falsa sobre o que a PGE analisou.

## 6.1. `precedentes` — o campo que faltava

Implementado junto com esta RFC, e **vazio em todas as 112 regras**: existe
para que o trabalho de §3 tenha onde ser gravado.

Um `precedentes:` no frontmatter da regra é a lista de casos concretos em que
ela já foi aplicada. É onde os 25 números da planilha vão parar — não em
`atos_validacao` — e, quando houver parecer extraído, é a entrada que o
referencia: **ela é o vínculo** (§6), não uma anotação ao lado dele.

```yaml
precedentes:
  - identificador: 0031.117501/2020-19
    fonte: SEI
    parecer: /pareceres/parecer-0001.md   # opcional
    observacao: concessão deferida        # opcional
```

Três decisões de representação, cada uma com a sua razão:

- **`fonte` é texto livre**, como `AtoValidacao.fonte`, e pelo mesmo motivo: a
  Q12 (o SEI é a única origem válida?) segue em aberto, e um enum aqui
  responderia por decreto uma pergunta institucional.
- **`precedentes` fica fora da chave material do P2**
  (`igualdade_material._IGNORED_FRONTMATTER_KEYS`), junto de `dispositivos` e
  `atos_validacao`. O argumento é o de `dispositivos` e mais forte: duas
  regras materialmente iguais têm a *mesma* fundamentação, logo casam com a
  mesma linha da planilha e acabam com os mesmos precedentes — só divergem
  enquanto uma foi anotada e a outra não. Material, o grupo P2 se dissolveria
  no meio da anotação e se reformaria no fim, invalidando os achados que o
  documentam sem que regra nenhuma tivesse mudado.
- **É anotação de auditoria, não campo do Sisprev.** Vai para o CSV *derivado*
  em coluna própria, JSON-codificada, como `atos_validacao` e `dispositivos`;
  não entra no contrato legado que o compilador da RFC 0004 confere.

O relatório da PGE imprime a seção "Casos em que esta regra foi aplicada"
quando houver algum — hoje, em nenhum capítulo.

**Preencher `precedentes` está liberado** desde a decisão de §4.3: o
`identificador` recebe o número do processo. O campo segue vazio nas 112
regras porque o trabalho de conferência ainda não foi feito — não porque
falte política.

## 7. O que **não** fazer

- **Não preencha `atos_validacao`** de regra nenhuma a partir daqui. Esse campo
  é o ato que **valida** a regra e é a condição de `status_auditoria: validada`
  (`estado_auditoria` exige a lista não vazia). Um parecer emitido num caso de
  aplicação não valida a regra em abstrato — preenchê-lo faria uma regra virar
  `validada` por ter sido *usada*, com o gate verde e o selo aceso no site e no
  relatório, afirmando uma validação que ninguém assinou.
- **Não edite nenhum `regra-*.md`** neste trabalho. Se o parecer contradisser
  uma regra, isso é um **achado** (`okf/regras-sisprev/achados/`), autorado à
  mão, com `natureza: juridica`.
- **Não coloque o PDF original no repositório**, nem numa pasta ignorada, nem
  "temporariamente". Trabalhe fora da árvore do git e traga só o texto revisado.
- **Não faça commit antes da revisão humana do §4.2.3.** O histórico do git é
  permanente; um `git rm` posterior não remove nada.
- **Não invente `tipo`/`autoridade`** que o documento não declare.

## 8. Commit

O bundle novo não tem gate próprio ainda, então os gates existentes não vão
proteger contra erro de conteúdo — só de forma. Antes de commitar:

```bash
uv run python scripts/md_format.py okf docs README.md CLAUDE.md
uv run ruff format --check && uv run ruff check && uv run ty check
uv run pytest -q
uv run python scripts/gerar_indices.py     # se tocou em regra/achado
uv run python scripts/validar_regras.py
```

Um commit por parecer, ou um por lote pequeno — nunca 25 de uma vez. A
mensagem diz qual processo originou, quantas substituições foram feitas e
quem revisou. Abra a PR normalmente; o `site.yml` vai rebuildar, e se o bundle
novo virar coleção do site (fase seguinte, não esta) o relatório passa a poder
citá-lo.

## 9. Fases

- **Fase 0 — esta RFC.** Nada é baixado. **Concluída**, com as decisões de §2
  e §4.3 tomadas em 2026-07-29 e o campo `precedentes` implementado.
- **Fase 1** — um parecer, do começo ao fim, como piloto: baixar, despersonalizar
  com as duas leituras de §2, autorar o documento, vincular às regras. Ele é que
  revela o que este documento errou, e é barato errar em um.
- **Fase 2** — os demais, em lotes; `parecer_schema.py` e gate de forma.
- **Fase 3** — o parecer aparece no capítulo da regra no relatório da PGE.
  Decisão institucional própria: citar num documento sobre regras um parecer
  proferido no caso de um terceiro não é consequência automática de o corpus
  existir.

## 10. Reavaliação de `data/raw/` (aberto)

Decidido em 2026-07-29 que a questão será reaberta; **como** ela se resolve,
não. Este é o registro do que quem for decidir precisa saber.

Os 25 números de processo entraram no repositório em `49a9d38`, na Fase 0, e
`data/raw/xlsx/regras-processo-sei.csv` está sob o gate `original-raw-immutable`
do `ci.yml` — que verifica que **cada entrada congelada tem exatamente um commit
em todo o histórico**. Hoje o arquivo tem esse um commit e nada mais.

Isso torna a reavaliação estranha, e vale enunciar antes de alguém tentar:

- **não dá para "corrigir" o arquivo com um commit.** Um segundo commit
  tocando nele reprova o gate, por construção. E mesmo que passasse, não
  removeria nada: o conteúdo antigo continua no histórico;
- **remover de verdade exige reescrever o histórico**, o que invalida todo SHA
  já publicado — inclusive os impressos nas capas dos relatórios de validação
  que forem juntados a processos, que é justamente o mecanismo pelo qual um
  anexo se identifica;
- **manter também é uma decisão**, e é a que vale por omissão. Só não deveria
  valer por esquecimento.

As duas saídas plausíveis, portanto, são "manter e registrar por escrito por
que se manteve" ou "reescrever o histórico e aceitar o custo". A escolha é de
quem responde pelo tratamento de dados pessoais, não da auditoria — e não
bloqueia nada do resto desta RFC.
