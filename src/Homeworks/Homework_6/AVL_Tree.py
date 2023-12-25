from typing import TypeVar, Generic, Any
from dataclasses import dataclass

REMOVING_VALUE = None


@dataclass
class TreeNode:
    key: Any
    value: Any
    left: "TreeNode"
    right: "TreeNode"
    height: int = 1


@dataclass
class Tree:
    root: TreeNode = None


def create_tree_map() -> Tree:
    return Tree()


def delete_tree_map(map: Tree):
    def rec_delete(root: TreeNode):
        if not (root is None):
            rec_delete(root.left)
            rec_delete(root.right)
            del root

    map.root = rec_delete(map.root)


def _balance(node: TreeNode) -> int:
    return 0 if node is None else _height(node.left) - _height(node.right)


def _height(node: TreeNode) -> int:
    return 0 if node is None else node.height


def rotate_left(node: TreeNode) -> TreeNode:
    a = node.right
    b = a.left
    a.left = node
    node.right = b
    update_height(node)
    update_height(a)
    return a


def rotate_right(node: TreeNode) -> TreeNode:
    a = node.left
    b = a.right
    a.right = node
    node.left = b
    update_height(node)
    update_height(a)
    return a


def put(map: Tree, key: Any, value: Any):
    if map.root is None:
        map.root = TreeNode(key, value, None, None, 1)
    else:
        map.root = insert(map.root, key, value)


def update_height(root: TreeNode):
    root.height = 1 + max(_height(root.left), _height(root.right))


def balancing(root: TreeNode, key) -> TreeNode | None:
    balance = _balance(root)
    if balance > 1:
        if root.left.key > key:  # small rotate
            return rotate_right(root)
        root.left = rotate_left(root.left)
        return rotate_right(root)  # big rotate
    if balance < -1:
        if key > root.right.key:  # small rotate
            return rotate_left(root)
        root.right = rotate_right(root.right)
        return rotate_left(root)  # big rotate
    return None


def insert(root: TreeNode, key: Any, value: Any) -> TreeNode:
    if root is None:
        return TreeNode(key, value, None, None, 1)
    if key > root.key:
        root.right = insert(root.right, key, value)
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.value = value
    update_height(root)
    rotate_root = balancing(root, key)
    if rotate_root is not None:
        return rotate_root
    return root


def get(map: Tree, key: Any) -> Any:
    current_root = map.root
    while current_root is not None:
        if key == current_root.key:
            return current_root.value
        elif key > current_root.key:
            current_root = current_root.right
        else:
            current_root = current_root.left
    raise AttributeError("BST hasn't Node with this key")


def has_key(map: Tree, key: Any) -> bool:
    current_root = map.root
    while current_root is not None:
        if key == current_root.key:
            return True
        elif key > current_root.key:
            current_root = current_root.right
        elif key < current_root.key:
            current_root = current_root.left
    return False


def get_maximum(map: Tree) -> Any:
    current_root = map.root
    maximum_key = current_root.key
    while current_root is not None:
        maximum_key = current_root.key
        current_root = current_root.right
    return maximum_key


def get_minimum(map: Tree) -> Any:
    current_root = map.root
    minimum_key = current_root.key
    while current_root is not None:
        minimum_key = current_root.key
        current_root = current_root.left
    return minimum_key


def get_upper_bound(map: Tree, key: Any) -> Any:
    if get_maximum(map) < key:
        raise AttributeError
    current_root = map.root
    upper_bound = current_root.key
    while current_root is not None:
        upper_bound = current_root.key if current_root.key > key else upper_bound
        if current_root.key > key:
            current_root = current_root.left
        else:
            current_root = current_root.right
    return upper_bound


def get_lower_bound(map: Tree, key: Any) -> Any:
    if has_key(map, key):
        return key
    return get_upper_bound(map, key)


def find_min_in_right_subtree(root: TreeNode) -> TreeNode:
    current_root = root.right
    if current_root is None:
        return root
    while current_root.left is not None:
        current_root = current_root.left
    return current_root


def remove(map: Tree, key: Any) -> Any:
    if not has_key(map, key):
        raise AttributeError("BST hasn't Node with this key")
    deleting_value = get(map, key)

    def _remove(current_root: TreeNode, key: Any):
        if current_root.key > key:
            current_root.left = _remove(current_root.left, key)
        elif current_root.key < key:
            current_root.right = _remove(current_root.right, key)
        else:
            if current_root.left is None:
                return current_root.right
            elif current_root.right is None:
                return current_root.left

            new_node = find_min_in_right_subtree(current_root)
            current_root.key, current_root.value = new_node.key, new_node.value
            current_root.right = _remove(current_root.right, current_root.key)
        update_height(current_root)
        rotate_root = balancing(current_root, key)
        if rotate_root is not None:
            return rotate_root
        return current_root

    map.root = _remove(map.root, key)
    return deleting_value


def pre_order_traverse(root: TreeNode, nodes):
    if not (root is None):
        nodes.append(root.key)
        pre_order_traverse(root.left, nodes)
        pre_order_traverse(root.right, nodes)
    return nodes


def in_order_traverse(root: TreeNode, nodes):
    if not (root is None):
        in_order_traverse(root.left, nodes)
        nodes.append(root.key)
        in_order_traverse(root.right, nodes)
    return nodes


def post_order_traverse(root: TreeNode, nodes):
    if not (root is None):
        post_order_traverse(root.left, nodes)
        post_order_traverse(root.right, nodes)
        nodes.append(root.key)
    return nodes


def traverse(map: Tree, order: str):
    ans = []
    if order == "pre-order":
        return pre_order_traverse(map.root, ans)
    if order == "in-order":
        return in_order_traverse(map.root, ans)
    if order == "post-order":
        return post_order_traverse(map.root, ans)


# ______________________________________________________________________________

if __name__ == "__main__":
    TEST_AVL_TREE = Tree(
        root=TreeNode(
            key=8,
            value=2,
            left=TreeNode(
                key=3,
                value=4,
                left=TreeNode(
                    key=1,
                    value=6,
                    left=TreeNode(
                        key=-5, value=[12, 2, 3], left=None, right=None, height=1
                    ),
                    right=TreeNode(
                        key=2, value="12122", left=None, right=None, height=1
                    ),
                    height=2,
                ),
                right=TreeNode(
                    key=6,
                    value=-1,
                    left=TreeNode(key=4, value="ad", left=None, right=None, height=1),
                    right=TreeNode(key=7, value=1, left=None, right=None, height=1),
                    height=2,
                ),
                height=3,
            ),
            right=TreeNode(
                key=11,
                value="1",
                left=TreeNode(key=9, value=5, left=None, right=None, height=1),
                right=TreeNode(
                    key=13,
                    value=3,
                    left=None,
                    right=TreeNode(
                        key=15, value=(-12, 3), left=None, right=None, height=1
                    ),
                    height=2,
                ),
                height=3,
            ),
            height=4,
        )
    )
    remove(TEST_AVL_TREE, 11)
    print(get_lower_bound(TEST_AVL_TREE, 11))
