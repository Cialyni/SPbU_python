import pytest
from src.LeetCode.leet_code_task3 import find_min_substring_with_size


@pytest.mark.parametrize(
    "nums, k, expected",
    (
        ("1432219", 3, [1, 2, 1, 9]),
        ("10200", 1, [2, 0, 0]),
        ("10", 2, [0]),
        ("3452346723432423423566581", 14, [2, 2, 2, 2, 2, 3, 5, 6, 5, 8, 1]),
        ("1321000011030104050063010", 10, [6, 3, 0, 1, 0]),
    ),
)
def test_find_min_substring_with_size(nums, k, expected):
    actual = find_min_substring_with_size(nums, k)
    assert actual == expected
