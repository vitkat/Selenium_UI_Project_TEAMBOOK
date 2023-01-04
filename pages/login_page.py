from .settings import VALID_LOGIN, VALID_PASSWORD
from .base_page import BasePage
from .locators import LoginPageLocators


class Login_Page(BasePage):
    def go_login(self):
        login = self.browser.find_element(*LoginPageLocators.EMAIL)
        login.send_keys(VALID_LOGIN)

    def go_password(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys(VALID_PASSWORD)

    def go_button(self):
        button = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        button.click()

    def go_create_new_organiz(self):
        create_new_organiz = self.browser.find_element(*LoginPageLocators.CREEATE_NEW_ORGANIZ)
        create_new_organiz.click()

    def go_forgot_pass(self):
        forgot_pass = self.browser.find_element(*LoginPageLocators.FORGOT_PASS)
        forgot_pass.click()

    def go_authoriz_google(self):
        authoriz_google = self.browser.find_element(*LoginPageLocators.AUTHORIZ_WITH_GOOGLE)
        authoriz_google.click()

    def click_personal(self):
        click = self.browser.find_element(*LoginPageLocators.BUTTON_PERSONAL)
        click.click()

    def click_logout(self):
        out = self.browser.find_element(*LoginPageLocators.LOGOUT)
        out.click()
