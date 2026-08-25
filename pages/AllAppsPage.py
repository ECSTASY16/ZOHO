from pages.CrmPage import CRMPage
from pages.BasePage import BasePage



class AllAppsPage(BasePage):
    def __init__(self,page):
        super(). __init__(page)


    def goto_calendar(self):
        pass
        return self

    def goto_cliq(self):
        pass
        return self

    def goto_crm(self):

        self.verify_element_visible('CRM_link', timeout=15000)
        self.click('CRM_link')
        return CRMPage(self.page)

    def goto_desk(self):
        pass

        return self

    def goto_mail(self):
        pass

    def goto_meeting(self):
        pass

    def goto_pdf_editor(self):
        pass
        return self
    def goto_people(self):
        pass
        return self
    def goto_projects(self):
        pass
        return self
    def goto_sheet(self):
        pass

    def goto_show(self):
        pass

    def goto_sign(self):
        pass

    def goto_workdrive(self):
        pass

    def goto_writer(self):
        pass