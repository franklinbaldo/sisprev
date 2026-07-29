# RFC 0010 — Corpus de pareceres da PGE: extração do SEI, despersonalização e vínculo com as regras

- **Status**: proposta (2026-07-29). **Especificação e procedimento, sem
  implementação.** Nenhum arquivo de `okf/` é criado por esta RFC; ela existe
  para que uma sessão **com acesso ao SEI** possa executar o trabalho sem ter
  de decidir, sozinha e no meio do caminho, coisas que não são dela.
- **Depende de**:
  [`docs/analysis/processos-sei-da-planilha-da-pge.md`](../analysis/processos-sei-da-planilha-da-pge.md)
  (o inventário das 40 linhas e o mapeamento por texto exato) e da
  [RFC 0008](0008-traducao-sem-perdas-entre-os-dois-esquemas.md) (por que uma
  relação jurídica não se deriva de prosa).
- **Não-objetivo**: alterar `regra-*.md`, o schema deployável, o CSV derivado
  ou o relatório da PGE. Preencher `atos_validacao` — ver §2, que é a razão
  principal de esta RFC existir antes do trabalho.

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
3. **Duas decisões desta RFC não são suas** — §2 e §4.3. Se chegar nelas sem
   resposta escrita de quem coordena a auditoria, **pare e pergunte**. Seguir
   com um palpite aqui produz um repositório público com dado pessoal dentro,
   e isso não se desfaz com um commit de correção: o histórico do git guarda.

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

## 2. Decisão pendente: o que se extrai do parecer

**Esta é a bifurcação principal e ela não é do agente executor.**

- **(A) Só a fundamentação jurídica.** Extrai-se a seção do parecer que
  raciocina sobre a regra e a lei, descartando relatório, dispositivo e
  qualquer trecho que descreva o caso. É o que a auditoria de fato precisa, e
  é a opção com menor superfície de risco.
- **(B) O parecer integral, despersonalizado.** Mantém-se o documento inteiro
  e removem-se os identificadores.

**Recomendação: (A).** Não por conservadorismo abstrato — por três razões
concretas:

- despersonalizar (B) num parecer de incapacidade é **muito difícil e o erro é
  silencioso**. Não basta tirar o nome: doença + data de ingresso + regra
  aplicada + órgão de lotação reidentifica uma pessoa dentro de um universo de
  servidores estaduais. Um documento que "parece limpo" e reidentifica é
  exatamente o modo de falha que ninguém percebe na conferência;
- o relatório e a análise não usam o caso. Usam a leitura da norma. (B)
  carrega risco por conteúdo que não vai ser lido;
- (A) é conferível: dá para ler o trecho extraído inteiro e afirmar que ele
  não fala de ninguém. (B) exige afirmar que *nada* no documento identifica —
  uma negativa universal sobre trinta páginas.

Se a coordenação escolher (B), §4 continua valendo mas deixa de ser
suficiente, e a revisão passa a exigir duas leituras humanas independentes.

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
5. registre no próprio documento **quantas substituições de cada tipo** foram
   feitas, e quem revisou.

**"O regex não achou nada" nunca é conclusão de que não há PII.** Esse é o
mesmo erro que a RFC 0008 documenta no leitor de citações, com o sinal
invertido: lá o mecanismo afirmava demais; aqui ele deixaria de afirmar, e o
silêncio seria lido como limpeza.

### 4.3 Decisão pendente: o número do processo entra no repositório?

O número do processo **reidentifica**: com ele, qualquer pessoa com acesso ao
SEI chega ao requerimento inteiro, com tudo que a despersonalização tirou. Um
parecer despersonalizado que declara o próprio processo não está
despersonalizado para quem tem esse acesso.

Registre-se um fato que a coordenação precisa conhecer antes de decidir: **os
25 números já estão no repositório público**, em
`data/raw/xlsx/regras-processo-sei.csv`, desde a importação original — e
`data/raw/` é imutável por política, verificada em CI
(`original-raw-immutable`). Ou seja, a decisão aqui não é "expor ou não pela
primeira vez"; é se o corpus novo **repete e amplifica** uma exposição que já
existe, e se aquela primeira exposição deve ser reavaliada. A segunda pergunta
é maior que esta RFC.

Não decida isto sozinho. Enquanto não houver resposta, **não grave o número do
processo** no frontmatter: use o identificador do parecer (`Parecer nº 1271/2023 — PGE/RO`), que é a identidade institucional citável do documento e
não aponta para os autos de ninguém.

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
escopo: fundamentacao_juridica   # ou `integral`, conforme a decisão de §2
regras:                          # vínculo autorado, N:N — ver §6
  - /regras/regra-0012.md
  - /regras/regra-0013.md
despersonalizacao:
  revisado_por: <quem leu o texto inteiro>
  revisado_em: 2026-08-05
  substituicoes:                 # contagem por tipo, nunca os valores
    NOME: 7
    CPF: 1
    MATRICULA: 2
    DATA: 4
fonte_interna: <referência não pública, se a coordenação a exigir>
```

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

## 6. O vínculo com as regras

`regras:` é **autorado**, uma entrada por vez, exatamente como `dispositivos:`
numa regra. Nada no repositório pode derivá-lo, e a razão é a mesma da
RFC 0008: uma relação jurídica extraída por semelhança de texto é uma
afirmação plausível e não verificada.

O ponto de partida — e só isso — é a tabela de correspondência exata em
[`processos-sei-da-planilha-da-pge.md`](../analysis/processos-sei-da-planilha-da-pge.md),
onde 26 das 40 linhas casam com uma ou mais regras por **texto idêntico** de
fundamentação. Duas consequências práticas:

- **a relação é N:N e quase nunca 1:1.** Só 2 das 26 linhas correspondem a uma
  única regra; 20 correspondem a duas, e uma corresponde a seis. Um parecer que
  trate da linha 35 vincula-se às seis regras `regra-0059`…`regra-0064`. Isso
  não é imprecisão: é a partição da PGE sendo mais grossa que a do Sisprev, e é
  o assunto da RFC 0004;
- **as 14 linhas sem correspondência exata não estão mapeadas.** A tabela de
  candidatos por sobreposição de vocabulário daquele documento é auxílio de
  leitura, não mapeamento — a linha 13 é o contraexemplo: descreve voluntária
  por idade e tempo de contribuição, e seus melhores candidatos são regras de
  especial de professor, porque citam os mesmos artigos.

Onde o parecer não permitir dizer com segurança a que regra se refere,
**não vincule** e escreva no corpo por quê. Uma lacuna registrada é conferível;
um vínculo errado é uma afirmação falsa sobre o que a PGE analisou.

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

- **Fase 0 — esta RFC.** Nada é baixado.
- **Fase 1** — decisões de §2 e §4.3 respondidas por escrito.
- **Fase 2** — um parecer, do começo ao fim, como piloto. Ele é que revela o
  que este documento errou.
- **Fase 3** — os demais, em lotes; `parecer_schema.py` e gate de forma.
- **Fase 4** — o parecer aparece no capítulo da regra no relatório da PGE.
  Decisão institucional própria: citar num documento sobre regras um parecer
  proferido no caso de um terceiro não é consequência automática de o corpus
  existir.
