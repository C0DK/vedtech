from pathlib import Path

import typer
from rich import print

from vedtech import parse_document
from vedtech.default_templates import Template


app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def new(template: Template) -> str:
    # We need two commands, for typer to give me command names
    raise NotImplementedError()


@app.command()
def check(path: str, template: Template, verbose: bool = False) -> str:
    try:
        with Path.open(path, encoding="utf-8") as document_file:
            document = parse_document(document_file.read())
    except FileNotFoundError:
        fail(f"No such file or directory: '{path}'")
    except IsADirectoryError:
        fail(f"You cannot check an entire folder (yet)")

    if not template.matches(document):
        fail(f"Document '{path}' did not match template '{template.value}'!")

    print(f":tada: '{path}' matched template '{template.value}'! :tada:")


def fail(msg: str) -> None:
    print(f"[bold red]Fail:[/bold red] {msg}")
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
