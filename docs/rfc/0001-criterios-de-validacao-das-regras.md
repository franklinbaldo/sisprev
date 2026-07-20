# RFC 0001 — Critérios de validação e processo de auditoria das regras

- **Status**: Aceita (2026-07-17)
- **Criada em**: 2026-07-17
- **Atualizada em**: 2026-07-17 — incorpora as decisões consolidadas sobre
  P1/P2 (nada é fundido nem excluído; inativação documentada como
  **mecanismo disponível** condicionado a conclusão de auditoria; campo
  `status_regra`; CSV derivado estendido) — ver
  [comentário na PR #2](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005164122) —
  e sobre P3/P5/P7 (dispositivos na menor unidade citada; sentinelas
  mantidas e documentadas; máquina mínima de estados com a regra de
  desenho "estado novo exige invariante novo") — ver
  [segundo comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005233600) —
  e sobre P2.1 (sem campo de ponteiro: o membro ativo de um grupo é
  condição derivada, não campo armazenado; encerramento temporal ≠
  inativação) — ver
  [terceiro comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005286024) —
  e sobre a separação detecção × conclusão (evidências são achados a
  investigar, não veredictos; nenhum resultado de auditoria é
  predeterminado) — ver
  [quarto comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005343565) —
  e sobre a exigência de especificação semântica de `type: Regra` + mapa
  normativo CSV → OKF como fonte única (P13, com as questões Q1–Q12) — ver
  [quinto comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005449361) —
  e sobre `NOME ↔ nome` (sem `title` em `Regra`), achados como fonte de
  verdade (verificação bidirecional com o validador) e a remoção dos
  resíduos que antecipavam a resolução de E2 — ver
  [sexto comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005598005) —
  e sobre P14 (achados como conceitos OKF próprios em `achados/`, com
  `regras_afetadas` como fonte única, verificação mecânica/manual/híbrida
  e backlinks gerados) — ver
  [sétimo comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005658014) —
  e sobre o **princípio da semântica adiada** (interpretação provisória de
  campo não vira erro/bloqueio antes da P13; checks em quatro camadas;
  neutralização de E3/E5, código `P2_IGUALDADE_MATERIAL_ATIVA`, `nome`,
  sentinelas, datas-vs-marcos, P6-como-função, fluxo SEI e classificação
  de campos) — ver
  [oitavo comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005748991) —
  e sobre o **princípio da autoria humana e automação derivada** (código
  detecta fatos mecânicos, valida contratos e gera artefatos deriváveis,
  mas **não** autora achados: `nome`/`severidade`/`natureza`/
  `regras_afetadas`/evidências/questão são escritos por uma pessoa;
  detector e validador são operações puras; bidirecionalidade sobre
  `fingerprints` de ocorrências, separando `deteccoes` de
  `regras_afetadas`; a Fase 0 revisada exige detectores que apenas
  reportam) — ver
  [nono comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5006297110) —
  e sobre as **ferramentas de validação** (lógica normativa numa
  biblioteca Python pura e sem efeitos colaterais que retorna `Detection`/
  `Violation`; schema/invariantes em modelos tipados reutilizáveis —
  Pydantic ou equivalente; CLI fina somente-leitura; `pytest` como runner
  de contrato no CI, não como modelo de domínio nem segunda representação
  das detecções; Hypothesis opcional para propriedades; índices/CSV
  derivados por comando separado conferido com `git diff`) — ver
  [décimo comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5006363548) —
  e sobre a **revisão da Fase 1** (`status_auditoria` como vocabulário
  fechado verificado explicitamente; `revisada`/`validada` exigem
  `auditado_por`/`auditado_em` reais, não vazios, e não futuros — P11 deixa
  de ser apenas modelada e passa a ser exigida; `atos_validacao` malformado
  — tipo errado, item não-mapeamento — vira violação em vez de ser
  silenciosamente descartado da validação; a exigência de "commit próprio"
  na mudança de `status_auditoria` deixa de estar listada como
  `[bloqueante]` — nenhum gate de CI a implementa, então fica como
  convenção de processo até (e se) um gate assim for construído) — ver
  [revisão na PR #7](https://github.com/franklinbaldo/sisprev/pull/7#pullrequestreview-4726961366) —
  e sobre a **segunda rodada da revisão da Fase 1** (P1 passa a rodar sobre
  **todas** as regras, inclusive inativas — unicidade global de fato, não
  só entre ativas; `status_auditoria`/`auditado_por`/os quatro campos de
  cada `ato_validacao` deixam de aceitar qualquer valor truthy — exigem
  string não vazia real, e o default de `status_auditoria` só vale quando
  a chave está **ausente**, nunca quando presente com valor vazio/nulo/
  malformado; as quatro primeiras perguntas da P13.1 passam de convenção
  opcional para seções obrigatórias e não vazias no corpo de toda regra
  `revisada`, resolvendo a contradição entre "fronteira explícita" e
  "registro opcional") — ver
  [revisão na PR #7 (round 2)](https://github.com/franklinbaldo/sisprev/pull/7#pullrequestreview-4727369112).
- **Depende de**: PR #1 (bundle OKF inicial, CSV original congelado, CSV derivado)

> **Convenção de referência**: regras são sempre citadas pelo `id`
> (`regra-NNNN`), nunca por "linha do CSV". A linha física do CSV tem
> deslocamento de +2 em relação ao `row_index` (linha em branco +
> cabeçalho da exportação) — citar "linha 76" quando se quer `regra-0074`
> é um erro fácil e já ocorreu durante a discussão deste RFC. Onde a
> linha física for mencionada, é sempre entre parênteses e como
> informação secundária.

> **Princípio epistemológico — detecção ≠ conclusão**: este RFC define
> critérios, evidências, estados e formas de registrar conclusões — ele
> **não** produz antecipadamente as conclusões de mérito da auditoria que
> pretende organizar. Toda evidência mecânica (igualdade material, data
> divergente, incompatibilidade aparente entre campos, sobreposição) é
> motivo para **abrir um achado e investigar**, nunca um veredito. O
> validador detecta e reporta; quem conclui é a auditoria, e a conclusão é
> registrada com sua justificativa. Antes da investigação, usa-se
> linguagem neutra: "grupo de igualdade material", "registros envolvidos",
> "possível redundância" — não "cópia", "duplicata confirmada" ou
> "canônica".

> **Princípio da semântica adiada — interpretação provisória não bloqueia**:
> enquanto a **P13** (spec semântica + mapa normativo) não tiver confirmado
> a semântica de um campo, o detector pode **reportar** a ocorrência
> mecânica, mas o CI **não pode** transformar uma interpretação provisória
> em erro de mérito, severidade bloqueante, ou condição de `revisada` (P7).
> Interpretações provisórias, se registradas, dão origem a achados
> **informativos** ou **híbridos** (P14) **escritos pelo auditor**; só viram
> invariantes bloqueantes depois de documentadas no mapa P13.2. Isso
> classifica os checks da validação (P10) em quatro camadas:
>
> 1. **invariantes estruturais confirmados** (id/row_index/sequência,
>    proveniência, round-trip, unicidade de `id`) — **bloqueantes** desde já;
> 2. **detectores mecânicos neutros** (igualdade material, valores vazios,
>    grafias divergentes) — **reportam ocorrências**; quem registra o achado
>    correspondente é o auditor (ver o princípio da autoria humana, abaixo),
>    sem veredito;
> 3. **heurísticas semânticas provisórias** (aparência de incompatibilidade,
>    data fora dos marcos conhecidos) — o detector reporta a ocorrência; o
>    achado, se aberto, é **informativo ou híbrido** e escrito pelo auditor,
>    nunca falha de mérito nem bloqueio;
> 4. **regras semânticas confirmadas na P13.2** — só então podem virar
>    **bloqueantes**.
>
> As marcas **[bloqueante]** nas propostas abaixo que dependem de semântica
> ainda em Q1–Q12 devem ser lidas como **[bloqueante após P13]** — a
> detecção existe desde a Fase 0, a força bloqueante espera o mapa.

> **Princípio da autoria humana e automação derivada**: documentos que
> contêm significado, evidência selecionada, unidade de investigação ou
> conclusão são **fontes autorais** e são editados diretamente por uma
> pessoa. O código pode importar uma fonte congelada **uma única vez**
> (bootstrap), detectar fatos mecânicos, validar contratos e gerar
> representações **integralmente deriváveis**; **não** pode criar ou
> modificar conteúdo de auditoria como se tivesse realizado a investigação.
> Um detector afirma um fato mecânico — ele não decide, por si só, a
> unidade adequada de investigação, se duas ocorrências têm a mesma causa,
> quais regras são juridicamente afetadas além das detectadas, a natureza,
> a severidade, quais evidências contextuais importam, nem como formular a
> questão a investigar. Essas são decisões de auditoria, escritas nos
> `.md` por uma pessoa; do contrário o gerador vira autor da auditoria —
> exatamente a antecipação que "detecção ≠ conclusão" e "semântica adiada"
> pretendem impedir. A fronteira é explícita:
>
> ```text
> Fontes autorais (editadas diretamente):
>   okf/regras-sisprev/regras/regra-*.md
>   okf/regras-sisprev/achados/achado-*.md
>   docs/spec/regra.md
>
> Saídas mecânicas transitórias (não versionadas como fonte):
>   stdout/JSON dos detectores
>   fingerprints de ocorrências detectadas
>
> Artefatos derivados (gerados por comando, conferidos no CI):
>   regras/index.md, achados/index.md, index.md do bundle
>   data/regras-sisprev.csv
>   relatórios JSON/HTML
> ```
>
> **Exceção de bootstrap**: `csv_to_okf.py` continua válido como migração
> inicial e única do CSV congelado para os `regra-*.md`. Depois do
> bootstrap, os documentos das regras são fonte viva e não são
> regenerados a partir do CSV. A exceção **não** se estende aos achados:
> não existe fonte congelada anterior de onde um `achado-*.md` possa ser
> importado mecanicamente — o detector fornece evidência, o auditor cria o
> documento.
>
> **Resumo**: código encontra padrões; pessoas formulam achados. Código
> valida contratos; pessoas registram significado e conclusão. Código gera
> apenas o que pode ser integralmente reconstruído das fontes autorais.

## Contexto

O repositório contém o catálogo de regras de aposentadoria e pensão do
Sisprev como um bundle OKF (`okf/regras-sisprev/`), com o objetivo de
auditar e validar cada regra até que possa ser aplicada no sistema com
segurança jurídica (ver `README.md`). Este RFC propõe **o que** significa
uma regra ser válida — os critérios objetivos que o conjunto de regras deve
satisfazer — e **como** o processo de auditoria deve registrar isso.

A análise da importação original (112 linhas) já revela por que critérios
formais são necessários **antes** de começar a auditoria jurídica de mérito.
As evidências abaixo são **fatos mecânicos verificados na planilha** — cada
uma justifica abrir um achado e investigar; nenhuma delas é, por si só, uma
conclusão sobre erro, redundância ou qual campo está certo:

| #   | Evidência (fato mecânico)                                                                                                                                                                                                                                                                                                                                                                         | Quantidade                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E1  | Nomes repetidos (`NOME` igual em mais de uma linha) — indicam identidade insuficiente para o bundle; **não provam, por si sós, que as regras sejam iguais**                                                                                                                                                                                                                                       | 41 nomes, cobrindo 94 das 112 linhas                                                                                                                                                                                                                                                                                                                                                                      |
| E2  | **Grupos de igualdade material**: linhas com as 26 colunas não-`NOME` byte-a-byte idênticas na importação congelada (o detector ignora `NOME`, por P1/P2) — possível redundância **a investigar** (pode haver significado externo não capturado nas colunas, repetição intencional por configuração do sistema, origem em contextos distintos, ou problema de modelagem que exija outra correção) | 17 registros em 7 grupos: `regra-0012`/`0013`, `regra-0014`/`0015`, `regra-0065`/`0066`, `regra-0068`–`0070`, `regra-0074`–`0077` (5 grupos onde o próprio `NOME` também coincide) e `regra-0059`/`0063`, `regra-0060`/`0064` (2 grupos onde o `NOME` difere — incisos/graus de deficiência distintos, mas as 26 demais colunas idênticas, inclusive a fundamentação: descoberto pelo detector na Fase 0) |
| E3  | `TIPO_CALCULO = "Não identificado"` (valor literal observado; significado a investigar — Q10: dado faltante, estado legado, não aplicável, cálculo externo/manual, ou convenção válida para certos benefícios?)                                                                                                                                                                                   | 13 regras                                                                                                                                                                                                                                                                                                                                                                                                 |
| E4  | `SEXO` e `INTEGRAL` vazios (co-ocorrem com as 13 de E3) — vazio sem significado presumido (Q10)                                                                                                                                                                                                                                                                                                   | 13 regras                                                                                                                                                                                                                                                                                                                                                                                                 |
| E5  | `INTEGRAL = N` com `FUNDAMENTACAO_PROPORCIONAL` vazia (co-ocorrência de valores; a relação obrigatória entre os campos depende de Q6/Q7, ainda não confirmada)                                                                                                                                                                                                                                    | 17 regras                                                                                                                                                                                                                                                                                                                                                                                                 |
| E6  | Citação da mesma norma com grafias distintas ("LC 1100/21", "LC 1.100/2021", "Lc nº 1100/21")                                                                                                                                                                                                                                                                                                     | recorrente                                                                                                                                                                                                                                                                                                                                                                                                |
| E7  | **Incompatibilidade aparente** entre `SEXO = MASCULINO` e fundamentação que cita o dispositivo da mulher ("artigo 1º, inciso II, alínea 'b', da LC 51/1985 ... regra transitória - idade + tempo de contribuição + mulher") — sem conclusão prévia sobre **qual** campo está errado                                                                                                               | ao menos 1 (`regra-0078`)                                                                                                                                                                                                                                                                                                                                                                                 |
| E8  | **Datas divergentes** dos marcos legais e das regras relacionadas em `DATA_ADM_ATE`: `14/06/2021` (`regra-0049`/`0050`) e `09/09/2021` (`regra-0057`/`0058`) onde as gêmeas usam `14/09/2021` (data da ECE 146/2021) — divergência a conferir jurídica/documentalmente, não erro de digitação presumido                                                                                           | 4 regras                                                                                                                                                                                                                                                                                                                                                                                                  |

O corpus normativo **explicitamente observado na importação** contém cerca
de 16 normas: CF/88 (art. 40 em múltiplas redações), ECs 20/1998, 41/2003,
47/2005, 70/2012, 88/2015, 103/2019, ECE 146/2021, LCs 51/1985, 144/2014,
152/2015, LCEs 432/2008, 949/2017, 1.100/2021, Lei 10.887/2004 e IN nº
5/2020. O vocabulário é **controlado e extensível por PR**, não presumido
completo — a auditoria pode encontrar citações omitidas, normas
complementares ou dependências externas. Ainda assim, a ordem de grandeza
torna viável a proposta P3 (bundle de dispositivos) sem explosão de escopo.

______________________________________________________________________

## Propostas

Cada proposta tem um identificador (P1, P2, ...) para referência em
discussões e PRs. As marcadas **[bloqueante]** viram checks automáticos
(teste + CI) quando aceitas; as demais são processo/convenção.

### P1 — Nome: identidade humana, unicidade como meta de `revisada` (não bloqueio de importação)

**Campos de identidade (decisão 2026-07-17 — `NOME ↔ nome`, sem
`title` em `Regra`):**

- `id` — **identidade estável** do documento no bundle;
- `row_index` — **vínculo de proveniência** com a linha da importação
  congelada;
- `nome` — **rótulo humano** da regra, correspondente diretamente à coluna
  `NOME` (mapeamento `NOME ↔ nome`, sem transformação conceitual — o
  genérico `title` do OKF não acrescenta informação aqui e criaria uma
  conversão desnecessária; `title` continua em uso em outros tipos, como
  `Dataset`, mas não em `Regra`);
- não manter `title` e `nome` simultaneamente: seriam duas fontes para o
  mesmo dado. O índice de regras é gerado de `nome`.

```yaml
type: Regra
id: regra-0001
row_index: 1
nome: Aposentadoria por Invalidez Anterior à EC nº 20/1998
```

**Na importação, `nome` preserva o `NOME` recebido, mesmo repetido** — a
identidade técnica que distingue inequivocamente cada documento já é o
`id`. Nome repetido **não basta, sozinho, para navegação sem o `id`**: por
isso navegação e índices exibem `nome — regra-NNNN` (derivado, sem alterar
o dado). Forçar 94 registros a receberem nomes distintos **na Fase 0** —
com sufixos como "— Feminino" ou "— Proporcional" — anteciparia qual
dimensão distingue cada par, o que depende justamente das Q3/Q6/Q7/Q8/Q10;
por isso **não** é bloqueio de importação.

A qualificação dos nomes acontece **durante a auditoria**, depois que a
distinção real de cada par for confirmada. A unicidade global de `nome` é
uma **meta de `revisada`** (invariante que uma regra deve satisfazer para
avançar no P7), não um requisito bloqueante da importação: enquanto não
confirmada a distinção, o nome repetido gera **achado** (P14) para
qualificar, não falha de CI que trava a Fase 0.

Quando a auditoria concluir pela inativação de um registro por redundância
(P2.1), o sufixo do inativado referencia **o `id` do membro que permaneceu
ativo** (nunca "linha do CSV" — ver a convenção de referência no topo
deste RFC): "— duplicata de regra-0074". O sufixo é **informativo** — a
verdade normativa é o grupo derivado (P2.1); numa eventual troca posterior
de qual membro fica ativo, o PR renomeia os dois lados de qualquer forma.

Check proposto: **detecção** de `nome` repetido (case- e acento-insensível,
espaços normalizados) sobre todos os `regra-*.md` → achado; **bloqueante
apenas como invariante de `revisada`**, não da importação.

O mapa normativo P13.2 reflete `NOME ↔ nome`, e a estrutura declarativa
única conduz importação, exportação, geração de índice, tabela `# Schema`
e testes.

### P2 — Igualdade material entre regras ativas é achado a investigar [bloqueante como detecção]

O validador identifica **grupos de regras materialmente idênticas entre as
regras ativas** e exige, para cada grupo, um `type: Achado` aberto com
`detector: P2_IGUALDADE_MATERIAL_ATIVA` e as regras do grupo em `regras_afetadas`
(ver P14 — o achado é um conceito próprio em `achados/`, **não** uma seção
inserida nos `regra-*.md`). Cada grupo deve ser **investigado** para
determinar se representa redundância indevida, distinção não modelada ou
outro problema de origem. **O RFC não predetermina a resolução.**
Inativação documentada (P2.1) é uma solução **permitida** quando a
auditoria concluir que os registros não representam regras autônomas
distintas — não a única nem a automática.

O que a igualdade material **prova**: que as colunas comparadas (as 26
não-`NOME`) não distinguem os registros — evidência forte e suficiente para
abrir o achado (dois registros ativos indistinguíveis multiplicam o custo
de auditoria e criam risco de divergência silenciosa). Nos dois grupos onde
o `NOME` difere (`regra-0059`/`0063`, `regra-0060`/`0064`), a evidência é
ainda mais específica: os nomes indicam incisos/graus de deficiência
distintos, mas as 26 demais colunas — inclusive a fundamentação — não os
distinguem. O que ela **não prova**: que a repetição
é erro, que só um registro deve permanecer operacional, ou qual deles.
Pode haver significado externo não capturado nas colunas, repetição
intencional por configuração do sistema, origem em contextos distintos, ou
um problema anterior de modelagem que exija outra correção.

Em qualquer resolução, **nada é fundido nem excluído**: cada linha da
importação original permanece para sempre representada pelo seu próprio
`regra-*.md` (proveniência integral — nenhum `regra-*.md` importado
desaparece jamais). Isso **não congela o catálogo**: criar regras novas é
parte normal da vida do bundle (legislação nova, distinção que a auditoria
concluir precisar ser modelada) — uma regra nova recebe o próximo
`row_index` da sequência e incrementa o `row_count` do doc Dataset; a
sequência `1..row_count` de `_validate_identity()` continua válida com
qualquer N ≥ 112. O que a integridade proíbe é **remover ou renumerar** o
que já existe, nunca **acrescentar**. (Consequência de implementação: o
check de CI `bundle-imports-original`, que hoje exige contagem exatamente
igual à da importação, passa a exigir **cobertura** — todo `regra-0001..0112`
presente, contagem ≥ 112 — quando a primeira regra nova for criada.)

Estado inicial (até a conclusão de cada investigação): **112 regras
importadas, 112 tratadas como ativas por default, 7 achados de possível
igualdade material envolvendo 17 registros** — cada grupo um `type: Achado`
aberto (P14), **escrito pelo auditor** (não gerado por código — ver o
princípio da autoria humana), que referencia a ocorrência mecânica do
detector `P2_IGUALDADE_MATERIAL_ATIVA` por `fingerprint` (P14.6).

Check proposto: o detector `P2_IGUALDADE_MATERIAL_ATIVA` retorna grupos de
`regra-*.md` com `status_regra: ativa` e frontmatter + corpo materialmente
iguais (ignorando `id`, `row_index`, `nome` e os campos administrativos/de
auditoria de P2.1 e P7), cada grupo com um `fingerprint` estável (P14.6). O
detector **reporta a ocorrência**; o auditor **escreve o achado**. A
resolução nunca é automática, e o achado nunca é gerado por código.

### P2.1 — Inativação documentada de regras (mecanismo disponível, não resultado predeterminado)

Esta seção descreve **o mecanismo** que a auditoria usa **quando** (e
somente quando) concluir que um registro não representa uma regra autônoma
distinta. Nada aqui pressupõe que essa conclusão ocorrerá para qualquer
grupo específico.

Novo campo `status_regra` no frontmatter, **separado de `status_auditoria`
(P7)** — são dimensões diferentes: `status_regra` indica se o registro
participa como regra autônoma do catálogo; `status_auditoria` responde em
que etapa da revisão jurídica ela está.

- `status_regra: ativa` — participa do conjunto operacional (default;
  **todas as 112 regras importadas começam ativas**, e regras sem o campo
  são tratadas como ativas durante a migração).
- `status_regra: inativa` — a auditoria **concluiu, com justificativa
  registrada**, que o registro não tem identidade autônoma (motivos
  iniciais: redundância confirmada ou erro de importação); permanece no
  bundle apenas para proveniência, auditoria e histórico.

**Inativação ≠ encerramento temporal** (decisão 2026-07-17): uma regra cuja
janela de aplicação já se encerrou continua `status_regra: ativa` — ela
segue sendo uma regra autônoma, aplicável a fatos pretéritos (*tempus regit
actum*: quem adquiriu direito sob ela continua regido por ela). Revogação
ou término de vigência **não** são motivos de inativação; o encerramento
temporal já está representado pelas janelas de datas da própria regra.

Exemplo **hipotético** — se a auditoria do grupo `regra-0074`–`0077`
concluir que os quatro registros são o mesmo comando normativo e que só um
deve permanecer operacional, o resultado se registra assim:

```yaml
# regra-0074 — único membro ativo do grupo (condição derivada, não campo)
status_regra: ativa
```

```yaml
# regra-0077
type: Regra
id: regra-0077
row_index: 77
nome: Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021 — duplicata de regra-0074
status_regra: inativa
motivo_inativacao: duplicata
```

A investigação pode igualmente concluir outra coisa — p.ex. que os
registros se distinguem por algo não capturado nas 27 colunas (caso em que
a correção é **modelar a distinção**, mantendo todos ativos, e o achado se
resolve sem inativação alguma).

**Não existe campo `regra_canonica`** (decisão 2026-07-17): os grupos de
igualdade material são derivados mecanicamente das linhas no CSV original
congelado e, **se** houver inativações num grupo, o membro que permanece
ativo é **inferido** — condição derivada, não ponteiro armazenado.
Armazenar o ponteiro repetiria informação derivável — e com isso
desaparecem os checks de autorreferência e de cadeias `A → B → C`, o risco
de ponteiro obsoleto, e a ambiguidade sobre a "permanência da canônica"
(questão que se dissolve em vez de ser respondida). Trocar qual membro do
grupo fica ativo é uma transição atômica no mesmo PR: uma regra passa a
`inativa`/`duplicata` e a outra a `ativa` (com os renomes correspondentes
da P1).

**Regras inativas ficam fora de:** detecção de igualdade material (P2),
análise de cobertura e ambiguidade (P6), contagens operacionais, e
qualquer motor decisório futuro. **Continuam sujeitas a:** todos os checks
estruturais e de integridade documental (`_validate_identity`, P1,
frontmatter válido), e aparecem no CSV derivado (ver P12).

**Efeito na P7:** a inativação **congela** o `status_auditoria` no ponto em
que estiver — um registro inativado não precisa (nem deve) avançar até
`validada`; audita-se somente o membro que permaneceu ativo. Auditar N
registros materialmente idênticos seria o mesmo trabalho N vezes.

**Nota — `status_regra` ≠ `atualmente_no_sistema`:** inativar no bundle é o
veredito da *auditoria*; o Sisprev real continua com a regra até que alguém
a remova lá (`atualmente_no_sistema` segue refletindo o sistema). A
divergência entre os dois campos é, na prática, **a fila de mudanças a
aplicar no sistema** — um subproduto operacional valioso da auditoria.

Invariantes [bloqueantes] — verificados **por grupo de linhas
originalmente idênticas** (grupos derivados do CSV congelado) e por regra:

- Regra inativa tem `motivo_inativacao` (vocabulário fechado — ver P8;
  inicial: `duplicata` e `erro_de_importacao` — **não** existe motivo
  `revogada`: encerramento temporal não é inativação, ver acima).
- Em cada grupo de igualdade material: se houver membros inativos por
  `duplicata`, **exatamente uma** regra ativa no grupo (o membro ativo é a
  condição derivada). Enquanto a investigação não concluiu, todos os
  membros podem estar ativos — é o que a detecção
  `P2_IGUALDADE_MATERIAL_ATIVA` reporta e o achado (escrito à mão)
  documenta, como deve.
- Toda regra inativa por `duplicata` pertence a um grupo com **mais de uma
  linha original** — ninguém pode ser "duplicata" de nada se sua linha era
  única na importação.
- **Igualdade material verificável para sempre**: duplicata inativa ≡ **sua
  própria linha no CSV congelado** (recuperada por `row_index`), exceto
  `nome` (renomeado pela P1) e os campos administrativos
  (`status_regra`, `motivo_inativacao`, `status_auditoria` e correlatos de
  P7/P11). Como os registros de cada grupo de E2 eram byte-a-byte iguais
  entre si na importação, essa formulação prova por transitividade a
  igualdade original dentro do grupo — e o CI consegue re-verificá-la em
  qualquer commit futuro.
- A unicidade global de `nome` (P1) continua valendo para todos os
  membros do grupo, ativos e inativos.
- Não é necessário `nome_original`: a origem é recuperável por
  `id`/`row_index` na linha correspondente do CSV congelado. O CSV original
  preserva o nome recebido; o `.md` preserva a identidade auditada atual;
  `id`/`row_index` ligam os dois.

O resultado numérico da auditoria dos 5 grupos de E2 **não é
predeterminado** — depende da conclusão de cada investigação (inativação,
distinção a modelar, ou outra correção). O que o índice raiz e o doc
Dataset devem fazer é reportar as contagens de ativas e inativas
**separadamente**, refletindo o estado corrente do bundle, seja ele qual
for.

### P3 — Bundle de dispositivos legais (`okf/dispositivos/`)

Criar um segundo bundle OKF onde **cada `.md` é um único dispositivo
legal** (artigo/parágrafo/inciso/alínea) com o **texto exato** da norma, na
redação aplicável:

```
okf/dispositivos/
├── index.md
├── cf88/
│   ├── art-40-caput-original.md          # redação original de 1988
│   ├── art-40-p1-iii-ec-103-2019.md      # redação dada pela EC 103/2019
│   └── ...
├── ec-41-2003/
│   ├── art-2.md
│   ├── art-6.md
│   └── art-6a-ec-70-2012.md              # 6º-A com redação da EC 70/2012
├── lce-432-2008/
│   ├── art-20.md
│   └── ...
├── lce-1100-2021/
├── ece-146-2021/
└── lc-51-1985/
```

Convenções:

- **Um dispositivo por arquivo, na menor unidade efetivamente citada
  pelas regras** (decisão 2026-07-17): se a regra cita o artigo, o arquivo
  é o artigo; se cita parágrafo, inciso ou alínea, cria-se o arquivo nessa
  granularidade. A decomposição é **sob demanda** — não se fragmenta
  preventivamente a norma inteira. Frontmatter: `type: Dispositivo`,
  `norma`, `artigo`, `paragrafo`/`inciso`/`alinea` (quando houver),
  `redacao_dada_por` (norma alteradora, se não for a redação original),
  `vigencia_inicio` / `vigencia_fim` (quando revogado/alterado), `fonte`
  (URL oficial — Planalto, ALE/RO ou Diário Oficial).
- **Corpo = texto exato** do dispositivo, sem paráfrase. Se a redação mudou
  ao longo do tempo, cada redação é um arquivo separado (a regra cita a
  redação específica que a fundamenta).
- Regras passam a **linkar** seus dispositivos: no frontmatter de cada
  `regra-*.md`, um campo `dispositivos:` com a lista dos concept IDs
  citados (ex.: `- /dispositivos/cf88/art-40-p1-iii-ec-103-2019.md`), na
  forma de links absolutos do OKF (SPEC.md §5.1).

É isso que transforma a conferência de fundamentação de "abrir o site do
Planalto" em "diff entre o que a regra cita e o que o dispositivo diz" — e
uma mudança legislativa futura vira um diff no bundle de dispositivos que
aponta imediatamente quais regras são afetadas (backlinks).

Check proposto (após adoção): todo item de `dispositivos:` resolve para um
arquivo existente; toda regra auditada (P7 ≥ `revisada`) tem
`dispositivos:` não vazio.

### P4 — Formato canônico de citação [bloqueante após P3]

Definir uma forma canônica de citar cada norma (ex.: sempre
"LCE nº 1.100/2021", nunca "Lc 1100/21") e um vocabulário fechado de
normas citáveis (o corpus de ~16 normas acima; adições passam por PR no
`okf/dispositivos/`). E6 mostra que hoje a mesma norma aparece com pelo
menos 3 grafias — impossível de verificar mecanicamente.

A fundamentação em prosa continua livre; o que é canônico é o frontmatter
`dispositivos:` (P3). A prosa é para humanos; o frontmatter é para checks.

### P5 — Janelas temporais: consistência estrutural [bloqueante] + heurísticas semânticas provisórias

**Estrutural (bloqueante desde a Fase 0)**: para toda regra, datas
parseáveis e `DATA_ADM_APOS ≤ DATA_ADM_ATE`, `DATA_DIREITO_APOS ≤ DATA_DIREITO_ATE`. Isto é forma, não semântica — não depende de Q1/Q2, e
hoje as 112 passam. (Ver Q1: se o par é `[APOS, ATE]` exclusivo/inclusivo
ainda é a confirmar, mas a ordenação vale em qualquer convenção de
fronteira.)

**Datas-sentinela (decisão 2026-07-17)**: as sentinelas atuais
(`01/01/1910`, `01/01/1950`, `31/12/2099`) **serão mantidas**, para
preservar o round-trip com a planilha original, e documentadas como
**convenção observada**. **Não são interpretadas** — nem como datas reais
nem como limites abertos — antes da confirmação (P13): são apenas
**preservadas e excluídas das análises semânticas**. A P6 e qualquer
cálculo temporal **não rodam sobre esses casos** antes da resolução
correspondente na P13. Eventual migração para `null`/campos explícitos
fica para RFC/PR próprio.

**Heurística de datas vs. marcos legais (informativa/híbrida, NÃO
bloqueante)**: uma janela cuja fronteira não coincide com uma data de
vigência de norma conhecida gera **achado informativo** para conferência.
Isto **não** presume que toda fronteira deva coincidir com vigência formal
de dispositivo — pode haver publicação, produção de efeitos, regulamentação
local, data imediatamente anterior/posterior por inclusividade, ou outro
marco factual. A relação esperada só é confirmável com Q1/Q2 e a modelagem
dos dispositivos (P3); até lá, a heurística aponta E8 como achado a
conferir, nunca como veredito de erro de digitação nem como bloqueio.

### P6 — Cobertura e não-ambiguidade do espaço de decisão (após P13)

**Esta proposta não pressupõe que o catálogo seja uma função sobre um
conjunto de campos já escolhidos.** Quais campos são predicados de seleção,
se o resultado é uma regra ou várias candidatas, e onde vivem as condições
especiais são exatamente as questões Q3/Q4/Q5 — abertas. Portanto:

> Depois que a P13 identificar os predicados efetivamente usados pelo
> Sisprev, a P6 analisará a relação entre **perfis confirmados** e regras
> candidatas, **sem presumir cardinalidade única** (uma regra vs. várias
> candidatas vs. escolha do operador) **nem critérios de desempate**.

Dois fenômenos a reportar, uma vez que os predicados sejam conhecidos:

- **Lacuna**: perfil plausível para o qual nenhuma regra se aplica.
- **Sobreposição**: mais de uma regra ativa aplicável ao mesmo perfil. Não
  é previamente erro — pode representar **concurso legítimo, alternativas,
  ou outro comportamento a investigar**. A análise reporta a sobreposição
  **cujo tratamento não está documentado**; a auditoria decide caso a
  caso.

Proposta: um script de análise (`scripts/analisar_cobertura.py`),
**não-bloqueante** e considerando somente regras ativas (P2.1) e
**excluindo casos com sentinela não resolvida** (P5). Insumo de auditoria,
não critério pass/fail.

**Pré-requisito estrito: P13.** Sem saber quais campos são predicados e
quais são resultados/apresentação (Q3), a análise não é confiável — a P6
só roda depois que o mapa normativo classificar as colunas.

### P7 — Máquina mínima de estados de auditoria [proposta sujeita à confirmação do fluxo institucional]

**(Reformulada em 2026-07-17 — substitui a proposta original de 5+
estados.)** Substituir os booleanos soltos pelo **menor conjunto possível**
de estados (campo `status_auditoria` no frontmatter). A máquina e os
requisitos de `validada` são uma **proposta sujeita à confirmação do fluxo
institucional** (Q12) — não são inferidos da importação (ver nota sobre os
112 valores iguais adiante):

```
importada → revisada → validada
```

- `importada` — os invariantes de `revisada` **não estão (ou não estão
  mais) satisfeitos**. Definição negativa, de propósito: uma regra que já
  foi revisada e depois passa a constar em `regras_afetadas` de um achado
  bloqueante aberto (P14) volta a ser `importada` — o histórico de que um
  dia foi `revisada` fica no git, que é a trilha de auditoria. Não existe
  estado `inconsistente`.
- `revisada` — auditoria técnica concluída: **nenhum achado bloqueante
  aberto que inclua a regra em `regras_afetadas`** (P14), nome único **entre
  todas as regras, inclusive inativas** (P1 — unicidade global, não só
  entre ativas), `dispositivos:` vinculados e válidos (P3), sem igualdade
  material com outra ativa (P2) e, se inativa, inativação corretamente
  justificada (P2.1). `auditado_por`/`auditado_em` preenchidos com uma
  trilha real (P11). Deve também ser possível responder às cinco perguntas
  da spec semântica (P13.1) — as quatro primeiras (automático, manual,
  documentos, resultado) têm resposta **registrada em seções obrigatórias e
  não vazias** no corpo da regra, verificadas estruturalmente pelo CI; a
  quinta (dispositivos que justificam cada critério e efeito) fica com P3
  até esse bundle existir (Fase 2). **Não inclui campos coerentes (P9)**:
  como o próprio texto da P9 explicita (camada 3, "heurísticas semânticas
  provisórias" acima), suas co-ocorrências são informativas e nunca
  bloqueiam CI por mérito antes de a P13.2 confirmar a semântica exata dos
  campos envolvidos — listar P9 aqui, junto de invariantes que de fato
  bloqueiam, sugeria o contrário.
- `validada` — além de `revisada`, existe **documento verificável** que
  formaliza a validação, registrado em `atos_validacao`.

Não existem `em_revisao`, `aguardando_validacao` ou similares: são estados
de processo — descrevem a agenda de um humano, não um fato sobre a regra —
e quem rastreia "quem está trabalhando em quê" são os PRs e issues.

**As três dimensões são ortogonais e cada uma tem um dono:**
`status_auditoria` = progresso comprovado; os **achados** (conceitos em
`achados/`, P14) = qualidade (a existência de problemas é representada por
achados, nunca pelo estado da regra); `status_regra` (P2.1) =
**participação/autonomia do registro no catálogo**. Note: `status_regra`
**não** é vigência/aplicabilidade temporal — essa é outra dimensão, e vive
nas janelas de datas da regra (P5).

Exemplo (campos provisórios — ver ressalva abaixo):

```yaml
status_regra: ativa
status_auditoria: validada
atos_validacao:
  - tipo: parecer          # tipo do ato
    autoridade: PGE        # autoridade emissora
    identificador: "..."   # nº do processo/documento
    fonte: SEI             # onde o documento é verificável (a confirmar)
```

`atos_validacao` é uma **lista** (um item por ato institucional), com
`tipo`, `autoridade`, `identificador` e `fonte`. **Ressalvas a confirmar
antes de fechar o invariante de `validada`** (Q12, fluxo institucional):

- **Não se fixa o SEI** como fonte única até confirmação — pode haver
  documento relevante fora do SEI. O invariante exige documento
  **verificável**, cuja `fonte` é registrada, não necessariamente `SEI`.
- **112× `FALSE/FALSE` na importação não demonstra** que PGE e Presidência
  sejam um único ato: ausência de casos divergentes numa base 100% não
  validada é falta de evidência, não evidência de unicidade. Se são um ou
  dois atos obrigatórios, e se ambas as autoridades são necessárias, é a
  confirmar — e muda o **invariante** de `validada` (exigir uma entrada de
  cada autoridade), não a máquina de estados.

Invariantes \[bloqueantes\]:

- **Invariantes valem continuamente, não só na transição.** Estado é
  contrato: o CI verifica em todo commit que cada regra satisfaz os
  invariantes do estado que declara (`P7_ESTADO_INVALIDO` quando não). Uma
  regra `revisada` que passa a constar em `regras_afetadas` de um achado
  bloqueante aberto (P14) vira violação, forçando um commit explícito de
  rebaixamento para `importada` — o rebaixamento é *derivável* dos
  invariantes, sem precisar de estado extra. O estado da regra depende do
  **join com `achados/*`**, não de um campo interno à regra.
- Transição para `validada` exige `atos_validacao` não vazio, com documento
  verificável identificável (fonte registrada, não fixada em SEI — ver
  ressalvas acima) — ninguém marca validada sem apontar o ato que a
  sustenta.
- Achados são conceitos próprios em `achados/` (P14), não seções no corpo
  da regra.

**Convenção de processo (2026-07-17, não verificada por CI)**: mudança de
`status_auditoria` deveria ser commit próprio (não misturada com correção
de conteúdo), com a justificativa na mensagem. Esta recomendação **não**
está marcada `[bloqueante]` porque não há gate de CI que a implemente —
verificar isso exigiria inspecionar o diff de cada commit da regra, não
apenas o estado final do documento, o que está fora do escopo da Fase 1.
Continua sendo boa prática de auditoria, mas hoje é responsabilidade do
revisor humano do PR, não do CI. Se um gate de commit vier a ser
implementado, esta nota deve ser promovida de volta para a lista de
invariantes bloqueantes.

**Regra de desenho para estados futuros** (catraca contra proliferação):

> Um novo estado só é criado quando muda os invariantes exigidos pelo CI
> ou representa um ato institucional distinto.

Leitura estrita: os dois critérios são um só teste — **estado novo exige
invariante novo verificável**. Um "ato institucional distinto" só qualifica
porque produz um artefato conferível (o documento de validação), e a
exigência desse artefato *é* o invariante novo; ato sem artefato
verificável não vira estado. Dois estados com o mesmo conjunto de
invariantes são o mesmo estado e devem ser fundidos.

Qualquer PR futuro que proponha um estado novo deve preencher este
template:

> **Estado proposto**: X. **Invariantes de CI que passam a valer**: […].
> **Ato institucional**: […]. **Documento verificável exigido**: […].
> **Por que nenhum estado existente cobre isso**: […].

### P8 — Vocabulários fechados: administrativos agora, de domínio após P13

Os **campos administrativos** têm vocabulário fechado e verificado desde a
Fase 0 (são estrutura, não semântica de domínio): `status_regra`
(`ativa`/`inativa`), `motivo_inativacao` (`duplicata` | `erro_de_importacao`
— **sem** `revogada`: encerramento temporal não é inativação, ver P2.1) e
`status_auditoria` (`importada`/`revisada`/`validada` — P7).

Os **campos de domínio** (`TIPO DE BENEFICIO`, `TIPO_CALCULO`, `SEXO`,
`TIPO`, campos S/N e TRUE/FALSE) terão seus vocabulários **fixados pelo
mapa P13.2**, campo a campo — até lá, o validador detecta valores fora do
conjunto observado como ocorrência, sem tratá-los como erro (um valor não
visto na importação pode ser legítimo). `"Não identificado"` em
`TIPO_CALCULO` (13 registros — E3) **não tem severidade predeterminada**:
até a Q10 ser respondida, é ocorrência a investigar (pode significar dado
faltante,
estado legado, não aplicável, cálculo externo/manual, ou convenção válida);
o mapa P13.2 decide, campo a campo, quando o valor é admissível e quando —
se — bloqueia a `revisada`.

**Enums de achados**: `situacao` (`aberto` | `resolvido`), `severidade`
(`bloqueante` | `informativo`), `verificacao` (`mecanica` | `manual` |
`hibrida`) e `natureza` (enum fechado, **valores a definir na
implementação** após examinar os casos reais — p.ex. jurídica, dados,
modelagem, processo) — todos declarados no doc Dataset. O schema completo
do frontmatter de `type: Achado` está na **P14**, que substitui o antigo
"schema mínimo de achados" embutido nas regras: como o invariante de
`revisada` depende de "nenhum achado bloqueante aberto que afete a regra",
a severidade é estrutural, e o achado precisa ser um conceito verificável
— não texto livre no corpo de um `regra-*.md`.

### P9 — Coincidências entre campos: detecção provisória, semântica adiada à P13

**Nenhum dos padrões abaixo é bloqueante antes da P13** (princípio da
semântica adiada, topo do RFC): são **co-ocorrências de valores** que o
detector **reporta** como ocorrências; se o auditor decidir abrir um
achado, ele será **informativo ou híbrido** (P14) e **escrito à mão** — a
*relação obrigatória* entre os campos só nasce quando o mapa P13.2
confirmar o que cada campo significa (Q6, Q7, Q10). Até lá, o detector
aponta o padrão; não afirma incoerência nem autora o achado.

Padrões detectados (constatação mecânica, entre parênteses a questão que
os mantém provisórios):

- `INTEGRAL = S` com `FUNDAMENTACAO_INTEGRAL` vazia (hoje: 0 ocorrências) —
  a obrigatoriedade depende de Q6/Q7;
- `INTEGRAL = N` com `FUNDAMENTACAO_PROPORCIONAL` vazia (hoje: **17
  ocorrências** — E5) — a obrigatoriedade depende de Q6/Q7; granularidade
  do(s) achado(s) decidida após investigação (a coincidência do código de
  detecção não prova identidade de causa ou resolução);
- co-ocorrência de `SEXO` vazio, `INTEGRAL` vazio e `TIPO_CALCULO = "Não identificado"` (13 registros — E3/E4) — **evidência observada, não regra
  de admissibilidade**; até a Q10, valores vazios ou `Não identificado`
  são ocorrências a investigar **sem significado ou severidade
  presumidos**; o mapa P13.2 definirá, campo a campo, se o valor é
  permitido, o que significa e quais efeitos produz no estado de auditoria;
- fundamentação que menciona sexo específico ("mulher", "alínea b")
  aparentemente incompatível com o campo `SEXO` (E7) — achado **híbrido**:
  o detector comprova só a aparência textual, **nunca conclusão jurídica**;
  não diz qual campo está errado (nem se algum está) — a auditoria
  determina.

### P10 — Validação executável (biblioteca pura + CLI + `pytest`)

**Três operações conceitualmente distintas** (nunca misturadas no mesmo
comando — princípio da autoria humana):

1. **detectar** — operação **pura**, sem escrita no bundle; carrega as
   fontes e emite **ocorrências mecânicas** (`Detection`) em memória/JSON,
   cada uma com um `fingerprint` estável (P14.6);
2. **validar** — operação **pura**, sem escrita; verifica documentos
   (schema, invariantes), relações e a cobertura das detecções, retornando
   `Violation`s com **códigos estáveis** (ex.:
   `P2_IGUALDADE_MATERIAL_ATIVA`, `P21_INATIVA_SEM_MOTIVO`,
   `P21_GRUPO_SEM_ATIVA`, `P21_GRUPO_MULTIPLAS_ATIVAS`,
   `P21_DUPLICATA_SEM_GRUPO`, `P21_DIVERGE_DO_ORIGINAL`,
   `P7_ESTADO_INVALIDO`, `P14_ACHADO_SEM_DETECCAO`,
   `P14_DETECCAO_SEM_ACHADO`);
3. **derivar** — gera **apenas** artefatos integralmente calculáveis das
   fontes (índices, CSV, relatórios), idealmente com modo `--check` no CI.

O validador **não cria nem atualiza `achado-*.md`**, e **não modifica
índices como efeito colateral**. Um processo que valida e depois exige
`git diff` estaria misturando validação com geração; por isso derivar é um
comando à parte.

**Ferramentas de validação.** A lógica normativa executável vive numa
**biblioteca Python reutilizável e sem efeitos colaterais**: ela carrega o
bundle, valida schema/invariantes, executa detectores e retorna objetos
estruturados (`Detection`, `Violation`); não escreve arquivos, não chama
`sys.exit()` e não conhece o GitHub Actions. O **schema do frontmatter** é
um modelo Python tipado reutilizável (Pydantic ou equivalente) — validações
entre campos ficam no modelo (`manual` proíbe `detector`; `mecanica`/
`hibrida` exigem `deteccoes`; campos desconhecidos tratados
deliberadamente); invariantes **entre** documentos ficam na camada de
bundle. A **CLI** (`scripts/validar_regras.py`) é fina e **somente
leitura**: carrega o bundle, chama a biblioteca, imprime texto/JSON e
encerra com 0/1 — não autora `.md`, índices ou qualquer fonte. O **`pytest`**
é o runner de contrato no CI (job `validar-regras`): testa unitariamente os
detectores, parametriza o contrato de todos os `achado-*.md` e executa a
correspondência bidirecional sobre o **bundle real** — chamando a
biblioteca, **nunca** reimplementando a lógica nem mantendo uma segunda
representação manual das detecções esperadas. **Hypothesis** é complemento
opcional (não bloqueante) para propriedades dos detectores e do round-trip
(permutação da ordem não muda `fingerprint`; alterar campo ignorado não
muda P2; alterar campo semântico muda P2; serializar/parsear preserva o
modelo). Artefatos derivados (índices/CSV) são gerados por comando separado
(ex.: `scripts/gerar_indices.py`) e conferidos no CI com
`git diff --exit-code`.

**Nem todo check é bloqueante** — a validação opera nas quatro camadas do
princípio da semântica adiada (topo do RFC):

1. **invariantes estruturais confirmados** (identidade/proveniência/
   sequência, round-trip, unicidade de `id`, ordenação de datas P5, schema
   de achados P14) — **exit code ≠ 0**, bloqueiam o CI desde a Fase 0;
2. **detectores mecânicos neutros** (igualdade material P2, valores
   ausentes, grafias divergentes) — **reportam ocorrências**; o achado é
   escrito pelo auditor. Não falham o CI por si; o que falha é a
   *incoerência* achado↔detecção (bidirecionalidade abaixo);
3. **heurísticas semânticas provisórias** (co-ocorrências da P9, datas fora
   dos marcos conhecidos P5) — o detector reporta a ocorrência; o achado,
   se aberto, é **informativo/híbrido** e escrito pelo auditor, **nunca**
   exit ≠ 0 por mérito;
4. **regras semânticas confirmadas na P13.2** — migram para a camada 1
   (bloqueantes) só depois de documentadas no mapa.

O exit code ≠ 0 vem, portanto, da camada 1 e da quebra de
bidirecionalidade — não de uma interpretação provisória de campo, nem da
ausência de um artefato derivado (isso é tarefa do comando de derivar).

A implementação da P7 é uma tabela **estado → conjunto de predicados**,
verificada continuamente para toda regra (`invariantes(status(r)) ⊆ fatos(r)`) — não um verificador de transições. É isso que torna o
rebaixamento derivável (P7) e as violações re-verificáveis em qualquer
commit.

**Os arquivos em `achados/` (P14) são a baseline auditável (decisão
2026-07-17)** — não existe baseline paralela (sem
`data/baseline-violacoes.json`): as ocorrências pré-existentes da
importação (E1–E8) vivem como conceitos `type: Achado` (P14),
**escritos pelo auditor**. O CI faz **verificação bidirecional** entre os
achados mecânicos e as **detecções** — sobre `fingerprint`s, não sobre
igualdade exata entre `frozenset(regras_afetadas)` e o grupo retornado pelo
detector (P14.6):

- toda detecção mecânica atual que exige registro deve estar referenciada
  (por `fingerprint`) por um achado aberto, ou explicitamente dispensada por
  uma decisão registrada (`P14_DETECCAO_SEM_ACHADO` — detecção sem achado =
  regressão, bloqueia o CI);
- todo `fingerprint` em `deteccoes` de um achado aberto deve continuar
  sendo emitido pelo detector (`P14_ACHADO_SEM_DETECCAO` quando o detector
  não o reproduz mais — o achado precisa ser **resolvido ou atualizado no
  mesmo PR** que eliminou a ocorrência);
- a relação **não** é 1:1: um achado pode reunir várias detecções com causa
  comum; uma detecção deve estar coberta por exatamente uma investigação
  aberta, salvo regra explícita em contrário. O CI **não** decide a
  severidade nem a granularidade da investigação.

Assim o CI não nasce vermelho (o legado está documentado como achados
abertos, escritos à mão) e bloqueia regressões desde o dia 1 — e o conjunto
de achados abertos encolhe conforme a auditoria corrige o legado, com o
próprio CI forçando a atualização dos documentos. Um relatório JSON global
pode existir apenas como **artefato derivado** (gerado pelo comando de
derivar para consumo externo), nunca como fonte normativa paralela.

### P11 — Trilha de auditoria por regra

Convenções de registro (complementa P7):

- `log.md` no diretório `regras/` (formato OKF SPEC.md §7) com o histórico
  agregado de mudanças por data;
- No frontmatter de cada regra: `auditado_por` e `auditado_em` (preenchidos
  na transição para `revisada`);
- Inconsistências entre regras (ex.: um problema que afeta duas ou mais)
  são **achados transversais versionados no bundle** (P14) — um
  `type: Achado` com várias `regras_afetadas`, com histórico git próprio.
  Issues do GitHub, documentos SEI ou outras evidências externas são
  **opcionais e complementares** (referenciadas no corpo do achado), não a
  fonte da relação.

### P12 — CSV derivado estendido: colunas originais + campos administrativos [bloqueante]

**Decisão (2026-07-17)**: `data/regras-sisprev.csv` (o export derivado do
bundle) passa a conter **as 27 colunas originais E os campos
administrativos novos** — `status_regra`, `motivo_inativacao`,
`status_auditoria` (e os demais campos de P7/P11 conforme forem
adotados) — como colunas adicionais ao final.

Sem isso, o export do estado atual mentiria por omissão: mostraria 112
regras aparentemente operacionais, sem revelar quais foram inativadas ou em
que estágio de auditoria cada uma está. O CSV derivado existe justamente
para ser "o conteúdo exato das regras atuais" em forma plana — e o estado
atual inclui a dimensão administrativa.

Consequências:

- Só o **congelado** (`data/raw/`) tem formato imutável; o derivado é
  regenerado por script e seu formato evolui junto com o bundle.
- `okf_to_csv.py` emite as colunas administrativas com defaults explícitos
  para regras que ainda não têm os campos (`status_regra: ativa`,
  `status_auditoria: importada`, demais vazios) — o CSV derivado nunca tem
  célula "desconhecida".
- O teste de round-trip do bootstrap (CSV congelado → bundle → CSV) segue
  comparando apenas as 27 colunas originais; o teste de sincronia do
  derivado (`tests/test_bundle_sync.py`) compara o CSV completo, com as
  colunas novas.

### P13 — Especificação semântica de `type: Regra` + mapa normativo CSV → OKF

O doc Dataset atual descreve as 27 colunas isoladamente, mas não define
como elas **se combinam**, quais são avaliadas pelo Sisprev, quais dependem
de análise manual/jurídica e qual consequência cada regra produz. **O
catálogo não deve ser tratado como motor decisório integralmente
automático**: a hipótese de trabalho (a confirmar — Q3/Q4/Q5) é que uma
regra pode ser apenas parcialmente parametrizada — o Sisprev usaria os
campos estruturados para filtrar ou apresentar regras candidatas, enquanto
requisitos não parametrizáveis seriam verificados manualmente, com base em
documentos e análise jurídica. Nada disso é afirmado como funcionamento
confirmado.

Definição de trabalho (sem antecipar o funcionamento concreto, que ainda
deve ser investigado — ver Q1–Q12 abaixo):

> Uma regra reúne critérios estruturados usados pelo Sisprev, requisitos
> adicionais que podem depender de prova ou análise manual, consequências
> aplicadas depois de sua seleção e a fundamentação jurídica
> correspondente. A correspondência automática dos campos estruturados não
> equivale, por si só, à conclusão jurídica de que a regra se aplica ao
> caso concreto.

Dois entregáveis distintos:

#### P13.1 — Spec semântica (`docs/spec/regra.md`)

O contrato semântico separa explicitamente, para o tipo `Regra`, as
categorias abaixo. **Só identidade/proveniência e estado estão
confirmados**; a atribuição de cada campo de domínio a uma categoria é
**hipótese/candidato de classificação, a confirmar campo a campo pela
investigação** (Q6, Q9) — não classificação normativa já decidida:

- **identidade e proveniência** (confirmado): `id` (identidade estável),
  `row_index` (proveniência), `nome` (rótulo humano — P1), vínculo com a
  linha congelada;
- **critérios parametrizados** (a confirmar quais — Q3): campos que o
  Sisprev efetivamente avalia automaticamente;
- **requisitos de verificação manual/jurídica** (a confirmar quais — Q5):
  fatos, documentos ou enquadramentos não decididos pelos campos
  estruturados;
- **resultado/efeitos da seleção** (*candidatos*, Q6): p.ex. `integral`,
  `tipo_calculo`, `paridade`, adicional — a definição operacional de cada
  um e se é resultado ou também predicado é justamente Q6;
- **comportamento de implementação/apresentação** (*candidatos*, Q9): p.ex.
  `simulavel`, visibilidade na DTC, `TabelaPontuacao`, relatório de
  reserva, `atualmente_no_sistema` — se são condições, efeitos ou controles
  de interface é justamente Q9;
- **fundamentação e dispositivos** (P3);
- **estado no catálogo e estado da auditoria** (confirmado — P2.1/P7), sem
  confundir com aplicabilidade temporal.

A spec **não exige que tudo seja parametrizado**; exige que a fronteira
entre **automático**, **manual** e **desconhecido** seja explícita. Para
cada regra `revisada` (P7), deve ser possível responder, em linguagem
humana:

1. Quais fatos o sistema verifica automaticamente?
2. Quais fatos devem ser confirmados manualmente?
3. Quais documentos/evidências sustentam essa confirmação?
4. O que o sistema faz depois que a regra é selecionada?
5. Quais dispositivos jurídicos justificam cada critério e efeito?

Isso **deve** aparecer no corpo de cada regra `revisada`, em quatro seções
convencionais de nível 1 (mesmo padrão de `FUNDAMENTACAO_*` — heading único,
sem aninhamento; o parser do bundle só reconhece `# Heading`, não `##`):

```markdown
# Critérios avaliados pelo Sisprev

# Requisitos de verificação manual

# Documentos ou evidências necessários

# Resultado após a seleção
```

**Decisão (revisão da PR #7, round 2)**: a existência textual das quatro
seções é uma **invariante estrutural bloqueante de `revisada`**
(`P7_ESTADO_INVALIDO` quando ausente ou vazia) — o CI confere que a
resposta *existe e não está vazia*, nunca seu mérito ou correção jurídica.
Antes desta decisão, a spec afirmava que a fronteira deveria ser
"explícita para cada regra `revisada`" enquanto tratava estas seções como
"opcionais e prospectivas" — as duas afirmações não se sustentavam juntas:
sem um registro obrigatório, uma regra chegava a `revisada` apenas com
`auditado_por`/`auditado_em`, sem nenhum conteúdo semântico auditável. A
seção "Quais dispositivos jurídicos justificam..." (pergunta 5) permanece
fora deste requisito — depende de P3 (`okf/dispositivos/`), ainda não
construído (Fase 2); quando existir, deve se tornar a quinta seção
obrigatória do mesmo jeito.

O corpo da regra **não** contém seção `# Achados`: problemas de auditoria
são conceitos próprios em `achados/` que apontam para a regra via
`regras_afetadas` (P14), nunca embutidos no `regra-*.md`.

#### P13.2 — Mapa normativo das 27 colunas [bloqueante]

Hoje o mapeamento CSV → bundle existe de forma implícita no código
(`NOME` → campo de nome; `FUNDAMENTACAO_*` → seções do corpo; demais
colunas → `slugify_column()`). Permite round-trip, mas não é especificação
legível. O mapa deve enumerar **todas as 27 colunas**, sem exigir que o
leitor deduza a transformação do slug, com no mínimo:

| Coluna CSV original      | Destino no `.md`           | Local       | Tipo/enum | Categoria semântica | Semântica de vazio | Transformação ida            | Transformação volta |
| ------------------------ | -------------------------- | ----------- | --------- | ------------------- | ------------------ | ---------------------------- | ------------------- |
| `NOME`                   | `nome`                     | frontmatter | string    | identidade humana   | não vazio          | cópia direta (`NOME ↔ nome`) | `nome` → `NOME`     |
| `FUNDAMENTACAO_INTEGRAL` | `# Fundamentação Integral` | corpo       | texto     | fundamentação       | a definir          | coluna → seção               | seção → coluna      |
| `TabelaPontuacao`        | `tabelapontuacao`          | frontmatter | S/N       | a investigar (Q9)   | a definir          | cópia direta                 | cópia direta        |

Para cada coluna, o mapa também esclarece: se é **entrada**, **resultado**,
**controle de implementação**, **apresentação**, **proveniência** ou
**auditoria**; se participa da seleção automática; se é apenas informativa;
se vazio significa `desconhecido`, `não aplicável`, `qualquer valor`,
`pendente` ou erro; valores permitidos e normalização; sentinelas e
defaults; inclusividade/exclusividade de limites de data; e se há
dependência de configuração externa ausente do CSV. (Enquanto a resposta
for "a investigar", o mapa registra isso explicitamente — fronteira do
desconhecido declarada, nunca implícita.)

O mapa é **fonte única usada pelo código**, não tabela editorial
duplicada: a combinação dispersa de `BODY_COLUMNS`, `BODY_HEADINGS`,
`COLUMN_SCHEMA` e `slugify_column()` é substituída por uma estrutura
declarativa única, da qual derivam a importação CSV → OKF, a exportação
OKF → CSV, a tabela `# Schema` do Dataset, a validação de cobertura do
mapeamento e os testes de round-trip.

Invariantes de CI \[bloqueantes\]:

- toda coluna original aparece exatamente uma vez no mapa;
- todo destino declarado existe e é lido na volta;
- nenhum campo original é descartado ou duplicado sem regra explícita;
- a ordem original das 27 colunas é preservada no export;
- o mapeamento ida-e-volta é bijetivo para os campos legados;
- campos administrativos novos (P2.1/P7/P12) ficam em namespace/lista
  separada, jamais confundidos com a origem congelada.

#### Questões semânticas abertas (Q1–Q12) — a investigar, não a responder aqui

O RFC lista estas questões **sem respondê-las**; respondê-las é trabalho
de investigação (junto ao Sisprev, à documentação e à análise jurídica), e
cada resposta alimenta a spec P13.1 e o mapa P13.2:

01. **Q1** — `DATA_*_APOS` é limite exclusivo e `DATA_*_ATE` inclusivo? O
    nome sugere isso, mas é preciso confirmar no Sisprev.
02. **Q2** — Qual fato jurídico concreto corresponde a `DATA_DIREITO`:
    implementação dos requisitos, data do óbito, data do laudo,
    requerimento, ou outra referência conforme o benefício?
03. **Q3** — Quais campos realmente participam da seleção automática e
    quais apenas configuram o cálculo ou a apresentação?
04. **Q4** — Quando vários registros passam pelos filtros estruturados, o
    Sisprev retorna uma regra, várias candidatas, ou opções entre as quais
    o operador escolhe a juridicamente aplicável/mais vantajosa?
05. **Q5** — Onde vivem requisitos não presentes no CSV — idade mínima,
    tempo de contribuição, pedágio, atividade policial, natureza da
    incapacidade, exposição especial etc.? Em código, tabelas externas,
    outra tela, ou análise manual?
06. **Q6** — `integral`, `tipo_calculo` e `paridade` são dimensões
    independentes? Qual é a definição operacional exata de cada uma?
07. **Q7** — Por que uma mesma linha pode conter fundamentação proporcional
    E integral? São textos alternativos, ramos jurídicos, material de
    exibição, ou apenas legado da planilha?
08. **Q8** — Em pares como `regra-0006`/`0007`, o critério que distingue os
    resultados está parametrizado em outro lugar ou é decisão manual?
09. **Q9** — O que significam precisamente `simulavel`, `TabelaPontuacao`,
    `Requisitos da IN Nº 5/2020`, `TIPO_REMUN`, os campos de visibilidade
    DTC e o relatório de reserva? São condições, efeitos, ou controles de
    interface?
10. **Q10** — Como distinguir `AMBOS`, vazio, desconhecido e não aplicável
    em `SEXO`, `INTEGRAL`, `TIPO_CALCULO` e demais campos?
11. **Q11** — Quais documentos/evidências são esperados para cada
    requisito manual, e onde a conclusão do caso concreto é registrada?
12. **Q12** — Qual é a fronteira entre (a) correspondência automática de
    uma regra ao caso, (b) verificação manual dos fatos do caso, e (c)
    validação jurídica da própria configuração da regra?

#### Relação com as demais propostas

A spec semântica é **pré-requisito** para:

- **P6** — não dá para analisar cobertura e sobreposição sem saber quais
  campos são predicados e quais são resultados (Q3);
- **P9** — coerência interna depende da definição exata dos campos (Q6,
  Q10); até lá, os checks da P9 são provisórios, baseados na melhor
  interpretação corrente, e revisáveis quando o mapa P13.2 os formalizar;
- **auditoria de mérito** — o revisor precisa saber o que o sistema faz
  automaticamente e o que permanece para análise manual (Q11, Q12);
- **eventual simulador/motor futuro** — sem que este RFC presuma que o
  catálogo já seja um motor completo.

O ponto central: o RFC não deve apenas dizer quando uma regra está "bem
preenchida" — deve exigir uma explicação verificável de **como a regra
participa do processo decisório híbrido do Sisprev**, preservando
explicitamente tudo o que depende de análise humana e jurídica.

### P14 — Achados como conceitos OKF

Os achados de auditoria são **conceitos próprios** no bundle, não seções
embutidas nos `regra-*.md`. Isso resolve os achados manuais, jurídicos e
**transversais** (um problema que afeta várias regras, ou que não pode ser
reproduzido integralmente por código): fonte única + derivação, o mesmo
princípio que este RFC já aplicou a `regra_canonica` e a `title`/`nome`.

#### P14.1 — Localização e fonte única

```text
okf/regras-sisprev/
├── regras/
├── achados/
│   ├── index.md          # listagem gerada, sem frontmatter (SPEC.md §6)
│   ├── achado-0001.md
│   └── ...
└── regras-sisprev.md
```

A relação achado ↔ regra existe **apenas** no achado, em `regras_afetadas`.
As regras **não** carregam `achados:` — evita duas listas que possam
divergir. Índices e backlinks por regra são **gerados** (ver P14.7).

#### P14.2 — Schema (`type: Achado`), escrito à mão

O achado é uma **fonte autoral**: `nome`, `severidade`, `natureza`,
`regras_afetadas`, descrição, evidências e questão a investigar são
**escritos por uma pessoa** (princípio da autoria humana). Nenhum comando
gera esses campos.

```yaml
---
type: Achado
id: achado-0001
nome: Possível incompatibilidade entre sexo e fundamentação
situacao: aberto            # aberto | resolvido
severidade: informativo     # bloqueante | informativo (default humano: informativo)
verificacao: hibrida        # mecanica | manual | hibrida
deteccoes:                  # evidência mecânica que originou o achado (P14.6)
  - detector: P9_SEXO_FUNDAMENTACAO
    fingerprint: sha256:...  # obrigatório se mecanica/hibrida; ausente se manual
natureza: juridica          # enum fechado, valores a definir na implementação
regras_afetadas:            # alcance da investigação humana — pode divergir das detecções
  - /regras/regra-0078.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---
```

Corpo convencional: `# Descrição`, `# Evidências`, `# Questão a investigar`,
`# Resolução` (preenchida ao resolver).

**Scaffold opcional.** Um utilitário pode apenas **reservar o próximo `id`**
e produzir um esqueleto incompleto — `nome: TODO`, `severidade: TODO`,
`natureza: TODO`, `regras_afetadas: []` — **sem defaults semânticos**. Esse
scaffold **não é válido** para o CI enquanto os `TODO` permanecerem: ele
economiza a numeração, não a autoria.

#### P14.3 — Ciclo de vida

- `id` sequencial (`achado-NNNN`), **estável, nunca reutilizado nem
  renumerado** — igual ao dos `regra-*`;
- achado `resolvido` **nunca é apagado** — é a trilha de auditoria (o
  histórico de cada investigação fica legível em `git log`);
- `situacao: resolvido` exige `resolvido_em`, `resolvido_por` e a seção
  `# Resolução` não vazia.

#### P14.4 — Relação com regras: `deteccoes` ≠ `regras_afetadas`

- `regras_afetadas` é a **única** fonte de verdade da relação achado↔regra
  (o *alcance da investigação humana*); toda regra referenciada deve
  existir;
- `deteccoes` registra a **evidência mecânica** que originou o achado —
  cada entrada é `detector` + `fingerprint` estável. São dados
  **distintos**: `regras_afetadas` pode ser mais amplo (a investigação
  revela regras afetadas além das detectadas) ou reunir várias detecções;
- **granularidade**: um achado representa uma questão investigável e
  resolvível **como unidade**, não necessariamente uma mensagem individual
  do detector. A coincidência do código de detecção **não prova**
  identidade de causa ou resolução. Problemas independentes → achados
  distintos; uma causa comum afetando várias regras → um achado
  transversal reunindo várias `deteccoes`; um grupo de igualdade material →
  um achado conjunto enquanto a investigação for única — mas **a
  granularidade é decidida pelo auditor após investigação**, não
  predeterminada nem imposta pela relação 1:1 detector↔achado (as 17
  ocorrências de E5, p.ex., podem ter causa comum ou causas diferentes).

#### P14.5 — Verificação mecânica, manual e híbrida

- `verificacao: mecanica` — a condição é integralmente reproduzível por um
  `detector` (ex.: `P2_IGUALDADE_MATERIAL_ATIVA`), referenciado em
  `deteccoes` por `fingerprint`. O CI verifica a correspondência
  bidirecional (P14.6). O detector **reporta**; o achado é **escrito** pelo
  auditor.
- `verificacao: manual` — jurídica/documental; **sem** `deteccoes`. O CI
  **não decide o mérito**: valida estrutura, referências, estado,
  evidências mínimas e efeitos sobre as regras.
- `verificacao: hibrida` — a máquina detecta a **condição** que originou o
  alerta (ex.: `P9_SEXO_FUNDAMENTACAO` — a aparência de incompatibilidade)
  e a registra em `deteccoes`, mas a **conclusão** é humana. O CI pode
  exigir que o padrão ainda seja reproduzido enquanto o achado estiver
  aberto, mas **não conclui que existe erro jurídico** — o `fingerprint`
  comprova só a condição mecânica, nunca o mérito.

#### P14.6 — Invariantes de CI [bloqueantes] e `fingerprint`

Cada ocorrência mecânica é representada por um `fingerprint` **estável**,
derivado **apenas** de `detector` + versão do detector + sujeito mecânico
canônico (ordem de leitura irrelevante). É esse identificador — não o
conjunto `regras_afetadas` — que ancora a bidirecionalidade.

- `id` sequencial, estável, nunca reutilizado ou renumerado;
- achados resolvidos nunca são apagados;
- `regras_afetadas` é a única fonte da relação; toda regra referenciada
  existe;
- `situacao: resolvido` exige `resolvido_em`, `resolvido_por` e `# Resolução`;
- `deteccoes` (com `fingerprint`) obrigatório para `mecanica` e `hibrida`;
  **proibido** para `manual`;
- **bidirecional (sobre `fingerprints`, não 1:1)**: toda detecção mecânica
  atual que exija registro está referenciada por um achado aberto
  (`P14_DETECCAO_SEM_ACHADO`), e todo `fingerprint` de achado aberto
  continua sendo emitido pelo detector (`P14_ACHADO_SEM_DETECCAO`); uma
  detecção é coberta por **exatamente uma** investigação aberta, salvo
  regra explícita — dois achados abertos reivindicando a mesma detecção
  sem relação declarada é violação;
- regra `revisada` ou `validada` não pode constar em `regras_afetadas` de
  nenhum achado `bloqueante` `aberto` (join com a P7);
- abertura de achado, resolução e eventual rebaixamento da regra afetada
  acontecem **coerentemente no mesmo PR**;
- backlinks existem somente em índices/relatórios gerados, nunca dentro das
  regras;
- `natureza` é enum fechado, com valores **definidos na implementação**
  após examinar casos reais (declarados no doc Dataset — P8).

Esses invariantes são provados por **`pytest` sobre o bundle real**,
chamando a biblioteca de domínio (P10) — testes parametrizados por
`achado-*.md` para o schema/ciclo de vida e testes de correspondência
(`uncovered_detections(bundle) == []`, `stale_detection_refs(bundle) == []`) para a bidirecionalidade. Os testes **não** reimplementam a lógica nem
mantêm uma segunda lista das detecções esperadas.

#### P14.7 — Índices e relatórios derivados

Apenas artefatos deriváveis são **gerados**, e por um comando separado (o
"derivar" da P10), nunca pela validação: `achados/index.md` (listagem) e os
backlinks por regra saem de `regras_afetadas`, jamais escritos à mão nem
armazenados dentro dos `regra-*.md`. Um relatório JSON global, se existir, é
**artefato derivado** para consumo externo, jamais fonte normativa paralela
(P10). O corpo autoral do achado (`# Descrição`, `# Evidências`, `# Questão a investigar`, `# Resolução`) **nunca** é gerado.

#### Formulação-resumo

> Os achados são conceitos próprios em `okf/regras-sisprev/achados/`,
> **escritos e revisados diretamente por pessoas**. Cada achado lista as
> regras afetadas e as detecções mecânicas que o originaram, e possui
> situação, severidade, natureza, forma de verificação, evidências e
> resolução. O código **detecta** fatos mecânicos e **valida** contratos,
> mas não autora achados; o `pytest` prova continuamente a coerência entre
> as detecções da biblioteca e os achados escritos à mão. Para achados
> mecânicos, o CI verifica a correspondência bidirecional sobre
> `fingerprints`. Achados manuais ou jurídicos não são decididos pelo CI,
> mas seus efeitos sobre os estados das regras são aplicados e verificados
> automaticamente.

______________________________________________________________________

## O que este RFC não propõe

- **Não** propõe corrigir o mérito jurídico de nenhuma regra — isso é o
  trabalho de auditoria que estes critérios estruturam.
- **Não** propõe alterar `data/raw/regras-sisprev.csv` (congelado, sempre).
- **Não** propõe motor de decisão/simulador — P6 analisa cobertura, não
  executa regras.
- **Não** presume que o catálogo seja (ou deva virar) um motor decisório
  integralmente automático — o processo do Sisprev é híbrido, e a P13
  exige exatamente que a fronteira automático/manual/desconhecido fique
  explícita, preservando o que depende de análise humana e jurídica.

## Sequenciamento sugerido

1. **Fase 0** (este RFC aceito): P10 nas **camadas 1 e 2** (invariantes
   estruturais de P1-identidade/P2-detecção/P5-estrutural/P14-schema +
   detectores mecânicos neutros que **apenas reportam ocorrências**) + P12
   (estender o CSV derivado) + **P13.2** (mapa normativo como estrutura
   declarativa única, substituindo
   `BODY_COLUMNS`/`BODY_HEADINGS`/`COLUMN_SCHEMA`/`slugify_column` — os
   conversores e testes passam a derivar dele; inclui `NOME ↔ nome`) +
   **P14** (infraestrutura de `achados/`, o schema `type: Achado`, a
   biblioteca de domínio pura, a CLI somente-leitura e os detectores com
   `fingerprint`). O **registro dos achados iniciais** (ocorrências legadas
   E1–E8) é **trabalho autoral assistido pelas saídas dos detectores** —
   cada `achado-*.md` é escrito à mão a partir da evidência mecânica, **sem
   antecipar conclusões nem severidade** (default humano: `informativo`),
   com a verificação bidirecional da P10 sobre `fingerprints`. As
   **heurísticas semânticas (camada 3)** só reportam ocorrências; qualquer
   achado delas é informativo/híbrido, escrito à mão, e não bloqueia.
   Nenhum comando de validação escreve `.md` ou índices. CI passa;
   regressões bloqueadas. Estado inicial: 112 regras importadas, todas
   ativas por default. A **primeira ação de auditoria concreta** é escrever
   os 7 achados `P2_IGUALDADE_MATERIAL_ATIVA` de E2 (17 registros
   envolvidos) para investigação — inativações, se houver, só depois da
   conclusão de cada investigação, registrada com justificativa.
2. **Fase 1**: P7 (máquina mínima) + P11 — adiciona `status_auditoria`
   a todas as regras (`importada`), implementa a tabela estado→predicados
   no validador e define o fluxo dos PRs de auditoria. Em paralelo,
   **P13.1** (spec semântica `docs/spec/regra.md`) começa com a estrutura
   e a fronteira automático/manual/desconhecido declarada, e evolui à
   medida que as questões Q1–Q12 forem respondidas pela investigação.
3. **Fase 2**: P3 + P4 — bundle `okf/dispositivos/` começando pelas normas
   mais citadas (CF/88 art. 40, ECE 146/2021, LCE 1.100/2021, LCE
   432/2008); regras ganham `dispositivos:` conforme são revisadas.
4. **Fase 3**: P6 (análise de cobertura, só regras ativas) — **depende de
   P13** (classificação predicado × resultado, Q3) e de massa crítica de
   regras revisadas.
5. **Auditoria de mérito**: ciclos 1º → 4º — **depende da spec P13.1**
   (o revisor precisa saber o que é automático, o que é manual e o que é
   desconhecido), com critérios objetivos e checks automáticos por trás.

## Questões resolvidas

1. ~~P2: fundir registros iguais alteraria `row_count` do bundle vs.
   importação~~ — **resolvida (2026-07-17)**: os grupos de igualdade
   material são **investigados**; nada é fundido nem excluído. A inativação
   documentada (P2.1) é um mecanismo disponível **apenas se** a auditoria
   concluir que determinado registro não representa uma regra autônoma.
   Em qualquer desfecho, `row_count` e a sequência `1..N` permanecem
   intactos; nenhum check de CI existente precisa mudar de forma.
2. ~~CSV derivado carrega os campos administrativos novos?~~ — **resolvida
   (2026-07-17)**: sim, colunas originais + campos novos (P12).
3. ~~P3: granularidade dos dispositivos~~ — **resolvida (2026-07-17)**:
   menor unidade efetivamente citada pelas regras, decomposição sob
   demanda, sem fragmentar preventivamente a norma inteira.
4. ~~P5: migrar sentinelas quebra o round-trip?~~ — **resolvida
   (2026-07-17)**: sentinelas mantidas (round-trip preservado),
   documentadas no Dataset e **preservadas/excluídas das análises
   semânticas** — não interpretadas nem como data real nem como limite
   aberto antes da P13; eventual migração fica para RFC/PR próprio.
5. ~~P7: nomes dos estados~~ — **resolvida quanto à estrutura
   (2026-07-17)**: máquina mínima `importada → revisada → validada`;
   estados de processo e `inconsistente` eliminados (problemas são
   `achados`; rebaixamento é derivável dos invariantes contínuos); estados
   futuros só via regra de desenho + template (P7). **O fluxo institucional
   de `validada` (fonte do documento, se um ou dois atos, quais
   autoridades) NÃO está fechado** — é proposta sujeita à confirmação
   (`atos_validacao` provisório; SEI não fixado) e integra a Q12, não é
   inferido dos 112× `FALSE/FALSE`.
6. ~~P2.1: permanência do invariante "`regra_canonica` aponta para regra
   ativa"~~ — **dissolvida (2026-07-17)**: o campo `regra_canonica` foi
   removido. Os grupos de igualdade material são derivados mecanicamente
   do CSV congelado e, **se** a auditoria concluir por inativações num
   grupo, o membro que permanece ativo é inferido — condição derivada, não
   ponteiro armazenado; não havendo ponteiro, a pergunta sobre sua
   permanência deixa de existir. Junto, ficou consolidado que encerramento
   temporal (janela de aplicação vencida) **não** é inativação: a regra
   continua `ativa` porque rege fatos pretéritos; `inativa` significa
   descarte de identidade autônoma pela auditoria (`duplicata`,
   `erro_de_importacao`).

## Questões em aberto

As **doze questões semânticas Q1–Q12** (ver P13) estão abertas **por
desenho**: dizem respeito a como o Sisprev realmente funciona (semântica
de datas, seleção de candidatas, campos externos ao CSV, definição
operacional de cálculo/integralidade/paridade, semântica de vazios,
campos de DTC/interface, e a fronteira entre correspondência automática,
verificação manual do caso e validação jurídica da regra). Elas **não**
serão respondidas neste RFC — são respondidas pela investigação junto ao
Sisprev, à documentação e à análise jurídica, e cada resposta alimenta a
spec P13.1 e o mapa P13.2.

Nenhuma questão estrutural do próprio RFC permanece aberta — todas foram
resolvidas ou dissolvidas (ver acima).
