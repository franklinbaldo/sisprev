# RFC 0007 — Prontidão de conjunto: o checklist que autoriza a produção

- **Status**: proposta (2026-07-28). **Especificação revisável, sem
  implementação.** Não edita nenhum `regra-*.md`, não altera o schema
  deployável, o CSV derivado, os dispositivos, os achados, os detectores, o
  simulador, o site nem os workflows. Entrega o desenho do gate e a medição do
  estado atual contra ele.
- **Parte de / depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P7
  `status_auditoria`, P13.1, P14 achados, camadas de detecção),
  [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) (compilador
  e ordem total normativa) e [RFC 0006](0006-conjuntos-de-regras.md), cujas
  fases 0 e 1 estão implementadas — `type: Conjunto`, `resolve(C)`,
  `substituicao_schema`, o gate do catálogo auditado. Esta RFC ocupa a lacuna
  que a RFC 0006 §10 chama de **fase 4 (ativação)** e diz apenas que exige
  "`decisao_completude` e ato suficiente", sem dizer o que é suficiente.
- **Não-objetivo**: responder a Q12 da RFC 0001 (qual fluxo institucional vale);
  autorar qualquer conjunto, unidade auditada ou achado — autorar é ato humano;
  alterar `data/raw/regras-sisprev.csv`, imutável para sempre; converter o P2
  para allowlist (RFC 0004 §11).

## 0. O problema

Hoje é possível responder "esta regra está válida?" — o P7 é um join
reverificado a cada commit. **Não** é possível responder "este conjunto de
regras pode entrar em produção no Sisprev?", e as duas perguntas não são a
mesma.

A distância entre elas é concreta. Uma regra pode estar `validada` e o conjunto
que a contém ainda não compilar; um conjunto pode ter ato da PGE e conter uma
regra cuja fundamentação cita um dispositivo que não existe; e — o caso que
mais preocupa — **todo o resto pode estar limpo e ainda assim haver 110
detecções camada 3 que ninguém nunca leu**, porque camada 3 não exige achado e
portanto não bloqueia nada. Entrar em produção assim não é uma decisão
informada: é uma decisão que não sabe o que está decidindo.

A RFC 0006 criou o objeto certo — o conjunto é o que se ativa e o que se
reverte inteiro — e parou antes do gate. Esta RFC é o gate.

## 1. Onde estamos hoje, medido

Números obtidos de `validar_regras.py --json`, `relatorio_citacoes.py` e do
próprio bundle, em 2026-07-28 (`75d5027`). O relatório
[estado-da-auditoria](../analysis/estado-da-auditoria.md) é anterior ao
trabalho de P3/P4 e seus totais já não batem; estes substituem os de lá.

| Item                                    | Hoje                                           |
| --------------------------------------- | ---------------------------------------------- |
| Regras no catálogo                      | 112                                            |
| `status_auditoria`                      | 112 `importada` (ausente)                      |
| Regras com trilha (`auditado_por`)      | 0                                              |
| Regras com as 4 seções P13.1            | **0** (corpo vazio em todas)                   |
| Regras com `dispositivos:` não vazio    | 95 (faltam 17)                                 |
| Regras com `atos_validacao`             | 0                                              |
| `validado_pge` / `validado_presidencia` | `FALSE` em 112 / 112                           |
| Violations (`validar_regras.py`)        | **0**                                          |
| Detecções totais                        | 156                                            |
| — camada 2 (`requires_achado`)          | 15 (7 P2 + 8 P4_REDACAO), **todas com achado** |
| — camada 3 sem achado                   | **110** (69 P4_CITACAO + 41 P1)                |
| Achados                                 | 13, **todos** `aberto` + `informativo`         |
| Regras tocadas por achado aberto        | 49                                             |
| Regras em grupo P1 ativo                | 94 (P2: 17)                                    |
| Conjuntos autorados                     | 1 (`catalogo-legado`, raiz, vigente)           |

Lidos juntos, três fatos organizam tudo o que falta:

1. **O corpo das 112 regras está vazio.** As quatro seções que o P7 exige para
   `revisada` não existem em nenhuma. É a barreira única e sistêmica: enquanto
   ela estiver de pé, *nenhuma* regra pode passar de `importada`, por mais
   limpo que esteja o resto.
2. **Nada está podre, muita coisa está por ler.** Zero violations e zero
   detecções camada 2 órfãs significa que o que o repositório afirma, ele
   sustenta. As 110 camada 3 sem achado não são erros — são leituras humanas
   ainda não feitas, e é exatamente essa a distinção que o gate precisa
   preservar sem deixá-las passar caladas.
3. **O conjunto raiz é o caso degenerado.** `catalogo-legado` já está em
   produção e é dispensado de `decisao_completude` e ato (RFC 0006 §6.1). O
   checklist não pode retroagir sobre ele — governa quem **transita**.

## 2. O que ainda falta, por frente

### 2.1 Corpo das regras (P13.1) — bloqueia tudo

Quatro seções obrigatórias, hoje ausentes em 112/112: `Critérios avaliados pelo Sisprev`, `Requisitos de verificação manual`, `Documentos ou evidências necessários`, `Resultado após a seleção`. O CI checa que a resposta **existe**,
nunca o mérito.

### 2.2 Dispositivos (P3/P4)

17 regras sem `dispositivos:`. Das 95 vinculadas, 69 ainda têm lacuna entre a
prosa da fundamentação e o que está declarado. A fila de transcrição é curta e
concentrada — 5 provisões da LCE 432/2008 (`art-20`, `art-31-par-1`,
`art-31-par-2`, `art-32-inc-i`, `art-33`) e 5 redações citadas cujo texto não
foi transcrito. A fila **vincular** está vazia: tudo que existe e é citado já
está declarado.

Restam três resíduos que não se resolvem transcrevendo: 7 provisões presas em
campo com mais de uma fundamentação (`|`), 8 citações sem norma identificável
mecanicamente, e 67 vínculos feitos à provisão inteira quando a prosa estreitava
a cláusula ("segunda parte") — resolução que o frontmatter não carrega.

### 2.3 Achados e detecções

Os 13 achados abertos são todos `informativo`, então nenhum bloqueia `revisada`
hoje. As 110 detecções camada 3 sem achado são o volume real: 69
`P4_CITACAO_NAO_VINCULADA` (caem junto com §2.2) e 41 `P1_NOME_REPETIDO`, que
sozinhas mantêm 94 das 112 regras fora de `revisada`.

### 2.4 Trilha e atos

Zero regras com `auditado_por`/`auditado_em`; zero com `atos_validacao`; zero
atos em qualquer conjunto. A Q12 da RFC 0001 — quais atos e quais fontes valem
institucionalmente — continua aberta, e o §4 abaixo diz onde a resposta se
registra sem fingir tê-la.

### 2.5 Infraestrutura ainda não construída

Da RFC 0006: fase 2 (primeiro conjunto proposto), fase 3 (atos e projeção de
`validado_*` por conjunto), fase 4 (ativação), fase 5 (site). Da RFC 0004: a
interleavação de linhas legadas não substituídas num único export.

## 3. O gate: `prontidao(C)`

**Prontidão é derivada, nunca declarada.** Não existe — e não pode passar a
existir — um campo `pronto_para_producao: true` que alguém digite. O que se
autora são atos humanos com autor, data e fonte: a decisão de completude e a
aceitação nominal de pendência. Todo o resto é join, recalculado a cada commit,
pelo mesmo motivo que o P7 é join: um conjunto pronto ontem deixa de estar
pronto quando um achado bloqueante é aberto sobre uma regra dele, **sem que
ninguém toque no conjunto**.

```python
prontidao(conjunto, bundle) -> Prontidao          # puro, sem I/O
Prontidao.itens: tuple[ItemProntidao, ...]
ItemProntidao(codigo, camada, titulo, satisfeito, evidencia, bloqueante)
```

Quatro camadas, avaliadas sobre `resolve(C)` — a pertinência, nunca um campo de
procedência (RFC 0006 §3).

### Camada 1 — cada regra do conjunto resolvido

| Código                   | Item                                                                          | Situação                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `P16_REGRA_VALIDADA`     | toda regra de `resolve(C)` com `status_auditoria: validada`                   | P7, já implementado                                                                      |
| `P16_REGRA_TRILHA`       | `auditado_por` + `auditado_em` real e não futuro                              | P7/P11, já implementado                                                                  |
| `P16_REGRA_P13_1`        | as 4 seções obrigatórias, não vazias                                          | P7, já implementado                                                                      |
| `P16_REGRA_DISPOSITIVO`  | `dispositivos:` **não vazio**, cada item resolvendo para uma redação autorada | **novo** — `check_p3_dispositivos` já resolve o que é declarado; falta exigir que exista |
| `P16_REGRA_P13_1_QUINTA` | quinta seção: *quais dispositivos justificam cada critério e efeito*          | **novo** — adiada pela RFC 0001 "até P3 existir"; P3 existe                              |

`P16_REGRA_VALIDADA` já arrasta, por P7, a ausência de achado bloqueante aberto
e a ausência de grupo P1/P2 ativo. Não se duplicam aqui.

### Camada 2 — o conjunto

| Código                     | Item                                                                                                                                         | Situação                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `P15_*`                    | exatamente um vigente, base resolvível e acíclica, proveniência dos grupos, `decisao_completude`, ato com `efeito: valida`                   | já implementado                            |
| `P16_ATO_POR_AUTORIDADE`   | `validado_pge`/`validado_presidencia` só projetam `TRUE` se houver ato daquela autoridade, com `efeito: valida` e `escopo: {tipo: conjunto}` | **novo** — RFC 0006 fase 3                 |
| `P16_PENDENCIA_NAO_ACEITA` | toda detecção camada 3 e todo achado aberto que toque `resolve(C)` está resolvido **ou** nominalmente aceito                                 | **novo** — o coração desta RFC, §4         |
| `P16_CONJUNTO_NO_OP`       | um `proposto` cuja projeção é byte-idêntica à da base é sinalizado                                                                           | **novo**, não bloqueante — RFC 0006 fase 2 |

### Camada 3 — o que efetivamente sai

| Código                   | Item                                                                                                 | Situação                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `P16_COMPILA_DEPLOYABLE` | toda unidade auditada em `resolve(C)` compila `deployable=True`, zero `P_COMPILA_*`                  | compilador pronto (RFC 0004 Fase 1A); falta ligar ao conjunto |
| `P16_SEM_COLISAO`        | `detectar_colisoes()` vazio                                                                          | pronto, idem                                                  |
| `P16_EXPORTA_FECHADO`    | nada no resolvido que o CSV de 27 colunas não compile — falha fechado, nunca omite                   | RFC 0006 §10 fase 0                                           |
| `P16_ORDEM_TOTAL`        | ordem determinística da RFC 0004 §1.6 sobre o conjunto                                               | **novo** — Q5 da RFC 0006                                     |
| `P16_DERIVADOS_EM_DIA`   | `derived-csv-in-sync`, `original-csv-immutable`, round-trip byte-idêntico, `emit_site_data` emitindo | já é gate de CI                                               |

### Camada 4 — humana, assinada, não checada

Não vira código, e por isso é a parte que o documento tem de nomear: o **mérito**
das respostas P13.1 (o CI só vê que existem); a Q12 da RFC 0001; a Q6 (causa da
incapacidade, regra-0021/0022, indecidível com as colunas atuais); e o aceite
operacional do Sisprev — janela de ativação e plano de reversão. Entram na
`justificativa` da `decisao_completude`, que é onde uma assinatura humana já
mora.

## 4. Aceitação de pendência: por item, com autor

O item que muda o comportamento real é `P16_PENDENCIA_NAO_ACEITA`. Hoje uma
detecção camada 3 não bloqueia nada — e essa é a semântica correta *para a
auditoria*: detecção não é conclusão, e exigir achado para as 110 obrigaria o
auditor a escrever 110 conclusões que ele ainda não tem. Mas o que é correto
para a auditoria é insuficiente para a **produção**: pôr em produção um conjunto
com 110 sinais não lidos é decidir sem saber.

A saída não é elevar a camada 3 a bloqueante. É exigir que, **no momento da
ativação e só nele**, cada pendência esteja num de dois estados: resolvida, ou
aceita nominalmente pelo conjunto.

```yaml
pendencias_aceitas:
  - referencia: "sha256:3575e88f…"     # fingerprint da detecção, ou id do achado
    decidido_por: …
    decidido_em: 2026-08-14
    justificativa: >-
      Nomes repetidos entre regra-0059 e regra-0063 são intencionais: a
      distinção está em data_direito_apos, não no rótulo.
    fonte: …
```

Três regras fecham a porta ao carimbo genérico:

- **Por item, nunca por classe.** Uma referência é um fingerprint ou um id de
  achado. Não existe aceitar "todos os P1", nem aceitar por severidade — porque
  aceitar por classe é exatamente a forma de não ler.
- **A referência tem de existir.** Uma aceitação que aponta para fingerprint
  inexistente é violação, não ruído: senão a lista envelhece em silêncio quando
  a detecção muda de fingerprint, e o conjunto passa a exibir uma leitura que
  ninguém fez.
- **Camada 2 não é aceitável.** Uma detecção `requires_achado=True` exige achado
  **resolvido**, nunca aceitação. É o que separa "há um sinal que decidimos
  tolerar" de "há uma citação legal falsa no documento que chega ao servidor".

## 5. Quando o gate morde

`P16_PRONTIDAO_INCOMPLETA` dispara para o conjunto que **é** `vigente` ou que
**transita** para `vigente`. Nunca para um `proposto`: um proposto com itens
abertos é o painel de trabalho normal — se o gate mordesse ali, ninguém
conseguiria autorar uma proposta antes de já a ter terminado, e a RFC 0006
perderia o objeto que ela criou para tornar a proposta representável.

Corolário, herdado do P7 e deliberado: **nada rebaixa sozinho**. Se um conjunto
vigente deixa de satisfazer a prontidão — um achado bloqueante novo sobre uma
regra dele, uma detecção camada 3 que apareceu depois da ativação — o CI passa a
falhar até que um humano registre a aceitação ou reverta o conjunto. O gate
vermelho é a função de forçamento; a máquina não decide por ninguém.

## 6. Superfícies

- `scripts/prontidao_conjunto.py` — `prontidao()` puro, sem I/O, testável
  isoladamente; camadas 1–3 como funções separadas.
- `scripts/relatorio_prontidao.py` — CLI **read-only**, `--json`, imprimindo os
  itens não satisfeitos ordenados por quantas regras cada um destrava (mesma
  forma do `relatorio_citacoes.py`, que já provou ser a leitura útil).
- `validar_regras.py` — acrescenta as violations à mesma lista, sem mudar a
  forma do payload `--json`, como `catalogo_auditado_gate` já faz.
- `/conjuntos/<id>/` no site (RFC 0006 fase 5) — o checklist renderizado, cada
  item levando à listagem recortada. A contagem se confere clicando; um item
  satisfeito mostra a evidência, não só o selo.

## 7. Plano incremental

1. **Fase A — medir sem bloquear.** `prontidao()` + o CLI, computando os itens
   já implementáveis (camadas 1 e 3). Nenhuma violation nova. Entrega o número
   honesto de quanto falta, que hoje só existe somando três relatórios à mão.
2. **Fase B — os dois itens novos da camada 1.** `P16_REGRA_DISPOSITIVO` e a
   quinta seção P13.1. Só valem dentro de `validada`, e como há 0 regras
   `validada`, entram sem quebrar nada — e ficam de pé antes da primeira
   transição, que é o único momento em que introduzi-las seria caro.
3. **Fase C — `pendencias_aceitas`.** Schema, validação de referência
   existente, recusa de camada 2. Inerte enquanto não houver conjunto
   transitando.
4. **Fase D — o gate.** `P16_PRONTIDAO_INCOMPLETA` na transição, depois da fase
   3 da RFC 0006 (atos e projeção), pelo mesmo motivo que ela dá: ativar sem os
   atos registrados é o que o P7 existe para impedir.
5. **Fase E — site.**

Ordem deliberada: o gate é o último. Construir o gate antes de haver o que ele
mede produz um vermelho que ninguém sabe apagar.

## 8. Questões em aberto

- **Q1 — `atos_validacao` da regra versus `atos` do conjunto.** A RFC 0006 §5
  mostrou que `validado_*` não pode ser campo estático; o mesmo argumento se
  aplica a `atos_validacao`, que hoje o P7 exige na regra para `validada`. Se um
  ato da PGE cobre o conjunto, exigi-lo *também* em cada regra duplica o
  registro e reintroduz o problema do campo estático. **Recomendação**:
  `validada` passa a admitir cobertura por ato do conjunto, projetada; o campo
  na regra permanece para validação que de fato foi individual. Não decidida
  aqui porque muda um invariante P7 já implementado e testado.
- **Q2 — Aceitação herda pela base?** Se `pge-2026` tem base em
  `catalogo-legado`, as aceitações da base valem? **Recomendação**: não. Herdar
  aceitação faz uma decisão tomada num contexto atravessar calada para outro —
  e é barato repetir o que ainda vale.
- **Q3 — Aceitação caduca?** Uma aceitação de 2026 continua valendo em 2029?
  **Recomendação**: caduca junto com o conjunto que a carrega, não por prazo.
  Prazo produziria vermelho de calendário, que se apaga sem leitura.
- **Q4 — Prontidão parcial.** Ativar metade de um conjunto. **Recomendação**:
  não — pela mesma razão que a RFC 0006 §5 dá para o escopo do ato. Validação
  parcial é **um conjunto menor**.
- **Q5 — Quem assina a `decisao_completude` do conjunto?** É a Q12 da RFC 0001
  aplicada a outro objeto, e continua aberta.

## 9. O que esta RFC não decide

- O fluxo institucional (Q12 da RFC 0001): §3 camada 4 diz **onde** a resposta
  se registra, não qual é.
- O mérito de qualquer resposta P13.1.
- Q1–Q5 acima.
- Qualquer conjunto, unidade auditada, achado ou aceitação concreta. Autorar é
  ato humano — nenhum comando cria nada disso, como nenhum comando cria um
  achado.
