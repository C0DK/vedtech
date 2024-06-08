from vedtech import parse_document, DocumentTemplate, SectionTemplate

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
        ]
    )


def test_nygaard_match_template():
    with open("tests/samples/nygaard_example.md") as file:
        document = parse_document(file.read())

    assert nygaard_template.matches(document)


def test_empty_does_not_match_template():
    with open("tests/samples/empty_file.md") as file:
        document = parse_document(file.read())

    assert not nygaard_template.matches(document)
