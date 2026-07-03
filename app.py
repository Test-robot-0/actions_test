from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    url = "https://leetcode.com/problems/asteroid-collision/description/"

    page.goto(url, wait_until="domcontentloaded", timeout=60000)

    # Give Cloudflare some time if it's going to automatically verify.
    page.wait_for_timeout(30000)

    print("URL:", page.url)
    print("Title:", page.title())

    page.screenshot(path="page.png", full_page=True)

    html = page.content()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    browser.close()
