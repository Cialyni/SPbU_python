from dataclasses import dataclass
from typing import Any


@dataclass
class FSMachine:
    initial: int
    accepting: list[int]
    transitions: dict[int, dict[Any, int]]


def create_fs_machine(initial, accepting, transitions) -> FSMachine:
    return FSMachine(initial, accepting, transitions)


def create_aboba_fs_machine():
    fsm = create_fs_machine(
        initial=0,
        accepting=[
            3,
        ],
        transitions={
            0: {"a": 1, "b": 0},
            1: {"a": 1, "b": 2},
            2: {"a": 1, "b": 3},
            3: {"a": 1, "b": 0},
        },
    )
    return fsm


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_condition = fsm.initial
    for token in string:
        if token in fsm.transitions[current_condition]:
            current_condition = fsm.transitions[current_condition][token]
        else:
            return False
    return current_condition in fsm.accepting
