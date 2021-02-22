import time

from locust import events
from selenium.webdriver.remote.webelement import WebElement


# lazy loader for WebElements / WEwrapper
# java eq is @FindBy
# Can by only initialized in static context
# Cache and added measure not yet tested

class FindBy(WebElement):
    driver = None
    cache = {}

    def __init__(self, loc_type, loc_str, use_cache=True, measure=False):
        self.loc_type = loc_type
        self.loc_str = loc_str
        self.use_cache = use_cache
        self.measure = measure

    def __get__(self, instance, owner):
        if (FindBy.cache.get(self.describe()) is None) or self.use_cache:
            start_time = time.time()
            web_element = self.driver.find_element(self.loc_type, self.loc_str)
            stop_time = (time.time() - start_time) * 1000
            events.request_success.fire(request_type="Element",
                                        name=self.describe(),
                                        response_time=int(stop_time),
                                        response_length=0)
            FindBy.cache[self.describe()] = web_element
            return web_element
        else:
            print("using cached value")
            return FindBy.cache.get(self.describe())

    def describe(self):
        return str(self.loc_type+":"+self.loc_str)

    @staticmethod
    def set_driver(driver):
        FindBy.driver = driver




