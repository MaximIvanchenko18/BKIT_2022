Feature: Unique() iterator work

  Scenario: List of Integers
    Given we have list of integers [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
     When we run Unique() iterator
     Then we get values without repetition [1, 2]
  Scenario: Generator of Integers
    Given we have generator [1, 1, 3, 1, 1, 2, 2, 3, 2, 1]
     When we run Unique() iterator
     Then we get values without repetition [1, 2, 3]
  Scenario: List of Strings
    Given we have list of strings [a, A, b, B, a, A, b, B]
     When we run Unique() iterator
      Then we get symbols without repetition [a, b, A, B]
  Scenario: List of Strings with ignore_case
    Given we have list of strings [a, A, b, B, a, A, b, B]
     When we run Unique() iterator with ignore_case
      Then we get symbols without repetition [a, b]
