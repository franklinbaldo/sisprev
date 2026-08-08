---
titulo: Relatório jurídico conclusivo do Ciclo 9
subtitulo: >-
  Janelas históricas de aposentadoria por invalidez — manifestação para
  assinatura e carga parcial de homologação destinada ao IPERON
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
processo_sei: ''
expediente_de_origem: ''
unidade_solicitante: ''
unidade_coordenadora: ''
destinatarios: ''
---

<!-- encaminhamento -->

# Encaminhamento institucional

Este relatório consolida o resultado jurídico do Ciclo 9 sobre as janelas
históricas de aposentadoria por invalidez e identifica a carga de homologação
formada exclusivamente pelos componentes cuja auditoria está concluída.

## Conclusão submetida à assinatura

**Não se identifica óbice jurídico ao encaminhamento para homologação dos
{{destinosNaCarga}} destinos pertencentes aos {{gruposAtivos}} componentes
prontos**, observadas as ressalvas verificáveis deste relatório.

O componente não pronto e seus {{destinosForaDaCarga}} destinos ficam
expressamente excluídos da carga. Essa exclusão preserva a atomicidade e não
converte a lacuna jurídica residual em aprovação, validação ou risco aceito
pela instituição.

## Providência esperada da coordenação

1. preencher os dados administrativos de origem antes da assinatura;
2. colher a assinatura da autoridade jurídica competente;
3. encaminhar ao IPERON este relatório, a carga identificada por resumo
   criptográfico e os CSVs que acompanham o artefato da execução;
4. acompanhar a homologação e documentar o resultado das ressalvas;
5. submeter eventual implantação à autoridade administrativa competente.

## Providência esperada do IPERON

1. conferir a integridade do arquivo e inserir em homologação somente os
   {{destinosNaCarga}} destinos que ele contém;
2. executar os cenários de fronteira e de causa indicados nas ressalvas;
3. documentar entradas, resultados esperados, resultados obtidos e
   divergências;
4. instituir controles administrativos onde o automatismo não representar os
   fatos do segurado ou da instrução;
5. não ativar em produção regra com divergência não tratada.

## Limite desta manifestação

Este relatório não registra assinatura, validação da PGE, aprovação do IPERON,
homologação, decisão de implantação ou ativação em produção. Esses atos são
posteriores e somente existem quando praticados e documentados pela autoridade
competente.

<!-- abertura -->

# Objeto, alcance e conclusões jurídicas

## Objeto

O Ciclo 9 examina as regras históricas de aposentadoria por invalidez que podem
fundamentar requerimentos posteriores quando os requisitos do direito foram
implementados dentro das respectivas janelas. A data do requerimento não fecha
nem reabre uma janela de direito adquirido.

A proposta alcança {{origens}} regras cadastradas e as decompõe em
{{destinos}} unidades, ligadas em {{grupos}} componentes conexos pelo grafo
origem↔destino. A atomicidade é consequência desse grafo, não agrupamento
editorial.

## Resultado da auditoria

Das {{destinos}} unidades, {{destinosConcluidos}} têm dispositivo, requisitos,
fórmula e representação juridicamente determinados; {{destinosEmElaboracao}}
permanece em elaboração. Por isso, {{gruposAtivos}} componentes integram a
carga e {{gruposBloqueados}} permanece fora dela por inteiro.

## Conclusões jurídicas

1. **As janelas são de implementação do direito.** Requerimento posterior pode
   invocar direito adquirido, mas requisito implementado depois do marco final
   não entra na regra histórica.
2. **As causas são discriminantes jurídicos.** Acidente em serviço, doença
   grave catalogada e moléstia profissional afastam a proporcionalização nos
   regimes que as qualificam; a causa comum é o ramo residual e exige exclusão
   probatória das qualificadas.
3. **Base, proporcionalidade e reajuste são dimensões distintas.** “Integral”
   significa ausência do redutor temporal e não escolhe, sozinho, remuneração
   do cargo ou média contributiva. Paridade é regime de revisão posterior.
4. **A EC 20 exige ponte interpretativa expressa.** Na causa comum, os
   denominadores de 35/30 no primeiro trecho resultam de interpretação
   sistemática, corroborada sem efeito vinculante estadual pela IN SEAP
   5/1999; desde a LCE 228, as frações vêm diretamente da lei estadual.
5. **O art. 6º-A da EC 41 preserva remuneração do cargo e paridade.** As causas
   qualificadas dessa janela não recebem redução temporal; o reconhecimento do
   acidente, do rol ou do nexo profissional pertence à instrução do caso.
6. **O art. 4º da ECE 146 preserva a legislação vigente em 14/09/2021.** A LCE
   1.100/2021, posterior, não substitui o rol da LCE 432 na janela que fecha em
   31/12/2024.
7. **A causa comum sob a LCE 68 contém risco residual localizado.** O veto ao
   parágrafo único do art. 235 deixou sem denominador expresso a
   proporcionalidade. Não se importou silenciosamente razão de outro regime;
   o componente inteiro permanece fora da carga.

## Decisões de modelagem

As causas qualificadas são representadas em unidades próprias para que seleção,
prova e revisão sejam rastreáveis. Mudança de fonte estadual sem alteração de
base, fórmula, resultado ou projeção não cria nova unidade. A separação por
subfaixa ocorre quando muda a operação de cálculo, e não apenas porque mudou o
número da lei citada.

## Distinção entre os cinco planos

A proposta registra o que o catálogo representa. Ressalvas sobre dados do
segurado, motor de cálculo, instrução administrativa e ato concessório não são
convertidas em afirmação de incapacidade do Sisprev. Onde a evidência apenas
mostra que não se sabe como o sistema executa a hipótese, a matéria segue para
homologação ou controle administrativo documentado.

<!-- responsabilidades -->

# Ressalvas, controles e responsabilidades

{{regrasComRessalva}}. As classes constam do Anexo II e são derivadas dos
predicados estruturados das propostas, nunca de palavras encontradas na prosa.

## Cenários mínimos de homologação

- causa comum com tempo inferior ao denominador, conferindo base, fração,
  arredondamento e piso;
- acidente em serviço com e sem nexo reconhecido;
- doença catalogada na véspera e no dia de cada mudança do rol;
- moléstia profissional com e sem conclusão de nexo ocupacional;
- véspera e dia de cada marco de direito, mantendo a data do requerimento como
  eixo independente.

Cada cenário deve registrar dados de entrada, regra selecionada, memória de
cálculo, resultado esperado, resultado obtido e evidência da unidade
responsável. Divergência impede ativação da regra alcançada, mas não apaga da
carga as demais regras do mesmo componente já encaminhado para homologação.

## Dependências externas e controles

Processo, expediente, unidades e destinatários são pendências documentais
nomeadas na seção de situação. Protocolos de reconhecimento de acidente, rol e
nexo profissional cabem ao IPERON. A ausência de coluna própria no catálogo
não demonstra ausência de dado, cálculo, instrução ou registro no ato
concessório.

## Matriz de responsabilidades

| Responsável                  | Competência nesta entrega                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Procuradoria-Geral do Estado | assinar, se adotar a manifestação; prestar esclarecimento jurídico e decidir futuramente sobre a lacuna residual |
| Coordenação                  | completar a origem administrativa; encaminhar relatório e arquivos; acompanhar o retorno                         |
| IPERON — unidade técnica     | conferir o hash; carregar somente os destinos relacionados; executar e documentar a homologação                  |
| IPERON — concessão           | definir controles, responsáveis, provas e momento da conferência no processo individual                          |
| Autoridade administrativa    | decidir sobre implantação somente após homologação; não autorizar produção diante de divergência não tratada     |

<!-- notas -->

# Notas de seção do relatório

## origens

As regras cadastradas abaixo são as origens do componente. A manifestação só
propõe sua substituição quando o componente está pronto, homologado e objeto de
ato posterior de implantação. Origem de componente bloqueado não deve ser
desativada por força deste relatório.

## destinos

As regras propostas abaixo pertencem ao componente. O selo do capítulo informa
se entram na carga atual ou permanecem fora dela por atomicidade.

## projecao

O arquivo contém exatamente os destinos dos componentes prontos. A relação
completa, inclusive as propostas excluídas, está no Anexo I; o Anexo III
reproduz somente as fichas que efetivamente constam da carga.

## dispositivos

Os textos abaixo são transcrições destiladas dos dispositivos usados pela
auditoria. As fontes integrais e suas transcrições pesquisáveis permanecem
versionadas no repositório. O papel atribuído a cada dispositivo é conclusão
analítica; a transcrição é a evidência normativa.

## manifestacao

Este capítulo contém conferências ainda abertas. Elas devem ser classificadas
pelo efeito: jurídica ou de modelagem bloqueia o componente; operacional ou
externa segue como ressalva ou providência sem rebaixar conclusão jurídica já
determinada.

## manifestacao-sem-pontos

Não há item pendente no corpo das propostas deste componente. As ressalvas de
homologação indicadas nos selos permanecem condições para ativação, não para a
entrada na carga.

## manifestacao-geral

Concluída a auditoria jurídica das regras deste componente, **não se identifica
óbice jurídico ao seu encaminhamento na carga de homologação**, observadas as
ressalvas registradas. Isso não constitui aprovação institucional nem
autorização de produção.

## manifestacao-bloqueada

Este componente **não integra a carga de homologação**. A causa comum sob a LCE
68/1992 permanece sem denominador juridicamente demonstrado após o veto ao
parágrafo único do art. 235. A atomicidade impede encaminhar apenas as demais
unidades da mesma origem. Não se registra aceitação institucional desse risco.

<!-- encerramento -->

# Fechamento e documentos da entrega

## Resultado material

- {{destinosConcluidos}} unidades estão juridicamente determinadas;
- {{destinosEmElaboracao}} unidade permanece em elaboração;
- {{gruposAtivos}} dos {{grupos}} componentes estão prontos;
- {{destinosNaCarga}} destinos integram a carga de homologação;
- {{destinosForaDaCarga}} destinos permanecem fora da carga por atomicidade;
- {{regrasComRessalva}}.

## Atos que ainda não ocorreram

1. preenchimento dos dados administrativos desta minuta;
2. assinatura da manifestação pela autoridade competente;
3. remessa formal do relatório e dos arquivos ao IPERON;
4. inserção no ambiente de homologação;
5. execução e documentação dos cenários;
6. decisão administrativa sobre implantação;
7. ativação em produção.

Nenhum desses atos é inferido de CI verde, geração de PDF, abertura de PR ou
existência do arquivo. O catálogo em produção permanece inalterado até ato
institucional próprio.

## Documentos que compõem a entrega

1. este relatório jurídico;
2. Anexo I — relação completa das propostas e situação na carga;
3. Anexo II — matriz das regras da carga com ressalva;
4. Anexo III — projeção das regras efetivamente presentes na carga;
5. `data/regras-propostas-ciclo-09.csv`, identificado pelo resumo
   criptográfico impresso;
6. CSV global e artefato `relatorio-e-carga` da execução da PR.

O componente residual poderá ser objeto de manifestação posterior sem alterar
o conteúdo já determinado dos componentes prontos.
