# Conferência `critério → dispositivo` — regras 0006 a 0009 (invalidez)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. É a primeira
> aplicação da conferência descrita na RFC 0008 §5 — para cada critério da
> regra, qual dispositivo o funda —, feita sobre as quatro regras de
> invalidez que já tinham pendência registrada. Toda conclusão sobre citação
> é ato humano, em achado próprio.

## O método

A RFC 0008 §5 registra a definição da coordenação da auditoria: a
fundamentação **articula** os dispositivos de forma a fundamentar os
critérios da própria regra, cada um deles. Logo a relação é
`critério → dispositivo(s)`, e `dispositivos:` é a união achatada dela.

Conferir é desachatar: percorrer os critérios que a regra parametriza e,
para cada um, dizer qual provisão o funda. Um dispositivo que não funda
critério nenhum é suspeito; um critério sem dispositivo é lacuna.

## As quatro regras, lado a lado

Todas: `APOSENTADORIA POR INVALIDEZ`, `sexo: AMBOS`, `simulavel: S`,
`apos_especial: N`, `adicional_inatividade: N`, `tabelapontuacao: N`,
`requisitos_da_in_no_5_2020: N`, `data_adm_apos: 01/01/1950`,
`data_direito_apos: 31/12/2003`, `data_direito_ate: 31/12/2099`.

O que as distingue:

|                | 0006        | 0007                   | 0008                        | 0009                        |
| -------------- | ----------- | ---------------------- | --------------------------- | --------------------------- |
| `data_adm_ate` | 31/12/2099  | 31/12/2099             | **31/12/2003**              | **31/12/2003**              |
| `integral`     | S           | N                      | S                           | N                           |
| `tipo_calculo` | Valor Médio | Proporcionalidade Dias | Remuneração de Contribuição | Remuneração de Contribuição |
| `paridade`     | N           | N                      | **S**                       | **S**                       |

Duas famílias: **0006/0007** (regime geral do art. 40, § 1º, I, cálculo por
média, sem paridade) e **0008/0009** (regime de transição do art. 6º-A da EC
41/2003, cálculo pela remuneração do cargo, com paridade).

## A conferência

### 0006 e 0007 — regime do art. 40, § 1º, I

| critério                                      | valor                              | fundado por                                                                                                      | fecha?                        |
| --------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| tipo de benefício                             | invalidez permanente               | `cf88/art-40-par-1-inc-i/ec-41-2003` + `lce-432-2008/art-20-caput/original`                                      | ✅                            |
| sexo                                          | AMBOS                              | nenhuma das provisões distingue por sexo                                                                         | ✅ por ausência               |
| início do direito                             | após 31/12/2003                    | data de publicação da EC 41/2003, que dá a redação citada                                                        | ✅                            |
| ingresso                                      | sem restrição                      | o art. 40, § 1º, I não condiciona a ingresso                                                                     | ✅ por ausência               |
| `integral: S` (0006)                          | proventos integrais                | exceção do art. 40, § 1º, I e do art. 20, *caput* — "acidente em serviço, moléstia profissional ou doença grave" | ⚠️ **rol não vinculado**      |
| `integral: N` (0007)                          | proporcionais ao tempo             | regra do art. 40, § 1º, I e do art. 20, *caput*                                                                  | ✅                            |
| `tipo_calculo: Valor Médio` (0006)            | média das 80% maiores              | `lce-432-2008/art-45/lce-672-2012`                                                                               | ✅                            |
| `tipo_calculo: Proporcionalidade Dias` (0007) | fração em dias                     | `lce-432-2008/art-17/original` (§ 2º: "em número de dias") + `art-20-par-14`                                     | ✅ (só 0007)                  |
| `paridade: N`                                 | reajuste para preservar valor real | `lce-432-2008/art-62/original`                                                                                   | ✅                            |
| aplicabilidade pós-2021                       | regime preservado                  | `ece-146-2021/art-4/original`                                                                                    | ⚠️ **ver §"O prazo de 2024"** |

**Dispositivo sem critério em 0006**: `lce-432-2008/art-17/original` é a
regra de **proporcionalidade**. A regra 0006 é a integral. Não há critério
dela que o art. 17 funde — provável excesso de vínculo herdado do par 0007.

**Critério sem dispositivo em 0006**: a regra é integral *porque* a
incapacidade decorre de doença grave, contagiosa ou incurável — e o rol que
define quais são, `lce-432-2008/art-20-par-9/original`, **não está
vinculado** (está em 0008/0009, que o citam). É o dispositivo que mais
diretamente decide a aplicação da regra, e é o que falta.

### 0008 e 0009 — regime de transição do art. 6º-A

| critério                                    | valor                                   | fundado por                                                                                                                            | fecha?        |
| ------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| tipo de benefício                           | invalidez permanente                    | `cf88/art-40-par-1-inc-i/ec-41-2003` + `lce-432-2008/art-20/original`                                                                  | ✅            |
| `data_adm_ate: 31/12/2003`                  | ingresso até a publicação da EC 41/2003 | `ec-41-2003/art-6a/ec-70-2012` — "que tenha ingressado no serviço público até a data de publicação desta Emenda Constitucional"        | ✅            |
| `tipo_calculo: Remuneração de Contribuição` | base é a remuneração do cargo           | `ec-41-2003/art-6a/ec-70-2012` — "calculados com base na remuneração do cargo efetivo"                                                 | ✅            |
| `paridade: S`                               | reajuste com paridade                   | `ec-41-2003/art-6a/ec-70-2012` — "não sendo aplicáveis [...] os §§ 3º, 8º e 17 do art. 40" (afastar o § 8º é o que devolve a paridade) | ✅            |
| `integral: S` (0008)                        | integrais                               | exceção do art. 20, *caput* + rol do `art-20-par-9/original`                                                                           | ✅            |
| `integral: N` (0009)                        | proporcionais                           | regra do art. 20, *caput*                                                                                                              | ✅            |
| aplicabilidade pós-2021                     | regime preservado                       | `ece-146-2021/art-4/original`                                                                                                          | ⚠️ ver abaixo |

O art. 6º-A funda **três** critérios de uma vez — o corte de ingresso, a
base de cálculo e a paridade. É o exemplo mais limpo do que a conferência
mostra e o achatamento esconde: no `dispositivos:` ele é uma linha entre
sete, indistinguível das demais.

## Três coisas que a conferência revelou

### 1. O art. 40, § 1º, III não funda critério nenhum — nas quatro

`cf88/art-40-par-1-inc-iii/ec-103-2019` está vinculado nas quatro regras.
Percorrendo os critérios de cada uma — tipo de benefício, sexo, janelas de
ingresso e de direito, integralidade, tipo de cálculo, paridade — **nenhum
é fundado por ele**. O inciso III trata de aposentadoria **voluntária por
idade**.

Isso confirma, por outro caminho, as pendências **P-3** e **P-4** já
registradas em
[`base-normativa-invalidez-incapacidade.md`](base-normativa-invalidez-incapacidade.md).

Sobre a "2ª parte" que a prosa de 0008/0009 invoca: o inciso **de fato se
biparte** — "no âmbito da União, aos 62 [...] se mulher, e aos 65 [...] se
homem" / "e, no âmbito dos Estados, do Distrito Federal e dos Municípios,
na idade mínima estabelecida mediante emenda às respectivas Constituições" —
e é a segunda metade que alcança o RPPS estadual. A leitura textual existe.
Mas **nenhuma das duas metades funda critério de incapacidade**, então o
recorte não socorre a citação. É o que a pergunta da P13.1 revela e a
leitura textual sozinha não revelava.

### 2. O prazo de 31/12/2024 da ECE 146/2021 não aparece nas quatro

As quatro citam `ece-146-2021/art-4/original`, cujo texto condiciona:

> [...] observará os requisitos e os critérios exigidos pela legislação
> vigente até a data de entrada em vigor desta Emenda Constitucional,
> **desde que sejam cumpridos até 31 de dezembro de 2024**, sendo
> assegurada a qualquer tempo.

Mas as quatro têm `data_direito_ate: 31/12/2099` — a sentinela, que o
catálogo não interpreta (P5). Outras regras do catálogo **gravam
31/12/2024** nesse campo (0012 e 0013, por exemplo).

Ou o art. 4º não é o fundamento da janela temporal dessas quatro, ou a
janela está gravada errada. A conferência não decide qual — mas mostra que
o vínculo declarado e o valor gravado **discordam**, e isso não aparecia
enquanto o vínculo era uma lista achatada.

### 3. O critério que distingue cada par não é parametrizado

0006 difere de 0007, e 0008 de 0009, pela **causa da incapacidade**:
acidente em serviço, moléstia profissional ou doença grave (integral) versus
as demais causas (proporcional). Isso está no art. 40, § 1º, I e no art. 20,
*caput*, e o rol está no art. 20, § 9º.

Nenhuma coluna do Sisprev registra a causa. O que o cadastro grava —
`integral: S/N` — é o **resultado**, não o critério. É a **Q6**, aberta, e a
conferência a reencontra pelo lado do fundamento em vez do lado do dado.

## O que decorre, e para quem

**Para o auditor** (ato humano, achado próprio):

1. Decidir a citação do art. 40, § 1º, III nas quatro — P-3/P-4 já
   registradas, agora com a conferência mostrando que ele não funda critério.
2. Decidir a discordância entre `data_direito_ate: 31/12/2099` e o prazo de
   31/12/2024 do art. 4º da ECE 146/2021.

**Vínculos a acrescentar**, se as decisões acima confirmarem a leitura:

- `lce-432-2008/art-20-par-9/original` em **0006** — o rol de doenças graves
  é o que sustenta a integralidade, e é o que falta.

**Vínculo a remover**, idem:

- `lce-432-2008/art-17/original` de **0006** — regra de proporcionalidade
  numa regra integral.

Nada disso foi aplicado. A conferência propõe; a decisão é de quem audita.
