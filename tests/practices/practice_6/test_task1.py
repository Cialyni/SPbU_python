import builtins, pytest
from unittest import mock
from src.practices.practice_6.task1 import (
    quadratic_equation_solve,
    linear_equation_solve,
    parse_user_input,
    main,
)


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (1, 2, -3, (-3, 1)),
        (1, 2, 1, (-1,)),
        (0, 1, 5, (-5,)),
    ),
)
def test_quadratic_equation(a, b, c, expected):
    actual = quadratic_equation_solve(a, b, c)
    if len(actual) == 2:
        assert actual[0] == expected[0] and actual[1] == expected[1]
    else:
        assert actual[0] == expected[0]


def test_exception_in_quadratic_equation(a=1, b=2, c=10):
    with pytest.raises(ValueError, match="Negative discriminant, can not solve it"):
        quadratic_equation_solve(a, b, c)


@pytest.mark.parametrize("k, b, expected", ((12, 54, (-54 / 12)), (5, 0, 0)))
def test_linear_equation(k, b, expected):
    actual = linear_equation_solve(k, b)
    assert actual == expected


def test_ZeroDivisionError_exception_in_quadratic_equation(b=0, k=5):
    with pytest.raises(ZeroDivisionError, match="division by zero: k = 0"):
        linear_equation_solve(b, k)


def test_ValueError_exception_in_quadratic_equation(b=0, k=0):
    with pytest.raises(ValueError, match="infinite number of solutions with k = b = 0"):
        linear_equation_solve(b, k)


@pytest.mark.parametrize(
    "lst, expected",
    (
        ("1 2 3", (1, 2, 3)),
        (" 24.2  11    0", (24.2, 11, 0)),
        (" 24.2  11. .0", (24.2, 11.0, 0.0)),
        ("1e3 1.133e-5 1", (1e3, 1.133e-5, 1)),
    ),
)
def test_parse_user_input(lst, expected):
    actual = parse_user_input(lst)
    assert actual == expected


@pytest.mark.parametrize(
    "s",
    (
        " 24..2  11. 0",
        "adf 1 dl-dd",
        "11.1",
        "1 2 3 4",
        "1,13 4,3 1",
        " ",
        "adf 1 dl-dd",
    ),
)
def test_ValueError_exception_in_parse_user_input(s):
    with pytest.raises(
        ValueError, match="Need 3 float arguments in one string with space: A B C"
    ):
        parse_user_input(s)


def test_main():
    with mock.patch.object(builtins, "input", lambda _: "1 4 3"):
        assert main() == (-3.0, -1.0)
