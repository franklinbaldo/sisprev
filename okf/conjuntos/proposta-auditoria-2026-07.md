---
type: Conjunto
id: proposta-auditoria-2026-07
nome: Proposta da auditoria — julho de 2026
situacao: proposto
base: catalogo-legado
substituicoes:
  - grupo: servidor-com-deficiencia-por-grau
    origens_legacy:
      - /regras/regra-0059.md
      - /regras/regra-0060.md
      - /regras/regra-0061.md
      - /regras/regra-0062.md
      - /regras/regra-0063.md
      - /regras/regra-0064.md
    destinos_auditados:
      - /regras-auditadas/unidades/servidor-com-deficiencia-moderada-feminino.md
      - /regras-auditadas/unidades/servidor-com-deficiencia-moderada-masculino.md
      - /regras-auditadas/unidades/servidor-com-deficiencia-grave-feminino.md
      - /regras-auditadas/unidades/servidor-com-deficiencia-grave-masculino.md
      - /regras-auditadas/unidades/servidor-com-deficiencia-leve-feminino.md
      - /regras-auditadas/unidades/servidor-com-deficiencia-leve-masculino.md
    estado_grupo: inativo
  - grupo: policial-civil-alinea-masculina
    origens_legacy:
      - /regras/regra-0078.md
    destinos_auditados:
      - /regras-auditadas/unidades/policial-civil-voluntaria-masculino.md
    estado_grupo: inativo
---

# O que este conjunto é

A **primeira composição derivada** do catálogo: o que a auditoria propõe em
julho de 2026, ao lado do que está em vigor. `situacao: proposto`, `base: catalogo-legado` — nada aqui substitui nada hoje.

Ele existe porque editar uma regra é destrutivo. Corrigir a `regra-0078` no
lugar apagaria o estado anterior, que só sobreviveria em `data/raw/` e no git —
nenhum dos dois consultável como catálogo. Este documento é o que permite dizer,
ao mesmo tempo, *"esta é a regra operada"* e *"esta é a que a auditoria propõe no
lugar dela"*.

# Por que a marca não está nas regras

A leitura intuitiva seria marcar cada regra original como "a ser desativada". A
RFC 0006 decidiu o contrário, e por uma razão que se comprova em vez de se
argumentar: **o frontmatter das 112 regras não muda.**

Se houvesse um campo `a_desativar` numa regra, ele entraria — ou teria de ser
deliberadamente excluído — da **chave material do `P2_IGUALDADE_MATERIAL_ATIVA`**,
que trata toda coluna de domínio como material. Marcar seis regras faria grupos
P2 aparecerem ou desaparecerem por causa de um campo de escrituração, não de
mérito. O diagnóstico da auditoria se moveria sem que nenhum fato jurídico
tivesse mudado.

Com o delta no conjunto, a pertinência é **derivada**:
`regras(C) = regras(base) − origens − revogadas + destinos + introduzidas`. A
regra legada continua intacta em identidade e cardinalidade, e "esta regra está
proposta para substituição" passa a ser uma **consulta**, não um campo.

Há também o caso que um campo na regra não cobriria: **revogação pura**, sem
sucessora. Não existe documento onde pendurar a marca, e é para isso que o
conjunto tem `revoga` — hoje vazio.

# Os dois grupos, e por que são atômicos

Um `GrupoSubstituicao` **ativa e reverte inteiro**. A composição dos dois grupos
segue disso:

**`servidor-com-deficiencia-por-grau`** — seis origens, seis destinos, 6:6. Não
é um grupo por conveniência de tamanho: as seis unidades **só fazem sentido
juntas**. O que cada uma acrescenta é a identificação do seu grau na
fundamentação, e é a existência das outras cinco que torna a distinção
informativa. Ativar só a "grave" deixaria as outras quatro no estado atual, em
que moderada e leve continuam materialmente idênticas — trocaria dois grupos P2
por um, sem resolver nada.

**`policial-civil-alinea-masculina`** — uma origem, um destino, 1:1. A
`regra-0078` cita a alínea feminina da LC 51/1985 tendo `sexo: MASCULINO`
(ver [`achado-0017`](../regras-sisprev/achados/achado-0017.md)); a unidade
propõe a alínea "a" e o descritor "homem". A `regra-0079`, gêmea feminina, cita
corretamente e **não entra** — não há o que substituir nela.

Os dois estão `inativo`, o que é obrigatório enquanto as unidades estiverem em
`estado_unidade: elaboracao`. Ativar exige `decisao_completude`, isto é, decisão
humana registrada — e nenhuma foi tomada.

# O que este conjunto não faz

- **Não altera a exportação operacional**, que segue 100% do bundle legado. Como
  `catalogo_vigente` continua sendo `catalogo-legado`, a resolução não passa por
  aqui.
- **Não transita para `vigente`.** Isso exige `autoridade`,
  ato de ativação e `decisao_completude`, ausentes de propósito.
- **Não cobre as demais regras com achado.** Vinte e um achados estão abertos, e
  a maioria descreve defeito cuja correção ainda não foi proposta como unidade.
  Este conjunto é o começo do registro, não o seu fim — e é por isso que se chama
  pela data.
- **Não resolve o campo `fundamentacao` de `regra-0061`/`0062`**, que cita um
  parágrafo único inexistente do art. 39 da LCE 432/2008
  ([`achado-0021`](../regras-sisprev/achados/achado-0021.md)). As unidades do
  grupo tocam `fundamentacao_integral`; aquele campo é outro defeito, com decisão
  própria, e está registrado como tal.
