---
type: Achado
id: achado-0047
nome: Dezesseis regras gravam o corte de 31/12/2024 sem vincular a norma que o institui, por três causas distintas — e em quatro delas a emenda não aparece em campo nenhum
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0010.md
  - /regras/regra-0011.md
  - /regras/regra-0028.md
  - /regras/regra-0029.md
  - /regras/regra-0030.md
  - /regras/regra-0031.md
  - /regras/regra-0093.md
  - /regras/regra-0094.md
  - /regras/regra-0095.md
  - /regras/regra-0096.md
  - /regras/regra-0107.md
  - /regras/regra-0108.md
  - /regras/regra-0109.md
  - /regras/regra-0110.md
  - /regras/regra-0111.md
  - /regras/regra-0112.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Vinte e oito regras gravam `data_direito_ate: 31/12/2024`. Essa data não é
arbitrária: é o prazo do art. 4º da ECE 146/2021, transcrito em
[`achado-0022`](achado-0022.md) — "desde que sejam cumpridos até 31 de dezembro
de 2024". Ela **só** aparece no catálogo por causa daquele artigo.

Em **dezesseis** dessas regras não há vínculo `dispositivos:` a
`ece-146-2021/art-4/original`. A janela mais restritiva da regra está gravada, e
o catálogo não fecha o laço com a norma que a impõe.

Este é o espelho do [`achado-0022`](achado-0022.md): lá, sete regras vinculam o
artigo e não gravam o prazo; aqui, dezesseis gravam o prazo e não vinculam o
artigo. Defeitos opostos, correções opostas, por isso dois achados.

# Evidências

`verificacao: manual`: a contagem junta `data_direito_ate`, `dispositivos:` e a
leitura dos campos de texto, e é reproduzível — mas a premissa (que 31/12/2024
vem do art. 4º e de nada mais) é leitura da norma, não do dado.

As dezesseis não têm o mesmo defeito. São **três causas**, e cada uma pede
conserto diferente:

| causa                                                              | regras                                                                         | o que falta                             |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------- |
| cita o art. 4º em campo de fundamentação, **sem numerar a emenda** | `0093`, `0094`                                                                 | o número, e então o vínculo             |
| cita a emenda **apenas no `nome`**                                 | `0010`, `0011`, `0028`, `0029`, `0095`, `0096`, `0109`, `0110`, `0111`, `0112` | a citação num campo de fundamentação    |
| **nenhum campo** menciona a emenda                                 | `0030`, `0031`, `0107`, `0108`                                                 | tudo — a janela não tem fonte declarada |

## Duas regras citam o artigo e não a emenda

`regra-0093` e `regra-0094` trazem, no fim da `fundamentacao_integral`:

> ... art. 4° da Emenda à Constituição Estadual - CF

O artigo está lá. A emenda não tem número, e é só isso que separa estas duas da
forma completa. A correlação é perfeita e vale registrar: **26 regras do
catálogo citam esse artigo em campo de fundamentação; as 24 que numeram a emenda
são exatamente as 24 que a vinculam, e as 2 que não numeram são exatamente as 2
que não vinculam.** O vínculo acompanha o número, não a citação.

Aqui o conserto é o menor dos três — acrescentar "nº 146/2021" — e depois o
vínculo se torna declarável.

## Dez citam só no rótulo

`regra-0010`, `regra-0011`, `regra-0028`, `regra-0029`, `regra-0095`,
`regra-0096`, `regra-0109`, `regra-0110`, `regra-0111`, `regra-0112`.

Exemplo, a `regra-0011` nos campos que importam:

| campo                                          | valor                                                                                  |
| ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| `nome`                                         | Pensão por Morte oriunda do Art. 3º da EC nº 47/2005 **c/c art. 4º da EC nº 146/2021** |
| `fundamentacao_integral`                       | art. 40, § 7, I da CF/88 com redação da EC 41/2003 c/c art. 3º, § único da EC 47/2005  |
| `fundamentacao` / `fundamentacao_proporcional` | *(vazios)*                                                                             |
| `data_direito_ate`                             | **31/12/2024**                                                                         |

A citação existe, no campo errado. E o campo em que ela está é justamente o
único que **não é fundamentação**: `nome` está **fora** da chave material do
`P2_IGUALDADE_MATERIAL_ATIVA` e `FUNDAMENTACAO*` está **dentro**. A norma que
fecha a janela mora, nessas dez, no único lugar que o detector de igualdade
ignora — e é por isso que o defeito nunca apareceu como detecção.

Quatro delas exigem cuidado extra, e a primeira versão deste achado errou nisso:
`regra-0109` a `regra-0112` **citam** a ECE 146/2021 na
`fundamentacao_integral`, mas pelo **art. 7º, §§ 2º e 3º** — outra via, com
requisitos próprios (idade mínima e pedágio) e sem prazo. Uma busca por "146" no
texto as faz parecer completas; ler o artigo citado mostra que, quanto ao art.
4º, elas estão na mesma situação das outras seis. A divergência entre a via da
janela e a via da fundamentação nessas quatro é defeito próprio, tratado em
[`achado-0039`](achado-0039.md).

Por isso **não há vínculo a acrescentar** nas dez: um vínculo afirma *"a
fundamentação desta regra cita esta provisão"* (RFC 0008, e
`docs/spec/dispositivo.md`), e a fundamentação delas não cita o art. 4º.
Vinculá-lo aqui seria falsificar o vínculo para consertar o dado — o mesmo que a
recusa registrada nas `regra-0021`/`0022` evita. O conserto, se houver, é na
fundamentação; o vínculo vem depois, como consequência.

## Quatro não citam em campo nenhum

`regra-0030`, `regra-0031`, `regra-0107`, `regra-0108`. Nem o art. 4º, nem a
emenda, em `nome`, `fundamentacao`, `fundamentacao_integral` ou
`fundamentacao_proporcional`: **zero ocorrências nos quatro campos, nas quatro
regras**. Elas gravam 31/12/2024 e o catálogo inteiro não registra por quê.

## A forma completa existe em mais de um décimo do catálogo

Dez regras (`0097`–`0106`) gravam o prazo, citam o artigo numerado na
fundamentação **e** o vinculam. É a forma completa, e ela ser majoritária entre
as que citam faz das dezesseis desvio de um padrão interno, não ausência de
padrão.

# Consequência prática

O dano é sobre a **motivação do ato**, não sobre a elegibilidade. Diferente do
`achado-0022`, aqui a janela está gravada como (provavelmente) deveria: quem tem
requisito completado depois de 31/12/2024 é corretamente excluído. O que falta é
o fundamento.

Para as dez, o documento entregue ao servidor tem a citação — no rótulo. Para as
quatro, a exclusão acontece sem que nenhum campo diga qual norma a impõe: uma
pessoa cujo requisito se completou em 2025 é recusada por um prazo que a regra
não fundamenta. É a diferença entre decisão motivada e decisão apenas correta.

Há um efeito de auditoria também: nas quatro, se alguém "corrigir" a janela para
a sentinela por não achar fundamento para ela, nada detectaria — não há detector
de janela, e a chave material do P2 mudaria de um jeito que dissolve ou forma
grupo sem que fato jurídico algum tenha mudado.

# Questão a investigar

1. **Se as quatro sem citação alguma têm outro fundamento.** Antes de assumir
   que 31/12/2024 veio da ECE 146/2021 nelas, cabe conferir se alguma outra
   norma estadual fixa a mesma data. A coincidência é forte, e `regra-0030`/
   `0031` têm janela abrindo em 04/12/2015 (compulsória, redação da EC 88/2015),
   o que combina com resguardo — mas coincidência de data não é fundamento, e
   nenhuma delas o declara.

2. **Se a correção é escrever na fundamentação ou tirar da janela.** As duas
   fecham a incoerência e têm efeitos opostos sobre quem completou requisito em
   2025\. `FUNDAMENTACAO*` e `data_direito_ate` são ambos deployáveis; a escolha é
   de quem responde pelo produto.

3. **Se `nome` pode carregar citação que a fundamentação não tem.** Dez regras
   fazem isso hoje. Se a resposta for não, o padrão de nome do
   [`achado-0020`](achado-0020.md) tem de dizê-lo — e ali a questão está aberta
   como "qual padrão adotar", sem tocar nesta. Se for sim, então `nome` é fonte
   normativa parcial, e nada no repositório o trata como tal.

4. **Se numerar a emenda em `0093`/`0094` é conserto suficiente.** A correlação
   número↔vínculo sugere que sim, mas as duas têm outros defeitos que interagem
   ([`achado-0011`](achado-0011.md), [`achado-0044`](achado-0044.md),
   [`achado-0045`](achado-0045.md)), e a ordem entre eles não está decidida.
