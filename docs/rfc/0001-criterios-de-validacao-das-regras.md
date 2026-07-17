# RFC 0001 — Critérios de validação e processo de auditoria das regras

- **Status**: Proposta (em discussão)
- **Criada em**: 2026-07-17
- **Depende de**: PR #1 (bundle OKF inicial, CSV original congelado, CSV derivado)

## Contexto

O repositório contém o catálogo de regras de aposentadoria e pensão do
Sisprev como um bundle OKF (`okf/regras-sisprev/`), com o objetivo de
auditar e validar cada regra até que possa ser aplicada no sistema com
segurança jurídica (ver `README.md`). Este RFC propõe **o que** significa
uma regra ser válida — os critérios objetivos que o conjunto de regras deve
satisfazer — e **como** o processo de auditoria deve registrar isso.

A análise da importação original (112 linhas) já revela por que critérios
formais são necessários **antes** de começar a auditoria jurídica de mérito.
Evidências encontradas na própria planilha:

| # | Evidência | Quantidade |
|---|---|---|
| E1 | Nomes duplicados (`NOME` repetido em mais de uma linha) | 41 nomes, cobrindo 94 das 112 linhas |
| E2 | Linhas **100% idênticas** em todas as 27 colunas (redundância pura) | 13 linhas em 5 grupos — ex.: a regra "Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021" aparece 4× byte-a-byte igual |
| E3 | `TIPO_CALCULO = "Não identificado"` (pendência assumida) | 13 regras |
| E4 | `SEXO` e `INTEGRAL` vazios (as mesmas 13 regras de E3, todas de ciclos antigos) | 13 regras |
| E5 | `INTEGRAL = N` (proventos proporcionais) mas `FUNDAMENTACAO_PROPORCIONAL` vazia | 17 regras |
| E6 | Citação inconsistente da mesma norma ("LC 1100/21", "LC 1.100/2021", "Lc nº 1100/21") | recorrente |
| E7 | Contradição interna: regra com `SEXO = MASCULINO` cuja fundamentação cita o dispositivo da **mulher** ("artigo 1º, inciso II, alínea 'b', da LC 51/1985 ... regra transitória - idade + tempo de contribuição + mulher") | ao menos 1 (linha 80 do CSV) |
| E8 | Par de regras irmãs com datas suspeitas de digitação (`DATA_ADM_ATE = 14/06/2021` vs `14/09/2021` na regra gêmea — a EC 146 é de 14/09/2021) | linhas 51–52 |

O corpus normativo citado é pequeno e fechado: CF/88 (art. 40 em múltiplas
redações), ECs 20/1998, 41/2003, 47/2005, 70/2012, 88/2015, 103/2019, ECE
146/2021, LCs 51/1985, 144/2014, 152/2015, LCEs 432/2008, 949/2017,
1.100/2021, Lei 10.887/2004 e IN nº 5/2020 — cerca de 16 normas. Isso torna
viável a proposta P3 (bundle de dispositivos) sem explosão de escopo.

---

## Propostas

Cada proposta tem um identificador (P1, P2, ...) para referência em
discussões e PRs. As marcadas **[bloqueante]** viram checks automáticos
(teste + CI) quando aceitas; as demais são processo/convenção.

### P1 — Nome único por regra [bloqueante]

Toda regra deve ter `nome` único no bundle. Nome é identidade: se duas
linhas têm o mesmo nome, ou são a mesma regra (e devem ser fundidas — ver
P2), ou são regras diferentes que o nome não distingue (e o nome deve ser
qualificado com o que as distingue: sexo, período de admissão, magistério,
proporcional/integral etc.).

Hoje 94 das 112 linhas violam isso (E1). A maioria dos pares duplicados
difere apenas em `SEXO` (MASCULINO/FEMININO) ou em `TIPO_CALCULO` — a
qualificação natural é sufixar o nome: p.ex. "… — Feminino",
"… — Proporcional".

Check proposto: unicidade de `nome` (case- e acento-insensível, espaços
normalizados) sobre todos os `regra-*.md`.

### P2 — Nenhuma regra pode ser materialmente idêntica a outra [bloqueante]

Duas regras não podem ter exatamente as mesmas propriedades (todas as 27
colunas). Regra duplicada não acrescenta capacidade decisória ao sistema e
multiplica o custo de auditoria — cada correção teria que ser repetida N
vezes, e uma cópia esquecida vira regra divergente silenciosa.

Hoje 13 linhas violam isso (E2). A resolução é **fundir** cada grupo em uma
única regra (mantendo o menor `row_index` como referência histórica da
origem) — nunca apagar sem registrar no corpo da regra sobrevivente quais
linhas da importação original ela consolida.

Check proposto: nenhuma dupla de `regra-*.md` com frontmatter + corpo
materialmente iguais (ignorando `id`/`row_index`).

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

- **Um dispositivo por arquivo**, granularidade mínima citável (inciso ou
  alínea quando a regra cita nesse nível). Frontmatter: `type: Dispositivo`,
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
arquivo existente; toda regra auditada (P7 ≥ revisão técnica) tem
`dispositivos:` não vazio.

### P4 — Formato canônico de citação [bloqueante após P3]

Definir uma forma canônica de citar cada norma (ex.: sempre
"LCE nº 1.100/2021", nunca "Lc 1100/21") e um vocabulário fechado de
normas citáveis (o corpus de ~16 normas acima; adições passam por PR no
`okf/dispositivos/`). E6 mostra que hoje a mesma norma aparece com pelo
menos 3 grafias — impossível de verificar mecanicamente.

A fundamentação em prosa continua livre; o que é canônico é o frontmatter
`dispositivos:` (P3). A prosa é para humanos; o frontmatter é para checks.

### P5 — Coerência de janelas temporais [bloqueante]

Para toda regra: `DATA_ADM_APOS ≤ DATA_ADM_ATE` e
`DATA_DIREITO_APOS ≤ DATA_DIREITO_ATE`, com datas parseáveis. (Hoje as 112
passam — o check existe para continuar passando.)

Adicionalmente, documentar as **datas-sentinela** (`01/01/1910`,
`01/01/1950`, `31/12/2099` = "sem limite") como convenção explícita no doc
Dataset, e propor a médio prazo substituí-las por campos vazios com
semântica "aberto" — data mágica parece dado real e engana análises (o
check de E8 só é possível porque 14/09/2021 é a data da ECE 146; sentinela
não carrega essa informação).

Check adicional proposto: datas de marcos legais citadas nas janelas devem
pertencer ao conjunto de datas de vigência das normas do bundle de
dispositivos (16/12/1998 = EC 20, 31/12/2003 = EC 41, 14/09/2021 = ECE 146,
etc.) ou ser sentinela — qualquer outra data exige justificativa no corpo
da regra. Isso teria flagrado E8 automaticamente.

### P6 — Cobertura e não-ambiguidade do espaço de decisão

O conjunto de regras funciona como uma função: dado um perfil de servidor
(sexo, data de admissão, data de aquisição do direito, tipo de benefício,
condição especial), quais regras se aplicam? Dois problemas simétricos:

- **Lacuna**: perfil plausível para o qual nenhuma regra se aplica.
- **Ambiguidade**: duas regras do mesmo `TIPO DE BENEFICIO` cobrindo o
  mesmo perfil com **fundamentação ou cálculo diferentes** sem que haja um
  critério de desempate documentado (concurso de regras é legítimo — o
  servidor pode ter direito à regra mais vantajosa — mas o desempate deve
  ser explícito, não acidente).

Proposta: um script de análise (`scripts/analisar_cobertura.py`) que
particiona o espaço (sexo × janela de admissão × janela de direito × tipo)
e reporta lacunas e sobreposições. Não-bloqueante no início — o resultado é
insumo de auditoria, não critério pass/fail — até calibrarmos o que é
sobreposição legítima.

### P7 — Máquina de estados de validação [bloqueante]

Substituir os booleanos soltos por um fluxo explícito. Estados propostos,
por regra (campo novo `status_auditoria` no frontmatter):

```
importada → em_revisao → revisada → validada_pge → validada_presidencia
                │            │
                └── inconsistente (achado registrado, aguardando correção)
```

Invariantes [bloqueantes]:

- `validado_pge: 'TRUE'` exige `status_auditoria` ≥ `validada_pge`, e
  vice-versa (os campos legados viram derivados do estado).
- Transição para `validada_pge`/`validada_presidencia` **exige referência
  ao ato aprovador** (campo `aprovacao:` com documento/processo SEI/data) —
  ninguém marca TRUE sem apontar o ato que o sustenta.
- Mudança de `status_auditoria` deve ser commit próprio (não misturada com
  correção de conteúdo), com a justificativa na mensagem — o histórico git
  é a trilha de auditoria (quem, quando, por quê).
- Regra em `inconsistente` lista os achados abertos em uma seção
  `# Achados` no corpo do `.md`.

### P8 — Vocabulários fechados (enums) [bloqueante]

`TIPO DE BENEFICIO`, `TIPO_CALCULO`, `SEXO`, `TIPO`, e os campos S/N e
TRUE/FALSE passam a ter vocabulário fechado, declarado no doc Dataset
(`regras-sisprev.md`), e verificado por teste. `"Não identificado"` em
`TIPO_CALCULO` (13 regras — E3) permanece **permitido, porém marcado**: é
uma pendência explícita que impede a regra de avançar além de `em_revisao`
na máquina de estados (P7).

### P9 — Coerência interna dos campos [bloqueante]

Regras de consistência entre colunas da própria regra:

- `INTEGRAL = S` ⟹ `FUNDAMENTACAO_INTEGRAL` não vazia (hoje: 0 violações);
- `INTEGRAL = N` ⟹ `FUNDAMENTACAO_PROPORCIONAL` não vazia (hoje: **17
  violações** — E5; cada uma vira achado de auditoria);
- `SEXO` vazio só é admissível junto com `TIPO_CALCULO = "Não identificado"`
  (as 13 pendências de E3/E4 — regra nova não pode nascer sem sexo);
- Fundamentação que menciona sexo específico ("mulher", "alínea b") deve
  ser compatível com o campo `SEXO` (teria flagrado E7). Este último começa
  como heurística de alerta, não bloqueio.

### P10 — Validação executável (`scripts/validar_regras.py`) [bloqueante]

Todo critério bloqueante deste RFC vira código: um script que lê o bundle e
reporta violações por proposta (P1, P2, P5, P7, P8, P9 — P3/P4 quando o
bundle de dispositivos existir), com saída legível e exit code ≠ 0 em
violação. Roda no `pytest` (um teste por proposta) e no CI como job
`validar-regras`.

Importante: as violações **pré-existentes** da importação (E1–E5) entram
numa *baseline* explícita (arquivo `data/baseline-violacoes.json` ou
marcador por regra) — o CI bloqueia **regressões** (violação nova) desde o
dia 1, e a baseline vai encolhendo conforme a auditoria corrige o legado.
Sem isso, o CI nasceria vermelho e seria ignorado.

### P11 — Trilha de auditoria por regra

Convenções de registro (complementa P7):

- `log.md` no diretório `regras/` (formato OKF SPEC.md §7) com o histórico
  agregado de mudanças por data;
- No frontmatter de cada regra: `auditado_por` e `auditado_em` (preenchidos
  na transição para `revisada`);
- Achados que não são da regra em si (ex.: inconsistência entre duas
  regras) viram issues no GitHub, referenciadas na seção `# Achados` das
  regras envolvidas.

---

## O que este RFC não propõe

- **Não** propõe corrigir o mérito jurídico de nenhuma regra — isso é o
  trabalho de auditoria que estes critérios estruturam.
- **Não** propõe alterar `data/raw/regras-sisprev.csv` (congelado, sempre).
- **Não** propõe motor de decisão/simulador — P6 analisa cobertura, não
  executa regras.

## Sequenciamento sugerido

1. **Fase 0** (este RFC aceito): P10 com P1, P2, P5, P8, P9 + baseline das
   violações legadas. CI passa; regressões bloqueadas.
2. **Fase 1**: P7 (máquina de estados) + P11 — adiciona `status_auditoria`
   a todas as regras (`importada`), define o fluxo dos PRs de auditoria.
3. **Fase 2**: P3 + P4 — bundle `okf/dispositivos/` começando pelas normas
   mais citadas (CF/88 art. 40, ECE 146/2021, LCE 1.100/2021, LCE
   432/2008); regras ganham `dispositivos:` conforme são revisadas.
4. **Fase 3**: P6 (análise de cobertura) quando houver massa crítica de
   regras revisadas.
5. **Auditoria de mérito**: ciclos 1º → 4º, agora com critérios objetivos e
   checks automáticos por trás.

## Questões em aberto

1. P2: fundir duplicatas altera `row_count` do bundle vs. importação — o
   check de CI `bundle-imports-original` (que exige cobertura de todas as
   linhas originais) precisa aprender que uma regra pode consolidar
   múltiplas linhas (`consolida_linhas: [76, 77, 78, 79]` no frontmatter?).
2. P3: granularidade — um arquivo por alínea pode gerar centenas de
   arquivos para a LCE 1.100/2021; começar por artigo e subdividir só onde
   as regras citam mais fino?
3. P5: migrar sentinelas para campos vazios quebra o round-trip com o
   formato da planilha original — vale o custo, ou documentar e conviver?
4. P7: os nomes dos estados e a exigência de ato aprovador com número de
   processo — validar com quem opera o fluxo PGE/Presidência na prática.
