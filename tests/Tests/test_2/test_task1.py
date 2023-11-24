import pytest
from io import StringIO
from src.Tests.test_2.task1 import fib_number_finder, main


@pytest.mark.parametrize(
    "n, expected",
    (
        (13, 233),
        (66, 27777890035288),
    ),
)
def test_fib_number_finder(n, expected):
    assert fib_number_finder(n) == expected


def test_exception_in_fib_number_finder():
    with pytest.raises(
        ValueError,
    ):
        fib_number_finder(-1)
        fib_number_finder(91)
        fib_number_finder("ase")


@pytest.mark.parametrize(  # this strange format made black :)
    "imitation_input, expected",
    (
        (
            "-1",
            "ERROR!\nEnter only one integer number in range [0:90]",
        ),
        ("0 0 0", "ERROR!\nEnter only one integer number in range [0:90]"),
        ("abasdasf", "ERROR!\nEnter only one integer number in range [0:90]"),
        ("45", "Result is: 1134903170"),
        ("90", "Result is: 2880067194370816120"),
    ),
)
def test_main(monkeypatch, imitation_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: imitation_input)
    imitation_output = StringIO()
    monkeypatch.setattr("sys.stdout", imitation_output)
    main()
    output = imitation_output.getvalue()
    assert output == expected + "\n"
