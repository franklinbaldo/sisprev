---
type: Achado
id: achado-0051
nome: regra-0039 e regra-0040 fundam os requisitos numa redação extinta em 2003 e se aplicam a quem ingressou depois disso — o art. 4º da ECE 146/2021 não a ressuscita
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0039.md
  - /regras/regra-0040.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0039` e `regra-0040` (aposentadoria voluntária de professor, o par
masculino/feminino) fundam os seus **requisitos** no art. 40, § 1º, III, "a" e no
§ 5º da Constituição Federal **na redação da EC 20/1998**, e se aplicam a quem
ingressou no serviço público **após 31/12/2003**.

Aquela redação deixou de vigorar em **30/12/2003**. A população que as regras
descrevem começa no dia seguinte ao seu último dia de vigência.

Não é defeito de janela: é defeito de **fundamento**. Fechar
`data_direito_ate` em 31/12/2024, que é a correção proposta pelo
[`achado-0022`](achado-0022.md) para as sete regras daquele grupo, deixaria estas
duas aplicando por três anos requisitos que nunca lhes foram aplicáveis.

# Evidências

`verificacao: manual`. A acusação se apoia em três datas, todas conferidas, e a
`fundamentacao_integral` das duas regras é que separa os eixos — não é leitura
imputada a ela:

> Aposentadoria especial de professor, com proventos integrais (cálculo por
> média) e sem paridade, com base no artigo 40, §1º, inciso III, alínea "a" e
> §5º, da Constituição Federal, **com redação dada pela Emenda Constitucional nº
> 20/1998, quanto ao preenchimento dos requisitos de aposentadoria**; artigo 40,
> §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, **no que
> tange à fórmula de cálculo e reajuste**; artigos 24, 45 e 62 da Lei
> Complementar Estadual nº 432/2008, e no artigo 4º da Emenda Constitucional
> Estadual nº 146/2021.

O campo atribui explicitamente à redação da EC 20/1998 "o preenchimento dos
requisitos" — e essa **separação de eixos é legítima**, não idiossincrasia de
redação: a própria LCE 1.100/2021 trata requisito e fórmula por dispositivos
distintos, preservando um sem preservar o outro (os §§ 13 e 14 do art. 30
ressalvam "o direito adquirido a outra fórmula"). O defeito não é separar os
eixos; é qual redação está citada no eixo dos requisitos. E:

| fato                                                                | data           | fonte                                                           |
| ------------------------------------------------------------------- | -------------- | --------------------------------------------------------------- |
| fim da vigência da redação da EC 20/1998 do art. 40, § 1º, III, "a" | **30/12/2003** | `okf/dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md` |
| fim da vigência da redação da EC 20/1998 do art. 40, § 5º           | **30/12/2003** | `okf/dispositivos/cf88/art-40-par-5/ec-20-1998.md`              |
| `data_adm_apos` das duas regras (ingresso **após**)                 | **31/12/2003** | frontmatter                                                     |
| `data_direito_apos` das duas regras                                 | 18/10/2021     | frontmatter                                                     |

As duas datas de vigência são as da EC 41/2003, publicada em 31/12/2003, que deu
nova redação ao *caput* do art. 40 e ao § 1º — e os dois vínculos declarados
pelas regras apontam para a redação anterior a ela.

## Por que o art. 4º da ECE 146/2021 não alcança

A defesa disponível é que o art. 4º preserva a legislação anterior, e as regras o
citam e o vinculam. Ela não funciona, e o motivo está no próprio texto:

> ...observará os requisitos e os critérios exigidos pela **legislação vigente
> até a data de entrada em vigor desta Emenda Constitucional**, desde que sejam
> cumpridos até 31 de dezembro de 2024...

O art. 4º congela o estado da legislação **no momento em que a emenda entrou em
vigor**, em 2021. Naquele momento a redação vigente do art. 40, § 1º, III era a
da **EC 103/2019**; a da EC 20/1998 havia sido substituída dezoito anos antes,
primeiro pela EC 41/2003 e depois pela EC 103/2019. Uma cláusula que preserva o
que está em vigor não ressuscita o que já não estava.

## Por que direito adquirido também não salva

O caminho alternativo seria dizer que a regra atende a quem adquiriu direito sob
a redação da EC 20/1998, o que dispensaria o art. 4º (art. 5º, XXXVI da CF e
Súmula 359 do STF). **A própria janela de admissão exclui essa leitura**: as duas
regras se aplicam a quem ingressou **após 31/12/2003**, e ninguém dessa população
poderia ter reunido requisitos sob uma redação que se extinguiu em 30/12/2003.

O par complementar confirma que o corte é deliberado e não descuido: `0080`/`0081`
gravam `data_adm_apos: 31/12/2003` para o trilho de cálculo do art. 24 da LCE
1.100/2021, e `0035`/`0036` gravam `data_adm_ate: 31/12/2003` para o trilho do
art. 25 — os dois lados de um mesmo divisor. Estas duas estão do lado de depois.

## O que está conferido e não é defeito

Registrado para que a acusação fique restrita ao que sustenta: os demais
elementos das duas regras foram conferidos e fecham. Os arts. 24, 45 e 62 da LCE
432/2008 estão citados, vinculados e transcritos; a atribuição do cálculo e
reajuste aos §§ 3º e 8º do art. 40 na redação da EC 41/2003 é coerente com
`tipo_calculo` por média e `paridade: N`; `apos_especial: S` é fundado no § 5º
(magistério) — cuja redação, aliás, é o segundo dispositivo alcançado por este
achado.

# Consequência prática

`FUNDAMENTACAO_INTEGRAL` é campo deployável: o ato de concessão entregue ao
professor invoca, como fundamento dos seus requisitos, texto constitucional que
não vigia quando ele ingressou nem quando adquiriu o direito. É vício de
motivação num ato de aposentadoria.

E há a consequência de método, que é a razão da severidade: **este achado impede
que a correção do `achado-0022` seja aplicada uniformemente às sete regras**.
Gravar `31/12/2024` nas duas sem decidir o fundamento produziria uma regra
formalmente arrumada e materialmente sem base — pior que o estado atual, porque a
janela consertada sugere que a regra foi conferida.

`bloqueante` pela mesma razão do `achado-0022`: o campo é entregue, e o defeito é
no fundamento do requisito, não em anotação de auditoria.

# Questão a investigar

1. **Qual redação a regra pretendia invocar.** Três hipóteses, nenhuma
   verificada. A da **EC 103/2019** do inciso III, que era a vigente em 2021 —
   mas ela não tem alíneas, então "alínea 'a'" não existiria nela. A da **EC
   41/2003**, que tem a alínea e vigeu de 31/12/2003 a 12/11/2019 — compatível
   com o ingresso após 31/12/2003, e é o vizinho imediato do documento vinculado.
   Ou o art. 24 da **LCE 432/2008**, já citado no mesmo campo, que é a norma
   estadual do magistério. A segunda é a mais econômica e continua hipótese.

2. **Se corrigir o fundamento muda a janela.** Se a redação correta for a da EC
   41/2003, ela se extinguiu em 12/11/2019 — antes de a janela abrir em
   18/10/2021 —, e então a regra volta a depender do art. 4º e do prazo de
   31/12/2024, isto é, recai no `achado-0022`. Se for o art. 24 da LCE 432/2008,
   a análise é outra: aquele artigo deixou de vigorar em 18/10/2021, primeiro dia
   da janela. Nenhuma das saídas é indiferente à janela, e é por isso que os dois
   achados têm de ser decididos juntos.

3. **Se as duas regras deveriam existir.** O art. 4º só preserva o que vigia em
   2021, e o regime novo tem a sua própria regra de magistério: o **art. 33 da
   LCE 1.100/2021**. E ela já está no catálogo — `regra-0107`/`0108` a vinculam,
   **sem corte de ingresso** (`data_adm_apos: 01/01/1950`,
   `data_adm_ate: 31/12/2099`), de modo que a população destas duas (magistério,
   ingresso após 31/12/2003) já está coberta por regras fundadas na norma certa.

   Isso **não** decide se `0039`/`0040` devem ser revogadas — é decisão de quem
   responde pelo catálogo —, mas remove o argumento de que revogá-las abriria
   lacuna. Ver a [análise jurídica](../../../docs/analysis/analise-juridica-art-4-ece-146.md)
   §9. Registrado também que as duas regras do art. 33 têm defeito próprio de
   janela ([`achado-0052`](achado-0052.md)), que é o espelho deste: elas gravam a
   janela que estas duas deveriam ter, e vice-versa.
