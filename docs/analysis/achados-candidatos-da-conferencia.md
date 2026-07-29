# Achados candidatos da conferência `critério → dispositivo`

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. Consolida os sete
> relatórios de conferência que cobrem 101 das 112 regras. **Nada aqui é
> achado** — achado é documento autorado por humano em `achados/`, e a
> decisão de qual destes vira um é do auditor.

## Como ler esta lista

A ordem é de **gravidade**, e o critério é o dano que o erro causa se a regra
for aplicada a um requerimento real:

1. **A regra invoca provisão de outro benefício ou de outra pessoa** — aplica
   direito que não é o do caso.
2. **A regra funda-se em provisão que não vigia na janela dela** — aplica
   direito revogado, ou ainda não vigente.
3. **O valor gravado contradiz a lei que a própria regra cita** — o cadastro
   e a fundamentação, ambos deployáveis, dizem coisas diferentes.
4. **Critério decisivo sem dispositivo que o funde** — a regra decide por um
   critério que nenhuma provisão citada sustenta.
5. **Padrões sistêmicos** — repetem-se em lotes independentes, o que os torna
   estruturais.

Marcações: **[V]** = conferi pessoalmente o texto do dispositivo e o campo da
regra; **[R]** = vem do relatório do grupo, não reconferido aqui.

______________________________________________________________________

## 1. Provisão de outro benefício ou de outra pessoa

### 1.1 `regra-0078` funda-se na alínea que rege mulheres **[V]**

`sexo: MASCULINO`. O campo `fundamentacao_integral` cita — e `dispositivos:`
vincula — `lc-51-1985/art-1-inc-ii-al-b`, cujo texto é:

> **b)** após **25** anos de contribuição, desde que conte, pelo menos, **15**
> anos de exercício em cargo de natureza estritamente policial, **se mulher**.

A alínea **"a"**, imediatamente acima na mesma norma, é a masculina: **30**
anos de contribuição e **20** de exercício policial, "se homem".

Uma regra masculina exigindo o tempo de contribuição feminino — cinco anos a
menos. O `achado-0010` já registra o `P9_SEXO_FUNDAMENTACAO` nesta regra, mas
o detector só enxerga a palavra "mulher" no texto; a conferência mostra qual
provisão é invocada e o que ela exige.

### 1.2 `regra-0084`: `sexo: AMBOS` vinculando só a alínea feminina **[R]**

Mesmo padrão, sem detector nenhum apontando — o `P9_SEXO_FUNDAMENTACAO` não
dispara porque o campo `sexo` é `AMBOS`.

### 1.3 `regra-0061` e `regra-0062` citam auxílio-reclusão **[V]**

Ambas são `APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`. O campo
`fundamentacao` de cada uma cita "Art. 39, parágrafo único da Lei
Complementar" — e o art. 39 da LCE 432/2008 é:

> Art. 39. **O auxílio-reclusão** do segurado, servidor ativo, será concedido
> ao conjunto de seus dependentes, a contar da data em que o segurado preso
> deixa de perceber vencimentos [...]

Benefício inteiramente diverso, com fato gerador diverso e beneficiário
diverso.

**A consequência de segunda ordem importa tanto quanto o erro:** essa citação
é a **única coisa** que mantém 0061/0062 fora de um grupo
`P2_IGUALDADE_MATERIAL_ATIVA`. Corrigi-la faz três pares colapsarem — o erro
está, hoje, escondendo duplicação material.

______________________________________________________________________

## 2. Provisão fora de vigência na janela da regra

### 2.1 `regra-0032` funda-se no que foi revogado no primeiro dia da sua janela **[V]**

```
data_direito_apos: 18/10/2021
  lce-432-2008/art-17         vigência → 2021-10-18
  lce-432-2008/art-21-par-1   vigência → 2021-10-18
  lce-432-2008/art-45         vigência → 2021-10-18
  lce-432-2008/art-62         vigência → 2021-10-18
```

Quatro dos seis dispositivos vinculados encerram vigência exatamente no dia
em que a janela da regra abre.

### 2.2 `regra-0030`/`0031` são o espelho **[R]**

Janela desde 04/12/2015, citando a LCE 1.100/2021 — vigente só a partir de
18/10/2021. As janelas de 0030/0031 e 0032 ainda **se sobrepõem por três
anos**, com leis estaduais excludentes que fixam idades-limite diferentes: 70
anos pelo art. 21 da LCE 432/2008, 75 pela LC 152/2015 e pelo art. 31 da LCE
1.100/2021.

______________________________________________________________________

## 3. Valor gravado contra a fundamentação da própria regra

Este é o bloco mais numeroso. Em todos, os dois lados são **campo deployável**
— o cadastro e o texto entregue ao servidor discordam entre si.

### 3.1 `regra-0041` × `regra-0107`: string idêntica, três campos opostos **[V]**

|                          | 0041                                | 0107            |
| ------------------------ | ----------------------------------- | --------------- |
| `fundamentacao_integral` | **idêntica, caractere a caractere** | ←               |
| `sexo`                   | MASCULINO                           | MASCULINO       |
| `apos_especial`          | S                                   | S               |
| `integral`               | **S**                               | **N**           |
| `tipo_calculo`           | **Remuneração de Contribuição**     | **Valor Médio** |
| `paridade`               | **S**                               | **N**           |

O mesmo texto jurídico sustentando resultados opostos. Uma das duas está
errada, e o texto não diz qual.

### 3.2 Onze regras do regime novo gravam resultado contrário à própria fundamentação **[R]**

Relatado no grupo LCE 1.100/2021, sobre 24 regras.

### 3.3 `regra-0109`/`0110`: três campos contra o único dispositivo que os funda **[R]**

`ece-146-2021/art-7-par-3` estabelece totalidade da remuneração do cargo e
reajuste paritário. As duas gravam `integral: N`, `paridade: N`,
`tipo_calculo: Valor Médio`. A janela de admissão (2003–2024) também é
incompatível com o corte de ingresso até 13/11/2019 do próprio art. 7º.

### 3.4 `regra-0033`/`0034`: `integral: N` num texto que diz "proventos integrais" **[R]**

O único campo de fundamentação preenchido é o integral, e ele diz "com
proventos integrais".

### 3.5 `regra-0019`/`0020`: texto diz "integrais e com paridade", campos gravam `N` **[R]**

### 3.6 `regra-0032`: `tipo_calculo: Tipo Cálculo Nova Previdência` **[R]**

O texto da própria regra diz "média aritmética simples", e seus vínculos são
os arts. 17 e 45 da LCE 432/2008.

### 3.7 `regra-0057`/`0058`: integralidade dependendo do sexo, sem dispositivo que a funde **[R]**

______________________________________________________________________

## 4. Critério decisivo sem dispositivo

### 4.1 A idade-limite não é campo de regra nenhuma na compulsória **[R]**

O critério que **define** a aposentadoria compulsória — a idade em que ela
incide — não está parametrizado em nenhuma das seis regras do tipo.

### 4.2 `apos_especial: S` sem fundamento em campo nenhum **[R]**

Em `0099`/`0100` (transição) e em três dos quatro subgrupos especiais do
regime novo, o que **define** a especialidade não tem dispositivo citado.

### 4.3 `sexo` não é fundado por provisão transcrita nenhuma nas doze de transição **[R]**

E em `0030`/`0031` o `sexo` M/F é hoje a única coisa que impede o `P2` de
agrupá-las — sem dispositivo que o justifique.

### 4.4 O art. 34 diz "para ambos os sexos", e quatro regras se dividem por sexo **[R]**

### 4.5 A causa da incapacidade (Q6) **[V, já registrado]**

Distingue `0006`↔`0007` e `0008`↔`0009`, e nenhuma coluna a registra. Os
campos de 0006 e 0007 são **literalmente idênticos**; o que as separa está
dentro do parêntese de um texto compartilhado.

______________________________________________________________________

## 5. Padrões sistêmicos

Apareceram em lotes independentes, conferidos por agentes diferentes — o que
os torna estruturais, não coincidência.

### 5.1 O prazo de 31/12/2024 está invertido — **cinco dos seis grupos**

O art. 4º da ECE 146/2021 é o **único** dispositivo do corpus inteiro que fixa
essa data. E:

- regras que **o citam e vinculam** gravam `31/12/2099` ou `03/12/2015`;
- regras que **gravam 31/12/2024** não o citam em campo deployável — nas
  `0028`/`0029` e `0109`–`0112` ele aparece só no `nome`, que não é
  fundamentação;
- pares que vinculam os mesmos dispositivos gravam datas diferentes.

É o achado mais repetido da conferência inteira.

### 5.2 O art. 40, § 1º, III não funda critério nenhum — em pelo menos 29 regras

Confirmado nas 4 de invalidez, nas 13 de policial e nas 12 de transição, por
três agentes independentes. Já registrado como pendências **P-3**/**P-4** em
[`base-normativa-invalidez-incapacidade.md`](base-normativa-invalidez-incapacidade.md).

### 5.3 Transcrições que param no *caput*, e os requisitos estão nos incisos

- os três artigos de transição (art. 2º e 6º da EC 41/2003, art. 3º da EC
  47/2005) — os requisitos que as 12 regras precisam estão nos incisos;
- art. 35 da LCE 1.100/2021 — transcrito até "observadas as seguintes
  condições:", e os incisos não existem no corpus;
- **caput do art. 7º da ECE 146/2021** — funda o corte de ingresso e a idade
  de 55 anos das policiais, e não existe como dispositivo autorado.

Isso é fila `TRANSCREVER` nova, não detectada pela lista congelada.

### 5.4 Dezesseis regras da ECE 146/2021 não citam o dispositivo que estabelece seus requisitos **[R]**

______________________________________________________________________

## 6. O que nenhum grupo propôs

**Nenhum vínculo a acrescentar ou remover, nos seis grupos.** O
`dispositivos:` espelha o que as fundamentações citam, em todo o catálogo
conferido.

Todo o problema está em **valores gravados** e em **citações erradas** — e as
duas coisas são campo deployável, logo achado autorado, nunca correção de
link. Cada relatório registra também o que o agente **recusou** concluir.

## 7. Correção à lista congelada

A pendência da `regra-0025` está na fila errada em
[`pendencias-de-citacao-congeladas.md`](pendencias-de-citacao-congeladas.md):
é `TRANSCREVER`, não `REDACAO`. A redação da EC 20/1998 existe — o próprio
`achado-0013` a transcreve.
