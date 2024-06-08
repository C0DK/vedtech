from pathlib import Path

from vedtech import DocumentTemplate, SectionTemplate, parse_document


def test_nygaard_match_template():
    with Path.open("tests/samples/nygaard_example.md") as file:
        assert nygaard_template.matches(parse_document(file.read()))


def test_edgex_match_template():
    with Path.open("tests/samples/edgex_example.md") as file:
        assert edgex_template.matches(parse_document(file.read()))


def test_empty_does_not_match_template():
    with Path.open("tests/samples/empty_file.md") as file:
        assert not nygaard_template.matches(parse_document(file.read()))


nygaard_template = DocumentTemplate(
    sections=[
        SectionTemplate(
            title="Decision record template by Michael Nygard",
            size=1,
        ),
        SectionTemplate(
            title="Title",
            size=1,
        ),
        SectionTemplate(
            title="Status",
            size=2,
        ),
        SectionTemplate(
            title="Context",
            size=2,
        ),
        SectionTemplate(
            title="Decision",
            size=2,
        ),
        SectionTemplate(
            title="Consequences",
            size=2,
        ),
    ],
)

edgex_template = DocumentTemplate(
    sections=[
        SectionTemplate(
            title="Architecture Decision Record (ADR) template"
            " <!-- Replace with ADR title -->",
            size=1,
        ),
        SectionTemplate(
            title="Submitters",
            size=3,
        ),
        SectionTemplate(
            title="Change Log",
            size=2,
        ),
        SectionTemplate(
            title="Referenced Use Case(s)",
            size=2,
        ),
        SectionTemplate(
            title="Context",
            size=2,
        ),
        SectionTemplate(
            title="Proposed Design",
            size=2,
        ),
        SectionTemplate(
            title="Considerations",
            size=2,
        ),
        SectionTemplate(
            title="Decision",
            size=2,
        ),
        SectionTemplate(
            title="Other Related ADRs",
            size=2,
        ),
        SectionTemplate(
            title="References",
            size=2,
        ),
    ],
)
