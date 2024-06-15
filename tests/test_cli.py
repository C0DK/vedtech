import pytest
from vedtech.cli import (
    CommandHandler,
    DocumentDidNotMatchTemplate,
    PathWasDirectoryExit,
    Template,
)


def test_egdex_doesnot_match_template():
    with pytest.raises(DocumentDidNotMatchTemplate):
        CommandHandler().check("tests/samples/edgex_example.md", Template.ADR_NYGAARD)


def test_nygaard_match_template():
    assert "matched template" in CommandHandler().check(
        "tests/samples/nygaard_example.md",
        Template.ADR_NYGAARD,
    )


def test_throws_on_directory():
    with pytest.raises(PathWasDirectoryExit):
        CommandHandler().check("tests/samples/", Template.ADR_NYGAARD)
