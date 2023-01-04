from .base_page import BasePage
from .locators import ProfilePageLocators


class Profile_Page(BasePage):
    def go_edit(self):
        edit = self.browser.find_element(*ProfilePageLocators.EDIT)
        edit.click()

    def go_first_name(self):
        first_name = self.browser.find_element(*ProfilePageLocators.FIRST_NAME)
        first_name.click()

    def click_email_pass(self):
        email = self.browser.find_element(*ProfilePageLocators.BUTTON_EMAIL_PASS)
        email.click()

    def input_old_pass(self):
        old = self.browser.find_element(*ProfilePageLocators.OLD_PASS)
        old.send_keys('5566220')

    def input_new_pass(self):
        new = self.browser.find_element(*ProfilePageLocators.NEW_PASS)
        new.send_keys('556622006')

    def input_confirm_pass(self):
        conf = self.browser.find_element(*ProfilePageLocators.CONF_NEW_PASS)
        conf.send_keys('556622006')

    def button_update(self):
        up = self.browser.find_element(*ProfilePageLocators.BUTTON_UPDATE)
        up.click()

    def button_shedule(self):
        shed = self.browser.find_element(*ProfilePageLocators.BUTTON_SHEDULE)
        shed.click()

    def input_fri(self):
        fri = self.browser.find_element(*ProfilePageLocators.INPUT_FRI)
        fri.send_keys('2')

    def button_save(self):
        save = self.browser.find_element(*ProfilePageLocators.BUTTON_SAVE)
        save.click()

    def button_notification(self):
        notif = self.browser.find_element(*ProfilePageLocators.BUTTON_NOTIFICATION)
        notif.click()

    def radio_button(self):
        but = self.browser.find_element(*ProfilePageLocators.RADIO_BUTTON_1)
        but.click()

    def radio_button_second(self):
        sec = self.browser.find_element(*ProfilePageLocators.RADIO_BUTTON_2)
        sec.click()

    def radio_button_first(self):
        first = self.browser.find_element(*ProfilePageLocators.RADIO_BUTTON_FIRST)
        first.click()

    def save(self):
        save = self.browser.find_element(*ProfilePageLocators.BUTTON_SAVE_1)
        save.click()

    def button_edit(self):
        edit = self.browser.find_element(*ProfilePageLocators.BUTTON_EDIT)
        edit.click()

    def input_phone(self):
        phone = self.browser.find_element(*ProfilePageLocators.INPUT_PHONE)
        phone.send_keys('9379992')

    def button_ok(self):
        ok = self.browser.find_element(*ProfilePageLocators.BUTTON_SAVE_2)
        ok.click()

