---
type: Achado
id: achado-0045
nome: O único dispositivo vinculado por regra-0094 é uma redação cuja vida termina em 30/12/2003, um dia antes de a janela de direito da regra abrir — interseção vazia
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0094.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0094` declara um vínculo só,
`cf88/art-40-par-1-inc-iii-al-a/ec-20-1998`, e o declara corretamente: a
`fundamentacao_integral` cita "Artigo 40, §1º, inciso III, alínea 'a', da
Constituição Federal, **com redação dada pela Emenda Constitucional nº
20/1998**", e a alínea "a" é, de fato, redação da EC 20/1998.

O problema é de **qual documento** essa citação nomeia. O diretório
`cf88/art-40-par-1-inc-iii-al-a/` tem duas redações, e a alínea tem o mesmo
texto nas duas — o que as separa é a cadeia acima dela:

| documento    | vigência                    | por que existe                                         |
| ------------ | --------------------------- | ------------------------------------------------------ |
| `ec-20-1998` | 1998-12-16 → **2003-12-30** | criou a alínea                                         |
| `ec-41-2003` | **2003-12-31** → 2019-11-12 | a EC 41/2003 reescreveu o *caput* do art. 40 e do § 1º |

A janela de direito declarada pela `regra-0094` é
`[31/12/2003 , 31/12/2024]`. Ela abre no **dia seguinte** ao último dia do
documento vinculado. A interseção entre a vida da redação vinculada e a janela
da regra é **vazia** — em nenhum dia de vigência da regra o dispositivo que ela
vincula estava em vigor.

O documento que cobre a abertura da janela **existe e está autorado**:
`cf88/art-40-par-1-inc-iii-al-a/ec-41-2003`.

# Evidências

## Por que há duas redações de uma alínea que nunca mudou de texto

Um dispositivo é a unidade endereçada **com toda a cadeia que a contém**
([`docs/spec/dispositivo.md`](../../../docs/spec/dispositivo.md), "O corpo é a
cadeia legível até o dispositivo"), e alterar um ancestral cria redação nova.
A EC 41/2003 reescreveu o *caput* do art. 40 ("de caráter contributivo" → "de
caráter contributivo e solidário, mediante contribuição do respectivo ente
público, dos servidores ativos e inativos e dos pensionistas") **e** o *caput*
do § 1º ("calculados os seus proventos a partir dos valores fixados na forma
**do § 3º**" → "na forma **dos §§ 3º e 17**"), deixando os incisos II e III e as
alíneas do III sob linha de reticências.

Conferido no art. 1º da EC 41/2003, publicação do Planalto arquivada
localmente (`fontes-oficiais/arquivos/planalto-emc41.htm`, sha256
`af74d4331bb95caacbfffd2293e784e4365761c646f900c2a08b12bcb5bb518f`, no
`manifesto.yaml`; o arquivo é **cp1252**, não UTF-8). A reticência significa
"este texto não mudou", **não** "esta emenda não alcança este dispositivo" — e
foi por essa leitura que os dois documentos de `al-a` foram separados na
[varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md)
§3, que corrigiu exatamente as alíneas *a* e *b* deste inciso e autorou as
redações `ec-41-2003` faltantes.

Os `componentes` dos dois documentos registram isso com precisão. Em
`al-a/ec-41-2003`, o artigo e o § 1º são `redacao_dada_por: ec-41-2003`
(2003-12-31 →), enquanto o inciso III e a alínea *a* seguem
`redacao_dada_por: ec-20-1998` (1998-12-16 → 2019-11-12). **A alínea "a" é
redação da EC 20/1998 nos dois documentos**, que é por que a citação da regra
está certa e o vínculo, apesar disso, aponta para o documento errado: a prosa
fala no nível da alínea, o bundle endereça a cadeia.

## As duas datas, e por que não é questão de um dia de arredondamento

A abertura `data_direito_apos: 31/12/2003` não é acidental: **31/12/2003 é o
primeiro dia de vigência da EC 41/2003** (DOU de 31.12.2003; art. 11, "entra em
vigor na data de sua publicação"), e é o valor que `ec-41-2003/norma.md`
declara. É a convenção dominante do catálogo — o `achado-0015` conta 30
ocorrências de `data_direito_apos` gravando o dia de início da redação nesse
marco, e nenhuma gravando o dia anterior.

Sob qualquer das duas leituras de `DATA_DIREITO_APOS` que a Q1/issue #39 deixa
abertas, a conclusão é a mesma:

- se `APOS` é **exclusivo** (simétrico a `DATA_ADM_APOS`), a regra cobre de
  01/01/2004 em diante, e a redação vinculada morreu em 30/12/2003 — dois dias
  de distância;
- se `APOS` é **inclusivo**, a regra cobre de 31/12/2003, e a redação vinculada
  ainda assim já não existia — um dia de distância.

Não há leitura em que as duas se toquem. É o oposto do caso do `achado-0015`,
onde a divergência era de um dia **dentro** de uma fronteira; aqui a janela
inteira está fora.

## A mesma citação, resolvida de duas maneiras no catálogo

Seis regras vinculam `al-a/ec-20-1998`: `0039`, `0040`, `0089`, `0090`, `0093`
e `0094`. **Nenhuma** vincula `al-a/ec-41-2003`, embora o documento exista.
Duas dessas seis — `0089` e `0090` — gravam janela de direito
`[16/12/1998 , 31/12/2003)`, que é, ao dia, a vida da redação vinculada; nelas o
vínculo está certo. As outras quatro, incluindo esta, gravam janelas que
começam em ou depois de 31/12/2003.

Isso separa o defeito de uma hipótese concorrente: não é que o catálogo escolha
sempre a redação mais antiga por descuido sistemático — em duas das seis a
escolha é exata. O desencontro está onde a janela mudou e o vínculo não
acompanhou.

## `data_adm_ate: 31/12/2024` põe no eixo de admissão um prazo de outro eixo

Segundo desencontro entre janela e dispositivo, na dimensão da admissão. Só
seis das 112 regras gravam 31/12/2024 em `data_adm_ate`: `0093`, `0094`,
`0095`, `0096`, `0109` e `0110`. A data tem fonte única em todo o corpus — o
art. 4º da ECE 146/2021 —, e o que ela fixa lá é **prazo para cumprir os
requisitos**, não corte de ingresso (transcrito em
`ece-146-2021/art-4/original`, do PDF do SAPL/ALE-RO, sha256 `947726c7…`):

> [...] observará os requisitos e os critérios exigidos pela legislação vigente
> até a data de entrada em vigor desta Emenda Constitucional, **desde que sejam
> cumpridos até 31 de dezembro de 2024**, sendo assegurada a qualquer tempo.

A `regra-0094` já grava esse prazo no eixo próprio (`data_direito_ate: 31/12/2024`); repeti-lo em `data_adm_ate` afirma que a regra serve a quem
ingressou em 2024. Nenhum dispositivo citado o permite, e a alínea "a" exige 30
anos de contribuição (se mulher), o que torna a hipótese materialmente
impossível. O valor gravado é inócuo na prática e falso no registro. §3.3 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)
registra o mesmo defeito em `0109`/`0110`; o `achado-0043` o registra em
`0095`/`0096`.

# Consequência prática

O vínculo é o que o site e o relatório da PGE exibem, e é onde o procurador lê
o **texto integral** do dispositivo em que a regra se funda. Hoje ele lê o
art. 40 na redação "de caráter contributivo" e o § 1º remetendo "na forma do
§ 3º" — a redação que valia até 30/12/2003 —, enquanto a regra vale de
31/12/2003 em diante e a sua própria fundamentação cita, na mesma frase, os
§§ 3º **e 8º** na redação da EC 41/2003. O capítulo do relatório reimprime,
portanto, uma cadeia normativa que não é a da janela da regra.

O erro é **silencioso por construção**: o caminho confere, o vínculo resolve,
`check_vigencias` não acusa (ele só proíbe duas redações do mesmo dispositivo
em vigor ao mesmo tempo) e `check_p3_dispositivos` também não — nada no
repositório compara a janela de uma regra com a vigência da redação que ela
nomeia. É o mesmo modo de falha do `achado-0014`, com o sinal invertido: lá a
janela **extrapola** o fim da redação citada; aqui ela nem começa dentro dela.

Nada aqui afirma que o cálculo esteja errado. Os requisitos da alínea "a" — 55
anos de idade e 30 de contribuição, se mulher — são idênticos nas duas
redações, porque a alínea não mudou. O que muda é a cadeia, e é a cadeia que o
documento exibe.

# Questão a investigar

1. **Se o vínculo se troca por `al-a/ec-41-2003`.** É a correção mínima e não
   toca campo deployável nenhum: `dispositivos:` é anotação de auditoria, a
   citação da regra ("alínea 'a' com redação dada pela EC 20/1998") continua
   verdadeira no nível da alínea, e o documento de destino declara exatamente
   isso nos seus `componentes`. **Este achado não faz a troca**: escolher a
   redação de um vínculo é ato autoral, e há uma segunda hipótese abaixo que
   ela apagaria.

2. **Ou se a regra abrange dois períodos normativos e a fundamentação é que
   está incompleta.** A janela vai até 31/12/2024 e atravessa também a EC
   103/2019, que extinguiu a alínea "a" — de modo que nem `ec-41-2003`
   (termina em 2019-11-12) cobre a janela inteira. É a mesma disjunção do
   `achado-0014`, item 2, e ela não se fecha vinculando: se a regra agrega
   períodos sucessivos, o que falta é a citação do que sustenta o trecho de
   2019 em diante — e isso depende do item 3.

3. **O que sustenta a regra depois de 13/11/2019, e é conclusão jurídica que
   este achado não toma.** A alínea "a" foi extinta pela EC 103/2019 no plano
   federal, mas o art. 36, II daquela emenda condiciona, **para os regimes
   próprios dos Estados**, as revogações do seu art. 35 à "data de publicação
   de lei de iniciativa privativa do respectivo Poder Executivo que as
   referende integralmente". Qual lei estadual cumpre esse papel em Rondônia — e
   se a LCE 1.100/2021 o cumpre — é a pendência registrada na §5.2 e nas
   "quatro recusas" da
   [varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md),
   e é o que impede datar o fim dos dispositivos de transição no corpus. Nada
   nos itens 1 e 2 depende dessa resposta; o alcance de 2019 a 2024, sim.

4. **`data_adm_ate: 31/12/2024`.** Campo deployável, e a correção depende de
   saber qual é o corte de ingresso desta regra — que é a mesma pergunta do
   item 3 por outra porta: a alínea "a" não tem corte de ingresso próprio, e
   quem o traria é a legislação preservada pelo art. 4º da ECE 146/2021.
