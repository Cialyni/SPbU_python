import pytest
from io import StringIO
from src.Tests.test_2.recurrence import recurrence_number_finder, main


@pytest.mark.parametrize(
    "n, expected",
    (
        (13, -1971),
        (66, -158659334067458348538784),
        (0, -1),
        (100, -932063386610336536921060661316263595),
    ),
)
def test_fib_number_finder(n, expected):
    assert recurrence_number_finder(n) == expected


def test_exception_in_fib_number_finder():
    with pytest.raises(
        ValueError,
    ):
        recurrence_number_finder(-1)
        recurrence_number_finder(101)
        recurrence_number_finder("ase")
        recurrence_number_finder(1.23)


@pytest.mark.parametrize(
    "imitation_input, expected",
    (
        (
            "-1",
            "ERROR!\nN must be in diapason [0, 100]",
        ),
        ("0 0 0", "ERROR!\nInput only one integer number"),
        ("abasdasf", "ERROR!\nInput only one integer number"),
        ("45", "Result is -2059409901020726"),
        ("70", "Result is -5043111233072992795511577"),
    ),
)
def test_main(monkeypatch, imitation_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: imitation_input)
    imitation_output = StringIO()
    monkeypatch.setattr("sys.stdout", imitation_output)
    main()
    output = imitation_output.getvalue()
    assert output == expected + "\n"
