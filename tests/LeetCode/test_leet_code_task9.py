import pprint
from typing import List

import pytest
from src.LeetCode.leet_code_task9 import longest_univalue_path, TreeNode


def build_tree_from_list(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    que = [root]
    i = 1
    while i < len(nums):
        curr = que.pop(0)
        if i < len(nums):
            curr.left = TreeNode(nums[i])
            que.append(curr.left)
            i += 1
        if i < len(nums):
            curr.right = TreeNode(nums[i])
            que.append(curr.right)
            i += 1
    return root


@pytest.mark.parametrize(
    "nums, expected",  # very uncomfortable to put here tree like TreeNode(val, left=TreNode(.......), but excepted only full tree, without spaces
    (
        ([1, 4, 5, 4, 4, None, 5], 2),
        ([5, 4, 5, 1, 1, None, 5], 2),
        ([], 0),
        (
            [
                1,
                2,
                43,
                2,
                34,
                2,
                423,
                None,
                1,
                1,
                2,
                2,
                None,
                None,
                None,
                None,
                None,
                3,
                4,
                5,
                66,
                7,
                8,
                5,
                3,
                3,
                4,
                6,
                7,
                8,
            ],
            1,
        ),
        (
            [
                5,
                4,
                5,
                1,
                1,
                None,
                5,
                5,
                5,
                5,
                None,
                None,
                5,
                5,
                5,
                1,
                1,
                3,
                4,
                5,
                5,
                5,
                5,
            ],
            3,
        ),
        (
            [
                1,
                1,
                1,
                1,
                None,
                None,
                1,
                1,
                None,
                None,
                None,
                None,
                1,
                11,
                1,
                1,
                1,
                1,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                1,
            ],
            8,
        ),
        ([4, 3, 4, 5, 3, 4, 3, 4, None, None, None, 4, 4, 3], 3),
    ),
)
def test_longest_univalue_path(nums, expected):
    tree = build_tree_from_list(nums)
    assert longest_univalue_path(tree) == expected
