from pathlib import Path

from vedtech import parse_document
from vedtech.default_templates import ADR_EDGEX_TEMPLATE, ADR_NYGAARD_TEMPLATE


def test_nygaard_match_template():
    with Path.open("tests/samples/nygaard_example.md") as file:
        assert ADR_NYGAARD_TEMPLATE.matches(parse_document(file.read()))


def test_edgex_match_template():
    with Path.open("tests/samples/edgex_example.md") as file:
        assert ADR_EDGEX_TEMPLATE.matches(parse_document(file.read()))


def test_empty_does_not_match_template():
    with Path.open("tests/samples/empty_file.md") as file:
        assert not ADR_NYGAARD_TEMPLATE.matches(parse_document(file.read()))
