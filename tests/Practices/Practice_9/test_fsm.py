import pytest
from io import StringIO

from src.Practices.Practice_9.fsm import validate_string, create_fs_machine
from src.Practices.Practice_9.main import main


FSM = create_fs_machine(
    initial=0,
    accepting=[
        3,
    ],
    transitions={
        0: {"a": 1, "b": 0},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"a": 1, "b": 0},
    },
)


@pytest.mark.parametrize(
    "string, expected",
    (
        ("", False),
        ("abb", True),
        ("ababababbbbbaaabb", True),
        ("abbabbabbabb", True),
        ("abababeedfsseabb", False),
        ("abbab", False),
        ("sefafeczvcnny", False),
    ),
)
def test_validate_string(string, expected):
    assert validate_string(FSM, string) == expected


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