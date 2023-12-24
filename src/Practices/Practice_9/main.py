from .fsm import (
    create_fs_machine,
    give_message_about_string,
)
import string


def main():
    line = input("Enter a string to verify that you belong to one of the languages\n")
    fsm_aboba = create_fs_machine(
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
    fsm_float = create_fs_machine(
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
    give_message_about_string([fsm_aboba, fsm_float], line)


if __name__ == "__main__":
    main()
