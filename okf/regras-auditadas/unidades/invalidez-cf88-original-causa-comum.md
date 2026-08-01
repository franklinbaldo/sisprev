---
type: UnidadeAuditada
id: invalidez-cf88-original-causa-comum
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
- regra-0001
- regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
- predicado: a incapacidade permanente não decorre de acidente em serviço, moléstia profissional nem doença catalogada na norma aplicável
  protocolo_verificacao:
    pergunta: Há prova suficiente para excluir as classes qualificadas e enquadrar o caso no ramo residual proporcional?
    responsavel: junta médica oficial e instrução previdenciária do IPERON
    meio_de_prova: laudo médico oficial, prontuários, histórico ocupacional, apuração de eventual acidente e rol legal vigente
    momento: instrução e seleção da regra
    evidencia_exigida: incapacidade permanente comprovada e investigação suficiente das causas qualificadas; silêncio ou prova insuficiente não bastam
  portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
- ref: /dispositivos/cf88/art-40-inc-i/original.md
  papel: determina proventos proporcionais nos demais casos
projecao:
  nome: Invalidez · CF/88 original · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Não identificado
proveniencia:
  fontes_consultadas:
  - /dispositivos/cf88/art-40-inc-i/original.md
  - EC 20/1998, art. 3º — preservação do direito adquirido
  - legislação estadual vigente na data de implementação dos requisitos: LC 1/1984, LC 39/1990 ou LC 68/1992
  - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: O ramo residual exige exclusão probatória das causas qualificadas; ausência de informação não equivale a causa comum. Origem material: substituição.
decisoes:
- data: 2026-08-01
  quem: franklinbaldo
  o_que: Substituir a regra proporcional legada por unidade com fundamento e protocolo próprios.
confianca: media
---

# Síntese

Hipótese residual de invalidez proporcional sob CF/88 original. O valor `Não identificado` preserva a falta de projeção fiel da fórmula no enum legado, não desconhecimento do ramo jurídico.

# Pendências localizadas

- fechar a fórmula estadual aplicável em cada trecho da janela;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
