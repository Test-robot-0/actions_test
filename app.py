from playwright.sync_api import sync_playwright

URL = "https://leetcode.com/problems/asteroid-collision/description/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("Opening page...")
    page.goto(URL, wait_until="domcontentloaded", timeout=120000)

    print("Waiting 60 seconds...")
    page.wait_for_timeout(60000)   # Wait for 60 seconds

    print("Current URL:", page.url)
    print("Title:", page.title())

    html = page.content()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    page.screenshot(path="page.png", full_page=True)

    browser.close()

print("Done.")
