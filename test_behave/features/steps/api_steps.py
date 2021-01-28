from behave import given, then, when
from hamcrest import *
import requests

API_DEF = 'https://jsonplaceholder.typicode.com'

@given('some api')
@then('some api')
@given('api')
def step(context):
    print('not defined')
    assert_that(False, equal_to(True),' this is failing')

@when('I request post {post_id:d}')
def step(context,post_id):
    url = API_DEF + '/posts/' + str(post_id)
    response = requests.get(url)
    print(response.status_code)
    context.response = response
    context.response_json = response.json()


def step(context):
    url = API_DEF + '/posts/'
    request = {'title': 'MyTitle', 'body': 'MyBody', 'userId': '12'}
    response = requests.post(url, request)
    print(response.status_code)
    print(response.text)

@then('response contains key:"{key}" equal to "{value}"')
def step(context, key, value):
    assert_that(context.response_json.get(key),equal_to(value),'actual differs from expected')

@then('response status is {code:d}')
def step(context, code):
    assert_that(context.response.status_code,equal_to(code),'actual differs from expected')