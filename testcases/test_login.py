import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from testcases.Basetest import BaseTest
from utilities import dataProvider


class Test_logintest(BaseTest):
#     @pytest.mark.parametrize('scenario,email,password,status', dataProvider.get_data('Sheet1'))
#     def test_login_scenarios(self, page,setup, scenario, email, password, status,login_page):
#         lp = LoginPage(page).click_login_link().enter_email(email).click_next()
#
#         error_after_email = lp.get_error_message()
#         if error_after_email:
#             assert error_after_email == status, f"Expected '{status}' but got '{error_after_email}'"
#             return
#
#         lp.enter_password(password).click_signIn_btn()
#
#         if status.strip().lower() == "success":
#             lp.verify_url_contains("home")
#             lp.do_logout()
#         else:
#             error_after_password = lp.get_error_message()
#             assert error_after_password == status, f"Expected '{status}' but got '{error_after_password}'"



    def test_check_login_link(self,page,login_page):
        login_page.click_login_link()


    def test_enter_email(self,page,login_page):
        email_field=login_page.get_email_field()
        expect(email_field).to_be_visible()
        expect(email_field).to_be_enabled()
        expect(email_field).to_be_editable()
        expect(email_field).to_be_empty()

    @pytest.mark.parametrize('email',['pranayrahate680@gmail.com'])
    def test_email_field(self,page,login_page,email):
        login_page.enter_email(email)

#     def test_signin_link_visible(self, page):
#         lp = LoginPage(page)
#         expect(lp.page.get_by_role('link', name='Sign In', exact=True)).to_be_visible()
#
#     def test_click_signin_link(self, page):
#         """Clicking SignIn should reveal the email input field."""
#         lp = LoginPage(page).click_login_link()
#         lp.verify_element_visible('enteremail')
#
#     @pytest.mark.parametrize('email,password', dataProvider.get_data('Sheet1'))
#     def test_next_button_enabled_after_email(self, page, email, password):
#         """Next button should be enabled once a valid email is entered."""
#         lp = LoginPage(page).click_login_link().enter_email(email).click_next()
#         assert lp.is_enabled('clickNext_btn'), "Next button is not enabled after entering email"
#
#     @pytest.mark.parametrize('email,password', dataProvider.get_data('Sheet1'))
#     def test_click_next_shows_password_field(self, page, email, password):
#         """Clicking Next should reveal the password input field."""
#         lp = LoginPage(page).click_login_link().enter_email(email).click_next()
#         lp.verify_element_visible('enterpassword')
#
#     @pytest.mark.parametrize('email,password', dataProvider.get_data('Sheet1'))
#     def test_login_success_url_contains_home(self, page, email, password):
#         """Full login flow should succeed and land on the home page."""
#         lp = (
#             LoginPage(page)
#             .click_login_link()
#             .enter_email(email)
#             .click_next()
#             .enter_password(password)
#             .click_signIn_btn()
#         )
#         lp.verify_url_contains("home")

