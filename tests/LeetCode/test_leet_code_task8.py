import pytest
from src.LeetCode.leet_code_task8 import find_closest_elements


@pytest.mark.parametrize(
    "arr, k, x, expected",
    (
        ([-2, -1, 1, 2, 3, 4, 5], 7, 3, [-2, -1, 1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        ([1, 3, 5, 6, 7], 2, 10, [6, 7]),
    ),
)
def test_find_closest_elements(arr, k, x, expected):
    actual = find_closest_elements(arr, k, x)
    assert actual == expected
