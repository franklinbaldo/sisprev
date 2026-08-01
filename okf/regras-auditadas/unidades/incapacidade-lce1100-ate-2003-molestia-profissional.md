---
type: UnidadeAuditada
id: incapacidade-lce1100-ate-2003-molestia-profissional
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0019
predicados:
  causa_incapacidade: molestia_profissional
  regime: lce1100-incapacidade-ingresso-ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de moléstia profissional, com nexo
      ocupacional reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente,
        impossibilidade de readaptação e nexo entre a doença e o trabalho?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, histórico ocupacional, prontuários, exames e
        apuração administrativa do nexo
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente e conclusão fundamentada sobre o nexo
        profissional
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: inclui moléstia profissional entre as causas qualificadas
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: remete as causas qualificadas à média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: assegura paridade à coorte de ingresso até 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso até 2003 · moléstia
    profissional · média integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O § 13 remete ao art. 24 e o art. 27, I, mantém paridade. Moléstia
    profissional é classe jurídica própria e exige aferição humana do nexo.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Individualizar a moléstia profissional e aplicar a fórmula especial do §
      13 sem confundi-la com a regra geral do art. 25.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado até 31/12/2003, com
incapacidade decorrente de moléstia profissional. Aplica-se a média do art. 24,
sem proporcionalização, com paridade do art. 27, I.

# Pendências localizadas

- definir o protocolo institucional de reconhecimento do nexo profissional;
- confirmar a projeção operacional da média com paridade no Sisprev;
- resolver Q6-S/Q6-T e completar o gate humano.
