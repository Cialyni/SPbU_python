from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_univalue_path(root: TreeNode) -> int:

    def _traverse(current_root: TreeNode) -> Tuple[int, int]:
        if current_root is None or current_root.val is None:
            return 0, 0
        left_res = _traverse(current_root.left)
        right_res = _traverse(current_root.right)
        right = (
            right_res[0] + 1
            if current_root.right and current_root.val == current_root.right.val
            else 0
        )
        left = (
            left_res[0] + 1
            if current_root.left and current_root.val == current_root.left.val
            else 0
        )
        return max(left, right), max(max(left_res[1], right_res[1]), left + right)

    return _traverse(root)[1]
