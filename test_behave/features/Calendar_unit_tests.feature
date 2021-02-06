@unit_test
Feature: Calendar
  Scenario: Calendar3
    Given calendars
      | calendars                                       | bounds      |
      | 9:00-10:30,12:00-13:00,16:00-18:00              | 9:00-20:00  |
      | 10:00-11:45,12:30-14:30,14:30-15:00,16:00-17:00 | 10:00-18:30 |
    Then possible meetings at '15:00-16:00,18:00-18:30'


  Scenario Outline: Calendar free time
    Examples: data
      | min duration | outcome                                                      |
      | 181          | []                                                           |
      | 121          | [['13:00', '16:00']]                                         |
      | 60           | [['13:00', '16:00'], ['18:00', '20:00']]                     |
      | 30           | [['10:30', '11:00'], ['13:00', '16:00'], ['18:00', '20:00']] |
    Given calendar
      | calendar                            | bounds      |
      | 09:00-10:30,11:00-13:00,16:00-18:00 | 09:00-20:00 |
    Then possible meetings with <min duration> are at <outcome>
