from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
driver.implicitly_wait(3)


@given('I am on the {page} homepage')
def step(context, page):
    driver.get(page)

    try:
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src, 'consent.google.com')]"))
        driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span').click()
    except:
        pass


@when('I enter search term: {search}')
def step(context, search):
    element = driver.find_element(By.NAME, "q")
    element.send_keys(search)


@then('Search results for {search_result} should appear')
def step(context, search_result):
    time.sleep(5)
    driver.close()