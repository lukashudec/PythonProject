from selenium.webdriver.remote.webelement import WebElement


class welement(WebElement):
    driver = None

    def __init__(self, loc_type, loc_str, return_page = None):
        self.loc_type = loc_type
        self.loc_str = loc_str
        self.return_page = return_page

    def __get__(self) -> WebElement:
        return self.driver.find_element(self.loc_type, self.loc_str)

    def click(self):
        if self.return_page is not None:
            super.click()
            return self.return_page
        return super.click()

some = welement('xpath', '...')


