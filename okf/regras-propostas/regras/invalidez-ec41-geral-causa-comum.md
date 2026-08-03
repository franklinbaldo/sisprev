---
type: RegraProposta
id: invalidez-ec41-geral-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0007
predicados:
  causa_incapacidade: causa_comum
  regime: ec41-regra-geral-lce432-preservada-art-4-ece146
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença grave catalogada na norma aplicável
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir todas as classes qualificadas e
        enquadrar o caso no ramo residual proporcional?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e rol legal vigente
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e investigação suficiente das causas
        qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 13/03/2008 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: determina o ramo proporcional nos demais casos
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-17/original.md
    papel: disciplina a proporcionalização em dias
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: define o ramo residual proporcional
  - ref: /dispositivos/lce-432-2008/art-45/original.md
    papel: disciplina a base média de 13/03/2008 a 08/08/2012
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: disciplina a base média desde 09/08/2012
  - ref: /dispositivos/lce-432-2008/art-45-par-9/original.md
    papel: limita as remunerações mensais consideradas
  - ref: /dispositivos/lce-432-2008/art-45-par-10/original.md
    papel: limita a base à remuneração do cargo antes da fração
projecao:
  nome: >-
    Invalidez · EC 41/2003 · LCE 432 · demais causas · média proporcional em
    dias · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: N
  tipo_calculo: Proporcionalidade Dias
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/lce-432-2008/art-17/original.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-45/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    - /dispositivos/lce-432-2008/art-45-par-9/original.md
    - /dispositivos/lce-432-2008/art-45-par-10/original.md
    - /formas-calculo/forma-calculo-media-proporcional-dias-lce432.md
  notas: >-
    Esta unidade foi estreitada na reabertura da S3. Desde 13/03/2008, a base é
    a média do art. 45, limitada pelos §§ 9º e 10, e a fração é aplicada em dias
    pelo art. 17. O rótulo legado expressa apenas a fração e tem fidelidade
    parcial. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Separar o segmento da LCE 432 dos segmentos anteriores, porque a
      granularidade em dias e os limitadores alteram materialmente o cálculo.
confianca: alta
---

# Síntese

Hipótese residual da regra geral da EC 41 desde 13/03/2008. O provento é a média
contributiva limitada do art. 45, proporcionalizada em dias pelo art. 17, sem
paridade.

A unidade não cobre os direitos de 31/12/2003 a 12/03/2008, representados por
duas unidades próprias. A causa comum exige exclusão probatória das classes
qualificadas.

# Pendências localizadas

- confirmar a projeção técnica da fórmula composta no Sisprev;
- resolver Q6-S/Q6-T quanto à classificação operacional da causa.
