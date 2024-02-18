import pytest
from src.LeetCode.leet_code_task_1 import nextPermutation


@pytest.mark.parametrize(
    "nums, expected",
    (
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 4, 1, 5, 1, 8, 9], [1, 4, 1, 5, 1, 9, 8]),
        ([1, 1, 1], [1, 1, 1]),
    ),
)
def test_solution_next_permutation(nums, expected):
    actual = nextPermutation(nums)
    assert actual == expected
