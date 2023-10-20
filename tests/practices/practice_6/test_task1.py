import pytest
from src.practices.practice_6.task1 import quadratic_equation_solve, linear_equation_solve, is_float_numbers

"""def test_raise_exception():
    with pytest.raises(ValueError):
        my_func()"""

test_value_quadratic = [(1, 2, -3, (-3, 1)), (1, 2, 1, (-1, None)), (1, 2, 10, ()), (0, 1, 5, (-5, None))]


@pytest.mark.parametrize("a,b,c,expected", test_value_quadratic)
def test_quadratic_equation(a, b, c, expected):
    actual = quadratic_equation_solve(a, b, c)
    assert actual[0] == expected[0] and actual[1] == expected[1]


test_value_linear = [(12, 54, (-54 / 12)), (0, 0, None), (0, 5, None), (5, 0, 0)]


@pytest.mark.parametrize("k, b, expected", test_value_linear)
def test_linear_equation(k, b, expected):
    actual = linear_equation_solve(k, b)
    assert actual == expected


test_value_checker = [('1 2 3', True), (' ', False), (' 24.2  11    0', True),
                      ('adf 1 dl-dd', False), ('11.1', False), ('1 2 3 4', False)]


@pytest.mark.parametrize("lst, expected", test_value_checker)
def test_is_float_numbers(lst, expected):
    actual = is_float_numbers(lst)
    assert actual == expected
