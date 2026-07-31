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
  - grupo: agentes-nocivos-art-41-iii-integralidade-paridade
    origens_legacy:
      - /regras/regra-0065.md
      - /regras/regra-0066.md
      - /regras/regra-0067.md
    destinos_auditados:
      - /regras-auditadas/unidades/agentes-nocivos-art-41-iii-integralidade-paridade.md
    estado_grupo: inativo
  - grupo: agentes-nocivos-art-41-iii-media-sem-paridade
    origens_legacy:
      - /regras/regra-0071.md
    destinos_auditados:
      - /regras-auditadas/unidades/agentes-nocivos-art-41-iii-media-sem-paridade.md
    estado_grupo: inativo
  - grupo: policial-civil-alinea-masculina
    origens_legacy:
      - /regras/regra-0078.md
    destinos_auditados:
      - /regras-auditadas/unidades/policial-civil-voluntaria-masculino.md
    estado_grupo: inativo
revoga:
  - /regras/regra-0016.md
  - /regras/regra-0017.md
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

# Os quatro grupos, e por que são atômicos

Um `GrupoSubstituicao` **ativa e reverte inteiro**. A composição dos dois grupos
segue disso:

**`servidor-com-deficiencia-por-grau`** — seis origens, seis destinos, 6:6. Não
é um grupo por conveniência de tamanho: as seis unidades **só fazem sentido
juntas**. O que cada uma acrescenta é a identificação do seu grau na
fundamentação, e é a existência das outras cinco que torna a distinção
informativa. Ativar só a "grave" deixaria as outras quatro no estado atual, em
que moderada e leve continuam materialmente idênticas — trocaria dois grupos P2
por um, sem resolver nada.

**`agentes-nocivos-art-41-iii-integralidade-paridade`** — três origens, um
destino, 3:1. `regra-0065` e `regra-0066` são materialmente idênticas, e
`regra-0067` difere apenas no membro de `tipo_calculo`. As três apontam para o
mesmo texto e o mesmo processo na planilha da PGE. O destino consolida a
hipótese, corrige os dois limites temporais incompatíveis com os arts. 25 e 27,
I, e adota `Valor Efetivo` como hipótese de trabalho. O grupo permanece
inativo porque a unidade está em `preview`: o significado do enum de cálculo,
`tabelapontuacao` e a cobertura dos incisos I e II do art. 41 ainda dependem de
decisão.

**`agentes-nocivos-art-41-iii-media-sem-paridade`** — uma origem, um destino,
1:1. É a irmã pós-2003 do grupo anterior: preserva `Valor Médio`,
`paridade: N` e o marco de direito da LCE 1.100/2021, mas move o corte
31/12/2003 de `data_adm_ate` para `data_adm_apos`, conforme os arts. 24 e 27,
II. O grupo segue inativo porque a unidade está em `preview`, aguardando as
mesmas decisões sobre `tabelapontuacao` e sobre a cobertura dos incisos I e II
do art. 41.

**`policial-civil-alinea-masculina`** — uma origem, um destino, 1:1. A
`regra-0078` cita a alínea feminina da LC 51/1985 tendo `sexo: MASCULINO`
(ver [`achado-0017`](../regras-sisprev/achados/achado-0017.md)); a unidade
propõe a alínea "a" e o descritor "homem". A `regra-0079`, gêmea feminina, cita
corretamente e **não entra** — não há o que substituir nela.

**`estado_grupo` é uma afirmação sobre a proposta, não sobre a produção.** O
grupo da deficiência segue `inativo`, porque suas seis unidades ainda estão em
`elaboracao`; os dois de agentes nocivos, porque seus destinos estão em
`preview`; e o do policial, porque a correção já foi aplicada diretamente à
origem e o grupo ficou sem objeto. Um grupo `inativo` **não pode** carregar
`decisao_completude` (rollback tem de limpá-la,
`P15_DECISAO_SEM_ATIVACAO`) — é por isso que "unidade escrita" e "grupo
completo" não são o mesmo estado e não se escrevem no mesmo campo.

O que separa a proposta da produção é a `situacao` deste documento, não o
`estado_grupo` dos seus grupos. `catalogo_vigente` resolve **só** o conjunto
`vigente`, e este é `proposto`: um grupo ativo aqui não move uma linha do
catálogo exportado. Adotá-lo é promover o conjunto, ato que exige `autoridade` e
ato de ativação, e que ninguém praticou.

# O que este conjunto não faz

- **Não altera a exportação operacional**, que segue 100% do bundle legado. Como
  `catalogo_vigente` continua sendo `catalogo-legado`, a resolução não passa por
  aqui.
- **Não transita para `vigente`.** Isso exige `autoridade`,
  ato de ativação e `decisao_completude`, ausentes de propósito.
- **Não cobre as demais regras com achado.** A maioria dos achados abertos
  descreve defeito cuja correção ainda não foi proposta como unidade. Este
  conjunto carrega os grupos que existem, não os que faltam, e é por isso que se
  chama pela data. A contagem não fica escrita aqui porque envelheceria a cada
  achado autorado — quem quer o recorte roda
  `uv run python scripts/validar_regras.py` e lê os achados.
- **Não resolve o campo `fundamentacao` de `regra-0061`/`0062`**, que cita um
  parágrafo único inexistente do art. 39 da LCE 432/2008
  ([`achado-0021`](../regras-sisprev/achados/achado-0021.md)). As unidades do
  grupo tocam `fundamentacao_integral`; aquele campo é outro defeito, com decisão
  própria, e está registrado como tal.

# A revogação das duas regras de pensão desdobradas por sexo

`regra-0016` e `regra-0017` desdobram por sexo uma regra de pensão por morte cujo
conjunto de dispositivos citados não diferencia por sexo — a conferência está no
`achado-0056`, e a única menção ao sexo nos onze dispositivos, no art. 51, II da
LCE 1.100/2021, é cláusula equalizadora. A `regra-0018` cita exatamente os mesmos
dispositivos e grava `AMBOS`, que é o que eles dizem.

**Por que revogação e não correção de campo.** A alternativa seria gravar `AMBOS`
nas duas, alinhando-as ao que a norma diz. Foi tentada e descartada, e o motivo é
estrutural, não de gosto: alterar critério de regra legada muda a **chave
material** do P2. As três passariam a ser materialmente idênticas, o detector
formaria um grupo novo, e o estado conhecido do catálogo — ancorado em teste —
mudaria por efeito de uma edição cujo propósito era outro. A regra legada é o que
foi operado; corrigi-la no lugar apaga esse fato em favor do que deveria ter
sido.

A revogação faz o oposto e é o motivo de o delta viver aqui: o frontmatter das
regras não muda, a chave material do P2 fica intocada **por construção**, e o
catálogo passa a poder dizer as duas coisas ao mesmo tempo — que estas regras
foram operadas, e que a auditoria propõe que deixem de existir.

**Por que revogação pura, sem destino.** Um grupo de substituição existe quando há
sucessor a apontar. Aqui não há: a `regra-0018` permanece, herdada da base, e já
carrega o conteúdo íntegro das três. Inventar uma unidade auditada para ser
destino criaria documento novo para dizer o que uma regra existente já diz. É
exatamente o caso que a RFC 0006 descreve — revogação pura não tem documento
sucessor onde se pendurar, e é por isso que o delta é do conjunto.

**São duas, e a que permanece é a `regra-0018`.** Ela nunca afirmou o critério sem
lastro; as outras duas o afirmam cada uma para um sexo. O critério de escolha é
esse, e não menor `row_index` ou uso histórico — o catálogo não registra uso.

**Enquanto este conjunto for `proposto`, nada sai do catálogo operado.** As duas
regras seguem em vigor, seguem exportadas ao CSV derivado, e o `achado-0056`
segue `aberto` — ele só se resolve quando a revogação alcançar o catálogo
vigente, o que exige `decisao_completude` no nível do conjunto e ato de ativação.

# Por que o grupo do policial civil foi desativado

O grupo `policial-civil-alinea-masculina` existia para propor, sem tocar na regra
de origem, a troca da alínea "b" pela "a" da LC 51/1985 no
`fundamentacao_integral` da `regra-0078` — o defeito do `achado-0017`. Ele esteve
`ativo`, com `decisao_completude` registrada.

A Decisão 10 de
[`docs/analysis/decisoes-de-auditoria-2026-07-30.md`](../../docs/analysis/decisoes-de-auditoria-2026-07-30.md)
autorizou a auditoria a alterar `FUNDAMENTACAO*` diretamente na regra, e a
correção foi aplicada ali. **O grupo ficou sem objeto**: seu destino propunha
exatamente o texto que a origem passou a ter.

`decisao_completude` foi removida junto, como o `P15_DECISAO_SEM_ATIVACAO` exige
— decisão de completude é da ativação, e um grupo desativado que a conserva
declara uma decisão que não vale mais. A justificativa que ela carregava também
tinha envelhecido por outro motivo: afirmava que o destino diferia da origem "em
exatamente uma coluna", e a renomeação do catálogo introduziu uma segunda,
`nome`.

**A unidade `policial-civil-voluntaria-masculino` permanece.** Ela é o documento
onde a correção foi escrita e conferida contra a fonte, e o `achado-0010` e a
disposição da `regra-0078` a citam como origem do texto adotado. Apagá-la
apagaria a proveniência de uma correção que hoje está no catálogo operado.
