from selenium import webdriver
import time
import pytest
from test_e2e.POM.pages import MainPage, SignInPage
from test_e2e.utilities.step import scenario
from test_e2e.utilities.welement import welement


@pytest.fixture
def browser():
    driver = webdriver.Chrome('C:/Users/lenovo/Downloads/chromedriver_win32_87/chromedriver.exe')
    welement.set_driver(driver)
    driver.implicitly_wait(2)
    yield driver
    time.sleep(1)
    driver.quit()


@scenario("Test sign in to application")
@pytest.mark.parametrize("usr,pwd",
                         [("user1","password"),("user2","password")])
def test_sign_in(browser, usr, pwd):
    main_page = MainPage(browser)
    main_page = main_page.go()
    sign_page:SignInPage = main_page.Sign_in()
    sign_page.username.send_keys(usr)
    sign_page.password.send_keys(pwd)
    sign_page.save_screen("pic.png")
    assert sign_page.login_form, "Form not found"


