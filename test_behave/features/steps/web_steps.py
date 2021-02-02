from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import *
import requests
from xml.etree import ElementTree


def get_list_of_games():
    result = []
    response = requests.get('https://boardgamegeek.com//xmlapi2/hot?type=boardgame')
    print(response.status_code, response.text)
    tree = ElementTree.fromstring(response.content)
    for branch in tree:
        result.append([branch.attrib['rank'], branch.attrib['id'], branch[1].attrib['value']])
    return result


@given('I am on the {page} homepage')
def step(context, page):
    context.driver.get(page)


@when('I enter search term: {search}')
def step(context, search):
    element = context.driver.find_element(By.NAME, "searchTerm")
    element.send_keys(search)
    element.send_keys(Keys.ENTER)


@then('Search results for link_text: {search_result} should appear')
def step(context, search_result):
    elements = context.driver.find_elements_by_link_text(search_result)
    assert_that(elements, is_not(equal_to(None)), 'Elements not found')


@then('Search results for xpath: {search_result} should appear')
def step(context, search_result):
    elements = context.driver.find_elements_by_xpath(search_result)
    assert_that(elements, is_not(equal_to(None)), 'Elements not found')
