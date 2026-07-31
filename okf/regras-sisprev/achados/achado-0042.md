---
type: Achado
id: achado-0042
nome: regras 0065–0067 e 0071 gravam janelas incompatíveis com os arts. 24/25 e 27 da LCE 1.100/2021
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0065.md
  - /regras/regra-0066.md
  - /regras/regra-0067.md
  - /regras/regra-0071.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0065`, `regra-0066`, `regra-0067` e `regra-0071` são a mesma hipótese
material — aposentadoria voluntária do servidor exposto a agentes nocivos,
art. 41, III da LCE 1.100/2021 — divididas pelo **regime de cálculo e
reajuste**, que é o que os demais dispositivos decidem:

| regra        | cita                      | `paridade` | `tipo_calculo`  |
| ------------ | ------------------------- | ---------- | --------------- |
| `regra-0065` | arts. **25** e **27, I**  | `S`        | `Valor Médio`   |
| `regra-0066` | arts. **25** e **27, I**  | `S`        | `Valor Médio`   |
| `regra-0067` | arts. **25** e **27, I**  | `S`        | `Valor Efetivo` |
| `regra-0071` | arts. **24** e **27, II** | `N`        | `Valor Médio`   |

Esses quatro artigos têm, no seu próprio texto, **corte de ingresso**: os
arts. 25 e 27, I alcançam quem ingressou **até 31/12/2003**; os arts. 24 e
27, II alcançam quem ingressou **após 31/12/2003**. Não é matéria de
interpretação — a data está escrita em cada um dos quatro.

Nenhuma das quatro regras grava a janela de admissão que os seus próprios
dispositivos exigem. As três primeiras omitem o corte; a última grava o lado
oposto:

| regra         | janela de admissão gravada                | população que os dispositivos citados alcançam |
| ------------- | ----------------------------------------- | ---------------------------------------------- |
| `0065`–`0067` | `[01/01/1950 , 31/12/2099]` — sem corte   | só ingresso **até** 31/12/2003                 |
| `regra-0071`  | `[01/01/1950 , 31/12/2003]` — só até 2003 | só ingresso **após** 31/12/2003                |

Na `regra-0071` a interseção entre as duas colunas é **vazia**: a regra é
parametrizada exatamente para a população que os artigos que ela cita
excluem.

# Evidências

## O texto dos quatro artigos, conferido na compilação oficial

Conferido em `fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`
(sha256 `bcac2238855c79d940b4fabd772841462ed58b6ab3d37b1b150bd0750ef69a99`,
já no `manifesto.yaml`), que é a `fonte:` declarada pelos quatro documentos do
bundle. As quatro citações são verbatim:

> **Art. 24.** No cálculo dos proventos de aposentadoria dos servidores
> titulares de cargo efetivo que tenham ingressado no serviço público em cargo
> efetivo **após 31 de dezembro de 2003** [...] será considerada a média
> aritmética simples das maiores remunerações [...]

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de
> 2003** [...] corresponderá à **totalidade da remuneração no cargo efetivo**
> em que se der a aposentadoria.

> **Art. 27.** [...] **I** - de acordo com o disposto no art. 7° da Emenda
> Constitucional n° 41 [...] para aposentadorias concedidas a servidor público
> que tenha ingressado no serviço público em cargo efetivo **até 31 de
> dezembro de 2003** [...]; e **II** - nos termos estabelecidos para o RGPS,
> para as aposentadorias concedidas a servidor público que tenha ingressado no
> serviço público em cargo efetivo **após 31 de dezembro de 2003** [...]

O art. 41, III — o dispositivo que define a hipótese, comum às duas regras —
não tem corte de ingresso nenhum: exige 20 anos de serviço público, 5 anos no
cargo, 86 pontos e 25 anos de efetiva exposição. **O corte vem dos artigos de
cálculo e reajuste**, e é por isso que ele decide qual das duas regras se
aplica.

## O catálogo sabe gravar esse corte, e o grava dezenas de vezes

Levantadas todas as regras que vinculam o mesmo par de dispositivos:

| par citado        | regras                                                                    | `data_adm_*` gravada                        |
| ----------------- | ------------------------------------------------------------------------- | ------------------------------------------- |
| arts. 25 + 27, I  | `0019`, `0020`, `0035`, `0036`, `0041`, `0042`, `0082`, `0083`            | `ate = 31/12/2003` (**8×**)                 |
| arts. 25 + 27, I  | `0059`–`0064`, `0065`, `0066`, **`0067`**, `0095`, `0096`, `0107`, `0108` | sem corte (`ate` = sentinela ou 31/12/2024) |
| arts. 24 + 27, II | `0080`, `0081`                                                            | `apos = 31/12/2003` (**2×**)                |
| arts. 24 + 27, II | `0030`, `0031`, `0033`, `0034`, `0037`, `0038`                            | sem corte                                   |
| arts. 24 + 27, II | **`0071`**                                                                | `ate = 31/12/2003`                          |

Duas coisas ficam demonstradas por esta tabela, e é bom separá-las:

1. **A forma existe.** `regra-0082`/`0083` (policial, arts. 25 e 27, I) gravam
   `data_adm_ate: 31/12/2003`; `regra-0080`/`0081` (policial, arts. 24 e
   27, II) gravam `data_adm_apos: 31/12/2003`. É o **mesmo par de regras
   irmãs** que 0067/0071 são, no subgrupo do policial, e ali as duas janelas
   estão certas e são complementares. O `nome` das duas até diz — "Admissão
   até 31/12/2003".
2. **`regra-0071` é única.** É a **única** regra do catálogo que cita os
   arts. 24 e 27, II e grava o marco 31/12/2003 no campo `ATE`. As outras oito
   ou gravam no campo `APOS` (2) ou não gravam (6). Gravar no campo errado não
   é omissão — é o complemento exato do conjunto pretendido.

## A hipótese da troca, e o que a sustenta

Trocar os dois valores entre as duas regras torna **as duas** corretas de uma
vez: `0067` passaria a `data_adm_ate: 31/12/2003` (a forma das oito) e `0071`
a `data_adm_apos: 31/12/2003` (a forma de `0080`/`0081`). Que as duas sejam o
único par do catálogo a citar o art. 41, III, e que estejam adjacentes na
mesma família de quatro linhas, torna a troca de célula uma explicação
plausível.

**É hipótese, não causa verificada.** Nada no catálogo registra a ordem em que
as linhas foram preenchidas, e o defeito de `0067` também aparece em `0065` e
`0066`, que não têm par invertido nenhum — ou seja, a ausência de corte na
`0067` pode ter causa própria, independente da `0071`.

## A janela de direito das regras 0065–0067 é anterior a tudo o que elas citam

Segunda incompatibilidade, na outra dimensão temporal:

| regra         | `data_direito_apos` | primeira vigência entre os dispositivos citados |
| ------------- | ------------------- | ----------------------------------------------- |
| `0065`–`0067` | **31/12/2003**      | 13/11/2019 (EC 103/2019)                        |
| `regra-0071`  | 18/10/2021          | 13/11/2019 (EC 103/2019)                        |

Os cinco vínculos das regras 0065–0067 são
`cf88/art-40-par-1-inc-iii/ec-103-2019`
e `cf88/art-40-par-4c/ec-103-2019` (vigência a partir de 2019-11-13) e três
artigos da LCE 1.100/2021 (a partir de 2021-10-18). **Nenhum existia em
31/12/2003** — o § 4º-C, que é a autorização constitucional para o benefício
de agentes nocivos no RPPS, foi criado pela EC 103/2019, e a lei
complementar estadual que o exerce é de 2021.

Contra isso, das 35 regras que vinculam algum dispositivo da LCE 1.100/2021,
**19 gravam `data_direito_apos: 18/10/2021`** — o dia de vigência da lei, que é
o que a `regra-0071` grava. As sete que gravam 31/12/2003 são `0065`, `0066`,
`0067`, `0095`, `0096`, `0107` e `0108` — e todas as sete estão também na
lista das que citam os arts. 25 e 27, I **sem** gravar o corte de admissão. Os
dois desencontros temporais aparecem juntos, ainda que a recíproca não valha
(`0059`–`0064` não gravam o corte e gravam 18/10/2021). O `achado-0016` tabula
esse valor em `0107`/`0108` sem fazer dele objeto; o `achado-0043` o alcança em
`0095`/`0096`.

# Extensão da população às regras 0065 e 0066

A rodada seguinte confirmou que `regra-0065` e `regra-0066` têm exatamente as
mesmas janelas e os mesmos dispositivos da `regra-0067`. Elas foram incluídas
em `regras_afetadas`, como este achado já orientava, em vez de receberem um
achado temporal duplicado. A incompatibilidade própria de
`tipo_calculo: Valor Médio` continua separada no `achado-0057`.

A unidade auditada
[`agentes-nocivos-art-41-iii-integralidade-paridade`](../../regras-auditadas/unidades/agentes-nocivos-art-41-iii-integralidade-paridade.md)
propõe, sem alterar o catálogo vigente, `data_adm_ate: 31/12/2003` e
`data_direito_apos: 18/10/2021` para a consolidação das três origens.

# Consequência prática

As quatro regras são `simulavel: S`, e `data_adm_ate`/`data_adm_apos` são campos
**deployáveis** que o motor lê. O efeito de seleção é o seguinte:

- **`regra-0071`** não seleciona ninguém a quem os arts. 24 e 27, II se
  apliquem. Para quem ingressou após 2003 — a população do cálculo por média,
  sem paridade — ela está fechada; e ela abre para quem ingressou antes, a quem
  o catálogo já oferece a `regra-0067`.
- **`regra-0065`–`0067`** selecionam também quem ingressou após 2003 e, para essa
  pessoa, entrega paridade e integralidade que o art. 25 e o art. 27, I
  reservam a quem ingressou até 2003. Aqui o erro é **em favor** do servidor e
  contra o regime, o que o torna material para controle externo.

Somados, os efeitos apontam na mesma direção: hoje a família do art. 41
oferece o tratamento do regime antigo a todos e o do regime novo a ninguém.

Por afetar campos de seleção usados por regras `simulavel: S` e permitir a
aplicação do regime de integralidade e paridade à população que os
dispositivos excluem, a severidade é `bloqueante`.

Nada aqui afirma o que o motor de fato faz com os campos: a leitura de
`DATA_ADM_APOS`/`ATE` está confirmada quanto à inclusividade
([`docs/spec/regra.md`](../../../docs/spec/regra.md), "Elegibilidade
temporal") mas **a que ato de ingresso a coluna se refere** — nomeação, posse,
exercício — segue aberto. Isso não afeta este achado: qualquer que seja o ato,
o corte cai em 31/12/2003 e o lado do corte é que está trocado.

# Questão a investigar

1. **Qual ponta corrigir em cada regra.** Se as janelas estão certas, são os
   vínculos e a fundamentação que estão errados — e aí a `regra-0071` seria
   uma segunda regra de integralidade, o que a deixaria sem par para o regime
   novo. Se os vínculos estão certos, são as duas janelas. A segunda leitura é
   a que o catálogo sustenta (dez regras irmãs gravam o corte na direção do
   dispositivo), mas `data_adm_*` é campo deployável e escolher é ato de quem
   responde pelo produto.

2. **Se a família do art. 41 deveria ter quatro regras.** O art. 41 tem
   **três incisos** — 66 pontos/15 anos de exposição, 76/20 e 86/25,
   conferidos na compilação oficial — e as quatro regras existentes citam
   todas o **inciso III**. Nenhuma coluna registra pontuação nem tempo de
   exposição, então o catálogo não pode distinguir os incisos I e II mesmo que
   quisesse; é a mesma lacuna de schema que o `CLAUDE.md` descreve para
   `0068`/`0069`/`0070` (art. 8º da ECE 146/2021, também três incisos). Este
   achado não conclui se faltam regras ou se as três faixas são
   deliberadamente atendidas por uma só: é pergunta ao IPERON sobre
   granularidade, e a granularidade é escolha dele
   ([`docs/spec/regra.md`](../../../docs/spec/regra.md)).

3. **Se `Valor Efetivo` e `Remuneração de Contribuição` são o mesmo comando.**
   O art. 25 manda pagar "a totalidade da remuneração no cargo efetivo", e as
   regras que o citam se dividem: `0019` e `0067` gravam `Valor Efetivo`;
   `0035`, `0036`, `0041`, `0042`, `0082`, `0083` gravam `Remuneração de Contribuição`. Se os dois valores do enum significam a mesma coisa, a
   divergência é cosmética; se não, uma das duas famílias calcula errado sob a
   mesma lei. É Q6, e o catálogo não responde.
