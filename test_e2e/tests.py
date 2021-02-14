from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys

from test_e2e.POM.pages import MainPage, SignInPage, GeekSearchResultPage
from test_e2e.utilities.step import scenario, STEP_IN
from test_e2e.utilities.welement import WElement


@pytest.fixture
def browser():
    driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
    WElement.set_driver(driver)
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
    result_page = main_page.search(game_name)
    STEP_IN("Checking game link and picture")
    result_1 = result_page.get_game_link(game_name)
    result_2 = result_page.get_game_image(game_name)
    assert len(result_1) > 0
    assert len(result_2) > 0


