## to be used to scrape data off the internet which will be used to update internal db

import os
from playwright.sync_api import sync_playwright

def scrape_cricbuzz_archive():
    scrape_url("cricbuzz-archive", "https://www.cricbuzz.com/cricket-scorecard-archives")

def scrape_url(name: str, url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        save(f"{name}.html", page.content())
        
        # page.content()
        browser.close()

def save(filename: str, content: str):
    os.makedirs("out/", exist_ok=True)
    with open(f"out/{filename}", 'w') as f:
        f.write(content)

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()

