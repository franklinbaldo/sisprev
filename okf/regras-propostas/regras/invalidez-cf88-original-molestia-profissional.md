---
type: RegraProposta
id: invalidez-cf88-original-molestia-profissional
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: molestia_profissional
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de moléstia profissional, com nexo
      ocupacional reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e ocupacional demonstra incapacidade permanente e nexo
        entre a moléstia e o trabalho?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, histórico ocupacional, prontuários, laudo
        ambiental e assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        conclusão médica de incapacidade permanente e prova suficiente do nexo
        ocupacional
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define as classes de causa e os ramos integral e proporcional
projecao:
  nome: Invalidez · CF/88 original · moléstia profissional · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    A legislação estadual é apurada na versão vigente na data do direito;
    mudança apenas de fonte não cria outra regra. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa, com uma
      hipótese material por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por moléstia profissional. A seleção
exige prova positiva do nexo ocupacional.

# Pendências localizadas

- transcrever os dispositivos estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
