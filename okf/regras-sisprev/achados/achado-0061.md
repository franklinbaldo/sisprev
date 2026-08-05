---
type: Achado
id: achado-0061
nome: Mesmo valor de tipo_calculo abrange benefícios e fórmulas juridicamente distintos sem mecanismo de desambiguação confirmado
situacao: aberto
severidade: bloqueante
verificacao: hibrida
natureza: dados
regras_afetadas:
  - /regras/regra-0020.md
  - /regras/regra-0021.md
  - /regras/regra-0007.md
  - /regras/regra-0027.md
  - /regras/regra-0028.md
  - /regras/regra-0029.md
  - /regras/regra-0030.md
  - /regras/regra-0031.md
detectado_em: 2026-08-04
detectado_por: franklinbaldo
---

# Constatação

Oito regras do catálogo legado gravam `tipo_calculo: Proporcionalidade Dias`
e pertencem a quatro `tipo_de_beneficio` diferentes:

| regra                                    | tipo_de_beneficio       | fundamentação               |
| ---------------------------------------- | ----------------------- | --------------------------- |
| `regra-0020`, `regra-0021`               | Incapacidade permanente | causa comum, LCE 1.100/2021 |
| `regra-0007`                             | Invalidez               | LC 228/2000 + LCE 432/2008  |
| `regra-0027`, `regra-0030`, `regra-0031` | Compulsória             | —                           |
| `regra-0028`, `regra-0029`               | Por idade               | —                           |

Dentro do próprio universo de causa comum por incapacidade/invalidez, a
auditoria já identificou, para regras propostas deste ciclo e do Bloco B,
três `FormaCalculo` juridicamente distintas projetando o mesmo rótulo:

- `forma-calculo-media-proporcional-dias-lce1100` — média do art. 24 da LCE
  1.100/2021, proporcionalizada pelo art. 26;
- `forma-calculo-media-proporcional-dias-lce432` — média do art. 45 da LCE
  432/2008 (80% maiores remunerações, limitada pelos §§ 9º e 10), proporcionalizada
  pelo art. 17;
- `forma-calculo-remuneracao-cargo-ec70-proporcional-dias` — remuneração do
  cargo efetivo (não é uma média), proporcionalizada pelo art. 17 da LCE
  432/2008 via o art. 6º-A da EC 41/2003.

# Presunção de trabalho

Na ausência de evidência em contrário, presume-se que valores iguais de
`tipo_calculo` levam o Sisprev a executar a mesma rotina de cálculo. É a
leitura natural de um campo de código: sem outro dado conhecido que
diferencie o tratamento, o rótulo é o que resta para inferir o
comportamento do sistema.

# Contraponto registrado

A amplitude da colisão constatada acima — quatro tipos de benefício
juridicamente muito distintos entre si, não só três fórmulas de causa comum
— torna também plausível que o Sisprev **não** dependa de `tipo_calculo`
isoladamente para selecionar a rotina, e sim de alguma combinação com outras
colunas já existentes no schema legado (`tipo_de_beneficio`, ao menos).
Um sistema em produção que computasse literalmente a mesma fórmula para
aposentadoria compulsória, por idade e por incapacidade seria uma hipótese
mais grave e menos parcimoniosa do que uma rotina de proporcionalização
compartilhada, com a base determinada por outro campo.

# Estado probatório

Nenhum dos dois mecanismos — execução única sob o mesmo rótulo, ou
desambiguação por outro campo — está confirmado. `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`
não registra resposta do IPERON/fornecedor sobre este ponto. Este achado
**não afirma** que o Sisprev calcula hoje, em produção, algum destes
benefícios incorretamente — afirma a colisão documental no cadastro e a
ausência de mecanismo de desambiguação demonstrado.

# Fórmula exigida no Ciclo 1

Para `regra-0020` e `regra-0021` — causa comum da incapacidade permanente
sob a LCE 1.100/2021, coortes até e a partir de 31/12/2003 — a fórmula
juridicamente exigida é a média do art. 24 proporcionalizada pelo art. 26,
documentada em `forma-calculo-media-proporcional-dias-lce1100`.

# Correção funcional proposta

Deve existir, no Sisprev, um tipo de cálculo ou uma combinação de
parâmetros que implemente univocamente essa fórmula, distinguindo-a das
fórmulas da LCE 432/2008 e do art. 6º-A/EC 70/2012 que hoje compartilham o
mesmo rótulo. Uma proposta possível de rótulo discriminante: `Média proporcional em dias — LCE 1.100`.

A solução técnica é aberta e cabe ao IPERON/fornecedor, não à auditoria:
cadastrar um novo valor na coluna, criar rotina própria, parametrizar a
rotina existente, ou demonstrar que a desambiguação já ocorre por outro
campo — qualquer uma delas resolve a pendência.

# Efeito

`incapacidade-lce1100-ate-2003-causa-comum` e
`incapacidade-lce1100-apos-2003-causa-comum` permanecem `estado_proposta: preview`; os grupos de substituição correspondentes do Ciclo 1 permanecem
`estado_grupo: inativo` (RFC 0004 §1.4, §5.3), enquanto a correção funcional
proposta acima não for implantada ou a desambiguação por outro campo não for
demonstrada.

# Delimitação de alcance

Este achado registra uma colisão transversal observada no catálogo
original. No Ciclo 1, sua disposição alcança apenas as regras legadas
`regra-0020` e `regra-0021` e as respectivas propostas de substituição. A
inclusão de `regra-0007`, `regra-0027`, `regra-0028`, `regra-0029`,
`regra-0030` e `regra-0031` em `regras_afetadas` documenta a extensão
factual do uso do valor `Proporcionalidade Dias`, sem antecipar sua revisão
jurídica, alterar seus estados ou invadir a propriedade dos ciclos
correspondentes a essas regras.
