from typing import TypeVar, Generic, Tuple, Any, NamedTuple
from dataclasses import dataclass

DEFAULT_HASH_TABLE_SIZE = 8
Entry = NamedTuple("Entry", [("key", Any), ("value", Any)])


@dataclass
class Bucket:
    entries: list[Entry]


@dataclass
class HashTable:
    buckets: list[Bucket | None]
    total_buckets: int = DEFAULT_HASH_TABLE_SIZE
    size: int = 0


def _hash(item: Any, hash_table: HashTable) -> int:
    return hash(item) % hash_table.total_buckets


def create_hash_table(n=DEFAULT_HASH_TABLE_SIZE) -> HashTable:
    return HashTable([Bucket([]) for i in range(n)], n)


def delete_hash_table(hash_table: HashTable):
    while hash_table.total_buckets > 0:
        hash_table.total_buckets -= 1
        del hash_table.buckets[0]
    del hash_table


def hash_table_resize(hash_table: HashTable):
    new_hash_table = create_hash_table(n=hash_table.total_buckets * 2)
    item_lst = items(hash_table)
    for key_value in item_lst:
        put(new_hash_table, key_value[0], key_value[1])
    hash_table.size, hash_table.total_buckets, hash_table.buckets = (
        new_hash_table.size,
        new_hash_table.total_buckets,
        new_hash_table.buckets.copy(),
    )
    delete_hash_table(new_hash_table)


def _get_node_from_bucket(bucket: list[Entry], key: Any) -> Entry | None:
    for entry in bucket:
        if entry.key == key:
            return entry
    return None


def put(hash_table: HashTable, key: Any, value: Any):
    if (hash_table.size / hash_table.total_buckets) >= 1:
        hash_table_resize(hash_table)
    hash_id = _hash(key, hash_table)
    if hash_table.buckets[hash_id] is None:
        hash_table.buckets[hash_id].entries.append(Entry(key, value))
        hash_table.size += 1
    else:
        old_entry = _get_node_from_bucket(hash_table.buckets[hash_id].entries, key)
        if old_entry is None:
            hash_table.buckets[hash_id].entries.append(Entry(key, value))
            hash_table.size += 1
        else:
            hash_table.buckets[hash_id].entries.remove(old_entry)
            hash_table.buckets[hash_id].entries.append(Entry(key, value))


def get(hash_table: HashTable, key: Any) -> Any:
    if not has_key(hash_table, key):
        raise AttributeError("This key does not exist")
    hash_id = _hash(key, hash_table)
    get_entry_from_bucket = _get_node_from_bucket(
        hash_table.buckets[hash_id].entries, key
    )
    return get_entry_from_bucket.value


def has_key(hash_table: HashTable, key: Any) -> bool:
    hash_id = _hash(key, hash_table)
    get_entry_from_bucket = _get_node_from_bucket(
        hash_table.buckets[hash_id].entries, key
    )
    if get_entry_from_bucket is None:
        return False
    return True


def items(hash_table: HashTable) -> list[tuple[Any, Any]]:
    lst_items = []
    for bucket in hash_table.buckets:
        if bucket.entries:
            for key_value in bucket.entries:
                lst_items.append((key_value[0], key_value[1]))
    return lst_items


def remove(hash_table: HashTable, key: Any) -> Any:
    if not has_key(hash_table, key):
        raise AttributeError("Removing key does not exist")
    hash_id = _hash(key, hash_table)
    get_entry_from_bucket = _get_node_from_bucket(
        hash_table.buckets[hash_id].entries, key
    )
    hash_table.buckets[hash_id].entries.remove(get_entry_from_bucket)
    hash_table.size -= 1
    return get_entry_from_bucket.value


if __name__ == "__main__":
    ht = create_hash_table()
    put(ht, 1, ["1"])
    put(ht, "2", 'value for key "2"')
    put(ht, 3, "3")
    put(ht, 4, 44)
    put(ht, 5, "value for key 5")
    put(ht, 6, ("value for key = 6"))
    put(ht, 7, "value for key 7")
    put(ht, "8", 8)
    put(ht, 9, 9)
    put(ht, -10, ["value for key -10"])
    put(ht, -11, "value for key -11")
    put(ht, -12, ["value for key -12"])
    put(ht, 14, ["first value for key 14"])
    put(ht, 14, ["second value for key 14"])
    put(ht, 14, ["third value for key 14"])
    put(ht, 14, ["last value for key 14"])
    put(ht, "abababbabobabab", 11)

    lst = items(ht)
    print("le")
