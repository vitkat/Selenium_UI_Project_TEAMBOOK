import pytest
import time
from utilits.login import login
from pages.userrr_page import User_Page
from pages.settings import url_user_page


@pytest.mark.regression
def test_create_user(browser):
    """Creating a new user in the User section"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.button_create_user()
    page.input_first_name()
    page.input_last_name()
    page.input_email()
    page.user_role()
    page.input_phone()
    page.button_setting()
    page.button_create()
    time.sleep(2)


@pytest.mark.regression
def test_edit_user(browser):
    """A test that performs editing of user data"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.choose_user()
    page.edit_user()
    page.input_number()
    page.button_save()
    time.sleep(2)


@pytest.mark.skip
def test_delete_user(browser):
    """Test performing user deletion"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.delete_user()
    page.button_delete()
    page.button_deactivate()
    time.sleep(2)


@pytest.mark.smoke
def test_manage_tag(browser):
    """A test that creates a new tag and then deletes it"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.manage_tag()
    page.add_tag()
    page.input_name()
    page.button_ok()
    page.button_exit()
    page.manage_tag()
    page.delete_tag()
    page.del_tag()
    time.sleep(2)


@pytest.mark.regression
def test_upload_user(browser):
    """A test that opens the file download page and then closes it"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.upload_user()
    page.button_cancel()
    time.sleep(2)


@pytest.mark.smoke
def test_input_search(browser):
    """A test that searches for a user by name through the name input form and opens it"""
    login(browser)
    time.sleep(3)
    link = url_user_page
    page = User_Page(browser, link)
    page.open()
    page.input_search()
    page.user_vit()
    time.sleep(2)
