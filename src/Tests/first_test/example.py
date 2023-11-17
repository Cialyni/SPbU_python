from Deque import (
    MyDeque,
    Node,
    create,
    tail,
    pushBack,
    pushFront,
    delete,
    print_deq,
    size,
    head,
    popFront,
    popBack,
    is_empty,
)

deq = create()
pushBack(deq, 10)  # 10
pushFront(deq, 1)  # 1 10
pushFront(deq, 3)  # 3 1 10
pushBack(deq, 11)  # 2 3 1 10 11
pushFront(deq, 2)  # 2 3 1 10
pushBack(deq, -12)  # 2 3 1 10 11 -12
print_deq(deq)
print(tail(deq))  # -12
print(head(deq))  # 2
print(size(deq))  # 6
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
