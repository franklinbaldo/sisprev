---
type: Achado
id: achado-0028
nome: regra-0037 e regra-0038 seguem o trilho de cálculo de quem ingressou após 31/12/2003 e não gravam esse corte — com as gêmeas 0035/0036 elas cobrem duas vezes quem ingressou antes
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0037.md
  - /regras/regra-0038.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0037` (`sexo: MASCULINO`) e `regra-0038` (`sexo: FEMININO`) são a
aposentadoria voluntária comum do regime permanente da LCE 1.100/2021 pelo
**trilho da média**: vinculam e citam `lce-1100-2021/art-24` e
`lce-1100-2021/art-27-inc-ii`, gravam `tipo_calculo: Valor Médio` e
`paridade: N`.

Os dois dispositivos que elas citam delimitam a sua clientela pela **mesma**
cláusula literal: servidor "que tenha ingressado no serviço público em cargo
efetivo **após 31 de dezembro de 2003**". As duas regras gravam
`data_adm_apos: 01/01/1910` e `data_adm_ate: 31/12/2099` — **corte nenhum, nos
dois eixos**.

O par imediatamente anterior, `regra-0035`/`regra-0036`, é a mesma regra pelo
**trilho da integralidade** (`art-25` + `art-27-inc-i`, "até 31 de dezembro de
2003") e grava `data_adm_ate: 31/12/2003`. Os dois pares deveriam **particionar**
a população por data de ingresso, e não particionam: quem ingressou até
31/12/2003 é alcançado pelos quatro registros.

# Evidências

## O corte está no texto dos dois dispositivos citados, verbatim

Conferido na compilação oficial da DITEL arquivada localmente
(`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`, sha256
`bcac2238…`, `manifesto.yaml`) — não no texto transcrito no corpus, embora os
dois coincidam:

> **Art. 24.** No cálculo dos proventos de aposentadoria dos servidores
> titulares de cargo efetivo que tenham ingressado no serviço público em cargo
> efetivo **após 31 de dezembro de 2003** e que não tenham feito a opção de que
> trata o § 16 do art. 40 da Constituição Federal [...] será considerada a
> média aritmética simples das maiores remunerações [...] correspondentes a 80%
> [...]

> **Art. 27.** [...] **II** - nos termos estabelecidos para o RGPS, para as
> aposentadorias concedidas a servidor público que tenha ingressado no serviço
> público em cargo efetivo **após 31 de dezembro de 2003** [...]

E o complemento, que é o que `0035`/`0036` citam:

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**
> [...] corresponderá à totalidade da remuneração no cargo efetivo [...]

Os dois trilhos são, portanto, **um par complementar de coortes de ingresso**,
e não apenas dois modos de calcular: escolher o trilho decide de uma vez
`tipo_calculo`, `paridade` **e** a janela de admissão. É a articulação que a
[conferência do grupo LCE 1.100/2021](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-regime-novo.md)
§1.1 descreve, e este achado é o caso `0037`/`0038` da sua tabela de §5.1.

## O próprio catálogo sabe escrever o corte complementar, para este mesmo trilho

`regra-0080` e `regra-0081` (voluntária de policial, LCE 1.100/2021) seguem o
**mesmo** trilho `art-24` + `art-27-inc-ii` e gravam
`data_adm_apos: 31/12/2003`; as suas gêmeas de integralidade, `0082`/`0083`,
gravam `data_adm_ate: 31/12/2003`. As quatro particionam a população
exatamente na convenção `ATE_anterior = APOS_seguinte` confirmada em
[`semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md)
§1.1 (`ate = M` seguido de `apos = M` particiona sem buraco nem sobreposição,
porque `ATE` é inclusivo e `APOS` exclusivo).

Ou seja: o valor que falta em `0037`/`0038` existe no catálogo, no mesmo campo,
para o mesmo trilho, a seis linhas de distância. A comparação é **interna ao
grupo**, não uma interpretação da sentinela.

## O que não se afirma sobre `01/01/1910`

`01/01/1910` e `31/12/2099` são **sentinelas não interpretadas** (P5). Este
achado não as lê como "sem limite": lê apenas que **não são o marco
31/12/2003** que os dois dispositivos citados declaram, e que a regra irmã de
trilho complementar grava esse marco.

Vale, ainda assim, registrar o que a contagem mostra sobre `01/01/1910`, porque
ela reduz o espaço de hipóteses. O valor aparece em 20 das 112 regras, e
**dezoito delas são de regimes encerrados** — ciclos 1º, 2º e 4º, com
`data_adm_ate` em 15/12/1998, 16/12/1998 ou 31/12/2003. `regra-0037` e
`regra-0038` são as **únicas duas de 3º ciclo** a usá-lo, e as únicas em que
ele se combina com `data_adm_ate: 31/12/2099`. As demais regras do grupo LCE
1.100/2021 usam `01/01/1950` como piso — inclusive as gêmeas `0035`/`0036`.
Não concluo o que a troca significa; registro que ela isola este par.

# Consequência prática

Um servidor admitido, digamos, em 1999 satisfaz a janela de admissão dos
**quatro** registros: `0035`/`0036` (integralidade, com paridade) e
`0037`/`0038` (média, sem paridade). Os quatro são `simulavel: S`, têm o
**mesmo `nome`** ([`achado-0029`](achado-0029.md)) e o motor não lê
fundamentação — de modo que, para esse servidor, nada no cadastro indica que
`0037`/`0038` são a regra de quem ingressou **depois** dele.

A diferença entre os dois resultados não é marginal: totalidade da remuneração
do cargo com reajuste pelo art. 7º da EC 41/2003, contra média de 80% do
período contributivo com reajuste do RGPS.

`DATA_ADM_APOS` é campo **deployável**. Preenchê-lo é alterar o produto, e há
duas saídas opostas: gravar `31/12/2003` no eixo `APOS` de `0037`/`0038`
(alinhando-as ao trilho que citam e às `0080`/`0081`), ou concluir que a
ausência de corte é deliberada — e nesse caso é a **fundamentação** que está
errada, porque cita dois dispositivos que excluem metade da população que a
regra alcança. Escolher é de quem responde pelo campo.

**Nenhum vínculo é proposto.** `dispositivos:` de `0037` e `0038` espelha
exatamente o que os campos de fundamentação citam — conferido campo a campo, os
quatro vínculos (`cf88/art-40-par-1-inc-iii/ec-103-2019`, `art-24`,
`art-27-inc-ii`, `art-32`) são citados e nada citado deixa de ser vinculado. O
defeito está no valor gravado, não no link.

# Questão a investigar

1. **Se o corte é `31/12/2003` no eixo `APOS` ou se as duas regras agregam as
   duas coortes.** A primeira leitura é a que o texto dos dispositivos sustenta
   e a que `0080`/`0081` implementam. A segunda exigiria explicar por que a
   fundamentação nomeia justamente os dois artigos que excluem quem ingressou
   antes de 2004.

2. **A opção do § 16 do art. 40 da CF não tem coluna.** Tanto o art. 24 quanto
   o art. 25 exigem, além da data, que o servidor **não** tenha optado pela
   previdência complementar — e nada no Sisprev registra essa opção. Mesmo com
   a data corrigida, uma parte da separação entre os dois trilhos continua sem
   suporte no cadastro. É a mesma família da Q6: critério real que nenhuma
   coluna carrega.

3. **Se as outras treze regras da tabela de §5.1 da conferência do grupo têm a
   mesma causa.** Onze regras de trilho `25`+`27-I` sem corte gravado e a
   `regra-0071` com o corte **invertido** compõem o resto do padrão. Estão fora
   do conjunto deste achado; a hipótese de origem única (um lote preenchido sem
   o eixo de admissão) é econômica e não verificada.
