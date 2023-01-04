from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import ActualsPageLocators


class Actuals_Page(BasePage):
    def open_actuals(self):
        actual_link = self.browser.find_element(*ActualsPageLocators.ACT_LINK)
        actual_link.click()

    def button_next(self):
        next = self.browser.find_element(*ActualsPageLocators.BUTTON_NEXT)
        next.click()

    def click_calendar_left(self):
        click_left = self.browser.find_element(*ActualsPageLocators.CALENDAR_LEFT)
        click_left.click()

    def click_calendar_right(self):
        click_right = self.browser.find_element(*ActualsPageLocators.CALENDAR_RIGHT)
        click_right.click()

    def copy_planner(self):
        copy = self.browser.find_element(*ActualsPageLocators.BUT_COPY_PLANNER)
        copy.click()

    def select_data(self):
        data = self.browser.find_element(*ActualsPageLocators.SELECT_DATA)
        data.click()

    def choose_number(self):
        number = self.browser.find_element(*ActualsPageLocators.NUMBER)
        number.click()

    def choose_user(self):
        user = self.browser.find_element(*ActualsPageLocators.CHOOSER_USER)
        user.click()

    def button_submit(self):
        submit = self.browser.find_element(*ActualsPageLocators.BUTTON_SUB)
        submit.click()

    def checking_for_an_emerging_window(self):
        """Проверка и закрытие всплывающего окна на странице Actuals"""
        self.browser.maximize_window()
        try:
            self.browser.find_element(*ActualsPageLocators.POP_UP_WINDOW_BTN).click()
        except NoSuchElementException:
            print("There is no pop-up window")

    def button_download(self):
        download = self.browser.find_element(*ActualsPageLocators.BUTTON_DOWNLOAD)
        download.click()

    def start_data(self):
        start = self.browser.find_element(*ActualsPageLocators.START_DATA)
        start.click()

    def data_2(self):
        data = self.browser.find_element(*ActualsPageLocators.NUMBER_2)
        data.click()

    def finish_data(self):
        data = self.browser.find_element(*ActualsPageLocators.FINISH_DATA)
        data.click()

    def finish_number(self):
        data = self.browser.find_element(*ActualsPageLocators.FINISH_NUMBER)
        data.click()

    def click_but_sub(self):
        but = self.browser.find_element(*ActualsPageLocators.BUTTON_OK_SUB)
        but.click()

    def button_appruv_logs(self):
        logs = self.browser.find_element(*ActualsPageLocators.BUTTON_APPRUV_LOGS)
        logs.click()

