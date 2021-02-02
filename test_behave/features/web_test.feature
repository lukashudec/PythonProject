@web_test
Feature: LambdaTest search
  Scenario: Search for google on google
    Given I am on the https://www.boardgamegeek.com/ homepage
    When I enter search term: Prophecy
    Then Search results for link_text: Prophecy should appear
    And Search results for xpath: //img[@alt='Board Game: Prophecy'] should appear
    And verify list