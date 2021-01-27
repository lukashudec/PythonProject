from behave import given, then
from hamcrest import *
import requests


@given('some api')
@then('some api')
@given('api')
def step(context):
    print('not defined')
    assert_that(False, equal_to(True),' this is failing')

