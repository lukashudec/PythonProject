@web_test
Feature: LambdaTest search

  Scenario Outline: Test search for game, check if picture and link are shown properly
    Examples: Data
      | game_name         |
      | Prophecy          |
      | Gloomhaven        |
      | Terraforming Mars |
    Given I am on the homepage
    When I enter search term: <game_name>
    Then Search results for link_text: <game_name> should appear
    And Search results for xpath: //img[@alt='Board Game: <game_name>'] should appear
    And verify list

  Scenario: Test if sign in is available and it contains field username and password
    Given I am on the homepage
    When I click on Sign in button
    Then popup is shown
    And it contains field username
    And it contains field password

  Scenario Outline: Test FAQ page and searching
    Examples: Data
      | search_option | search_result       |
      | API           | BGG_XML_API2        |
      | contest       | Official_Contests   |
      | contest       | Unofficial_Contests |
    Given I am on the FAQ page
    Then search box is present
    And BoardGameGeek FAQ article is present
    When I search for <search_option>
    Then List of results with <search_result> is shown

  Scenario Outline: Test FAQ page and searching - alternative scenario
    Examples: Data
      | search_option | search_result       |
      | API           | BGG_XML_API2        |
      | contest       | Official_Contests   |
      | contest       | Unofficial_Contests |
    * I am on the homepage
    * I click on Help
    * I click on FAQ
    * search box is present
    * BoardGameGeek FAQ article is present
    * I search for <search_option>
    * List of results with <search_result> is shown

    @wip2
  Scenario Outline: Test FAQ page and searching - extra alternative scenario
    Examples: Data
      | search_option | search_result       |
      | API           | BGG_XML_API2        |
      | contest       | Official_Contests   |
      | contest       | Unofficial_Contests |
  * scenario hidden in one step <search_option> , <search_result>