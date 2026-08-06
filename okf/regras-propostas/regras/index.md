# Regras propostas

Toda `RegraProposta` do repositório, agrupada por `ciclo` — o lote temático
que a autora e é dono do fechamento dela (`okf/spec/ciclo.md`). Campos do
schema atual, sem sinônimo:

- **`estado_auditoria`** (`elaboracao` / `preview` / `concluida`) — a
  maturidade da derivação jurídica: `concluida` afirma que a fórmula que a
  lei exige está determinada e representada, nada além disso.
- **`estado_implantacao`** (`confirmada` / `confirmada_com_ressalva` /
  `pendente_mapeamento_sisprev`) —
  eixo independente: se o valor de domínio fechado projetado para o Sisprev
  já é reconhecido pelo sistema sem ambiguidade
  (`okf/spec/regraproposta.md`). Uma unidade `concluida` com implantação
  pendente não é `preview`.
- **origens legadas** (`origens_legacy`) — as linhas do catálogo legado de
  que a unidade descende. Não há campo de grupo declarado à parte: quando
  duas ou mais unidades do mesmo ciclo compartilham, direta ou
  transitivamente, uma origem, elas formam um **componente de implantação**
  — a unidade atômica que precisa entrar junta na carga do Sisprev,
  calculada por `scripts/derivar.py` a partir do grafo origem↔destino
  (`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada").
  Só entra em `data/regras-propostas.csv` o componente cujos membros têm
  todos `estado_auditoria: concluida` **e** `estado_implantacao: confirmada`.
- **tipo_calculo (projeção legada)** — o valor que `projecao.tipo_calculo`
  grava para o Sisprev, mostrado abaixo por conveniência de leitura. Não é
  a identidade da fórmula: o **tipo de cálculo canônico** — base, ajustes,
  limitadores e fundamentação normativa — está em `okf/tipos-calculo/` e é
  referenciado em `proveniencia.fontes_consultadas` de cada unidade
  (`okf/spec/tipocalculo.md`).

### ciclo-01

| unidade                                                                                                                                                                 | origens legadas | tipo_calculo (projeção legada) | estado_auditoria | estado_implantacao        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------ | ---------------- | ------------------------- |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-acidente-em-servico`](incapacidade-lce1100-2004-ate-2018-sem-rpc-acidente-em-servico.md)                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-causa-comum`](incapacidade-lce1100-2004-ate-2018-sem-rpc-causa-comum.md)                                                   | `regra-0021`    | `Proporcionalidade Dias`       | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-alienacao-mental`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-alienacao-mental.md)                           | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-anomalia-da-fala-magisterio`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-anomalia-da-fala-magisterio.md)     | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-cardiopatia-grave`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-cardiopatia-grave.md)                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-cegueira-bilateral`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-cegueira-bilateral.md)                       | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-contaminacao-por-radiacao`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-contaminacao-por-radiacao.md)         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-doenca-de-paget`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-doenca-de-paget.md)                             | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-doenca-de-parkinson`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-doenca-de-parkinson.md)                     | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-esclerose-multipla`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-esclerose-multipla.md)                       | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-espondiloartrose-anquilosante`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-espondiloartrose-anquilosante.md) | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-hanseniase`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-hanseniase.md)                                       | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-hepatopatia-grave`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-hepatopatia-grave.md)                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-nefropatia-grave`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-nefropatia-grave.md)                           | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-neoplasia-maligna`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-neoplasia-maligna.md)                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-paralisia-irreversivel`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-paralisia-irreversivel.md)               | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-sida-aids`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-sida-aids.md)                                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-surdez-permanente-magisterio`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-surdez-permanente-magisterio.md)   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-tuberculose-ativa`](incapacidade-lce1100-2004-ate-2018-sem-rpc-doenca-tuberculose-ativa.md)                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-2004-ate-2018-sem-rpc-molestia-profissional`](incapacidade-lce1100-2004-ate-2018-sem-rpc-molestia-profissional.md)                               | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-apos-2018-ou-rpc-acidente-em-servico`](incapacidade-lce1100-apos-2018-ou-rpc-acidente-em-servico.md)                                             | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-causa-comum`](incapacidade-lce1100-apos-2018-ou-rpc-causa-comum.md)                                                             | `regra-0021`    | `Proporcionalidade Dias`       | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-alienacao-mental`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-alienacao-mental.md)                                     | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-anomalia-da-fala-magisterio`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-anomalia-da-fala-magisterio.md)               | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-cardiopatia-grave`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-cardiopatia-grave.md)                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-cegueira-bilateral`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-cegueira-bilateral.md)                                 | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-contaminacao-por-radiacao`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-contaminacao-por-radiacao.md)                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-doenca-de-paget`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-doenca-de-paget.md)                                       | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-doenca-de-parkinson`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-doenca-de-parkinson.md)                               | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-esclerose-multipla`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-esclerose-multipla.md)                                 | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-espondiloartrose-anquilosante`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-espondiloartrose-anquilosante.md)           | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-hanseniase`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-hanseniase.md)                                                 | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-hepatopatia-grave`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-hepatopatia-grave.md)                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-nefropatia-grave`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-nefropatia-grave.md)                                     | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-neoplasia-maligna`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-neoplasia-maligna.md)                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-paralisia-irreversivel`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-paralisia-irreversivel.md)                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-sida-aids`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-sida-aids.md)                                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-surdez-permanente-magisterio`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-surdez-permanente-magisterio.md)             | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-doenca-tuberculose-ativa`](incapacidade-lce1100-apos-2018-ou-rpc-doenca-tuberculose-ativa.md)                                   | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-apos-2018-ou-rpc-molestia-profissional`](incapacidade-lce1100-apos-2018-ou-rpc-molestia-profissional.md)                                         | `regra-0022`    | `Valor Médio`                  | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-ate-2003-sem-rpc-acidente-em-servico`](incapacidade-lce1100-ate-2003-sem-rpc-acidente-em-servico.md)                                             | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-causa-comum`](incapacidade-lce1100-ate-2003-sem-rpc-causa-comum.md)                                                             | `regra-0020`    | `Proporcionalidade Dias`       | `concluida`      | `confirmada_com_ressalva` |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-alienacao-mental`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-alienacao-mental.md)                                     | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-anomalia-da-fala-magisterio`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-anomalia-da-fala-magisterio.md)               | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-cardiopatia-grave`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-cardiopatia-grave.md)                                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-cegueira-bilateral`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-cegueira-bilateral.md)                                 | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-contaminacao-por-radiacao`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-contaminacao-por-radiacao.md)                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-doenca-de-paget`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-doenca-de-paget.md)                                       | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-doenca-de-parkinson`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-doenca-de-parkinson.md)                               | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-esclerose-multipla`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-esclerose-multipla.md)                                 | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-espondiloartrose-anquilosante`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-espondiloartrose-anquilosante.md)           | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-hanseniase`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-hanseniase.md)                                                 | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-hepatopatia-grave`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-hepatopatia-grave.md)                                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-nefropatia-grave`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-nefropatia-grave.md)                                     | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-neoplasia-maligna`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-neoplasia-maligna.md)                                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-paralisia-irreversivel`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-paralisia-irreversivel.md)                         | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-sida-aids`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-sida-aids.md)                                                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-surdez-permanente-magisterio`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-surdez-permanente-magisterio.md)             | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-doenca-tuberculose-ativa`](incapacidade-lce1100-ate-2003-sem-rpc-doenca-tuberculose-ativa.md)                                   | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |
| [`incapacidade-lce1100-ate-2003-sem-rpc-molestia-profissional`](incapacidade-lce1100-ate-2003-sem-rpc-molestia-profissional.md)                                         | `regra-0019`    | `Valor Efetivo`                | `concluida`      | `confirmada`              |

### ciclo-05

| unidade                                                                                         | origens legadas | tipo_calculo (projeção legada) | estado_auditoria | estado_implantacao |
| ----------------------------------------------------------------------------------------------- | --------------- | ------------------------------ | ---------------- | ------------------ |
| [`servidor-com-deficiencia-grave-feminino`](servidor-com-deficiencia-grave-feminino.md)         | `regra-0061`    | `—`                            | `elaboracao`     | `confirmada`       |
| [`servidor-com-deficiencia-grave-masculino`](servidor-com-deficiencia-grave-masculino.md)       | `regra-0062`    | `—`                            | `elaboracao`     | `confirmada`       |
| [`servidor-com-deficiencia-leve-feminino`](servidor-com-deficiencia-leve-feminino.md)           | `regra-0063`    | `—`                            | `elaboracao`     | `confirmada`       |
| [`servidor-com-deficiencia-leve-masculino`](servidor-com-deficiencia-leve-masculino.md)         | `regra-0064`    | `—`                            | `elaboracao`     | `confirmada`       |
| [`servidor-com-deficiencia-moderada-feminino`](servidor-com-deficiencia-moderada-feminino.md)   | `regra-0059`    | `—`                            | `elaboracao`     | `confirmada`       |
| [`servidor-com-deficiencia-moderada-masculino`](servidor-com-deficiencia-moderada-masculino.md) | `regra-0060`    | `—`                            | `elaboracao`     | `confirmada`       |

### ciclo-06

| unidade                                                                                                     | origens legadas                          | tipo_calculo (projeção legada) | estado_auditoria | estado_implantacao |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------ | ---------------- | ------------------ |
| [`agentes-nocivos-art-41-i-integralidade-paridade`](agentes-nocivos-art-41-i-integralidade-paridade.md)     | `regra-0065`, `regra-0066`, `regra-0067` | `Valor Efetivo`                | `preview`        | `confirmada`       |
| [`agentes-nocivos-art-41-i-media-sem-paridade`](agentes-nocivos-art-41-i-media-sem-paridade.md)             | `regra-0071`                             | `Valor Médio`                  | `concluida`      | `confirmada`       |
| [`agentes-nocivos-art-41-ii-integralidade-paridade`](agentes-nocivos-art-41-ii-integralidade-paridade.md)   | `regra-0065`, `regra-0066`, `regra-0067` | `Valor Efetivo`                | `preview`        | `confirmada`       |
| [`agentes-nocivos-art-41-ii-media-sem-paridade`](agentes-nocivos-art-41-ii-media-sem-paridade.md)           | `regra-0071`                             | `Valor Médio`                  | `concluida`      | `confirmada`       |
| [`agentes-nocivos-art-41-iii-integralidade-paridade`](agentes-nocivos-art-41-iii-integralidade-paridade.md) | `regra-0065`, `regra-0066`, `regra-0067` | `Valor Efetivo`                | `preview`        | `confirmada`       |
| [`agentes-nocivos-art-41-iii-media-sem-paridade`](agentes-nocivos-art-41-iii-media-sem-paridade.md)         | `regra-0071`                             | `Valor Médio`                  | `concluida`      | `confirmada`       |
| [`agentes-nocivos-ece-146-2021`](agentes-nocivos-ece-146-2021.md)                                           | `regra-0068`, `regra-0069`, `regra-0070` | `Valor Médio`                  | `preview`        | `confirmada`       |

### ciclo-08

| unidade                                                                         | origens legadas | tipo_calculo (projeção legada) | estado_auditoria | estado_implantacao |
| ------------------------------------------------------------------------------- | --------------- | ------------------------------ | ---------------- | ------------------ |
| [`policial-civil-voluntaria-masculino`](policial-civil-voluntaria-masculino.md) | `regra-0078`    | `Remuneração de Contribuição`  | `concluida`      | `confirmada`       |

### ciclo-09

| unidade                                                                                                           | origens legadas            | tipo_calculo (projeção legada) | estado_auditoria | estado_implantacao |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------ | ---------------- | ------------------ |
| [`invalidez-cf88-original-acidente-em-servico`](invalidez-cf88-original-acidente-em-servico.md)                   | `regra-0001`, `regra-0002` | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-cf88-original-causa-comum`](invalidez-cf88-original-causa-comum.md)                                   | `regra-0001`, `regra-0002` | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-cf88-original-doenca-catalogada`](invalidez-cf88-original-doenca-catalogada.md)                       | `regra-0001`, `regra-0002` | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-cf88-original-molestia-profissional`](invalidez-cf88-original-molestia-profissional.md)               | `regra-0001`, `regra-0002` | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec20-acidente-em-servico`](invalidez-ec20-acidente-em-servico.md)                                     | `regra-0004`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec20-causa-comum`](invalidez-ec20-causa-comum.md)                                                     | `regra-0004`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec20-doenca-catalogada`](invalidez-ec20-doenca-catalogada.md)                                         | `regra-0004`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec20-molestia-profissional`](invalidez-ec20-molestia-profissional.md)                                 | `regra-0004`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-acidente-em-servico`](invalidez-ec41-geral-acidente-em-servico.md)                         | `regra-0006`               | `Valor Médio`                  | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-causa-comum`](invalidez-ec41-geral-causa-comum.md)                                         | `regra-0007`               | `Proporcionalidade Dias`       | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-doenca-catalogada`](invalidez-ec41-geral-doenca-catalogada.md)                             | `regra-0006`               | `Valor Médio`                  | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-media-lc228-causa-comum`](invalidez-ec41-geral-media-lc228-causa-comum.md)                 | `regra-0007`               | `Valor Médio`                  | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-molestia-profissional`](invalidez-ec41-geral-molestia-profissional.md)                     | `regra-0006`               | `Valor Médio`                  | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-pre-mp167-acidente-em-servico`](invalidez-ec41-geral-pre-mp167-acidente-em-servico.md)     | `regra-0006`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-pre-mp167-causa-comum`](invalidez-ec41-geral-pre-mp167-causa-comum.md)                     | `regra-0007`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-pre-mp167-doenca-catalogada`](invalidez-ec41-geral-pre-mp167-doenca-catalogada.md)         | `regra-0006`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec41-geral-pre-mp167-molestia-profissional`](invalidez-ec41-geral-pre-mp167-molestia-profissional.md) | `regra-0006`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec70-art-6a-acidente-em-servico`](invalidez-ec70-art-6a-acidente-em-servico.md)                       | `regra-0008`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec70-art-6a-causa-comum`](invalidez-ec70-art-6a-causa-comum.md)                                       | `regra-0009`               | `Proporcionalidade Dias`       | `elaboracao`     | `confirmada`       |
| [`invalidez-ec70-art-6a-doenca-catalogada`](invalidez-ec70-art-6a-doenca-catalogada.md)                           | `regra-0008`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec70-art-6a-lc228-causa-comum`](invalidez-ec70-art-6a-lc228-causa-comum.md)                           | `regra-0009`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
| [`invalidez-ec70-art-6a-molestia-profissional`](invalidez-ec70-art-6a-molestia-profissional.md)                   | `regra-0008`               | `Valor Efetivo`                | `elaboracao`     | `confirmada`       |
