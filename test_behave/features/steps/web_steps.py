from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import *
import requests
from xml.etree import ElementTree

from selenium.webdriver.remote.webelement import WebElement


def get_list_of_games():
    result = []
    response = requests.get('https://boardgamegeek.com//xmlapi2/hot?type=boardgame')
    print(response.status_code, response.text)
    tree = ElementTree.fromstring(response.content)
    for branch in tree:
        result.append([branch.attrib['rank'], branch.attrib['id'], branch[1].attrib['value']])
    return result


@given('I am on the {page} homepage')
@given('I am on the {page} FAQ page')
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


@when('I click on Sign in button')
def step(context):
    context.driver.find_element(By.LINK_TEXT, "Sign In").click()


@then('it contains field username')
def step(context):
    username = context.driver.find_element(By.ID, "inputUsername")
    username.send_keys("user")
    assert_that(username, is_not(equal_to(None)), 'Elements not found')


@then('it contains field password')
def step(context):
    password = context.driver.find_element(By.ID, "inputPassword")
    password.send_keys("pass")
    assert_that(password, is_not(equal_to(None)), 'Elements not found')


@then('popup is shown')
def step(context):
    login_form = context.driver.find_element(By.XPATH, "//form[@name='loginform']")
    assert_that(login_form, is_not(equal_to(None)), 'Elements not found')


@then('verify list')
def step(context):
    pass


@given('search box is present')
@then('search box is present')
def step(context):
    help_search = context.driver.find_element(By.ID, "wiki-search")
    assert_that(help_search, is_not(equal_to(None)), 'Elements not found')


@given('BoardGameGeek FAQ article is present')
@then('BoardGameGeek FAQ article is present')
def step(context):
    table = context.driver.find_element(By.XPATH, "//table[@class='forum_table']")
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    result: WebElement = table.find_element(By.XPATH, "//a[@href='/wiki/page/BoardGameGeek_FAQ']")
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I search for {search_option}')
@when('I search for {search_option}')
def step(context, search_option):
    help_search = context.driver.find_element(By.ID, "wiki-search")
    help_search.send_keys(search_option)
    help_search_button = context.driver.find_element(By.NAME, "B1")
    help_search_button.click()


@given('List of results with {search_result} is shown')
@then('List of results with {search_result} is shown')
def step(context, search_result):
    table: WebElement = context.driver.find_element(By.XPATH, "//table[@class='forum_table']")
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    result: WebElement = table.find_element(By.XPATH, "//a[@href='/wiki/page/"+search_result+"']")
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I click on Help')
def step(context):
    help_search = context.driver.find_element(By.XPATH, "//button[contains(.,'Help ')]")
    help_search.click()
    assert_that(help_search, is_not(equal_to(None)), 'Elements not found')


@given('I click on FAQ')
def step(context):
    faq = context.driver.find_element(By.LINK_TEXT, "FAQ")
    faq.click()
    assert_that(faq, is_not(equal_to(None)), 'Elements not found')


'''
def page_map_preparation(driver):
    root = 'https://www.boardgamegeek.com/'
    search_bar = driver.find_element(By.NAME, "searchTerm")
    game_link = driver.find_elements_by_link_text('Prophecy')
    game_image = driver.find_elements_by_xpath("//img[@alt='Board Game: Prophecy']")
    login = driver.find_element(By.LINK_TEXT, "Sign In")
    username = driver.find_element(By.ID, "inputUsername")
    password = driver.find_element(By.ID, "inputPassword")
    loginform = driver.find_element(By.XPATH, "//button[contains(.,'Cancel')]")
    help_dropdown = driver.find_element(By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = driver.find_element(By.LINK_TEXT, "FAQ")
    help_search = driver.find_element(By.ID, "wiki-search")
    help_search_button = driver.find_element(By.NAME, "B1")
'''
