---
type: Achado
id: achado-0048
nome: A regra-0011 não grava o corte de ingresso de 16/12/1998 do art. 3º da EC 47/2005, que as três regras irmãs do catálogo gravam
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0011.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

A `regra-0011` é a pensão por morte derivada do art. 3º da EC 47/2005. Aquele
artigo condiciona o benefício a **ingresso no serviço público até 16/12/1998**,
e a regra grava `data_adm_ate: 31/12/2099` — a sentinela, isto é, **nenhum corte
de ingresso**.

O texto do art. 3º, transcrito em `okf/dispositivos/ec-47-2005/art-3-par-unico/original.md`
a partir do Planalto, é explícito:

> Art. 3º Ressalvado o direito de opção à aposentadoria pelas normas
> estabelecidas pelo art. 40 da Constituição Federal ou pelas regras
> estabelecidas pelos arts. 2º e 6º da Emenda Constitucional nº 41, de 2003, o
> servidor da União, dos Estados, do Distrito Federal e dos Municípios,
> incluídas suas autarquias e fundações, **que tenha ingressado no serviço
> público até 16 de dezembro de 1998** poderá aposentar-se com proventos
> integrais, desde que preencha, cumulativamente, as seguintes condições:
>
> Parágrafo único. Aplica-se ao valor dos proventos de aposentadorias concedidas
> com base neste artigo o disposto no art. 7º da Emenda Constitucional nº 41, de
> 2003, observando-se igual critério de revisão **às pensões derivadas dos
> proventos de servidores falecidos que tenham se aposentado em conformidade com
> este artigo**.

O parágrafo único — que é o dispositivo efetivamente vinculado pela regra — não
cria requisito novo: ele estende às pensões o critério de revisão das
aposentadorias concedidas **com base neste artigo**. Quem não ingressou até
16/12/1998 não se aposenta pelo art. 3º, logo não deixa pensão derivada dele.

# Evidências

`verificacao: manual`. O que sustenta a acusação não é só a leitura do artigo —
é o **próprio catálogo**, que grava esse corte em toda parte menos aqui.

| regra        | fundamento                                    | `data_adm_ate` |
| ------------ | --------------------------------------------- | -------------- |
| `regra-0085` | art. 3º da EC 47/2005 (voluntária, feminino)  | **16/12/1998** |
| `regra-0086` | art. 3º da EC 47/2005 (voluntária, masculino) | **16/12/1998** |
| `regra-0011` | art. 3º, § único da EC 47/2005 (pensão)       | **31/12/2099** |

As duas regras que aplicam o mesmo artigo gravam exatamente a data do artigo. A
terceira, que deriva delas, não grava nenhuma.

## A objeção óbvia foi testada, e o catálogo a refuta

A objeção correta é: *numa pensão, `data_adm_*` talvez não seja a admissão do
servidor falecido — pode ser campo sem uso, ou sobre o dependente.* Se fosse
assim, a sentinela seria a gravação certa e não haveria achado.

Não é assim, e a prova está na pensão vizinha. A `regra-0010` é a pensão
derivada do art. 6º-A da EC 41/2003 (redação da EC 70/2012), cujo texto exige
ingresso "até a data de publicação desta Emenda Constitucional" — a EC 41/2003,
publicada em 31/12/2003. A `regra-0010` grava `data_adm_ate: 31/12/2003`.

Ou seja: **dentro do mesmo tipo de benefício**, uma pensão por morte usa
`data_adm_ate` para gravar precisamente o corte de ingresso do artigo que a
funda. O campo tem esse uso em pensão, e a `regra-0011` é a que não o exerce.

Limite declarado desta conferência: ela não alcança o código do Sisprev, e
portanto não prova como o sistema **lê** `data_adm_ate` numa linha de pensão.
Prova que o catálogo o **preenche** como corte de ingresso do servidor, em duas
pensões conferidas, e que a `regra-0011` destoa das suas três irmãs. Se a
implementação ignorar o campo em pensão, o defeito muda de natureza (passa a ser
de documentação, não de elegibilidade) e não desaparece.

# Consequência prática

`data_adm_ate` é deployável e, se lido, decide elegibilidade. Lida como está
escrita, a `regra-0011` concede pensão derivada do art. 3º da EC 47/2005 a
dependente de servidor **admitido em qualquer data** — inclusive quem ingressou
em 2015 e nunca teve direito à aposentadoria daquele artigo. É a regra mais
generosa que a norma, no campo mais silencioso: não há detector de janela, e o
`P2_IGUALDADE_MATERIAL_ATIVA` não a aproxima de `0085`/`0086` porque benefício e
fundamentação diferem.

A `regra-0011` também está em [`achado-0047`](achado-0047.md), por outro campo
(`data_direito_ate: 31/12/2024` sem citar a ECE 146/2021 na fundamentação). São
dois defeitos independentes na mesma regra: um no corte de ingresso, outro no
prazo do resguardo estadual.

# Questão a investigar

1. **Se a data é 16/12/1998 ou 15/12/1998.** As irmãs gravam `16/12/1998`, e a
   convenção do catálogo é a janela **semiaberta `[apos, ate)`** — nove
   confirmações independentes, a última no [`achado-0015`](achado-0015.md). Sob
   ela, `data_adm_ate: 16/12/1998` exclui quem ingressou exatamente em
   16/12/1998, que o artigo inclui ("até 16 de dezembro"). O desvio de um dia é
   o mesmo que o `achado-0015` levanta e que este achado não resolve: copiar as
   irmãs propaga a convenção, e a convenção pode estar um dia fora da norma nos
   dois casos.

2. **Se a pensão herda o corte ou tem o seu próprio.** O parágrafo único fala
   das pensões derivadas de quem "se aposentou em conformidade com este artigo",
   o que sugere herança integral. Mas o catálogo não tem coluna que expresse
   "requisito do instituidor" versus "requisito do dependente", e usar
   `data_adm_*` para o primeiro é convenção observada, não contrato declarado.
   Isso é território da Q3/Q6 e não se fecha aqui.

3. **Se corrigir é ato da auditoria.** Não: o campo é entregue, e apertar a
   janela retira elegibilidade de casos que hoje ela admite — inclusive,
   possivelmente, de benefícios já concedidos. Quem responde pelo produto decide;
   este achado registra que as três irmãs discordam de uma só.
