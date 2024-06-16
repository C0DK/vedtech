from pathlib import Path
from typing import Annotated

import typer
from rich import print

from vedtech import parse_document
from vedtech.default_templates import Template

app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def new() -> str:
    # We need two commands, for typer to give me command names
    raise NotImplementedError


@app.command()
def check(
    document_file: Annotated[
        Path,
        typer.Argument(
            exists=True,
            dir_okay=False,
            file_okay=True,
            readable=True,
            resolve_path=True,
            allow_dash=True,
        ),
    ],
    template: Template,
) -> str:
    document = parse_document(document_file.read_text())

    if not template.matches(document):
        fail(f"Document '{document_file}' did not match template '{template.value}'!")

    print(f":tada: '{document_file}' matched template '{template.value}'! :tada:")


def fail(msg: str) -> None:
    print(f"[bold red]Fail:[/bold red] {msg}")
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
