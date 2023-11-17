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
    current: Node = None
    len: int = 0


def create():
    return MyDeque


def delete(deq: MyDeque):
    while not deq.current.value is None:
        del deq.current.prev
        deq.current = deq.current.next
    del deq


def tail(deq: MyDeque) -> Any:
    go_to_tail(deq)
    return deq.current.value


def head(deq: MyDeque) -> Any:
    go_to_head(deq)
    return deq.current.value


def size(deq: MyDeque) -> int:
    return deq.len


def is_empty(deq: MyDeque) -> bool:
    return deq.len == 0


def go_to_head(deq: MyDeque):
    if deq.len > 1:
        cur_node = deq.current
        while not cur_node.prev is None:
            cur_node = cur_node.prev
        deq.current = cur_node


def go_to_tail(deq: MyDeque):
    if deq.len > 1:
        cur_node = deq.current
        while not cur_node.next is None:
            cur_node = cur_node.next
        deq.current = cur_node


def pushFront(deq: MyDeque, element: Any):
    go_to_head(deq)
    new_node = Node(prev=None, value=element, next=deq.current)
    if deq.len != 0:
        new_node.next.prev = new_node
    deq.current = new_node
    deq.len += 1


def pushBack(deq: MyDeque, element: Any):
    if deq.len == 0:
        pushFront(deq, element)
        return
    go_to_tail(deq)
    new_node = Node(prev=deq.current, value=element, next=None)
    new_node.prev.next = new_node
    deq.current = new_node
    deq.len += 1


def popFront(deq: MyDeque) -> Any:
    if deq.len == 1:
        return_element = deq.current.value
        deq.current = None
        deq.len -= 1
        return return_element
    if deq.len == 0:
        raise AttributeError("Nothing to remove")
    go_to_head(deq)
    return_element = deq.current.value
    new_node = deq.current.next
    new_node.prev = None
    deq.current = new_node
    deq.len -= 1
    return return_element


def popBack(deq: MyDeque) -> Any:
    if deq.len == 1:
        return_element = deq.current.value
        deq.current = None
        deq.len -= 1
        return return_element
    if deq.len == 0:
        raise AttributeError("Nothing to remove")
    go_to_tail(deq)
    return_element = deq.current.value
    deq.current.prev.next = None
    deq.current = deq.current.prev
    deq.len -= 1
    return return_element


def print_deq(deq: MyDeque):
    go_to_head(deq)
    cur_node = deq.current
    while not cur_node.next is None:
        print(cur_node.value, end=" ")
        cur_node = cur_node.next
    print(cur_node.value)
