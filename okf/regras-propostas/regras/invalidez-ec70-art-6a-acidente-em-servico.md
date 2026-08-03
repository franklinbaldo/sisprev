---
type: RegraProposta
id: invalidez-ec70-art-6a-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0008
predicados:
  causa_incapacidade: acidente_em_servico
  regime: ec70-art-6a-preservado-art-4-ece146
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
        incapacidade permanente comprovada e ato ou conjunto probatório que
        reconheça o nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: é o fundamento de invalidez exigido pelo art. 6º-A
  - ref: /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
    papel: fixa ingresso, remuneração do cargo e paridade
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-20-par-6/original.md
    papel: define acidente em serviço no período da LCE 432/2008
projecao:
  nome: >-
    Invalidez · EC 70/2012 · art. 6º-A · acidente em serviço · integral ·
    paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente decorre de acidente em serviço,
    com nexo causal reconhecido; a verificação foi realizada por junta médica oficial e instrução
    previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente,
    prontuários e assentamentos funcionais, tendo sido exigida a seguinte evidência: incapacidade
    permanente comprovada e ato ou conjunto probatório que reconheça o nexo com o serviço.
    Ficou também demonstrado que os requisitos foram implementados em 31/12/2003 ou depois,
    mas antes de 01/01/2025 e que o ingresso no serviço público ocorreu até 31/12/2003, inclusive.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 41/2003 é o fundamento de invalidez
    exigido pelo art. 6º-A. art. 6, da Emenda Constitucional nº 41/2003 fixa ingresso, remuneração
    do cargo e paridade. art. 4, da Emenda à Constituição do Estado nº 146/2021 preserva os
    requisitos anteriores se implementados até 31/12/2024. art. 20, § 6º, da Lei Complementar
    Estadual nº 432/2008 define acidente em serviço no período da LCE 432/2008.


    O cálculo inicial segue a forma “Remuneração integral do cargo efetivo na invalidez qualificada
    da LC 228/2000”, vinculada a esta regra e sustentada pelos dispositivos articulados acima.
    O resultado não sofre redução proporcional ao tempo. Após a concessão, os proventos são
    revistos com paridade, segundo o dispositivo específico articulado acima. Eventual parâmetro
    ainda indicado como pendente na forma de cálculo ou no corpo da regra não é antecipado
    por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-remuneracao-cargo-integral-lc228.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/lce-432-2008/art-20-par-6/original.md
    - LC 228/2000, texto oficial do SAPL — regime estadual anterior à LCE 432/2008
  notas: >-
    A hipótese usa a remuneração do cargo efetivo, sem proporcionalização, e
    paridade. O enum legado correspondente ainda não está comprovado. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o art. 6º-A por classe de causa e ramo de resultado.
confianca: media
---

# Síntese

Hipótese do art. 6º-A por acidente em serviço: remuneração do cargo efetivo,
sem proporcionalização e com paridade.

A fronteira superior exclusiva em 01/01/2025 inclui o último dia permitido,
31/12/2024.

# Pendências localizadas

- transcrever e versionar os dispositivos estaduais anteriores à LCE 432/2008;
- confirmar qual enum projeta a remuneração do cargo efetivo;
- resolver Q6-S/Q6-T quanto à classificação operacional da causa;
- completar o gate humano e a decisão institucional de completude.
