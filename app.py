from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://leetcode.com/problems/asteroid-collision/description/",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(5000)

    html = page.content()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    browser.close()
