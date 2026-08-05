---
type: TipoCalculo
id: tipo-calculo-remuneracao-cargo-proporcional-cf88-original
nome: Vencimento do cargo e vantagens, proporcional ao tempo — CF/88 original
base:
  tipo: vencimento_cargo_acrescido_vantagens_pecuniarias
  dispositivos:
    - /dispositivos/lce-39-1990/art-156/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-inc-i/original.md
      - /dispositivos/lce-1-1984/art-154-par-3/original.md
      - /dispositivos/lce-39-1990/art-155-par-unico/original.md
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: pendente
  justificativa: >-
    `Valor Efetivo` não representa o ajuste proporcional. A composição
    estatutária da base está identificada de 31/07/1990 em diante, e a medida
    da fração está transcrita nos dois primeiros segmentos; no terceiro, a
    ausência de fração expressa decorre do veto ao parágrafo único do art. 235
    da LC 68/1992. O enum não carrega o segmento nem o denominador. Faltam a
    base do trecho anterior a 31/07/1990, o denominador aplicável sob a LC
    68/1992 e a convenção operacional de conversão do tempo.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 40, inciso I, da Constituição Federal em seu texto original define
o ramo proporcional residual, mas não define a composição da base.

Nos períodos disciplinados pela LCE 39/1990 e pela LCE 68/1992, a base é o
vencimento do cargo acrescido da gratificação adicional temporalmente aplicável
e de outras vantagens pecuniárias, conforme os arts. 156 e 236,
respectivamente. Sobre essa base incide a fração proporcional ao tempo. Falta a
base do trecho anterior a 31/07/1990, sob a LC 1/1984, e ela não foi presumida
por analogia com as duas posteriores.

Os dois artigos não são idênticos: o art. 156 lê "gratificação adicional por
tempo" e o art. 236 lê "por tempo de serviço". A diferença foi verificada na
imagem da página e não é artefato de reconhecimento.

## A medida da fração

O quadro normativo dos três segmentos está identificado e **muda em cada um**:

| direito implementado    | dispositivo                    | fração                                                   |
| ----------------------- | ------------------------------ | -------------------------------------------------------- |
| 05/10/1988 a 30/07/1990 | LC 1/1984, art. 154, § 3º      | 1/30 por ano de serviço, sem distinção de sexo           |
| 31/07/1990 a 08/12/1992 | LC 39/1990, art. 155, p. único | 1/35 homem, 1/30 mulher; 1/30 professor, 1/25 professora |
| 09/12/1992 a 30/01/2000 | LC 68/1992                     | sem fração expressa                                      |

Dois servidores homens com o mesmo tempo recebem frações diferentes conforme o
direito se implemente antes ou depois de 31/07/1990 — a LC 1/1984 não distingue
sexo, a LC 39/1990 passa a distinguir.

No terceiro segmento a constatação é negativa e verificável em fonte com camada
de texto: o parágrafo único do art. 235 da LC 68/1992 — que nas leis anterior e
posterior é justamente onde a fração mora — consta do texto compilado como
**VETADO**. A LC 68/1992 é decalque quase verbatim da LC 39/1990 e perdeu a
fração por veto, não por omissão de redação. O denominador desse segmento sai
por construção do art. 232, III, a (35 anos homem, 30 mulher), e essa construção
é leitura da auditoria, não texto — por isso não é adotada como parâmetro.

**A medida é em anos, não em dias.** Os três diplomas apuram o tempo em dias e o
convertem em anos (ano de 365 dias), com regra de arredondamento endereçada
nominalmente ao cálculo proporcional. A medida da fração em dias aparece por
dispositivo expresso apenas em 2008, no art. 17, § 2º da LCE 432/2008 — ter sido
preciso escrevê-lo é indício de que antes não era assim. É a convenção
operacional que permanece pendente aqui.

A paridade não integra esta fórmula; decorre do art. 40, § 4º, do texto
constitucional original e opera como regime de revisão posterior.

# Fórmula

```text
base_estatutaria = vencimento_cargo
       + gratificacao_adicional_temporalmente_aplicavel
       + outras_vantagens_pecuniarias

provento_inicial = base_estatutaria × fracao_proporcional_tempo
```

# Entradas e saídas

Entradas já identificadas: vencimento do cargo, gratificação adicional conforme
a redação do estatuto aplicável, outras vantagens pecuniárias e tempo apurado
no caso.

Saída: provento inicial proporcional. No primeiro segmento, o valor depende
ainda da identificação da base; no terceiro, do denominador aplicável; em todos,
da convenção operacional de conversão do tempo.

# Implementação

A projeção atual combina `tipo_calculo: Valor Efetivo` com `integral: N`.
Essa combinação distingue o ramo no legado, mas não representa a fórmula
completa.

# Onde esta forma é usada

No Ciclo 1, na unidade `invalidez-cf88-original-causa-comum`.
