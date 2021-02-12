@class_unit_test
Feature: Calendar
  Scenario: Test possible free time for events for two calendars
    Given calendars
      | calendars                                       | bounds      |
      | 09:00-10:30,12:00-13:00,16:00-18:00             | 09:00-20:00 |
      | 10:00-11:45,12:30-14:30,14:30-15:00,16:00-17:00 | 10:00-18:30 |
    Then possible meetings at '15:00-16:00,18:00-18:30'


  Scenario Outline: Test free time parametrized computation for single calendar
    Examples: data
      | min_duration | outcome                             |
      | 181          | -                                   |
      | 121          | 13:00-16:00                         |
      | 60           | 13:00-16:00,18:00-20:00             |
      | 30           | 10:30-11:00,13:00-16:00,18:00-20:00 |
      | 0            | 10:30-11:00,13:00-16:00,18:00-20:00 |
    Given calendar
      | calendars                           | bounds      |
      | 09:00-10:30,11:00-13:00,16:00-18:00 | 09:00-20:00 |
    Then possible meetings with <min_duration> are at <outcome>

  Scenario: Test that merging calendars will return proper calendar
    Given calendars
      | calendars               | bounds      |
      | 12:00-13:00,16:00-18:00 | 09:00-20:00  |
      | 10:00-11:45,12:30-14:30 | 10:00-18:30 |
    Then merged calendar
      | calendars                                       | bounds      |
      | 10:00-11:45,12:00-13:00,12:30-14:30,16:00-18:00 | 10:00-18:30 |
