# Relatório residual — regras permanentes de agentes nocivos

**Estado: análise interna. Não é consulta nem comunicação externa.**

Este relatório substitui a minuta de consulta. As perguntas foram pesquisadas
primeiro no repositório e em fontes oficiais. Cinco dos seis pontos foram
resolvidos sem contato com terceiros; resta uma única informação sobre a
execução interna do SISPREV.

## Conclusões já alcançadas

1. **Janelas e marco de ingresso.** Os ramos são:

   | ramo              | `data_adm_apos` | `data_adm_ate` | `data_direito_apos` |
   | ----------------- | --------------- | -------------- | ------------------- |
   | arts. 25 + 27, I  | `01/01/1950`    | `31/12/2003`   | `18/10/2021`        |
   | arts. 24 + 27, II | `31/12/2003`    | `31/12/2099`   | `18/10/2021`        |

   `DATA_ADM_ATE` inclui o dia gravado; `DATA_ADM_APOS` o exclui;
   `DATA_DIREITO_APOS` inclui o primeiro dia coberto. Para o fato jurídico,
   “ingresso em cargo efetivo” corresponde à **investidura, que ocorre com a
   posse**, e não à nomeação ou ao início do exercício. A Portaria MTP
   1.467/2022, art. 166, usa a investidura mais remota, e a LC estadual
   68/1992, art. 10, determina que a investidura ocorre com a posse.

2. **`tabelapontuacao`.** A leitura sustentada pelo catálogo é “tabela
   progressiva”, não “qualquer requisito expresso em pontos”. As faixas
   66/15, 76/20 e 86/25 dos arts. 8º da ECE 146/2021 e 41 da LCE 1.100/2021
   são fixas. Portanto, `tabelapontuacao: N` está correto nas unidades do art.
   41\. O candidato a correção é o `S` das regras 0068–0070, não o `N` das
   regras permanentes.

3. **Cobertura.** O art. 41 contém três hipóteses autônomas e nenhuma fonte
   autoriza omitir os incisos I e II. O modelo auditado deve ter seis unidades:
   três faixas em cada um dos dois ramos de cálculo e reajuste.

4. **Protocolo de prova.** O art. 42 da LCE 1.100/2021 e o Parecer
   PGE/IPERON 608/2025 confirmam formulários históricos, LTCAT conforme o
   período e PPP a partir de 2004. Prova apenas testemunhal ou recebimento de
   adicional de insalubridade não bastam.

5. **Responsabilidade documental.** O Decreto estadual 27.338/2022, arts. 4º
   e 23, distribui o fluxo: o órgão de pessoal de origem instrui o processo; o
   órgão ou entidade responsável pelos assentamentos emite o PPP; profissional
   habilitado emite o LTCAT; a equipe de atendimento do IPERON confere o
   checklist; e o IPERON recebe e processa o pedido.

## Única dúvida residual: `tipo_calculo` do art. 25

### O que já sabemos

- O comando jurídico é “totalidade da remuneração no cargo efetivo”.
- `Valor Médio` está descartado para esse ramo.
- O catálogo usa dois códigos para o mesmo comando:
  `Valor Efetivo` e `Remuneração de Contribuição`.
- `Remuneração de Contribuição` é o código predominante nas regras que
  descrevem totalidade; `Valor Efetivo` aparece em poucas regras e foi
  preservado na proposta porque já consta na `regra-0067`.
- Nenhuma documentação pública localizada define a fórmula executada por
  esses dois membros do enum.

### Por que a dúvida permanece

O texto legal resolve qual base deve ser aplicada, mas não revela o significado
interno dos códigos do produto. Escolher só pela proximidade do nome poderia
trocar a fórmula efetivamente executada pelo motor, que é justamente o que a
auditoria pretende evitar.

### Busca na fonte do fornecedor

Também foi pesquisado o domínio público da Agenda Assessoria, desenvolvedora do
Sisprev. A [página do Sisprev Web](https://www.agendaassessoria.com.br/page/sisprev-web)
confirma a existência de simulador parametrizável e de apuração de cálculo, e o
[catálogo da empresa](https://www.agendaassessoria.com.br/produtos-servicos)
confirma a autoria do produto. A [notícia sobre a implantação na
Amazonprev](https://www.agendaassessoria.com.br/post/fundacao-amazonprev-manausam-apresenta-novo-sistema-previdenciario-com-recursos-para-simulacao-de-concessao-de-aposentadoria-e-pensao-em-ambiente-virtual)
registra apresentação técnica, capacitação e painel de dúvidas. Nenhuma dessas
fontes, nem os PDFs públicos localizados, funciona como manual do enum ou
define a fórmula de `Valor Efetivo` e `Remuneração de Contribuição`. A busca,
portanto, reforça a ausência de evidência pública; não resolve a escolha.

### Hipótese atual

Os manuais de procedimento consultados no NotebookLM alteram o peso das
hipóteses. Eles descrevem **Remuneração Efetiva** como o valor da remuneração do
segurado e distinguem **Remuneração do Cargo Efetivo** de **Remuneração de
Contribuição**. Esta última é apresentada como base para as contribuições e pode
incluir gratificações/verbas com incidência previdenciária. Assim, a semântica
dos manuais favorece provisoriamente `Valor Efetivo` para o comando legal de
totalidade no cargo efetivo, embora o padrão do catálogo ainda favoreça
`Remuneração de Contribuição` por frequência.

O conflito restante é técnico, não mais puramente semântico: os manuais
descrevem campos da interface, mas não afirmam qual membro do enum
`tipo_calculo` os alimenta nem exibem um cálculo comparativo.

### Informação necessária

Basta **uma** das seguintes evidências internas:

- descrição ou ajuda da tela que define os dois tipos de cálculo;
- exemplo de cálculo do mesmo caso processado uma vez com cada código;
- conhecimento funcional de qual código representa a última remuneração no
  cargo efetivo.

Os trechos já localizados são: Meu RPPS, volume 2, p. 87; cadastro do segurado,
volume 1, p. 152; arrecadação, volume 1, pp. 77–78; e gratificações, volume 1,
p. 140. Os PDFs originais ainda precisam ser preservados no repositório ou
referenciados por caminho verificável para que essa evidência seja auditável.

Até isso ser esclarecido, as três unidades pré-2004 permanecem em `preview`.
As unidades pós-2003 não dependem dessa resposta, pois o art. 24 e o código
`Valor Médio` são coerentes entre si.

## Fontes

- [LCE 1.100/2021 compilada](https://ditel.casacivil.ro.gov.br/cotel/Livros/Files/LC1100%20-%20COMPILA%C3%87%C3%83O.pdf)
- [LC 68/1992 compilada](https://ditel.casacivil.ro.gov.br/cotel/Livros/Files/LC68%20-%20COMPILADA.pdf)
- [Portaria MTP 1.467/2022 atualizada](https://www.gov.br/previdencia/pt-br/assuntos/rpps/legislacao-dos-rpps/9PortariaMTPn1.467de02jun2022Atualizadaat3jun2024.pdf)
- [Decreto estadual 27.338/2022 no Diário Oficial](https://diof.ro.gov.br/data/uploads/2022/07/Doe-20-07-2022.pdf)
- [`Parecer PGE/IPERON 608/2025`](../../fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md)
