---
type: RegraProposta
id: invalidez-ec20-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0004
predicados:
  causa_incapacidade: doenca_catalogada
  regime: cf88-ec20-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol legal vigente na data do direito
    protocolo_verificacao:
      pergunta: >-
        O diagnóstico causador da incapacidade consta do rol legal vigente
        quando os requisitos foram implementados?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, exames, prontuários e texto legal do rol vigente
        na data do direito
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        diagnóstico confirmado, incapacidade permanente e correspondência
        expressa com o rol legal temporalmente aplicável
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 16/12/1998 00:00
    data_direito_ate: 31/12/2003 00:00
  versao_rol: norma-estadual-vigente-na-data-do-direito
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    papel: condiciona a integralidade à doença especificada em lei
  - ref: /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    papel: fixa a base na totalidade da remuneração do cargo efetivo
  - ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    papel: assegura paridade
  - ref: /dispositivos/ec-41-2003/art-3-caput/original.md
    papel: preserva a concessão pelos critérios anteriores para o direito adquirido
projecao:
  nome: Invalidez · EC 20/1998 · doença grave catalogada · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente decorria de doença grave, contagiosa
    ou incurável incluída no rol legal vigente na data do direito; a verificação foi realizada
    por junta médica oficial e instrução previdenciária do IPERON, mediante laudo médico oficial,
    exames, prontuários e texto legal do rol vigente na data do direito, tendo sido exigida
    a seguinte evidência: diagnóstico confirmado, incapacidade permanente e correspondência
    expressa com o rol legal temporalmente aplicável. Ficou também demonstrado que os requisitos
    foram implementados em 16/12/1998 ou depois, mas antes de 31/12/2003.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. O art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 20/1998 condiciona a integralidade
    à doença especificada em lei. O art. 40, § 3º, da Constituição Federal, na redação da
    EC 20/1998 fixa a base na totalidade da remuneração do cargo efetivo. O art. 40, § 8º,
    da Constituição Federal, na redação da EC 20/1998 assegura paridade. O art. 3, caput,
    da Emenda Constitucional nº 41/2003 preserva a concessão pelos critérios anteriores para
    o direito adquirido.


    O cálculo inicial segue a forma “Totalidade da remuneração do cargo efetivo — CF, redação
    da EC 20/1998”, vinculada a esta regra e sustentada pelos dispositivos articulados acima.
    O resultado não sofre redução proporcional ao tempo. Após a concessão, os proventos são
    revistos com paridade, segundo o dispositivo específico articulado acima. Eventual parâmetro
    ainda indicado como pendente na forma de cálculo ou no corpo da regra não é antecipado
    por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-remuneracao-cargo-efetivo-ec20.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    - >-
      legislação estadual vigente na data do direito: LC 68/1992 ou LC 228/2000
    - /dispositivos/ec-41-2003/art-3-caput/original.md
  notas: >-
    O rol é taxonomia versionada pela data do direito; a mudança de lista não
    produz uma regra por doença. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor a regra-0004 por classe de causa e manter o rol como taxonomia
      temporal.
confianca: media
---

# Síntese

Hipótese integral por doença catalogada no regime da EC 20/1998. O rol
aplicável é o vigente na data em que o direito foi implementado.

# Pendências localizadas

- transcrever os rols estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
