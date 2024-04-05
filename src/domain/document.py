from dataclasses import dataclass


@dataclass
class Section:
    title: str
    size: int
    lines: list[str]


@dataclass
class Document:
    sections: list[Section]


@dataclass
class SectionTemplate:
    title: str
    size: int

    def matches(self, section: Section) -> bool:
        return self.title == section.title and self.size == section.size


@dataclass
class DocumentTemplate:
    sections: list[SectionTemplate]

    def matches(self, document: Document) -> bool:
        return len(self.sections) == len(document.sections) and all(
            template.matches(section)
            for template, section in zip(
                self.sections,
                document.sections,
            )
        )
