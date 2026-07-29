---
type: Achado
id: achado-0015
nome: Seis regras marcam o mesmo fim de regime em datas diferentes — três destoam da convenção do catálogo por um dia
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0001.md
  - /regras/regra-0002.md
  - /regras/regra-0003.md
  - /regras/regra-0023.md
  - /regras/regra-0024.md
  - /regras/regra-0088.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Seis regras delimitam o **mesmo marco temporal** — o fim do regime anterior à
EC 20/1998 — e gravam duas datas diferentes para ele:

| regra        | `data_direito_ate` | benefício                            |
| ------------ | ------------------ | ------------------------------------ |
| `regra-0001` | **15/12/1998**     | aposentadoria por invalidez          |
| `regra-0002` | **15/12/1998**     | aposentadoria por invalidez          |
| `regra-0003` | **15/12/1998**     | pensão por morte                     |
| `regra-0023` | **16/12/1998**     | aposentadoria compulsória            |
| `regra-0024` | **16/12/1998**     | aposentadoria por idade              |
| `regra-0088` | **16/12/1998**     | voluntária por tempo de contribuição |

São benefícios diferentes, então não são duplicatas: são regras distintas que
compartilham a mesma fronteira. E a fronteira é uma só — a EC 20/1998 entrou
em vigor em **16/12/1998** (art. 16, "entra em vigor na data de sua
publicação"; DOU de 16/12/1998, conferido na publicação original da Câmara,
arquivada em `fontes-oficiais/`).

# Evidências

`verificacao: manual`, e a razão importa: as contagens abaixo são
reproduzíveis, mas **nenhum detector as produz**. Saíram de consulta ad hoc
sobre o bundle, e a fronteira contra a qual foram comparadas — 16/12/1998 —
veio de ler o art. 16 da emenda. Classificar como `mecanica` exigiria um
detector comitado com fingerprint estável, e transformar isto em detector é
decisão que este achado não toma (a conclusão que ele alcança é sobre
**qual grupo destoa**, não sobre qual está certo — e essa parte não é
mecânica).

O que decide não é qual das duas leituras é juridicamente melhor, e sim que o
**catálogo já tem uma convenção**, seguida em toda parte menos aqui. Contando
as ocorrências dos dois campos nos marcos de vigência conhecidos:

| campo               | marco          | grava o dia **anterior** | grava o **dia do marco** |
| ------------------- | -------------- | ------------------------ | ------------------------ |
| `data_direito_apos` | EC 20/1998     | 0×                       | 8×                       |
| `data_direito_apos` | EC 41/2003     | 0×                       | 30×                      |
| `data_direito_apos` | LCE 1.100/2021 | 0×                       | 22×                      |
| `data_direito_ate`  | EC 41/2003     | 0×                       | 8×                       |
| `data_direito_ate`  | EC 20/1998     | **3×**                   | 3×                       |

**Sessenta e oito linhas gravam "o dia em que a redação começa". Três não** —
e as três são `regra-0001`, `regra-0002` e `regra-0003`.

A convenção fica ainda mais nítida quando os dois marcos de uma mesma regra
são lidos juntos. Sete regras têm ambos coincidindo com fronteiras de redação,
e todas as sete formam intervalo **semiaberto**, `[apos, ate)`:

```
regra-0004  [1998-12-16 , 2003-12-31)   ← exatamente a vida da redação EC 20/1998
regra-0023  [1910-01-01 , 1998-12-16)   ← exatamente a vida da redação original
regra-0026  [1998-12-16 , 2003-12-31)
regra-0089  [1998-12-16 , 2003-12-31)
regra-0090  [1998-12-16 , 2003-12-31)
```

A redação EC 20/1998 do art. 40, § 1º, I vige de 1998-12-16 a 2003-12-30, e a
`regra-0004` grava `[1998-12-16, 2003-12-31)`. O fecho da regra é o primeiro
dia da redação **seguinte**, não o último da sua. É a mesma forma em todas.

# Consequência prática

Sob a convenção dominante, um requerimento cujo direito se perfez em
**15/12/1998** — o último dia do regime anterior — é alcançado por
`regra-0023`, `0024` e `0088`, e **não** por `regra-0001`, `0002` e `0003`.
As três que destoam perdem o seu último dia.

O efeito não é uniforme entre benefícios, e é aí que dói: quem pediu
aposentadoria compulsória naquele dia está coberto; quem pediu aposentadoria
por invalidez ou pensão por morte, não. Nada na lei justifica a diferença — a
EC 20/1998 alcançou os três benefícios na mesma data.

`data_direito_ate` é campo **deployável**. Corrigi-lo é alterar o produto, não
auditar o catálogo, e depende de quem responde por ele.

# Questão a investigar

1. **Qual dos dois grupos corrige.** A contagem de 68 × 3 estabelece qual é a
   convenção *do catálogo*, não qual é a leitura *correta*. Se a convenção
   estiver certa, corrigem-se as três; se estiver errada, corrigem-se as
   sessenta e oito. A segunda hipótese é cara, mas não pode ser descartada por
   ser cara.

2. **O que o motor do Sisprev faz com o campo.** Esta é a pergunta que a
   contagem **não** responde e da qual tudo depende. Saber que 68 linhas foram
   preenchidas com "o dia em que a redação começa" diz como o catálogo foi
   escrito, não se o sistema trata `DATA_DIREITO_ATE` como inclusiva ou
   exclusiva ao selecionar a regra. Se o motor comparar com `<=` e a convenção
   for semiaberta, todas as 68 concedem um dia a mais do que deveriam — o erro
   seria da convenção, não das três.

3. **Relação com a Q1/issue #39.** Esta é evidência nova e mecânica para a
   pendência sobre a semântica de `DATA_DIREITO_APOS`/`ATE` registrada em
   [`semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md)
   §1.2 — e é a mais limpa até agora, porque não depende de interpretar
   nenhuma prosa: são datas gravadas comparadas com vigências conferidas em
   publicação oficial. Mas continua sendo evidência sobre o **preenchimento**,
   e a questão em aberto é sobre o **comportamento**. Não a fecha.

4. **Por que só neste marco.** Na fronteira da EC 41/2003 o catálogo é
   unânime (8× no dia do marco, 0× no anterior). A divergência existe apenas
   em 1998, o que sugere lote de preenchimento ou autor distinto, e não
   decisão consciente. Hipótese, não causa verificada.
