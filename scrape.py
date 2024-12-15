## to be used to scrape data off the internet which will be used to update internal db

import os
from urllib.parse import urlparse
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
        browser.close()

def scrape_match_info(url: str):
    url_segments = urlparse(url)
    match_slug = os.path.split(url_segments.path)[-1]

    print(f"Match slug: {match_slug}")

    sections = ['Commentary', 'Scorecard', 'Squads', 'Highlights']
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)        

        navigable_sections = page.locator("a.cb-nav-tab").all()
        for idx, section in enumerate(sections):
            nav_bar = navigable_sections[idx]
            nav_bar_title = nav_bar.inner_text()
            if (nav_bar_title != section):
                raise Exception(f"expected the nav bar title to be {section} but was {nav_bar_title}")
            
            nav_bar.click()
            save(f"{match_slug}/{section}.html", page.content())
            



def save(filepath: str, content: str):
    rootdir, filename = os.path.split(filepath)
    rootdir = os.path.join("out", rootdir)
    os.makedirs(rootdir, exist_ok=True)

    finalpath = os.path.join(rootdir, filename)

    with open(finalpath, 'w') as f:
        f.write(content)

