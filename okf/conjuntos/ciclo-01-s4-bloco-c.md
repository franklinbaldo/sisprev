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
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-doenca-catalogada.md
      - /regras-propostas/regras/incapacidade-lce1100-ate-2003-causa-comum.md
    estado_grupo: inativo
  - grupo: incapacidade-lce1100-ingresso-apos-2003
    origens_legacy:
      - /regras/regra-0021.md
      - /regras/regra-0022.md
    destinos_propostos:
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-acidente-em-servico.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-molestia-profissional.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-doenca-catalogada.md
      - /regras-propostas/regras/incapacidade-lce1100-apos-2003-causa-comum.md
    estado_grupo: inativo
---

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

# Estado dos grupos

Os grupos permanecem `inativo` e as unidades em `elaboracao`. Antes de ativação,
é obrigatório:

1. criar ou confirmar a FormaCalculo de média proporcional em dias;
2. confirmar a projeção das combinações de cálculo e reajuste no Sisprev;
3. resolver Q6-S/Q6-T quanto à classificação operacional da causa;
4. completar o gate humano das unidades;
5. harmonizar na S5 a ressalva de direito adquirido com os blocos históricos; e
6. registrar decisão de completude e ato institucional.

Este conjunto deriva de `ciclo-01-s3-bloco-b`. A proposta é cumulativa e mantém
as substituições dos Blocos A e B. Nada muda no catálogo vigente enquanto os
grupos estiverem inativos.
