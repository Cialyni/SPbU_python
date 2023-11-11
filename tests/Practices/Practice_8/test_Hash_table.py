import pytest
from src.Practices.Practice_8.Hash_table import (
    Bucket,
    HashTable,
    put,
    get,
    has_key,
    remove,
    create_hash_table,
    items,
    Entry,
)

test_HashTable1 = HashTable(
    buckets=[
        Bucket(entries=[Entry(key="2", value='value for key "2"')]),
        Bucket(entries=[Entry(key=1, value=["1"])]),
        Bucket(entries=[]),
        Bucket(entries=[Entry(key=3, value="3")]),
        Bucket(
            entries=[
                Entry(key=4, value=44),
                Entry(key=-12, value=["value for key -12"]),
            ]
        ),
        Bucket(
            entries=[
                Entry(key=5, value="value for key 5"),
                Entry(key=-11, value="value for key -11"),
            ]
        ),
        Bucket(
            entries=[
                Entry(key=6, value="value for key = 6"),
                Entry(key=-10, value=["value for key -10"]),
            ]
        ),
        Bucket(entries=[Entry(key=7, value="value for key 7")]),
        Bucket(entries=[]),
        Bucket(entries=[Entry(key=9, value=9)]),
        Bucket(entries=[]),
        Bucket(entries=[]),
        Bucket(
            entries=[Entry(key="8", value=8), Entry(key="abababbabobabab", value=11)]
        ),
        Bucket(entries=[]),
        Bucket(entries=[Entry(key=14, value=["last value for key 14"])]),
        Bucket(entries=[]),
    ],
    total_buckets=16,
    size=14,
)

test_HashTable1_items = [
    (1, ["1"]),
    (3, "3"),
    (4, 44),
    (-12, ["value for key -12"]),
    (5, "value for key 5"),
    (-11, "value for key -11"),
    (6, "value for key = 6"),
    (-10, ["value for key -10"]),
    ("abababbabobabab", 11),
    (7, "value for key 7"),
    (9, 9),
    ("2", 'value for key "2"'),
    ("8", 8),
    (14, ["last value for key 14"]),
]


def test_exception_in_get(key1=212, key2="1412"):
    with pytest.raises(AttributeError, match="This key does not exist"):
        get(test_HashTable1, key1)
        get(test_HashTable1, key2)


def test_exception_in_remove(key1=212, key2="1412"):
    with pytest.raises(AttributeError, match="Removing key does not exist"):
        remove(test_HashTable1, key1)
        remove(test_HashTable1, key2)


def test_create_hash_table():
    assert type(create_hash_table()) == HashTable


@pytest.mark.parametrize(
    "key, expected",
    (
        (14, True),
        ("2", False),
        (122, False),
    ),
)
def test_has_key(key, expected):
    assert has_key(test_HashTable1, key) == expected


@pytest.mark.parametrize(
    "key, expected",
    (
        (14, ["last value for key 14"]),
        (9, 9),
    ),
)
def test_get(key, expected):
    assert get(test_HashTable1, key) == expected


def test_put(key1=212, key2="1412", value1="212", value2=1412):
    ht = create_hash_table()
    put(ht, key1, value1)
    put(ht, key2, value2)
    assert (
        has_key(ht, key1)
        and has_key(ht, key2)
        and get(ht, key1) == value1
        and get(ht, key2) == value2
    )


def test_items():
    check = True
    for entry in items(test_HashTable1):
        if not entry in test_HashTable1_items:
            check = False
    assert check == True
