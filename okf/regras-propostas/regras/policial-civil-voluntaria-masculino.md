---
type: RegraProposta
id: policial-civil-voluntaria-masculino
ciclo: ciclo-08
schema_version: 1
estado_auditoria: concluida
origens_legacy:
  - regra-0078
predicados:
  sexo: masculino
  regime: transitorio-ece-146-2021
  marco_ingresso: ate-2019-11-13
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 01/01/1950 00:00
    data_adm_ate: 13/11/2019 00:00
    data_direito_apos: 14/09/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/ece-146-2021/art-7-par-1/original.md
    papel: regra de transição — corte de ingresso até a vigência da EC 103/2019
  - ref: /dispositivos/ece-146-2021/art-7-par-3/original.md
    papel: integralidade dos proventos e paridade no reajuste
  - ref: /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
    papel: tempo de contribuição e de exercício policial exigidos do homem (30 e 20 anos)
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: competência e remissão à lei complementar do ente
projecao:
  nome: Voluntária do Policial Civil - Art. 7º, § 3º da EC nº 146/2021
  tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
  atualmente_no_sistema: 'TRUE'
  ciclo_de_validacao: 3º
  validado_pge: 'FALSE'
  validado_presidencia: 'FALSE'
  simulavel: S
  tipo: CIVIL
  apos_especial: S
  tipo_remun: ''
  paridade: S
  tabelapontuacao: N
  requisitos_da_in_no_5_2020: N
  relatorio_p_reserva_remunerada_por_idade_ex_officio: N
  adicional_inatividade: N
  fundamentacao_proporcional: ''
  visivel_dtc_proporcional: N
  fundamentacao_integral: >-
    Aposentadoria especial de policial, com proventos integrais (cálculo por
    integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda
    Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da
    Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da
    Constituição Federal, com a redação dada pela Emenda Constitucional nº
    103/2019 - regra transitória - idade + tempo de contribuição + homem.
  visivel_dtc_integral: N
  sexo: MASCULINO
  integral: S
  tipo_calculo: Remuneração de Contribuição
  fundamentacao: Artigo 7º, §§1º e 3º da Emenda Constitucional Estadual nº 146/2021
proveniencia:
  fontes_consultadas:
    - https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp51.htm
    - /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
    - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
  notas: >-
    Correção proposta a partir do achado-0017. Duas trocas em relação à
    regra-0078: a alínea citada ("b" -> "a") e o descritor final ("mulher" ->
    "homem"). Nenhum outro campo muda.
decisoes:
  - data: 2026-07-29
    quem: franklinbaldo
    o_que: >-
      Propor a fundamentação com a alínea masculina, sem alterar a regra-0078.
      A unidade fica em `elaboracao`: nada é exportado, e a decisão de corrigir
      o campo deployável é de quem responde pelo produto.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Completar a projeção com as 27 colunas legadas e promover a
      `deployable`. As 26 colunas que não são `fundamentacao_integral` foram
      copiadas verbatim da `regra-0078` e conferidas campo a campo contra ela
      (seção "Projeção deployável, campo a campo"), de modo que a diferença
      entre origem e destino é exatamente uma. Promover a unidade não a põe em
      produção: o conjunto que a carrega segue `proposto` e a exportação
      operacional continua saindo integralmente do bundle legado.
  - data: '2026-07-30'
    quem: franklinbaldo
    o_que: >-
      Registrar a proveniência desta unidade (RFC 0004, round 11): ela
      propunha, sem tocar a regra-0078, a troca da alínea “b” pela “a” da LC
      51/1985 no fundamentacao_integral, defeito do achado-0017. A Decisão 10
      (docs/analysis/decisoes-de-auditoria-2026-07-30.md) autorizou a
      auditoria a alterar FUNDAMENTACAO* diretamente na regra legada, e a
      correção foi aplicada ali — a proposta ficou sem objeto de implantação.
      Esta unidade permanece porque é o documento onde a correção foi escrita
      e conferida contra a fonte; o achado-0010 e a disposição da regra-0078 a
      citam como origem do texto adotado. Antes registrado no Conjunto
      proposta-auditoria-2026-07 (retirado).
confianca: alta
---

# O que esta unidade propõe

A `regra-0078` tem `sexo: MASCULINO` e cita a alínea **"b"** do art. 1º, II da
LC 51/1985 — que exige 25 anos de contribuição e 15 de exercício policial, "se
**mulher**". A alínea masculina é a **"a"**: 30 e 20 anos, "se homem". O texto
da regra ainda termina com o descritor "idade + tempo de contribuição +
**mulher**".

Esta unidade projeta a mesma regra com as duas trocas — a alínea e o
descritor. Nada mais muda: `integral`, `paridade`, `tipo_calculo`, as janelas e
o `nome` são os da origem.

O registro do defeito é o [`achado-0017`](../../regras-sisprev/achados/achado-0017.md).
Esta unidade é a outra metade: o achado diz o que está errado, a unidade diz
qual seria o certo, e as duas coisas ficam separadas de propósito.

# Por que uma regra proposta, e não uma edição na regra

`FUNDAMENTACAO_INTEGRAL` é campo **deployável** — o texto que o Sisprev entrega
no documento do servidor. Editá-lo em `regra-0078` seria alterar o produto sem
que ninguém tivesse decidido alterá-lo, e o catálogo perderia o estado
anterior (a RFC 0006 registra que editar uma regra é destrutivo).

O catálogo auditado existe exatamente para isto: identidade própria, bundle
separado, e a regra legada **intocada em cardinalidade e identidade**.

# Projeção deployável, campo a campo

`estado_proposta: deployable` afirma que a projeção compila fechada — as 27
colunas legadas estão resolvidas, sem pendência, e o compilador as checa
também contra os tipos declarados da coluna de destino. A afirmação que ela
**não** faz é a de estar em produção. São três estados distintos, e só o
terceiro entrega: a unidade compila (`estado_proposta`), o grupo que a carrega
está escrito por inteiro (`estado_grupo: ativo`, com `decisao_completude`), e o
conjunto está em vigor (`situacao`). Este está `proposto`, e `catalogo_vigente`
resolve só o conjunto vigente — nada daqui sai no CSV operacional.

A comparação abaixo é o que a decisão de adotar esta unidade custa, coluna por
coluna. Vinte e seis colunas são a origem verbatim; uma difere.

| coluna                   | `regra-0078`          | esta unidade         |
| ------------------------ | --------------------- | -------------------- |
| `fundamentacao_integral` | alínea "b" / "mulher" | alínea "a" / "homem" |
| as outras 26             | —                     | idênticas            |

As quatro colunas de data vivem em `aplicabilidade_temporal.datas_legadas`,
nunca em `projecao` — é o único lugar onde podem ser declaradas, e os valores
são os da origem. As duas colunas que a origem tem vazias (`tipo_remun`,
`fundamentacao_proporcional`) são declaradas explicitamente vazias, para que a
projeção nomeie as 27 e "não declarada" nunca se confunda com "vazia na
origem".

`dispositivos:` não é coluna do CSV: o compilador o monta a partir de
`taxonomias`, e é aí que a troca de alínea aparece pela segunda vez — a
unidade vincula `art-1-inc-ii-al-a`, a origem vincula `al-b`.

# O que esta unidade não faz

- **Não altera a `regra-0079`.** A gêmea feminina cita a alínea "b"
  corretamente; o defeito não é dela.
- **Não toca a `regra-0084`.** Ela é `sexo: AMBOS` e o § 2º do art. 7º remete à
  LC 51 sem fixar tempo — o caso pede as **duas** alíneas, e provavelmente uma
  decomposição, não uma troca de letra. Fica para unidade própria.
- **Não afirma o que o motor faz.** `regra-0078` é `simulavel: S`, e nessa
  condição o motor não lê a fundamentação: tempo de contribuição e tempo de
  exercício policial não têm coluna. A correção é do documento entregue.
- **Não põe a correção em produção.** O conjunto que carrega o grupo é
  `proposto`, e a exportação operacional segue 100% do bundle legado. Adotar a
  correção é ato de quem responde pelo produto, registrado na disposição do
  `achado-0017` na `regra-0078`.
- **Não corrige o `nome`.** Ele é copiado verbatim, colisão de
  `P1_NOME_REPETIDO` com a `regra-0079` incluída — o `nome` é problema próprio,
  registrado no [`achado-0020`](../../regras-sisprev/achados/achado-0020.md), e
  resolvê-lo aqui de passagem alteraria também a gêmea, que este grupo não
  alcança.

# Conferência da fonte

O texto das duas alíneas foi conferido **contra a publicação oficial arquivada**,
não apenas contra os dispositivos autorados. A LC 51/1985 está em
`fontes-oficiais/arquivos/planalto-lcp51.htm`, com `sha256` no manifesto, e cada
parágrafo de `lc-51-1985/art-1-inc-ii-al-a/lc-144-2014` e de `.../al-b/...` foi
comparado literalmente com ela: o inciso II e as duas alíneas casam verbatim,
inclusive a nota "(Incluído pela Lei Complementar n° 144, de 2014)". A única
divergência aparente é no caput, e é artefato de leitura: o Planalto marca o
ordinal em `<sup>`, de modo que remover as tags produz "Art. 1 o" onde o
dispositivo grava "Art. 1o".

**Uma versão anterior desta seção afirmava que a fonte não pôde ser aberta**
(HTTP 000) e que a LC 51/1985 era o primeiro item da fila de pendências. As duas
coisas deixaram de ser verdade e o texto não acompanhou. O que causava o HTTP 000
era o **filtro de User-Agent do Planalto** sobre o `curl` padrão, diagnosticado e
corrigido em `scripts/arquivo_de_fontes.py`; o
[`PENDENCIAS.md`](../../../fontes-oficiais/PENDENCIAS.md) registra o episódio
inteiro e o estado sem faltantes. A conferência do piloto passa portanto a
apoiar-se na fonte primária arquivada, que é o padrão que o repositório já
exigia.
