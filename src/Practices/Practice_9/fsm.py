from dataclasses import dataclass


@dataclass
class FSMachine:
    initial: None
    accepting: None
    transitions: None


def create_fs_machine(initial, accepting, transitions) -> FSMachine:
    return FSMachine(initial, accepting, transitions)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_condition = fsm.initial
    for token in string:
        if token in fsm.transitions[current_condition]:
            current_condition = fsm.transitions[current_condition][token]
        else:
            return False
    return current_condition in fsm.accepting
