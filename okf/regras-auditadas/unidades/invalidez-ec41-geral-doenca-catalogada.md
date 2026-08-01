---
type: UnidadeAuditada
id: invalidez-ec41-geral-doenca-catalogada
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: doenca_catalogada
  regime: ec41-regra-geral-preservada-art-4-ece146
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol vigente na data de implementação dos requisitos
    protocolo_verificacao:
      pergunta: >-
        A doença incapacitante consta do rol legal temporalmente aplicável e
        está comprovada pela perícia oficial?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários e versão vigente do rol legal de
        doenças
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente, diagnóstico e correspondência com o rol
        aplicável ao marco temporal do direito
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: define o ramo integral ou proporcional conforme a causa
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: inclui a doença grave entre as causas qualificadas
  - ref: /dispositivos/lce-432-2008/art-20-par-9/original.md
    papel: contém o rol no período da LCE 432/2008
  - ref: /dispositivos/lei-10887-2004/art-1/original.md
    papel: disciplina a média contributiva no regime da EC 41/2003
projecao:
  nome: >-
    Invalidez · EC 41/2003 · regra geral preservada · doença grave catalogada ·
    integral · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-20-par-9/original.md
    - LC 228/2000, texto oficial do SAPL — rol estadual anterior à LCE 432/2008
  notas: >-
    `doenca_catalogada` é o valor implementado do vocabulário controlado e
    corresponde à classe descrita na S1 como doença grave catalogada. O rol é
    versionado pela data do direito. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco B por regime constitucional e classe de causa, com um
      ramo de resultado por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez em **EC 41/2003 · regra geral preservada**, por **doença
grave catalogada**. O ramo é **integral**, com reajuste sem paridade.

O rol deve ser lido na versão vigente quando os requisitos foram implementados.
A fronteira superior exclusiva em 01/01/2025 inclui 31/12/2024.

# Pendências localizadas

- transcrever e versionar o rol anterior à LCE 432/2008;
- fechar a forma de cálculo do intervalo inicial da EC 41/2003;
- confirmar o fluxo operacional de cotejo do diagnóstico com o rol temporal;
- resolver Q6-S/Q6-T quanto à classificação operacional da causa.
