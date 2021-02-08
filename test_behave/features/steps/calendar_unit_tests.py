from behave import given, then
from Calendar import CalendarClass
from hamcrest import *


@given('xx calendars')
@given('xx calendar')
def step_impl(context):
    context.calendars = []
    for row in context.table:
        context.calendars.append(CalendarClass.from_string(row['calendars'], row['bounds']))


@then("xx possible meetings at '{expected_result}'")
def step_imp(context, expected_result):
    output_calendar = context.calendars[0].get_possible_events_with(context.calendars[1])
    assert_that(output_calendar,
                equal_to(CalendarClass.extract_time(expected_result)), "different values expected")


@then("xx merged calendar")
def step_impl(context):
    cal1: CalendarClass = context.calendars[0]
    cal2 = context.calendars[1]

    merged_calendar = cal1.merge_with_calendar(cal2)
    output_calendar = CalendarClass.from_string(context.table[0]['calendars'], context.table[0]['bounds'])

    assert_that(merged_calendar.raw_calendar,
                equal_to(output_calendar.raw_calendar), output_calendar.raw_calendar)
    assert_that(merged_calendar.bounds,
                equal_to(output_calendar.bounds), "different values expected")


@then("xx possible meetings with {min_duration} are at {outcome}")
def step_impl(context, min_duration, outcome):
    calendar = context.calendars[0]
    if outcome == '-':
        outcome = []
    else:
        outcome = CalendarClass.extract_time(outcome)

    if min_duration == '0':
        free_time = calendar.get_free_time_pretty()
    else:
        free_time = calendar.get_free_time_pretty(int(min_duration))
    assert_that(free_time,
                equal_to(outcome), 'Not equal')
