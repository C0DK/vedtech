import pytest
from vedtech.cli import (
    check,
    DocumentDidNotMatchTemplate,
    PathWasDirectoryExit,
    Template,
)


def test_egdex_doesnot_match_template():
    with pytest.raises(DocumentDidNotMatchTemplate):
        check("tests/samples/edgex_example.md", Template.ADR_NYGAARD)


def test_nygaard_match_template():
    assert "matched template" in check(
        "tests/samples/nygaard_example.md",
        Template.ADR_NYGAARD,
    )


def test_throws_on_directory():
    with pytest.raises(IsADirectoryError):
        check("tests/samples/", Template.ADR_NYGAARD)


def test_throws_on_non_file():
    with pytest.raises(FileNotFoundError):
        check("/aaadasdasdasdasda", Template.ADR_NYGAARD)


# TODO: test on invalid files
