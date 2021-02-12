from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    root = None

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(self.root)

    def find(self, element):
        return self.driver.find_element(*element)


class BoardGameBasePage(BasePage):
    search_bar: WebElement = (By.NAME, "searchTerm")
    login = (By.LINK_TEXT, "Sign In")
    help_dropdown = (By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = (By.LINK_TEXT, "FAQ")
    login_form = (By.XPATH, "//form[@name='loginform']")


class SignInPage(BasePage):
    username = (By.ID, "inputUsername")
    password = (By.ID, "inputPassword")


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
