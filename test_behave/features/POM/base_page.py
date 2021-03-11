from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import inspect


class BasePage:
    root = None

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.root)

    def find(self, element):
        return self.driver.find_element(*element)

# attempt at creation of FindBy equivalent (better implementation in test_e2e/utilities/FindBy
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


class BoardGameBasePage(BasePage):
    search_bar: WebElement = (By.NAME, "searchTerm")
    sign_in = (By.LINK_TEXT, "Sign In")
    help_dropdown = (By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = (By.LINK_TEXT, "FAQ")


class SignInPage(BasePage):
    username = (By.ID, "inputUsername")
    password = (By.ID, "inputPassword")
    login_form = (By.XPATH, "//form[@name='loginform']")


class MainPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/'


class GeekSearchResultPage(BoardGameBasePage):
    game_link = (By.LINK_TEXT, 'Prophecy')
    game_image = (By.XPATH, "//img[@alt='Board Game: Prophecy']")


class FaqPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/wiki/page/BoardGameGeek_FAQ'
    help_search = (By.ID, "wiki-search")
    help_search_button = (By.NAME, "B1")
    forum_table = (By.XPATH, "//table[@class='forum_table']")
    faq_article = (By.XPATH, "//a[@href='/wiki/page/BoardGameGeek_FAQ']")

