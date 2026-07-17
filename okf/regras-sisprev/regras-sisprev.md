---
type: Dataset
title: Regras do Sisprev — Regime Próprio de Previdência (RO)
description: Catálogo de regras de aposentadoria e pensão por morte do Sisprev, com
  fundamentação legal, elegibilidade e forma de cálculo.
tags:
- previdencia
- aposentadoria
- pensao
- sisprev
- rondonia
source_file: data/raw/regras-sisprev.csv
row_count: 112
columns:
- NOME
- TIPO DE BENEFICIO
- ATUALMENTE NO SISTEMA
- CICLO DE VALIDAÇÃO
- VALIDADO PGE
- VALIDADO PRESIDENCIA
- SIMULAVEL
- TIPO
- APOS_ESPECIAL
- TIPO_REMUN
- PARIDADE
- TabelaPontuacao
- Requisitos da IN Nº 5/2020
- Relatório p/ Reserva Remunerada por Idade ex-officio
- ADICIONAL_INATIVIDADE
- DATA_ADM_ATE
- DATA_ADM_APOS
- DATA_DIREITO_ATE
- DATA_DIREITO_APOS
- FUNDAMENTACAO_PROPORCIONAL
- VISIVEL DTC PROPORCIONAL
- FUNDAMENTACAO_INTEGRAL
- VISIVEL DTC INTEGRAL
- SEXO
- INTEGRAL
- TIPO_CALCULO
- FUNDAMENTACAO
---

Catálogo de regras de aposentadoria e pensão por morte do Sisprev, com fundamentação legal, elegibilidade e forma de cálculo.

# Schema

| Coluna | Tipo | Descrição |
|---|---|---|
| `NOME` | string | Nome da regra de aposentadoria/pensão. |
| `TIPO DE BENEFICIO` | string (enum) | Categoria do benefício (ex.: APOSENTADORIA POR INVALIDEZ, PENSÃO POR MORTE). |
| `ATUALMENTE NO SISTEMA` | TRUE/FALSE | Se a regra está atualmente implementada no Sisprev. |
| `CICLO DE VALIDAÇÃO` | string (1º-4º) | Ciclo de validação jurídica da regra. |
| `VALIDADO PGE` | TRUE/FALSE | Se a regra foi validada pela Procuradoria-Geral do Estado. |
| `VALIDADO PRESIDENCIA` | TRUE/FALSE | Se a regra foi validada pela Presidência do órgão previdenciário. |
| `SIMULAVEL` | S/N | Se a regra pode ser usada em simulações de aposentadoria. |
| `TIPO` | string | Categoria do servidor (ex.: CIVIL). |
| `APOS_ESPECIAL` | S/N | Se é uma aposentadoria especial (ex.: magistério, policial, exposição a agentes nocivos). |
| `TIPO_REMUN` | string | Tipo de remuneração aplicável, quando preenchido. |
| `PARIDADE` | S/N | Se os proventos têm paridade com a remuneração da ativa. |
| `TabelaPontuacao` | S/N | Se a regra usa tabela de pontuação (idade + tempo de contribuição). |
| `Requisitos da IN Nº 5/2020` | S/N | Se a regra segue os requisitos da Instrução Normativa nº 5/2020. |
| `Relatório p/ Reserva Remunerada por Idade ex-officio` | S/N | Se a regra gera relatório de reserva remunerada por idade de ofício. |
| `ADICIONAL_INATIVIDADE` | S/N | Se há adicional de inatividade aplicável. |
| `DATA_ADM_ATE` | datetime (DD/MM/AAAA HH:MM) | Data-limite superior de admissão para a regra se aplicar. |
| `DATA_ADM_APOS` | datetime (DD/MM/AAAA HH:MM) | Data-limite inferior de admissão para a regra se aplicar. |
| `DATA_DIREITO_ATE` | datetime (DD/MM/AAAA HH:MM) | Data-limite superior de aquisição do direito. |
| `DATA_DIREITO_APOS` | datetime (DD/MM/AAAA HH:MM) | Data-limite inferior de aquisição do direito. |
| `FUNDAMENTACAO_PROPORCIONAL` | text | Fundamentação legal do cálculo proporcional (corpo do documento da regra). |
| `VISIVEL DTC PROPORCIONAL` | S/N | Se a fundamentação proporcional é visível na Declaração de Tempo de Contribuição (DTC). |
| `FUNDAMENTACAO_INTEGRAL` | text | Fundamentação legal do cálculo integral (corpo do documento da regra). |
| `VISIVEL DTC INTEGRAL` | S/N | Se a fundamentação integral é visível na DTC. |
| `SEXO` | string (enum) | Sexo a que a regra se aplica: MASCULINO, FEMININO, AMBOS ou vazio. |
| `INTEGRAL` | S/N | Se os proventos são integrais. |
| `TIPO_CALCULO` | string (enum) | Método de cálculo dos proventos (ex.: Valor Efetivo, Valor Médio, Remuneração de Contribuição, Proporcionalidade Dias). |
| `FUNDAMENTACAO` | text | Fundamentação legal geral/adicional (corpo do documento da regra). |

# Regras

Uma regra por linha da planilha original — ver [regras/](regras/index.md).
