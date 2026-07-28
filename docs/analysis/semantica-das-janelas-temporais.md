# Semântica das janelas temporais — o que ficou confirmado e o que falta

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. Registra a
> semântica de `DATA_ADM_*`/`DATA_DIREITO_*` confirmada pela coordenação da
> auditoria, o critério de conferência que dela decorre, e a **lista exata**
> das informações ainda necessárias. Toda correção de regra é ato humano, em
> PR própria, depois de decisão sobre as pendências da seção 5.

## 1. O que ficou confirmado

Confirmado pela coordenação da auditoria em 2026-07-28, respondendo à **Q1**
do RFC 0001 e a parte da **Q2**:

1. **`DATA_*_ATE` é inclusivo.** `ate = X` cobre o próprio dia X.
2. **`DATA_ADM_APOS` é exclusivo.** `apos = X` cobre a partir do dia
   **seguinte** a X. Confirmado no caso concreto: `data_adm_apos = 31/12/2003` significa "admitido a partir de 01/01/2004".
3. **A escolha do campo segue a forma do requisito legal.** Quando o direito
   exige data *até*, usa-se o campo `ATE`; quando exige data *após* certo
   dia, usa-se o campo `APOS`.
4. **O valor gravado é o marco, ajustado à semântica da coluna** e ao que
   efetivamente consta na legislação — **não** o primeiro dia da cobertura.
5. **`DATA_DIREITO_ATE` é o prazo de implementação dos requisitos**: todos os
   requisitos precisam estar completos até essa data.

### 1.1 A consequência que fecha a incompatibilidade da issue #37

Dos pontos 1, 2 e 4 decorre que **janelas adjacentes gravam o mesmo valor nos
dois campos**:

```
regra anterior:  ate  = M      cobre  ... até M, inclusive
regra seguinte:  apos = M      cobre  a partir de M+1
```

Isso particiona sem buraco e sem sobreposição. Logo, das duas convenções que
a issue #37 encontrou no catálogo, a correta é `ATE_anterior = APOS_seguinte`
— e `ATE_anterior + 1 dia = APOS_seguinte` produz um dia descoberto.

### 1.2 O que **não** está confirmado

Registrado explicitamente para que nada aqui seja lido além do que foi dito:

- **A confirmação veio da coordenação da auditoria, não de documentação do
  Sisprev nem de teste no sistema.** Três requerimentos sintéticos
  confirmariam empiricamente: admissão em 01/01/2004 (as `regra-0021`/`0022`
  aparecem?), admissão em 31/12/2003 (`regra-0080` *e* `regra-0082`
  aparecem?), direito adquirido em 31/12/2003.
- **`DATA_DIREITO_APOS` não foi confirmado** — a leitura simétrica ("os
  requisitos não podiam estar completos até essa data") é a presumível, mas
  a issue #39 é exatamente sobre não presumir que os dois eixos compartilhem
  semântica. Ver 5.3.
- **A que ato `DATA_ADM_*` se refere** (nomeação, posse, exercício, ingresso
  em sentido amplo) segue aberto.
- **As sentinelas seguem não interpretadas** (P5, decisão de 2026-07-17).

## 2. O critério de conferência que decorre disso

Se o valor gravado é o marco, então **todo limite não-sentinela deveria
coincidir com uma data declarada pelos dispositivos que a própria regra
cita** — a vigência da norma, ou um prazo fixado no texto do dispositivo.

Isso é mais forte do que parece, porque **dispensa parear regras entre si**.
A tentativa de detectar a incompatibilidade comparando janelas adjacentes
esbarra em não haver chave de pareamento confiável: agrupar por
benefício+sexo devolve 88 pares no eixo `adm`, a maioria sem relação de
complementaridade; exigir regras idênticas exceto pela janela devolve zero
(as metades complementares divergem em 8 a 10 campos, incluindo `paridade`,
`integral` e `tipo_calculo`); e `sexo` está vazio em 13 regras
(`achado-0008`, aberto), justamente as que quebram o agrupamento. Conferir
cada regra contra os dispositivos que ela já declara não tem nenhum desses
problemas.

O gabarito ainda é parcial: das 16 normas do vocabulário, 9 têm
`vigencia_inicio` autorada e 7 não (seção 5.1), e os prazos internos aos
dispositivos dependem da transcrição sob demanda do P3.

## 3. A varredura com o gabarito atual

Marcos autorados hoje em `okf/dispositivos/*/norma.md`:

| data       | norma                                        |
| ---------- | -------------------------------------------- |
| 05/10/1988 | CF/88 (início)                               |
| 16/12/1998 | EC 20/1998 (início)                          |
| 31/12/2003 | EC 41/2003 (início)                          |
| 13/03/2008 | LCE 432/2008 (início)                        |
| 30/03/2012 | EC 70/2012 (início)                          |
| 09/08/2012 | LCE 672/2012 (início)                        |
| 13/11/2019 | EC 103/2019 (início)                         |
| 14/09/2021 | ECE 146/2021 (início)                        |
| 18/10/2021 | LCE 1.100/2021 (início) e LCE 432/2008 (fim) |

Aplicando o critério aos quatro campos de data das 112 regras, excluídas as
sentinelas: **230 limites**, dos quais **166 coincidem** com um marco
(`16/12/1998`, `31/12/2003`, `13/11/2019`, `14/09/2021`, `18/10/2021`) e
**64 não coincidem com marco nenhum**:

| valor        | ocorrências | onde                                                    |
| ------------ | ----------- | ------------------------------------------------------- |
| `31/12/2024` | 34          | `data_adm_ate` de 6 regras; `data_direito_ate` de 28    |
| `15/12/1998` | 6           | `data_adm_ate` e `data_direito_ate` de 0001, 0002, 0003 |
| `01/01/2004` | 6           | `data_adm_apos` de 0014, 0015, 0021, 0022, 0057, 0058   |
| `01/01/2024` | 5           | `data_direito_apos` de 0014–0018                        |
| `23/10/2021` | 4           | `data_direito_apos` de 0019–0022                        |
| `04/12/2015` | 2           | `data_direito_apos` de 0030, 0031                       |
| `14/06/2021` | 2           | `data_adm_ate` de 0049, 0050                            |
| `09/09/2021` | 2           | `data_adm_ate` de 0057, 0058                            |
| `01/01/1969` | 1           | `data_direito_apos` de 0003                             |
| `01/12/2002` | 1           | `data_direito_ate` de 0087                              |
| `03/12/2015` | 1           | `data_direito_ate` de 0027                              |

Não coincidir **não é veredito de erro**: pode ser prazo fixado no
dispositivo, marco de norma ainda sem vigência autorada, ou norma fora do
vocabulário atual (o RFC 0001 é explícito que o corpus de ~16 normas não é
presumido completo). O que a tabela produz é uma **fila de conferência**, não
uma acusação.

### 3.1 Os dois casos que o gabarito atual já sustenta

Estes dois erram por um dia contra marco **já autorado no próprio repositório**:

- **`15/12/1998`** em `regra-0001`, `0002`, `0003` (nos dois eixos). A EC
  20/1998 vige em 16/12/1998 — data autorada em três dispositivos do bundle.
  As outras 14 regras que fecham nesse marco no eixo `adm` usam 16/12/1998.
- **`01/01/2004`** em `data_adm_apos` de `regra-0014`, `0015`, `0021`,
  `0022`, `0057`, `0058`. A EC 41/2003 vige em 31/12/2003. Sob `APOS`
  exclusivo, `01/01/2004` cobre a partir de **02/01/2004**, deixando
  01/01/2004 descoberto.

Um detalhe de proveniência: `regra-0014` e `0015` aparecem **duas vezes** na
tabela — gravaram `01/01/2004` em `data_adm_apos` e `01/01/2024` em
`data_direito_apos`. É o mesmo hábito (gravar o primeiro dia da cobertura em
vez do marco) aplicado nas duas pontas, o que sugere erro de tradução da
semântica e não decisão jurídica deliberada. `regra-0057`/`0058` também
acumulam dois itens da tabela.

### 3.2 Relação com o E8 do RFC 0001

`14/06/2021` (`regra-0049`/`0050`) e `09/09/2021` (`regra-0057`/`0058`) são o
**E8** do RFC 0001, aqui rederivado por critério independente: ambas as
famílias citam a ECE 146/2021, cujas gêmeas usam `14/09/2021`. O E8 nunca
recebeu achado próprio; o mesmo critério cobriria os dois.

## 4. O que este documento não decide

Não corrige nenhuma regra, não escreve achado e não fecha nenhuma questão
além da Q1 e da parte da Q2 registradas na seção 1. A correção de um campo
de data é mudança em **campo deployable** — as quatro colunas de data são
colunas do CSV, chegam ao Sisprev e decidem qual regra se aplica a um
servidor. Nenhuma foi alterada desde a importação original: todas as edições
já feitas em `okf/regras-sisprev/regras/` foram na fatia administrativa
(`dispositivos:`, 95 de 112 regras).

Quando a correção vier, o veículo indicado é um `Conjunto` `proposto` (P15,
RFC 0006) e não edição in-place, justamente para que o estado anterior não
sobreviva apenas no git.

## 5. Lista exata do que falta

### 5.1 Vigência das 7 normas sem data

Sem elas o gabarito da seção 2 fica parcial. Formato: data de publicação /
entrada em vigor, e de revogação quando houver.

| norma                 | `vigencia_inicio` | `vigencia_fim` |
| --------------------- | ----------------- | -------------- |
| EC 47/2005            | ?                 | —              |
| EC 88/2015            | ?                 | —              |
| LC 51/1985 (federal)  | ?                 | ?              |
| LC 144/2014 (federal) | ?                 | —              |
| LC 152/2015 (federal) | ?                 | —              |
| LCE 949/2017          | ?                 | ?              |
| Lei 10.887/2004       | ?                 | —              |

As nove restantes já estão autoradas (tabela da seção 3). **LC 152/2015 é a
mais urgente** — sem ela não se fecha o item 5.2.3.

### 5.2 As 11 datas sem marco

Para cada uma: **qual norma ou dispositivo estabelece essa data**, ou "é erro".

01. **`15/12/1998`** — `regra-0001`, `0002`, `0003`, nos dois eixos. A EC
    20/1998 vige em 16/12/1998. Confirma que é erro de um dia?
02. **`01/01/2004`** — `data_adm_apos` de `0014`, `0015`, `0021`, `0022`,
    `0057`, `0058`. Sob `APOS` exclusivo cobre a partir de 02/01/2004.
    Confirma que a intenção era "a partir de 01/01/2004", logo o valor
    deveria ser `31/12/2003`?
03. **`03/12/2015` vs `04/12/2015`** — `regra-0027` (Compulsória, EC 41 + LC
    432\) fecha `data_direito_ate` em 03/12; `regra-0030`/`0031`
    (Compulsória, LC 152/15) abrem `data_direito_apos` em 04/12. Mesmo
    defeito estrutural do item 1: sob a semântica confirmada há um dia
    descoberto em 04/12/2015. Se a LC 152/2015 vige em 04/12/2015,
    `regra-0027` deveria fechar em 04/12. Confirma?
04. **`14/06/2021`** — `data_adm_ate` de `0049`/`0050` ("Art. 6º, §2º, II da
    EC 146/21 — Magistério"), cujas gêmeas usam `14/09/2021`. Erro de
    digitação do mês, ou marco próprio?
05. **`09/09/2021`** — `data_adm_ate` de `0057`/`0058` ("Art. 5º, §4º da EC
    146/21 — Magistério"), gêmeas em `14/09/2021`. Erro do dia, ou marco
    próprio?
06. **`23/10/2021`** — `data_direito_apos` de `0019`–`0022` (incapacidade
    permanente, EC 103/19 c/c **art. 30 da LC 1.100/21**). A LC 1.100 vige em
    18/10/2021, cinco dias antes. O art. 30 tem vacatio própria, produção de
    efeitos diferida, ou é erro?
07. **`01/01/2024`** — `data_direito_apos` de `0014`–`0018` (Pensão por Morte
    do **art. 46 da LC 1.100/2021**, vigente desde 18/10/2021). Por que o
    direito só se adquire a partir de 2024? Há norma de 2023/2024 que altere
    isso, ou é erro?
08. **`31/12/2024`** — `data_adm_ate` de 6 regras e `data_direito_ate` de 28.
    É o maior grupo sem marco. Pela definição confirmada de
    `DATA_DIREITO_ATE`, a hipótese é que seja **prazo de regra de transição**
    e não vigência de norma. Qual norma fixa 31/12/2024?
09. **`01/01/1969`** — `data_direito_apos` de `regra-0003` (Pensão por Morte,
    redação original da CF/88). Data anterior à própria CF/88. É sentinela
    não catalogada, ou marco real?
10. **`01/12/2002`** — `data_direito_ate` de `regra-0087`, cujo nome é "Apos.
    Voluntária Tempo de Serviço — **Anterior a E.C. 20/1998**", mas que fecha
    em 2002. O que é 01/12/2002?

### 5.3 Confirmações semânticas

1. `DATA_ADM_*` refere-se a qual ato: nomeação, posse, exercício, ou
   ingresso no serviço público em sentido amplo?
2. `DATA_DIREITO_APOS` tem a leitura simétrica do `ATE` — "os requisitos não
   podiam estar completos até essa data" (exclusivo)? Pergunta feita
   explicitamente porque a issue #39 é sobre não presumir que os dois eixos
   compartilhem semântica.
3. Para **pensão por morte**, "todos os requisitos completados" equivale à
   data do óbito?
4. As sentinelas `01/01/1900`, `01/01/1910`, `01/01/1950` e `31/12/2099`
   significam "sem limite"? São três valores para o mesmo sentido no limite
   inferior, ou distinguem algo?

### 5.4 Decisões de auditoria

Não são fatos a levantar, são decisões a tomar:

1. Os casos confirmados como erro entram em **um** achado ou em achados
   separados por causa?
2. Severidade: `bloqueante` (trava `status_auditoria: revisada` das regras
   afetadas até a correção) ou `informativo`? Diferentemente do E8 original,
   que era suspeita, aqui há erro provado contra marco autorado — o que
   sugere `bloqueante`.
3. Quem assina `detectado_por`.

## 6. Referências

- RFC 0001, **Q1** e **Q2** (questões semânticas abertas) e **P5** (janelas
  temporais), [`docs/rfc/0001-criterios-de-validacao-das-regras.md`](../rfc/0001-criterios-de-validacao-das-regras.md)
- Spec P13.1, seção "Elegibilidade temporal",
  [`docs/spec/regra.md`](../spec/regra.md)
- Contrato do dispositivo e da norma,
  [`docs/spec/dispositivo.md`](../spec/dispositivo.md)
- Issues #37 (duas convenções de fronteira), #38 (detector de consistência de
  marco), #39 (Q1 por eixo)
