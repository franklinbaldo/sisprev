---
type: Achado
id: achado-0052
nome: regra-0107 e regra-0108 fundam-se no regime novo e abrem o direito em 31/12/2003, dezoito anos antes da lei que invocam
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0107.md
  - /regras/regra-0108.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0107` e `regra-0108` (aposentadoria especial de professor, o par
masculino/feminino) fundam-se **inteiramente no regime novo**: art. 40, § 5º da
CF na redação da **EC 103/2019**, e arts. 25, 27, I e **33 da LCE 1.100/2021**.
Os cinco vínculos declarados são todos posteriores a 2019.

A janela de direito delas é `[31/12/2003, 31/12/2024)`.

Ela abre **dezoito anos antes** da lei estadual que a funda e **dezesseis antes**
da redação constitucional que ela cita. E fecha num prazo cuja norma
instituidora — o art. 4º da ECE 146/2021 — nenhum campo delas menciona.

# Evidências

`verificacao: manual`. Nenhum detector produz isto: não há detector de janela, e
o que os detectores veem nessas duas é outra coisa (o `P1_NOME_REPETIDO` com
`0041`/`0042`, e o `P9_INTEGRAL_SEM_FUNDAMENTACAO` em cada uma).

A `fundamentacao_integral`, idêntica nas duas:

> Aposentadoria especial de professor (...) com base no artigo 40, § 5°, da
> Constituição Federal, **com redação dada pela Emenda Constitucional nº
> 103/2019**, artigos **25, 27, I; 33, da Lei Complementar nº 1.100/2021** e
> artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal (...)

Confrontada com as vigências, todas conferidas no bundle:

| norma citada                             | em vigor desde | janela abre em |
| ---------------------------------------- | -------------- | -------------- |
| art. 40, § 5º, CF, red. EC 103/2019      | 13/11/2019     | **31/12/2003** |
| art. 40, § 1º, III, CF, red. EC 103/2019 | 13/11/2019     | **31/12/2003** |
| arts. 25, 27-I e 33 da LCE 1.100/2021    | 18/10/2021     | **31/12/2003** |

Nenhuma das cinco existia em 31/12/2003. A data gravada é o marco da **EC
41/2003**, que nenhuma das duas cita.

## O prazo de 2024 também não tem fonte declarada aqui

`data_direito_ate: 31/12/2024` é o prazo do art. 4º da ECE 146/2021 — a única
norma do corpus a fixá-lo. Estas duas regras **não o citam em campo nenhum**,
nem no `nome`, e é por isso que já estão em
[`achado-0047`](achado-0047.md), no grupo das quatro cujo corte não tem fonte
declarada.

Aqui o achado acrescenta o que aquele não podia dizer sem esta conferência: sendo
regras do **regime novo**, elas provavelmente **não deveriam ter prazo algum**. A
LCE 1.100/2021 não tem regra de transição nem menciona 2024 — conferido por busca
exaustiva na compilação oficial, registrada na
[análise jurídica do art. 4º](../../../docs/analysis/analise-juridica-art-4-ece-146.md)
§9. Um regime que substitui o anterior não se extingue em 2024.

Então a leitura mais provável é que **as duas datas estão erradas na mesma
direção**: a janela deveria ser `[18/10/2021, 31/12/2099)` — vigência da LCE
1.100/2021 até a sentinela —, que é exatamente a janela que `regra-0039`/`0040`
gravam com a fundamentação errada. As duas famílias parecem ter trocado janelas.

**Isso é hipótese, não conclusão.** O que está provado é a incompatibilidade
entre os vínculos e a data de abertura; qual das pontas cede é decisão de quem
responde pelo campo.

## O que não é este achado

Estas duas regras têm outros dois defeitos, ambos já autorados, e nenhum é
alcançado aqui:

- a `fundamentacao_integral` afirma "cálculo por integralidade" e "com paridade"
  enquanto o frontmatter grava `tipo_calculo: Valor Médio` e `paridade: N` —
  [`achado-0016`](achado-0016.md);
- `integral: N` com a proporcional vazia — `achado-0009`, via
  `P9_INTEGRAL_SEM_FUNDAMENTACAO`.

O defeito deste achado é só a janela, e ele é independente daqueles: corrigi-los
não a move.

# Consequência prática

`data_direito_apos` decide elegibilidade e é campo entregue. Lida como está, a
regra concede sob a lei estadual de 2021 a quem completou requisitos em 2004 —
dezessete anos antes de ela existir. Se o Sisprev a aplica, é concessão sob norma
que não vigia no fato gerador; se não aplica, a janela é letra morta que
ninguém confere.

Há também o efeito sobre a leitura do catálogo: `0107`/`0108` são as regras de
professor **sem corte de ingresso**, isto é, as que cobrem toda a população. Com
a janela abrindo em 2003, elas se sobrepõem a praticamente todas as regras de
magistério do catálogo, e a sobreposição some se a janela for corrigida para
18/10/2021.

# Questão a investigar

1. **Se a janela foi trocada com `regra-0039`/`0040`.** As duas famílias são de
   magistério, e a hipótese é econômica: `0039`/`0040` gravam
   `[18/10/2021, 31/12/2099)` com fundamentação do regime **antigo**, e estas
   gravam `[31/12/2003, 31/12/2024)` com fundamentação do regime **novo** — cada
   par com a janela do outro. Nada no repositório registra a ordem de
   preenchimento, então continua hipótese.

2. **Se `31/12/2003` é o marco de outra coisa.** A data é a publicação da EC
   41/2003 e aparece em 30 regras como `data_direito_apos`. Pode ser herança de
   um lote preenchido por cópia, e não uma afirmação sobre estas duas.

3. **Se o regime novo deve ter prazo.** A LCE 1.100/2021 não fixa nenhum. Se a
   resposta for "não deve", `data_direito_ate` destas duas é a sentinela, e elas
   saem do grupo do `achado-0047` pela mesma razão que a `regra-0032` sai do
   `achado-0022`: o defeito não é a janela aberta, é a data fechada.
