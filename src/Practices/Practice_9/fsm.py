from dataclasses import dataclass


@dataclass
class FSMachine:
    language_name: str
    initial: int
    accepting: tuple
    transitions: {int: dict}


def create_fs_machine(language_name, initial, accepting, transitions) -> FSMachine:
    return FSMachine(language_name, initial, accepting, transitions)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_condition = fsm.initial
    for token in string:
        flag = False
        for transition in fsm.transitions[current_condition].keys():
            if token in transition:
                current_condition = fsm.transitions[current_condition][transition]
                flag = True
        if not flag:
            return False

    return current_condition in fsm.accepting


def give_message_about_string(fsm_lst: list[FSMachine], string: str):
    flag = False
    if string == "":
        print("Еhe empty set is suitable for both languages")
        return
    for fsm in fsm_lst:
        if validate_string(fsm, string):
            print("This string belong to the", fsm.language_name)
            flag = True
    if not flag:
        print("This string does not belong to the any of given languages")
