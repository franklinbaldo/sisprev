---
type: Achado
id: achado-0044
nome: A fundamentação de regra-0094 cita quatro provisões e dispositivos declara uma; o art. 4º da Emenda à Constituição Estadual não é vinculado porque o campo não numera a emenda, ainda que o nome e a data gravada a identifiquem
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0094.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

A `fundamentacao_integral` de `regra-0094` é, na íntegra:

> Artigo 40, §1º, inciso III, alínea "a", da Constituição Federal, com redação
> dada pela Emenda Constitucional nº 20/1998 **e artigo 40, §§ 3º e 8º com
> redação dada pela Emenda Constitucional nº 41/2003**, **art. 4° da Emenda à
> Constituição Estadual** - CF

São **quatro** provisões citadas — a alínea "a", o § 3º, o § 8º e o art. 4º de
uma emenda estadual. `dispositivos:` declara **uma**:
`cf88/art-40-par-1-inc-iii-al-a/ec-20-1998`. A `regra-0094` está entre as dez
regras com um vínculo só — e a lacuna tem **três causas distintas**, não uma,
que é o que este achado separa.

# Evidências

## As três provisões sem vínculo, uma a uma

| provisão citada       | documento no bundle                     | por que não está vinculada             |
| --------------------- | --------------------------------------- | -------------------------------------- |
| art. 40, § 3º (EC 41) | **não autorado**                        | falta transcrição                      |
| art. 40, § 8º (EC 41) | `cf88/art-40-par-8/ec-41-2003` (existe) | norma dona não nomeada — `achado-0011` |
| art. 4º da ECE        | `ece-146-2021/art-4/original` (existe)  | emenda estadual citada **sem número**  |

A segunda linha é exatamente o objeto do
[`achado-0011`](achado-0011.md): a oração nomeia só a emenda **alteradora**
(EC 41/2003) e nunca a norma **dona** dos parágrafos (a Constituição
Federal), e por isso o vínculo é recusado em vez de inferido. Aquele achado
alcança `regra-0039` e `regra-0093` — e **não** `regra-0094`, cuja
`fundamentacao_integral` é **idêntica caractere a caractere** à da `regra-0093`
(246 caracteres, sha256 `8944204766c5…` nas duas). É o mesmo modo de falha que
a primeira versão do `achado-0016` cometeu: alcançar uma metade do par e perder
a outra, porque a divergência é só `sexo`. Este achado registra a extensão;
o raciocínio do `achado-0011` já a cobria.

## O art. 4º é identificável, e por três vias independentes

A terceira linha é o achado próprio. A fundamentação escreve "art. 4° da
Emenda à Constituição Estadual" — sem número, sem ano. Uma citação sem norma
identificada não se vincula, e a lista congelada classifica corretamente a
`regra-0094` como `LEITURA-HUMANA`, `sem_norma (3×)`
([`pendencias-de-citacao-congeladas.md`](../../../docs/analysis/pendencias-de-citacao-congeladas.md)).

Só que aqui a norma **é** determinável, e sem inferir nada da prosa:

1. **O `nome` da própria regra a numera**: `Voluntária por Tempo de Contribuição - Art. 40, §1º, III, "a" da CF c/c art. 4º da EC 146/21`.
2. **A regra grava a data que só aquele artigo fixa.** `data_direito_ate: 31/12/2024`, e o art. 4º da ECE 146/2021 é o **único dispositivo de todo o
   corpus** que fixa 31/12/2024 (registrado em §5.1 da
   [lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)).
   Conferido em `ece-146-2021/art-4/original`, transcrito do PDF do SAPL/ALE-RO
   (sha256 `947726c79d3a934512908451efd0646f199687da3033fcde782abf7c76a550bf`,
   no `manifesto.yaml`): "desde que sejam cumpridos **até 31 de dezembro de
   2024**, sendo assegurada a qualquer tempo".
3. **As irmãs da mesma família escrevem a mesma citação com o número, e a
   vinculam.** `regra-0039` e `regra-0040` — o magistério da mesma transição da
   alínea "a" — dizem "no artigo 4º da **Emenda Constitucional Estadual nº
   146/2021**" e declaram `/dispositivos/ece-146-2021/art-4/original.md`.
   Varrido o catálogo inteiro: **26** regras citam o art. 4º dessa emenda em
   campo de fundamentação; **24** o numeram e **as 24 o vinculam**. As duas que
   não numeram são `0093` e `0094`, e são exatamente as duas que não vinculam.
   A correlação é perfeita e num só sentido — não há regra que numere e não
   vincule, nem regra que vincule sem numerar.

Ou seja: a lacuna não é de identificação da norma, é de **grafia do campo**. A
diferença com a segunda linha da tabela importa — no § 8º a norma dona
simplesmente não aparece em lugar nenhum do registro; no art. 4º ela aparece
duas vezes, só não no campo que conta.

## Relação com o `achado-0047`, e uma correção de classificação

O [`achado-0047`](achado-0047.md), autorado na mesma rodada, alcança a
`regra-0094` pelo outro lado do mesmo campo: ele registra que a regra grava
`data_direito_ate: 31/12/2024` sem que nenhum campo de fundamentação cite a ECE
146/2021. Os dois achados são compatíveis e complementares — aquele olha a
janela gravada e conclui pela falta da citação; este olha a citação e conclui
pela falta do vínculo.

Uma correção pontual, e é sobre grau, não sobre a conclusão: aquele achado
coloca a `regra-0093` e a `regra-0094` no grupo das que citam a emenda "no
`nome`, e só nele". Não é exato. A `fundamentacao_integral` das duas **cita o
artigo** — "art. 4° da Emenda à Constituição Estadual" —, só não numera a
emenda; a busca por "146" nos campos de texto não as encontra, e é dela que a
classificação saiu. A diferença importa para a correção: nas outras seis daquele
grupo há uma citação a **acrescentar**, e aqui há uma citação a **completar**.
A conclusão do `achado-0047` — que a norma não está identificada em campo de
fundamentação — permanece verdadeira nas duas leituras.

## O § 3º é fila de transcrição, e é a única das três que destrava sozinha

`cf88/art-40-par-3` não existe no bundle em redação nenhuma. A da EC 41/2003
está conferida na publicação do Planalto arquivada localmente
(`fontes-oficiais/arquivos/planalto-emc41.htm`, sha256 `af74d4331bb9…`):

> § 3º Para o cálculo dos proventos de aposentadoria, por ocasião da sua
> concessão, serão consideradas as remunerações utilizadas como base para as
> contribuições do servidor aos regimes de previdência de que tratam este
> artigo e o art. 201, na forma da lei.

É o dispositivo que funda `tipo_calculo: Valor Médio` na regra — a média das
remunerações de contribuição, em oposição à totalidade da remuneração do cargo.
**Transcrevê-lo não basta para vincular**, porque a citação continua sem norma
dona nomeada (é a mesma oração do § 8º). Fica registrado como fila
`TRANSCREVER` nova, não coberta pela lista congelada, que para a `regra-0094`
só registrou `sem_norma`.

# Consequência prática

O art. 4º da ECE 146/2021 é o dispositivo que **mantém a regra viva**: é ele
que assegura, "a qualquer tempo", a aposentadoria pelos requisitos da
legislação anterior à EC 146/2021, desde que cumpridos até 31/12/2024. Sem
ele, uma regra fundada na alínea "a" do art. 40, § 1º, III — provisão que a EC
103/2019 extinguiu — não tem como alcançar requerimento nenhum apresentado
hoje. Ele é, portanto, a provisão de que depende a aplicabilidade presente da
regra, e é a que não está vinculada.

O efeito é sobre o **rastro de auditoria**, não sobre o cálculo: quem abre a
ficha da `regra-0094` no site, ou a lê no relatório da PGE, vê um único
dispositivo, que é o da alínea revogada, e não vê o que sustenta a regra hoje.
`FUNDAMENTACAO_INTEGRAL` também é o texto entregue ao servidor, e ali a emenda
estadual aparece sem número — o servidor não tem como localizá-la.

# Questão a investigar

1. **Se a grafia do campo se corrige.** Acrescentar "nº 146/2021" à
   fundamentação alinha a `regra-0094` (e a `0093`) às 24 irmãs e destrava o
   vínculo. Mas `FUNDAMENTACAO*` é campo **deployável**: é alteração de
   produto, não de auditoria, e depende de quem responde por ele. A hipótese
   alternativa — a de que a citação aponta para outra emenda à Constituição
   Estadual — não está descartada por leitura de campo; o que a torna
   improvável é o `nome` e a data gravada, não o texto.

2. **Se o vínculo pode ser declarado antes disso.** O `achado-0011` já deixa a
   mesma pergunta aberta na hipótese 2 dele ("convenção de redação — o vínculo
   é declarado à mão, com este achado como justificativa"). Aqui a base para
   declarar é mais forte que lá, porque a norma está numerada no `nome` da
   própria regra. **Este achado não declara o vínculo**: fazê-lo é decidir que
   o `nome` supre a fundamentação, e essa é a decisão que a RFC 0008 reserva a
   ato humano explícito, não a um efeito colateral de conferência.

3. **A transcrição do art. 40, § 3º.** Ela é útil independentemente da
   decisão acima — outras regras citam os §§ 3º/17 como base de cálculo —, mas
   não fecha nada aqui por si só.
