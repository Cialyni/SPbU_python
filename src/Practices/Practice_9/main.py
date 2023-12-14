from .fsm import validate_string, create_fs_machine


def main():
    string = input(
        "Enter a string to verify that it belongs to the language: (a|b)*abb\n"
    )
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
    if validate_string(fsm, string):
        print("This line belongs to the (a|b)*abb")
    else:
        print("This line does not belong to the (a|b)*abb")


if __name__ == "__main__":
    main()
