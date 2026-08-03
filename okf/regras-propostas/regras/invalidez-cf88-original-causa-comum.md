---
type: RegraProposta
id: invalidez-cf88-original-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-direito-adquirido
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
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: determina proventos proporcionais nos demais casos
projecao:
  nome: Invalidez · CF/88 original · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontra em estado de invalidez
    permanente, tendo sido igualmente demonstrado que essa invalidez não decorreu de
    acidente em serviço, de moléstia profissional nem de doença grave, contagiosa ou
    incurável especificada em lei; a incapacidade permanente e o afastamento de
    todas as causas qualificadas foram apurados por junta médica oficial e pela
    instrução previdenciária do IPERON, mediante
    laudo médico oficial, prontuários, histórico ocupacional, apuração de eventual
    acidente e o rol legal vigente, tendo sido exigidas conclusão médica de
    incapacidade permanente e investigação suficiente das causas qualificadas — o
    silêncio ou a prova insuficiente não bastam para enquadrar o caso neste ramo.
    Ficou também demonstrado que o direito foi implementado antes de 16/12/1998,
    data em que entrou em vigor a Emenda Constitucional nº 20/1998, de modo que a
    concessão se rege pelo texto original do art. 40 da Constituição Federal, por
    direito adquirido.

    Todos esses requisitos se extraem do art. 40, inciso I, da Constituição Federal
    em seu texto original, que determina a aposentadoria do servidor por invalidez
    permanente e, no mesmo inciso, distingue os ramos do cálculo: reserva os
    proventos integrais às invalidezes decorrentes de acidente em serviço, moléstia
    profissional ou doença grave, contagiosa ou incurável especificada em lei, e
    atribui proventos proporcionais nos demais casos. O ramo aqui aplicado é
    residual por construção do próprio dispositivo — ele se define pela exclusão das
    três hipóteses qualificadas, e é por isso que a demonstração de que nenhuma
    delas ocorreu integra os requisitos da regra.

    Do enquadramento nas demais causas resulta o cálculo dos proventos sobre a
    remuneração do cargo efetivo em que se deu a aposentadoria, reduzida na
    proporção do tempo de serviço, e com paridade em relação aos servidores em
    atividade. O fundamento desse cálculo é o próprio art. 40, inciso I, da
    Constituição Federal em sua redação original, na parte final em que atribui
    proventos proporcionais aos casos não qualificados.
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    O ramo residual exige exclusão probatória das causas qualificadas; ausência
    de informação não equivale a causa comum. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir a regra proporcional legada por unidade com fundamento e
      protocolo próprios.
confianca: media
---

# Síntese

Hipótese residual de invalidez proporcional sob CF/88 original. O rótulo
`Não identificado` preserva a falta de projeção fiel da fórmula no enum legado,
não desconhecimento do ramo jurídico.

# Pendências localizadas

- fechar a fórmula estadual aplicável em cada trecho da janela;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
