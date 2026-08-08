---
type: Analise
id: atomicidade-cf88-original-ciclo-09
nome: Atomicidade e fórmulas da CF/88 original no Ciclo 9
data: 2026-08-08
---

# Atomicidade e fórmulas da CF/88 original — Ciclo 9

## Questão examinada

A proposta inicial de causa comum cobria toda a janela de 05/10/1988 a
15/12/1998. A auditoria verificou se essa unidade tinha uma única identidade de
cálculo ou se escondia mudanças materiais de base, razão, conversão ou sexo.

Foram consultadas e preservadas as publicações integrais originais da LCE
1/1984, da LCE 39/1990 e da LCE 68/1992. Os dispositivos usados abaixo foram
também cotejados visualmente e destilados em `okf/dispositivos/`. A compilação
atual da Constituição do Estado foi arquivada como fonte consultada, mas não foi
usada como prova autônoma de redação histórica nem para preencher lacunas.

## Matriz das fórmulas

| direito implementado       | base                                                                                            | razão          | conversão                                | sexo         | conclusão                  |
| -------------------------- | ----------------------------------------------------------------------------------------------- | -------------- | ---------------------------------------- | ------------ | -------------------------- |
| `[05/10/1988, 31/07/1990)` | remuneração da atividade, por interpretação sistemática dos arts. 94 e 154, § 2º, da LCE 1/1984 | `1/30` por ano | ano de 365 dias; resto `> 182` arredonda | ambos        | fórmula determinada        |
| `[31/07/1990, 09/12/1992)` | vencimento + adicional por tempo + outras vantagens pecuniárias, art. 156 da LCE 39/1990        | `1/35` por ano | ano de 365 dias; resto `> 180` arredonda | masculino    | fórmula determinada        |
| `[31/07/1990, 09/12/1992)` | mesma base do art. 156                                                                          | `1/30` por ano | mesma conversão                          | feminino     | fórmula determinada        |
| `[09/12/1992, 16/12/1998)` | vencimento + adicional por tempo + outras vantagens pecuniárias, art. 236 da LCE 68/1992        | ausente        | ano de 365 dias; resto `> 180` arredonda | não decidido | pendência jurídica externa |

`DATA_DIREITO_APOS` inclui o primeiro dia e `DATA_DIREITO_ATE` exclui o marco
final. Por isso as quatro linhas cobrem a janela inteira, sem lacuna nem
sobreposição.

## Decisões classificadas

### Jurídicas

- A LCE 1/1984 determina a razão de `1/30` para os demais casos e define a
  conversão. A adoção da remuneração da atividade como referência resulta da
  conjugação dos arts. 94 e 154, § 2º; não é apresentada como cláusula literal
  de base.
- A LCE 39/1990 determina razões diferentes para homem e mulher, além de base e
  conversão expressas.
- A LCE 68/1992 determina proporcionalidade, base e conversão, mas o parágrafo
  único do art. 235 está expressamente vetado. O texto não fornece o
  denominador.
- Não se importam `35/30` da aposentadoria voluntária do art. 232, III, “a”, da
  LCE 68/1992. Fazer isso seria preencher por interpretação uma lacuna
  produzida por veto e exige manifestação jurídica específica.

### De modelagem

- Identidades diferentes de fórmula exigem TiposCalculo diferentes. A causa
  comum foi decomposta em quatro propostas: LCE 1; LCE 39 masculino; LCE 39
  feminino; e LCE 68.
- A decomposição aumenta a população do ciclo de 22 para 25 unidades. Ela não
  cria direito novo: torna visíveis discriminantes jurídicos que a unidade
  anterior ocultava.
- As três causas qualificadas continuam sendo uma unidade cada porque a forma
  sem redução proporcional preserva identidade material; as variações
  temporais da fonte da base ficam articuladas na mesma forma de cálculo.

### Operacionais

- O enum legado `Valor Efetivo` não demonstra base, razão, arredondamento ou
  sexo. Seu cotejo permanece ressalva de implantação.
- A exclusão das causas qualificadas e a apuração do tempo exigem prova e fluxo
  administrativo; não alteram a conclusão jurídica das três fórmulas fechadas.
- A unidade da LCE 68 fica em `pendente_mapeamento_sisprev`, pois sem
  denominador não há fórmula completa que possa ser projetada para homologação.

## Questão externa localizada

A manifestação jurídica deve definir qual denominador rege a aposentadoria por
invalidez de causa comum cujo direito foi implementado entre 09/12/1992 e
15/12/1998, considerando que o art. 235, II, da LCE 68/1992 determina
proporcionalidade, mas seu parágrafo único foi vetado. A manifestação deve dizer
também se sexo integra a fórmula. Até esse ato, a auditoria dessa unidade
permanece em elaboração; nenhuma aprovação, decisão institucional ou ativação é
registrada aqui.
