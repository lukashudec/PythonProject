from selenium import webdriver
import time


def before_all(context):
    context.driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
    context.driver.implicitly_wait(3)


def after_all(context):
    time.sleep(5)
    context.driver.close()