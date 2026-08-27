
from pages.AllAppsPage import AllAppsPage
from testcases.Basetest import BaseTest


class Test_crmtest(BaseTest):
    #
    # @pytest.mark.parametrize(
    #     'acnt_name,phone,street_name,city,state,code,country_name,desc',
    #     dataProvider.get_data('Sheet2')
    # )
    def test_crm_account_creation_flow(self, authenticated_page):
        """Full CRM account creation journey, with checks at each step."""
        ap = AllAppsPage(authenticated_page)
        crm = ap.goto_crm()

    def test_select_account(self, authenticated_page):
        ap = AllAppsPage(authenticated_page)
        crm = ap.goto_crm()  # rebuild from scratch
        crm.click_create()

        # crm.verify_element_visible('create_btn', timeout=20000)
        #
        # crm.click_create()
        # crm.select_account_option()
        # crm.verify_element_visible('street_add_input_field', timeout=20000)
        #
        # crm.enter_account_name(acnt_name)
        # crm.verify_element_visible('Account_name_input_field')
        #
        # crm.enter_phone(phone)
        # crm.verify_element_visible('Phone_input_field')
        #
        # crm.enter_street_address(street_name)
        # crm.enter_city(city)
        # crm.enter_state(state)
        # crm.verify_element_visible('State_input_field')
        #
        # crm.enter_code(code)
        # crm.enter_country(country_name)
        #
        # crm.enter_description(desc)
        #
        # crm.click_save()
