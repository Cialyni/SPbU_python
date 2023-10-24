import builtins, pytest
from unittest import mock
from src.practices.practice_6.task1 import (
    quadratic_equation_solve,
    linear_equation_solve,
    is_float_numbers,
    main,
)


@pytest.mark.parametrize(
    "a, b, c, expected",
    (
        (1, 2, -3, (-3, 1)),
        (1, 2, 1, (-1, None)),
        (0, 1, 5, (-5, None)),
    ),
)
def test_quadratic_equation(a, b, c, expected):
    actual = quadratic_equation_solve(a, b, c)
    assert actual[0] == expected[0] and actual[1] == expected[1]


def test_exception_in_quadratic_equation(a=1, b=2, c=10):
    with pytest.raises(ValueError, match="Negative discriminant, can not solve it"):
        quadratic_equation_solve(a, b, c)


@pytest.mark.parametrize(
    "k, b, expected", ((12, 54, (-54 / 12)), (0, 0, None), (0, 5, None), (5, 0, 0))
)
def test_linear_equation(k, b, expected):
    actual = linear_equation_solve(k, b)
    assert actual == expected


@pytest.mark.parametrize(
    "lst, expected",
    (
        ("1 2 3", True),
        (" ", False),
        (" 24.2  11    0", True),
        (" 24.2  11. .0", True),
        (" 24..2  11. 0", False),
        ("adf 1 dl-dd", False),
        ("11.1", False),
        ("1 2 3 4", False),
        ("1,13 4,3 1", False),
        ("1e3 1.133e-5 1", True),
    ),
)
def test_is_float_numbers(lst, expected):
    actual = is_float_numbers(lst)
    assert actual == expected


def test_main():
    with mock.patch.object(builtins, "input", lambda: "1 4 3"):
        assert main() == (-3.0, -1.0)
