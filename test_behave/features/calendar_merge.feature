@unit_test
Feature: Calendar
  Scenario: Calendar
    Given '9:00-10:30,12:00-13:00,16:00-18:00','9:00-20:00','10:00-11:45,12:30-14:30,14:30-15:00,16:00-17:00','10:00-18:30'
    Then possible meetings at '15:00-16:00,18:00-18:30'


  Scenario: Calendar3
    Given calendars
       | calendars                                       | bounds      |
       | 9:00-10:30,12:00-13:00,16:00-18:00              | 9:00-20:00  |
       | 10:00-11:45,12:30-14:30,14:30-15:00,16:00-17:00 | 10:00-18:30 |
    Then possible meetings at '15:00-16:00,18:00-18:30'