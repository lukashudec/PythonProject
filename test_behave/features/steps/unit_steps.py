from behave import given, then, when
from calendar_merge import *
from hamcrest import *


def extract_time(input_list):
    result = []
    for time_frame in input_list.split(','):
        result.append(time_frame.split('-'))
    return result


@given("'{list1}','{bound1}','{list2}','{bound2}'")
def step_impl(context, list1, bound1, list2, bound2):
    context.calendars = []
    context.bounds = []
    context.calendars.append(extract_time(list1))
    context.bounds.append(extract_time(bound1))
    context.calendars.append(extract_time(list2))
    context.bounds.append(extract_time(bound2))


@given('calendars')
def step_impl(context):
    context.calendars = []
    context.bounds = []
    for row in context.table:
        context.calendars.append(extract_time(row['calendars']))
        context.bounds.append(extract_time(row['bounds']))


@then("possible meetings at '{expected_result}'")
def step_imp(context, expected_result):
    assert_that(get_free_block(context.calendars[0], context.bounds[0], context.calendars[1], context.bounds[1]),
                equal_to(extract_time(expected_result)), "different values expected")
