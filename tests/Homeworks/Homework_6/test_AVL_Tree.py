import pytest, copy
from src.Homeworks.Homework_6.AVL_Tree import (
    TreeNode,
    Tree,
    put,
    get,
    has_key,
    remove,
    create_tree_map,
    get_maximum,
    get_lower_bound,
    get_minimum,
    get_upper_bound,
    traverse,
    rotate_left,
    rotate_right,
    insert,
)

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
                right=TreeNode(key=2, value="12122", left=None, right=None, height=1),
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
                right=TreeNode(key=15, value=(-12, 3), left=None, right=None, height=1),
                height=2,
            ),
            height=3,
        ),
        height=4,
    )
)


def test_exception_in_get(key1=212, key2=0):
    with pytest.raises(ValueError, match="BST hasn't Node with this key"):
        get(TEST_AVL_TREE, key1)
        get(TEST_AVL_TREE, key2)


def test_rotate_left():
    expected = Tree(
        root=TreeNode(
            key=5,
            value=0,
            left=TreeNode(key=0, value=0, left=None, right=None, height=1),
            right=TreeNode(key=10, value=0, left=None, right=None, height=1),
            height=2,
        )
    )
    test_tree = Tree(
        root=TreeNode(
            key=0,
            value=0,
            left=None,
            right=TreeNode(
                key=5,
                value=0,
                left=None,
                right=TreeNode(key=10, value=0, left=None, right=None, height=1),
                height=2,
            ),
            height=3,
        )
    )
    test_tree.root = rotate_left(test_tree.root)
    assert test_tree == expected


def test_rotate_right():
    expected = Tree(
        root=TreeNode(
            key=-5,
            value=0,
            left=TreeNode(key=-10, value=0, left=None, right=None, height=1),
            right=TreeNode(key=0, value=0, left=None, right=None, height=1),
            height=2,
        )
    )
    test_tree = Tree(
        root=TreeNode(
            key=0,
            value=0,
            left=TreeNode(
                key=-5,
                value=0,
                left=TreeNode(key=-10, value=0, left=None, right=None, height=1),
                right=None,
                height=2,
            ),
            right=None,
            height=3,
        )
    )
    test_tree.root = rotate_right(test_tree.root)
    assert test_tree == expected


def test_big_rotate_right():
    expected = Tree(
        root=TreeNode(
            key=4,
            value=0,
            left=TreeNode(
                key=2,
                value=0,
                left=TreeNode(key=1, value=0, left=None, right=None, height=1),
                right=TreeNode(key=3, value=0, left=None, right=None, height=1),
                height=2,
            ),
            right=TreeNode(
                key=5,
                value=0,
                left=None,
                right=TreeNode(key=7, value=0, left=None, right=None, height=1),
                height=2,
            ),
            height=3,
        )
    )
    test_tree = Tree(
        root=TreeNode(
            key=5,
            value=0,
            left=TreeNode(
                key=2,
                value=0,
                left=TreeNode(key=1, value=0, left=None, right=None, height=1),
                right=TreeNode(
                    key=4,
                    value=0,
                    left=None,
                    right=None,
                    height=1,
                ),
                height=2,
            ),
            right=TreeNode(key=7, value=0, left=None, right=None, height=1),
            height=3,
        )
    )
    put(test_tree, 3, 0)
    assert test_tree == expected


def test_big_rotate_left():
    expected = Tree(
        root=TreeNode(
            key=30,
            value=0,
            left=TreeNode(
                key=20,
                value=0,
                left=TreeNode(key=10, value=0, left=None, right=None, height=1),
                right=TreeNode(key=25, value=0, left=None, right=None, height=1),
                height=2,
            ),
            right=TreeNode(
                key=40,
                value=0,
                left=None,
                right=TreeNode(key=50, value=0, left=None, right=None, height=1),
                height=2,
            ),
            height=3,
        )
    )
    test_tree = Tree(
        root=TreeNode(
            key=20,
            value=0,
            left=TreeNode(key=10, value=0, left=None, right=None, height=1),
            right=TreeNode(
                key=40,
                value=0,
                left=TreeNode(key=30, value=0, left=None, right=None, height=1),
                right=TreeNode(key=50, value=0, left=None, right=None, height=1),
                height=2,
            ),
            height=3,
        )
    )
    put(test_tree, 25, 0)
    assert test_tree == expected


def test_exception_in_remove(key1=212, key2=-1):
    with pytest.raises(ValueError, match="BST hasn't Node with this key"):
        remove(TEST_AVL_TREE, key1)
        remove(TEST_AVL_TREE, key2)


def test_exception_in_lower_and_upper_bound(key1=212, key2=17):
    with pytest.raises(ValueError, match="In the map there not key bigger than given"):
        get_upper_bound(TEST_AVL_TREE, key1)
        get_lower_bound(TEST_AVL_TREE, key2)


def test_create_avl_tree():
    assert type(create_tree_map()) == Tree


@pytest.mark.parametrize(
    "key, expected",
    (
        (13, True),
        (-2, False),
        (122, False),
    ),
)
def test_has_key(key, expected):
    assert has_key(TEST_AVL_TREE, key) == expected


@pytest.mark.parametrize(
    "key, expected",
    (
        (-5, [12, 2, 3]),
        (4, "ad"),
    ),
)
def test_get(key, expected):
    assert get(TEST_AVL_TREE, key) == expected


def test_put():
    bst = create_tree_map()
    put(bst, 1, 0)
    put(bst, 2, 0)
    put(bst, 3, 0)
    put(bst, 4, 0)
    put(bst, -4, 0)
    put(bst, 2.5, 0)
    assert traverse(bst, "in-order") == [-4, 1, 2, 2.5, 3, 4]


def test_general_behavior():
    new_test_tree = copy.deepcopy(TEST_AVL_TREE)
    put(new_test_tree, 4.5, "aboba")
    put(new_test_tree, -13, "aboba")
    flag1 = (
        True
        if traverse(new_test_tree, "pre-order")
        == [8, 3, 1, -5, -13, 2, 6, 4, 4.5, 7, 11, 9, 13, 15]
        else False
    )
    remove(new_test_tree, 11)
    remove(new_test_tree, 6)
    flag2 = (
        True
        if traverse(new_test_tree, "pre-order")
        == [7, 3, 1, -5, -13, 2, 4, 4.5, 9, 8, 13, 15]
        else False
    )
    flag3 = True if has_key(new_test_tree, 6) == False else True
    assert flag1 and flag2 and flag3


def test_remove_example():
    expected = Tree(
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
                key=13,
                value=3,
                left=TreeNode(key=9, value=5, left=None, right=None, height=1),
                right=TreeNode(key=15, value=(-12, 3), left=None, right=None, height=1),
                height=2,
            ),
            height=4,
        )
    )
    new_test_tree = copy.deepcopy(TEST_AVL_TREE)
    remove_value = remove(new_test_tree, 11)
    assert expected == new_test_tree and remove_value == "1"


def test_insert():
    expected = Tree(
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
                    left=TreeNode(key=12, value=12, left=None, right=None, height=1),
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
    new_test_tree = copy.deepcopy(TEST_AVL_TREE)
    assert expected.root == insert(new_test_tree.root, 12, 12)


def test_put(key1=212, key2=0, value1="212", value2=1412):
    ht = create_tree_map()
    put(ht, key1, value1)
    put(ht, key2, value2)
    assert (
        has_key(ht, key1)
        and has_key(ht, key2)
        and get(ht, key1) == value1
        and get(ht, key2) == value2
    )


@pytest.mark.parametrize(
    "order, expected",
    (
        ("pre-order", [8, 3, 1, -5, 2, 6, 4, 7, 11, 9, 13, 15]),
        ("in-order", [-5, 1, 2, 3, 4, 6, 7, 8, 9, 11, 13, 15]),
        ("post-order", [-5, 2, 1, 4, 7, 6, 3, 9, 15, 13, 11, 8]),
    ),
)
def test_traverse(order, expected):
    if order == "pre-order":
        assert traverse(TEST_AVL_TREE, "pre-order") == expected
    if order == "in-order":
        assert traverse(TEST_AVL_TREE, "in-order") == expected
    if order == "post-order":
        assert traverse(TEST_AVL_TREE, "post-order") == expected


def test_get_minimum_and_get_maximum():
    assert get_minimum(TEST_AVL_TREE) == -5 and get_maximum(TEST_AVL_TREE) == 15


@pytest.mark.parametrize(
    "given_value, expected",
    (
        (11, 13),
        (-11, -5),
        (4, 6),
        (10, 11),
    ),
)
def test_upper_bound(given_value, expected):
    assert get_upper_bound(TEST_AVL_TREE, given_value) == expected


@pytest.mark.parametrize(
    "given_value, expected",
    (
        (11, 11),
        (-1, 1),
        (12, 13),
        (5, 6),
    ),
)
def test_lower_bound(given_value, expected):
    assert get_lower_bound(TEST_AVL_TREE, given_value) == expected
