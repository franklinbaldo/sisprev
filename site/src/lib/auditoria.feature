Feature: Legacy selector audit

  Scenario: harmful agents 66/15 band
    Given the legacy catalog
    And a request with the following facts:
      | tipoDeBeneficio | voluntaria |
      | sexo | null |
      | aposEspecial | true |
      | dataAdmissao | 2020-01-10 |
      | dataDireito | 2022-06-01 |
      | faixa_exposicao | 66-pontos-15-anos |
    When the legacy filter is executed
    Then the following fields are observed:
      | expectativa.elegivel | true |
      | expectativa.faixa_exposicao | 66-pontos-15-anos |
      | legado.quantidade_esperada | 1 |
      | legado.quantidade_observada | 26 |
      | legado.divergente | true |
      | legado.inclui | regra-0068,regra-0069,regra-0070 |
      | legado.exclui | nenhum |
      | legado.fora_escopo | regra-0001 |

  Scenario: harmful agents insufficient points
    Given the legacy catalog
    And a request with the following facts:
      | tipoDeBeneficio | voluntaria |
      | sexo | null |
      | aposEspecial | true |
      | dataAdmissao | 2020-01-10 |
      | dataDireito | 2022-06-01 |
      | pontos | 65 |
      | anos_exposicao | 15 |
      | faixa_exposicao | nenhuma |
    When the legacy filter is executed
    Then the following fields are observed:
      | expectativa.elegivel | false |
      | expectativa.faixa_exposicao | nenhuma |
      | legado.quantidade_esperada | 0 |
      | legado.quantidade_observada | 26 |
      | legado.divergente | true |
      | legado.inclui | regra-0068,regra-0069,regra-0070 |
      | legado.exclui | nenhum |
      | legado.fora_escopo | regra-0001 |

  Scenario: pension family uses the same steps
    Given the legacy catalog
    And a request with the following facts:
      | tipoDeBeneficio | pensao |
      | sexo | null |
      | aposEspecial | false |
    When the legacy filter is executed
    Then the following fields are observed:
      | expectativa.elegivel | false |
      | legado.quantidade_esperada | 0 |
      | legado.quantidade_observada | 0 |
      | legado.divergente | false |
      | legado.inclui | nenhum |
      | legado.exclui | regra-0068,regra-0069,regra-0070 |
