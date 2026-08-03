---
type: RegraProposta
id: invalidez-ec20-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0004
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-ec20-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença catalogada na norma aplicável
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir as classes qualificadas e enquadrar o
        caso no ramo residual proporcional?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e rol legal vigente
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e investigação suficiente das causas
        qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 16/12/1998 00:00
    data_direito_ate: 31/12/2003 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    papel: determina proventos proporcionais nos demais casos
  - ref: /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    papel: fixa a base na totalidade da remuneração do cargo efetivo
  - ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    papel: assegura paridade
projecao:
  nome: Invalidez · EC 20/1998 · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Não identificado
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    - /formas-calculo/forma-calculo-totalidade-proporcional-tempo.md
    - EC 41/2003, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data do direito: LC 68/1992 ou LC 228/2000
  notas: >-
    O enum legado não representa fielmente totalidade da remuneração
    proporcional ao tempo; ausência de informação não equivale a causa comum.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: Decompor a regra-0004 por classe de causa e resultado.
confianca: media
---

# Síntese

Hipótese residual proporcional sob EC 20/1998. A fórmula jurídica é conhecida,
mas a projeção fiel ainda exige forma de cálculo parametrizável no Sisprev.

# Pendências localizadas

- confirmar os parâmetros estaduais da proporcionalidade;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
