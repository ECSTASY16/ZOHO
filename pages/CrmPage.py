from pages.BasePage import BasePage


class CRMPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_create(self):
        self.click("create_btn")
        return self

    def select_account_option(self):
        self.wait_for_load_state("networkidle")
        self.click_by_text("Account_optn")
        return self

    #
    # def enter_account_name(self, acnt_name):
    #     self.type('Account_name_input_field', acnt_name)
    #     return self
    #
    # def enter_phone(self, phone):
    #     self.type('Phone_input_field', str(phone))
    #     return self
    #
    # def select_rating(self, rating):
    #     """Opens the rating dropdown and selects the given rating value in
    #     one action, since these two steps are never meaningfully used
    #     independently."""
    #     self.click('rating_dropdown')
    #     self.click_by_text(rating)
    #     return self
    #
    # def enter_street_address(self, street_name):
    #     self.type('street_add_input_field', street_name)
    #     return self
    #
    # def enter_city(self, city):
    #     self.type('city_input_field', city)
    #     return self
    #
    # def enter_state(self, state):
    #     self.type('State_input_field', state)
    #     return self
    #
    # def enter_code(self, code):
    #     self.type('code_input_field', str(code))
    #     return self
    #
    # def enter_country(self, country_name):
    #     self.type('country_input_field', country_name)
    #     return self
    #
    # def enter_description(self, description):
    #     self.type('description_input_field', description)
    #     return self
    #
    # def click_save(self):
    #     self.click('Save_btn')
    #     return self
    #
    # def crm_flow(self, acnt_name, phone, street_name, city, state, code, country_name, rating, description=""):
    #     return (
    #         self.click_create()
    #         .select_account_option()
    #         .enter_account_name(acnt_name)
    #         .enter_phone(phone)
    #         .select_rating(rating)
    #         .enter_street_address(street_name)
    #         .enter_city(city)
    #         .enter_state(state)
    #         .enter_code(code)
    #         .enter_country(country_name)
    #         .enter_description(description)
    #         .click_save()
    #     )
