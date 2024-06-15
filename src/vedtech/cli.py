from pathlib import Path

import typer
from rich import print

from vedtech import parse_document
from vedtech.default_templates import Template


class DocumentDidNotMatchTemplate(typer.Exit):
    def __init__(self, path: str, template_name: str) -> None:
        # TODO: dont do it like this.
        print(f"[bold red]document '{path}' did not match template '{template_name}'![/bold red]")
        super().__init__(code=1)


app = typer.Typer()


@app.command()
def new(template: Template) -> str:
    # We need two commands, for typer to give me command names
    raise NotImplementedError()


@app.command()
def check(path: str, template: Template) -> str:
    with Path.open(path, encoding="utf-8") as document_file:
        document = parse_document(document_file.read())

    if not template.matches(document):
        raise DocumentDidNotMatchTemplate(path, template.name)

    return f"{path} matched template '{template.name}'!"


if __name__ == "__main__":
    app()
