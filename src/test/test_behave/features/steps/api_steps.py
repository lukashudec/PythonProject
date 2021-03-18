import requests
from behave import given, then, when
from hamcrest import *

API_ENDPOINT = 'https://jsonplaceholder.typicode.com'
GET_POSTS = API_ENDPOINT + '/posts/'
POST_POSTS = API_ENDPOINT + '/posts/'


@given('title:{title}, body:{body}, userId:{user_id}')
def step(context, title, body, user_id):
    context.request = {'title': title, 'body': body, 'userId': user_id}


@when('I request post with id:{post_id}')
def step(context, post_id):
    context.response = requests.get(GET_POSTS + str(post_id))
    context.response_json = context.response.json()


@when('I send post request')
def step(context):
    context.response = requests.post(POST_POSTS, context.request)
    context.response_json = context.response.json()


@then('response match key:"{key}" equal to "{value}"')
def step(context, key, value):
    assert_that(context.response_json.get(key), equal_to(value), 'actual differs from expected')


@then('response contains key:"{key}" equal to "{value}"')
def step(context, key, value):
    assert_that(value in context.response_json.get(key), equal_to(True), 'actual differs from expected')


@then('response status is {code:d}')
def step(context, code):
    assert_that(context.response.status_code, equal_to(code), 'actual differs from expected')
