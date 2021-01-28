@api_test
Feature: Some feature
  Scenario: Some scenario
    When I request post 1
    Then response contains key:"title" equal to "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    And response status is 200

  Scenario: Some failing scenario
    When I request post 1
    Then response contains key:"title" equal to "FAIL"
    And response status is 400