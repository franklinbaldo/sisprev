---
type: RegraProposta
id: invalidez-cf88-original-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: acidente_em_servico
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de acidente em serviço, com nexo causal
      reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente e
        nexo causal com acidente em serviço?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, comunicação e apuração do acidente, prontuários e
        assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        conclusão médica de incapacidade permanente e ato ou conjunto
        probatório que reconheça o nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define as classes de causa e os ramos integral e proporcional
projecao:
  nome: Invalidez · CF/88 original · acidente em serviço · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    A legislação estadual e o rol de doenças são apurados na versão vigente na
    data de implementação dos requisitos. A mudança de diploma, sem alteração
    demonstrada de critério ou efeito, não cria por si só outra regra. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa, com uma
      hipótese material por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por acidente em serviço. A seleção
exige prova positiva da causa; ausência de informação não autoriza enquadramento
em `causa_comum`.

# Pendências localizadas

- transcrever os dispositivos estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
