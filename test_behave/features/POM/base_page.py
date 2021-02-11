from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import inspect


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __getattribute__(self, attr):
        attr_name = __class__.__dict__.get(attr)
        if type(attr_name) is tuple:
            return self.driver.find_element(*attr_name)
        return super(__class__, self).__getattribute__(attr)

    def visit(self, page):
        self.driver.get(page)


