from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for background
        page = browser.new_page()

        page.goto("https://www.google.com")

        # 👉 Get and print title
        print("Page Title:", page.title())

        browser.close()

if __name__ == "__main__":
    run()