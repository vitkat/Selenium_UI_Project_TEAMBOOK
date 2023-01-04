from .base_page import BasePage
from .locators import ProjectPageLocators


class Project_Page(BasePage):
    def button_create_project(self):
        button = self.browser.find_element(*ProjectPageLocators.BUTTON_CREATE_PROJ)
        button.click()

    def input_name(self):
        name = self.browser.find_element(*ProjectPageLocators.INPUT_NAME)
        name.send_keys('Bistriy')

    def input_short_name(self):
        name = self.browser.find_element(*ProjectPageLocators.INPUT_SHOT_NAME)
        name.send_keys('Bis')

    def input_bis_unit(self):
        unit = self.browser.find_element(*ProjectPageLocators.BIS_UNIT)
        unit.send_keys('Fall')

    def input_discrible(self):
        ds = self.browser.find_element(*ProjectPageLocators.DISCRIBLE)
        ds.send_keys('that is cool!!!')

    def button_save(self):
        save = self.browser.find_element(*ProjectPageLocators.BUTTON_SAVE)
        save.click()

    def project_bis(self):
        bis = self.browser.find_element(*ProjectPageLocators.PROJECT_BIS)
        bis.click()

    def button_edit(self):
        edit = self.browser.find_element(*ProjectPageLocators.EDIT_PROJET)
        edit.click()

    def input_hours(self):
        hours = self.browser.find_element(*ProjectPageLocators.INPUT_HOURS)
        hours.send_keys('3')

    def click_save(self):
        save = self.browser.find_element(*ProjectPageLocators.BUT_SAVE)
        save.click()

    def input_search(self):
        search = self.browser.find_element(*ProjectPageLocators.SEARCH)
        search.send_keys('Bis')

    def check_box(self):
        box = self.browser.find_element(*ProjectPageLocators.CHECKBOX)
        box.click()

    def check_box_off(self):
        off = self.browser.find_element(*ProjectPageLocators.CHECK_BOX_OFF)
        off.click()

    def delete_project(self):
        delete = self.browser.find_element(*ProjectPageLocators.BUTTON_DELETE)
        delete.click()

    def ok_delete(self):
        delete = self.browser.find_element(*ProjectPageLocators.DEL_PROJECT)
        delete.click()

    def button_manage(self):
        manage = self.browser.find_element(*ProjectPageLocators.MANAGE_CLIENTS)
        manage.click()

    def add_client(self):
        add = self.browser.find_element(*ProjectPageLocators.ADD)
        add.click()

    def input_client_name(self):
        name = self.browser.find_element(*ProjectPageLocators.INPUT_NAME_CLIENT)
        name.send_keys('John')

    def input_email(self):
        email = self.browser.find_element(*ProjectPageLocators.EMAIL_CLIENT)
        email.send_keys('JohnyJohnyYes@mail.ru')

    def save_client(self):
        save = self.browser.find_element(*ProjectPageLocators.CLICK_OK_CLIENT)
        save.click()

    def edit_client(self):
        edit = self.browser.find_element(*ProjectPageLocators.EDIT_CLIENT)
        edit.click()

    def number_client(self):
        client = self.browser.find_element(*ProjectPageLocators.INPUT_PHONE_CLIENT)
        client.send_keys('4554344')

    def save_edit(self):
        save = self.browser.find_element(*ProjectPageLocators.EDIT_SAVE)
        save.click()

    def delete_client(self):
        client = self.browser.find_element(*ProjectPageLocators.DEL_CLIENT)
        client.click()

    def delete_ok(self):
        ok = self.browser.find_element(*ProjectPageLocators.DELETE_OK_CLIEN)
        ok.click()

    def button_upload_project(self):
        upload = self.browser.find_element(*ProjectPageLocators.UPLOAD_PROJECT)
        upload.click()

    def input_com(self):
        com = self.browser.find_element(*ProjectPageLocators.INPUT_COMMENT)
        com.send_keys('Абра-Кадабра')

    def upload_cancel(self):
        cancel = self.browser.find_element(*ProjectPageLocators.CANCEL_UPLOAD)
        cancel.click()