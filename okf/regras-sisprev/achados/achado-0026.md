---
type: Achado
id: achado-0026
nome: Três pares de regras simulavel S de incapacidade só se distinguem por campos de resultado, e o critério que os separa — a causa da incapacidade — não tem coluna; o motor não tem como escolher entre eles
situacao: aberto
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0021.md
  - /regras/regra-0022.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0006`/`0007`, `regra-0008`/`0009` e `regra-0021`/`0022` são três pares
de regras **todas com `simulavel: S`**. Dentro de cada par, **todo campo que
difere é um campo de resultado** — `integral`, `tipo_calculo` — ou um campo de
texto que o motor não lê. Nenhum predicado difere.

O critério que de fato separa cada par é a **causa da incapacidade**: acidente
em serviço, moléstia profissional ou doença grave, contagiosa ou incurável
levam a proventos integrais; as demais causas, a proporcionais. Esse critério
**não tem coluna no cadastro** — está apenas dentro do parêntese de um texto de
fundamentação que os dois membros de cada par compartilham, palavra por
palavra.

Daí a consequência que a spec P13.1 nomeia e que este achado registra em caso
concreto: *"uma regra `simulavel: S` é escolhida pelo motor, que não lê prosa:
se duas regras `simulavel: S` são idênticas em todos os parâmetros, o sistema
não tem como selecioná-las, e corrigir a fundamentação deixa o registro
verdadeiro sem resolver a seleção"*
([`okf/spec/regra.md`](../../../okf/spec/regra.md)).

# Evidências

## O que difere dentro de cada par, campo a campo

Diferença de frontmatter, excluídos `id` e `row_index`:

| par             | campos que diferem                                          | `simulavel` |
| --------------- | ----------------------------------------------------------- | ----------- |
| `0008` / `0009` | **`integral`** (S/N) — e mais nada                          | S / S       |
| `0021` / `0022` | `integral`, `tipo_calculo`                                  | S / S       |
| `0006` / `0007` | `integral`, `tipo_calculo`, `fundamentacao`, `dispositivos` | S / S       |

O par `0008`/`0009` é o caso extremo do catálogo: **uma única chave de
frontmatter separa as duas regras**, e é `integral`.

Dos quatro campos que separam `0006` de `0007`, nenhum é predicado:
`integral` e `tipo_calculo` são os "resultados candidatos" da Q6;
`fundamentacao` é prosa; e `dispositivos` é anotação de auditoria,
explicitamente fora da chave material do P2 (ver
[`okf/spec/dispositivo.md`](../../../okf/spec/dispositivo.md)).

## Os campos que o filtro de seleção lê são idênticos dentro de cada par

Os predicados estruturados hoje avaliáveis são `tipo_de_beneficio`, `sexo`,
`apos_especial` e as duas janelas de datas (é a lista que
`site/src/lib/simulador.ts` avalia, e a razão declarada é que os demais campos
não variam ou não são predicados). Dentro de cada um dos três pares, **os seis
são iguais**:

| campo               | `0006`/`0007` | `0008`/`0009` | `0021`/`0022` |
| ------------------- | ------------- | ------------- | ------------- |
| `tipo_de_beneficio` | INVALIDEZ     | INVALIDEZ     | INCAP. PERM.  |
| `sexo`              | AMBOS         | AMBOS         | AMBOS         |
| `apos_especial`     | N             | N             | N             |
| `data_adm_apos`     | 01/01/1950    | 01/01/1950    | 01/01/2004    |
| `data_adm_ate`      | 31/12/2099    | 31/12/2003    | 31/12/2099    |
| `data_direito_apos` | 31/12/2003    | 31/12/2003    | 23/10/2021    |
| `data_direito_ate`  | 31/12/2099    | 31/12/2099    | 31/12/2099    |

Logo, para qualquer conjunto de fatos que alcance um membro do par, alcança
igualmente o outro.

## O critério que os separa está dentro de um texto compartilhado

Nos pares `0006`/`0007` e `0008`/`0009`, os **dois** campos de fundamentação
são byte-idênticos entre os dois membros, e cada regra carrega as duas metades:

- a integral, cujo parêntese diz "(acidente em serviço, moléstia profissional
  ou doença grave, contagiosa ou incurável [...])";
- a proporcional, cujo parêntese diz "(doença não catalogada [...])" em
  `0006`/`0007` e "(sem acidente em serviço, moléstia profissional ou doença
  grave [...])" em `0008`/`0009`.

Em `0021`/`0022` o `fundamentacao_integral` é igualmente byte-idêntico entre os
dois, e é ele que empacota **três** cláusulas separadas por `|`, uma por classe
de causa.

Nos três casos o discriminante é nomeado — e nomeado **só ali**, num texto que
os dois membros compartilham. Nenhuma das 27 colunas do cadastro registra causa
da incapacidade; é a **Q6**, aberta, com a direção A já registrada em
[`q6-causa-incapacidade.md`](../../../docs/analysis/q6-causa-incapacidade.md)
§10.

## Nenhum detector reporta isto, e há razão para cada silêncio

Sobre estas cinco regras, a biblioteca emite hoje **apenas**
`P1_NOME_REPETIDO`, com `requires_achado: false`. Os três silêncios são
coerentes com o desenho de cada detector, e é por isso que a condição precisa
de achado autoral:

- **`P2_IGUALDADE_MATERIAL_ATIVA` não dispara**, e está certo: `integral` e
  `tipo_calculo` são campos de domínio, logo materiais, logo as regras **não
  são** materialmente iguais. Pela definição de trabalho da coordenação
  ("havendo divergência nos critérios aferidos, as regras não são idênticas"),
  elas são legitimamente duas.
- **`P1_NOME_REPETIDO` dispara**, mas mede outra coisa — o rótulo. Renomear
  resolveria o P1 sem tocar na seleção, porque o motor não lê `nome` para
  filtrar.
- **`P9_INTEGRAL_SEM_FUNDAMENTACAO` não dispara** em nenhuma das cinco: ele
  exige `integral: N` **com** `fundamentacao_proporcional` vazia, e aqui
  `0007`/`0009` têm o campo preenchido enquanto `0022` grava `integral: S`.

Ou seja: o defeito cai exatamente no ponto cego dos três detectores, e cada um
deles está correto ao não dispará-lo.

## O que é mecânico e o que não é

`verificacao: manual`, e a razão importa. As diferenças de frontmatter acima
são reproduzíveis por `diff` e o filtro do `/simulador/` **sinaliza** a
condição — ele detecta que duas regras compartilham todos os critérios
conhecidos e divergem apenas no resultado candidato, e emite pendência
explícita de Q6 nas duas. Mas isso é o motor TypeScript do site, **não um
detector com `fingerprint` estável** em `scripts/detectors/`; classificar como
`mecanica` exigiria comitar esse detector, e essa é uma decisão que este achado
não toma. Além disso, a conclusão — que os campos que diferem são *resultado* e
não predicado — **depende da Q6**, e Q6 é pergunta ao IPERON, não cálculo.

## O contraste com `regra-0019`/`0020` mostra o que `simulavel` decide

`regra-0019`/`0020` são o mesmo formato — `fundamentacao_integral`
byte-idêntico, diferença material em `integral` e `tipo_calculo`, causa da
incapacidade como discriminante sem coluna — **mas as duas são
`simulavel: N`**. Ali a regra é escolhida por um humano lendo a fundamentação,
e a ausência de coluna é problema de registro, não de seleção: o texto basta
para escolher.

É a distinção que a spec P13.1 faz e que este achado usa como recorte. Por isso
`0019` **não** está em `regras_afetadas`: a lacuna de representação é a mesma,
a consequência operacional não é.

## Limite desta conferência, declarado

- **A Q6 não é fechada aqui.** Se a coordenação responder que `integral` e
  `tipo_calculo` são também predicados aferidos — hipótese que a spec deixa
  expressamente aberta ("duas regras com aferição idêntica que divirjam só em
  `integral`/`tipo_calculo`/`paridade` podem ou não ser a mesma regra") —,
  então cada par são duas regras com predicado distinto e a impossibilidade de
  seleção desaparece. Este achado **não presume** a resposta; ele registra que
  as duas leituras possíveis levam a conclusões opostas, e qual é cada uma.
- **Não se afirma o que o motor do Sisprev faz.** O que se afirma é que os
  campos disponíveis não contêm o discriminante. Se o Sisprev seleciona por
  algo fora do CSV — outra tela, tabela externa, escolha do operador —, isso é
  informação que o catálogo não carrega, e é a pergunta de Q5.
- **`regra-0021` está em `regras_afetadas`** junto com as outras cinco: o
  defeito é *do par*, e um par não pode ser alcançado por metade. A
  conferência começou pelo lote que não a incluía; a população do achado é a
  do defeito, não a do lote. São seis regras, três pares.
- Nenhum vínculo `dispositivos:` é proposto, e nenhum campo é proposto para
  alteração: **a saída não é parametrização**, é granularidade (ver abaixo).

# Consequência prática

Um requerimento de aposentadoria por incapacidade permanente com ingresso até
31/12/2003 casa, pelos critérios estruturados, **igualmente** com `regra-0008`
e `regra-0009`. Uma delas concede proventos integrais e a outra proporcionais.
Nada nos campos decide, e as duas são `simulavel: S` — isto é, o cadastro
declara que a seleção é automática justamente onde ela não pode ser.

O par `0006`/`0007` reproduz o mesmo para ingresso sem restrição, e
`0021`/`0022` para ingresso após 2003 no regime da LCE 1.100/2021. São **três
das quatro faixas temporais do benefício**, e a única que escapa é a que grava
`simulavel: N`.

O erro que isso produz é assimétrico e a favor do erro caro: se o desempate
acabar sendo o primeiro casamento, a ordem de linha decide entre integral e
proporcional. Não afirmo que seja o comportamento real — é o que o catálogo
não impede.

Vale registrar o que **não** resolve. Diferenciar o texto da fundamentação
resolveria para uma regra `simulavel: N`; aqui deixa o registro verdadeiro e a
seleção igualmente indecidível, porque o motor não lê prosa. E renomear resolve
apenas o `P1_NOME_REPETIDO`.

# Questão a investigar

1. **Responder a Q6.** Se a causa da incapacidade é critério aferido — e as
   três classes da lei (com definição para duas delas, ver
   [`achado-0025`](achado-0025.md)) sugerem que é —, a saída dentro do escopo é
   a **decomposição em uma linha por classe de causa**, direção A da Q6 §10:
   três regras onde hoje há uma, cada uma com a sua fundamentação e o seu
   resultado. Isso é granularidade, que a definição de trabalho põe
   expressamente dentro do escopo ("a granularidade da aferição é conveniência
   do IPERON"). **Criar coluna de causa está fora do escopo** — é alterar o
   Sisprev, e seria pedido ao IPERON, registrado como tal.

2. **Se `simulavel: S` está correto nas cinco.** A alternativa mais barata, e
   que não depende da Q6, é rebaixar para `simulavel: N` — o que torna
   verdadeiro o que o cadastro afirma sobre si mesmo e alinha os três pares ao
   formato de `0019`/`0020`. É perda de automação assumida em vez de automação
   que não funciona. É campo deployável: decisão de quem responde por ele.

3. **Como o Sisprev hoje desempata.** É pergunta ao IPERON e a única que revela
   se o defeito já produziu efeito. Três requerimentos sintéticos a
   responderiam — ingresso em 1990, em 2000 e em 2010, todos por incapacidade
   permanente: quantas regras cada um oferece, e em que ordem.

4. **A ordem em relação aos outros achados deste lote.** A decomposição da Q6
   replicaria, em cada linha nova, a citação errada que
   [`achado-0050`](achado-0050.md) registra em `regra-0022`. **Corrigir a
   citação antes de decompor** evita multiplicar o defeito por três — a mesma
   inversão de urgência aparente do [`achado-0021`](achado-0021.md).
