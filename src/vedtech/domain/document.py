from dataclasses import dataclass


@dataclass
class Section:
    title: str
    size: int
    lines: list[str]


@dataclass
class Document:
    sections: list[Section]
