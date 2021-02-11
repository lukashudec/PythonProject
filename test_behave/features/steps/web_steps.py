import inspect

from behave import given, then, when, runner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import *
from test_behave.features.POM.bbg_base_page import FaqPage, MainPage


@given('I am on the homepage')
def step_home_page(context):
    page = MainPage(context.driver)
    page.visit()


@given('I am on the FAQ page')
def step_faq_page(context):
    page = FaqPage(context.driver)
    page.visit()


@when('I enter search term: {search}')
def step(context, search):
    page = MainPage(context.driver)
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
    page = MainPage(context.driver)
    page.login.click()


@then('it contains field username')
def step(context):
    page = MainPage(context.driver)
    page.username.send_keys("user")
    assert_that(page.username, is_not(equal_to(None)), 'Elements not found')


@then('it contains field password')
def step(context):
    page = MainPage(context.driver)
    page.password.send_keys("pass")
    assert_that(page.password, is_not(equal_to(None)), 'Elements not found')


@then('popup is shown')
def step(context):
    page = MainPage(context.driver)
    assert_that(page.login_form, is_not(equal_to(None)), 'Elements not found')


@then('verify list')
def step(context):
    pass


@given('search box is present')
@then('search box is present')
def step_search_present(context):
    page = FaqPage(context.driver)
    assert_that(page.help_search, is_not(equal_to(None)), 'Elements not found')


@given('BoardGameGeek FAQ article is present')
@then('BoardGameGeek FAQ article is present')
def step_article_present(context):
    page = FaqPage(context.driver)
    table = page.forum_table
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    result = page.faq_article
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I search for {search_option}')
@when('I search for {search_option}')
def step_search_for(context, search_option):
    page = FaqPage(context.driver)
    page.help_search.send_keys(search_option)
    page.help_search_button.click()


@given('List of results with {search_result} is shown')
@then('List of results with {search_result} is shown')
def step_list_shown(context, search_result):
    page = FaqPage(context.driver)
    table = page.forum_table
    result = table.find_element(By.XPATH, "//a[@href='/wiki/page/"+search_result+"']")
    assert_that(table, is_not(equal_to(None)), 'Elements not found')
    assert_that(result, is_not(equal_to(None)), 'Elements not found')


@given('I click on Help')
def step_help_click(context):
    page = MainPage(context.driver)
    page.help_dropdown.click()


@given('I click on FAQ')
def step_faq_click(context):
    page = MainPage(context.driver)
    page.faq_button.click()


@given('scenario hidden in one step {search_option} , {search_result}')
def step(context, search_option, search_result):

    step_home_page(context)
    step_help_click(context)
    get_decorators(step_faq_click, context)
    step_search_present(context)
    step_article_present(context)
    get_decorators(step_search_for,context, search_option)
    step_list_shown(context, search_result)


def get_decorators(function, *args):
    source = inspect.getsource(function)
    index1 = source.find('@')
    index2 = source.find("def")
    print(str(source[index1:index2]))
    function(*args)
