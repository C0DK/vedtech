import pytest

from .document import Document, Section
from .file_loader import extract_next_section, parse_document


def test_parse_document_empty():
    assert parse_document("") == Document(sections=[])


def test_parse_document_one_section():
    assert (
        parse_document(
            """
# Heading
some content
""",
        )
        == Document(sections=[Section(title="Heading", size=1, lines=["some content"])])
    )


def test_parse_document_multiple_section():
    assert (
        parse_document(
            """
# Heading
## Smaller header
some content
# Bigger header
some other content
""",
        )
        == Document(
            sections=[
                Section(title="Heading", size=1, lines=[]),
                Section(title="Smaller header", size=2, lines=["some content"]),
                Section(title="Bigger header", size=1, lines=["some other content"]),
            ],
        )
    )


def test_extract_next_section_fails_on_empty_string():
    with pytest.raises(ValueError, match="is empty"):
        extract_next_section("")


def test_extract_next_section_fails_on_not_start_of_section():
    with pytest.raises(ValueError, match="did not start with headin"):
        extract_next_section("test\n# heading")


def test_extract_next_section_only_heading():
    assert extract_next_section("# Test")[0] == Section("Test", size=1, lines=[])


def test_extract_next_section_simple():
    assert extract_next_section("# Test \nsome \nlines")[0] == Section(
        "Test",
        size=1,
        lines=["some ", "lines"],
    )


def test_extract_next_section_simple_other_size():
    assert extract_next_section("### Test")[0] == Section("Test", size=3, lines=[])


def test_extract_next_section_complex():
    assert (
        extract_next_section(
            """
# Test
some
   lines

> And something
**BOLD**?

""",
        )
        == (
            Section(
                "Test",
                size=1,
                lines=[
                    "some",
                    "   lines",
                    "",
                    "> And something",
                    "**BOLD**?",
                    "",
                ],
            ),
            "",
        )
    )


def test_extract_next_section_remainder_with_content():
    assert extract_next_section("# Test \ntest\n# Test 2")[1] == "# Test 2"


def test_extract_next_section_remainder_empty():
    assert extract_next_section("# Test \ntest")[1] == ""
