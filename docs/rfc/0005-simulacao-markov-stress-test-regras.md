# RFC 0005 — Stress test transversal de requerimentos sintéticos para o catálogo de regras (piloto invalidez/incapacidade)

- **Status**: proposta (2026-07-23). **Especificação revisável, sem
  implementação.** Não cria diretório, schema, kernel, gerador, avaliador,
  coletor de métricas, runner, registry de benchmarks ou publicação no site.
  Não edita nenhum `regra-*.md`, achado, dispositivo, detector, o simulador
  existente (`site/src/lib/simulador.ts`, RFC 0002) ou qualquer workflow.
  Entrega apenas o desenho. Revisão 2026-07-23 (round 2, consolidação de
  decisões de produto): reposiciona o MVP como **stress test transversal**
  de muitos requerimentos sintéticos **independentes** (cada um um
  *snapshot*, não uma trajetória) — a simulação longitudinal em cadeia de
  Markov, que era o motor principal na primeira versão desta RFC, passa a
  ser uma **extensão futura** (§12), com todo o desenho já feito preservado
  ali. Formaliza geração híbrida (sistemática + dois kernels aleatórios),
  suítes coerente/adversarial separadas, a distinção entre resultado
  estrutural e ranking experimental, critérios de aceitação verificáveis
  por tipo de caso, execução em camadas (PR/main/benchmark), promoção
  automática por gates fortes, identidade imutável de benchmark, seeds
  reproduzíveis, versionamento de protocolo, revogação por sucessor (nunca
  reescrita), e o escopo exato de publicação no site.
- **Parte de / depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) (semântica adiada,
  autoria humana, P2/P13, Q1–Q12),
  [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (avaliação trivalente,
  papel do `nome`, o piloto executado à mão),
  [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) (schema
  enriquecido `auditoria:`, os três universos do simulador exploratório —
  §12.2 —, o modelo de cinco partes do requisito de verificação humana —
  §7 —, e `base_avaliacao`), a spec [`docs/spec/regra.md`](../spec/regra.md)
  (P13.1), o piloto executado
  [`docs/analysis/piloto-selecao-invalidez-incapacidade.md`](../analysis/piloto-selecao-invalidez-incapacidade.md),
  a reconciliação
  [`docs/analysis/reconciliacao-invalidez-incapacidade.md`](../analysis/reconciliacao-invalidez-incapacidade.md)
  e a base normativa
  [`docs/analysis/base-normativa-invalidez-incapacidade.md`](../analysis/base-normativa-invalidez-incapacidade.md).
- **Não-objetivo**: implementar qualquer parte do motor de geração,
  avaliação, gates, registry de benchmarks ou publicação; responder Q1–Q12
  ou Q6-S; fixar probabilidades reais de incidência; estimar a população do
  IPERON; decidir mérito jurídico de qualquer regra; alterar o simulador
  exploratório existente (`/simulador/`, RFC 0002/0004 §12.2) ou seu
  pipeline; criar campo novo em `okf/regras-sisprev/`, `okf/dispositivos/`
  ou no schema enriquecido de RFC 0004; produzir qualquer resultado
  numérico como se fosse execução real; publicar qualquer dado de
  solicitação real.

## 0. Escopo desta frente e terminologia

Esta RFC é **exclusivamente arquitetural e documental**. Ela propõe um
**harness de stress test** que gera muitos **requerimentos sintéticos
independentes** — distinto do **simulador exploratório** já existente
(`/simulador/`, RFC 0002, implementado no PR #28; pipeline de três
universos especificado em RFC 0004 §12.2). Os nomes não devem ser
confundidos:

| Termo                                              | O que é                                                                                                                          | Estado                                                                                                   | Público                                                                  |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **simulador exploratório** (RFC 0002/0004 §12.2)   | filtro/avaliador **interativo**, um requerimento por vez, digitado por um humano no site                                         | parcialmente implementado (filtro de RFC 0002 §7 no site; pipeline completo de RFC 0004 §12.2 ainda não) | usuário do site pessoal                                                  |
| **harness de stress test** (esta RFC, MVP)         | gerador **automatizado** de muitos requerimentos sintéticos **independentes** ("transversal" — sem evolução temporal entre eles) | não implementado — só a spec desta RFC (§1–§11)                                                          | auditor/desenvolvedor (ferramenta de auditoria, não user-facing até §10) |
| **extensão longitudinal (Markov)** (esta RFC, §12) | cadeia de Markov em tempo discreto que evolui **trajetórias** de um mesmo requerente sintético — já especificada, mas **futura** | não implementada — spec completa preservada em §12, não é o MVP                                          | auditor/desenvolvedor, fase posterior                                    |

Os três podem, no futuro, compartilhar o **avaliador** — a lógica que
confronta um requerimento sintético com um catálogo e produz
candidatas/exclusões/indeterminações. Essa reutilização é uma decisão de
implementação revisável, não algo que esta RFC decide ou assume.

## 1. Tese central: o requerimento sintético não pode ser derivado de "regra atualmente aplicável"

> O gerador produz muitos **requerimentos sintéticos independentes** — cada
> um um *snapshot* de fatos de um requerente hipotético, numa única data de
> referência, sem relação temporal com os demais. O avaliador de regras
> **observa** cada requerimento e produz candidatas, exclusões,
> indeterminações e explicações, separadamente em cada um dos três
> universos (§5). A sequência é:
>
> ```text
> gerador (sistemático + dois kernels aleatórios, §2) → requerimento sintético (§4)
>                                                       → avaliação independente nos catálogos (§5)
>                                                       → resultado estrutural: candidatas/exclusões/indeterminações + rastro (§5.3, §11)
>                                                       → métricas e gates (§6, §8)
>                                                       → (separadamente, nunca alterando o resultado estrutural) ranking experimental (§5.3)
> ```

**Por que "regra atualmente aplicável" não pode orientar a geração
(circularidade).** Se o gerador decidisse quais fatos produzir em função de
qual regra deveria "bater", ele estaria descrevendo o próprio objeto que
este stress test pretende auditar — e as regras (o objeto testado)
passariam a determinar a geração dos casos usados para testá-las. Um bug de
cobertura no catálogo (uma lacuna, uma regra nunca alcançável, uma colisão)
nunca apareceria como anomalia, porque o gerador já teria "resolvido" a
seleção antes de o avaliador rodar — o motor testaria a si mesmo, não o
catálogo. Isso repete, num nível diferente, exatamente o erro que a
primeira versão do simulador cometeu ao reivindicar "compatível" sem poder
sustentar essa alegação de completude (RFC 0002 §7) — aqui a versão
estocástica desse mesmo erro seria "o gerador sabe qual regra se aplica",
quando é precisamente **isso** que o avaliador existe para descobrir, e o
próprio catálogo pode não saber (`indeterminado` é o desfecho mais comum
hoje — piloto §3.2). A tese vale **igualmente** para geração transversal
(esta seção) e para a extensão longitudinal (§12) — trocar "trajetória" por
"muitos requerimentos independentes" não muda o argumento, só remove a
dimensão temporal dele.

**A separação exigida**:

- o **gerador** (sistemático ou qualquer um dos dois kernels aleatórios,
  §2) nunca lê `okf/regras-sisprev/`, o catálogo enriquecido de RFC 0004,
  nem qualquer `fundamentacao*`/`nome` — ele produz fatos do mundo (idade,
  tempo de contribuição, ocorrência de incapacidade, ...), nunca "que regra
  bate";
- o **avaliador** lê o requerimento sintético e os catálogos, mas nunca
  escreve de volta no requerimento nem retroalimenta o gerador — a
  avaliação de um caso não pode influenciar a geração de outro (isso
  reintroduziria a circularidade por outra porta);
- o **ranking experimental** (§5.3) é sempre derivado depois, sobre o
  resultado estrutural já fechado — nunca é lido de volta pelo gerador nem
  altera o conjunto de candidatas/exclusões/indeterminações.

## 2. Modelo de geração: stress test transversal (MVP)

### 2.1 Por que transversal, não longitudinal, no MVP

O motor principal desta RFC gera um **grande conjunto de requerimentos
sintéticos independentes** — sem relação de "antes/depois" entre eles.
Comparado a uma cadeia de Markov longitudinal (a primeira versão desta
RFC), a abordagem transversal:

- não exige resolver o contrato de suficiência de acumuladores nem a
  composição de tick (§12.2/§12.5 tratam disso, quando a extensão avançar)
  antes de já poder produzir stress test útil;
- cobre o mesmo objetivo imediato — achar lacunas, ambiguidades, colisões e
  fronteiras defeituosas no catálogo (§ herdado de RFC 0004 §12.2) — sem
  precisar simular a passagem do tempo;
- é **estritamente mais simples de reproduzir e auditar**: um requerimento
  sintético é uma linha, não uma sequência de estados — a superfície de bug
  do motor é menor;
- não impede a extensão longitudinal depois — o schema do requerimento
  sintético (§4) é desenhado para ser o mesmo "estado" que, se e quando a
  Fase de extensão avançar (§12; Fase 6, §15), passa a evoluir via o kernel
  de transição já especificado em §12.

**Nada aqui descarta a extensão longitudinal.** Ela continua especificada
em detalhe (§12) exatamente como na primeira versão desta RFC — só deixou
de ser o motor do MVP.

### 2.2 Geração híbrida: sistemática + aleatória

Nenhuma estratégia de amostragem sozinha é suficiente (mesmo argumento já
levantado pela primeira versão desta RFC): amostragem
puramente aleatória sub-explora fronteiras e casos raros; amostragem
puramente sistemática não descobre o que os autores do desenho não
anteciparam. O MVP combina três fontes, sempre rotuladas na proveniência de
cada caso (`origem_geracao`, §4.1):

1. **casos sistemáticos** — fronteiras de data conhecidas (31/12/2003,
   vigência da EC 146/2021 em 14/09/2021, ...), mutação de um fato por vez
   a partir de um caso-base, e pares/*pairwise* contrafactuais isolando um
   único discriminante jurídico (p.ex. `classe_causa`) — cada um desenhado
   deliberadamente, com uma expectativa de invariante verificável (§6.1),
   nunca uma "resposta certa" jurídica;
2. **kernel de cobertura estrutural** (aleatório, §2.3) — amostra
   deliberadamente para maximizar a cobertura do espaço de estados
   conhecido (todas as combinações de `tipo_de_beneficio` × `classe_causa`
   × janelas de data × presença/ausência de cada fato verificável), sem
   pretender plausibilidade demográfica;
3. **kernel de plausibilidade sintética** (aleatório, §2.3) — amostra numa
   distribuição desenhada para *parecer* com um caso plausível de
   requerente (sem qualquer calibração com dados reais, §9.5), útil para
   detectar comportamento sob uma carga que se assemelha, em forma, a uso
   real.

Nenhuma das três é dispensável: a sistemática garante que os casos mais
importantes (fronteiras, discriminantes conhecidos) são sempre testados
mesmo com pouquíssimas execuções (§7, camada PR); os dois kernels
aleatórios garantem volume e descoberta do que a sistemática não previu.

### 2.3 Dois kernels aleatórios separados

Os dois kernels aleatórios têm **propósitos distintos e configuração
própria versionada**: `versao`, `fonte`, `justificativa` — nunca norma
jurídica, nunca estimativa atuarial (§9.5):

| Kernel                       | Objetivo                                                                                                                                           | Amostra                                                                                                             | Nunca é lido como                                                       |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **cobertura estrutural**     | maximizar a fração do espaço de estados conhecido (combinações de campos do schema, §4.1) efetivamente exercitada                                  | estratificada/quase-sistemática sobre as dimensões conhecidas; deliberadamente **não** ponderada por plausibilidade | "distribuição real de requerentes"                                      |
| **plausibilidade sintética** | exercitar o motor sob uma distribuição que **parece** com um caso plausível, para achar comportamento que só aparece sob combinações "verossímeis" | ponderada por uma distribuição sintética própria (versionada, §9.5), nunca calibrada com dados reais de segurados   | "estimativa de incidência real" ou "distribuição real do IPERON" (§9.5) |

Cada kernel tem sua própria `kernel_version`, e cada execução registra qual
seed derivada (§9.2) foi usada por kernel — os dois nunca compartilham
implicitamente uma fonte de aleatoriedade, para que trocar um não afete a
reprodutibilidade do outro.

### 2.4 Suítes coerente e adversarial — completamente separadas

Todo caso gerado (sistemático ou de qualquer kernel) pertence a exatamente
uma de duas suítes, e as duas **nunca são misturadas** na mesma métrica,
gate ou visualização sem rótulo explícito (gate `P_SIM_SUITE_MISTURADA`,
§14):

- **suíte coerente** — fatos internamente consistentes (nenhuma
  contradição deliberada); usada para exercitar o "caminho normal" do
  avaliador: cobertura, indeterminação por falta de informação, divergência
  entre universos;
- **suíte adversarial** — fatos deliberadamente contraditórios ou
  desenhados para expor acoplamento indevido (p.ex. um fato de
  `fatos_verificacao_humana[]` com `avaliacao: satisfeito` para "nexo com
  acidente em serviço" mas `classe_causa = causa_comum`; um fato irrelevante
  mutado para testar invariância metamórfica; um fato removido para
  verificar degradação para `indeterminado`) — usada para verificar que o
  avaliador **reporta** a contradição em vez de escolher um lado
  silenciosamente.

Misturar as duas suítes numa métrica corromperia o seu significado: uma
"taxa de indeterminação" que inclui casos adversariais desenhados para
produzir indeterminação deixaria de medir o que a suíte coerente mede. Por
isso toda métrica (§6, §8) é sempre reportada **por suíte**, nunca agregada
entre as duas.

## 3. Escopo do piloto: só invalidez/incapacidade permanente

Esta RFC especifica o piloto **exclusivamente** para aposentadoria por
invalidez/incapacidade permanente — as 11 regras as-is (`regra-0001`,
`0002`, `0004`, `0006`–`0009`, `0019`–`0022`), as 8 hipóteses PGE (P1–P7,
P9), e a decomposição por classe de causa já especificada em RFC 0004 §3
(`causa_incapacidade`: `acidente_em_servico`, `molestia_profissional`,
`doenca_catalogada`, `causa_comum`). Esta família já tem:

- reconciliação as-is × PGE (documento irmão, com as classes de tensão
  E1–E8 herdadas de RFC 0001 e os cruzamentos 0022×P6/P7);
- base normativa (dispositivos coletados em `okf/dispositivos/`, pendências
  P-1 a P-6 categorizadas por tipo);
- 11 regras legadas identificadas e um piloto de seleção explicável já
  executado à mão (12 casos sintéticos, RFC 0002);
- o modelo do requisito de verificação humana em cinco partes (RFC 0004
  §7): predicado (Q6-R), fato da solicitação (Q6-S), protocolo de
  verificação (Q6-R), constatação concreta (Q6-S), avaliação;
- o problema Q6-R/Q6-S/Q6-T documentado (predicado × fato × taxonomia
  versionada).

**Fora de escopo desta RFC** (expansão futura possível, Fase 8, §15):
pensão por morte, aposentadoria voluntária, professor, compulsória, PCD. O
schema do requerimento sintético (§4) é desenhado para não impedir essa
expansão, mas nenhuma modalidade além de invalidez/incapacidade é modelada
aqui.

## 4. Schema do requerimento sintético

O requerimento sintético é um **schema próprio**, deliberadamente separado
de três outras representações com papéis distintos:

| Representação                                                | Papel                                                                                         | Onde vive (proposto ou existente)                             |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Schema do requerimento sintético** (este RFC)              | fatos sintéticos de um requerente hipotético, numa única data de referência, para stress test | proposto, não criado — §13                                    |
| **Schema enriquecido da auditoria** (`auditoria:`, RFC 0004) | predicados jurídicos estruturados **da regra**, não do requerente                             | `okf/regras-auditadas/` (proposto em RFC 0004)                |
| **27 colunas do Sisprev** (`regra_schema.py::COLUMNS`)       | formato-alvo legado, também da **regra**, nunca do requerente                                 | `okf/regras-sisprev/`, `data/regras-sisprev.csv`              |
| **Registro institucional real da solicitação**               | o fato e a constatação de um requerimento **real**, no Sisprev de produção                    | fora deste repositório — não modelado nem tocado por esta RFC |

Misturar essas quatro camadas seria o mesmo erro que RFC 0004 §2 já evita
entre semântica operacional e metadado de auditoria — aqui a distinção
adicional é entre **fato do requerente** (o que este RFC modela) e
**predicado da regra** (o que RFC 0004 modela). Um requerimento sintético
nunca edita `auditoria:` nem as 27 colunas, e nunca é confundido com um
requerimento real.

### 4.1 Vetor de fatos mínimo

Cada coordenada abaixo é um **fato do snapshot**, sampleado diretamente
pelo gerador **numa única data de referência** — nenhuma coordenada é
mantida por incremento ao longo do tempo no MVP (isso só existe na extensão
longitudinal, §12, que reaproveita quase todas estas mesmas coordenadas
como *acumuladores* evoluídos por um kernel de transição). A lista é um
**mínimo**, não um teto; a implementação pode adicionar coordenadas
conforme a Fase 2 (§15) revelar necessidade, sempre com a mesma disciplina
de versionamento de kernel/protocolo (§2.3, §9.3).

| Coordenada                           | Papel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Nota                                                                                                                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `data_referencia_caso`               | data única que o snapshot representa (não é um relógio que avança — cada caso tem a sua própria, usada para cobrir janelas de data distintas entre casos, §2.2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | fixa por caso; não avança dentro de um caso — evolução temporal só existe na extensão longitudinal (§12)                                                                                                                 |
| `nascimento`                         | data de nascimento sintética                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | idade é **derivada** de `nascimento` + `data_referencia_caso`, não duplicada como coordenada independente (evita duas fontes divergentes)                                                                                |
| `data_ingresso_servico_publico`      | marco de ingresso no serviço público                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | fato de entrada usado **pelo avaliador** (nunca pelo gerador) para derivar `marco_ingresso`/regime previdenciário aplicável (RFC 0004 §3) — ver nota após a tabela                                                       |
| `data_ingresso_cargo`                | marco de ingresso no cargo específico (pode divergir do ingresso no serviço público em casos de mudança de cargo)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | fato independente                                                                                                                                                                                                        |
| `tempo_contribuicao_acumulado`       | meses de contribuição computados até `data_referencia_caso`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | fato sampleado diretamente, não incrementado por kernel no MVP                                                                                                                                                           |
| `tempo_servico_publico_acumulado`    | meses de serviço público efetivo até `data_referencia_caso`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | fato distinto de `tempo_contribuicao_acumulado` (podem divergir — não presumidos iguais)                                                                                                                                 |
| `tipo_vinculo_funcional`             | natureza **factual** do vínculo funcional em `data_referencia_caso`: estatutário / celetista / comissionado / outro (enum a fechar na implementação)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | um fato administrativo puro — nunca inferido de `nome`/`fundamentacao*` (gate §14); **não** codifica qual regime previdenciário (pré-EC20, EC20, EC41+LCE432, EC103+LC1100, ...) se aplica — ver nota após a tabela      |
| `estado_funcional`                   | ativo / afastado / aposentado / exonerado / outro (enum a fechar na implementação)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | fato em `data_referencia_caso`                                                                                                                                                                                           |
| `incapacidade_ocorreu`               | booleano                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | fato de `data_referencia_caso`                                                                                                                                                                                           |
| `data_ocorrencia_incapacidade`       | data do evento, quando `incapacidade_ocorreu = true`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | nunca posterior a `data_referencia_caso` (invariante, §4.3)                                                                                                                                                              |
| `classe_causa`                       | `acidente_em_servico` \| `molestia_profissional` \| `doenca_catalogada` \| `causa_comum` \| `indeterminada` (mesmo enum de RFC 0004 §3, com o valor adicional `indeterminada` para representar o fato ainda não classificado)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | nunca preenchido antes de `incapacidade_ocorreu = true`                                                                                                                                                                  |
| `duracao_incapacidade_meses`         | fato: meses entre `data_ocorrencia_incapacidade` e `data_referencia_caso`, medindo a persistência do fato médico/funcional em si                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | independente de constatação — a certificação não desfaz o fato de a incapacidade ter ocorrido                                                                                                                            |
| `tempo_aguardando_constatacao_meses` | fato **distinto**: meses entre `data_ocorrencia_incapacidade` e a data da primeira `constatacao_documentada` em `fatos_verificacao_humana[]` (ou até `data_referencia_caso`, se ainda não há nenhuma) — mede o atraso procedimental, não a duração médica                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | pode ser igual a `duracao_incapacidade_meses` (nenhuma constatação ainda) ou menor (já houve constatação antes de `data_referencia_caso`) — nunca maior                                                                  |
| `diagnostico_classificacao`          | classificação médico-jurídica, quando aplicável (referencia a taxonomia versionada — próxima linha)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | opcional; `null` até informado                                                                                                                                                                                           |
| `data_referencia_versao_rol`         | qual data serve de referência para localizar a versão do rol de doenças vigente — deliberadamente **não fixada** por esta RFC (candidatas plausíveis incluem a data da ocorrência da incapacidade, da constatação, ou do requerimento; Q6-T não decide qual é a correta)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | pode ser `pendente` — nesse caso o gerador não escolhe uma data sozinho, é uma coordenada válida que representa a própria abertura de Q6-T                                                                               |
| `versoes_rol_candidatas`             | **conjunto** (nunca um único valor) de versões do rol de doenças compatíveis com o caso — quando `data_referencia_versao_rol` está `pendente` ou o mapeamento data→versão é ele próprio controverso, o conjunto contém todas as versões conhecidas (LCE 432/2008: 14 doenças; LCE 1.100/2021: 16), nunca uma escolhida arbitrariamente                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | o avaliador consome o conjunto inteiro por universo — nunca colapsa para uma versão só fora do que Q6-T já resolveu (RFC 0004 §16.2)                                                                                     |
| `fatos_verificacao_humana`           | lista de `{predicado, base_avaliacao, avaliacao, responsavel?, data?, referencia?}` — espelha as cinco partes de RFC 0004 §7; é aqui, e só aqui, que o requerimento registra o fato de uma solicitação sobre um requisito específico (nexo com acidente, moléstia profissional, enquadramento no rol, ...) — nunca em coordenadas dedicadas por predicado, que colapsariam num único rótulo genérico requisitos cujo protocolo de verificação (RFC 0004 §7, parte 1/3) só existe no catálogo, pode variar por universo, e não é papel do gerador antecipar; a lista pode conter mais de uma entrada para o mesmo predicado (p.ex. uma `hipotese_informada` seguida de uma `constatacao_documentada`), já que um snapshot pode representar um histórico de verificação resumido, mesmo sem o caso ser uma trajetória temporal (§12); **nota**: a base normativa (§3.3.3 do documento irmão) já registra que nenhum dos dois regimes estaduais lidos define "moléstia profissional" (P-6) — a geração pode produzir esse predicado como `indeterminado`/`sem_informacao` estruturalmente, sem que isso implique que a lacuna jurídica foi resolvida | ver §4.2 desta RFC                                                                                                                                                                                                       |
| `contradicoes_e_dados_ausentes`      | lista estruturada de contradições detectadas dentro do próprio requerimento (p.ex. uma entrada de `fatos_verificacao_humana[]` com `predicado: "nexo com acidente em serviço"`, `avaliacao: satisfeito` mas `classe_causa = causa_comum`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | usada pela suíte adversarial (§2.4)                                                                                                                                                                                      |
| `origem_geracao`                     | `{modo: sistematico \| aleatorio_cobertura \| aleatorio_plausibilidade, suite: coerente \| adversarial, kernel_version?, seed_derivada?, motivo_sistematico?}` — proveniência obrigatória de todo caso                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `motivo_sistematico` só existe para `modo: sistematico` (p.ex. "fronteira 31/12/2003", "mutação de `classe_causa` a partir do caso base X"); `kernel_version`/`seed_derivada` só existem para os modos aleatórios (§9.2) |

**Todo requisito verificável por humano é modelável** (princípio herdado de
RFC 0004 §7): o que pode faltar é a **informação** ou a **constatação**
(representadas por `base_avaliacao = sem_informacao`), nunca a
**possibilidade de representação**. Um campo `pendente`/`indeterminado` é
sempre uma coordenada válida — nunca a ausência de uma coordenada.

**Por que nenhum predicado de requisito (nexo de acidente, moléstia
profissional, enquadramento no rol, ...) vira uma coordenada dedicada.** Um
requerimento que já chegasse com um campo `nexo_acidente_servico = satisfeito` estaria pré-computando, fora do avaliador, uma avaliação (item
5 do modelo de cinco partes, §4.2) que RFC 0004 §7 define como **derivada
por regra fixa a partir do predicado lido do catálogo** — portanto uma
saída do avaliador, específica de cada universo e de cada regra que declara
aquele predicado, nunca um fato genérico do requerente. A representação
correta do fato é sempre uma entrada em `fatos_verificacao_humana[]` — o
avaliador, não o gerador, decide o que fazer com ela em cada universo.

**Por que `tipo_vinculo_funcional` é factual e "regime previdenciário
aplicável" não é uma coordenada do schema.** O tipo de vínculo funcional
(estatutário, celetista, comissionado, ...) é um fato administrativo puro,
independente de interpretação jurídica — por isso é coordenada do schema.
Já "qual regime previdenciário está em vigor para este vínculo" (pré-EC20,
EC20, EC41+LCE432, EC103+LC1100, ...) só se resolve cruzando
`data_ingresso_servico_publico`/`data_ingresso_cargo` com as janelas de
vigência documentadas em `okf/dispositivos/` — exatamente o tipo de
classificação derivada e potencialmente controversa (janelas de emenda se
sobrepõem, há regras de transição) que este RFC não pode assumir como fato
bruto sem reintroduzir, num nível diferente, o mesmo erro de pré-computar
uma conclusão jurídica dentro do gerador (§1). O avaliador deriva o regime
aplicável a partir dos fatos de ingresso, por universo, podendo produzir
mais de um regime candidato ou `pendente` — nunca lê um valor único
pré-resolvido do requerimento.

### 4.2 `base_avaliacao` e os cinco componentes do requisito de verificação humana

Reaproveita **integralmente** o modelo de RFC 0004 §7 e §12.2, sem
reabri-lo:

1. **predicado da regra** (Q6-R) — não vive no requerimento sintético; é
   lido do catálogo (`auditoria.requisitos_verificacao_humana[].predicado`)
   pelo avaliador, nunca gerado.
2. **fato da solicitação** (Q6-S) — é o que o gerador produz em
   `fatos_verificacao_humana[]` (§4.1).
3. **protocolo de verificação** (Q6-R) — idem ao item 1, lido do catálogo.
4. **constatação concreta** (Q6-S) — quando o gerador produz uma entrada
   `constatacao_documentada`; carrega `responsavel`, `data`, `referencia`
   sintéticos.
5. **avaliação** — `satisfeito`/`não satisfeito`/`indeterminado`, derivada
   por regra fixa (nunca livre) a partir dos itens 2+3+4, exatamente como
   RFC 0004 §7 define.

`base_avaliacao` tem os três valores já ratificados por RFC 0004 §12.2:

- **`hipotese_informada`** — o "usuário sintético" da simulação preenche uma
  resposta ao protocolo, **sem** constatação real por trás; nunca pode
  aparecer, em nenhum universo, rotulada como constatação do IPERON.
- **`constatacao_documentada`** — um "avaliador sintético" registra
  resultado, responsável, data e referência — a única base que pode ser
  lida como equivalente a uma constatação de fato (ainda que sintética e
  fora do processo real).
- **`sem_informacao`** — nenhuma das duas ocorreu; avaliação
  `indeterminado`, **nunca** "não avaliável".

**Invariante que esta RFC adiciona, específico da geração**: quando um
requerimento sintético contém tanto uma entrada `hipotese_informada` quanto
uma `constatacao_documentada` posterior para o mesmo predicado, a primeira
**nunca é descartada** — a segunda é *acrescentada*, preservando a entrada
anterior intacta no rastro (§11). Perder essa distinção a jusante é o gate
`P_SIM_BASE_AVALIACAO_PERDIDA` (§14).

### 4.3 Invariantes do requerimento sintético [bloqueantes propostos]

Como cada caso é um *snapshot* (§4.1), estes invariantes são mais simples
que os de uma trajetória evoluindo no tempo (que só existem na extensão
longitudinal, §12.5.3) — mas continuam bloqueantes:

- **Ordem temporal interna**: nenhuma data do requerimento
  (`data_ocorrencia_incapacidade`, datas de constatação em
  `fatos_verificacao_humana[]`) pode ser posterior a `data_referencia_caso`.
- **Constatação nunca antes do fato**: toda entrada de
  `base_avaliacao: constatacao_documentada` tem `data ≥ data_ocorrencia_incapacidade` (quando o predicado depende da incapacidade) e
  `data ≤ data_referencia_caso`.
- **Vigência normativa dentro do período**: quando `data_referencia_versao_rol` não é `pendente`, `versoes_rol_candidatas` só pode
  conter versões cuja janela de vigência (as mesmas janelas documentadas em
  `okf/dispositivos/`, base normativa §2) cobre essa data — nunca uma
  versão fora da janela. `tipo_vinculo_funcional` não tem janela de
  vigência própria (é fato administrativo, não classificação normativa); a
  classificação de regime previdenciário aplicável, quando o avaliador a
  deriva de `data_ingresso_servico_publico`/`data_ingresso_cargo`, respeita
  a mesma disciplina de janelas, mas como responsabilidade do avaliador
  (§4.1), fora do que este invariante cobre.
- **Estados mutuamente incompatíveis proibidos**: p.ex.
  `incapacidade_ocorreu = false` com `classe_causa ≠ indeterminada` e vazio;
  `tempo_aguardando_constatacao_meses` maior que `duracao_incapacidade_meses`.
- **Proveniência obrigatória**: nenhum caso é gerado sem `origem_geracao`
  completo (§4.1) — para casos de kernel aleatório, isso inclui
  `kernel_version`/`seed_derivada`; para casos sistemáticos,
  `motivo_sistematico`. Um caso "sem configuração" é erro, nunca default
  silencioso.

## 5. Avaliação nos três universos

### 5.1 Três universos obrigatórios

Cada requerimento sintético é avaliado **separadamente** contra os três
universos já especificados em RFC 0004 §12.2 — esta RFC não redefine os
universos, só formaliza que **todo caso** passa pelos três, e que o
resultado registra qual universo produziu qual candidata:

1. **catálogo legado as-is** — as 112 linhas de `okf/regras-sisprev/`, sem
   enriquecimento; para a família de invalidez, as 11 regras as-is.
2. **catálogo auditado ativo/deployable** — exatamente o que o exportador
   real (RFC 0004 §12.1) também exportaria; hoje, para invalidez, ainda
   **vazio** (nenhum grupo de substituição está `estado_grupo: ativo` — RFC
   0004 §16 mostra os exemplos ainda em `preview`).
3. **catálogo auditado experimental** — inclui unidades em `elaboracao`,
   `preview`, e unidades de grupos `inativo` — a face completa de uma
   decomposição 1:N (p.ex. as duas faces de `regra-0022`, RFC 0004 §16)
   mesmo antes de qualquer grupo ativar.

**Invariante herdado, reafirmado**: a geração/avaliação **nunca** ativa
grupos, altera manifesto, produz export Sisprev, ou transforma unidade
experimental em `deployable`. O avaliador **lê**; nunca escreve nos bundles
(`okf/regras-sisprev/`, `okf/regras-auditadas/` proposto) nem nos artefatos
derivados. Isso vale mesmo quando o universo 2 estiver vazio (como hoje,
para invalidez) — o avaliador registra "universo 2: nenhuma candidata"
honestamente, nunca promove uma candidata do universo 3 para preencher essa
lacuna (gate `P_SIM_UNIVERSO_MISTURADO`, §14).

O resultado de cada avaliação registra **qual universo** produziu cada
candidata/exclusão/indeterminação, permitindo comparação lado a lado — é
esse registro que alimenta a métrica de divergência entre universos (§6) e
o Sankey proposto (§10).

### 5.2 Avaliação dos requisitos humanos

Reafirma, sem alterar, os cinco componentes de RFC 0004 §7 (predicado, fato
da solicitação, protocolo de verificação, constatação concreta, avaliação)
e o vocabulário de `base_avaliacao` (§4.2). Duas regras adicionais
específicas do contexto de geração sintética:

- **Uma hipótese fornecida pelo "usuário sintético" pode ser usada pelo
  avaliador, mas não pode aparecer como constatação do IPERON** em nenhuma
  saída, rastro, métrica ou visualização — toda apresentação de um
  resultado que depende de uma entrada `hipotese_informada` carrega esse
  rótulo explicitamente, na mesma linha do resultado, nunca num rodapé
  genérico.
- **Sem informação → `indeterminado`**, nunca "não avaliável" — o
  protocolo de verificação (parte 3) sempre existe no catálogo para todo
  requisito modelado (RFC 0004 §7), então a avaliação é sempre *possível em
  princípio*; o que falta é o fato, não a capacidade de avaliar.

### 5.3 Resultado primário: conjunto estrutural, nunca ranking

O resultado primário de avaliar um requerimento sintético num universo é um
**conjunto estrutural**: `{candidatas, exclusões, indeterminações}` mais o
rastro (§11) que explica cada elemento. Esse conjunto é o que os gates
(§8), as métricas (§6) e a publicação (§10) tratam como fonte de verdade.

**Ranking é sempre um produto experimental derivado, versionado
separadamente, e nunca altera o conjunto estrutural.** Um ranking (p.ex.
"qual candidata é mais provável dado X") pode ser calculado *depois*, sobre
um conjunto estrutural já fechado — mas:

- não remove nem acrescenta elementos ao conjunto de
  candidatas/exclusões/indeterminações;
- é publicado (quando publicado, §10) num espaço visual **separado**, nunca
  na mesma tabela sem rótulo explícito de "experimental";
- tem sua própria versão (`ranking_version`), independente da
  `benchmark_protocol_version` (§9.3) — mudar o ranking nunca invalida nem
  precisa republicar o resultado estrutural.

Violar essa separação (ranking alterando o conjunto estrutural, ou
aparecendo sem rótulo de experimental) é o gate
`P_SIM_RANKING_CONTAMINOU_RESULTADO` (§14). O mesmo vale, por construção
futura, para a extensão longitudinal (§12) — a matriz "regra anterior →
regra posterior" que ela pode derivar é do mesmo tipo (produto analítico
experimental), nunca gerador nem parte do resultado estrutural.

## 6. Critérios de aceitação verificáveis por tipo de caso

### 6.1 Casos sistemáticos — invariantes de comportamento, nunca "regra correta"

Um caso sistemático (§2.2) sempre carrega uma **expectativa sobre o
comportamento do motor**, nunca uma afirmação de qual regra é
"juridicamente correta" — isso evitaria inventar uma resposta que ainda
depende de decisão jurídica não tomada (Q1–Q12/Q6-S, RFC 0001; P-1 a P-6,
base normativa). Um caso sistemático que carregasse uma expectativa de
"regra correta" para uma questão ainda aberta é o gate `P_SIM_REGRA_INVENTADA` (§14). Exemplos de invariantes aceitáveis (todos
mecanicamente verificáveis, sem depender de mérito jurídico):

| Invariante esperado                                                                                                           | Exemplo de caso sistemático                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| ausência de fato produz pendência/`indeterminado`, nunca exclusão silenciosa                                                  | requerimento sem `diagnostico_classificacao` → face "rol" fica `indeterminado`, nunca `excluída`                    |
| fronteira de data gera pendência explícita, nunca decide para um lado                                                         | `data_referencia_caso` = 31/12/2003 exatamente → resultado marca pendência de janela, não escolhe regime            |
| hipótese informada nunca aparece rotulada como constatação real                                                               | qualquer caso com `base_avaliacao: hipotese_informada` → rótulo sobrevive em toda visualização do caso              |
| universo 2 vazio nunca é preenchido por candidata de outro universo                                                           | qualquer caso, hoje, na família de invalidez (universo 2 vazio) → resultado do universo 2 é sempre `[]`             |
| duas regras indistinguíveis pelos critérios conhecidos geram pendência explícita de indistinguibilidade, não uma só candidata | caso sem `classe_causa` classificada → `0021`/`0022` aparecem juntas com pendência (mesma lógica de `simulador.ts`) |
| contradição deliberada é reportada, nunca escondida atrás de uma escolha silenciosa                                           | caso adversarial com `nexo: satisfeito` + `classe_causa: causa_comum` → `contradicoes_e_dados_ausentes` não vazio   |
| colisão após projeção para as 27 colunas é sempre reportada                                                                   | mesmo critério de RFC 0004 §10/§11 (`P_COMPILA_COLISAO`), aplicado ao resultado de um caso                          |

Cada linha acima é, por desenho, **independente de qual regra "deveria"
ganhar** — testa o motor, não o mérito. Quando um caso sistemático toca uma
questão que **depende** de decisão jurídica ainda aberta (p.ex. se
`0021`/`0022` deveriam ser uma só regra), o critério de aceitação nunca é
"a resposta é X" — é sempre "o motor reporta a situação honestamente"
(pendência, indistinguibilidade, indeterminação), exatamente como a linha
correspondente da tabela acima.

### 6.2 Casos aleatórios — sem rótulo de verdade

Casos dos dois kernels aleatórios (§2.3) **nunca carregam um rótulo de
"resposta certa"** — nem de regra aplicável, nem de resultado esperado.
Um caso aleatório com esse rótulo é o gate
`P_SIM_ROTULO_DE_VERDADE_EM_ALEATORIO` (§14). Em vez disso, servem para:

- **descobrir** ambiguidades, lacunas, colisões e regiões do espaço de
  estados sem cobertura — não para confirmar uma resposta pré-definida;
- alimentar as métricas dependentes do kernel (§6.3): frequência de
  indeterminação, divergência entre universos, cobertura de estados, pares
  indistinguíveis — sempre lidas como comportamento do motor **sob aquela
  configuração sintética**, nunca como taxa real (§9.5);
- disparar revisão humana quando **anômalos** — um caso é anômalo quando
  produz uma violação de invariante estrutural (§6.1 aplica-se igualmente
  aqui, já que invariantes de comportamento do motor valem para qualquer
  kernel válido) ou uma divergência incomum entre universos; casos
  anômalos são os que ficam navegáveis individualmente no site (§10).

Critério de aceitação para o **motor**, não para o caso individual: sobre
qualquer volume de casos aleatórios, zero violações dos invariantes
estruturais de §6.1 (aplicáveis a qualquer caso, sistemático ou aleatório)
é a condição de promoção (§8) — não "os resultados parecem certos".

### 6.3 Métricas de stress test

Divididas entre as que verificam a **corretude estrutural** do motor (devem
valer para **qualquer** kernel válido — uma violação é bug do motor, não
característica do kernel, e é sempre um dos gates de §14) e as que medem o
**comportamento de uma configuração específica** (variam conforme os dois
kernels aleatórios, §2.3, e por isso nunca são lidas como "a taxa real" de
nada, §9.5). Toda métrica abaixo é sempre reportada **por suíte** — coerente
e adversarial nunca agregadas juntas (§2.4):

| Métrica                                                                |                                                       Estrutural (motor)                                                       |                                                              Depende do kernel                                                              |
| ---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: |
| frequência de nenhuma candidata                                        |                                                                                                                                |                                                                      ✓                                                                      |
| frequência de candidatura única                                        |                                                                                                                                |                                                                      ✓                                                                      |
| frequência de múltiplas candidatas                                     |                                                                                                                                |                                                                      ✓                                                                      |
| frequência de indeterminação                                           |                                                                                                                                |                                                                      ✓                                                                      |
| divergência entre os três universos                                    |                                                                                                                                | ✓ (frequência/magnitude); a **existência** de divergência estrutural (p.ex. universo 2 sempre vazio hoje) é fato do catálogo, não do kernel |
| sensibilidade a datas de fronteira                                     |                           ✓ (o comportamento — gerar pendência, nunca decidir — deve ser constante)                            |                                      ✓ (frequência de *atingir* a fronteira, sem amostragem dirigida)                                       |
| sensibilidade a fatos ausentes                                         |                              ✓ (ausência deve sempre virar pendência, nunca exclusão silenciosa)                               |                                                                                                                                             |
| sensibilidade a hipóteses humanas                                      |                                     ✓ (rótulo `hipotese_informada` deve sempre sobreviver)                                     |                                                                                                                                             |
| dependência de requisito sem constatação                               |                             ✓ (deve sempre ficar `indeterminado`, nunca `satisfeito` por omissão)                              |                                                                                                                                             |
| colisão depois da projeção para as 27 colunas                          |                            ✓ (`P_COMPILA_COLISAO`, RFC 0004 §10/§11 — reportar sempre que ocorrer)                             |                                                                                                                                             |
| perda de expressividade A → B                                          |                                                 ✓ (mesma origem — RFC 0004 §5)                                                 |                                                                                                                                             |
| cobertura de estados conhecidos (kernel de cobertura estrutural, §2.3) |                                                                                                                                |                                                                      ✓                                                                      |
| regras nunca alcançadas                                                |                                                                                                                                |                                                                      ✓                                                                      |
| pares de regras frequentemente indistinguíveis                         | ✓ (quais pares são indistinguíveis pelos critérios conhecidos é estrutural — `simulador.ts`'s `assinaturaCriteriosConhecidos`) |                                 ✓ (a frequência de gerar casos nessa região é do kernel de plausibilidade)                                  |
| taxa de casos anômalos (§6.2)                                          |                                                                                                                                |                                                                      ✓                                                                      |
| estabilidade do ranking experimental (§5.3)                            |                                                                                                                                |                                                                      ✓                                                                      |

A distinção importa porque uma métrica "depende do kernel" nunca é lida
como um fato sobre o Sisprev real ou sobre segurados reais (§9.5) — ela mede
o comportamento do motor **sob aquela configuração sintética**, útil para
comparar execuções entre si (só dentro da mesma `benchmark_protocol_version`, §9.3) ou para verificar que uma mudança no catálogo
alterou o comportamento esperado, nunca para estimar frequência real. É
sobre esta tabela que os alertas de "mudança grande de métrica" (§8) e a
visualização de churn/indeterminação (§10) operam. Duas métricas
inerentemente longitudinais (churn do conjunto de candidatas entre `t` e
`t+1`; distribuição do tempo até mudança do resultado) só existem na
extensão futura (§12), já que o MVP transversal não tem uma noção de "antes
e depois" para o mesmo requerente.

## 7. Execução em camadas

Três camadas, com escopo e frequência crescentes — nenhuma delas expõe
publicamente mais do que a anterior (§10 restringe publicação só à camada
benchmark):

| Camada                 | Quando roda                                                  | Escopo (valores ilustrativos, a calibrar na Fase 2, §15 — nunca fixados por esta RFC)                                                           | Propósito                                                                   |
| ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **PR (smoke)**         | toda PR que toca o motor/gerador/avaliador                   | todos os casos sistemáticos da família invalidez + amostra pequena de cada kernel (ex.: ~50–200 casos)                                          | feedback rápido (segundos), nunca é publicado, nunca vira benchmark oficial |
| **main (referência)**  | todo push em `main`                                          | todos os sistemáticos + cobertura completa do kernel de cobertura estrutural + amostra média do kernel de plausibilidade (ex.: alguns milhares) | sinal de CI mais forte que o smoke, ainda interno — nunca publicado (§10)   |
| **benchmark (grande)** | agendado (ex.: semanal) ou sob demanda (`workflow_dispatch`) | volume grande dos dois kernels aleatórios (ex.: dezenas a centenas de milhares)                                                                 | única camada elegível a promoção (§8) e publicação (§10)                    |

Os tamanhos na tabela são **exemplos ilustrativos** para tornar a proposta
concreta — nenhum é um compromisso desta RFC; a calibração real (quanto
tempo cada camada pode gastar, quanto volume é suficiente para as métricas
de §6 serem informativas) é trabalho de implementação e fica registrada
como questão aberta (§16).

## 8. Gates, promoção automática e alertas

**Gates fortes de integridade, validade e reprodutibilidade** — cada
execução da camada benchmark (§7) só é promovida a benchmark oficial se
**todos** passam (zero violações):

- **integridade**: schema válido para 100% dos casos (`P_SIM_SCHEMA_INVALIDO`); rastro completo para 100% dos casos
  (`P_SIM_RASTRO_INCOMPLETO`); nenhuma escrita em `okf/`/`data/`
  (`P_SIM_MUTOU_CATALOGO`); nenhum efeito em manifesto
  (`P_SIM_EFEITO_MANIFESTO`); artefato de lote completo disponível
  (`P_SIM_LOTE_COMPLETO_INDISPONIVEL`, §10);
- **validade**: todo invariante estrutural de §6.1 satisfeito para 100% dos
  casos sistemáticos e adversariais; universo 2 nunca preenchido por outro
  universo (`P_SIM_UNIVERSO_MISTURADO`); `base_avaliacao` nunca perdida
  (`P_SIM_BASE_AVALIACAO_PERDIDA`); suítes nunca misturadas
  (`P_SIM_SUITE_MISTURADA`); nenhum caso aleatório com rótulo de verdade
  (`P_SIM_ROTULO_DE_VERDADE_EM_ALEATORIO`); nenhum caso sistemático com
  regra inventada (`P_SIM_REGRA_INVENTADA`); ranking não contaminou o
  resultado estrutural (`P_SIM_RANKING_CONTAMINOU_RESULTADO`);
- **reprodutibilidade**: replay com a mesma seed mestra produz resultado
  idêntico (`P_SIM_SEED_NAO_REPRODUTIVEL`, §9.2); toda métrica reportada é
  recalculável a partir do rastro serializado
  (`P_SIM_METRICA_NAO_DERIVAVEL`).

**Promoção automática**: se todos os gates acima passam, a execução é
automaticamente marcada `vigente` e fica elegível à publicação (§10) — não
exige aprovação humana adicional, porque os próprios gates já são a
verificação. Se qualquer gate falha, a execução **não** vira benchmark
oficial (gate `P_SIM_PROMOCAO_SEM_GATES` protege contra publicar sem
passar por isso) — permanece só como **artefato técnico** (logs, saída
bruta de CI), nunca navegável no site nem citável como benchmark.

**Alertas, não bloqueios, para mudanças grandes de métrica**: uma métrica
dependente-do-kernel (§6.3) que varia "muito" em
relação ao benchmark `vigente` anterior da **mesma** `benchmark_protocol_version` (§9.3) dispara um **alerta** anexado ao
benchmark — nunca impede a promoção, porque a mudança pode ser legítima
(catálogo mudou, kernel foi deliberadamente ajustado). O limiar exato de
"muito" não é fixado por esta RFC — fica registrado como questão aberta
(§16), a calibrar empiricamente depois dos primeiros benchmarks reais.

## 9. Identidade, versionamento de protocolo e reprodutibilidade

### 9.1 Identificador imutável

Todo benchmark tem um `benchmark_id` **imutável**, construído como:

```text
benchmark_id = "{data_utc}_{sha_main_curto}_{hash_config_curto}"
# exemplo ilustrativo, nunca um resultado real:
# 2026-07-24_92b7a31_9f3a1c2
```

- `data_utc` — data UTC da execução (não a data do commit);
- `sha_main_curto` — SHA (curto) do commit de `main` contra o qual a
  execução rodou;
- `hash_config_curto` — hash (curto) da configuração completa (os dois
  kernels + `benchmark_protocol_version` + seeds mestras, §9.2) — muda
  mesmo sem mudança de código, se algum parâmetro de configuração muda.

Um `benchmark_id` publicado **nunca é reaproveitado** para outro conteúdo
(gate `P_SIM_BENCHMARK_ID_COLIDIU`, §14).

### 9.2 Seeds mestras e derivadas

Toda execução registra uma **seed mestra** (`seed_mestra`) explícita — nunca
uma fonte de entropia implícita do sistema. Seeds por componente (cada
kernel, §2.3; cada suíte, §2.4) são **derivadas deterministicamente** da
seed mestra (p.ex. `hash(seed_mestra, nome_do_componente)`), documentadas
como parte da `configuracao_completa`. Replay exato exige só a seed mestra
mais a configuração completa — nunca depende de estado de RNG implícito
global. **Mesma entrada + mesma seed mestra deve produzir resultado
idêntico** — gate `P_SIM_SEED_NAO_REPRODUTIVEL`.

Cada execução registra, no manifesto (mesma disciplina de proveniência que
RFC 0004 exige do manifesto de substituição — §1.4):

- `benchmark_id`, `seed_mestra`, seeds derivadas por componente;
- `sha_catalogo` por universo (§5.1) — podem divergir se um roda contra
  `HEAD` e outro contra um commit fixado para comparação;
- `benchmark_protocol_version` (§9.3), `kernel_version` por kernel (§2.3);
- `configuracao_completa` — os dois kernels inteiros (todas as
  probabilidades, proveniência, justificativas), não só suas versões;
- `numero_de_casos` por suíte e por origem (`origem_geracao`, §4.1);
- `premissas` — toda suposição assumida para preencher uma lacuna do
  gerador ou do avaliador;
- `data_da_execucao`;
- as **métricas e rastros** produzidos (§6, §11).

### 9.3 `benchmark_protocol_version` e comparações

`benchmark_protocol_version` versiona o **formato** do benchmark — o schema
do requerimento sintético (§4), o formato do rastro (§11), a definição das
métricas (§6) e a estrutura dos gates (§8/§14) — independente do SHA de
código ou da versão de cada kernel (que podem mudar sem mudar o protocolo).

- **Comparação direta (regressão real)** só é válida **dentro da mesma**
  `benchmark_protocol_version` — mesma definição de métrica, mesmo schema.
- **Comparação entre `benchmark_protocol_version` diferentes é permitida**,
  mas sempre **rotulada estrutural** — nunca "regressão" nem "melhora",
  porque a própria definição da métrica pode ter mudado. Uma comparação
  cross-protocolo apresentada como regressão é o gate
  `P_SIM_COMPARACAO_ENTRE_PROTOCOLOS_NAO_ROTULADA` (§14).

### 9.4 Revogação — nunca reescrita

Um benchmark publicado com defeito descoberto depois (ex.: um kernel tinha
um bug de geração, um gate tinha um falso negativo) **nunca é apagado nem
editado**. Recebe um registro de revogação:

```text
{estado: revogado, motivo, data_revogacao, benchmark_sucessor_id}
```

apontando para a execução corrigida que o substitui. Editar ou apagar o
conteúdo de um `benchmark_id` já publicado, em vez de revogar com sucessor,
é o gate `P_SIM_BENCHMARK_REESCRITO` (§14). O explorador do site (§10)
sempre mostra o estado (`vigente`/`revogado`) e, se revogado, o sucessor —
nunca esconde a existência de um benchmark revogado.

### 9.5 Kernels sintéticos não são previsão atuarial

Explícito, sem ambiguidade, para toda saída deste stress test, em qualquer
camada (§7):

- **parâmetros sintéticos não estimam incidência real** — nenhum número dos
  dois kernels (§2.3) representa a probabilidade real de um servidor sofrer
  incapacidade, nem a distribuição real de causas; "plausibilidade
  sintética" (§2.3) nunca é lida como "distribuição real de requerentes" ou
  "estimativa de incidência real";
- **percentuais não representam segurados reais** — nenhuma métrica (§6.3)
  é uma estatística sobre o IPERON ou sobre qualquer população real;
- **o objetivo é encontrar lacunas, ambiguidades, colisões, instabilidade e
  fronteiras defeituosas** no catálogo — não prever concessões nem
  dimensionar reservas;
- **eventual calibração com dados históricos é fase futura, com governança
  própria** (Fase 7, §15) — esta RFC não a autoriza nem a desenha em
  detalhe;
- **o motor continua sendo experimental e hospedado em site pessoal**
  (mesmo rótulo institucional de RFC 0004 §12.2) — nada aqui produz uma
  ferramenta oficial do IPERON.

## 10. Publicação no site

Apenas execuções da camada **benchmark** (§7) que passaram pelos gates de
promoção (§8, estado `vigente`) podem ser publicadas — smoke de PR e
referência de `main` são sinais de CI internos, **nunca** aparecem no site
como benchmark oficial.

O que fica navegável:

- **métricas agregadas** (§6.3) e visualizações derivadas delas (Sankey
  estado→universo→desfecho, heatmap de pares indistinguíveis — estrutura de
  dados a definir na implementação, sem números até haver execução real)
  para **todos os casos sistemáticos** — são poucos e cada um é
  interpretável individualmente;
- para casos aleatórios (§2.3): só os **anômalos/divergentes** (violação de
  invariante estrutural, divergência incomum entre universos, colisão,
  contradição não esperada) ficam navegáveis individualmente no explorador
  — o volume de casos "ordinários" (sem anomalia) é grande demais para
  publicar caso a caso; uma **amostra reprodutível** (seed derivada
  documentada, §9.2, tamanho fixo) fica navegável como representativa dos
  ordinários;
- o **lote completo** — todos os casos, sistemáticos e aleatórios,
  ordinários e anômalos — fica disponível como **artefato compacto para
  download** (formato a definir na implementação); quem quiser auditar o
  benchmark inteiro baixa o artefato em vez de depender do site renderizar
  cada caso; um benchmark publicado sem esse artefato é o gate
  `P_SIM_LOTE_COMPLETO_INDISPONIVEL` (§8, §14).

**Apenas dados inteiramente sintéticos.** Nenhuma solicitação real (nome,
CPF, número de processo, ...) entra no corpus gerado nem no que é
publicado, em nenhuma camada (gate `P_SIM_DADO_REAL_NO_CORPUS`, §14) —
mesma barreira já estabelecida por RFC 0004 §12.2 para o simulador
exploratório.

**Separação visual obrigatória.** O ranking experimental (§5.3), a camada
longitudinal/Markov quando existir (§12) e qualquer hipótese experimental
ficam num espaço visual **distinto** do resultado estrutural
(candidatas/exclusões/indeterminações, §5.3) — nunca misturados na mesma
tabela ou gráfico sem rótulo explícito de "experimental".

## 11. Rastro e serialização

Cada requerimento sintético avaliado produz um **rastro** — o requerimento
completo, a proveniência (`origem_geracao`), a avaliação em cada um dos
três universos, quaisquer contradições detectadas, e as métricas derivadas
daquele caso. O rastro é o que torna um caso **auditável depois**. Um
rastro nunca descarta uma entrada anterior de `base_avaliacao` (§4.2) — a
evolução `sem_informacao → hipotese_informada → constatacao_documentada`,
quando presente no mesmo caso, fica inteiramente visível, nunca só o valor
final.

## 12. Extensão futura: camada longitudinal (Markov)

**Esta seção preserva, sem alterar a substância, o desenho completo da
primeira versão desta RFC** — a cadeia de Markov em tempo discreto que
evolui **trajetórias** de um mesmo requerente sintético ao longo do tempo.
Ela deixou de ser o motor do MVP (§2.1), mas continua especificada em
detalhe para quando a Fase 6 (§15) avançar. Nada aqui é implementado por
esta RFC.

### 12.1 Por que uma trajetória não é o mesmo problema que um snapshot

A extensão longitudinal responde a uma pergunta diferente da do MVP: não
"este requerimento é candidato em qual regra", mas "como o conjunto de
candidatas de um mesmo requerente muda conforme o tempo passa e fatos se
acumulam" — útil para detectar instabilidade de resultado, churn de
candidatas, e sensibilidade a quando exatamente uma constatação chega. O
schema do requerimento sintético (§4) é o mesmo ponto de partida; a
extensão adiciona um **kernel de transição** que o evolve.

### 12.2 Comparação de modelos estocásticos — honestidade matemática

**Não presumimos que uma cadeia de Markov finita simples seja adequada.**
Cinco alternativas foram comparadas para o kernel de transição:

| #   | Modelo                                                                                                                                        | Preserva memória de idade/tempo de contribuição/serviço/duração da incapacidade/vigência normativa?                                                                                                                                                                                                                          | Adequação aqui                                                                                   |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1   | **Monte Carlo independente** (cada instante sorteado do zero)                                                                                 | **Não** — reamostrar idade/tempo acumulado a cada passo produz trajetórias fisicamente impossíveis (idade pode "recuar", tempo de contribuição não é monotônico)                                                                                                                                                             | Rejeitada como gerador principal da trajetória; útil só como bootstrap de estados iniciais (t=0) |
| 2   | **Cadeia de Markov em tempo discreto, estado = "regra atualmente aplicável"**                                                                 | **Não** — viola a tese central (§1): é circular, e mesmo ignorando a circularidade, "regra aplicável" colapsa muitos estados factuais distintos (inclusive `indeterminado`) num único rótulo, perdendo exatamente a informação de que a transição seguinte depende (idade real, causa real)                                  | Rejeitada                                                                                        |
| 3   | **Cadeia de Markov em tempo discreto, estado = fatos correntes sem acumuladores** (p.ex. só idade e causa, sem tempo de contribuição/serviço) | **Parcial** — a idade sozinha não basta: tempo de contribuição pode ter gaps (mudança de vínculo), tempo de serviço público pode divergir de tempo de contribuição, e a duração da incapacidade e o tempo de espera por constatação (dois acumuladores distintos, §12.4) afetam a probabilidade de a próxima perícia ocorrer | Insuficiente sem aumento de estado                                                               |
| 4   | **Semi-Markov** (tempo de permanência num estado, com distribuição própria, influencia a próxima transição)                                   | Sim, por desenho — mas com custo: kernel deixa de ser uma matriz de transição simples; exige distribuições de sojourn time por estado, versionadas e justificadas como qualquer outra probabilidade (§12.6)                                                                                                                  | Não descartado — ver §12.3                                                                       |
| 5   | **Markov com estado aumentado** (acumuladores como coordenadas do próprio estado)                                                             | Sob a **hipótese de suficiência dos acumuladores** — contrato confrontável, não presumido (§12.2.1)                                                                                                                                                                                                                          | **Escolhida como kernel principal desta extensão**                                               |
| 6   | **Geração dirigida a fronteiras/metamorphic testing**                                                                                         | N/A — não é um modelo probabilístico de transição, é uma **estratégia de amostragem** complementar (mutar um fato por vez, concentrar em limites de data, ...) — já adotada no MVP (§2.2), reaproveitada aqui                                                                                                                | **Adotada como complemento obrigatório**, não substituto                                         |

O kernel principal é uma **cadeia de Markov em tempo discreto** cujo
**estado é aumentado** com os acumuladores explicitamente listados no vetor
de estado (§12.4): idade (derivável de nascimento + instante, mas mantida
como coordenada calculável, não redundante), tempo de contribuição
acumulado, tempo de serviço público acumulado, duração desde a ocorrência
da incapacidade e tempo de espera por constatação (dois acumuladores
distintos, não um só), e a referência de vigência da taxonomia de doenças
relevante em cada data — que a geração pode deliberadamente deixar
`pendente`, já que Q6-T não está resolvida. **A granularidade inicial é
mensal** — fina o bastante para capturar mudanças de estado funcional e a
passagem de marcos legais (janelas de data), grossa o bastante para manter
o espaço de estados tratável num piloto.

#### 12.2.1 Suficiência dos acumuladores — contrato confrontável, não prova por definição

Uma cadeia é Markoviana quando `P(estado(t+1) | estado(t), estado(t-1), ...) = P(estado(t+1) | estado(t))` — o futuro depende só do presente, não do
histórico completo. O **contrato formal do kernel** é: `estado(t+1) = kernel(estado(t), rng)` — a função recebe exatamente o estado atual e uma
fonte de aleatoriedade (a seed, §9.2), **nunca** o histórico de estados
anteriores nem qualquer valor fora de `estado(t)`. Esse contrato é
verificável na implementação (a assinatura da função nunca aceita um
histórico) e é o que a propriedade de Markov exige.

O que **não** é verdade por definição é que os acumuladores listados no
vetor de estado (§12.4) — idade, tempo de contribuição, tempo de serviço
público, duração da incapacidade, tempo de espera por constatação,
referência de vigência normativa — sejam de fato estatísticas suficientes
do histórico relevante para toda transição que esta extensão venha a
precisar modelar. Essa é uma **hipótese de design, confrontável por
evidência**, não uma prova matemática: ela afirma que as regras jurídicas
(e portanto os kernels sintéticos que as testam) só precisam da quantidade
acumulada, nunca da trajetória detalhada de como ela foi composta — mas
essa afirmação só se sustenta enquanto nenhuma transição realmente
necessária depender de algo que os acumuladores atuais não capturam.

**O que fazer quando a hipótese falha.** Se um kernel precisar condicionar
uma transição em informação que nenhum acumulador do estado atual expõe
(por exemplo, *quando* dentro do intervalo acumulado um evento ocorreu, não
só *quanto* se acumulou), isso não é um bug a contornar — é o sinal de que
a hipótese de suficiência falhou para aquele caso, e a resposta é uma de
duas, nunca uma leitura de histórico por fora do contrato:

- **aumentar o estado** — adicionar uma nova coordenada que capture
  explicitamente exatamente a dependência descoberta, restaurando a
  suficiência (o preço já reconhecido: espaço de estados maior, mitigado
  pela granularidade mensal e por horizontes temporais limitados — questão
  em aberto, §16); ou
- **migrar para semi-Markov** (§12.3) — quando a dependência não é
  representável como um acumulador discreto (uma distribuição de sojourn
  time contínua, ou uma dependência de renovação que multiplicaria
  acumuladores além do tratável).

Nenhuma outra saída é aceitável: um kernel que lê estado além de
`estado(t)` para decidir `estado(t+1)` viola o contrato desta seção e deixa
de ser, por definição, uma cadeia de Markov.

### 12.3 Quando semi-Markov seria necessário — não descartado, deixado em aberto

A duração da incapacidade e o tempo de espera por constatação **já são
acumuladores distintos do estado aumentado** (§12.4) — logo, uma
probabilidade de transição que dependa de "quantos meses já se passaram
desde a ocorrência da incapacidade" (`duracao_incapacidade_meses`) ou de
"quantos meses sem uma constatação documentada"
(`tempo_aguardando_constatacao_meses`) **continua sendo Markoviana** sobre
o estado aumentado (a dependência é do *valor atual* de cada acumulador,
não do histórico bruto). Isso cobre boa parte do que um leitor apressado
chamaria de "precisa de semi-Markov" — mas não cobre tudo:

- se o kernel precisar de uma **distribuição de sojourn time contínua** (não
  discretizável em buckets mensais sem perda), ou
- se a probabilidade de transição depender de uma renovação (o tempo desde
  a *última* mudança de um sub-estado específico, não desde um evento fixo
  como a ocorrência da incapacidade), de um jeito que exigiria multiplicar
  acumuladores além do que é tratável,

então a formalização correta deixa de ser "Markov aumentado" e passa a ser,
de fato, **semi-Markov**. Esta RFC **não decide essa questão agora** — ela
fica registrada como questão aberta (§16) e como gatilho explícito de
revisão: se a implementação desta extensão revelar que a granularidade
mensal + acumuladores não bastam para representar uma transição relevante à
invalidez/incapacidade, a extensão para semi-Markov é o caminho a avaliar
primeiro, antes de qualquer solução ad hoc.

### 12.4 Vetor de estado aumentado

Reaproveita **integralmente** o vetor de fatos do MVP (§4.1), com duas
diferenças: `data_referencia_caso` volta a ser um relógio que avança
(`instante_simulado`, mensal), e ganha uma coordenada adicional só
significativa numa trajetória:

| Coordenada          | Papel                                                                | Nota                                                                                                                  |
| ------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `instante_simulado` | relógio da cadeia (mês/ano), substitui `data_referencia_caso` do MVP | avança monotonicamente — invariante (§12.5)                                                                           |
| `estado_terminal`   | `null` \| `obito` \| outro estado terminal a fechar na implementação | uma vez preenchido, a trajetória não gera mais transições (§12.5); não existe no MVP, que não tem "fim de trajetória" |

Todas as demais coordenadas de §4.1 (`nascimento`,
`data_ingresso_servico_publico`, `data_ingresso_cargo`,
`tempo_contribuicao_acumulado`, `tempo_servico_publico_acumulado`,
`tipo_vinculo_funcional`, `estado_funcional`, `incapacidade_ocorreu`,
`data_ocorrencia_incapacidade`, `classe_causa`,
`duracao_incapacidade_meses`, `tempo_aguardando_constatacao_meses`,
`diagnostico_classificacao`, `data_referencia_versao_rol`,
`versoes_rol_candidatas`, `fatos_verificacao_humana`,
`contradicoes_e_dados_ausentes`) passam a ser **acumuladores evoluídos pelo
kernel de transição** (§12.5), em vez de fatos sampleados de uma vez — as
mesmas distinções já estabelecidas no MVP (duração da incapacidade
independente de constatação; `tipo_vinculo_funcional` factual separado de
regime derivado; `data_referencia_versao_rol`/`versoes_rol_candidatas`
nunca resolvidos por presunção) continuam valendo, agora como invariantes
de evolução, não só de snapshot.

### 12.5 Kernel de transição

Cada tick mensal (`estado(t) → estado(t+1)`) aplica, **nesta ordem fixa**,
duas camadas distintas — nunca uma mistura implícita das duas, e nunca em
ordem invertida.

#### 12.5.1 Camada 1 — avanço determinístico (sempre aplicado, probabilidade 1)

Aplicada a **todo** tick, para todo estado com `estado_terminal = null`, sem
nenhuma amostragem — é uma função pura de `estado(t)`, não uma linha do
kernel probabilístico, e por isso não participa da soma "probabilidades
válidas" do §12.5.3:

| Coordenada                           | Regra do avanço                                                                                                                                    |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `instante_simulado`                  | `+= 1` (mês)                                                                                                                                       |
| `tempo_contribuicao_acumulado`       | `+= 1` se `tipo_vinculo_funcional`/`estado_funcional` contam como contribuição nesse mês                                                           |
| `tempo_servico_publico_acumulado`    | `+= 1` sob a mesma condição — pode divergir do anterior                                                                                            |
| `duracao_incapacidade_meses`         | `+= 1` se `incapacidade_ocorreu = true`, **independente de constatação**                                                                           |
| `tempo_aguardando_constatacao_meses` | `+= 1` se `incapacidade_ocorreu = true` **e** ainda não há `constatacao_documentada`; congelado (deixa de incrementar) após a primeira constatação |

Nenhum desses incrementos é sorteado. Um kernel que tornasse qualquer um
deles probabilístico estaria violando o próprio contrato de acumulador do
§12.2.1 — o acumulador deixaria de ser função pura do estado anterior.

#### 12.5.2 Camada 2 — evento probabilístico (amostrado uma vez por tick, após a camada 1)

Depois do avanço determinístico, o kernel amostra **no máximo um** evento da
tabela abaixo, condicionado ao estado já avançado pela camada 1 — mais o
candidato implícito **"nenhum evento"** (o tick termina só com o avanço
determinístico, sem nenhum dos eventos abaixo). **É esta distribuição —
todo evento cuja pré-condição o estado pós-avanço satisfaz, mais "nenhum
evento" — que precisa somar exatamente 1** (invariante "probabilidades
válidas", §12.5.3); a camada 1 nunca entra nessa soma, por não ser
amostrada.

| Evento                               | Efeito no estado                                                                                                                                                                                                                                                                                          | Pré-condição                                                                                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| acumulação de contribuição/serviço   | incremento adicional (p.ex. averbação de tempo)                                                                                                                                                                                                                                                           | `estado_funcional = ativo`                                                                                                                          |
| mudança de tipo de vínculo funcional | `tipo_vinculo_funcional` transita para outro valor do enum fechado (estatutário/celetista/comissionado/outro) — não implica, por si, nenhuma reclassificação de regime previdenciário aplicável (derivação do avaliador, §4.1)                                                                            | transições restritas ao enum fechado                                                                                                                |
| ocorrência de incapacidade           | `incapacidade_ocorreu: false → true`; fixa `data_ocorrencia_incapacidade = instante_simulado`; `classe_causa = indeterminada`                                                                                                                                                                             | `incapacidade_ocorreu = false`, `estado_funcional = ativo`                                                                                          |
| classificação inicial da causa       | `classe_causa: indeterminada → {acidente_em_servico, molestia_profissional, doenca_catalogada, causa_comum}`                                                                                                                                                                                              | `incapacidade_ocorreu = true`                                                                                                                       |
| realização de perícia                | produz uma entrada de constatação candidata (ainda não necessariamente favorável)                                                                                                                                                                                                                         | `incapacidade_ocorreu = true`                                                                                                                       |
| informação de hipótese pelo usuário  | adiciona entrada a `fatos_verificacao_humana[]` com `base_avaliacao: hipotese_informada`                                                                                                                                                                                                                  | requisito correspondente ainda `sem_informacao` ou já `hipotese_informada` (pode ser substituída por nova hipótese, nunca vira constatação sozinha) |
| constatação documentada              | adiciona entrada com `base_avaliacao: constatacao_documentada`, `responsavel`/`data`/`referencia` preenchidos; **congela** `tempo_aguardando_constatacao_meses` no valor atingido (nunca decrementa — permanece no rastro, §11); `duracao_incapacidade_meses` segue incrementando normalmente na camada 1 | `incapacidade_ocorreu = true`                                                                                                                       |
| revisão/correção de dado             | corrige um valor já registrado (p.ex. `classe_causa` reclassificada), sempre deixando o valor anterior no rastro                                                                                                                                                                                          | qualquer coordenada com valor anterior                                                                                                              |
| alteração de estado funcional        | `estado_funcional` transita conforme uma máquina de estados própria (a definir na implementação, análoga em rigor à P7 de RFC 0001)                                                                                                                                                                       | transições restritas ao enum fechado                                                                                                                |
| óbito ou outro estado terminal       | `estado_terminal` preenchido; nenhuma transição futura gerada                                                                                                                                                                                                                                             | sempre disponível (evento terminal pode ocorrer a qualquer momento)                                                                                 |

#### 12.5.3 Invariantes [bloqueantes propostos]

- **Ordem temporal**: `instante_simulado` é estritamente não-decrescente;
  nenhuma data derivada (`data_ocorrencia_incapacidade`, datas de
  constatação) pode ser posterior a `instante_simulado`.
- **Sem redução espontânea**: `tempo_contribuicao_acumulado`,
  `tempo_servico_publico_acumulado` e idade (derivada) nunca decrescem
  entre `t` e `t+1`.
- **Constatação nunca antes do fato**: toda entrada de
  `base_avaliacao: constatacao_documentada` tem `data ≥ data_ocorrencia_incapacidade` (quando o predicado depende da
  incapacidade) e `data ≤ instante_simulado` da transição que a produziu.
- **Vigência normativa dentro do período**: quando `data_referencia_versao_rol`
  não é `pendente`, `versoes_rol_candidatas` só pode conter versões cuja
  janela de vigência (as mesmas janelas documentadas em `okf/dispositivos/`,
  base normativa §2) cobre essa data — nunca uma versão fora da janela.
  `tipo_vinculo_funcional` não tem janela de vigência própria (é fato
  administrativo, não classificação normativa); a classificação de regime
  previdenciário aplicável, quando o avaliador a deriva de
  `data_ingresso_servico_publico`/`data_ingresso_cargo`, respeita a mesma
  disciplina de janelas, mas como responsabilidade do avaliador.
- **Estados mutuamente incompatíveis proibidos**: p.ex.
  `incapacidade_ocorreu = false` com `classe_causa ≠ indeterminada` e vazio,
  ou `estado_terminal ≠ null` com qualquer transição subsequente.
- **Probabilidades válidas**: a distribuição da camada de eventos
  probabilísticos (§12.5.2) — cada evento cuja pré-condição o estado
  pós-avanço determinístico satisfaz, mais o candidato implícito "nenhum
  evento" — soma exatamente 1 (tolerância de ponto flutuante a definir na
  implementação); nenhuma probabilidade negativa. O avanço determinístico
  da camada 1 (§12.5.1) nunca é amostrado — é aplicado com probabilidade 1,
  fora desta soma.
- **Proveniência obrigatória**: nenhuma transição é gerada sem que o kernel
  que a produziu tenha `versao`, `fonte` e `justificativa` registradas
  (§12.6) — uma transição "sem configuração" é erro, nunca default
  silencioso.

### 12.6 Onde vivem as probabilidades — nunca normas jurídicas

**As probabilidades não são normas jurídicas.** Elas vivem em
**configuração própria, versionada**, separada do vetor de estado — mesma
disciplina já estabelecida para os dois kernels do MVP (§2.3): versão
(`kernel_version`), fonte (sempre sintética, nunca dado real de segurados,
§9.5), justificativa (stress, nunca realismo demográfico), e possibilidade de
substituição (artefato de configuração, não código).

### 12.7 A matriz de transição entre regras é resultado analítico, nunca gerador

Reforça a tese central (§1) e a regra já estabelecida para o ranking do MVP
(§5.3): depois que muitas trajetórias tiverem rodado, é possível
**derivar** uma matriz "regra anterior → regra posterior" — quantas vezes,
ao longo de uma trajetória, a candidata predominante mudou de uma regra
para outra. Essa matriz é um **produto de análise**, e existe **depois** da
geração, calculada sobre os rastros já produzidos. Ela **nunca** é lida de
volta pelo kernel de transição do estado factual (§12.5) — fazer isso
reintroduziria exatamente a circularidade que §1 rejeita, só que numa etapa
posterior do pipeline em vez de na primeira.

### 12.8 Markov não é previsão atuarial

Explícito, sem ambiguidade, para toda saída desta extensão, em qualquer
fase:

- **parâmetros sintéticos não estimam incidência real** — nenhum número do
  kernel (§12.6) representa a probabilidade real de um servidor sofrer
  incapacidade, nem a distribuição real de causas;
- **percentuais não representam segurados reais** — nenhuma métrica é uma
  estatística sobre o IPERON ou sobre qualquer população real;
- **o objetivo é encontrar lacunas, ambiguidades, colisões, instabilidade e
  fronteiras defeituosas** no catálogo — não prever concessões nem
  dimensionar reservas;
- **eventual calibração com dados históricos é fase futura, com governança
  própria** (Fase 7, §15) — esta RFC não a autoriza nem a desenha em
  detalhe;
- **o simulador continua sendo experimental e hospedado em site pessoal**
  (mesmo rótulo institucional de RFC 0004 §12.2) — nada aqui produz uma
  ferramenta oficial do IPERON.

### 12.9 Exemplo trabalhado — trajetória sintética manual, passo a passo

Requerente sintético "S" (nenhum dado real, nenhuma correspondência com
pessoa ou processo existente) — este exemplo é explicitamente um traçado à
mão, no mesmo espírito do piloto de RFC 0002, e ilustra como a extensão
longitudinal ficaria **se** implementada; não é uma execução real:

1. **t₀ = 2010-03** — ingresso no serviço público e no cargo (mesma data,
   sem mudança de cargo nesta trajetória); `tipo_vinculo_funcional = estatutário`;
   `estado_funcional = ativo`; `incapacidade_ocorreu = false`. Qual regime
   previdenciário essa data de ingresso implica (EC41+LCE432, EC103+LC1100,
   ...) não é assumido aqui — é o avaliador, ao consumir
   `data_ingresso_servico_publico`, que deriva isso por universo, fora
   deste passo do gerador.
2. **t₁ = 2023-06** — passagem do tempo + acumulação de contribuição:
   `tempo_contribuicao_acumulado = tempo_servico_publico_acumulado = 159`
   meses; `estado_funcional` permanece `ativo`; `incapacidade_ocorreu`
   ainda `false`.
3. **t₂ = 2023-07** — **ocorrência de incapacidade**:
   `incapacidade_ocorreu: false → true`; `data_ocorrencia_incapacidade = 2023-07`; `classe_causa = indeterminada`; `duracao_incapacidade_meses = 0`;
   `tempo_aguardando_constatacao_meses = 0` (os dois acumuladores nascem
   juntos, mas evoluem de forma distinta a partir daqui, §12.5.1); todo
   `fatos_verificacao_humana[]` relevante começa `base_avaliacao: sem_informacao`, `avaliacao: indeterminado` — inclusive o requisito
   "doença enquadrada no rol aplicável" (face doença, abaixo), já que
   `diagnostico_classificacao` permanece `null` durante toda esta
   trajetória.
4. **t₃ = 2023-08** — **informação de hipótese pelo usuário sintético**:
   resposta "sim" à pergunta do protocolo de verificação "Há nexo entre a
   incapacidade e o acidente em serviço?" (RFC 0004 §3, exemplo);
   `fatos_verificacao_humana[]` ganha uma entrada `{predicado: "nexo com acidente em serviço", base_avaliacao: hipotese_informada, avaliacao: satisfeito}`. Nada disso é persistido em nenhum `regra-*.md` — é local a
   este caso sintético.
5. **t₄ = 2024-02** — **perícia / constatação documentada**:
   `{predicado: "nexo com acidente em serviço", base_avaliacao: constatacao_documentada, responsavel: "IPERON (sintético)", data: 2024-02-10, referencia: "laudo pericial sintético nº 1", avaliacao: satisfeito}` — **acrescentada** ao rastro, sem apagar a entrada
   anterior de `hipotese_informada` (§4.2). Nesse mesmo tick,
   `tempo_aguardando_constatacao_meses` **congela** no valor atingido em
   2024-02 (§12.5.1); `duracao_incapacidade_meses` continua incrementando
   normalmente nos ticks seguintes, porque mede a persistência do fato, não
   o atraso até a constatação. O requisito "doença enquadrada no rol
   aplicável" (face doença) permanece `sem_informacao`/`indeterminado`
   nesta trajetória — esta constatação é sobre nexo de acidente, um
   predicado distinto, e não fala nada sobre `diagnostico_classificacao`.

**Comparação nos três universos, ao longo da trajetória**:

| t   | Estado (resumo)                            | Universo 1 (legado as-is)                                                                                                                                                                                                                              | Universo 2 (auditado ativo)                                                                          | Universo 3 (auditado experimental)                                                                                                                                                                                                                                                                                                          |
| --- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| t₂  | incapacidade ocorrida, causa indeterminada | `0021`/`0022` não excluídas pelos critérios conhecidos (tipo de benefício, datas), sem campo de causa — indistinguíveis; pendência explícita de indistinguibilidade (mesma lógica de `sinalizarDivergenciaEntreRegrasIndistinguiveis`, `simulador.ts`) | **vazio** — nenhum grupo de substituição de invalidez está `estado_grupo: ativo` hoje (RFC 0004 §16) | as duas faces de `origens_legacy: [regra-0022]` (acidente, RFC 0004 §16.1; doença, §16.2), cada uma com seu **próprio** requisito: face acidente — "nexo com acidente em serviço" `indeterminado` (`sem_informacao`); face doença — "doença enquadrada no rol aplicável", também `indeterminado` (`diagnostico_classificacao` ainda `null`) |
| t₃  | + hipótese informada de acidente           | inalterado (o legado não tem esse predicado estruturado)                                                                                                                                                                                               | inalterado (vazio)                                                                                   | face acidente passa a `avaliacao: satisfeito` em seu requisito de nexo, rotulada **explicitamente** `hipotese_informada`; face doença **inalterada** em seu próprio requisito (rol) — nenhum fato sobre `diagnostico_classificacao` foi informado nesta trajetória                                                                          |
| t₄  | + constatação documentada                  | inalterado                                                                                                                                                                                                                                             | inalterado (vazio)                                                                                   | face acidente passa a `avaliacao: satisfeito` em seu requisito de nexo, rotulada `constatacao_documentada`; o rastro preserva as duas entradas anteriores (§4.2); face doença segue `indeterminado` — a constatação é sobre nexo de acidente, não sobre enquadramento no rol                                                                |

**Nenhuma etapa altera o manifesto de substituição, `estado_grupo`,
`decisao_completude`, o exportador ou qualquer artefato deployable** — o
universo 2 permanece exatamente como estava antes (vazio, para invalidez,
até que um humano ative um grupo fora deste pipeline); a face "acidente" do
universo 3 nunca se torna elegível ao export só por ter sido avaliada como
`satisfeito` dentro da simulação.

**Contrafactual — alterando só a constatação**: mesma trajetória até t₃; em
t₄, ao invés de uma constatação positiva, a perícia sintética produz
`{predicado: "nexo com acidente em serviço", avaliacao: não satisfeito}`
(nexo negado). O universo 3 diverge exatamente nesse ponto: a face acidente
passa a `excluída` em seu próprio requisito (nexo confirmado não
satisfeito). A face doença **não é afetada** por essa constatação — o
**seu** requisito é "doença enquadrada no rol aplicável", nunca "nexo com
acidente em serviço"; a perícia sintética deste contrafactual só fala sobre
nexo de acidente, então o requisito da face doença permanece
`indeterminado` pela mesma razão de sempre nesta trajetória (nenhum fato
sobre `diagnostico_classificacao` foi informado) — não porque "a mesma
constatação" tenha deixado de alcançá-la, mas porque é um predicado
estruturalmente distinto que o avaliador nunca mistura com o de nexo. O
universo 1 continua **idêntico** em ambos os ramos do contrafactual — ele
não tem o predicado estruturado, então não tem como reagir à mudança. Essa
divergência (universo 3 muda, universo 1 não) é precisamente o tipo de
achado que a métrica "divergência entre universos" (§6) foi desenhada para
capturar.

### 12.10 Estratégias de amostragem específicas de trajetória

As estratégias de geração híbrida do MVP (§2.2) valem igualmente aqui;
duas são específicas de uma trajetória evoluindo no tempo, e só fazem
sentido nesta extensão:

- **alternância entre hipótese informada e constatação documentada** — a
  mesma trajetória rodada duas vezes, uma só com hipótese, outra com
  constatação, comparando os rastros lado a lado (é exatamente o exemplo
  trabalhado, §12.9);
- **trajetórias que atravessam mudança normativa** — um `instante_simulado`
  que cruza a vigência de uma emenda durante a trajetória (não só um estado
  estático perto do limite), testando se `versoes_rol_candidatas` se
  restringe corretamente conforme `data_referencia_versao_rol` avança, e se
  a classificação de regime previdenciário que o avaliador deriva de
  `tipo_vinculo_funcional` + datas de ingresso muda no momento certo.

## 13. Arquitetura proposta, sem implementação

Nenhum destes é criado nesta RFC — os nomes e o layout ficam sujeitos a uma
implementação revisável (Fase 1 em diante, §15). Localizações
**propostas**, seguindo os padrões já estabelecidos no repositório
(biblioteca pura + CLI fina, RFC 0001 P10; separação schema/config/artefato
derivado):

| Componente                         | Papel                                                                                                                                                                     | Localização proposta                                                                                                                                                                  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| schema do requerimento sintético   | define o vetor de fatos (§4) como modelo tipado (Pydantic ou equivalente, mesmo padrão de `achado_schema.py`/`regra_schema.py`)                                           | `scripts/cenario_schema.py` (proposto)                                                                                                                                                |
| gerador sistemático                | produz casos de fronteira/mutação/pares (§2.2)                                                                                                                            | `scripts/stress/gerador_sistematico.py` (proposto)                                                                                                                                    |
| kernel de cobertura estrutural     | dados de configuração versionados (§2.3), não código                                                                                                                      | `stress/kernels/cobertura/` (proposto — fora de `okf/`, porque não é um bundle OKF de conceitos, é configuração numérica)                                                             |
| kernel de plausibilidade sintética | dados de configuração versionados (§2.3), não código                                                                                                                      | `stress/kernels/plausibilidade/` (proposto)                                                                                                                                           |
| adaptador para os três universos   | lê os bundles (`okf/regras-sisprev/`, o catálogo enriquecido de RFC 0004) e expõe uma interface comum aos três universos                                                  | `scripts/stress/universos.py` (proposto)                                                                                                                                              |
| avaliador                          | confronta um caso com um universo e produz o resultado estrutural (§5.3) — pode, no futuro, ser compartilhado com o simulador exploratório (§0), decisão de implementação | `scripts/stress/avaliador.py` (proposto)                                                                                                                                              |
| coletor de métricas                | calcula as métricas de §6 sobre um conjunto de rastros                                                                                                                    | `scripts/stress/metricas.py` (proposto)                                                                                                                                               |
| motor de gates                     | avalia os gates de §8/§14 sobre uma execução, decide promoção                                                                                                             | `scripts/stress/gates.py` (proposto)                                                                                                                                                  |
| registry de benchmarks             | persiste identidade (§9.1), estado (`vigente`/`revogado`, §9.4), manifesto de execução                                                                                    | formato e localização a definir na implementação; nunca sobrescreve um `benchmark_id` existente                                                                                       |
| serialização dos rastros           | formato de saída reprodutível (§11), inclui o manifesto de execução (§9.2)                                                                                                | provavelmente não versionado em git (mesmo padrão de `site/src/data/dados-do-site.json`, RFC 0003), regenerável por execução, exceto o registry de identidade/revogação de benchmarks |
| runner (camada PR/main)            | CLI fina, orquestra sistemático + kernels → avaliador → gates → resultado, com escopo pequeno/médio (§7)                                                                  | `scripts/stress_smoke.py` (proposto, mesmo padrão de CLI fina de `validar_regras.py`)                                                                                                 |
| runner (camada benchmark)          | orquestra a execução grande agendada/sob demanda, registra no registry, dispara promoção (§8)                                                                             | `scripts/stress_benchmark.py` (proposto), workflow próprio (fora do `ci.yml`, mesmo padrão de separação de `site.yml`, RFC 0003)                                                      |
| visualizações                      | consome rastros/métricas serializados, produz os diagramas propostos (Sankey, heatmap, explorador) quando há execuções reais                                              | possivelmente `site/` numa fase futura (§15, Fase 4), nunca antes disso                                                                                                               |
| extensão longitudinal (Markov)     | kernel de transição temporal (§12.5), gerador de trajetórias, matriz regra-anterior→regra-posterior — implementada só se/quando a Fase 6 (§15) avançar                    | `scripts/stress/longitudinal/` (proposto, fase futura)                                                                                                                                |

## 14. Gates futuros propostos

| Código proposto                                  | O que verifica                                                                                                                                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `P_SIM_SCHEMA_INVALIDO`                          | um requerimento sintético não valida contra o schema (§4)                                                                                                                                                                     |
| `P_SIM_KERNEL_INVALIDO`                          | algum dos dois kernels aleatórios (§2.3), ou o kernel de transição da extensão longitudinal (§12.6), não soma 1 sobre seu próprio espaço de amostragem, tem probabilidade negativa, ou falta `versao`/`fonte`/`justificativa` |
| `P_SIM_INVARIANTE_TEMPORAL`                      | qualquer violação de §12.5.3 (ordem, monotonicidade, constatação antes do fato, vigência fora do período) — só se aplica à extensão longitudinal                                                                              |
| `P_SIM_SEED_NAO_REPRODUTIVEL`                    | mesma seed mestra + mesma configuração produz saída diferente entre execuções (§9.2)                                                                                                                                          |
| `P_SIM_MUTOU_CATALOGO`                           | gerador ou avaliador escreveu em `okf/`, `data/` ou qualquer artefato derivado                                                                                                                                                |
| `P_SIM_EFEITO_MANIFESTO`                         | qualquer alteração de `estado_grupo`, `decisao_completude`, manifesto de substituição ou export (RFC 0004 §1.4/§12.1)                                                                                                         |
| `P_SIM_UNIVERSO_MISTURADO`                       | avaliação de um universo vazou para outro (p.ex. usar candidata do universo 3 para preencher o universo 2)                                                                                                                    |
| `P_SIM_BASE_AVALIACAO_PERDIDA`                   | uma entrada `hipotese_informada` foi sobrescrita em vez de complementada por `constatacao_documentada`, ou o rótulo desapareceu numa visualização/métrica (§4.2)                                                              |
| `P_SIM_RASTRO_INCOMPLETO`                        | rastro não permite reconstruir os fatos/avaliações/contradições completos de um caso (§11)                                                                                                                                    |
| `P_SIM_METRICA_NAO_DERIVAVEL`                    | uma métrica reportada não pode ser recalculada a partir do rastro serializado (mesmo princípio de `bundle.covering_tests`, RFC 0001)                                                                                          |
| `P_SIM_SEM_TESTE_METAMORFICO`                    | uma mudança no gerador/avaliador não inclui teste metamórfico correspondente (§2.4, invariância e sensibilidade)                                                                                                              |
| `P_SIM_FRONTEIRA_AUSENTE`                        | o conjunto obrigatório de casos sistemáticos de fronteira (§2.2) não está coberto por uma execução de referência                                                                                                              |
| `P_SIM_PREDICADO_DE_NOME`                        | o avaliador inferiu um predicado a partir de `nome` ou `fundamentacao*` em prosa, em vez de ler `auditoria.predicados` estruturado (mesmo princípio de RFC 0004 §12.2)                                                        |
| `P_SIM_SUITE_MISTURADA`                          | uma métrica, gate ou visualização mistura casos da suíte coerente com a adversarial sem rótulo separado (§2.4)                                                                                                                |
| `P_SIM_RANKING_CONTAMINOU_RESULTADO`             | o ranking experimental (§5.3) alterou, filtrou ou reordenou o conjunto estrutural de candidatas/exclusões/indeterminações                                                                                                     |
| `P_SIM_REGRA_INVENTADA`                          | um caso sistemático carrega uma expectativa de "regra correta" para uma questão que ainda depende de decisão jurídica não resolvida (§6.1)                                                                                    |
| `P_SIM_ROTULO_DE_VERDADE_EM_ALEATORIO`           | um caso da geração aleatória (qualquer um dos dois kernels) carrega um rótulo de "resposta certa" (§6.2)                                                                                                                      |
| `P_SIM_BENCHMARK_ID_COLIDIU`                     | dois benchmarks distintos compartilham o mesmo `benchmark_id` (§9.1)                                                                                                                                                          |
| `P_SIM_BENCHMARK_REESCRITO`                      | o conteúdo de um `benchmark_id` já publicado foi alterado ou apagado em vez de revogado com sucessor (§9.4)                                                                                                                   |
| `P_SIM_COMPARACAO_ENTRE_PROTOCOLOS_NAO_ROTULADA` | uma comparação entre execuções de `benchmark_protocol_version` diferentes aparece como regressão/melhora em vez de rotulada "estrutural" (§9.3)                                                                               |
| `P_SIM_DADO_REAL_NO_CORPUS`                      | qualquer fato de uma solicitação real (nome, CPF, processo, ...) aparece em um caso sintético ou artefato publicado (§10)                                                                                                     |
| `P_SIM_PROMOCAO_SEM_GATES`                       | um benchmark foi publicado no site sem os gates de integridade/validade/reprodutibilidade terem passado (§8)                                                                                                                  |
| `P_SIM_LOTE_COMPLETO_INDISPONIVEL`               | um benchmark publicado não tem o artefato compacto de download do lote completo disponível (§10)                                                                                                                              |

## 15. Plano incremental

Cada fase é uma PR revisável e independente; nenhuma fase autoriza pular
para a seguinte sem aprovação — mesmo padrão de RFC 0004 §15.

| Fase  | Entrega                                                                                                                                                                                                                                                               | Rollback                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **0** | Esta RFC. Nenhum código, nenhuma regra.                                                                                                                                                                                                                               | Fechar a PR.                                                                                            |
| **1** | Schema do requerimento sintético (§4) + gerador sistemático mínimo (fronteiras/mutação/pares para a família de invalidez, §2.2) + avaliador nos três universos (§5) — sem os dois kernels aleatórios ainda, sem site, só smoke local/CI (§7).                         | Remover o diretório/módulo novo; nenhum artefato existente é tocado.                                    |
| **2** | Dois kernels aleatórios completos (§2.3) + suítes coerente/adversarial (§2.4) + critérios de aceitação (§6) + gates estruturais (§14) rodando como smoke de PR (§7).                                                                                                  | Reverter a PR da Fase 2; a Fase 1 permanece funcional.                                                  |
| **3** | Execução em camadas completa: referência de `main` + benchmark grande agendado/sob demanda (§7) + identidade/versionamento/revogação (§9) + promoção automática com gates (§8).                                                                                       | Reverter a PR da Fase 3; a execução volta a só PR-smoke.                                                |
| **4** | Métricas (§6) e rastros (§11) com dados reais de execuções sintéticas — primeira vez com números, sempre rotulados com `benchmark_id` — + publicação no site (§10): explorador, Sankey/heatmap, artefato de download.                                                 | Remover a publicação/coletor de métricas; o gerador/avaliador das Fases 1–3 continuam válidos sem eles. |
| **5** | Ranking experimental (§5.3) — implementado e publicado, sempre separado visualmente do resultado estrutural.                                                                                                                                                          | Remover o ranking; o resultado estrutural continua íntegro sem ele.                                     |
| **6** | Extensão longitudinal (Markov, §12) — kernel de transição temporal, trajetórias, matriz regra-anterior→regra-posterior. Decisão explícita e nova PR de design antes de codar, mesmo com o desenho detalhado já pronto em §12.                                         | Reverter; as Fases 1–5 continuam válidas sem ela.                                                       |
| **7** | Eventual calibração com dados históricos — **somente mediante decisão e governança próprias**, fora do escopo desta RFC; exigiria uma RFC nova tratando de proveniência de dados reais, privacidade e o limite entre stress estrutural e estimativa atuarial (§12.8). | Reverter para kernels sintéticos; nenhuma Fase anterior depende de dados reais.                         |
| **8** | Expansão para outras modalidades (pensão, voluntária, professor, compulsória, PCD) — reaproveitando o schema do requerimento sintético (§4) generalizado, sob nova decisão de escopo.                                                                                 | Cada modalidade nova é aditiva; remover uma não afeta as demais.                                        |

## 16. Questões abertas

Listadas sem presunção de resposta — cada uma é trabalho de investigação ou
decisão humana futura, não desta RFC:

- **limiar de "mudança grande" de métrica** para disparar alerta (§8) —
  não decidido; calibrar empiricamente depois dos primeiros benchmarks
  reais;
- **tamanhos exatos das camadas** de execução (§7) — os valores da tabela
  são ilustrativos, não um compromisso;
- **formato do artefato de download** do lote completo (§10) — parquet?
  jsonl comprimido? não decidido;
- **arquivamento de benchmarks revogados muito antigos** — nunca apagar
  (§9.4), mas paginação/arquivamento do explorador não decidido;
- **se o kernel de plausibilidade sintética deveria, no futuro, ser
  informado por padrões observáveis publicamente** (sem dados pessoais) —
  mantém-se fechado por ora, mesma barreira de RFC 0004 §12.2 sobre dados
  reais;
- **granularidade mensal ou por evento** — relevante só para a extensão
  longitudinal (§12.2); um kernel orientado a evento pode se mostrar mais
  adequado depois do piloto dela;
- **Markov aumentado ou semi-Markov** — deixado explicitamente em aberto em
  §12.3, com o gatilho de revisão já registrado;
- **fontes futuras das probabilidades** — hoje só sintéticas (§9.5); se e
  quando dados reais entrarem em consideração (Fase 7), a fonte, a
  governança e os limites éticos ainda precisam de decisão própria;
- **quais estados são terminais** na extensão longitudinal — além de óbito,
  se `estado_funcional` admite outros estados terminais não está decidido;
- **tratamento de correlações** — entre coordenadas do schema (p.ex.
  `classe_causa` e `estado_funcional` podem ser correlacionadas no mundo
  real) não modelado nesta RFC;
- **horizonte temporal e volume mínimo de trajetórias** — só relevantes
  se/quando a extensão longitudinal (§12) avançar;
- **política para eventos raros** — se e quando adotar importance sampling
  para os dois kernels do MVP (§2.3) ou para a extensão longitudinal, e com
  qual critério de "raro", fica em aberto;
- **limites do ranking probabilístico** — se e como uma "estabilidade do
  ranking experimental" deveria influenciar qualquer decisão de auditoria
  (a resposta default, na ausência de decisão, é "não deveria" — mas isso
  não está formalmente fechado aqui).

## 17. Condições de parada honradas por esta RFC

- **RFC-only**: nenhum código foi escrito.
- **Nenhuma regra alterada**: nenhum `regra-*.md` foi tocado.
- **Nenhum campo novo nos schemas já implementados**: o schema do
  requerimento sintético (§4) é uma proposta separada, não uma extensão de
  `Regra`, `Achado`, `Dispositivo` ou do `auditoria:` de RFC 0004.
- **Nenhuma probabilidade apresentada como dado real**: todo número neste
  documento é rótulo de coluna/estrutura ou exemplo ilustrativo
  explicitamente rotulado como tal, nunca um valor executado.
- **Nenhuma decisão jurídica nova**: as pendências P-1 a P-6 e Q1–Q12/Q6-S
  permanecem exatamente como a reconciliação e a base normativa as deixaram
  — esta RFC as usa como insumo de design, nunca as resolve; casos
  sistemáticos nunca carregam uma "regra correta" inventada (§6.1).
- **Nenhum resultado fictício apresentado como experimento executado**: o
  único conteúdo com "resultado" é o exemplo trabalhado da extensão
  longitudinal (§12.9), explicitamente rotulado como traçado manual, no
  mesmo espírito do piloto de RFC 0002.
- **Gates locais verdes**: `md_format`, `ruff format`/`check`, `ty check` e
  `pytest` seguem passando — esta PR altera só este arquivo de
  documentação.
- **PR draft, não mergeada**: aberta como rascunho para revisão.
