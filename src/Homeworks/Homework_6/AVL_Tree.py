from typing import TypeVar, Generic, Any
from dataclasses import dataclass
from pprint import pprint


T = TypeVar("T")


@dataclass
class TreeNode(Generic[T]):
    key: Any
    value: Any
    left: "TreeNode[T]"
    right: "TreeNode[T]"
    height: int = 1


@dataclass
class Tree(Generic[T]):
    root: TreeNode[T] = None


def create_tree_map() -> Tree:
    return Tree()


def split(tree: Tree, key: Any) -> tuple[Tree, Tree]:
    lower_than_key = []
    bigger_than_key = []
    for elem in traverse(tree, "*"):
        if elem[0][0] < key:
            lower_than_key.append(elem)
        else:
            bigger_than_key.append(elem)
    new_tree1 = create_tree_map()
    for elem in lower_than_key:
        put(new_tree1, elem[0], elem[1])
    new_tree2 = create_tree_map()
    for elem in bigger_than_key:
        put(new_tree2, elem[0], elem[1])
    return (new_tree1, new_tree2)


def join(tree: Tree, another: Tree):
    another_elems = traverse(another, "*")
    for key_value in another_elems:
        put(tree, key_value[0], key_value[1])


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


def rotateL(node: TreeNode) -> TreeNode:
    a = node.right
    b = a.left
    a.left = node
    node.right = b
    node.height = 1 + max(_height(node.left), _height(node.right))
    a.height = 1 + max(_height(a.left), _height(a.right))
    return a


def rotateR(node: TreeNode) -> TreeNode:
    a = node.left
    b = a.right
    a.right = node
    node.left = b
    node.height = 1 + max(_height(node.left), _height(node.right))
    a.height = 1 + max(_height(a.left), _height(a.right))
    return a


def put(map: Tree, key: Any, value: Any):
    if map.root is None:
        map.root = TreeNode(key, value, None, None, 1)
    else:
        map.root = insert(map.root, key, value)


def insert(root: TreeNode, key: Any, value: Any):
    if root is None:
        return TreeNode(key, value, None, None, 1)
    if key > root.key:
        root.right = insert(root.right, key, value)
    elif key < root.key:
        root.left = insert(root.left, key, value)
    else:
        root.value = value
    root.height = 1 + max(_height(root.left), _height(root.right))
    balance = _balance(root)
    if balance > 1 and root.left.key > key:
        return rotateR(root)
    if balance < -1 and key > root.right.key:
        return rotateL(root)
    if balance > 1 and key > root.left.key:
        root.left = rotateL(root.left)
        return rotateR(root)
    if balance < -1 and key < root.right.key:
        root.right = rotateR(root.right)
        return rotateL(root)
    return root


def get(map: Tree, key: Any) -> Any:
    current_root = map.root
    while not (current_root is None):
        if key == current_root.key:
            return current_root.value
        elif key > current_root.key:
            current_root = current_root.right
        else:
            current_root = current_root.left
    raise AttributeError("BST hasn't Node with this key")


def has_key(map: Tree, key: Any) -> bool:
    current_root = map.root
    while not (current_root is None):
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
    while not current_root is None:
        maximum_key = current_root.key
        current_root = current_root.right
    return maximum_key


def get_minimum(map: Tree) -> Any:
    current_root = map.root
    minimum_key = current_root.key
    while not current_root is None:
        minimum_key = current_root.key
        current_root = current_root.left
    return minimum_key


def get_upper_bound(map: Tree, key: Any) -> Any:
    if get_maximum(map) < key:
        raise AttributeError
    current_root = map.root
    upper_bound = current_root.key
    while not (current_root is None):
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
    while not (current_root.left is None):
        current_root = current_root.left
    return current_root


def getAll(tree: Tree, key_left: Any, key_right: Any) -> list[Any]:
    keys = []
    for key in traverse(tree, "in-order"):
        if key_left <= key < key_right:
            keys.append(key)
    return keys


def remove_keys(tree: Tree, key_left: Any, key_right: Any):
    for key in traverse(tree, "in-order"):
        if key_left <= key < key_right:
            remove(tree, key)


def remove(map: Tree, key: Any) -> Any:
    if not has_key(map, key):
        raise AttributeError("BST hasn't Node with this key")
    deleting_value = get(map, key)

    def _removing(current_root: TreeNode, key: Any):
        if current_root.key > key:
            current_root.left = _removing(current_root.left, key)
        elif current_root.key < key:
            current_root.right = _removing(current_root.right, key)
        else:
            if current_root.left is None:
                return current_root.right
            elif current_root.right is None:
                return current_root.left

            new_node = find_min_in_right_subtree(current_root)
            current_root.key, current_root.value = new_node.key, new_node.value
            current_root.right = _removing(current_root.right, current_root.key)
        current_root.height = 1 + max(
            _height(current_root.left), _height(current_root.right)
        )
        balance = _balance(current_root)
        if balance > 1 and _balance(current_root.left) >= 0:
            return rotateR(current_root)
        if balance < -1 and _balance(current_root.right) <= 0:
            return rotateL(current_root)
        if balance > 1 and _balance(current_root.left) < 0:
            current_root.left = rotateL(current_root.left)
            return rotateR(current_root)
        if balance < -1 and _balance(current_root.right) > 0:
            current_root.right = rotateR(current_root.right)
            return rotateL(current_root)
        return current_root

    map.root = _removing(map.root, key)
    return deleting_value


def traverse(map: Tree, order: str) -> list[T]:
    if order == "pre-order":

        def _pre_order_traverse(root: TreeNode, nodes):
            if not (root is None):
                nodes.append(root.key)
                _pre_order_traverse(root.left, nodes)
                _pre_order_traverse(root.right, nodes)
            return nodes

        return _pre_order_traverse(map.root, [])
    if order == "in-order":

        def _in_order_traverse(root: TreeNode, nodes):
            if not (root is None):
                _in_order_traverse(root.left, nodes)
                nodes.append(root.key)
                _in_order_traverse(root.right, nodes)
            return nodes

        return _in_order_traverse(map.root, [])
    if order == "post-order":

        def _post_order_traverse(root: TreeNode, nodes):
            if not (root is None):
                _post_order_traverse(root.left, nodes)
                _post_order_traverse(root.right, nodes)
                nodes.append(root.key)
            return nodes

        return _post_order_traverse(map.root, [])
    if order == "*":

        def _traverse(root: TreeNode, nodes):
            if not (root is None):
                nodes.append((root.key, root.value))
                _traverse(root.left, nodes)
                _traverse(root.right, nodes)
            return nodes

        return _traverse(map.root, [])
    if order == "nodes":

        def _get_all_nodes(root: TreeNode, nodes):
            if not (root is None):
                nodes.append(root)
                _get_all_nodes(root.left, nodes)
                _get_all_nodes(root.right, nodes)
            return nodes

        return _get_all_nodes(map.root, [])


# ______________________________________________________________________________

if __name__ == "__main__":
    bst = create_tree_map()
    put(bst, 7, 1)
    put(bst, 8, 2)
    put(bst, 13, 3)
    put(bst, 3, 4)
    put(bst, 9, 5)
    put(bst, 1, 6)
    put(bst, 4, 111)
    put(bst, 6, -1)
    put(bst, 4, "ad")
    put(bst, 2, "12122")
    put(bst, -5, [12, 2, 3])
    put(bst, 11, "1")
    put(bst, 15, (-12, 3))
    pprint(traverse(bst, "in-order"))
    remove_keys(bst, 1, 9)
    pprint(traverse(bst, "in-order"))
