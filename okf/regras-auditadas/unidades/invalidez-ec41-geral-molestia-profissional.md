---
type: UnidadeAuditada
id: invalidez-ec41-geral-molestia-profissional
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: molestia_profissional
  regime: ec41-regra-geral-preservada-art-4-ece146
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de moléstia profissional, com nexo entre
      a patologia e a atividade funcional
    protocolo_verificacao:
      pergunta: >-
        A prova médica e ocupacional demonstra incapacidade permanente e nexo
        profissional suficiente?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, histórico ocupacional, prontuários, documentos
        ambientais e assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e conclusão fundamentada sobre o
        nexo profissional
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
    papel: inclui a moléstia profissional entre as causas qualificadas
  - ref: /dispositivos/lei-10887-2004/art-1/original.md
    papel: disciplina a média contributiva no regime da EC 41/2003
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: disciplina a média no período final da LCE 432/2008
projecao:
  nome: >-
    Invalidez · EC 41/2003 · regra geral preservada · moléstia profissional ·
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
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    - LC 228/2000, texto oficial do SAPL — regime estadual anterior à LCE 432/2008
    - docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md
  notas: >-
    A hipótese produz média contributiva temporalmente aplicável, sem
    proporcionalização. A definição operacional de moléstia profissional ainda
    depende de protocolo institucional. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco B por regime constitucional e classe de causa, com um
      ramo de resultado por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez em **EC 41/2003 · regra geral preservada**, por **moléstia
profissional**. O ramo é **integral**, com reajuste sem paridade.

A fronteira `data_direito_ate: 01/01/2025` é exclusiva e inclui os requisitos
implementados em 31/12/2024.

# Pendências localizadas

- transcrever e versionar os dispositivos estaduais anteriores à LCE 432/2008;
- fechar a forma de cálculo do intervalo inicial da EC 41/2003;
- definir o protocolo institucional de reconhecimento da moléstia profissional;
- resolver Q6-S/Q6-T quanto à classificação operacional da causa.
