import pytest
from src.LeetCode.leetcode_task5 import min_sum


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    (
        ([2, 0, 2, 0], [1, 4], -1),
        ([3, 2, 0, 1, 0], [6, 5, 0], 12),
        ([1, 45, 0, 2, 4, 0, 0, 0, 2], [0], 58),
    ),
)
def test_is_valid_sudoku(nums1, nums2, expected):
    actual = min_sum(nums1, nums2)
    assert actual == expected
