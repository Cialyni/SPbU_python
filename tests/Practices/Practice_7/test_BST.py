import pytest
from src.Practices.Practice_7.BST import (
    TreeNode,
    Tree,
    put,
    get,
    has_key,
    remove,
    traverse,
)


def test_get(
    map=Tree(
        root=TreeNode(
            key=10,
            value=10,
            left=TreeNode(key=4, value=4, left=None, right=None),
            right=TreeNode(
                key=16,
                value=16,
                left=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(key=11, value=11, left=None, right=None),
                    right=None,
                ),
                right=TreeNode(
                    key=18,
                    value=18,
                    left=TreeNode(key=17, value=17, left=None, right=None),
                    right=TreeNode(key=19, value=19, left=None, right=None),
                ),
            ),
        ),
        size=8,
    ),
    key=18,
    expected=18,
):
    actual = get(map, key)
    assert actual == expected


def test_exception_in_get(
    map=Tree(
        root=TreeNode(
            key=10,
            value=10,
            left=TreeNode(key=4, value=4, left=None, right=None),
            right=TreeNode(
                key=16,
                value=16,
                left=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(key=11, value=11, left=None, right=None),
                    right=None,
                ),
                right=TreeNode(
                    key=18,
                    value=18,
                    left=TreeNode(key=17, value=17, left=None, right=None),
                    right=TreeNode(key=19, value=19, left=None, right=None),
                ),
            ),
        ),
        size=8,
    ),
    key=123,
):
    with pytest.raises(AttributeError, match="BST hasn't Node with this key"):
        get(map, key)


@pytest.mark.parametrize(
    "map, key, expected",
    (
        (
            Tree(
                root=TreeNode(
                    key=10,
                    value=10,
                    left=TreeNode(key=4, value=4, left=None, right=None),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=14,
                            value=14,
                            left=TreeNode(key=11, value=11, left=None, right=None),
                            right=None,
                        ),
                        right=TreeNode(
                            key=18,
                            value=18,
                            left=TreeNode(key=17, value=17, left=None, right=None),
                            right=TreeNode(key=19, value=19, left=None, right=None),
                        ),
                    ),
                ),
                size=8,
            ),
            15,
            False,
        ),
        (
            Tree(
                root=TreeNode(
                    key=10,
                    value=10,
                    left=TreeNode(key=4, value=4, left=None, right=None),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=14,
                            value=14,
                            left=TreeNode(key=11, value=11, left=None, right=None),
                            right=None,
                        ),
                        right=TreeNode(
                            key=18,
                            value=18,
                            left=TreeNode(key=17, value=17, left=None, right=None),
                            right=TreeNode(key=19, value=19, left=None, right=None),
                        ),
                    ),
                ),
                size=8,
            ),
            18,
            True,
        ),
    ),
)
def test_has(map, key, expected):
    assert has_key(map, key) == expected


def test_exception_in_remove(
    map=Tree(
        root=TreeNode(
            key=10,
            value=10,
            left=TreeNode(key=4, value=4, left=None, right=None),
            right=TreeNode(
                key=16,
                value=16,
                left=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(key=11, value=11, left=None, right=None),
                    right=None,
                ),
                right=TreeNode(
                    key=18,
                    value=18,
                    left=TreeNode(key=17, value=17, left=None, right=None),
                    right=TreeNode(key=19, value=19, left=None, right=None),
                ),
            ),
        ),
        size=8,
    ),
    key=123,
):
    with pytest.raises(AttributeError, match="BST hasn't Node with this key"):
        remove(map, key)


@pytest.mark.parametrize(
    "map, order, expected",
    (
        (
            Tree(
                root=TreeNode(
                    key=10,
                    value=10,
                    left=TreeNode(key=4, value=4, left=None, right=None),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=14,
                            value=14,
                            left=TreeNode(key=11, value=11, left=None, right=None),
                            right=None,
                        ),
                        right=TreeNode(
                            key=18,
                            value=18,
                            left=TreeNode(key=17, value=17, left=None, right=None),
                            right=TreeNode(key=19, value=19, left=None, right=None),
                        ),
                    ),
                ),
                size=8,
            ),
            "pre-order",
            [
                [10, 10],
                [4, 4],
                [16, 16],
                [14, 14],
                [11, 11],
                [18, 18],
                [17, 17],
                [19, 19],
            ],
        ),
        (
            Tree(
                root=TreeNode(
                    key=10,
                    value=10,
                    left=TreeNode(key=4, value=4, left=None, right=None),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=14,
                            value=14,
                            left=TreeNode(key=11, value=11, left=None, right=None),
                            right=None,
                        ),
                        right=TreeNode(
                            key=18,
                            value=18,
                            left=TreeNode(key=17, value=17, left=None, right=None),
                            right=TreeNode(key=19, value=19, left=None, right=None),
                        ),
                    ),
                ),
                size=8,
            ),
            "in-order",
            [
                [4, 4],
                [10, 10],
                [11, 11],
                [14, 14],
                [16, 16],
                [17, 17],
                [18, 18],
                [19, 19],
            ],
        ),
        (
            Tree(
                root=TreeNode(
                    key=10,
                    value=10,
                    left=TreeNode(key=4, value=4, left=None, right=None),
                    right=TreeNode(
                        key=16,
                        value=16,
                        left=TreeNode(
                            key=14,
                            value=14,
                            left=TreeNode(key=11, value=11, left=None, right=None),
                            right=None,
                        ),
                        right=TreeNode(
                            key=18,
                            value=18,
                            left=TreeNode(key=17, value=17, left=None, right=None),
                            right=TreeNode(key=19, value=19, left=None, right=None),
                        ),
                    ),
                ),
                size=8,
            ),
            "post-order",
            [
                [4, 4],
                [11, 11],
                [14, 14],
                [17, 17],
                [19, 19],
                [18, 18],
                [16, 16],
                [10, 10],
            ],
        ),
    ),
)
def test_traverse(map, order, expected):
    actual = traverse(map, order)
    assert actual == expected


def test_remove(
    map=Tree(
        root=TreeNode(
            key=10,
            value=10,
            left=TreeNode(key=4, value=4, left=None, right=None),
            right=TreeNode(
                key=16,
                value=16,
                left=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(key=11, value=11, left=None, right=None),
                    right=None,
                ),
                right=TreeNode(
                    key=18,
                    value=18,
                    left=TreeNode(key=17, value=17, left=None, right=None),
                    right=TreeNode(key=19, value=19, left=None, right=None),
                ),
            ),
        ),
        size=8,
    ),
    key=16,
    expected=[[10, 10], [4, 4], [17, 17], [14, 14], [11, 11], [18, 18], [19, 19]],
):
    remove(map, key)
    actual_lst = traverse(map, "pre-order")
    assert actual_lst == expected


def test_put(
    map=Tree(
        root=TreeNode(
            key=10,
            value=10,
            left=TreeNode(key=4, value=4, left=None, right=None),
            right=TreeNode(
                key=16,
                value=16,
                left=TreeNode(
                    key=14,
                    value=14,
                    left=TreeNode(key=11, value=11, left=None, right=None),
                    right=None,
                ),
                right=TreeNode(
                    key=18,
                    value=18,
                    left=TreeNode(key=17, value=17, left=None, right=None),
                    right=TreeNode(key=19, value=19, left=None, right=None),
                ),
            ),
        ),
        size=8,
    ),
    key=100,
    value=100,
    expected=[
        [10, 10],
        [4, 4],
        [16, 16],
        [14, 14],
        [11, 11],
        [18, 18],
        [17, 17],
        [19, 19],
        [100, 100],
    ],
):
    put(map, key, value)
    actual_lst = traverse(map, "pre-order")
    assert actual_lst == expected
