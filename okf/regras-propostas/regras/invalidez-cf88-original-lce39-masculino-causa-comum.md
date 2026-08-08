---
type: RegraProposta
id: invalidez-cf88-original-lce39-masculino-causa-comum
ciclo: ciclo-09
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  Confirmar que `Valor Efetivo`, com `integral: N`, aplica 1/35 por ano ao
  servidor homem e observa a conversão e o arredondamento do art. 132.
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-lce39-direito-adquirido
  sexo: masculino
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença catalogada na norma aplicável
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir as classes qualificadas e enquadrar o
        caso no ramo residual proporcional?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e rol legal vigente
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e investigação suficiente das
        causas qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 31/07/1990 00:00
    data_direito_ate: 09/12/1992 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define o ramo proporcional residual
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva o direito adquirido
  - ref: /dispositivos/lce-39-1990/art-156/original.md
    papel: fixa a base estatutária
  - ref: /dispositivos/lce-39-1990/art-155-par-unico/original.md
    papel: fixa 1/35 por ano para homem
  - ref: /dispositivos/lce-39-1990/art-132/original.md
    papel: fixa conversão anual e arredondamento acima de 180 dias
projecao:
  nome: Invalidez · CF/88 original · LCE 39/1990 · homem · demais causas · 1/35 por ano · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: MASCULINO
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    O art. 40, inciso I, da Constituição Federal em seu texto original define
    o ramo proporcional residual e o art. 3º da EC 20 preserva o direito
    adquirido. De 31/07/1990 a 08/12/1992, o art. 156 da LCE 39/1990 fixa a
    base no vencimento acrescido da gratificação adicional por tempo e de
    outras vantagens pecuniárias. O art. 155, parágrafo único, determina para
    homem 1/35 por ano de efetivo exercício. O art. 132 manda apurar em dias,
    converter por anos de 365 dias e arredondar para um ano o resto superior a
    180 dias. O art. 40, § 4º, assegura a revisão paritária.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-remuneracao-lce39-proporcional-anos-masculino.md
    - /dispositivos/lce-39-1990/art-132/original.md
    - /dispositivos/lce-39-1990/art-155-par-unico/original.md
    - /dispositivos/lce-39-1990/art-156/original.md
  notas: >-
    O sexo é discriminante da fórmula neste trecho e não pode permanecer
    escondido em uma unidade com projeção AMBOS.
decisoes:
  - data: 2026-08-08
    quem: openai-codex
    o_que: >-
      Separar a fórmula masculina de 1/35 da fórmula feminina de 1/30.
confianca: alta
---

# Síntese

Hipótese residual proporcional masculina sob a LCE 39/1990.
