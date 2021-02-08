@class_unit_test
Feature: Calendar
  Scenario: Calendar3
    Given xx calendars
      | calendars                                       | bounds      |
      | 09:00-10:30,12:00-13:00,16:00-18:00             | 09:00-20:00 |
      | 10:00-11:45,12:30-14:30,14:30-15:00,16:00-17:00 | 10:00-18:30 |
    Then xx possible meetings at '15:00-16:00,18:00-18:30'


  Scenario Outline: Calendar free time
    Examples: data
      | min_duration | outcome                             |
      | 181          | -                                   |
      | 121          | 13:00-16:00                         |
      | 60           | 13:00-16:00,18:00-20:00             |
      | 30           | 10:30-11:00,13:00-16:00,18:00-20:00 |
      | 0            | 10:30-11:00,13:00-16:00,18:00-20:00 |
    Given xx calendar
      | calendars                           | bounds      |
      | 09:00-10:30,11:00-13:00,16:00-18:00 | 09:00-20:00 |
    Then xx possible meetings with <min_duration> are at <outcome>

  Scenario: Merging calendars
    Given xx calendars
      | calendars               | bounds      |
      | 12:00-13:00,16:00-18:00 | 09:00-20:00  |
      | 10:00-11:45,12:30-14:30 | 10:00-18:30 |
    Then xx merged calendar
      | calendars                                       | bounds      |
      | 10:00-11:45,12:00-13:00,12:30-14:30,16:00-18:00 | 10:00-18:30 |
