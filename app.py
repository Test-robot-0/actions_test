from playwright.sync_api import sync_playwright
import time

URL = "https://leetcode.com/problems/asteroid-collision/description/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="domcontentloaded", timeout=120000)

    timeout = 120  # seconds
    start = time.time()

    while time.time() - start < timeout:
        title = page.title()
        html = page.content()

        print(title)

        if (
            "Just a moment" not in title
            and "security verification" not in html.lower()
        ):
            print("Real page loaded!")
            break

        page.wait_for_timeout(2000)

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page.content())

    page.screenshot(path="page.png", full_page=True)

    browser.close()
