from pathlib import Path

import fire

from vedtech import parse_document
from vedtech.default_templates import Template


class PathWasDirectoryExit(SystemExit):
    def __init__(self, path: str) -> None:
        super().__init__(f"{path} is a directory - a file is needed!")


class DocumentDidNotMatchTemplate(SystemExit):
    def __init__(self, path: str, template_name: str) -> None:
        super().__init__(f"document '{path}' did not match template '{template_name}'!")


class CommandHandler:
    """A tool for validating RFCs/ADRs and other markdown structured documents"""

    def check(self, path: str, template: Template | str) -> str:
        if isinstance(template, str):
            template = Template[template]

        try:
            with Path.open(path, encoding="utf-8") as document_file:
                document = parse_document(document_file.read())
        except IsADirectoryError as err:
            raise PathWasDirectoryExit(path) from err

        if not template.matches(document):
            raise DocumentDidNotMatchTemplate(path, template.name)

        return f"{path} matched template '{template.name}'!"


if __name__ == "__main__":
    fire.Fire(CommandHandler)
