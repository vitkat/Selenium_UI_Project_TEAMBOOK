import time
import pytest
from pages.planning_page import Planning_Page
from utilits.login import login
from pages.settings import url_planning_page


@pytest.mark.skip
def test_add_user(browser):
    """A test that creates a new user"""
    login(browser)
    time.sleep(5)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.go_add_user()
    page.go_create_user()
    page.go_first_name()
    page.go_last_name()
    page.go_user_role()
    page.go_planner()
    page.go_button_submit()
    page.go_button_save()
    time.sleep(2)


@pytest.mark.smoke
def test_calendar(browser):
    """The test of pressing the calendar arrow "back" and after pressing the "today" button"""
    login(browser)
    time.sleep(4)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.click_calendar_left()
    time.sleep(1)
    page.click_calendar_right()
    time.sleep(1)
    page.button_today()
    time.sleep(1)


@pytest.mark.skip
def test_team_button(browser):
    """A test that creates a new command and then deletes it"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.team_button()
    page.new_team()
    page.input_team_name()
    page.button_ok()
    page.button_delete_team()
    time.sleep(1)
    page.input_delete()
    time.sleep(1)
    page.button_submit()


@pytest.mark.regression
def test_change_name_team(browser):
    """Changing the team name"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.change_name_team()
    page.button_change()
    page.input_name_team()
    page.button_save_name()
    time.sleep(2)


@pytest.mark.regression
def test_button_info(browser):
    """Checking the functionality of the "information" button and navigating through all the proposed sections"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.button_info()
    page.know_base()
    time.sleep(2)
    page.open()
    page.button_info()
    page.cont_us()
    time.sleep(2)
    page.open()
    page.button_info()
    page.suggest_feature()
    time.sleep(2)
    page.open()
    page.button_info()
    page.product_road_map()
    time.sleep(2)
    page.open()
    page.button_info()
    page.reopen()
    time.sleep(2)
    page.open()
    page.button_info()
    page.reopen_know()
    time.sleep(2)


@pytest.mark.smoke
def test_setting(browser):
    """A test that checks filters in the settings"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.setting()
    page.button_mounth()
    time.sleep(2)
    page.open()
    page.setting()
    page.button_days()
    time.sleep(2)
    page.open()
    page.setting()
    page.button_week()
    time.sleep(2)


@pytest.mark.skip
def test_button_download(browser):
    """Test downloading file"""
    login(browser)
    time.sleep(3)
    link = url_planning_page
    page = Planning_Page(browser, link)
    page.open()
    page.button_download()
    time.sleep(2)
    page.button_print_pdf()
    time.sleep(2)