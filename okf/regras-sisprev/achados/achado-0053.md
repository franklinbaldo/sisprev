---
type: Achado
id: achado-0053
nome: DATA_DIREITO_APOS grava sempre o dia da vigência da norma, e a leitura exclusiva tornaria a janela um dia curta em toda a população
situacao: resolvido
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0004.md
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0010.md
  - /regras/regra-0011.md
  - /regras/regra-0012.md
  - /regras/regra-0013.md
  - /regras/regra-0025.md
  - /regras/regra-0026.md
  - /regras/regra-0030.md
  - /regras/regra-0031.md
  - /regras/regra-0033.md
  - /regras/regra-0034.md
  - /regras/regra-0035.md
  - /regras/regra-0036.md
  - /regras/regra-0037.md
  - /regras/regra-0038.md
  - /regras/regra-0041.md
  - /regras/regra-0042.md
  - /regras/regra-0043.md
  - /regras/regra-0044.md
  - /regras/regra-0045.md
  - /regras/regra-0046.md
  - /regras/regra-0047.md
  - /regras/regra-0048.md
  - /regras/regra-0049.md
  - /regras/regra-0050.md
  - /regras/regra-0051.md
  - /regras/regra-0052.md
  - /regras/regra-0053.md
  - /regras/regra-0054.md
  - /regras/regra-0055.md
  - /regras/regra-0056.md
  - /regras/regra-0057.md
  - /regras/regra-0058.md
  - /regras/regra-0059.md
  - /regras/regra-0060.md
  - /regras/regra-0061.md
  - /regras/regra-0062.md
  - /regras/regra-0063.md
  - /regras/regra-0064.md
  - /regras/regra-0068.md
  - /regras/regra-0069.md
  - /regras/regra-0070.md
  - /regras/regra-0071.md
  - /regras/regra-0072.md
  - /regras/regra-0073.md
  - /regras/regra-0074.md
  - /regras/regra-0075.md
  - /regras/regra-0076.md
  - /regras/regra-0077.md
  - /regras/regra-0078.md
  - /regras/regra-0079.md
  - /regras/regra-0080.md
  - /regras/regra-0081.md
  - /regras/regra-0082.md
  - /regras/regra-0083.md
  - /regras/regra-0089.md
  - /regras/regra-0090.md
  - /regras/regra-0091.md
  - /regras/regra-0092.md
detectado_em: 2026-07-30
resolvido_em: 2026-07-30
resolvido_por: franklinbaldo
detectado_por: franklinbaldo
---

# Descrição

A **Q1** foi respondida em 2026-07-28: `DATA_ADM_APOS` é **exclusivo**, e o valor
gravado é o **marco** — `data_adm_apos = 31/12/2003` significa "admitido a partir
de 01/01/2004". A questão foi formulada com o curinga `DATA_*`, que pressupõe
semântica comum aos dois eixos, e por isso a leitura simétrica de
`DATA_DIREITO_APOS` (também exclusivo) parecia presumível.

A medição contra o próprio catálogo contradiz a simetria. Em toda regra cuja
`data_direito_apos` encosta na vigência de um dispositivo que ela mesma vincula,
o valor gravado é **o dia da entrada em vigor**, nunca o dia anterior. Não há uma
única exceção na importação congelada.

Sob a leitura exclusiva, a cobertura de cada uma dessas regras começaria no dia
**seguinte** ao da vigência da norma que lhe dá fundamento.

# Evidências

**A medição.** Para cada regra, comparou-se `data_direito_apos` com o
`vigencia_inicio` de cada dispositivo declarado em `dispositivos:`. Toda
coincidência encontrada é de igualdade exata; nenhuma é de um dia antes. A
população deste achado é exatamente o conjunto dessas regras, e o vínculo que a
prova é o dispositivo autorado no bundle, não uma tabela externa.

**Os quatro marcos, e o contraste entre as colunas.** Contando as grafias na
importação congelada, por marco de vigência e por coluna:

| marco          | `DATA_DIREITO_APOS` grava o dia | grava o dia anterior |
| -------------- | ------------------------------- | -------------------- |
| EC 20/1998     | sim                             | **nunca**            |
| EC 41/2003     | sim                             | **nunca**            |
| ECE 146/2021   | sim                             | **nunca**            |
| LCE 1.100/2021 | sim                             | **nunca**            |

O contraste com `DATA_ADM_APOS` é o ponto: ali o marco de 31/12/2003 é o **último
dia do regime antigo**, e a coordenação confirmou que a cobertura começa no dia
seguinte. Nas duas colunas o valor gravado é um marco legal real; o que difere é
**a relação entre o marco e o primeiro dia coberto**. Em `ADM_APOS` o marco fecha
o regime anterior; em `DIREITO_APOS` o marco abre o novo.

**A inconsistência entre as colunas está demonstrada. Qual das duas leituras o
motor aplica, não.** O catálogo não contém essa informação: nenhum campo registra
o operador de comparação, e a única fonte é o comportamento do Sisprev.

# Consequência prática

São duas possibilidades, e elas se excluem:

1. **`DATA_DIREITO_APOS` é inclusivo** — o valor é o primeiro dia coberto, o
   curinga `DATA_*` da formulação da Q1 foi uma generalização falsa, e **nenhuma
   regra desta população tem defeito de data**. A correção seria na spec, não no
   catálogo.
2. **O operador é uniformemente exclusivo** — e então toda regra desta população
   nega o benefício no **primeiro dia de vigência** da norma que a fundamenta.
   Seria erro sistemático de um dia num critério que o motor de fato afere, com
   consequência sobre requerimento protocolado exatamente naquele dia.

A diferença entre as duas não é de gravidade abstrata: é a diferença entre
"corrigir um parágrafo de spec" e "corrigir a janela de direito de quase todo o
catálogo".

**Este achado chegou tarde a uma conclusão que o [`achado-0015`](achado-0015.md)
já sustentava, e com evidência mais forte.** Ele estabelece que a convenção do
catálogo é o intervalo **semiaberto** `[apos, ate)`, por três caminhos
independentes: a contagem do preenchimento, sem exceção fora das três regras que
ele nomeia; o ladrilhamento da sucessão `regra-0091`→`regra-0097`, em que a
leitura fechada produziria sobreposição de regimes e a semiaberta não produz
nada; e a coincidência com o `vigencia_fim` dos dispositivos. A medição registrada
aqui **reproduz** aquela evidência por um quarto caminho, e não a substitui.

A consequência que este achado acrescenta é a do **outro** campo: se o intervalo é
semiaberto, então `DATA_DIREITO_APOS` é inclusivo *e* `DATA_DIREITO_ATE` é
exclusivo — o espelho do eixo da admissão, não a cópia dele. A spec foi corrigida
nesse ponto, porque afirmava `DATA_*_ATE` inclusivo com o mesmo curinga que já
havia induzido a leitura errada de `DATA_DIREITO_APOS`.

**A premissa firmada é a possibilidade 1** (2026-07-30, coordenação da auditoria):
`DATA_DIREITO_APOS` é lido como **inclusivo**, e o valor gravado é o primeiro dia
coberto. É a leitura que a medição sustenta — ela é a única que faz o valor
gravado significar o que ele de fato é, em toda a população, sem exceção. Sob ela,
**nenhuma regra desta população tem defeito de data**, e o que precisa de correção
é a generalização da Q1 pelo curinga `DATA_*`, não o catálogo.

O que a premissa muda é o ônus: a auditoria deixa de suspender a conferência da
fronteira inferior da janela e passa a conferi-la sob leitura declarada, uniforme
em todo o catálogo.

**Por que `informativo`, e não `bloqueante`.** O critério de severidade da
[spec](../../../docs/spec/regra.md) exige que o achado **demonstre** o defeito, e
registra que "achado cujo lado do erro é indeterminado permanece `informativo`,
porque bloquear exigiria fixar uma hipótese que o próprio achado declara aberta".
É exatamente este caso, e o precedente é o
[`achado-0024`](achado-0024.md), que foi `informativo` enquanto não se sabia se o
erro estava na regra ou no bundle, e virou `bloqueante` quando a fonte da
publicação desfez a simetria — sem que nenhum fato sobre o campo mudasse. Aqui a
simetria segue de pé: nada no catálogo diz qual lado cede.

Este achado é também o registro de uma **premissa retirada**. A leitura
simétrica de `DATA_DIREITO_APOS` foi proposta pela auditoria e ratificada como
premissa expressa, antes desta medição; a medição a derrubou, e a spec foi
corrigida no mesmo commit. A premissa se sustentava apenas na simetria do nome da
coluna — que é precisamente o que o curinga da Q1 já pressupunha.

# Questão a investigar

1. **Qual operador o Sisprev aplica às duas colunas do eixo do direito.** A
   convenção de **preenchimento** está estabelecida e não é mais o que se
   investiga. O que falta é o **comportamento do motor**, e a pergunta certa não é
   sobre `APOS` isolado: é se o Sisprev compara `DATA_DIREITO_ATE` com `<=` ou com
   `<`. Se for `<=` enquanto a convenção é semiaberta, cada janela concede um dia
   a mais, e o defeito é da convenção inteira em vez das exceções — é a segunda
   questão do [`achado-0015`](achado-0015.md), e nenhuma medição interna a
   alcança.
2. **Se o operador difere por coluna, o que mais difere.** Uma resposta que
   confirme assimetria entre `ADM` e `DIREITO` obriga a reabrir a Q1: o que foi
   confirmado com o curinga `DATA_*` vale para o eixo de admissão, e o eixo de
   direito passa a precisar de confirmação própria em cada uma das duas colunas —
   inclusive `DATA_DIREITO_ATE`, cuja inclusividade foi afirmada pela mesma
   resposta.
3. **Se há requerimento decidido exatamente no dia da vigência.** Sob a
   possibilidade 2, é o caso concreto em que o defeito se materializa, e é o que
   permitiria conferir o comportamento real do motor sem depender de
   documentação. Depende dos `precedentes`, cujo preenchimento está condicionado
   à decisão de PII da RFC 0010.

# Resolução

**Resolvido em 2026-07-30 pela adoção de critério uniforme, não por resposta do
Sisprev.**

A pergunta que este achado abriu — qual leitura das colunas do eixo do direito a
auditoria usa — está respondida: **o intervalo é semiaberto**, `DATA_DIREITO_APOS`
inclusivo e `DATA_DIREITO_ATE` exclusivo, aplicado uniformemente a todo o
catálogo. A evidência é a do [`achado-0015`](achado-0015.md), reproduzida aqui por
um quarto caminho, e o critério está registrado na
[spec](../../../docs/spec/regra.md) ("Elegibilidade temporal").

O que restou — se o motor compara o fecho com `<=` ou com `<` — **não é questão de
regra nenhuma**, e mantê-la como achado aberto sobre esta população teria um custo
sem contrapartida: cada uma destas regras passaria a precisar de disposição
escrita, uma a uma, para um ponto que é idêntico em todas e não decide nada sobre
nenhuma delas em particular. Se a resposta um dia for "`<=`", ela não corrige
regras: corrige a **convenção**, de uma vez.

Por isso a pergunta foi movida para onde ela de fato pertence: o **questionamento
geral do relatório de validação** (`docs/relatorio/abertura.md`, seção "Uma
questão geral, que não é de nenhum capítulo"), fora dos capítulos e fora da
manifestação por regra. Ela continua registrada e endereçada — deixa apenas de
pesar sobre documentos que não a respondem.

A conclusão de mérito deste achado **não muda com isso**: sob o critério adotado,
nenhuma regra desta população tem defeito de data.
