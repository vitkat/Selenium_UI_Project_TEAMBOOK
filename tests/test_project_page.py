import pytest
import time
from utilits.login import login
from pages.project_page import Project_Page
from pages.settings import url_project_page


@pytest.mark.regression
def test_create_project(browser):
    """A test that creates a new project"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.button_create_project()
    page.input_name()
    page.input_short_name()
    page.input_bis_unit()
    page.button_save()
    time.sleep(2)


@pytest.mark.skip
def test_edit_project(browser):
    """Test editing project"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.project_bis()
    page.button_edit()
    page.input_hours()
    page.click_save()
    time.sleep(2)


@pytest.mark.regression
def test_search(browser):
    """A test that checks the search input form as well as the correct operation of the check-box"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.input_search()
    page.check_box()
    time.sleep(2)
    page.check_box_off()
    time.sleep(2)


@pytest.mark.regression
def test_create_project(browser):
    """Test delete project"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.project_bis()
    page.delete_project()
    page.ok_delete()
    time.sleep(2)


@pytest.mark.smoke
def test_button_manage(browser):
    """A test that creates a new client"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.button_manage()
    page.add_client()
    page.input_client_name()
    page.input_email()
    page.save_client()
    time.sleep(2)


@pytest.mark.regression
@pytest.mark.smoke
def test_button_manage(browser):
    """A test that edits the data of an existing client"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.button_manage()
    page.edit_client()
    page.number_client()
    page.save_edit()
    time.sleep(2)


@pytest.mark.smoke
def test_button_manage(browser):
    """The test that removes the client"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.button_manage()
    page.delete_client()
    page.delete_ok()
    time.sleep(2)


@pytest.mark.smoke
def test_upload_project(browser):
    """A test verifying the correctness of the "upload" button"""
    login(browser)
    time.sleep(3)
    link = url_project_page
    page = Project_Page(browser, link)
    page.open()
    page.button_upload_project()
    page.input_com()
    page.upload_cancel()
    time.sleep(2)