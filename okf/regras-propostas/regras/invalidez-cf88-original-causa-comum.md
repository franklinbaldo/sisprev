---
type: RegraProposta
id: invalidez-cf88-original-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-direito-adquirido
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
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: determina proventos proporcionais nos demais casos
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade — revisão dos proventos na mesma proporção e data da remuneração dos ativos
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: assegura a concessão a quem cumpriu os requisitos antes da emenda, pelos critérios então vigentes
projecao:
  nome: Invalidez · CF/88 original · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    O ramo residual exige exclusão probatória das causas qualificadas; ausência
    de informação não equivale a causa comum. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir a regra proporcional legada por unidade com fundamento e
      protocolo próprios.
confianca: media
---

# Síntese

Hipótese residual de invalidez proporcional sob CF/88 original. `Valor Efetivo`
nomeia a base — a remuneração do cargo efetivo —, e a proporcionalidade é
carregada por `integral: N`; a **medida** da fração é o que segue sem fonte
identificada, e é por isso que a fundamentação desta unidade ainda não foi
autorada (RFC 0014 §2.3: sem `FormaCalculo` fechada não se escreve a parte 3).

# Pendências localizadas

- fechar a fórmula estadual aplicável em cada trecho da janela. A Constituição
  diz "proporcionais" sem denominador, e a LC 228/2000 é posterior à janela; as
  candidatas registradas em `proveniencia.fontes_consultadas` — LC 1/1984, LC
  39/1990 e LC 68/1992 — não foram cotejadas nem decididas. Sem isso não há
  `FormaCalculo` a vincular, e o grupo do Bloco A, que é atômico, não ativa;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
