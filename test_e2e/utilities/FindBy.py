from selenium.webdriver.remote.webelement import WebElement


# lazy loader for WebElements / WEwrapper
# java eq is @FindBy
#
class FindBy(WebElement):
    driver = None

    def __init__(self, loc_type, loc_str):
        self.loc_type = loc_type
        self.loc_str = loc_str

    def __get__(self, instance, owner):
        return self.driver.find_element(self.loc_type, self.loc_str)

    @staticmethod
    def set_driver(driver):
        FindBy.driver = driver
