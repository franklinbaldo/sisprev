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

A janela de direito delas grava `data_direito_apos: 31/12/2003` e
`data_direito_ate: 31/12/2024`.

Ela abre **dezoito anos antes** da lei estadual que a funda e **dezesseis antes**
da redação constitucional que ela cita. E fecha num prazo cuja norma
instituidora — o art. 4º da ECE 146/2021 — nenhum campo delas menciona.

A acusação é **condicional**, e a condição está dita na seção própria abaixo: ela
depende de `data_direito_apos` significar "quando o direito pode nascer", que é a
**Q2** e segue aberta no eixo do direito (issue #37).

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
§8. Um regime que substitui o anterior não se extingue em 2024.

Então a leitura mais provável é que **as duas datas estão erradas na mesma
direção**: `data_direito_apos` deveria marcar a vigência da LCE 1.100/2021
(18/10/2021) e `data_direito_ate` deveria ser a sentinela — que é exatamente o
par que `regra-0039`/`0040` gravam com a fundamentação errada. As duas famílias
parecem ter trocado janelas.

**Isso é hipótese, não conclusão.** O que está conferido é a incompatibilidade
entre as vigências dos vínculos e a data de abertura gravada; qual das pontas cede
é decisão de quem responde pelo campo.

## Este achado depende de uma questão aberta, e ela pode desfazê-lo

A acusação pressupõe que `data_direito_apos` marca **quando o direito pode
nascer**. Se marcar isso, uma regra fundada em lei de 2021 abrindo em 2003 é
defeito. Mas a semântica desse campo é a **Q2**, parcialmente aberta, e é o objeto
da issue #37: há duas convenções de fronteira incompatíveis nesse eixo, e o
próprio catálogo não declara qual usa.

Leituras alternativas que desfariam a acusação, nenhuma delas afastada aqui:

- se `data_direito_apos` fosse a data a partir da qual a **regra** é aplicável no
  sistema (marcador administrativo), a comparação com a vigência do dispositivo
  citado não seria pertinente;
- se fosse herança de migração — `31/12/2003` ocorre em 30 regras, o que é
  compatível com preenchimento por lote —, seria defeito de importação e não
  afirmação sobre estas duas.

Registrado como dependência explícita, e não como ressalva de estilo: **enquanto a
Q2 não fechar no eixo do direito, este achado é uma acusação condicional**. O que
não depende dela é o fato bruto: as cinco normas citadas entraram em vigor entre
2019 e 2021, e a data gravada é de 2003.

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

`data_direito_apos` é campo entregue, e **se** a leitura que a Q2 não confirmou
for a correta — o campo marcando quando o direito pode nascer — então a regra
funda em lei estadual de 2021 o direito de quem completou requisitos em 2004,
isto é, concessão sob norma que não vigia no fato gerador. Sob qualquer das
leituras alternativas o defeito muda de natureza, mas não desaparece: ou a janela
é letra morta que ninguém confere, ou é marcador administrativo cujo valor não
corresponde a marco algum das normas citadas.

Registro de notação, porque a versão anterior desta seção errava nele: a
convenção confirmada (Q1) é `DATA_*_ATE` **inclusivo** e `DATA_ADM_APOS`
**exclusivo** — logo o eixo de admissão é `(apos, ate]`, não `[apos, ate)`. No
eixo do direito, a simetria do `APOS` **não** está confirmada (issue #37), e é
por isso que este achado deixou de usar notação de intervalo e passou a nomear os
dois campos.

Há também o efeito sobre a leitura do catálogo. Os dois limites de admissão
dessas regras — `data_adm_apos: 01/01/1950` e `data_adm_ate: 31/12/2099` — são
**sentinelas**, então elas não declaram coorte de ingresso conferível alguma. Não
se pode concluir daí que "cobrem toda a população" (isso seria interpretar
sentinela, o que o P5 proíbe), mas com a janela de direito abrindo em 2003 elas
se sobrepõem no eixo temporal a quase toda regra de magistério do catálogo, e a
sobreposição diminui se a janela for corrigida para 18/10/2021.

# Questão a investigar

1. **Se a janela foi trocada com `regra-0039`/`0040`.** As duas famílias são de
   magistério, e a hipótese é econômica: `0039`/`0040` gravam
   `apos: 18/10/2021` / `ate: 31/12/2099` com fundamentação do regime
   **antigo**, e estas gravam `apos: 31/12/2003` / `ate: 31/12/2024` com
   fundamentação do regime **novo** — cada par com a janela do outro. Nada no repositório registra a ordem de
   preenchimento, então continua hipótese.

2. **Se `31/12/2003` é o marco de outra coisa.** A data é a publicação da EC
   41/2003 e aparece em 30 regras como `data_direito_apos`. Pode ser herança de
   um lote preenchido por cópia, e não uma afirmação sobre estas duas.

3. **Se o regime novo deve ter prazo.** A LCE 1.100/2021 não fixa nenhum. Se a
   resposta for "não deve", `data_direito_ate` destas duas é a sentinela, e elas
   saem do grupo do `achado-0047` pela mesma razão que a `regra-0032` sai do
   `achado-0022`: o defeito não é a janela aberta, é a data fechada.
