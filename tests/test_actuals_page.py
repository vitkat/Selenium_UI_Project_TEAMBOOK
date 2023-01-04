import pytest
import time
from pages.actuals_page import Actuals_Page
from pages.settings import url_actuals_page
from utilits.login import login


@pytest.mark.skip
def test_calendar(browser):
    """The test that goes into the current section and flipping through the calendar"""
    login(browser)
    time.sleep(3)
    link = url_actuals_page
    page = Actuals_Page(browser, link)
    page.open()
    page.open_actuals()
    time.sleep(2)
    page.button_next()
    page.click_calendar_left()
    time.sleep(1)
    page.click_calendar_right()


@pytest.mark.regression
def test_copy_plannner(browser):
    """A test that copies the plan according to the specified settings"""
    login(browser)
    time.sleep(3)
    link = url_actuals_page
    page = Actuals_Page(browser, link)
    page.open()
    page.checking_for_an_emerging_window()
    page.copy_planner()
    page.select_data()
    page.choose_number()
    page.choose_user()
    page.button_submit()


@pytest.mark.smoke
def test_button_download(browser):
    """Test downloading file and filtered by date"""
    login(browser)
    time.sleep(3)
    link = url_actuals_page
    page = Actuals_Page(browser, link)
    page.open()
    page.checking_for_an_emerging_window()
    page.button_download()
    page.start_data()
    page.data_2()
    page.finish_data()
    page.finish_number()
    time.sleep(2)
    page.click_but_sub()


@pytest.mark.smoke
def test_appruv_logs(browser):
    """A test that checks the functionality of the button"""
    login(browser)
    time.sleep(3)
    link = url_actuals_page
    page = Actuals_Page(browser, link)
    page.open()
    page.checking_for_an_emerging_window()
    page.button_appruv_logs()
    time.sleep(2)