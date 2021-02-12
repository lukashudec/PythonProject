from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from test_behave.features.POM.base_page import FaqPage, SignInPage
from test_e2e.utilities.step import step, step_in
from test_e2e.utilities.welement import welement


class BasePage:
    root = None

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def go(self):
        step_in(("Opening page", self.root))
        self.driver.get(self.root)
        return self

    def find(self, element):
        return self.driver.find_element(*element)

    @step("Saving screenshot")
    def save_screen(self, path):
        return self.driver.save_screenshot(path)


class BoardGameBasePage(BasePage):
    search_bar = welement(By.NAME, "searchTerm")
    sign_in = welement(By.LINK_TEXT, "Sign In")
    help_dropdown = welement(By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = welement(By.LINK_TEXT, "FAQ")

    @step("Click on Sign in button")
    def Sign_in(self):
        self.sign_in.click()
        return SignInPage(self.driver)


class SignInPage(BasePage):
    login_form = welement(By.XPATH, "//form[@name='loginform']")
    username = welement(By.ID, "inputUsername")
    password = welement(By.ID, "inputPassword")


class MainPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/'


class GeekSearchResultPage(BoardGameBasePage):
    game_link = welement(By.LINK_TEXT, 'Prophecy')
    game_image = welement(By.XPATH, "//img[@alt='Board Game: Prophecy']")


class FaqPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/wiki/page/BoardGameGeek_FAQ'
    help_search = welement(By.ID, "wiki-search")
    help_search_button = welement(By.NAME, "B1")
    forum_table = welement(By.XPATH, "//table[@class='forum_table']")
    faq_article = welement(By.XPATH, "//a[@href='/wiki/page/BoardGameGeek_FAQ']")
