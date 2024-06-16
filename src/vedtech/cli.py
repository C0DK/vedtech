import os
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
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            readable=True,
            resolve_path=True,
            allow_dash=True,
        ),
    ],
    template: Template,
) -> str:
    if path.is_dir():
        # in python 3.12 we should use path.walk
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    # this fails-fast - we probably should let it do more files
                    verify(Path(root) / file, template)
    else:
        verify(path, template)


def verify(document_file: Path, template: Template) -> None:

    document = parse_document(document_file.read_text())

    if not template.matches(document):
        fail(f"Document '{document_file}' did not match template '{template.value}'!")

    print(f":tada: '{document_file}' matched template '{template.value}'! :tada:")


def fail(msg: str) -> None:
    print(f"[bold red]Fail:[/bold red] {msg}")
    raise typer.Exit(1)


if __name__ == "__main__":
    app()
