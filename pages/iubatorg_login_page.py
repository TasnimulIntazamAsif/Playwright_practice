from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username_input=page.get_by_role("textbox", name="Student ID")
        self.password_input=page.get_by_role("textbox", name="Password")
        self.sign_in_button=page.get_by_role("button", name="Sign In")
    def enter_username(self, username:str):
        self.username_input.fill(username)

    def enter_password(self, password:str):
        self.password_input.fill(password)

    def click_sign_in(self):
        self.sign_in_button.click()

    


