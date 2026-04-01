import re
from playwright.sync_api import Page, expect
# playwright codegen to record started

def test_example(page: Page) -> None:
    page.goto("https://iubat.online/")
    page.get_by_role("link", name="Visit Student Services").click()
    page.get_by_role("textbox", name="Student ID#").click()
    page.get_by_role("textbox", name="Student ID#").fill("22203139")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("2Kz2PAWs#")
    page.get_by_role("button", name="Sign-In").click()
    page.get_by_role("link", name="Photo Student").click()
    page.get_by_role("link", name="Sign out").click()
    expect(page.get_by_role("link", name="IUBAT Admission")).to_be_visible()
    expect(page.locator("body")).to_contain_text("Student Portal")
