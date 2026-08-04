---
titulo: Relatório jurídico de fechamento do Ciclo 1
subtitulo: >-
  Proposta da Procuradoria-Geral do Estado para revisão das regras de invalidez
  e incapacidade permanente do Sisprev
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
# Processo em que esta remessa é juntada. Fica vazio até que ele exista: a
# capa omite a linha, em vez de estampar um número inventado.
processo_sei: ''
---

# Objeto, alcance e conclusão do Ciclo 1

## Contexto e finalidade da auditoria

Este relatório apresenta o resultado do primeiro ciclo de auditoria jurídica
realizado pela Procuradoria-Geral do Estado sobre as regras de aposentadoria por
invalidez e incapacidade permanente cadastradas no Sisprev.

A auditoria teve por finalidade verificar se as regras registradas representam,
de forma juridicamente correta e operacionalmente aplicável, os regimes
constitucionais e legais incidentes, especialmente quanto à causa da
incapacidade, à forma de cálculo dos proventos, à proporcionalidade e ao regime
de reajuste.

O recorte deste ciclo é a **norma em vigor para requerimento novo**. As janelas
anteriores continuam produzindo efeito para direito adquirido, mas não recebem
pedido novo, e por isso a revisão delas foi deslocada para o ciclo seguinte,
com o trabalho já iniciado.

## Conclusão executiva

No escopo examinado, foram identificadas **{{origens}} regras cadastradas que
não devem ser mantidas em sua configuração atual**. Elas agrupam hipóteses
juridicamente distintas sob um mesmo registro, deixam de explicitar elementos
relevantes para a seleção do benefício e, em um caso, aplicam cálculo
proporcional sem que nenhum texto no cadastro diga de onde ele decorre.

A Procuradoria-Geral do Estado propõe, em consequência, a substituição dessas
{{origens}} regras por **{{destinos}} regras individualizadas**. A ampliação do
número de regras **não cria benefício novo**: ela separa hipóteses que têm
requisitos, causas, cálculos ou efeitos jurídicos distintos e que hoje
compartilham o mesmo registro.

A composição proposta preserva as {{naoAfetadas}} regras do catálogo não
afetadas por este ciclo e acrescenta as {{destinos}} substitutivas, formando um
conjunto de {{composicao}} regras. Nenhuma das {{origens}} regras auditadas
permanece na composição proposta.

## O que a Procuradoria afirma juridicamente

A análise recai sobre o texto normativo transcrito em cada capítulo, e conclui
que a composição proposta cobre integralmente o tema no escopo do ciclo:

- **as causas que afastam a proporcionalização** estão cobertas uma a uma,
  conforme a lei as enumera, e a causa residual tem regra própria;
- **as doenças graves, contagiosas ou incuráveis** deixam de ser uma categoria
  única e passam a ter uma regra por moléstia, com o nome da doença expresso na
  regra e na sua fundamentação, e com a restrição de cargo consignada onde a lei
  a impõe;
- **as coortes de ingresso** que a lei distingue para efeito de reajuste têm
  regras separadas, porque a paridade não decorre do cálculo mas do regime de
  revisão posterior;
- **a base de cálculo e o ajuste proporcional** são tratados como dimensões
  distintas: a integralidade do ramo significa ausência de redução pelo tempo,
  e não implica, por si, cálculo sobre determinada base;
- **cada requisito aferido** tem fundamento identificado em dispositivo
  transcrito, e a fundamentação de cada regra articula como eles se combinam,
  em vez de enumerá-los.

Onde a análise deixou questão em aberto, ela está consignada como ressalva no
capítulo correspondente. Enquanto não resolvida, a conclusão sobre aquela regra
não vai além do que ali se afirma.

## O que depende do Instituto

A conclusão jurídica do ciclo está consolidada neste relatório. A implantação
efetiva no Sisprev depende de providências que não são de natureza jurídica e
que a Procuradoria não tem como praticar nem presumir praticadas:

1. **captura e classificação da causa da incapacidade** — a causa é o critério
   que decide o resultado do benefício, e é preciso confirmar que o sistema a
   registra e a persiste de modo utilizável;
2. **aderência dos campos do Sisprev** — confirmar que o rótulo de tipo de
   cálculo gravado em cada regra é aquele pelo qual o sistema implanta a fórmula
   descrita no capítulo correspondente;
3. **implementação das fórmulas de cálculo** — as fórmulas estão descritas
   juridicamente; a sua parametrização no produto é ato técnico;
4. **homologação da projeção** — conferir, na planilha anexa, que cada regra
   proposta ocupa as colunas do sistema do modo previsto; e
5. **ato de implantação** — a substituição efetiva do catálogo em vigor.

Os pontos 1 e 2 são também as duas questões que atravessam todos os capítulos e
que a auditoria não alcança por construção: elas dependem do comportamento do
programa, e não do texto da norma.

## Como este documento está organizado

Cada capítulo apresenta um **grupo de substituição** completo: as regras
cadastradas que saem e as regras propostas que entram, lado a lado, com a
fundamentação de cada uma e o texto integral dos dispositivos citados. A
conclusão da Procuradoria é consignada por grupo.

O documento é gerado a partir do repositório da auditoria, no commit indicado na
capa, e não é editado à mão: uma correção é feita no repositório e produz um
novo relatório, com novo commit de origem.

## Nota metodológica

**Regra proposta.** É a regra corrigida — uma regra inteira, com nome,
parâmetros e fundamentação próprios, pronta para ocupar uma linha do Sisprev.
Ela vive num espaço de identidade próprio porque o catálogo recebido é
preservado como veio, sem perder, renumerar ou fundir linha alguma, enquanto
corrigir frequentemente **muda o número de regras**.

**Grupo de substituição.** É a unidade de decisão: reúne as regras que saem e as
que entram, e ativa ou reverte inteiro. Aprovar metade de um grupo deixaria
hipótese sem representação ou representada duas vezes.

**Limite do que a auditoria altera.** A revisão trabalha dentro dos campos que o
Sisprev já tem. Estender o domínio de um campo ou criar coluna seria alterar o
sistema, o que está fora do escopo. Onde a projeção nas colunas existentes perde
algo que a regra proposta registra, a perda está declarada.

**A planilha anexa** traz cada regra proposta projetada nas colunas do Sisprev,
do jeito que entraria, com colunas adicionais de proveniência que identificam de
que regra cadastrada a linha descende e a que grupo pertence.
