from playwright.sync_api import Page, expect
class HomePage:

    def __init__(self, Page):
        self.page =Page
        self.sign_in_button = Page.get_by_role("sign-in")

        def is_sign_in(self):
            return self.sign_in_button.is_sign_in()

        def click_sign_in(self):
            return self.sign_in_button.click_sign_in()

