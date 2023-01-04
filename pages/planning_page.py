from .base_page import BasePage
from .locators import PlanningPageLocators


class Planning_Page(BasePage):
    def go_add_user(self):
        add_user = self.browser.find_element(*PlanningPageLocators.ADD_USER)
        add_user.click()

    def go_create_user(self):
        create_user = self.browser.find_element(*PlanningPageLocators.CREATE_USER)
        create_user.click()

    def go_first_name(self):
        first_name = self.browser.find_element(*PlanningPageLocators.FIRST_NAME)
        first_name.send_keys('Valdemar')

    def go_last_name(self):
        last_name = self.browser.find_element(*PlanningPageLocators.LAST_NAME)
        last_name.send_keys('Kubis')

    def go_user_role(self):
        user_role = self.browser.find_element(*PlanningPageLocators.USER_ROLE)
        user_role.click()

    def go_planner(self):
        planner = self.browser.find_element(*PlanningPageLocators.PLANNER)
        planner.click()

    def go_button_submit(self):
        button_submit = self.browser.find_element(*PlanningPageLocators.BUTTON_SUBMIT)
        button_submit.click()

    def go_button_save(self):
        button_save = self.browser.find_element(*PlanningPageLocators.BUTTON_SAVE)
        button_save.click()

    def click_calendar_left(self):
        click_calendar_right = self.browser.find_element(*PlanningPageLocators.CLICK_LEFT)
        click_calendar_right.click()

    def click_calendar_right(self):
        click_calendar_right = self.browser.find_element(*PlanningPageLocators.CLICK_RIGHT)
        click_calendar_right.click()

    def button_today(self):
        button_today = self.browser.find_element(*PlanningPageLocators.BUTTON_TODAY)
        button_today.click()

    def team_button(self):
        team_button = self.browser.find_element(*PlanningPageLocators.TEAM_BUTTON)
        team_button.click()

    def new_team(self):
        new_team = self.browser.find_element(*PlanningPageLocators.NEW_TEAM)
        new_team.click()

    def input_team_name(self):
        input_team_name = self.browser.find_element(*PlanningPageLocators.INPUT_TEAM_NAME)
        input_team_name.send_keys('secondStars')

    def button_ok(self):
        button_ok = self.browser.find_element(*PlanningPageLocators.BUTTON_OK)
        button_ok.click()

    def button_delete_team(self):
        button_delete_team = self.browser.find_element(*PlanningPageLocators.BUTTOM_DELETE_TEAM)
        button_delete_team.click()

    def input_delete(self):
        input_delete = self.browser.find_element(*PlanningPageLocators.INPUT_DELETE)
        input_delete.send_keys('secondStars')

    def button_submit(self):
        button_submit = self.browser.find_element(*PlanningPageLocators.BUTTON_SUBMIT_Q)
        button_submit.click()

    def change_name_team(self):
        change_name_team = self.browser.find_element(*PlanningPageLocators.TEAM_BUTTON)
        change_name_team.click()

    def button_change(self):
        button_change = self.browser.find_element(*PlanningPageLocators.BUTTON_CREATE)
        button_change.click()

    def input_name_team(self):
        input_name = self.browser.find_element(*PlanningPageLocators.INPUT_NAME)
        input_name.send_keys('Best')

    def button_save_name(self):
        button_save = self.browser.find_element(*PlanningPageLocators.BUTTON_SAVE_NAME)
        button_save.click()

    def button_info(self):
        info = self.browser.find_element(*PlanningPageLocators.BUTTON_INFO)
        info.click()

    def know_base(self):
        know_base = self.browser.find_element(*PlanningPageLocators.KNOWLEDGE_BASE)
        know_base.click()

    def cont_us(self):
        cont_us = self.browser.find_element(*PlanningPageLocators.CONTACT_US)
        cont_us.click()

    def suggest_feature(self):
        sug_feature = self.browser.find_element(*PlanningPageLocators.SUGGEST_FEATURE)
        sug_feature.click()

    def product_road_map(self):
        prod = self.browser.find_element(*PlanningPageLocators.PRODUCT_MAP)
        prod.click()

    def reopen(self):
        reopen = self.browser.find_element(*PlanningPageLocators.REOPEN)
        reopen.click()

    def reopen_know(self):
        reopen_k = self.browser.find_element(*PlanningPageLocators.REAPEN_KNOW)
        reopen_k.click()

    def setting(self):
        set = self.browser.find_element(*PlanningPageLocators.BUTTON_SETTING)
        set.click()

    def button_mounth(self):
        mounth = self.browser.find_element(*PlanningPageLocators.BUTTON_MOUNTH)
        mounth.click()

    def button_days(self):
        days = self.browser.find_element(*PlanningPageLocators.BUTTON_DAYS)
        days.click()

    def button_week(self):
        week = self.browser.find_element(*PlanningPageLocators.BUTTON_WEEK)
        week.click()

    def button_download(self):
        download = self.browser.find_element(*PlanningPageLocators.BUTTON_DOWNLOAD)
        download.click()

    def button_print_pdf(self):
        print_pdf = self.browser.find_element(*PlanningPageLocators.BUTTON_PRINT_PDF)
        print_pdf.click()
