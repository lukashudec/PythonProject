from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import inspect


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __getattributee__(self, attr):
        attr_name = __class__.__dict__.get(attr)
        if type(attr_name) is tuple:
            return self.driver.find_element(*attr_name)
        return super(__class__, self).__getattribute__(attr)

    def __getattribute__(self, attr):
        lol = None
        for i in inspect.getmro(type(self)):
            lol = i.__dict__.get(attr)
            if lol is not None:
                if type(lol) is tuple:
                    if str(tuple(lol)[0]) in (
                            "id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                            "css selector"):
                        return self.driver.find_element(*lol)
        return super().__getattribute__(attr)

    def visit(self, page):
        self.driver.get(page)

    def find(self, element):
        return self.driver.find_element(*element)


