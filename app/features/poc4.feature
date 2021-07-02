@poc
Feature:

  Scenario Outline:
    Given an async-step waits "<time>" seconds

    Examples:
      | time |
      | 5    |
      | 10   |
      | 3    |