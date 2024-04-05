import pytest
from .document import Document, DocumentTemplate, Section, SectionTemplate


@pytest.mark.parametrize(
    "template,value",
    [
        (
            SectionTemplate(title="A", size=1),
            Section(title="A", size=1, lines=[]),
        ),
        (
            SectionTemplate(title="title", size=4),
            Section(title="title", size=4, lines=[]),
        ),
    ],
)
def test_section_template_match(template: SectionTemplate, value: Section):
    assert template.matches(value)


@pytest.mark.parametrize(
    "template,value",
    [
        (
            SectionTemplate(title="A", size=1),
            Section(title="B", size=1, lines=[]),
        ),
        (
            SectionTemplate(title="A", size=1),
            Section(title="A", size=2, lines=[]),
        ),
        (
            SectionTemplate(title="A", size=2),
            Section(title="A", size=1, lines=[]),
        ),
    ],
)
def test_section_template_does_not_match(template: SectionTemplate, value: Section):
    assert not template.matches(value)


@pytest.mark.parametrize(
    "template,value",
    [
        (
            DocumentTemplate(
                sections=[
                    SectionTemplate(title="A", size=1),
                ]
            ),
            Document(
                sections=[
                    Section(title="B", size=1, lines=[]),
                ]
            ),
        ),
        (
            DocumentTemplate(
                sections=[
                    SectionTemplate(title="A", size=1),
                ]
            ),
            Document(
                sections=[
                    Section(title="A", size=2, lines=[]),
                ]
            ),
        ),
        (
            DocumentTemplate(
                sections=[
                    SectionTemplate(title="A", size=1),
                    SectionTemplate(title="B", size=1),
                ]
            ),
            Document(
                sections=[
                    Section(title="A", size=1, lines=[]),
                ]
            ),
        ),
        (
            DocumentTemplate(
                sections=[
                    SectionTemplate(title="A", size=1),
                ]
            ),
            Document(
                sections=[
                    Section(title="A", size=1, lines=[]),
                    Section(title="B", size=2, lines=[]),
                ]
            ),
        ),
        (
            DocumentTemplate(
                sections=[
                    SectionTemplate(title="A", size=1),
                    SectionTemplate(title="A", size=1),
                ]
            ),
            Document(
                sections=[
                    Section(title="A", size=1, lines=[]),
                    Section(title="B", size=2, lines=[]),
                ]
            ),
        ),
    ],
)
def test_document_template_does_not_match(template: DocumentTemplate, value: Document):
    assert not template.matches(value)
