@api_test
Feature: Some feature

  Scenario: Single positive test
    When I request post with id:1
    Then response status is 200
    And response match key:"title" equal to "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

  Scenario: Single negative test
    When I request post with id:1
    Then response status is 200
    And response match key:"title" equal to "FAIL"

  Scenario Outline: First test positive, Other negative
    Examples: Data
      | post_id | post_title | status |
      | 1       | sunt       | 200    |
      | 2       | FAIL       | 200    |
      | 105     | Lorem      | 404    |
    When I request post with id:<post_id>
    Then response status is <status>
    And response contains key:"title" equal to "<post_title>"

  Scenario Outline: All tests positive
    Examples:
      | title   | body      | user_id | status |
      | title1  | body1     | 1       | 201    |
      | title 2 | body body | -1      | 201    |
      | 123     | 123       | abc     | 201    |
    Given title:<title>, body:<body>, userId:<user_id>
    When I send post request
    Then response status is <status>
    And response match key:"body" equal to "<body>"
    And response match key:"title" equal to "<title>"
    And response match key:"userId" equal to "<user_id>"