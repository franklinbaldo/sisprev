---
type: Achado
id: achado-0043
nome: O nome e as janelas de regra-0095 e regra-0096 são de uma transição; a fundamentação e os cinco vínculos são da regra permanente do professor, e os arts. 25 e 27, I que ela cita contradizem paridade e tipo_calculo
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0095.md
  - /regras/regra-0096.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0095` (masculino) e `regra-0096` (feminino) são um par idêntico em tudo
menos `sexo`. Cada uma descreve, em campos diferentes do mesmo frontmatter,
**duas regras diferentes**:

| onde                     | o que diz                                                                                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nome`                   | `Art. 40, §1º, III, "a" da CF c/c art. 4º da EC 146/21 (Magistério)` — a **transição** preservada                                                                    |
| `fundamentacao_integral` | art. 40, §§ 5º e 1º, III da CF na redação da **EC 103/2019** + arts. 25, 27, I e 33 da LCE 1.100/2021, "**regra permanente** da aposentadoria especial de professor" |
| `dispositivos:`          | os cinco da regra permanente, espelhando a fundamentação                                                                                                             |
| janelas                  | `data_direito_ate: 31/12/2024` — prazo do art. 4º da ECE 146/2021, que só o `nome` cita                                                                              |

Nem a alínea "a" nem o art. 4º da ECE 146/2021 — as duas provisões que o
`nome` anuncia — aparecem na fundamentação ou em `dispositivos:`. E a "regra
permanente" que a fundamentação afirma ser não pode ter prazo de implementação
em 31/12/2024, porque é isso que "permanente" nega.

Sobrepondo-se a essa troca, há uma contradição interna que não depende de
resolvê-la: os dois artigos de cálculo e reajuste que a regra **cita e
vincula** determinam integralidade e paridade, e os campos gravam o contrário.

# Evidências

## A fundamentação é a da regra permanente, e o catálogo tem as originais

A cauda de citação da `fundamentacao_integral` de `0095`/`0096` é **idêntica
caractere a caractere** à de `regra-0041`, `regra-0042`, `regra-0107` e
`regra-0108`. A diferença é só o preâmbulo: as quatro começam por
"Aposentadoria especial de professor, com proventos integrais (cálculo por
integralidade) e com paridade, com base no"; `0095`/`0096` começam
diretamente em "Artigo 40, § 5°, da Constituição Federal". Fora isso, os 343
caracteres de `0095`/`0096` são o final exato dos 460 daquelas (sha256 das
strings completas: `924a8cad4737…` nas duas de `0095`/`0096`,
`602f65b81216…` nas quatro).

São, portanto, **seis** regras de professor sob a mesma citação. As
parametrizações são três:

| regras          | `data_adm_ate` | `data_direito_apos` | `data_direito_ate` | `integral` | `paridade` | `tipo_calculo`              |
| --------------- | -------------- | ------------------- | ------------------ | ---------- | ---------- | --------------------------- |
| `0041` / `0042` | 31/12/2003     | 18/10/2021          | 31/12/2099         | `S`        | `S`        | Remuneração de Contribuição |
| `0107` / `0108` | 31/12/2099     | 31/12/2003          | 31/12/2024         | `N`        | `N`        | Valor Médio                 |
| `0095` / `0096` | **31/12/2024** | 31/12/2003          | 31/12/2024         | `S`        | `N`        | Valor Médio                 |

`0041`/`0042` é a única das três coerente com a citação, e ponto por ponto:
`data_adm_ate: 31/12/2003` é o corte do art. 25, `data_direito_apos: 18/10/2021` é a vigência da LCE 1.100/2021, `data_direito_ate` é sentinela
porque a regra é permanente, e integralidade e paridade correspondem aos
arts. 25 e 27, I. O `achado-0016` já registra que `0107`/`0108` gravam o
oposto sob o mesmo texto. `0095`/`0096` é a terceira variante, e é a única em
que o `nome` aponta para fora da citação.

## Os dois artigos citados contradizem dois campos gravados

Conferido em `fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`
(sha256 `bcac2238855c79d940b4fabd772841462ed58b6ab3d37b1b150bd0750ef69a99`,
no `manifesto.yaml`), que é a `fonte:` dos próprios documentos vinculados:

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de
> 2003** [...] corresponderá à **totalidade da remuneração no cargo efetivo**
> em que se der a aposentadoria.

> **Art. 27.** [...] **I** - de acordo com o disposto no **art. 7° da Emenda
> Constitucional n° 41**, de 19 de dezembro de 2003, para aposentadorias
> concedidas a servidor público que tenha ingressado no serviço público em
> cargo efetivo **até 31 de dezembro de 2003** [...]

O art. 7º da EC 41/2003, para o qual o art. 27, I remete, é a regra da
paridade — proventos "revistos na mesma proporção e na mesma data, sempre que
se modificar a remuneração dos servidores em atividade" (conferido em
`fontes-oficiais/arquivos/planalto-emc41.htm`, sha256 `af74d433…`; está
transcrito no bundle como `ec-41-2003/art-7/original`).

Três desencontros, todos entre o que a regra cita e o que a regra grava:

| o que o dispositivo citado determina            | o que a regra grava                         |
| ----------------------------------------------- | ------------------------------------------- |
| art. 25 — totalidade da remuneração do cargo    | `tipo_calculo: Valor Médio`                 |
| art. 27, I — reajuste paritário (art. 7º EC 41) | `paridade: N`                               |
| arts. 25 e 27, I — ingresso **até** 31/12/2003  | `data_adm_ate: 31/12/2024` (sem corte real) |

O art. 33 — o terceiro artigo estadual citado — é a redução de cinco anos de
idade do professor, e ele **está** fundado: "O professor que comprove tempo de
efetivo exercício, exclusivamente, nas funções de magistério [...] terá o
requisito de idade reduzido em 5 (cinco) anos". Ele funda o `apos_especial: S`
e nada mais; não decide cálculo nem reajuste.

## `data_adm_ate: 31/12/2024` põe no eixo de admissão um prazo de outro eixo

Só **seis** das 112 regras gravam 31/12/2024 em `data_adm_ate`: `0093`,
`0094`, `0095`, `0096`, `0109` e `0110`. A data tem uma fonte única no corpus
inteiro — o art. 4º da ECE 146/2021, transcrito em
`ece-146-2021/art-4/original` a partir do PDF do SAPL/ALE-RO
(sha256 `947726c7…`) — e o que ela fixa lá é **prazo para cumprir requisitos**,
não corte de ingresso:

> Art. 4º A concessão de aposentadoria ao servidor público [...] observará os
> requisitos e os critérios exigidos pela legislação vigente até a data de
> entrada em vigor desta Emenda Constitucional, **desde que sejam cumpridos
> até 31 de dezembro de 2024**, sendo assegurada a qualquer tempo.

`0095`/`0096` já gravam esse prazo no eixo certo (`data_direito_ate: 31/12/2024`). Repeti-lo em `data_adm_ate` afirma que serve de regra a quem
ingressou em 2024 — o que nenhum dispositivo citado permite (o art. 25 corta
em 2003) e o que a própria matéria torna impossível (a aposentadoria voluntária
por tempo de contribuição exige 30 ou 35 anos). O efeito é inócuo hoje, mas o
valor gravado é falso. §3.3 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)
registra o mesmo defeito em `0109`/`0110`, contra o corte de ingresso do art. 7º
da ECE 146/2021.

O [`achado-0047`](achado-0047.md), da mesma rodada, alcança `0095`/`0096` pelo
lado complementar: a ECE 146/2021 **não é citada em campo de fundamentação
nenhum** destas duas, e o prazo dela está gravado em dois eixos. Os dois
achados são compatíveis — aquele registra a citação ausente, este registra que
a fundamentação presente é de outra regra.

## O que os detectores veem, e não é isto

`0095`/`0096` aparecem em `P1_NOME_REPETIDO` por terem o mesmo `nome` entre si
(fingerprint `sha256:653eb623f21d…`), e **em nenhuma outra detecção**. Não
formam grupo P2 porque `sexo` as separa, o que é a leitura certa. `nome`,
`fundamentacao_integral` e as datas não são lidos por detector nenhum quanto ao
conteúdo. Daí `verificacao: manual`.

# Consequência prática

`nome` é a ferramenta de seleção apresentada ao usuário
([`docs/spec/regra.md`](../../../docs/spec/regra.md), "O papel do campo
`nome`") e `fundamentacao_integral` é o texto entregue no documento do
servidor. Aqui os dois apontam para regras diferentes, e as duas são regras
que existem no catálogo — a transição da alínea "a" (a família
`0093`/`0094`, e `0039`/`0040` no magistério) e a permanente do art. 33
(`0041`/`0042`, `0107`/`0108`). Quem escolhe pelo nome e quem confere pela
fundamentação chegam a hipóteses distintas na mesma linha.

Sobre o cálculo, o efeito é o do `achado-0016` invertido: aqui a regra
concede **menos** do que os dispositivos que ela cita determinam — média em
vez de totalidade da remuneração, sem paridade —, e entrega um documento que
cita justamente os dois artigos que mandam o contrário. É a direção que
prejudica o servidor, e por isso a mais provável de virar litígio.

Nada aqui afirma o que o motor faz. As duas são `simulavel: S`, e em regra
simulável o motor não lê a fundamentação: `integral`, `paridade` e
`tipo_calculo` decidem o valor. O que se prova é sobre o registro e sobre o
documento.

# Questão a investigar

1. **Qual das duas regras `0095`/`0096` pretendem ser.** A leitura mais
   simples é que são a transição que o `nome` anuncia — as quatro datas de
   `0095`/`0096` são, valor por valor, as de `0093`/`0094`, que é a **mesma
   transição sem magistério**, e `Valor Médio`/`paridade: N` são o tratamento
   dela (art. 40, §§ 3º e 17, sem paridade). Nessa leitura o que está errado é
   `fundamentacao_integral` inteira, e o par se aproxima de `0039`/`0040`, que
   é o magistério da mesma transição e cita a alínea "a", o § 5º da EC
   20/1998, o art. 4º da ECE 146/2021 e os arts. 24, 45 e 62 da LCE 432/2008.
   A leitura oposta — que a fundamentação está certa e o par é uma terceira
   variante da permanente — colide com `data_direito_ate: 31/12/2024`.
   **Escolher é reescrever campo deployável**, e é decisão de quem responde
   pelo produto.

2. **Se seis regras de professor sob uma citação são seis regras.**
   `0041`/`0042`, `0095`/`0096` e `0107`/`0108` têm parametrizações
   incompatíveis entre si sob a mesma fundamentação. Ou a citação é a de uma
   regra só e cinco linhas estão erradas, ou são três regras cujas
   fundamentações deveriam divergir. O `achado-0016` deixa a mesma pergunta
   aberta para quatro delas; este a estende para seis. Não se propõe
   consolidação: granularidade é escolha do IPERON
   ([`docs/spec/regra.md`](../../../docs/spec/regra.md)).

3. **Nenhum vínculo é proposto, e é a recusa correta.** O art. 4º da ECE
   146/2021 e a alínea "a" do art. 40, § 1º, III só aparecem no `nome`, que
   não é campo de fundamentação; declarar vínculo a partir dele afirmaria que
   a fundamentação cita o que ela não cita (RFC 0008). Se a fundamentação for
   reescrita na direção da hipótese 1, os vínculos passam a ser possíveis — e
   os documentos existem, inclusive `cf88/art-40-par-1-inc-iii-al-a/ec-41-2003`,
   que é a redação contemporânea à abertura da janela.
