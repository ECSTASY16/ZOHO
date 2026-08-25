import time

from pages.AllAppsPage import AllAppsPage
from pages.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self,page):
        super(). __init__(page)

    def wait_for_page_to_load(self):
        self.wait_for_load_state('networkidle')

        # return self.page.url
        return AllAppsPage(self.page)
    # def click_user_profile(self):
    #     # Wait until the page reaches the home URL
    #     self.wait_for_load_state('networkidle')
    #
    #     # Then click the element
    #     self.click('userProfile')
    #     return self
    #
    #
    # def click_sign_out(self):
    #     self.click_by_text('signOut_btn')
    #     return self




