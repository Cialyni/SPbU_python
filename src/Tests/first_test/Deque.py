from dataclasses import dataclass
import os, sys
from typing import Any


@dataclass
class Node:
    value: None
    next: None
    prev: None


@dataclass
class MyDeque:
    head: Node = None
    len: int = 0


def create():
    return MyDeque


def delete(deq: MyDeque):
    while not deq.head.value is None:
        del deq.head.prev
        deq.head = deq.head.next
    del deq


def tail(deq: MyDeque) -> Any:
    cur_node = deq.head
    while not cur_node.next is None:
        cur_node = cur_node.next
    return cur_node.value


def head(deq: MyDeque) -> Any:
    return deq.head.value


def size(deq: MyDeque) -> int:
    return deq.len


def is_empty(deq: MyDeque) -> bool:
    return deq.len == 0


def go_to_head(deq: MyDeque):
    cur_node = deq.head
    while not cur_node.prev is None:
        cur_node = cur_node.prev
    deq.head = cur_node


def pushFront(deq: MyDeque, element: Any):
    new_node = Node(prev=None, value=element, next=deq.head)
    if deq.len != 0:
        new_node.next.prev = new_node
    deq.head = new_node
    deq.len += 1


def pushBack(deq: MyDeque, element: Any):
    if deq.len == 0:
        pushFront(deq, element)
        return
    cur_node = deq.head
    while not cur_node.next is None:
        cur_node = cur_node.next
    new_node = Node(prev=cur_node, value=element, next=None)
    new_node.prev.next = new_node
    deq.head = new_node
    go_to_head(deq)
    deq.len += 1


def popFront(deq: MyDeque) -> Any:
    if deq.len == 1:
        return_element = deq.head.value
        deq.head = None
        deq.len -= 1
        return return_element
    return_element = deq.head.value
    new_node = deq.head.next
    new_node.prev = None
    deq.head = new_node
    deq.len -= 1
    return return_element


def popBack(deq: MyDeque) -> Any:
    if deq.len == 1:
        return_element = deq.head.value
        deq.head = None
        deq.len -= 1
        return return_element
    cur_node = deq.head
    while not cur_node.next is None:
        cur_node = cur_node.next
    return_element = cur_node.value
    cur_node.prev.next = None
    deq.head = cur_node
    go_to_head(deq)
    deq.len -= 1
    return return_element


def print_deq(deq: MyDeque):
    cur_node = deq.head
    while not cur_node.next is None:
        print(cur_node.value, end=" ")
        cur_node = cur_node.next
    print(cur_node.value)


if __name__ == "__main__":
    deq = create()
    pushBack(deq, 10)  # 10
    pushFront(deq, 1)  # 1 10
    pushFront(deq, 3)  # 3 1 10
    pushBack(deq, 11)  # 2 3 1 10 11
    pushFront(deq, 2)  # 2 3 1 10
    pushBack(deq, -12)  # 2 3 1 10 11 -12
    print_deq(deq)  # 6
    print(size(deq))
    print(popFront(deq))  # 2
    print(popBack(deq))  # -12
    print(popBack(deq))  # 11
    print_deq(deq)
    print(size(deq))  # 3
    print(is_empty(deq))  # False
    popBack(deq)
    popFront(deq)
    popBack(deq)
    print(is_empty(deq))  # True
