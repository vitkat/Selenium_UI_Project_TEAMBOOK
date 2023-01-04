from .base_page import BasePage
from .locators import RegistrationPageLocators


class Registration_Page(BasePage):
    def go_first_name(self):
        first_name = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME)
        first_name.send_keys('John')

    def go_last_name(self):
        last_name = self.browser.find_element(*RegistrationPageLocators.LAST_NAME)
        last_name.send_keys('Travis')

    def go_email(self):
        email = self.browser.find_element(*RegistrationPageLocators.EMAIL)
        email.send_keys('qwerty@mail.ru')

    def go_company_name(self):
        company_name = self.browser.find_element(*RegistrationPageLocators.COMPANY_NAME)
        company_name.send_keys('BobbyStars')

    def go_password(self):
        password = self.browser.find_element(*RegistrationPageLocators.PASSWORD)
        password.send_keys('1234554321rb')

    def go_check_box(self):
        check_box = self.browser.find_element(*RegistrationPageLocators.CHECK_BOX)
        check_box.click()

    def go_button_create(self):
        button_create = self.browser.find_element(*RegistrationPageLocators.BUTTON_CREATE)
        button_create.click()

