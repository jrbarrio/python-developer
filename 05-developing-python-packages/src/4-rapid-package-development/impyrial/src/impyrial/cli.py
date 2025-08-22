"""Console script for impyrial."""

import typer
from rich.console import Console

from impyrial import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for impyrial."""
    console.print("Replace this message by putting your code into "
               "impyrial.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
