---
type: RegraProposta
id: invalidez-ec20-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0004
predicados:
  causa_incapacidade: acidente_em_servico
  regime: cf88-ec20-direito-adquirido
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
        conclusão médica de incapacidade permanente e reconhecimento suficiente
        do nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 16/12/1998 00:00
    data_direito_ate: 31/12/2003 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    papel: qualifica o acidente em serviço como ramo integral
  - ref: /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    papel: fixa a base na totalidade da remuneração do cargo efetivo
  - ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    papel: assegura paridade
  - ref: /dispositivos/ec-41-2003/art-3-caput/original.md
    papel: >-
      preserva a concessão pelos critérios anteriores para quem completou os
      requisitos antes de 31/12/2003
projecao:
  nome: Invalidez · EC 20/1998 · acidente em serviço · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontrava em estado de invalidez
    permanente, apurado por junta médica oficial mediante laudo, e que essa
    invalidez decorreu de acidente em serviço, cujo nexo com a atividade foi
    reconhecido a partir da comunicação e da apuração do acidente, dos
    prontuários e dos assentamentos funcionais. Ficou demonstrado, ainda, que os
    requisitos estavam integralmente cumpridos entre 16 de dezembro de 1998 e 30
    de dezembro de 2003.


    A hipótese se extrai da conjugação de quatro dispositivos, e é a articulação
    entre eles que a completa. O art. 40, § 1º, inciso I, da Constituição
    Federal, na redação da Emenda Constitucional nº 20/1998, autoriza a
    aposentadoria por invalidez permanente e, dentro do mesmo inciso, separa
    dois resultados: reserva os proventos integrais às invalidezes decorrentes
    de acidente em serviço, moléstia profissional ou doença grave, contagiosa ou
    incurável especificada em lei, e atribui proventos proporcionais nos demais
    casos. É por ser o acidente em serviço uma das causas ali qualificadas que
    esta regra conduz ao resultado integral, e é por isso que a demonstração do
    nexo com o serviço não é formalidade: dela depende o próprio ramo do
    cálculo. O art. 40, § 3º, na mesma redação, responde a pergunta que o inciso
    I não responde — sobre que valor o cálculo incide —, fixando a base na
    totalidade da remuneração do cargo efetivo; sem ele, "integral" diria apenas
    que não há redução, sem dizer redução de quê. O art. 40, § 8º, na mesma
    redação, opera depois da concessão e assegura a revisão dos proventos na
    mesma proporção e na mesma data da remuneração dos servidores em atividade.
    Por fim, como a concessão pode ocorrer depois de 31 de dezembro de 2003, o
    art. 3º da Emenda Constitucional nº 41/2003 é o que permite aplicar essa
    disciplina já alterada: ele assegura a concessão, a qualquer tempo, a quem
    houver cumprido todos os requisitos até a publicação daquela Emenda, com
    base nos critérios da legislação então vigente.


    Do enquadramento resulta a concessão de proventos integrais, sem redução
    proporcional ao tempo, calculados sobre a totalidade da remuneração do cargo
    efetivo, na forma de cálculo vinculada a esta regra e fundada no art. 40,
    § 3º, na redação da Emenda Constitucional nº 20/1998. A paridade não integra
    esse cálculo inicial: ela decorre do art. 40, § 8º e opera como regime de
    revisão posterior dos proventos já concedidos.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-totalidade-remuneracao-cargo-efetivo-ec20.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    - /dispositivos/ec-41-2003/art-3-caput/original.md
  notas: >-
    A mudança estadual sem efeito material distinto não cria nova regra. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: Decompor a regra-0004 por classe de causa e resultado.
confianca: media
---

# Síntese

Hipótese integral por acidente em serviço no regime da EC 20/1998, preservada
para direito adquirido até 30/12/2003.

# Pendências localizadas

- [ ] confirmar o fluxo operacional de classificação da causa.

A correspondência entre `tipo_calculo: Valor Efetivo` e a fórmula descrita acima
é **premissa declarada, não constatação**, e não é pendência desta regra: vale
igual para todo o catálogo e está registrada como questão geral na abertura do
relatório. É por ela que a `TipoCalculo` desta unidade traz
`fidelidade: parcial`.

A legislação estadual não é pendência **neste ramo**: o resultado é integral
sobre a totalidade da remuneração do cargo efetivo, e essa base vem do art. 40,
§ 3º, da própria Constituição na redação da EC 20/1998. A LC 68/1992 e a LC
228/2000 importariam se houvesse fração a medir, o que não é o caso aqui — é o
que separa esta unidade da `invalidez-ec20-causa-comum`.
