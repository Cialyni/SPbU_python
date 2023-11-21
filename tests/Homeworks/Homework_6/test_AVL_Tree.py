import pytest
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
    with pytest.raises(AttributeError, match="BST hasn't Node with this key"):
        get(TEST_AVL_TREE, key1)
        get(TEST_AVL_TREE, key2)


def test_exception_in_remove(key1=212, key2=-1):
    with pytest.raises(AttributeError, match="BST hasn't Node with this key"):
        remove(TEST_AVL_TREE, key1)
        remove(TEST_AVL_TREE, key2)


def test_exception_in_lower_and_upper_bound(key1=212, key2=17):
    with pytest.raises(AttributeError):
        get_upper_bound(TEST_AVL_TREE, key1)
        get_lower_bound(TEST_AVL_TREE, key2)


def test_create_hash_table():
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
