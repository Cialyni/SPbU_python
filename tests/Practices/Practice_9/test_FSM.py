import pytest
from io import StringIO

from src.Practices.Practice_9.FSM import create_fs_machine, validate_string
from src.Practices.Practice_9.Main import main


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
    fs_machine = create_fs_machine()
    assert validate_string(fs_machine, string) == expected


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
