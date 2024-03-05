import pytest
from src.LeetCode.leet_code_task3 import find_min_substring_with_size


@pytest.mark.parametrize(
    "nums, k, expected",
    (
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
        ("3452346723432423423566581", 14, "22222356581"),
        ("1321000011030104050063010", 10, "63010"),
    )
)
def test_find_min_substring_with_size(nums, k, expected):
    actual = find_min_substring_with_size(nums, k)
    assert actual == expected
