---
type: Achado
id: achado-0016
nome: Quatro regras de professor partilham uma fundamentação que afirma integralidade e paridade; em duas delas ela contradiz os próprios campos
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0041.md
  - /regras/regra-0042.md
  - /regras/regra-0107.md
  - /regras/regra-0108.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

**Quatro** regras de aposentadoria especial de professor — `regra-0041`,
`regra-0042`, `regra-0107` e `regra-0108` — têm `fundamentacao_integral`
**idêntica caractere a caractere entre as quatro**. O texto afirma:

> Aposentadoria especial de professor, com **proventos integrais (cálculo por
> integralidade) e com paridade**, com base no artigo 40, § 5°, da
> Constituição Federal, com redação dada pela Emenda Constitucional nº
> 103/2019, artigos 25, 27, I; 33, da Lei Complementar nº 1.100/2021 [...]

As quatro são dois pares idênticos em forma, separados por `sexo`. Em cada
par, a primeira corresponde ao texto e a segunda **não**:

| campo          | `0041` / `0042`             | `0107` / `0108`      |
| -------------- | --------------------------- | -------------------- |
| `sexo`         | MASCULINO / FEMININO        | MASCULINO / FEMININO |
| `integral`     | `S`                         | **`N`**              |
| `paridade`     | `S`                         | **`N`**              |
| `tipo_calculo` | Remuneração de Contribuição | **Valor Médio**      |

A primeira versão deste achado alcançava só `0041`/`0107` e **perdia metade
da população afetada** — `regra-0108` tem exatamente o mesmo defeito da
`0107`. A simetria por sexo é perfeita e não muda nada do raciocínio: o
defeito não tem relação com `sexo`, e por isso mesmo era fácil não vê-lo.

# Evidências

**As duas regras não são duplicatas, e isso é o que torna o achado preciso.**
As janelas as separam de forma juridicamente coerente:

| campo               | `0041` / `0042` | `0107` / `0108` |
| ------------------- | --------------- | --------------- |
| `data_adm_ate`      | 31/12/2003      | 31/12/2099      |
| `data_direito_apos` | 18/10/2021      | 31/12/2003      |
| `data_direito_ate`  | 31/12/2099      | 31/12/2024      |

`regra-0041`/`0042` alcançam quem **ingressou até 2003** — servidor do regime
anterior, para quem integralidade e paridade são o tratamento esperado.
`regra-0107`/`0108` não limitam a admissão, e gravam média sem paridade, que é o
tratamento do regime novo. **Resultados diferentes para populações diferentes
é o comportamento certo**, não a contradição.

A contradição é interna à `regra-0107` e à `regra-0108`: o texto que ela entrega afirma
"proventos integrais (cálculo por integralidade) e com paridade" enquanto os
seus próprios campos gravam `integral: N`, `paridade: N` e cálculo por valor
médio. Dois campos **deployáveis** da mesma regra dizem coisas opostas.

O `nome` das duas confirma a leitura, e é onde a distinção aparece — só que
ela não chegou à fundamentação.

**Isto corrige a formulação de §3.1 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md).**
Lá o item é "string idêntica, três campos opostos", o que convida a ler as
duas como um par contraditório ou duplicado. Conferidas as janelas, não são:
o par é legítimo, e o defeito está em **uma** delas.

# Consequência prática

`FUNDAMENTACAO_INTEGRAL` é o texto que o Sisprev entrega no documento do
servidor. Um requerimento decidido pela `regra-0107` ou pela `regra-0108` recebe proventos por
valor médio e sem paridade, acompanhados de uma fundamentação que afirma
integralidade e paridade — e afirma isso com citação de dispositivos, o que
lhe dá aparência de fundamento jurídico do que está sendo concedido.

Quem lê o documento e quem confere o cálculo veem coisas incompatíveis. A
discrepância favorece a expectativa do servidor contra o que o sistema de
fato concedeu, o que a torna material para eventual questionamento.

Nada aqui afirma que o **motor** aplique o texto: em regra `simulavel: S` ele
não lê a fundamentação, e a integralidade é decidida pelos campos. O problema
é de documento entregue, não de cálculo.

# Questão a investigar

1. **Se a fundamentação foi copiada.** Um mesmo texto em quatro regras cujos demais campos as separam em dois eixos (sexo e janela de admissão) é o que se espera de cópia, não de redação independente. É a explicação
   Hipótese, não causa verificada — nada no catálogo registra a ordem em que
   as linhas foram escritas.

2. **Qual das duas pontas corrigir na `0107` e na `0108`.** Se os campos estão certos, o
   texto tem de ser reescrito para descrever média sem paridade. Se o texto
   está certo, são `integral`, `paridade` e `tipo_calculo` que estão errados —
   e aí a regra concede menos do que deveria. As duas hipóteses têm
   consequência oposta para o servidor, e nenhuma se decide pelo catálogo:
   ambos os campos são deployáveis, e escolher entre eles é ato de quem
   responde pelo produto.

3. **Se `data_direito_ate: 31/12/2024` das duas é o mesmo padrão sistêmico.**
   A data reaparece em cinco dos seis grupos da conferência e coincide com o
   prazo do art. 4º da ECE 146/2021, registrado em §5.1 daquela lista como
   padrão fortemente sugestivo e **não** como conclusão. Este achado não o
   fecha nem depende dele.
