from dataclasses import dataclass
import string
from typing import Any


@dataclass
class FSMachine:
    language_name: str
    initial: int
    accepting: tuple[int]
    transitions: dict[int, dict[Any, int]]


def create_fs_machine(language_name, initial, accepting, transitions) -> FSMachine:
    return FSMachine(language_name, initial, accepting, transitions)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_condition = fsm.initial
    for token in string:
        for transition in fsm.transitions[current_condition].keys():
            if token in transition:
                current_condition = fsm.transitions[current_condition][transition]
                break
        else:
            return False

    return current_condition in fsm.accepting


def create_aboba_fs_machine():
    FSM_aboba = create_fs_machine(
        language_name="(a|b)*abb",
        initial=0,
        accepting=(0, 4),
        transitions={
            0: {"a": 2, "b": 1},
            1: {"a": 2, "b": 1},
            2: {"a": 2, "b": 3},
            3: {"a": 2, "b": 4},
            4: {"a": 2, "b": 1},
        },
    )
    return FSM_aboba


def create_float_fs_machine():
    FSM_float = create_fs_machine(
        language_name="digit+(.digit+)?(E(+|-)?digit+)?",
        initial=0,
        accepting=(0, 1, 5),
        transitions={
            0: {string.digits: 1},
            1: {string.digits: 1, "E": 3, ".": 2},
            2: {string.digits: 1},
            3: {string.digits: 5, "+-": 4},
            4: {string.digits: 5},
            5: {string.digits: 5},
        },
    )
    return FSM_float


def give_message_about_string(fsm_lst: list[FSMachine], string: str):
    output_str = ""
    if string == "":
        return "Еhe empty set is suitable for all languages\n"
    for fsm in fsm_lst:
        if validate_string(fsm, string):
            output_str += "This string belong to the " + fsm.language_name + "\n"
    if not output_str:
        return "This string does not belong to the any of given languages\n"
    return output_str
