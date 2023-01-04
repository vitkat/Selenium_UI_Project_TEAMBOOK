import time
import pytest
from pages.registration_page import Registration_Page
from pages.settings import url_registration_page


@pytest.mark.regression
def test_registration_page(browser):
    """Test performing new user accaunt"""
    link = url_registration_page
    page = Registration_Page(browser, link)
    page.open()
    page.go_first_name()
    page.go_last_name()
    page.go_email()
    page.go_company_name()
    page.go_password()
    page.go_check_box()
    page.go_button_create()
    time.sleep(2)
