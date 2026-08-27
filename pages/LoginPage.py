
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_login_link(self):

        self.click_by_role("link", locator="SignIn")
        # return self

    def get_email_field(self):
        return self.get_locator("check_email_field", timeout=30)

    def enter_email(self, email):
        self.type("enteremail", email)
        return self

    def click_next(self):
        self.click("clickNext_btn")
        return self

    def enter_password(self, password):
        self.type("enterpassword", password)
        return self

    def click_signIn_btn(self):
        self.click("signin_btn")

        return self

    def do_logout(self):

        self.verify_element_visible("userProfile", timeout=15000)
        self.click("userProfile")
        self.verify_element_visible("signOut_btn", timeout=5000)
        self.click("signOut_btn")
        return self

    def get_error_message(self):
        self.page.wait_for_timeout(1000)
        if self.is_visible("invalid_email", timeout=3000):
            return self.get_text("invalid_email")
        if self.is_visible("invalid_pwd_error", timeout=3000):
            return self.get_text("invalid_pwd_error")
        return None
