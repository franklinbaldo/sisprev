---
type: RegraProposta
id: invalidez-ec41-geral-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: acidente_em_servico
  regime: ec41-regra-geral-media-desde-mp167-preservada-art-4
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
    data_direito_apos: 20/02/2004 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: define o ramo sem proporcionalização nas causas qualificadas
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/mp-167-2004/art-1/original.md
    papel: institui a média desde 20/02/2004
  - ref: /dispositivos/lei-10887-2004/art-1/original.md
    papel: mantém a média federal após a conversão da MP
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: mantém o ramo qualificado no período estadual posterior
  - ref: /dispositivos/lce-432-2008/art-20-par-6/original.md
    papel: define acidente em serviço no período da LCE 432
  - ref: /dispositivos/lce-432-2008/art-45/original.md
    papel: reproduz a base média desde 13/03/2008
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: mantém a base média desde 09/08/2012
projecao:
  nome: >-
    Invalidez · EC 41/2003 · desde MP 167 · acidente em serviço · média sem
    proporcionalização · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente decorre de acidente em serviço,
    com nexo causal reconhecido; a verificação foi realizada por junta médica oficial e instrução
    previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente,
    prontuários e assentamentos funcionais, tendo sido exigida a seguinte evidência: incapacidade
    permanente comprovada e ato ou conjunto probatório que reconheça o nexo com o serviço.
    Ficou também demonstrado que os requisitos foram implementados em 20/02/2004 ou depois,
    mas antes de 01/01/2025.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 41/2003 define o ramo sem proporcionalização
    nas causas qualificadas. art. 4, da Emenda à Constituição do Estado nº 146/2021 preserva
    os requisitos anteriores se implementados até 31/12/2024. art. 1, da Medida Provisória
    nº 167/2004 institui a média desde 20/02/2004. art. 1, da Lei nº 10.887/2004 mantém a
    média federal após a conversão da MP. art. 20, da Lei Complementar Estadual nº 432/2008
    mantém o ramo qualificado no período estadual posterior. art. 20, § 6º, da Lei Complementar
    Estadual nº 432/2008 define acidente em serviço no período da LCE 432. art. 45, da Lei
    Complementar Estadual nº 432/2008 reproduz a base média desde 13/03/2008. art. 45, da
    Lei Complementar Estadual nº 432/2008 mantém a base média desde 09/08/2012.


    O cálculo inicial segue a forma “Média de 80% das remunerações de contribuição na invalidez
    da EC 41/2003”, vinculada a esta regra e sustentada pelos dispositivos articulados acima.
    O resultado não sofre redução proporcional ao tempo. Após a concessão, o reajuste ocorre
    sem paridade, de acordo com o regime articulado acima. Eventual parâmetro ainda indicado
    como pendente na forma de cálculo ou no corpo da regra não é antecipado por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-media-80-invalidez-ec41.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/mp-167-2004/art-1/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-20-par-6/original.md
    - /dispositivos/lce-432-2008/art-45/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  notas: >-
    A unidade foi estreitada para a média vigente desde 20/02/2004. O segmento
    de 31/12/2003 a 19/02/2004 usa remuneração integral do cargo e recebe unidade
    própria. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Separar a base remuneratória anterior à MP 167 da base média posterior.
confianca: alta
---

# Síntese

Invalidez qualificada por acidente em serviço, com direito implementado desde
20/02/2004. O cálculo usa a média de 80% sem proporcionalização e o reajuste é
sem paridade.

# Pendências localizadas

- confirmar a projeção operacional da média no Sisprev;
- resolver Q6-S/Q6-T quanto à obtenção e classificação da causa.
