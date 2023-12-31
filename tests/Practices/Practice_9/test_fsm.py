import pytest
from io import StringIO

from src.Practices.Practice_9.fsm import (
    give_message_about_string,
    create_aboba_fs_machine,
    create_float_fs_machine,
    validate_string,
)
from src.Practices.Practice_9.main import main

FSM_aboba = create_aboba_fs_machine()
FSM_float = create_float_fs_machine()


@pytest.mark.parametrize(
    "string, expected",
    (
        ("abb", True),
        ("123.1222", True),
        ("abbabbabbabb", True),
        ("abababeedfsseabb", False),
        ("abbab", False),
        ("1E32", True),
        ("1++32.22E", False),
        ("", True),
        ("12.25E+0049", True),
        ("12.25E+0049E-2324", False),
    ),
)
def test_validate_string(string, expected):
    assert (
        validate_string(FSM_float, string) == expected
        or validate_string(FSM_aboba, string) == expected
    )


@pytest.mark.parametrize(
    "imitation_input, expected",
    (
        ("sfse", "This line does not belong to the (a|b)*abb"),
        ("abbaaaaaabb", "This line belongs to the (a|b)*abb"),
        ("aboba", "This line does not belong to the (a|b)*abb"),
    ),
)
def test_main(monkeypatch, imitation_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: imitation_input)
    imitation_output = StringIO()
    monkeypatch.setattr("sys.stdout", imitation_output)
    main()
    output = imitation_output.getvalue()
    assert output == expected + "\n"
