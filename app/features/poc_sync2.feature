# -- TEST-RUN OUTPUT:

@pocsync2
Feature: Testando @pocsync2

  Scenario Outline: Teste Poc
    Given que eu faça get  no id "<id>"
    Examples:
      | id |
      | 1  |
      | 2  |
      | 3  |
      | 4  |
      | 5  |
      | 6  |
      | 7  |