import pytest
from io import StringIO

from src.Practices.Practice_9.fsm import validate_string, create_fs_machine
from src.Practices.Practice_9.main import main

FSM_aboba = create_fs_machine(
    initial=0,
    accepting=[0, 4],
    transitions={
        0: {"a": 2, "b": 1},
        1: {"a": 2, "b": 1},
        2: {"a": 2, "b": 3},
        3: {"a": 2, "b": 4},
        4: {"a": 2, "b": 1},
    },
)

FSM_float = create_fs_machine(
    initial=0,
    accepting=[0, 1, 5],
    transitions={
        0: {"DIGIT": 1},
        1: {"DIGIT": 1, "E": 3, ".": 2},
        2: {"DIGIT": 1},
        3: {"DIGIT": 5, "SIGN": 4},
        4: {"DIGIT": 5},
        5: {"DIGIT": 5},
    },
)


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
        ("sfse", "This string does not belong to any of these languages"),
        ("abbaaaaaabb", "This line belongs to the (a|b)*abb"),
        ("aboba", "This string does not belong to any of these languages"),
    ),
)
def test_main(monkeypatch, imitation_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: imitation_input)
    imitation_output = StringIO()
    monkeypatch.setattr("sys.stdout", imitation_output)
    main()
    output = imitation_output.getvalue()
    assert output == expected + "\n"
