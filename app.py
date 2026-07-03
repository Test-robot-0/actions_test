from playwright.sync_api import sync_playwright

print("Starting...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    url = "https://leetcode.com/problems/asteroid-collision/description/"
    page.goto(url)
    print("URL:", page.url)
    print("Title:", page.title())

    html = page.content()

    print(html[:500])
    
    page.wait_for_timeout(10000)

    print("URL:", page.url)
    print("Title:", page.title())

    html = page.content()

    print("Length:", len(html))

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    browser.close()

print("Done")
