---
type: Achado
id: achado-0014
nome: A citação de EC 41/2003 para o art. 40, § 1º, II nomeia a alteração do caput, que não está transcrito
situacao: aberto
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0027.md
  - /regras/regra-0028.md
  - /regras/regra-0029.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0027`, `regra-0028` e `regra-0029` citam o art. 40, § 1º, inciso II da
Constituição Federal "com redação dada pela Emenda Constitucional nº
41/2003" — em `nome` na primeira, em `fundamentacao_proporcional` nas outras
duas.

A EC 41/2003 **não alterou o texto literal do inciso II**. Alterou o *caput*
do § 1º, do qual o inciso extrai sua base de cálculo. **A citação é
legítima**, e este achado não a acusa: registra que ela não pode ser
conferida hoje, porque a redação que ela nomeia não está no corpus.

# Evidências

O inciso é oração subordinada ao *caput*: lê-se "os servidores [...] serão
aposentados, calculados os seus proventos a partir dos valores fixados na
forma \[...\]: **II - compulsoriamente, aos setenta anos de idade, com
proventos proporcionais ao tempo de contribuição**". Sozinho, o inciso não
diz como se calculam os proventos que ele mesmo determina serem
proporcionais — quem diz é o *caput*.

E foi exatamente o *caput* que a EC 41/2003 alterou (conferido nas
publicações originais das duas emendas, arquivadas localmente — ver
`fontes/manifesto.yaml`):

| redação    | *caput* do § 1º                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------- |
| EC 20/1998 | "[...] calculados os seus proventos a partir dos valores fixados na forma **do § 3º**:"        |
| EC 41/2003 | "[...] calculados os seus proventos a partir dos valores fixados na forma **dos §§ 3º e 17**:" |

A mudança é da **base de cálculo dos proventos**. Nas três regras o efeito
gravado é proventos proporcionais — em `0028` e `0029` a citação está no
campo `fundamentacao_proporcional`. A emenda nomeada é, portanto, a que rege
o efeito que a regra produz, ainda que as palavras do inciso não tenham
mudado com ela.

No texto promulgado da EC 41/2003 isso aparece assim: o art. 1º reproduz o
*caput* do art. 40, o *caput* do § 1º e o inciso I, e então vem a linha de
reticências. Os incisos II e III estão sob ela — não porque sejam
irrelevantes, mas porque **seu texto não mudou**, e a técnica legislativa
reproduz apenas o que se altera. Ler a reticência como "a emenda não alcança
o inciso II" confunde texto com norma: o inciso passou a ser lido sob um
*caput* novo.

# Consequência prática

`okf/dispositivos/cf88/art-40-par-1-caput/` contém **apenas
`ec-103-2019.md`**. Das três redações que o *caput* do § 1º teve — EC
20/1998 (que o criou, junto com os incisos; o § 1º original tratava de lei
complementar e atividades penosas, insalubres ou perigosas), EC 41/2003 e EC
103/2019 — **duas não estão transcritas**, entre elas justamente a que estas
regras citam.

Por isso a citação não vira vínculo hoje, e a recusa é correta: o documento
que ela nomeia não existe. O que falta é transcrição, não decisão de mérito.

Note-se onde a pendência se endereça. O bundle separa *caput* e incisos em
diretórios distintos (`art-40-par-1-caput/` e `art-40-par-1-inc-ii/`), cada
um com suas próprias redações. Uma alteração que atinge o inciso **por via do
caput** não produz redação nova no diretório do inciso — e é por isso que
`cf88/art-40-par-1-inc-ii/ec-41-2003` não pode existir, embora a citação seja
boa. Quem procurar a pendência no endereço do inciso não a encontra; ela está
no do *caput*.

Nenhum vínculo é proposto e nenhum é removido. `regra-0028` e `regra-0029`
declaram quatro dispositivos cada e `regra-0027` seis; nenhum é o art. 40, §
1º — nem *caput*, nem inciso.

A linha de `regra-0028`/`0029` em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](../../../docs/analysis/pendencias-de-citacao-congeladas.md)
está como `REDACAO`, e **está certa quanto à natureza** — falta transcrever.
O que ela erra é o endereço: aponta para o inciso, e o que falta transcrever é
o *caput*. `regra-0027` não aparece na lista, porque sua citação está no
`nome`, campo que o leitor congelado não varria.

# Questão a investigar

1. **Transcrever as duas redações faltantes do *caput* do § 1º** (EC 20/1998 e
   EC 41/2003) e então conferir se estas três regras devem declarar o vínculo
   ao *caput* além do inciso. É a pendência concreta que este achado abre, e é
   fila `TRANSCREVER`.

2. **Se a citação deveria nomear as duas provisões.** "Art. 40, § 1º, II com
   redação dada pela EC 41/2003" é economia de linguagem jurídica corrente e
   não é erro; mas o catálogo, que endereça *caput* e inciso separadamente,
   só consegue representar a articulação completa vinculando os dois. Se isso
   pede algo do texto da fundamentação — campo deployável — é decisão de quem
   responde pelo produto, não da auditoria.

3. **A janela declarada atravessa a alteração seguinte.** As três têm
   `data_direito_apos: 31/12/2003`; a EC 88/2015 — que mudou o texto do
   próprio inciso II, acrescentando os setenta e cinco anos na forma de lei
   complementar — vigora desde 08/05/2015. A janela de `0028` e `0029` vai até
   31/12/2024 e a de `0027` até 03/12/2015. Nenhuma das três é regida por uma
   única redação do inciso ao longo da janela que declara. Isto é observação
   sobre os marcos gravados, não conclusão sobre a regra: fechá-la depende da
   semântica de `DATA_DIREITO_APOS`, ainda não confirmada (issue #39).
