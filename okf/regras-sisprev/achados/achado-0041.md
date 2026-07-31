---
type: Achado
id: achado-0041
nome: regra-0072 é a quinta cópia idêntica de regra-0074 a regra-0077 e fica fora do grupo P2 por um campo que repete o que o nome já diz
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0072.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O `achado-0007` registra o maior grupo de igualdade material da importação:
`regra-0074`, `regra-0075`, `regra-0076` e `regra-0077`, "quatro registros
ativos com o mesmo `nome` e as 26 colunas não-`NOME` byte-a-byte idênticas".

São **cinco**. A `regra-0072` é igual às quatro em tudo — `nome`,
`fundamentacao_integral`, `sexo: MASCULINO`, as quatro janelas, `integral`,
`paridade`, `tipo_calculo`, `simulavel`, `apos_especial`, `dispositivos:` — com
uma única exceção: o campo `fundamentacao`, vazio nas quatro e preenchido nela
com

> Artigo 7º, §§ 2º e 3º, da Emenda Constitucional Estadual nº 146/2021.

E esse é exatamente o conteúdo que o `nome` da regra já carrega ("Voluntária do
Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021") e que a
`fundamentacao_integral` das cinco já cita ("com base no artigo 7º, §§ 2º e 3º
da Emenda Constitucional Estadual nº 146/2021"). O campo que separa a
`regra-0072` das outras quatro não diz nada que as outras quatro não digam.

# Evidências

A comparação é direta e reproduzível: `diff` entre a `regra-0072` e cada uma das
quatro, neutralizando `id` e `row_index`, devolve **uma** linha de diferença em
cada caso — a do campo `fundamentacao`. As quatro são idênticas entre si também
nesse campo (todas vazias).

`fundamentacao` é material para o `P2_IGUALDADE_MATERIAL_ATIVA`. O detector
trata **todo** campo de frontmatter como material por padrão e exclui
nominalmente apenas identidade, proveniência e anotação de auditoria
(`scripts/detectors/igualdade_material.py`: `_IGNORED_FRONTMATTER_KEYS`) —
`fundamentacao` não está entre eles, e não deve estar: é coluna deployável. Logo
o grupo detectado tem quatro membros e não cinco por causa de um único campo de
texto.

`verificacao: manual`, e a razão é a de sempre: a detecção do P2 existe e está
correta (é a que o `achado-0007` reivindica pelo fingerprint
`sha256:0e9b792a…`); o que ela **não** pode dizer é que o campo que a
`regra-0072` tem a mais não a distingue de nada. Isso exige ler os três campos e
comparar o que dizem, e é conclusão humana. Nenhuma detecção é reivindicada
aqui, e a do `achado-0007` continua sendo dele.

A `regra-0073` é a gêmea feminina da `0072` e **não** entra: `sexo` é critério
aferido confirmado ([`docs/spec/regra.md`](../../../docs/spec/regra.md)), e as
alíneas da LC 51/1985 exigem tempos diferentes por sexo — ela é legitimamente
distinta. `regra-0111` e `regra-0112` também não: apesar de carregarem
praticamente a mesma `fundamentacao_integral`, as janelas delas são outras (ver
[`achado-0039`](achado-0039.md)).

# Relação com o que já está registrado

O `achado-0007` é o registro do grupo e continua válido no que afirma; este
achado acrescenta o membro que a detecção não alcança e diz por que não alcança.
Não o substitui e não reivindica a sua detecção.

A forma é a do `achado-0021`, invertida. Lá, `regra-0061`/`0062` ficam fora de um
grupo P2 por uma diferença textual que é **ela própria um defeito** (a citação de
um parágrafo único que não existe), de modo que corrigir o defeito faria o grupo
crescer. Aqui a diferença textual não é defeito nenhum — é uma citação correta —
e ainda assim esconde uma quinta cópia. Os dois casos mostram a mesma coisa por
caminhos opostos: **um grupo de igualdade material tem a extensão que os campos
de texto permitem, não a que os fatos têm.**

E há a consequência de sentido contrário, que importa para quem for arrumar o
lote: preencher o campo `fundamentacao` das quatro com o mesmo texto da `0072` —
o que seria melhoria óbvia de registro — **dissolveria** o grupo P2 de quatro e
formaria um de cinco, ou dissolveria os dois, dependendo do texto escolhido. O
fingerprint do `achado-0007` deixaria de ser emitido e o achado ficaria
`P14_ACHADO_SEM_DETECCAO` sem que nenhuma regra tivesse mudado de mérito.

# Consequência prática

Cinco regras ativas, `sexo: MASCULINO`, `simulavel: S`, com as mesmas duas
janelas e o mesmo `apos_especial: S`. Um requerente homem, policial civil,
admitido até 13/11/2019, casa com **todas as cinco**, e o motor não tem por onde
escolher: os requisitos que poderiam separá-las — idade, tempo de contribuição,
tempo de exercício policial — não têm coluna, e a fundamentação, que o motor não
lê, é a mesma nas cinco.

É o caso que a spec descreve como o pior dos dois: "uma regra `simulavel: S` é
escolhida pelo motor, que não lê prosa: se duas regras `simulavel: S` são
idênticas em todos os parâmetros, o sistema **não tem como** selecioná-las, e
corrigir a fundamentação deixa o registro verdadeiro sem resolver a seleção".
Com cinco, a observação vale cinco vezes.

Nada aqui afirma que sejam repetição de origem. A `regra-0068`/`0069`/`0070` são
o precedente da leitura oposta — três regras idênticas para os três incisos do
art. 8º da ECE 146/2021, distinção que nenhuma coluna registra —, e a hipótese
correspondente aqui seria alguma granularidade do art. 7º que o cadastro não
expressa. O art. 7º, porém, **não** tem três nem cinco incisos que a
justificassem: tem o caput e três parágrafos, conferidos na publicação oficial
da Emenda arquivada em `fontes-oficiais/arquivos/sapl-emenda_146.pdf` (p. 8,
lida visualmente — o PDF é digitalizado). Nada nele produz cinco hipóteses.

# Questão a investigar

1. **Se a `regra-0072` e as quatro são a mesma regra.** É a pergunta do
   `achado-0007`, agora sobre cinco linhas em vez de quatro, e a resposta é do
   IPERON: a granularidade do catálogo é escolha operacional, e consolidar 5:1 é
   unidade auditada mais grupo de substituição
   ([RFC 0004](../../../docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md)),
   não edição de regra. Nenhuma é proposta aqui.

1. **Se o campo `fundamentacao` das quatro deve ser preenchido.** Parece
   melhoria e tem o efeito colateral descrito acima sobre o `achado-0007`. Se for
   feito, o achado precisa ser reescrito no **mesmo** PR — a RFC 0001 exige que
   abertura, resolução e efeito sobre a regra afetada aconteçam coerentemente
   junto.

1. **O que distingue `fundamentacao` de `fundamentacao_integral` no Sisprev.** As
   cinco regras têm a integral preenchida e só uma tem a genérica; no catálogo
   inteiro o padrão é irregular. Enquanto a função de cada campo não for
   conhecida, não se sabe se o campo vazio nas quatro é lacuna ou é o
   preenchimento correto — e essa é a pergunta que decide o item 2.

# Correção proposta

A **`regra-0072` é mantida ativa** como a regra de referência do grupo por carregar a citação formal no campo `fundamentacao` (diferindo textualmente de `regra-0074` a `0077`, mas sendo semanticamente equivalente por repetir o que o `nome` e a `fundamentacao_integral` já contêm).

As outras quatro regras (`regra-0074`, `regra-0075`, `regra-0076` e `regra-0077`) são **propostas para revogação em lote** no conjunto `proposta-auditoria-2026-07.md` ([`proposta-auditoria-2026-07.md`](../../conjuntos/proposta-auditoria-2026-07.md)). Na hipótese de ativação da proposta pelo titular do produto, o catálogo unificado consolidará a fundamentação na `regra-0072`.
