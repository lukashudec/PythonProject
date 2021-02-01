@web_test
Feature: LambdaTest search
  Scenario: Search for google on google
    Given I am on the https://www.google.com homepage
    When I enter search term: google
    Then Search results for google should appear