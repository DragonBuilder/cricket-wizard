from typing import Optional
import typer
from cricket_wizard.agent import start
# from scrape import scrape_url, scrape_cricbuzz_archive
import scrape

# from .httpserver import app as httpserver_app

app = typer.Typer()

scrapejob_app = typer.Typer()
app.add_typer(scrapejob_app, name="scrape")

# httpserver_app = typer.Typer()
# app.add_typer()

@app.command()
def chat_mode():
    start()

@scrapejob_app.command()
def archive():
    scrape.scrape_cricbuzz_archive()

@scrapejob_app.command()
def match_info():
    scrape.scrape_match_info("https://www.cricbuzz.com/live-cricket-scores/91796/aus-vs-ind-3rd-test-india-tour-of-australia-2024-25")



# @app.command()
# def start_httpserver(port: Optional[str] = "9999"):
#     pass

if __name__ == "__main__":
    # typer.run(main)
    app()