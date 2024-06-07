from .document import Document, Section


def parse_document(markdown_content: str) -> Document:

    sections = []
    while markdown_content:
        next_section, markdown_content = extract_next_section(markdown_content)
        sections.append(next_section)
    return Document(sections)


def extract_next_section(content: str) -> tuple[Section, str]:

    content = content.lstrip()

    if not content:
        raise EmptyContentError

    if content[0] != "#":
        raise DidNotStartWithHeadingError

    size = 0
    while content[0] == "#":
        size += 1
        content = content[1:]
    lines = content.splitlines()

    title = lines.pop(0).strip()

    section_lines = []
    while lines and not lines[0].startswith("#"):
        section_lines.append(lines.pop(0))

    return Section(title=title, size=size, lines=section_lines), "\n".join(lines)


class EmptyContentError(ValueError): ...


class DidNotStartWithHeadingError(ValueError):
    def __init__(self, content: str) -> None:
        super().__init__(f"Section did not start with heading! {content=}")
