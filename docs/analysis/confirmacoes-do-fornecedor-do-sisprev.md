# Confirmações da empresa responsável pelo Sisprev

> **Nota:** Registro de fatos sobre o **produto** obtidos junto à empresa que
> desenvolveu o Sisprev, trazidos à auditoria pela coordenação. **Não é artefato
> oficial** e não edita regra, dispositivo ou dado derivado. Existe porque um
> fato sobre o comportamento do sistema não é derivável do catálogo — ele vem de
> fora, e sem lugar próprio acabaria sobrevivendo só em conversa. Cada item diz o
> que foi confirmado e o que o item **não** resolve.

## Por que este documento existe

Boa parte das questões abertas da RFC 0001 pergunta o que um campo **significa
no sistema de origem** — a Q1 sobre o fato jurídico das datas, a Q10 sobre `sexo`
vazio e sobre `Não identificado`. Nenhuma delas se responde lendo o catálogo,
porque o catálogo é o que se quer interpretar.

A auditoria precisa de **hipótese de trabalho explícita** para prosseguir. Sem
ela, todo campo cuja semântica não esteja fechada ficaria imune a conferência, e
o catálogo sairia inauditável por uma questão que a auditoria existe para
resolver. Declarar a hipótese, e de onde ela veio, é o que permite saber
exatamente o que cai junto caso ela seja revista.

## As confirmações

### 1. `DATA_ADM_*` é a data de admissão

Fixa o **gênero** do marco: o campo registra entrada no serviço, não aquisição
de direito nem qualquer outro fato.

**O que não resolve.** A distinção fina da Q1 — nomeação, posse ou exercício —
segue aberta, e
[`docs/analysis/semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
continua correto ao registrá-la. Ela decide casos de fronteira.

**Ressalva com consequência própria.** "Admissão" e "ingresso na respectiva
carreira" podem não coincidir: quem foi admitido no serviço estadual numa data e
ingressou numa carreira específica em outra tem dois marcos distintos.
Dispositivos que recortam por ingresso em carreira — o art. 7º da ECE 146/2021 é
o caso trabalhado — recortam pelo segundo. Se o Sisprev afere o primeiro, o
descompasso atinge todas as regras daquele artigo.

**Onde já incide:** hipótese de trabalho declarada do `achado-0055`.

### 2. `sexo` vazio indica regra provavelmente desativada, mantida por histórico

A ausência de valor não é "ambos", nem "desconhecido": sinaliza que a regra
provavelmente não está mais em uso e permanece no cadastro para fins históricos.

**O que isso ilumina.** É a resposta que faltava para a Q10 na parte que
distingue `AMBOS` de vazio, e o marcador de inativação que o catálogo não
parecia ter — `atualmente_no_sistema` está uniformemente `TRUE` e por isso não
serve para essa leitura.

**Corroboração interna, não circular.** As regras com `sexo` vazio compartilham
uma assinatura que o campo não impõe: `integral` também vazio no mesmo conjunto,
`tipo_calculo: Não identificado` em todas, e `simulavel: N` em quase todas. Três
campos independentes concordando com a leitura do fornecedor é evidência de que
ela descreve um estado real do cadastro, e não uma coincidência de preenchimento.

**O que não resolve.** "Provavelmente desativada" não é ato de revogação. A
representação de uma regra fora de uso é `Conjunto.revoga` (RFC 0006), e isso
depende de decisão autorada por regra, não de inferência a partir de um campo
vazio. Também não se conclui que toda regra desativada tenha `sexo` vazio — a
implicação confirmada tem uma direção só.

### 3. O operador seleciona o **tipo do benefício** antes de escolher a regra pelo nome

O fluxo do sistema filtra por tipo primeiro; a lista de nomes que o operador vê
já está restrita àquele tipo.

**Consequência direta sobre o `nome`.** Repetir no nome o que o filtro anterior
já garantiu não ajuda a escolher e ocupa espaço: em toda a lista visível, o termo
é constante, e termo constante não recorta nada. É o mesmo raciocínio pelo qual o
site marca `data-pagefind-ignore` no que se repete igual em toda ficha.

**O que não resolve.** Se o tipo deve sumir do nome ou aparecer abreviado no
início é decisão de desenho, não fato do produto. Uma abreviação curta ainda
serve de âncora visual e protege contra leitura fora do fluxo — relatório,
planilha, ficha do site —, onde o filtro que dava o contexto não existe.

## Onde estas confirmações já estão incorporadas

Elas **não vivem só aqui**. Cada uma foi levada ao documento que governa a
leitura do campo, e é lá que quem audita a encontra sem precisar saber que este
documento existe:

- a semântica de `DATA_ADM_*` está na Q1 do quadro de questões e na seção
  "Elegibilidade temporal" de [`docs/spec/regra.md`](../spec/regra.md);
- a leitura de `sexo` vazio está na Q10 do mesmo quadro;
- a seleção do tipo antes do nome está na
  [Decisão 9](decisoes-de-auditoria-2026-07-30.md), que fixa a gramática de
  `nome`.

**O quadro de questões é a fonte operativa**; este documento é a proveniência.
Divergindo os dois, o quadro ganha e a divergência é ela própria um defeito a
corrigir — como vale para toda duplicação de verdade no repositório.

## O que este documento não é

Não é fonte normativa: nada aqui interpreta lei. Não é ato do IPERON: as
confirmações são sobre o comportamento do software, e quem responde pelo
conteúdo jurídico das regras é o instituto. E não é substituto de conferência —
uma confirmação sobre o produto explica o que o campo pretende registrar, jamais
que o valor gravado numa regra específica esteja correto.
