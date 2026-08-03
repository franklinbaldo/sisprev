---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0019
predicados:
  causa_incapacidade: acidente_em_servico
  regime: lce1100-incapacidade-ingresso-ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de acidente em serviço, com nexo causal
      reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente,
        impossibilidade de readaptação e nexo causal com acidente em serviço?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, comunicação e apuração do acidente, prontuários e
        assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e ato ou conjunto probatório que
        reconheça o nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: separa causas qualificadas e causa comum
  - ref: /dispositivos/lce-1100-2021/art-30-par-5/original.md
    papel: define acidente em serviço
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: remete as causas qualificadas à média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: assegura paridade à coorte de ingresso até 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso até 2003 · acidente em
    serviço · média integral · paridade
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
    - /dispositivos/lce-1100-2021/art-30-par-5/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O § 13 é regra especial da incapacidade e remete ao art. 24. O art. 25 não
    substitui essa remissão apenas pelo ingresso até 2003; outra fórmula depende
    de direito adquirido sob regime anterior. O art. 27, I, mantém a paridade.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Aplicar a fórmula especial do § 13 separadamente do regime de reajuste do
      art. 27, I.
confianca: media
---

# Síntese

Hipótese permanente da LCE 1.100/2021 para servidor ingressado até 31/12/2003,
com incapacidade decorrente de acidente em serviço. Os proventos correspondem à
média do art. 24 sem proporcionalização pelo tempo e são reajustados com
paridade.

A janela começa em 18/10/2021, data de publicação e vigência da lei. A seleção
exige prova positiva do nexo; falta de informação não autoriza causa comum.

# Pendências localizadas

- confirmar a projeção operacional da média com paridade no Sisprev;
- resolver Q6-S/Q6-T quanto à obtenção e classificação da causa;
- completar o gate humano e a decisão institucional de completude.
