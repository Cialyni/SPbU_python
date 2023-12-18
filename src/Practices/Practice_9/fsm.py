from dataclasses import dataclass


@dataclass
class FSMachine:
    initial: None
    accepting: None
    transitions: None


def create_fs_machine(initial, accepting, transitions) -> FSMachine:
    return FSMachine(initial, accepting, transitions)


def parse_string_into_tokens(string: str) -> list:
    tokens = []
    for smb in string:
        if smb.isdigit():
            tokens.append("DIGIT")
        elif smb in "+-":
            tokens.append("SIGN")
        else:
            tokens.append(smb)
    return tokens


def validate_string(fsm: FSMachine, string: str) -> bool:
    tokens = parse_string_into_tokens(string)
    current_condition = fsm.initial
    for token in tokens:
        if token in fsm.transitions[current_condition]:
            current_condition = fsm.transitions[current_condition][token]
        else:
            return False
    return current_condition in fsm.accepting
