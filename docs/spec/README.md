# Especificações do projeto

Este diretório contém os contratos semânticos vigentes. Quando documentos
históricos de `docs/analysis/`, achados antigos, comentários de PR ou trechos de
RFC registrarem hipótese anterior, prevalece a decisão mais recente nesta pasta.

## `type: Regra`

A leitura deve ser feita nesta ordem:

1. [`decisoes-semanticas-regra.md`](decisoes-semanticas-regra.md) — decisões da
   coordenação consolidadas em 2026-08-01 sobre ramos integral/proporcional,
   `INTEGRAL`, `TIPO_CALCULO`, `DATA_DIREITO_APOS` e `DATA_ADM_APOS`;
2. [`regra.md`](regra.md) — contrato geral do tipo, estrutura, estados e demais
   questões Q1–Q12.

Em caso de divergência entre os dois documentos nos temas enumerados no item 1,
`decisoes-semanticas-regra.md` prevalece até que a consolidação seja incorporada
integralmente ao contrato geral.

## Regra contra regressão documental

Os seguintes pontos não são perguntas abertas da auditoria:

- o catálogo auditado usa **um ramo por regra**;
- `integral: S` significa ausência de proporcionalização pelo tempo de
  contribuição;
- `tipo_calculo` referencia uma `FormaCalculo`, e novas formas ou nomes podem
  ser parametrizados;
- `DATA_DIREITO_APOS` é inclusivo e se refere à implementação de todos os
  requisitos; e
- `DATA_ADM_APOS` é inclusivo e se refere ao ingresso no serviço público, com a
  posse como marco do cargo efetivo.

Reabrir qualquer desses pontos exige proposta expressa de revisão, evidência nova
e identificação dos documentos e conclusões afetados.
