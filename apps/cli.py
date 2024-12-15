from typing import Optional
import typer
from cricket_wizard.agent import start
from scrape import scrape_url, scrape_cricbuzz_archive

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
    scrape_cricbuzz_archive()

# @app.command()
# def start_httpserver(port: Optional[str] = "9999"):
#     pass

if __name__ == "__main__":
    # typer.run(main)
    app()