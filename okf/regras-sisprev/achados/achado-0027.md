---
type: Achado
id: achado-0027
nome: regra-0049 e regra-0050 gravam data_adm_ate 14/06/2021, três meses antes de qualquer data que a ECE 146/2021 traga na própria face
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0049.md
  - /regras/regra-0050.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0049` (`sexo: MASCULINO`) e `regra-0050` (`sexo: FEMININO`) são o par de
magistério da transição do **art. 6º da ECE 146/2021** e gravam
`data_adm_ate: 14/06/2021`.

O *caput* do art. 6º condiciona o benefício a ter o servidor "ingressado em
cargo efetivo **até a data de entrada em vigor desta Emenda Constitucional**".
`data_adm_ate` é o eixo de ingresso, e é inclusivo (Q1, confirmada) — logo o
valor gravado deveria ser essa data.

**14/06/2021 não é ela, sob nenhuma das duas leituras que a própria Emenda
admite**, e não é `vigencia_*` de norma nenhuma do corpus. As gêmeas
não-magistério do mesmo inciso — `regra-0047` e `regra-0048`, idênticas a estas
em tudo menos `apos_especial` e o `§ 1º` do art. 6º — gravam `14/09/2021`.

# Evidências

## O corte é a entrada em vigor da Emenda, e a Emenda diz duas coisas sobre ela

Conferido por **leitura visual** do PDF oficial da ALE-RO arquivado localmente
(`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256 `947726c7…`,
`manifesto.yaml`). O arquivo é digitalização sem camada de texto — `pdftotext`
extrai 10 caracteres —, então **`grep` vazio aqui não é prova de ausência** e a
conferência foi feita renderizando as páginas em imagem. As duas páginas que
importam:

- **p. 7, *caput* do art. 6º** (verbatim): "Art. 6º O servidor público que
  tenha ingressado em cargo efetivo **até a data de entrada em vigor desta
  Emenda Constitucional** poderá aposentar-se voluntariamente quando preencher,
  cumulativamente, os seguintes requisitos:"
- **p. 10, art. 13 e encerramento**: "Art. 13. Esta Emenda à Constituição
  **entra em vigor na data de sua publicação**." — seguido de "ASSEMBLEIA
  LEGISLATIVA, **9 de setembro de 2021**".

Isto dá duas datas candidatas, e nenhuma é junho:

| candidata      | de onde vem                                                             | quem a grava no catálogo                    |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| **14/09/2021** | `vigencia_inicio` declarada em `okf/dispositivos/ece-146-2021/norma.md` | `0047`, `0048`, `0068`, `0069`, `0070` (5×) |
| **09/09/2021** | data lavrada na própria Emenda (p. 10)                                  | `0057`, `0058` (2×)                         |

O art. 13 remete à **publicação**, que não está arquivada: o PDF prova a data
de lavratura (09/09), não a de publicação. Qual das duas é a correta é decisão
que este achado **não** toma — e não precisa tomar, porque a conclusão não
depende dela: **14/06/2021 não é nenhuma das duas**, nem é `vigencia_inicio` ou
`vigencia_fim` de qualquer norma ou dispositivo do corpus.

## O valor é, no catálogo inteiro, um par de duas linhas

Contagem sobre as 112 regras, campo `DATA_ADM_ATE`:

| valor      | ocorrências | o que é                                      |
| ---------- | ----------- | -------------------------------------------- |
| 14/09/2021 | 5           | vigência declarada da ECE 146/2021           |
| 09/09/2021 | 2           | data lavrada na ECE 146/2021 (`0057`/`0058`) |
| 14/06/2021 | **2**       | **`regra-0049` e `regra-0050`, e mais nada** |

As duas ocorrências são exatamente este par. O dia (**14**) coincide com o da
vigência declarada e o **mês** não; a hipótese mais econômica é erro de
digitação do mês em `14/09/2021` — o valor das gêmeas diretas. É hipótese, e a
conferência não a converte em conclusão: `DATA_ADM_ATE` é campo **deployável**.

# Consequência prática

Sob `ATE` inclusivo, `regra-0049`/`0050` alcançam quem ingressou até
14/06/2021 e **não** alcançam quem ingressou entre 15/06/2021 e a entrada em
vigor da Emenda — uma janela de cerca de três meses que o *caput* do art. 6º
inclui expressamente.

O efeito é assimétrico dentro da mesma transição e recai justamente sobre a
classe que o § 1º do art. 6º pretende favorecer: o professor admitido em, por
exemplo, agosto de 2021 é alcançado por `regra-0047`/`0048` (a regra **comum**
do mesmo inciso II, `data_adm_ate: 14/09/2021`) e perde a redução de cinco anos
de idade e de tempo de contribuição que o § 1º lhe dá, porque a regra de
magistério correspondente se fecha antes dele. As duas são `simulavel: S`, e
`data_adm_ate` é coluna — então este é um dos poucos casos deste lote em que a
divergência de fato alcança a seleção automática, e não só o texto entregue.

Nada aqui afirma o que o motor faz com o campo: a leitura inclusiva de `ATE`
está confirmada como **semântica de preenchimento** (Q1), não como
comportamento do Sisprev — a mesma ressalva do
[`achado-0015`](achado-0015.md).

# Questão a investigar

1. **Qual data de entrada em vigor o catálogo adota.** Antes de corrigir
   `0049`/`0050` é preciso decidir entre 14/09/2021 (o que o corpus declara e o
   que 5 regras gravam) e 09/09/2021 (o que a Emenda traz na face e o que
   `0057`/`0058` gravam). Corrigir junho para setembro sem fechar essa questão
   troca um erro de três meses por um de cinco dias. O que destrava é a
   **publicação oficial** da Emenda no Diário Oficial do Estado, ausente de
   `fontes-oficiais/` — `PENDENCIAS.md` já registra a ECE 146/2021 como a
   pendência de coleta mais custosa do corpus, por outro motivo (falta de
   camada de texto).

2. **Se `0057`/`0058` são a mesma anomalia ou outra.** A
   [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
   §5.4 tratou `09/09/2021` e `14/06/2021` como duas datas igualmente sem
   fonte. A leitura do PDF desfaz metade disso: **09/09/2021 tem fonte** — é a
   data lavrada na Emenda. Só `14/06/2021` continua sem nenhuma. `0057`/`0058`
   estão fora do conjunto deste achado e a observação fica registrada para
   quem os conferir.

3. **Se o par deve gravar o corte do *caput* ou o do § 2º, II.** `0049`/`0050`
   seguem o trilho do inciso II do § 2º, cuja clientela é definida por
   complemento ("para o servidor público **não contemplado no inciso I**"), não
   por data. O corte de ingresso que resta aplicável é o do *caput*, e é o que
   `0047`/`0048` gravam. Mas o complemento do inciso I inclui também **não ter
   feito a opção do § 16 do art. 40 da CF**, que não tem coluna no Sisprev —
   de modo que a janela de admissão sozinha nunca separa as duas clientelas
   (mesma lacuna registrada em §5.3 da conferência do lote). Corrigir a data
   não fecha essa segunda metade.
