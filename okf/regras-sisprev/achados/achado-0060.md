---
type: Achado
id: achado-0060
nome: A redação original do § 10 do art. 45 da LCE 432/2008 foi transcrita com vigência atravessando a alteração do próprio caput
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0027.md
  - /regras/regra-0028.md
  - /regras/regra-0029.md
  - /regras/regra-0032.md
  - /regras/regra-0039.md
  - /regras/regra-0040.md
detectado_em: 2026-08-03
detectado_por: franklinbaldo
---

# Descrição

O documento `lce-432-2008/art-45-par-10/original` declarava vigência de
13/03/2008 a 18/10/2021 — a data da revogação da LCE 432/2008 pela LCE
1.100/2021. A LCE 672/2012, porém, deu nova redação ao **caput** do art. 45 em
09/08/2012, e o caput é ancestral do § 10.

A spec de dispositivo é expressa quanto à consequência: a vida de uma redação
termina na primeira alteração de **qualquer** nível da sua cadeia, e um nível
interno cujo texto não mudou, sob ancestral novo, é redação nova. A vigência
declarada atravessava essa fronteira, e por isso afirmava que o § 10 esteve em
vigor, na redação original, durante nove anos em que o artigo que o contém já
tinha outra redação. Nenhum documento com esse conteúdo esteve em vigor.

O defeito é o modo de falha que a própria spec descreve como silencioso: o
parágrafo é verbatim, o caminho confere, o vínculo resolve, e nenhum gate
acusa — `check_vigencias` só compara datas **dentro de um diretório**, e a
alteração que importa aconteceu no diretório do irmão.

# Evidências

A LC 432 compilada da Casa Civil, fonte já citada pelo próprio documento,
imprime no caput do art. 45 a nota `(Redação dada pela Lei Complementar n. 672, de 9/08/2012)`. O § 10 não traz nota de alteração; a compilação marca alteração
parágrafo a parágrafo, como se lê no § 12, `(Incluído pela Lei Complementar n. 672, de 9/08/2012)`. A LCE 672/2012, portanto, não reescreveu o § 10 — e é
exatamente por isso que o caso é o da cadeia, não o do texto.

O sinal estava dentro do bundle e não foi lido: o irmão
`lce-432-2008/art-45/original` já declarava `vigencia_fim: 2012-08-08`, e o
`lce-432-2008/art-45/lce-672-2012` já ocupava o segmento seguinte. O § 10
discordava do próprio artigo que o contém, no mesmo bundle, no mesmo commit.

A transcrição também omitia a vírgula que a fonte tem em `Os proventos, calculados de acordo com o caput`.

O defeito só apareceu na integração de duas frentes de auditoria que
transcreveram o mesmo parágrafo sem se ver: uma autorou a redação original com
a vigência longa, a outra autorou a redação da LCE 672/2012 a partir de
09/08/2012. Quando os dois documentos passaram a existir no mesmo bundle,
`P3_VIGENCIA_SOBREPOSTA` acusou — não a vigência longa em si, mas a
sobreposição. Sem a segunda frente, o defeito seguiria mudo.

# Consequência

As oito regras nomeadas vinculam a cadeia do art. 45 da LCE 432/2008 e têm o
cálculo governado pela média dessa lei, cujo teto é o § 10. Nenhum campo
deployável de nenhuma delas está errado por causa deste defeito, e é por isso
que o achado é `informativo`: o que estava errado era a datação de um documento
do bundle de dispositivos, não o produto.

O que o defeito produzia era pior de outro jeito — um leitor que montasse a
cadeia do § 10 para uma data entre 09/08/2012 e 18/10/2021 receberia o caput
antigo com o parágrafo, isto é, texto que nunca esteve em vigor junto, com
aparência de conferido. O relatório da PGE reimprime o texto integral de cada
dispositivo citado dentro do capítulo de cada regra; num anexo assinado, essa
montagem circularia como transcrição oficial.

A vigência e a vírgula foram corrigidas no mesmo commit que integrou as duas
frentes. Este achado registra que o defeito existiu, porque corrigir não
registra: quem lê o documento hoje encontra a data certa e não descobre que ela
esteve errada, nem por quanto tempo, nem que nenhum gate a pegou.

# Limites

Este achado não afirma que outras redações do bundle tenham o mesmo defeito. A
conferência que o encontrou foi pontual, provocada por uma sobreposição, e não
uma varredura da cadeia de todos os dispositivos transcritos.

Também não afirma que o gate deva passar a derivar a cadeia sozinho. Montar a
cadeia é leitura jurídica e curadoria manual por contrato da spec; a pergunta
aberta é se existe invariante **conferível** — recomputar e comparar, o idioma
do `_check_caminho` — que não decida nada pelo autor.

# Questão a investigar

1. Quantas outras redações declaram vigência que atravessa a alteração de um
   ancestral? A varredura é mecânica sobre os `componentes` já declarados e não
   depende de ancestral autorado.
2. Cabe um detector que compare a vigência de um documento com a dos
   documentos do mesmo nível superior, acusando travessia sem concluir qual das
   duas datas está errada?
3. A convenção de datar o fim pela revogação da norma (`2021-10-18`) foi
   aplicada a outros dispositivos cujo ancestral mudou antes disso?
