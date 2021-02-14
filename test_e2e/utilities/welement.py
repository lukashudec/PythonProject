from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class WEwrapper(WebElement):
    def __init__(self, parent, id_, w3c):
        super().__init__(parent, id_, w3c)

    @classmethod
    def from_we(cls, webelement: WebElement,):
        return cls(webelement.parent, webelement.id, webelement._w3c)

    def submit_keys(self, inp_str):
        self.send_keys(inp_str + Keys.ENTER)
        return self



class WElement(WEwrapper):
    # lazy loader for WebElements / WEwrapper
    driver = None

    def __init__(self, loc_type, loc_str, return_page=None):
        self.loc_type = loc_type
        self.loc_str = loc_str
        self.return_page = return_page

    def __get__(self, instance, owner):
        return WEwrapper.from_we(self.driver.find_element(self.loc_type, self.loc_str))

    @staticmethod
    def set_driver(driver):
        WElement.driver = driver

