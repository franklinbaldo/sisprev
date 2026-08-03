---
type: RegraProposta
id: incapacidade-lce1100-apos-2003-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0022
predicados:
  causa_incapacidade: doenca_catalogada
  regime: lce1100-incapacidade-ingresso-apos-2003
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
    data_adm_apos: 01/01/2004 00:00
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
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: determina reajuste sem paridade para ingresso após 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso após 2003 · doença
    catalogada · média integral · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-8/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O rol é taxonomia versionada. O § 13 fixa a média do art. 24 e o art. 27,
    II, determina reajuste sem paridade. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Individualizar a doença catalogada na coorte posterior a 2003.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado após 31/12/2003, acometido
de doença grave catalogada. Aplica-se a média do art. 24 sem proporcionalização
e sem paridade.

# Pendências localizadas

- confirmar o cotejo operacional do diagnóstico com o rol vigente;
- confirmar a projeção operacional da média sem paridade;
- resolver Q6-S/Q6-T e completar o gate humano.
