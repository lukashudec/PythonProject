@web_test
Feature: LambdaTest search
  Scenario: Search for LambdaTest on DuckDuckGo
    Given I am on the DuckDuckGo homepage
    When I enter search term: google
    Then Search results for google should appear