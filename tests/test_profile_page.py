import time
import pytest
from pages.profile_page import Profile_Page
from utilits.login import login
from pages.settings import url_profile_page


@pytest.mark.regression
def test_profile_page(browser):
    """A test that performs a click on a profile page"""
    login(browser)
    time.sleep(3 )
    link = url_profile_page
    page = Profile_Page(browser, link)
    page.open()
    page.go_edit()
    page.go_first_name()
    time.sleep(2)


@pytest.mark.skip
def test_email_pass(browser):
    """The test that logs in to the "profile" section"""
    login(browser)
    time.sleep(3)
    link = url_profile_page
    page = Profile_Page(browser, link)
    page.open()
    page.click_email_pass()
    page.input_old_pass()
    page.input_new_pass()
    page.input_confirm_pass()
    page.button_update()
    time.sleep(2)


@pytest.mark.regression
def test_shedule(browser):
    """A test that logs into a section and adds data"""
    login(browser)
    time.sleep(3)
    link = url_profile_page
    page = Profile_Page(browser, link)
    page.open()
    page.button_shedule()
    page.input_fri()
    page.button_save()
    time.sleep(2)


@pytest.mark.regression
@pytest.mark.smoke
def test_shedule(browser):
    """The test entering the notification section passes through the radio buttons and saves the result"""
    login(browser)
    time.sleep(3)
    link = url_profile_page
    page = Profile_Page(browser, link)
    page.open()
    page.button_notification()
    page.radio_button()
    time.sleep(1)
    page.radio_button_second()
    time.sleep(1)
    page.radio_button_first()
    time.sleep(1)
    page.button_save()


@pytest.mark.skip
def test_shedule(browser):
    """A test that modifies and adds personal data"""
    login(browser)
    time.sleep(3)
    link = url_profile_page
    page = Profile_Page(browser, link)
    page.open()
    page.button_edit()
    page.input_phone()
    page.button_ok()
    time.sleep(2)