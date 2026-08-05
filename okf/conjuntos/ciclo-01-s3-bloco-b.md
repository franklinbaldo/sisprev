---
type: Conjunto
id: ciclo-01-s3-bloco-b
nome: Ciclo 1 — S3 — substituição das regras de invalidez EC 41 e EC 70
situacao: proposto
base: ciclo-01-s2-bloco-a
substituicoes:
  - grupo: invalidez-ec41-regra-geral
    origens_legacy:
      - /regras/regra-0006.md
      - /regras/regra-0007.md
    destinos_propostos:
      - /regras-propostas/regras/invalidez-ec41-geral-pre-mp167-acidente-em-servico.md
      - /regras-propostas/regras/invalidez-ec41-geral-pre-mp167-molestia-profissional.md
      - /regras-propostas/regras/invalidez-ec41-geral-pre-mp167-doenca-catalogada.md
      - /regras-propostas/regras/invalidez-ec41-geral-pre-mp167-causa-comum.md
      - /regras-propostas/regras/invalidez-ec41-geral-acidente-em-servico.md
      - /regras-propostas/regras/invalidez-ec41-geral-molestia-profissional.md
      - /regras-propostas/regras/invalidez-ec41-geral-doenca-catalogada.md
      - /regras-propostas/regras/invalidez-ec41-geral-media-lc228-causa-comum.md
      - /regras-propostas/regras/invalidez-ec41-geral-causa-comum.md
    estado_grupo: inativo
  - grupo: invalidez-ec70-art-6a
    origens_legacy:
      - /regras/regra-0008.md
      - /regras/regra-0009.md
    destinos_propostos:
      - /regras-propostas/regras/invalidez-ec70-art-6a-acidente-em-servico.md
      - /regras-propostas/regras/invalidez-ec70-art-6a-molestia-profissional.md
      - /regras-propostas/regras/invalidez-ec70-art-6a-doenca-catalogada.md
      - /regras-propostas/regras/invalidez-ec70-art-6a-lc228-causa-comum.md
      - /regras-propostas/regras/invalidez-ec70-art-6a-causa-comum.md
    estado_grupo: inativo
---

# Decisão da S3

As quatro regras legadas recebem situação T4 `desativada_substituida`.

- `regra-0006` e `regra-0007` misturam ramos e não registram a causa que escolhe
  o resultado.
- `regra-0008` e `regra-0009` têm os mesmos problemas e carregam fundamento no
  inciso III do § 1º do art. 40, embora o art. 6º-A exija o inciso I.

Nenhuma origem fica `sem substituta`. A reabertura de cálculo refinou os oito
destinos iniciais para quatorze unidades porque base e ajuste mudam
materialmente dentro da janela.

# Matriz material refinada

Na regra geral da EC 41:

- de 31/12/2003 a 19/02/2004, as causas qualificadas usam remuneração integral
  do cargo e a causa comum usa remuneração proporcional pela LC 228;
- de 20/02/2004 a 12/03/2008, as qualificadas usam a média federal de 80% e a
  causa comum combina essa média com a fração anual da LC 228;
- desde 13/03/2008, as qualificadas usam a média do art. 45 da LCE 432 e a causa
  comum usa essa média, com os limites dos §§ 9º e 10, proporcionalizada em dias
  pelo art. 17.

No art. 6º-A da EC 70:

- as causas qualificadas usam remuneração do cargo sem proporcionalização e com
  paridade em toda a janela retroativa;
- a causa comum usa a remuneração do cargo com a fração anual da LC 228 até
  12/03/2008 e com a fração em dias da LCE 432 desde 13/03/2008.

A janela global é `[31/12/2003, 01/01/2025)`. Os limites internos são
contínuos e exclusivos no topo: `20/02/2004` e `13/03/2008` pertencem aos
segmentos que começam nessas datas.

A mudança da LC 228 para a LCE 432 não é mera troca de citação no ramo
proporcional: a primeira calcula 1/35 ou 1/30 por ano e impõe piso de um salário
mínimo; a segunda aplica razão em dias sobre a média previamente limitada.

# Formas autoradas

- `tipo-calculo-remuneracao-cargo-integral-lc228`;
- `tipo-calculo-remuneracao-cargo-proporcional-lc228`;
- `tipo-calculo-media-80-invalidez-ec41`;
- `tipo-calculo-media-proporcional-lc228-lei10887`;
- `tipo-calculo-media-proporcional-dias-lce432`; e
- `tipo-calculo-remuneracao-cargo-ec70-proporcional-anos`; e
- `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias`.

As duas últimas eram uma só, `tipo-calculo-remuneracao-cargo-proporcional-ec70`,
que abrigava os dois segmentos de medida do art. 6º-A num componente único. Foram
partidas em 03/08/2026: a medida do ajuste é o que as distingue — fração anual da
LC 228 até 12/03/2008, razão em dias do art. 17 da LCE 432 desde 13/03/2008 —, e uma
forma que abrigasse as duas não teria projeção única no enum do Sisprev.

# Estado dos grupos

Os grupos permanecem `inativo` e as unidades em `elaboracao`. A cobertura
jurídica de cálculo está fechada; ainda impedem ativação:

1. confirmar a projeção das fórmulas compostas no produto;
2. resolver Q6-S/Q6-T quanto à classificação operacional da causa;
3. demonstrar o tratamento administrativo de frações de ano no segmento da LC
   228;
4. completar o gate humano; e
5. registrar decisão de completude e ato institucional.

Este conjunto deriva de `ciclo-01-s2-bloco-a`. Nada muda no catálogo vigente
enquanto os grupos estiverem inativos.
