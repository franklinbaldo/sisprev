---
type: RegraProposta
id: invalidez-ec20-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0004
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-ec20-direito-adquirido
  sexo: ambos
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
        incapacidade permanente comprovada e investigação suficiente das causas
        qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 16/12/1998 00:00
    data_direito_ate: 31/12/2003 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    papel: determina proventos proporcionais nos demais casos
  - ref: /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    papel: fixa a base na totalidade da remuneração do cargo efetivo
  - ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    papel: assegura paridade
  - ref: /dispositivos/ec-41-2003/art-3-caput/original.md
    papel: preserva a concessão pelos critérios anteriores para o direito adquirido
projecao:
  nome: Invalidez · EC 20/1998 · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente não decorria de acidente em serviço,
    moléstia profissional nem doença catalogada na norma aplicável; a verificação foi realizada
    por junta médica oficial e instrução previdenciária do IPERON, mediante laudo médico oficial,
    prontuários, histórico ocupacional, apuração de eventual acidente e rol legal vigente,
    tendo sido exigida a seguinte evidência: incapacidade permanente comprovada e investigação
    suficiente das causas qualificadas; silêncio ou prova insuficiente não bastam. Ficou também
    demonstrado que os requisitos foram implementados em 16/12/1998 ou depois, mas antes de
    31/12/2003.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. O art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 20/1998 determina proventos
    proporcionais nos demais casos. O art. 40, § 3º, da Constituição Federal, na redação da
    EC 20/1998 fixa a base na totalidade da remuneração do cargo efetivo. O art. 40, § 8º,
    da Constituição Federal, na redação da EC 20/1998 assegura paridade. O art. 3, caput,
    da Emenda Constitucional nº 41/2003 preserva a concessão pelos critérios anteriores para
    o direito adquirido.


    O cálculo inicial segue a forma “Totalidade da remuneração do cargo efetivo, proporcional
    ao tempo de contribuição”, vinculada a esta regra e sustentada pelos dispositivos articulados
    acima. O resultado recebe a proporcionalização pelo tempo descrita nessa forma. Após a
    concessão, os proventos são revistos com paridade, segundo o dispositivo específico articulado
    acima. Eventual parâmetro ainda indicado como pendente na forma de cálculo ou no corpo
    da regra não é antecipado por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-proporcional-tempo.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    - >-
      legislação estadual vigente na data do direito: LC 68/1992 ou LC 228/2000
    - /dispositivos/ec-41-2003/art-3-caput/original.md
  notas: >-
    O enum legado não representa fielmente totalidade da remuneração
    proporcional ao tempo; ausência de informação não equivale a causa comum.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: Decompor a regra-0004 por classe de causa e resultado.
confianca: media
---

# Síntese

Hipótese residual proporcional sob EC 20/1998. A fórmula jurídica é conhecida,
mas a projeção fiel ainda exige forma de cálculo parametrizável no Sisprev.

# Pendências localizadas

- confirmar os parâmetros estaduais da proporcionalidade;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
