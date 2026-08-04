---
type: Conjunto
id: ciclo-01-s4-bloco-c
nome: Ciclo 1 — S4 — substituição das regras de incapacidade permanente
situacao: proposto
base: ciclo-01-s3-bloco-b
substituicoes:
  - grupo: incapacidade-lce1100-ingresso-ate-2003
    origens_legacy:
      - /regras/regra-0019.md
      - /regras/regra-0020.md
    destinos_propostos:
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-acidente-em-servico.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-molestia-profissional.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-tuberculose-ativa.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-hanseniase.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-alienacao-mental.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-neoplasia-maligna.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-cegueira-bilateral.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-paralisia-irreversivel.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-cardiopatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-doenca-de-parkinson.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-espondiloartrose-anquilosante.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-nefropatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-doenca-de-paget.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-sida-aids.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-contaminacao-por-radiacao.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-hepatopatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-esclerose-multipla.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-surdez-permanente-magisterio.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-anomalia-da-fala-magisterio.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-causa-comum.md
    estado_grupo: inativo
  - grupo: incapacidade-lce1100-ingresso-apos-2003
    origens_legacy:
      - /regras/regra-0021.md
      - /regras/regra-0022.md
    destinos_propostos:
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-acidente-em-servico.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-molestia-profissional.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-tuberculose-ativa.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-hanseniase.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-alienacao-mental.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-neoplasia-maligna.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-cegueira-bilateral.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-paralisia-irreversivel.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-cardiopatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-doenca-de-parkinson.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-espondiloartrose-anquilosante.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-nefropatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-doenca-de-paget.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-sida-aids.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-contaminacao-por-radiacao.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-hepatopatia-grave.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-esclerose-multipla.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-surdez-permanente-magisterio.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-anomalia-da-fala-magisterio.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-causa-comum.md
    estado_grupo: inativo
---

> **O corpo abaixo é o registro da sessão S4, não o estado atual.** Ele foi
> escrito quando o Bloco C tinha oito unidades, os grupos estavam `inativo` e as
> unidades em `elaboracao`. O frontmatter deste mesmo arquivo já traz o que a S6
> decidiu — quarenta destinos —, e é ele que vale. Onde as duas partes
> divergirem, vale o frontmatter, e o estado corrente do ciclo está em
> [`ciclo-01-s6-fechamento`](ciclo-01-s6-fechamento.md).

> **Os dois grupos voltaram a `estado_grupo: inativo` em 04/08/2026, em revisão
> de review à ativação de 03/08/2026.** RFC 0004 §1.4 exige que **todos** os
> destinos de um grupo estejam `deployable` para o grupo ativar; nenhum
> destino pode ativar isoladamente. Em cada grupo, a unidade de causa comum
> (`*-causa-comum.md`) recuou de `deployable` para `preview`, porque o rótulo
> `Proporcionalidade Dias` que ela projeta tem fidelidade parcial severa o
> bastante para admitir uma leitura que descarta a base média por completo —
> ver a issue #122 e RFC 0004 §5.3 (semântica operacional não confirmada é
> fail-closed para `deployable`). Consequentemente `decisao_completude` saiu
> do frontmatter: RFC 0004 §1.4 registra esse campo como ausente/nulo enquanto
> o grupo está `inativo`. A análise jurídica de completude que ele continha —
> reproduzida abaixo — não foi revista nem reaberta; o que mudou foi a
> confirmação operacional de uma das vinte unidades de cada grupo, e a regra
> de ativação é sempre por grupo inteiro, nunca por unidade isolada.
>
> **Análise de completude preservada (decidida por franklinbaldo em
> 2026-08-03, para os dois grupos):** o art. 30, caput, da LCE 1.100/2021
> enumera exaustivamente as causas que afastam a proporcionalização —
> acidente em serviço, moléstia profissional e doença grave, contagiosa ou
> incurável — e trata todas as demais como ramo residual. Os destinos de cada
> grupo cobrem as três causas nomeadas mais a causa comum, e a terceira delas
> é decomposta moléstia a moléstia pelo rol do § 8º: dezesseis incisos que
> produzem dezessete hipóteses, porque o inciso XVI reúne surdez permanente e
> anomalia da fala, ambas restritas ao magistério. São vinte destinos por
> grupo, e a conferência foi feita item a item contra o texto transcrito do
> art. 30, caput e §§ 5º, 8º, 13 e 14, da LCE 1.100/2021, com os dezesseis
> incisos do § 8º autorados como dispositivos próprios a partir da compilação
> da DITEL/Casa Civil — não contra o que já existia em disco. A cláusula
> "dentre outras que a lei indicar" não deixa hipótese descoberta: ela remete
> a lei, não a avaliação caso a caso, e nenhuma outra lei indicativa foi
> localizada — se vier a existir, faltará uma regra, e é esse o limite exato
> desta declaração.

# Decisão da S4

As quatro regras legadas recebem situação T4 `desativada_substituida`.

- `regra-0019` grava remuneração do cargo, mas o § 13 do art. 30 remete as
  causas qualificadas à média do art. 24; também agrupa três classes de causa.
- `regra-0020` representa uma combinação juridicamente possível — causa comum,
  proporcionalidade e paridade —, mas copia a fundamentação integral e não
  explicita que a proporcionalidade do art. 26 incide sobre a média do art. 24.
- `regra-0021` executa o ramo proporcional, porém traz fundamentações das causas
  qualificadas, cita a coorte anterior e não explicita a base média.
- `regra-0022` acerta média, integralidade e ausência de paridade no resultado,
  mas agrupa três causas e cita os arts. 25 e 27, I, próprios da outra coorte.

Nenhuma origem fica `sem substituta`: todas as hipóteses válidas são preservadas
nas oito unidades. Também não foi demonstrada lacuna preexistente no Bloco C.

# Matriz material

Para ingresso até 31/12/2003:

- acidente em serviço, moléstia profissional e doença catalogada conduzem à
  média do art. 24 sem proporcionalização, com paridade do art. 27, I;
- as demais causas conduzem à média proporcional em dias pelo art. 26, com
  paridade do art. 27, I.

Para ingresso a partir de 01/01/2004:

- acidente em serviço, moléstia profissional e doença catalogada conduzem à
  média do art. 24 sem proporcionalização, sem paridade;
- as demais causas conduzem à média proporcional em dias pelo art. 26, sem
  paridade.

Os §§ 13 e 14 do art. 30 são regras especiais do cálculo da incapacidade. A
ressalva ao direito adquirido a outra fórmula preserva hipóteses formadas sob
regime anterior; ela não converte, por si só, o ingresso até 2003 em exceção à
remissão expressa aos arts. 24 e 26.

A janela de direito começa em `18/10/2021`, data de publicação e vigência da LCE
1.100/2021. `DATA_DIREITO_APOS` é inclusivo. A divisão de ingresso é contínua:
`DATA_ADM_ATE = 31/12/2003` e `DATA_ADM_APOS = 01/01/2004`, ambos inclusivos.

# Estado dos grupos à época da S4

À época desta sessão os grupos estavam `inativo` e as unidades em `elaboracao`,
e a lista abaixo era o que a S4 exigia antes de ativar. O frontmatter registra o
que a S6 decidiu depois; os itens 3 e 4 desta lista continuam abertos no corpo
das unidades, e é disso que trata a conferência de conformidade do ciclo.

Antes de ativação, era obrigatório:

1. criar ou confirmar a FormaCalculo de média proporcional em dias;
2. confirmar a projeção das combinações de cálculo e reajuste no Sisprev;
3. resolver Q6-S/Q6-T quanto à classificação operacional da causa;
4. completar o gate humano das unidades;
5. harmonizar na S5 a ressalva de direito adquirido com os blocos históricos; e
6. registrar decisão de completude e ato institucional.

Este conjunto deriva de `ciclo-01-s3-bloco-b`. A proposta é cumulativa e mantém
as substituições dos Blocos A e B. Nada muda no catálogo vigente enquanto os
grupos estiverem inativos.
