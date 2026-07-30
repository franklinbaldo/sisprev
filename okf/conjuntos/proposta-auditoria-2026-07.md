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
    estado_grupo: ativo
    decisao_completude:
      decidido_por: franklinbaldo
      decidido_em: 2026-07-30
      fonte: okf/regras-auditadas/unidades/policial-civil-voluntaria-masculino.md
      justificativa: >-
        O grupo é 1:1 e seu único destino está escrito por inteiro: a projeção
        das 27 colunas legadas compila `deployable` sem pendência e difere da
        `regra-0078` em exatamente uma coluna,
        `fundamentacao_integral` — a troca da alínea "b" pela "a" da LC
        51/1985 e do descritor "mulher" por "homem", que é o defeito do
        `achado-0017`. Não há descendente que ninguém escreveu: o achado
        alcança três regras, e as outras duas (`regra-0079`, que cita
        corretamente, e `regra-0084`, cujo provimento judicial não foi
        localizado) não são origens deste grupo. Completude é do grupo, não do
        achado.
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

**`estado_grupo` é uma afirmação sobre a proposta, não sobre a produção.** O
grupo do policial está `ativo`: seu destino compila `deployable` e a
`decisao_completude` está registrada, o que é exatamente o que a ativação exige
— o grupo está escrito por inteiro e reverte inteiro. O da deficiência segue
`inativo`, porque suas seis unidades ainda estão em `elaboracao`, e um grupo
`inativo` **não pode** carregar `decisao_completude` (rollback tem de limpá-la,
`P15_DECISAO_SEM_ATIVACAO`) — é por isso que "grupo pronto" e "grupo em
produção" não são o mesmo estado e não se escrevem no mesmo campo.

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
