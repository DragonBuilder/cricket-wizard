import typer
from cricket_wizard.agent import start
from scrape import scrape_url, scrape_cricbuzz_archive

app = typer.Typer()

scrapejob_app = typer.Typer()
app.add_typer(scrapejob_app, name="scrape")

@app.command()
def chat_mode():
    start()

@scrapejob_app.command()
def archive():
    scrape_cricbuzz_archive()


    
    # sync_playwright()

# def main():
#     # start()
#     sync_playwright()


if __name__ == "__main__":
    # typer.run(main)
    app()