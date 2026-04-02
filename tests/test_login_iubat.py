import re
from playwright.sync_api import Page, expect
from pages.iubatorg_login_page import LoginPage
from pages.iubatorg_home_page import HomePage

def test_example(page: Page) -> None:
    page.goto("https://iubat.online/")
    page.get_by_role("link", name="Final Course Enrollment").click()
    page.get_by_role("textbox", name="Student ID").dblclick()
    page.get_by_role("textbox", name="Student ID").fill("22203139")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("2Kz2PAWs#")
    page.get_by_role("button", name="Sign-In").click()
    page.get_by_role("link", name="View Details").first.dblclick()
    expect(page.get_by_role("heading", name="STUDENT ENROLLMENT")).to_be_visible()

