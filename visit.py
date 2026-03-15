from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://section.iaesonline.com")
    page.locator("#login")
    #page.click("text=Sign in")
    #page.screenshot()
    browser.close()