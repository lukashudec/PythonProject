from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_e2e.utilities.DesignCheck import DesignCheck
from test_e2e.utilities.Growler import Growler
from test_e2e.utilities.step import step, STEP_IN
from test_e2e.utilities.FindBy import FindBy


class BasePage(object):
    root = None
    template = None

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.growler = Growler(self.driver)

    def go(self):
        STEP_IN("Opening page " + self.root)
        self.driver.get(self.root)
        return self

    def find(self, element):
        return self.driver.find_element(*element)

    @step("Saving screenshot")
    def save_screen(self, path):
        return self.driver.save_screenshot(path)

    @step("Verifying GUI look")
    def verify(self):
        return DesignCheck.verify(self.template, self.driver.get_screenshot_as_png())

    def growl(self, message, level):
        self.growler.growl(message, level)


class BoardGameBasePage(BasePage):
    search_bar = FindBy(By.NAME, "searchTerm")
    sign_in_button = FindBy(By.LINK_TEXT, "Sign In")
    help_dropdown = FindBy(By.XPATH, "//button[contains(.,'Help ')]")
    faq_button = FindBy(By.LINK_TEXT, "FAQ")

    @step("Click on Help")
    def click_on_help(self):
        self.help_dropdown.click()
        return self

    @step("Click on FAQ")
    def click_on_faq(self):
        self.faq_button.click()
        return FaqPage(self.driver)

    @step("Click on Sign in button")
    def sign_in(self):
        self.sign_in_button.click()
        return SignInPage(self.driver)

    @step("Searching for item")
    def search(self, inp_str):
        self.search_bar.send_keys(inp_str + Keys.ENTER)
        return GeekSearchResultPage(self.driver)


class MainPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/'


class HerokuPage(BasePage):
    root = 'https://the-internet.herokuapp.com/'


class GeekSearchResultPage(BoardGameBasePage):

    def get_game_link(self, inp):
        return self.driver.find_elements(By.LINK_TEXT, inp)

    def get_game_image(self, inp):
        return self.driver.find_elements(By.XPATH, "//img[@alt='Board Game: " + inp + "']")


class SignInPage(BasePage):
    template = "C:/Users/lenovo/PycharmProjects/calendar/test_e2e/resources/sign_in_template.png"
    login_form = FindBy(By.XPATH, "//form[@name='loginform']")
    username = FindBy(By.ID, "inputUsername")
    password = FindBy(By.ID, "inputPassword")


class FaqPage(BoardGameBasePage):
    root = 'https://www.boardgamegeek.com/wiki/page/BoardGameGeek_FAQ'
    help_search = FindBy(By.ID, "wiki-search")
    help_search_button = FindBy(By.NAME, "B1")
    forum_table = FindBy(By.XPATH, "//table[@class='forum_table']")
    faq_article = FindBy(By.XPATH, "//a[@href='/wiki/page/BoardGameGeek_FAQ']")

    def check_result_table(self, search_result):
        return self.forum_table.find_element(By.XPATH, "//a[@href='/wiki/page/" + search_result + "']")
