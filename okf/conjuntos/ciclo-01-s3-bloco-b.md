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
    destinos_auditados:
      - /regras-auditadas/unidades/invalidez-ec41-geral-acidente-em-servico.md
      - /regras-auditadas/unidades/invalidez-ec41-geral-molestia-profissional.md
      - /regras-auditadas/unidades/invalidez-ec41-geral-doenca-catalogada.md
      - /regras-auditadas/unidades/invalidez-ec41-geral-causa-comum.md
    estado_grupo: inativo
  - grupo: invalidez-ec70-art-6a
    origens_legacy:
      - /regras/regra-0008.md
      - /regras/regra-0009.md
    destinos_auditados:
      - /regras-auditadas/unidades/invalidez-ec70-art-6a-acidente-em-servico.md
      - /regras-auditadas/unidades/invalidez-ec70-art-6a-molestia-profissional.md
      - /regras-auditadas/unidades/invalidez-ec70-art-6a-doenca-catalogada.md
      - /regras-auditadas/unidades/invalidez-ec70-art-6a-causa-comum.md
    estado_grupo: inativo
---

# Decisão da S3

As quatro regras legadas recebem situação T4 `desativada_substituida`.

- `regra-0006` e `regra-0007` misturam os dois ramos, não registram a causa que
  escolhe o resultado e mantêm a janela aberta além do prazo do art. 4º da ECE
  146/2021.
- `regra-0008` e `regra-0009` têm os mesmos problemas e carregam fundamento no
  inciso III do § 1º do art. 40, embora o art. 6º-A exija expressamente o
  inciso I.

Nenhuma origem fica `sem substituta`. Os grupos são independentes porque regra
geral e art. 6º-A diferem em ingresso, base de cálculo, paridade e fundamento.

# Matriz material

| regime | acidente em serviço | moléstia profissional | doença catalogada | demais causas |
| --- | --- | --- | --- | --- |
| EC 41, regra geral preservada | média sem proporcionalização, sem paridade | média sem proporcionalização, sem paridade | média sem proporcionalização, sem paridade | média proporcional ao tempo, sem paridade |
| EC 70, art. 6º-A preservado | remuneração do cargo sem proporcionalização, paridade | remuneração do cargo sem proporcionalização, paridade | remuneração do cargo sem proporcionalização, paridade | remuneração do cargo proporcional ao tempo, paridade |

A janela é `[31/12/2003, 01/01/2025)`. O fecho é `01/01/2025`, e não
`31/12/2024`, porque `DATA_DIREITO_ATE` é exclusivo. Assim o último dia
admitido pela norma permanece coberto.

A LC 228/2000 e a LCE 432/2008 são versões estaduais dentro da janela. Elas
entram como proveniência, taxonomia e fórmula temporalmente aplicável; não
multiplicam regras sem alteração material demonstrada de resultado.

# Estado dos grupos

Os grupos permanecem `inativo` e as unidades em `elaboracao`. Antes de
ativação, é obrigatório:

1. transcrever e versionar os dispositivos estaduais anteriores à LCE 432/2008;
2. fechar as formas de cálculo dos subperíodos;
3. confirmar a projeção dos cálculos no enum legado;
4. resolver Q6-S/Q6-T quanto à classificação operacional da causa;
5. completar o gate humano; e
6. registrar decisão de completude e ato institucional.

Este conjunto deriva de `ciclo-01-s2-bloco-a`: a proposta é cumulativa e não
esquece as substituições do Bloco A. Nada muda no catálogo vigente enquanto os
grupos estiverem inativos.
