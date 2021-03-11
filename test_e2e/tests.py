from selenium import webdriver
import time
import pytest
from test_e2e.POM.pages import MainPage, HerokuPage
from test_e2e.utilities.step import scenario, STEP_IN, step
from test_e2e.utilities.FindBy import FindBy


@pytest.fixture
def browser():
    driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
    FindBy.set_driver(driver)
    driver.implicitly_wait(2)
    yield driver
    time.sleep(1)
    driver.quit()


@scenario("Test sign in to application")
@pytest.mark.parametrize("usr,pwd",
                         [("user1", "password"),
                          ("user2", "password")])
def test_sign_in(browser, usr, pwd):
    sign_page = MainPage(browser).go()\
        .sign_in()
    STEP_IN("Filling user info")
    sign_page.username.send_keys(usr)
    sign_page.password.send_keys(pwd)

    assert sign_page.verify() > 90, "Image is different then expected"
    assert sign_page.login_form, "Form not found"


@scenario("Test search for game, check if picture and link are shown properly")
@pytest.mark.parametrize("game_name",
                         [("Prophecy"),
                          ("Gloomhaven"),
                          ("Terraforming Mars")])
def test_game_search(browser, game_name):
    main_page = MainPage(browser).go()
    main_page.say("Notification")
    result_page = main_page.search(game_name)
    step("Checking game link and picture")
    result_1 = result_page.get_game_link(game_name)
    result_2 = result_page.get_game_image(game_name)
    assert len(result_1) > 0
    assert len(result_2) > 0


@scenario("Test search in FAQ, check if proper result is shown when searching")
@pytest.mark.parametrize("search_option, search_result",
                         [("API", "BGG_XML_API2"),
                          ("contest", "Official_Contests"),
                          ("contest", "Unofficial_Contests")])
def test_faq_page(browser, search_option, search_result):
    main_page = MainPage(browser).go()
    faq_page = main_page.click_on_help().click_on_faq()
    assert faq_page.help_search is not None
    assert faq_page.faq_article is not None
    faq_page.help_search.send_keys(search_option)
    faq_page.help_search_button.click()
    assert faq_page.check_result_table(search_result) is not None


@scenario("Test search for game, check if picture and link are shown properly")
def test_growler(browser):
    heroku = HerokuPage(browser).go()

    heroku.growl('WATCH ME', 'warning')
    heroku.growl('WATCH ME MORE', 'danger')
    heroku.growl('WATCH ME LESS', 'good')
    heroku.growl('WATCH ME LESS', 'attention')
    time.sleep(10)