from behave import given, then, when
from hamcrest import *
import requests

API_DEF = 'https://jsonplaceholder.typicode.com'


@given('title:{title}, body:{body}, userId:{user_id}')
def step(context, title, body, user_id):
    context.request = {'title': title, 'body': body, 'userId': user_id}


@when('I request post with id:{post_id}')
def step(context, post_id):
    url = API_DEF + '/posts/' + str(post_id)
    response = requests.get(url)
    context.response = response
    context.response_json = response.json()


@when('I send post request')
def step(context):
    url = API_DEF + '/posts/'
    response = requests.post(url, context.request)
    context.response = response
    context.response_json = response.json()


@then('response match key:"{key}" equal to "{value}"')
def step(context, key, value):
    assert_that(context.response_json.get(key), equal_to(value), 'actual differs from expected')


@then('response contains key:"{key}" equal to "{value}"')
def step(context, key, value):
    assert_that(value in context.response_json.get(key), equal_to(True), 'actual differs from expected')


@then('response status is {code:d}')
def step(context, code):
    assert_that(context.response.status_code, equal_to(code), 'actual differs from expected')
