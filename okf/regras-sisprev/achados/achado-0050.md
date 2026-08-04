---
type: Achado
id: achado-0050
nome: regra-0021 e regra-0022 são as regras do ingresso após 2003 e fundamentam-se nos dois artigos que a LCE 1.100/2021 reserva expressamente a quem ingressou até 31/12/2003
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0021.md
  - /regras/regra-0022.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0022` parametriza **ingresso após 31/12/2003**
(`data_adm_apos: 01/01/2004`, `data_adm_ate: 31/12/2099`), grava
`tipo_calculo: Valor Médio` e `paridade: N`.

As três cláusulas do seu `fundamentacao_integral` — separadas por `|`, uma por
classe de causa da incapacidade — citam, **todas as três**, o mesmo par de
artigos de cálculo e reajuste da LCE 1.100/2021:

> [...] e os artigos **25** e **27, inciso I** e 30, [recorte variável], da
> Lei Complementar Estadual nº 1.100/2021

Os dois artigos citados são, **pelo próprio texto**, os do ramo temporal
oposto: o art. 25 fixa a base de cálculo de quem ingressou **até** 31/12/2003
e o art. 27, I fixa o reajuste **com paridade** dessa mesma classe. Os dois
artigos que correspondem aos valores que a regra grava — art. 24 (média das
80% maiores, para ingresso **após** 31/12/2003) e art. 27, **II** (reajuste
nos termos do RGPS, idem) — **não são citados em nenhuma das três cláusulas**.

O desacordo atinge **três critérios independentes**: a janela de ingresso, o
`tipo_calculo` e a `paridade`.

# Evidências

Conferido na compilação oficial da LCE 1.100/2021 da DITEL/Casa Civil,
arquivada localmente (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`,
`sha256` no `fontes-oficiais/manifesto.yaml`) — não apenas na transcrição do
corpus.

## O que cada artigo diz, e a que classe se dirige

> **Art. 24.** No cálculo dos proventos de aposentadoria dos servidores
> titulares de cargo efetivo que tenham ingressado no serviço público em cargo
> efetivo **após 31 de dezembro de 2003** [...] será considerada a **média
> aritmética simples das maiores remunerações** [...] correspondentes a 80%
> (oitenta por cento) de todo o período contributivo [...]

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**
> [...] corresponderá à **totalidade da remuneração no cargo efetivo** em que
> se der a aposentadoria.

> **Art. 27.** [...] **I** - de acordo com o disposto no art. 7° da Emenda
> Constitucional n° 41 [...] para aposentadorias concedidas a servidor público
> que tenha ingressado no serviço público em cargo efetivo **até 31 de
> dezembro de 2003** [...]; e
>
> **II** - nos termos estabelecidos para o RGPS, para as aposentadorias
> concedidas a servidor público que tenha ingressado no serviço público em
> cargo efetivo **após 31 de dezembro de 2003** [...]

O corte é **literal e expresso nos quatro dispositivos**, com a mesma data e
as mesmas duas preposições. Não é interpretação sistemática: cada artigo
nomeia a sua classe no próprio corpo.

## Cotejo com os valores gravados

| campo de `regra-0022` | valor gravado | dispositivo que o funda | dispositivo citado | fecha? |
| --------------------- | ------------- | ----------------------- | ------------------ | ------ |
| `data_adm_apos`       | 01/01/2004    | art. 24 / art. 27, II   | arts. 25 e 27, I   | ✗      |
| `tipo_calculo`        | Valor Médio   | art. 24                 | art. 25            | ✗      |
| `paridade`            | N             | art. 27, **II**         | art. 27, **I**     | ✗      |
| `tipo_de_beneficio`   | INCAP. PERM.  | art. 30, *caput*        | art. 30 (recortes) | ✓      |

"Valor Médio" e "média aritmética simples das maiores remunerações [...] 80%"
são a mesma coisa, e o próprio campo da regra o diz: "proventos integrais
(**cálculo por média**)". "Totalidade da remuneração no cargo efetivo" (art.
25\) é o outro valor do enum — `Valor Efetivo` —, gravado por `regra-0019`, que
é a regra do ingresso **até** 2003. Ou seja: **os artigos que `regra-0022`
cita são exatamente os que fundam a sua irmã do outro ramo temporal.**

## O § 13 do art. 30 fecha a questão, e ele não estava disponível antes

A conferência anterior
([`conferencia-criterio-dispositivo-incapacidade-restantes.md`](../../../docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md)
§3) **recusou-se a concluir** sobre a base de cálculo deste benefício, porque
os §§ 13 e 14 do art. 30 — que roteiam o cálculo — não estavam transcritos em
`okf/dispositivos/` e a recusa era a resposta certa. Eles estão na fonte
oficial arquivada:

> **§ 13.** O cálculo dos proventos desse benefício dar-se-á **na forma do
> art. 24** desta Lei Complementar, ressalvado o direito adquirido a outra
> fórmula, **se a incapacidade for decorrente de acidente em serviço, moléstia
> profissional ou doença grave, contagiosa ou incurável**.
>
> **§ 14.** O cálculo dos proventos desse benefício dar-se-á **na forma do
> art. 26** desta Lei Complementar, ressalvado o direito adquirido a outra
> fórmula, **se a incapacidade não for decorrente** de acidente em serviço,
> moléstia profissional ou doença grave, contagiosa ou incurável.

As três hipóteses do § 13 são **exatamente** as três classes de causa das três
cláusulas do `fundamentacao_integral` de `regra-0022` — acidente em serviço,
doença grave/contagiosa/incurável, moléstia profissional. A norma manda, para
as três, calcular **na forma do art. 24**. É a segunda confirmação
independente de que o art. 24 é a base desta regra: uma pelo corte de ingresso
do próprio art. 24, outra pelo roteamento do § 13.

Com isso, a pendência **P-5** registrada em
[`base-normativa-invalidez-incapacidade.md`](../../../docs/analysis/base-normativa-invalidez-incapacidade.md)
§3.3 deixa de depender do corpus e passa a estar conferida contra a fonte
oficial.

## Limite desta conferência, declarado

- A fonte é a **compilação** da DITEL/Casa Civil, não a publicação original no
  Diário Oficial. Para os arts. 24 a 27 e 30 nenhuma nota de alteração aparece
  no compilado, o que os identifica como redação original de 2021 pela prática
  de anotação daquele documento; se a publicação original for obtida e
  contradisser isto, é ela que vale.
- Os §§ 13 e 14 do art. 30 **continuam sem dispositivo autorado** em
  `okf/dispositivos/lce-1100-2021/` (existem `art-30-caput` e os §§ 1, 2, 5, 6
  e 8). Transcrevê-los é ato autoral próprio, não praticado por este achado;
  até que sejam, quem ler apenas o bundle não encontra o roteamento acima.
- **Nenhum vínculo é proposto.** `regra-0022` tem `dispositivos:` vazio por
  recusa deliberada (a união achatada das três cláusulas poria `§§ 5º/6º` e
  `§ 8º` lado a lado como se fossem cumulativos, quando são ramos alternativos
  — Q6). Nada aqui muda isso: o defeito é do texto citado, e vincular os
  artigos errados os registraria como citação verdadeira, que é o que eles
  são.
- **`regra-0021` carrega o `fundamentacao_integral` byte-idêntico** e por isso
  o mesmo defeito de citação, com um agravante próprio (grava
  `integral: N`/`Proporcionalidade Dias`, e aí a base seria o art. 26 por
  força do § 14, também não citado). Ela está **em** `regras_afetadas`: a
  conferência documental foi feita sobre a `0022`, mas o texto conferido é o
  mesmo byte a byte, e um defeito de citação já demonstrado no texto idêntico
  não é hipótese a reencontrar. O que é limite do lote é a *investigação* do
  agravante do art. 26/§ 14, ainda não conferido item a item.

# Consequência prática

`FUNDAMENTACAO_INTEGRAL` é campo **deployável**. Um servidor que ingressou em
2010 e se aposenta por incapacidade decorrente de acidente em serviço recebe
hoje um ato fundamentado no art. 25 — "totalidade da remuneração no cargo
efetivo" — e no art. 27, I — reajuste com paridade —, enquanto o cadastro lhe
aplica `Valor Médio` e `paridade: N`. **O documento promete mais do que o
cálculo entrega**, e promete exatamente o regime mais vantajoso: base na
última remuneração em vez de média de 80%, e reajuste paritário em vez de
índice do RGPS.

É a combinação que produz litígio: o texto entregue ao interessado é a base do
pedido de revisão, e ele cita norma que lhe daria o cálculo melhor. Nada no
cadastro contradiz o texto para quem só lê o ato.

A direção oposta também é possível e não pode ser descartada aqui: se a
intenção era conceder o regime do art. 25, então são `tipo_calculo` e
`paridade` que estão errados, e o texto está certo. Qual lado cede é decisão
de quem responde pelos campos.

**Severidade `bloqueante`**, pelo critério de
[`okf/spec/regra.md`](../../../okf/spec/regra.md) ("Quando um achado é
`bloqueante`"): o defeito está demonstrado contra a compilação oficial, o
campo é deployável, e o texto promete regime de cálculo diferente do que o
cadastro executa — os três termos do critério, e em três critérios
independentes (janela de ingresso, `tipo_calculo`, `paridade`). Que a direção
da correção esteja aberta não o afasta: qualquer das duas direções confirma
que o par gravado hoje é internamente contraditório.

# Questão a investigar

1. **Qual lado cede.** Ou a `fundamentacao_integral` troca arts. 25/27-I por
   arts. 24/27-II (e passa a citar o art. 30, *caput*, e o § 13, que fundam o
   resto), ou `tipo_calculo`/`paridade`/`data_adm_apos` estão errados. As duas
   saídas são edição de campo deployável. A primeira é a compatível com o
   `nome` da regra ("Após 31/12/2003") e com a existência da irmã `regra-0019`
   para o ramo anterior; nada, porém, prova a intenção.

2. **Se a citação foi herdada da irmã.** `regra-0019` cita **os mesmos** arts.
   25 e 27, I, e ali eles estão **corretos** — é a regra do ingresso até 2003.
   A hipótese mais simples é que o texto de `0019` foi reaproveitado para o
   ramo pós-2003 sem trocar os artigos de cálculo e de reajuste, mantendo a
   troca apenas no recorte do art. 30. É hipótese, não causa verificada; o que
   a sustenta é que a única coisa que varia entre os dois textos é justamente
   o recorte do art. 30.

3. **Se os §§ 13 e 14 do art. 30 devem ser transcritos e citados.** Eles são o
   roteador do cálculo deste benefício nos dois ramos, e **nenhuma das quatro
   regras do regime vigente os cita**. Transcrevê-los é ato autoral; citá-los
   é edição de campo deployável. Os dois são pré-requisito para que a
   fundamentação desta regra explique, ela mesma, por que o cálculo é o do
   art. 24.

4. **Interação com a decomposição da Q6.** A direção A da
   [Q6](../../../docs/analysis/q6-causa-incapacidade.md) §10 decompõe esta
   regra em uma linha por classe de causa. Se a decomposição vier antes da
   correção, cada linha nascerá com a citação errada replicada três vezes; se
   vier depois, corrige-se um texto e a decomposição herda o texto certo.
   **Corrigir a citação primeiro é a ordem que não multiplica o defeito.**
