from .base_page import BasePage
from .locators import UserPageLocators


class User_Page(BasePage):
    def button_create_user(self):
        create = self.browser.find_element(*UserPageLocators.BUT_CREATE_USER)
        create.click()

    def input_first_name(self):
        first = self.browser.find_element(*UserPageLocators.INPUT_FIRST)
        first.send_keys('Bob')

    def input_last_name(self):
        last = self.browser.find_element(*UserPageLocators.INPUT_LAST)
        last.send_keys('Small')

    def input_email(self):
        mail = self.browser.find_element(*UserPageLocators.INPUT_EMAIL)
        mail.send_keys('Bobby@mail.ru')

    def user_role(self):
        role = self.browser.find_element(*UserPageLocators.USER_ROLE)
        role.click()

    def input_phone(self):
        phone = self.browser.find_element(*UserPageLocators.INPUT_PHONE)
        phone.send_keys('9379992')

    def button_setting(self):
        setting = self.browser.find_element(*UserPageLocators.BUTTON_SETTING)
        setting.click()

    def button_create(self):
        but = self.browser.find_element(*UserPageLocators.BUTTON_CREATE)
        but.click()

    def choose_user(self):
        choose = self.browser.find_element(*UserPageLocators.CHOOSE_USER)
        choose.click()

    def edit_user(self):
        edit = self.browser.find_element(*UserPageLocators.BUTTON_EDIT_USER)
        edit.click()

    def input_number(self):
        number = self.browser.find_element(*UserPageLocators.INPUT_NUMBER)
        number.send_keys('9379992')

    def button_save(self):
        save = self.browser.find_element(*UserPageLocators.BUTTON_SAVE)
        save.click()

    def delete_user(self):
        delete = self.browser.find_element(*UserPageLocators.CHOOSE_USER)
        delete.cclick()

    def button_delete(self):
        delete = self.browser.find_element(*UserPageLocators.BUTTON_DELETE)
        delete.click()

    def button_deactivate(self):
        deactivate = self.browser.find_element(*UserPageLocators.BUTTON_DEACTIVATE)
        deactivate.click()

    def manage_tag(self):
        manage = self.browser.find_element(*UserPageLocators.BUTTON_MANAGE_TAG)
        manage.click()

    def add_tag(self):
        add = self.browser.find_element(*UserPageLocators.ADD_TAG)
        add.click()

    def input_name(self):
        name = self.browser.find_element(*UserPageLocators.INPUT_NAME)
        name.send_keys('HollyWood')

    def button_ok(self):
        ok = self.browser.find_element(*UserPageLocators.BUTTON_OK)
        ok.click()

    def button_exit(self):
        exit = self.browser.find_element(*UserPageLocators.BUTTON_EXIT)
        exit.click()

    def delete_tag(self):
        tag = self.browser.find_element(*UserPageLocators.DELETE_TAG)
        tag.click()

    def del_tag(self):
        tag = self.browser.find_element(*UserPageLocators.BUTTON_DEL_TAG)
        tag.click()

    def upload_user(self):
        user = self.browser.find_element(*UserPageLocators.UPLOAD_USER)
        user.click()

    def button_cancel(self):
        cancel = self.browser.find_element(*UserPageLocators.BUTTON_CANCEL)
        cancel.click()

    def input_search(self):
        search = self.browser.find_element(*UserPageLocators.INPUT_SEARCH)
        search.send_keys('vit')

    def user_vit(self):
        vit = self.browser.find_element(*UserPageLocators.USER_VIT)
        vit.click()