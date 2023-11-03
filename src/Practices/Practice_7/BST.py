from typing import TypeVar, Generic
from dataclasses import dataclass

Key = TypeVar("Key")
Value = TypeVar("Value")
T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    key: Key
    value: Value
    left: "TreeNode[T]"
    right: "TreeNode[T]"


@dataclass
class Tree(Generic[T]):
    root: TreeNode[T]
    size: int


def create_tree_map() -> Tree:
    return Tree(TreeNode(None, None, None, None), 0)


def delete_tree_map(map: Tree):
    def rec_delete(root: TreeNode):
        if not (root is None):
            rec_delete(root.left)
            rec_delete(root.right)
            del root

    map.root = rec_delete(map.root)


def insert_first_root(map: Tree, key: Key, value: Value):
    map.root = TreeNode(key, value, None, None)
    map.size = 1


def put(map: Tree, key: Key, value: Value):
    if map.size == 0:
        insert_first_root(map, key, value)
    else:
        insert(map.root, key, value)
        map.size += 1


def insert(root: TreeNode, key: Key, value: Value):
    if root is None:
        return TreeNode(key, value, None, None)
    if key > root.key:
        root.right = insert(root.right, key, value)
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.value = value
    return root


def get(map: Tree, key: Key) -> Value:
    current_root = map.root
    while not (current_root is None):
        if key == current_root.key:
            return current_root.value
        elif key > current_root.key:
            current_root = current_root.right
        else:
            current_root = current_root.left
    raise AttributeError("BST hasn't Node with this key")


def has_key(map: Tree, key: Key) -> bool:
    current_root = map.root
    while not (current_root is None):
        if key == current_root.key:
            return True
        elif key > current_root.key:
            current_root = current_root.right
        elif key < current_root.key:
            current_root = current_root.left
    return False


def find_first_max_in_subtree(root: TreeNode):
    current_root = root.right
    if current_root is None:
        return root
    while not (current_root.left is None):
        current_root = current_root.left
    return current_root


def remove(map: Tree, key: Key) -> Value:
    if not has_key(map, key):
        raise AttributeError("BST hasn't Node with this key")

    def _removing(current_root: TreeNode, key: Key):
        if current_root.key > key:
            new_left, value = _removing(current_root.left, key)
            current_root.left = new_left
            return current_root, value
        elif current_root.key < key:
            new_right, value = _removing(current_root.right, key)
            current_root.right = new_right
            return current_root, value
        else:
            if current_root.left is None and current_root.right is None:
                return None, current_root.value
            elif not (current_root.left is None) + (not (current_root.right is None)):
                new_node = (
                    current_root.left
                    if current_root.right is None
                    else current_root.right
                )
                return new_node, current_root.value
            else:
                new_node = find_first_max_in_subtree(current_root)
                val = current_root.value
                current_root.key, current_root.value = new_node.key, new_node.value
                new_right, _ = _removing(current_root.right, current_root.key)
                current_root.right = new_right
                return current_root, val

    map.root, value = _removing(map.root, key)
    map.size -= 1
    return value


def pre_order_traverse(root: TreeNode, lst, tree_size):
    if len(lst) == tree_size:
        return lst
    if not (root is None):
        lst.append([root.key, root.value])
        pre_order_traverse(root.left, lst, tree_size)
        pre_order_traverse(root.right, lst, tree_size)
    return lst


def in_order_traverse(root: TreeNode, lst, tree_size):
    if len(lst) == tree_size:
        return lst
    if not (root is None):
        if not (root.left is None):
            in_order_traverse(root.left, lst, tree_size)
        lst.append([root.key, root.value])
        in_order_traverse(root.right, lst, tree_size)
    return lst


def post_order_traverse(root: TreeNode, lst, tree_size):
    if len(lst) == tree_size:
        return lst
    if not (root is None):
        post_order_traverse(root.left, lst, tree_size)
        post_order_traverse(root.right, lst, tree_size)
        lst.append([root.key, root.value])
    return lst


def traverse(map: Tree, order: str) -> list[T]:
    ans = []
    if order == "pre-order":
        return pre_order_traverse(map.root, ans, map.size)
    if order == "in-order":
        return in_order_traverse(map.root, ans, map.size)
    if order == "post-order":
        return post_order_traverse(map.root, ans, map.size)


# ______________________________________________________________________________

