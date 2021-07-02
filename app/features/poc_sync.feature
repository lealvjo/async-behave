# -- TEST-RUN OUTPUT:

@pocsync
Feature:
  Scenario:
    Given que eu faça get  no id "1"
    And   que eu faça get  no id "2"
    And   que eu faça get  no id "3"
    And   que eu faça get  no id "4"
    And   que eu faça get  no id "5"
    And   que eu faça get  no id "6"
    And   que eu faça get  no id "7"
    Then deve existir todos os ids na lista