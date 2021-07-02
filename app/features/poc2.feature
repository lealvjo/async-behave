# -- TEST-RUN OUTPUT:

@poc2
Feature:
  Scenario:
    Given I dispatch an async-call with param "Alice"
    And   I dispatch an async-call with param "Bob"
    And   I dispatch an async-call with param "Leo"
    And   I dispatch an async-call with param "Lucas"
    And   I dispatch an async-call with param "Joao"
    And   I dispatch an async-call with param "Pedro"
    Then the collected result of the async-calls is "ALICE, BOB, JOAO, LEO, LUCAS, PEDRO"