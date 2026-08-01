---
type: UnidadeAuditada
id: invalidez-ec41-geral-acidente-em-servico
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: acidente_em_servico
  regime: ec41-regra-geral-preservada-art-4-ece146
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
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: define o ramo integral ou proporcional conforme a causa
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: disciplina os ramos de causa no período da LCE 432/2008
  - ref: /dispositivos/lei-10887-2004/art-1/original.md
    papel: disciplina a média contributiva no regime da EC 41/2003
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: disciplina a média no período final da LCE 432/2008
  - ref: /dispositivos/lce-432-2008/art-20-par-6/original.md
    papel: define acidente em serviço no período da LCE 432/2008
projecao:
  nome: >-
    Invalidez · EC 41/2003 · regra geral preservada · acidente em serviço ·
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
    - /dispositivos/lce-432-2008/art-17/original.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    - LC 228/2000, texto oficial do SAPL — regime estadual anterior à LCE 432/2008
    - docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md
  notas: >-
    A hipótese produz média contributiva temporalmente aplicável, sem
    proporcionalização pelo tempo. A mudança de diploma ou de rol dentro da
    janela não cria outra regra sem diferença material demonstrada. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco B por regime constitucional e classe de causa, com um
      ramo de resultado por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez em **EC 41/2003 · regra geral preservada**, por **acidente
em serviço**. O ramo é **integral**, com reajuste sem paridade.

A fronteira superior usa `data_direito_ate: 01/01/2025` porque o campo é
exclusivo: assim ficam incluídos os requisitos implementados até 31/12/2024,
como exige o art. 4º da ECE 146/2021.

A seleção exige prova positiva da classe qualificada. Ausência de informação ou
prova insuficiente não autoriza enquadramento em `causa_comum`.

# Pendências localizadas

- transcrever e versionar os dispositivos estaduais anteriores à LCE 432/2008;
- fechar a forma de cálculo dos subperíodos entre 31/12/2003 e a plena aplicação
  da Lei 10.887/2004;
- confirmar a projeção da combinação base média + proporcionalidade no Sisprev;
- resolver Q6-S/Q6-T quanto à obtenção e classificação operacional da causa.
