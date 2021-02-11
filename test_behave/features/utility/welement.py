from selenium.webdriver.remote.webelement import WebElement


class welement():
    driver = None

    def __init__(self, loc_type, loc_str):
        self.loc_type = loc_type
        self.loc_str = loc_str

    def __get__(self) -> WebElement:
        return self.driver.find_element(self.loc_type, self.loc_str)
