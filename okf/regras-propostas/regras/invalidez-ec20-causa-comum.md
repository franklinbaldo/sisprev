---
type: RegraProposta
id: invalidez-ec20-causa-comum
ciclo: ciclo-09
schema_version: 1
estado_auditoria: elaboracao
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  A ponte jurídica entre a proporcionalidade da invalidez e os denominadores de 35/30, a conversão temporal, a projeção e o fluxo de seleção ainda serão fechados.
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
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
    papel: referência sistemática para os denominadores de 35 anos para homem e 30 para mulher; a aplicação ao ramo de invalidez ainda é interpretação jurídica pendente
  - ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    papel: assegura paridade
  - ref: /dispositivos/ec-41-2003/art-3-caput/original.md
    papel: >-
      preserva a concessão pelos critérios anteriores para quem completou os
      requisitos antes de 31/12/2003
projecao:
  nome: Invalidez · EC 20/1998 · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
    - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
    - /tipos-calculo/tipo-calculo-totalidade-proporcional-tempo.md
    - EC 41/2003, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data do direito: LC 68/1992 ou LC 228/2000
  notas: >-
    O enum legado não representa fielmente totalidade da remuneração
    proporcional ao tempo; ausência de informação não equivale a causa comum.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: Decompor a regra-0004 por classe de causa e resultado.
  - data: 2026-08-07
    quem: franklinbaldo
    o_que: >-
      Registrar a hipótese de aplicar sistematicamente os denominadores de 35/30
      ao ramo proporcional da invalidez, sem tratá-la como conclusão: o inciso
      III, alínea “a”, disciplina aposentadoria voluntária e a ponte para a
      invalidez, bem como a conversão de anos em dias, permanece pendente.
confianca: media
---

# Síntese

Hipótese residual proporcional sob EC 20/1998. A proporcionalidade e a base
estão identificadas. Os denominadores de 35/30 são uma hipótese de
interpretação sistemática a partir do inciso III, alínea “a”, e não uma regra
literal do ramo de invalidez; a ponte jurídica e a conversão de anos em dias
permanecem pendentes.

# Pendências localizadas

- [ ] justificar juridicamente a aplicação dos denominadores de 35/30 ao ramo
  de invalidez, distinguindo-a da aposentadoria voluntária;
- [ ] identificar a fonte ou convenção jurídica para converter anos em dias;
- [ ] parametrizar forma de cálculo fiel no Sisprev;
- [ ] confirmar o fluxo operacional de classificação da causa.
