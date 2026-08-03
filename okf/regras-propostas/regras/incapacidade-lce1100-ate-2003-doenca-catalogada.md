---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0019
predicados:
  causa_incapacidade: doenca_catalogada
  regime: lce1100-incapacidade-ingresso-ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol legal aplicável
    protocolo_verificacao:
      pergunta: >-
        A doença incapacitante consta do rol legal vigente e está comprovada
        pela perícia oficial?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, exames, prontuários e texto vigente do rol legal
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente, diagnóstico confirmado e correspondência com
        o rol legal
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
  versao_rol: lce-1100-2021-vigente-na-data-do-direito
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: inclui doença grave entre as causas qualificadas
  - ref: /dispositivos/lce-1100-2021/art-30-par-8/original.md
    papel: contém o rol legal de doenças
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: remete as causas qualificadas à média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: assegura paridade à coorte de ingresso até 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso até 2003 · doença
    catalogada · média integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente decorria de doença grave, contagiosa
    ou incurável incluída no rol legal aplicável; a verificação foi realizada por junta médica
    oficial e instrução previdenciária do IPERON, mediante laudo médico oficial, exames, prontuários
    e texto vigente do rol legal, tendo sido exigida a seguinte evidência: incapacidade permanente,
    diagnóstico confirmado e correspondência com o rol legal. Ficou também demonstrado que
    os requisitos foram implementados em 18/10/2021 ou depois e que o ingresso no serviço
    público ocorreu até 31/12/2003, inclusive.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. O art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 103/2019 funda a aposentadoria
    por incapacidade permanente. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021
    inclui doença grave entre as causas qualificadas. O art. 30, § 8º, da Lei Complementar
    Estadual nº 1.100/2021 contém o rol legal de doenças. O art. 30, § 13, da Lei Complementar
    Estadual nº 1.100/2021 remete as causas qualificadas à média do art. 24. O art. 24 da
    Lei Complementar Estadual nº 1.100/2021 disciplina a base média. O art. 27, inciso I,
    da Lei Complementar Estadual nº 1.100/2021 assegura paridade à coorte de ingresso até
    31/12/2003.


    O cálculo inicial segue a forma “Média das 80% maiores remunerações contributivas — LCE
    1.100/2021”, vinculada a esta regra e sustentada pelos dispositivos articulados acima.
    O resultado não sofre redução proporcional ao tempo. Após a concessão, os proventos são
    revistos com paridade, segundo o dispositivo específico articulado acima. Eventual parâmetro
    ainda indicado como pendente na forma de cálculo ou no corpo da regra não é antecipado
    por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-media-80-contribuicoes-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-8/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O rol é taxonomia versionada, não uma regra por doença. O § 13 fixa a média
    e o art. 27, I, mantém paridade. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Individualizar a doença catalogada e aplicar separadamente cálculo e
      reajuste.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado até 31/12/2003, acometido de
doença grave catalogada. Aplica-se a média do art. 24 sem proporcionalização e
a paridade do art. 27, I.

# Pendências localizadas

- confirmar o fluxo operacional de cotejo do diagnóstico com o rol vigente;
- confirmar a projeção da média com paridade no Sisprev;
- resolver Q6-S/Q6-T e completar o gate humano.
