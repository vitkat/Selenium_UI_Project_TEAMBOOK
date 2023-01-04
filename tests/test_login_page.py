import time
import pytest
from pages.login_page import Login_Page
from pages.settings import url_login_page
from utilits.login import login
from pages.settings import url_project_page


@pytest.mark.smoke
@pytest.mark.regression
def test_go_authorization(browser):
    """Test performing authorization"""
    link = url_login_page
    page = Login_Page(browser, link)
    page.open()
    page.go_login()
    page.go_password()
    page.go_button()
    time.sleep(2)


@pytest.mark.smoke
def test_create_new_organiz(browser):
    """Click to button <create new organization>"""
    link = url_login_page
    page = Login_Page(browser, link)
    page.open()
    page.go_create_new_organiz()
    time.sleep(2)


@pytest.mark.regression
def test_forgot_pass(browser):
    """Click to button <forgot password>"""
    link = url_login_page
    page = Login_Page(browser, link)
    page.open()
    page.go_forgot_pass()
    time.sleep(2)


@pytest.mark.smoke
def test_authoriz_google(browser):
    """Test performing authorization with Google"""
    link = url_login_page
    page = Login_Page(browser, link)
    page.open()
    page.go_authoriz_google()
    time.sleep(2)


@pytest.mark.skip
def test_logout(browser):
    """The test that comes out of the user's personal account"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Login_Page(browser, link)
    page.open()
    page.click_personal()
    page.click_logout()
    time.sleep(2)