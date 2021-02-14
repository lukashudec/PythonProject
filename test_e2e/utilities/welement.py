from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class WElement(WebElement):
    driver = None

    def __init__(self, loc_type, loc_str):
        self.loc_type = loc_type
        self.loc_str = loc_str

    def __get__(self, instance, owner):
        return self.driver.find_element(self.loc_type, self.loc_str)

    @staticmethod
    def set_driver(driver):
        WElement.driver = driver

    def submit_keys(self, input_string):
        return self.send_keys(input_string + Keys.ENTER)

