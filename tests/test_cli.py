import pytest
from typer.testing import CliRunner, Result
from vedtech.default_templates import Template
from vedtech.cli import (
    app,
    Template,
)

runner = CliRunner()


def run_check(*args):
    return runner.invoke(app, ["check", *args])


def assert_failed_with(msg: str, result: Result):
    assert result.exit_code == 1 and msg in result.stdout


def assert_success(result: Result):
    assert result.exit_code == 0


def test_egdex_doesnot_match_template():

    result = run_check("tests/samples/edgex_example.md", Template.ADR_NYGAARD)

    assert_failed_with("not match", result)


def test_nygaard_match_template():
    result = run_check(
        "tests/samples/nygaard_example.md",
        Template.ADR_NYGAARD,
    )
    assert_success(result)


def test_throws_on_directory():
    result = run_check(
        "tests/samples/",
        Template.ADR_NYGAARD,
    )
    assert_failed_with("cannot check", result)


def test_throws_on_non_file():
    result = run_check(
        "/aaaaaaaaaaaa",
        Template.ADR_NYGAARD,
    )
    assert_failed_with("No such file", result)
