# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_univalue_path(root: TreeNode) -> int:
    ans = [0]

    def _traverse(current_root: TreeNode) -> int:
        if current_root is None or current_root.val is None:
            return 0
        left_res, right_res = _traverse(current_root.left), _traverse(current_root.right)
        right = right_res + 1 if current_root.right and current_root.val == current_root.right.val else 0
        left = left_res + 1 if current_root.left and current_root.val == current_root.left.val else 0
        ans[0] = max(ans[0], left + right)
        return max(left, right)

    _traverse(root)
    return ans[0]
