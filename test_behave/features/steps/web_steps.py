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


@given('I am on the {page_url} homepage')
@given('I am on the {page_url} FAQ page')
def step(context, page_url):
    page = BoardGamePage(context.driver)
    page.visit(page_url)


@when('I enter search term: {search}')
def step(context, search):
    page = BoardGamePage(context.driver)
    page.search_bar.send_keys(search+Keys.ENTER)


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
    page = BoardGamePage(context.driver)
    page.login.click()


@then('it contains field username')
def step(context):
    page = BoardGamePage(context.driver)
    page.username.send_keys("user")
    assert_that(page.username, is_not(equal_to(None)), 'Elements not found')


@then('it contains field password')
def step(context):
    page = BoardGamePage(context.driver)
    page.password.send_keys("pass")
    assert_that(page.password, is_not(equal_to(None)), 'Elements not found')


@then('popup is shown')
def step(context):
    page = BoardGamePage(context.driver)
    assert_that(page.login_form, is_not(equal_to(None)), 'Elements not found')


@then('verify list')
def step(context):
    pass


@given('search box is present')
@then('search box is present')
def step(context):
    page = BoardGamePage(context.driver)
    assert_that(page.help_search, is_not(equal_to(None)), 'Elements not found')


@given('BoardGameGeek FAQ article is present')
@then('BoardGameGeek FAQ article is present')
def step(context):
    page = BoardGamePage(context.driver)
    table = page.forum_table
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    result = page.faq_article
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I search for {search_option}')
@when('I search for {search_option}')
def step(context, search_option):
    page = BoardGamePage(context.driver)
    page.help_search.send_keys(search_option)
    page.help_search_button.click()


@given('List of results with {search_result} is shown')
@then('List of results with {search_result} is shown')
def step(context, search_result):
    page = BoardGamePage(context.driver)
    table = page.forum_table
    result = table.find_element(By.XPATH, "//a[@href='/wiki/page/"+search_result+"']")
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I click on Help')
def step(context):
    page = BoardGamePage(context.driver)
    page.help_dropdown.click()


@given('I click on FAQ')
def step(context):
    page = BoardGamePage(context.driver)
    page.faq_button.click()


class BoardGamePage:
    root = 'https://www.boardgamegeek.com/'
    faq = 'https://www.boardgamegeek.com/wiki/page/BoardGameGeek_FAQ'
    search_bar = (By.NAME, "searchTerm")
    game_link = (By.LINK_TEXT, 'Prophecy')
    game_image = (By.XPATH, "//img[@alt='Board Game: Prophecy']")
    login = (By.LINK_TEXT, "Sign In")
    username = (By.ID, "inputUsername")
    password = (By.ID, "inputPassword")
    login_form = (By.XPATH, "//button[contains(.,'Cancel')]")
    help_dropdown = (By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = (By.LINK_TEXT, "FAQ")
    help_search = (By.ID, "wiki-search")
    help_search_button = (By.NAME, "B1")
    login_form = (By.XPATH, "//form[@name='loginform']")
    forum_table = (By.XPATH, "//table[@class='forum_table']")
    faq_article = (By.XPATH, "//a[@href='/wiki/page/BoardGameGeek_FAQ']")

    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, attr):
        __dict__ = BoardGamePage.__dict__.get(attr)
        if type(__dict__) is tuple:
            print(str(__dict__))
            print(str(":: "+tuple(__dict__)[0]))
            if str(tuple(__dict__)[0]) in ("id","xpath","link text","partial link text","name","tag name","class name","css selector"):
                return self.get(__dict__)
        return super(BoardGamePage, self).__getattribute__(attr)


    def visit(self,page):
        self.driver.get(page)

    def get(self,loc):
        if type(loc) is WebElement:
            return loc
        return self.driver.find_element(*loc)