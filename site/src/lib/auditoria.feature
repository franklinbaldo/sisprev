Feature: Auditoria de seleção legada

  Scenario: faixa 66/15 no art. 8º
    Given o catálogo legado
    And um requerimento com os seguintes fatos:
      | tipoDeBeneficio | voluntaria |
      | sexo | null |
      | aposEspecial | true |
      | dataAdmissao | 2020-01-10 |
      | dataDireito | 2022-06-01 |
      | faixa_exposicao | 66-pontos-15-anos |
    When o filtro legado for executado
    Then os seguintes campos devem ser observados:
      | expectativa.elegivel | true |
      | expectativa.faixa_exposicao | 66-pontos-15-anos |
      | legado.quantidade_esperada | 1 |
      | legado.quantidade_observada | 3 |
      | legado.divergente | true |
      | legado.inclui | regra-0068,regra-0069,regra-0070 |
      | legado.exclui | regra-0001 |

  Scenario: controle negativo sem pontos suficientes
    Given o catálogo legado
    And um requerimento com os seguintes fatos:
      | tipoDeBeneficio | voluntaria |
      | sexo | null |
      | aposEspecial | true |
      | dataAdmissao | 2020-01-10 |
      | dataDireito | 2022-06-01 |
      | pontos | 65 |
      | anos_exposicao | 15 |
      | faixa_exposicao | nenhuma |
    When o filtro legado for executado
    Then os seguintes campos devem ser observados:
      | expectativa.elegivel | false |
      | expectativa.faixa_exposicao | nenhuma |
      | legado.quantidade_esperada | 0 |
      | legado.quantidade_observada | 3 |
      | legado.divergente | true |
      | legado.inclui | regra-0068,regra-0069,regra-0070 |
      | legado.exclui | regra-0001 |

  Scenario: família de pensão usa os mesmos steps
    Given o catálogo legado
    And um requerimento com os seguintes fatos:
      | tipoDeBeneficio | pensao |
      | sexo | null |
      | aposEspecial | false |
    When o filtro legado for executado
    Then os seguintes campos devem ser observados:
      | expectativa.elegivel | true |
      | legado.quantidade_esperada | 1 |
      | legado.quantidade_observada | 1 |
      | legado.divergente | false |
      | legado.inclui | regra-0001 |
      | legado.exclui | regra-0068,regra-0069,regra-0070 |
