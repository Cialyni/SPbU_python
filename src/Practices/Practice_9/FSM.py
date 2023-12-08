from dataclasses import dataclass
from typing import Any


@dataclass
class FSMachine:
    initial: Any
    accepting: list[Any]
    transformation: dict
    alphabet: Any


def create_fs_machine() -> FSMachine:
    initial = 0
    accepting = [
        3,
    ]
    transitions = {
        0: {"a": 1, "b": 0},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"a": 1, "b": 0},
    }
    alphabet = "ab"
    return FSMachine(initial, accepting, transitions, alphabet)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_condition = fsm.initial
    for token in string:
        if token in fsm.transformation[current_condition]:
            current_condition = fsm.transformation[current_condition][token]
        else:
            return False
    return current_condition in fsm.accepting
