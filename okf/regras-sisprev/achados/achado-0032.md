---
type: Achado
id: achado-0032
nome: As quatro regras do art. 5º, § 6º, II da ECE 146/2021 não gravam o corte de ingresso do caput — duas gravam sentinela e duas gravam a data do ato em vez da data de vigência
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0055.md
  - /regras/regra-0056.md
  - /regras/regra-0057.md
  - /regras/regra-0058.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O *caput* do art. 5º da ECE 146/2021 abre a regra de transição **só** para quem
"tenha ingressado no serviço público em cargo efetivo **até a data de entrada
em vigor desta Emenda Constitucional**". É condição da regra inteira: os §§ 6º
e 7º, que as quatro regras citam e vinculam, dizem "as aposentadorias
concedidas nos termos do disposto **neste artigo**".

Nenhuma das quatro regras do § 6º, II grava esse corte:

| regra                       | `data_adm_apos` | `data_adm_ate` |
| --------------------------- | --------------- | -------------- |
| `regra-0055` / `regra-0056` | 01/01/1950      | **31/12/2099** |
| `regra-0057` / `regra-0058` | 01/01/2004      | **09/09/2021** |

`31/12/2099` é sentinela e o catálogo não a interpreta (P5) — na prática não
fecha janela nenhuma. `09/09/2021` é uma data real da norma, mas **não é a da
entrada em vigor**.

O piso de admissão de `regra-0057`/`0058` é objeto de achado próprio
(`achado-0033`); aqui trata-se só do teto.

# Evidências

Conferido na **publicação oficial** da Emenda arquivada localmente
(`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, SAPL/ALE-RO, registrada no
`manifesto.yaml`). O PDF é digitalização sem camada de texto — `pdftotext`
devolve 10 bytes —, então a leitura foi **visual**, página a página.

Três trechos, todos verbatim da publicação:

- **Título** (p. 1): "EMENDA CONSTITUCIONAL Nº 146, **DE 9 DE SETEMBRO DE
  2021**".
- **Art. 5º, *caput*** (p. 4): "O servidor público que tenha ingressado no
  serviço público em cargo efetivo **até a data de entrada em vigor desta
  Emenda Constitucional** e que não seja abrangido pelo § 16 do art. 40 da
  Constituição Federal, poderá aposentar-se voluntariamente quando preencher,
  cumulativamente, os seguintes requisitos:".
- **Art. 13** (p. 10): "Esta Emenda à Constituição **entra em vigor na data de
  sua publicação**." Logo abaixo: "ASSEMBLEIA LEGISLATIVA, 9 de setembro de
  2021".

Daí a conclusão, e ela é estreita: **09/09/2021 é a data do ato — a que o
próprio título da Emenda carrega — e o art. 13 amarra a entrada em vigor à
data da *publicação*, que é outra coisa.** O corpus dá essa publicação como
**14/09/2021** (`ece-146-2021/norma.md`, `vigencia_inicio: 2021-09-14`), e é
esse o valor que `regra-0047`/`0048` (o par gêmeo do art. 6º, § 2º, II) e
`regra-0068`–`0070` (art. 8º) gravam em `data_adm_ate`. O catálogo, portanto,
já usa a data de publicação em outras cinco regras da mesma Emenda.

## Isto reclassifica o E8 do RFC 0001

O E8 (RFC 0001, tabela de erros da importação) registra `09/09/2021` em
`regra-0057`/`0058` como "divergência a conferir jurídica/documentalmente,
**não erro de digitação presumido**", e a
[semântica das janelas](../../../docs/analysis/semantica-das-janelas-temporais.md)
§5.2.05 pergunta "erro do dia, ou marco próprio?". A recusa em presumir
digitação estava certa: **é marco próprio**. Só não é o marco que o *caput*
exige. Um valor que veio do título da norma não é lapso de teclado — é leitura
de qual das duas datas da Emenda o requisito nomeia.

Este achado **não** alcança `14/06/2021` de `regra-0049`/`0050`, o outro caso
do E8: nada na publicação lida corresponde a junho de 2021, e essas duas regras
não foram conferidas aqui.

## O limite desta conferência, declarado

A data de **publicação** não está na publicação promulgada que eu li — o PDF do
SAPL traz o texto promulgado, não a folha do Diário Oficial. `14/09/2021` vem
do registro do SAPL da norma, do modo como
[a varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md)
§4.4 já o classificou (**[V parcial]**). Portanto: que `09/09/2021` **não** é a
data de entrada em vigor está provado pelo art. 13 combinado com o título (a
publicação não pode preceder o ato); que a data correta seja exatamente
`14/09/2021` depende do registro do SAPL, não de conferência no DOE.

# Consequência prática

`DATA_ADM_ATE` é campo **deployável**: chega ao Sisprev e decide quem a regra
alcança. Os dois desvios têm efeitos opostos, e nenhum é neutro.

**`31/12/2099` em `regra-0055`/`0056`** alcança quem ingressou **depois** de a
Emenda entrar em vigor — exatamente quem o *caput* do art. 5º exclui, e para
quem a Emenda escreveu outra regra (o regime permanente do art. 250 da
Constituição Estadual, na redação que o art. 1º desta mesma Emenda lhe deu).
Uma regra de transição sem teto de ingresso deixa de ser transição.

**`09/09/2021` em `regra-0057`/`0058`** faz o oposto: exclui o professor que
ingressou entre 10 e 14 de setembro de 2021 e que o *caput* alcança. São cinco
dias de servidores que a regra deveria cobrir e não cobre — e, como o par
gêmeo não-magistério (`0055`/`0056`) não tem teto nenhum, o mesmo ingresso é
tratado de duas formas incompatíveis dentro do mesmo inciso.

# Questão a investigar

1. **Se `data_adm_ate` das quatro deve passar a `14/09/2021`.** É a leitura mais
   simples e a que as cinco outras regras da mesma Emenda já praticam. Depende
   de fechar a data de publicação (item 2) e é alteração de campo deployável,
   logo decisão de quem responde por ele — sob a RFC 0006 o veículo indicado é
   um `Conjunto` `proposto`, não edição in-place.

2. **Qual é a data de publicação da ECE 146/2021 no Diário Oficial.** Fecha ao
   mesmo tempo este achado, o `vigencia_inicio` da norma (hoje autorado sem
   conferência no DOE) e o item 5.2.05 da semântica das janelas.

3. **Se `31/12/2099` em `regra-0055`/`0056` é sentinela por descuido ou por
   decisão.** Há uma leitura em que o teto foi omitido de propósito: o § 6º, II
   define sua clientela por complemento ("para o servidor público **não
   contemplado no inciso I do § 6º**"), e esse complemento não é só temporal —
   alcança também quem ingressou antes de 2004 mas não atingiu a idade de
   62/65 anos que o inciso I exige para a integralidade, e quem fez a opção do
   § 16 do art. 40 da CF. Nada disso, porém, dispensa o teto do *caput*: o
   complemento é interno ao art. 5º, e o art. 5º inteiro só alcança quem
   ingressou até a vigência da Emenda.

4. **Se `09/09/2021` aparece em outros campos do catálogo.** Se a leitura "data
   do título" foi usada mais de uma vez, o conserto é de convenção e não de
   duas células. A varredura da semântica das janelas encontrou a data apenas
   nestas duas regras, mas varreu só os quatro campos de data.
