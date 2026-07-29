---
type: Achado
id: achado-0033
nome: regra-0057 e regra-0058 gravam um piso de admissão que o art. 5º, § 6º, II da ECE 146/2021 não estabelece, e ele deixa 01/01/2004 descoberto entre elas e regra-0053/0054
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0053.md
  - /regras/regra-0054.md
  - /regras/regra-0057.md
  - /regras/regra-0058.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As quatro regras são a **aposentadoria especial de professor** do art. 5º da
ECE 146/2021, partidas pelo inciso do § 6º que define os proventos:

| regras                      | § 6º | `data_adm_apos` | `data_adm_ate` | resultado                      |
| --------------------------- | ---- | --------------- | -------------- | ------------------------------ |
| `regra-0053` / `regra-0054` | I    | 01/01/1950      | **31/12/2003** | totalidade + paridade          |
| `regra-0057` / `regra-0058` | II   | **01/01/2004**  | 09/09/2021     | média das 80% maiores, s/ par. |

O piso `01/01/2004` de `regra-0057`/`0058` tem **dois** problemas, e o segundo
é maior que o primeiro.

**Primeiro, ele perde um dia.** Sob a semântica confirmada pela coordenação da
auditoria — `ATE` inclusivo, `APOS` exclusivo, janelas adjacentes gravando o
**mesmo** valor nos dois campos —, `data_adm_ate: 31/12/2003` cobre até
31/12/2003 e `data_adm_apos: 01/01/2004` cobre a partir de **02/01/2004**. O
professor admitido em **01/01/2004** não é alcançado por nenhuma das quatro. O
valor que particionaria sem buraco é `31/12/2003` nos dois campos.

**Segundo, o § 6º, II não estabelece piso nenhum.** Seu texto define a
clientela por complemento — "para o servidor público **não contemplado no
inciso I do § 6º** deste artigo" — e esse complemento **não é só temporal**.

# Evidências

Conferido na publicação oficial da Emenda arquivada localmente
(`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, SAPL/ALE-RO, no
`manifesto.yaml`). PDF digitalizado sem camada de texto, leitura visual.

O inciso I do § 6º (p. 5-6 da publicação) condiciona a integralidade a **três**
coisas cumulativas:

> I - à totalidade da remuneração do servidor público no cargo efetivo [...]
> para o servidor público que tenha ingressado no serviço público em cargo
> efetivo, **até 31 de dezembro de 2003**, e que **não tenha feito a opção de
> que trata o § 16 do art. 40 da Constituição Federal**, desde que tenha, no
> mínimo, 62 (sessenta e dois) anos de idade, se mulher, e 65 (sessenta e
> cinco) anos de idade, se homem, e, para os titulares do cargo de professor de
> que trata o § 4º deste artigo, **aos 57 (cinquenta e sete) anos de idade, se
> mulher, e 60 (sessenta) anos de idade, se homem**; e

Logo "não contemplado no inciso I" abrange **três** grupos, e só um deles é
temporal:

1. quem ingressou a partir de 2004;
2. quem ingressou antes, mas **fez a opção do § 16** do art. 40 da CF;
3. quem ingressou antes e não optou, mas **se aposenta antes dos 57/60 anos**
   (professor) — hipótese real, porque o *caput* do art. 5º, com o § 4º,
   permite ao professor aposentar-se aos 51 anos (mulher) e 56 (homem).

Os grupos 2 e 3 ingressaram **até 31/12/2003**. Um piso de admissão em 2004 os
exclui da única regra que o § 6º, II lhes dá — e não os devolve ao § 6º, I, cujo
requisito de idade eles não cumprem (grupo 3) ou cuja vedação do § 16 os alcança
(grupo 2).

O contraste interno ao catálogo mostra que a leitura sem piso é possível: o par
gêmeo não-magistério do **mesmo inciso II** (`regra-0055`/`0056`) grava
`data_adm_apos: 01/01/1950`, isto é, sentinela — nenhum piso. Dentro do mesmo
dispositivo, o catálogo parametriza o mesmo complemento de duas formas
incompatíveis.

## Relação com os documentos que já registraram parte disto

- A [semântica das janelas](../../../docs/analysis/semantica-das-janelas-temporais.md)
  §1.1 estabelece que `ATE_anterior + 1 dia = APOS_seguinte` é a convenção
  **incorreta**, e §3.1/§5.2.02 listam `01/01/2004` em `data_adm_apos` de
  `regra-0014`, `0015`, `0021`, `0022`, `0057` e `0058`. **Este achado não
  alcança as quatro primeiras** — elas são de outra família normativa e não
  foram conferidas aqui. O que este achado acrescenta às duas que confere é a
  segunda metade: nesta família o valor não é apenas um dia a mais, é um piso
  que o dispositivo não tem.
- A [conferência do lote da CF/88 e da ECE 146/2021](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
  §5.7 registrou o dia descoberto. §5.3 registrou as três parametrizações
  incompatíveis do complemento, mas tratou o complemento como temporal ("só
  0057/0058 aplicam o complemento"); a leitura do inciso I contra a fonte mostra
  que ele não é.

# Consequência prática

`DATA_ADM_APOS` é campo **deployável** e as quatro regras são `simulavel: S` —
o motor decide por elas, sem ler a fundamentação.

O buraco de 01/01/2004 é estreito e nítido: um professor admitido naquele dia
não é apresentado por nenhuma das quatro. Já a exclusão dos grupos 2 e 3 é
larga e silenciosa — o servidor existe, tem direito, e a regra que o
implementaria não o alcança porque a janela de admissão dela começa depois do
seu ingresso. Ele não recebe erro: recebe ausência de regra.

# Questão a investigar

1. **Se `data_adm_apos` de `regra-0057`/`0058` deve virar `31/12/2003`** (piso
   mantido, buraco fechado) **ou sentinela** (piso removido, alinhando-se a
   `regra-0055`/`0056`). As duas correções fecham o buraco de um dia; só a
   segunda resolve os grupos 2 e 3. A escolha depende de saber se o par foi
   desenhado para a metade temporal do complemento ou para o complemento
   inteiro — e é decisão de campo deployável, não da auditoria.

2. **Onde mora o critério que o cadastro não grava.** Nem a opção do § 16 do
   art. 40 da CF nem a idade do requerente têm coluna no Sisprev. Se o piso for
   removido, `regra-0053`/`0054` e `regra-0057`/`0058` passam a se sobrepor
   para todo ingresso até 2003, e nada nas colunas separa as duas — é o mesmo
   formato da Q6, registrado como ponto em aberto nº 4 da conferência do lote.
   A sobreposição seria **correta** juridicamente e indecidível
   mecanicamente.

3. **Se o mesmo hábito de gravar o primeiro dia da cobertura aparece nos outros
   quatro casos de `01/01/2004`** (`regra-0014`, `0015`, `0021`, `0022`). Se
   sim, o conserto é de convenção; a semântica das janelas §3.1 já sugere isso
   ("erro de tradução da semântica e não decisão jurídica deliberada"), mas
   sobre outra família.
