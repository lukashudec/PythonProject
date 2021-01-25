from behave import given, then
from calendar_merge import *
from hamcrest import *

l1 = []
lb1 = []


def extract_time_frame(input_list):
    result = []
    for ll in input_list.split(','):
        result.append(ll.split('-'))
    return result


def extract_time(input_list):
    result = []
    for ll in input_list.split(','):
        result = (ll.split('-'))
    return result


@given("'{list1}','{bound1}','{list2}','{bound2}'")
def step_impl(context, list1, bound1, list2, bound2):
    context.c1 = extract_time_frame(list1)
    context.b1 = extract_time(bound1)
    context.c2 = extract_time_frame(list2)
    context.b2 = extract_time(bound2)


@given("calendar '{list1}' with bounds '{bound1}'")
def step_impl(context, list1, bound1):
    l1.append(extract_time_frame(list1))
    lb1.append(extract_time(bound1))


@then("expected result is '{bound2}'")
def step_impl(context, bound2):
    assert_that(get_free_block(context.c1, context.b1, context.c2, context.b2),
                equal_to(extract_time_frame(bound2)), "different values expected")


@then("possible meetings are '{bound2}'")
def step_imp(context, bound2):
    assert_that(get_free_block(l1[0], lb1[0], l1[1], lb1[1]),
                equal_to(extract_time_frame(bound2)), "different values expected")
