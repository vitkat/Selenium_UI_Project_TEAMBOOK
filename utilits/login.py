from pages.login_page import Login_Page
from pages.settings import url_login_page


def login(browser):
    link = url_login_page
    page = Login_Page(browser, link)
    page.open()
    page.go_login()
    page.go_password()
    page.go_button()
