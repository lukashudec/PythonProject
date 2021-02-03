@web_test
Feature: LambdaTest search
  Scenario Outline: Search for google on google
    Examples: Data
      | game_name         |
      | Prophecy          |
      | Gloomhaven        |
      | Terraforming Mars |
    Given I am on the https://www.boardgamegeek.com/ homepage
    When I enter search term: <game_name>
    Then Search results for link_text: <game_name> should appear
    And Search results for xpath: //img[@alt='Board Game: <game_name>'] should appear
    And verify list

  Scenario: Login
    Given I am on the boardgamegeek homepage
    When I click on Sign in button
    Then popup is shown
    And it contains field username
    And it contains field password

  Scenario Outline: Search for google on google
    Examples: Data
      | search_option | search_result     |
      | API           | BGG XML API2      |
      | contest       | Official Contests |
      | contest       | Unofficial Contests |
    Given I am on the boardgamegeek FAQ page
    Then search box is present
    And BoardGameGeek FAQ article is present
    When I search for <search_option>
    Then List of results with <search_result> is shown
