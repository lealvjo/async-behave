Feature:

  Scenario Outline:
    Given I dispatch an async-call with param "<thing>"
    Then the collected result of the async-calls is "<thingUp>"

    Examples:
      | thing | thingUp |
      | Alice | ALICE   |
      | Bob   | BOB     |
      | Joao  | JOAO    |
      | Leo   | LEO     |
      | Lucas | LUCAS   |
      | Pedro | PEDRO   |