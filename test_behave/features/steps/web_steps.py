from behave import given, then, when
from hamcrest import *
from selenium import *

page = 'https://www.duckduckgo.com'
driver = webdriver.Firefox()
driver.implicitly_wait(3)

@given('I am on the {page} homepage')
def step(context, page):
    driver.get(page)

    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src, 'consent.google.com')]"))
    driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()

@when('I enter search term: {search}')
def step(context, search):
    element = driver.find_element(By.NAME, "q")
    element.send_keys("search")

@then('Search results for {search_result} should appear')
def step(context, search_result):
    driver.close()