from .fsm import validate_string, create_fs_machine


def main():
    string = input("Enter a string to verify that you belong to one of the languages\n")
    fsm_aboba = create_fs_machine(
        initial=0,
        accepting=[0, 4],
        transitions={
            0: {"a": 2, "b": 1},
            1: {"a": 2, "b": 1},
            2: {"a": 2, "b": 3},
            3: {"a": 2, "b": 4},
            4: {"a": 2, "b": 1},
        },
    )
    fsm_float = create_fs_machine(
        initial=0,
        accepting=[0, 1, 5],
        transitions={
            0: {"DIGIT": 1},
            1: {"DIGIT": 1, "E": 3, ".": 2},
            2: {"DIGIT": 1},
            3: {"DIGIT": 5, "SIGN": 4},
            4: {"DIGIT": 5},
            5: {"DIGIT": 5},
        },
    )
    if string == "":
        print("Еhe empty set is suitable for both languages")
        return
    if validate_string(fsm_aboba, string):
        print("This line belongs to the (a|b)*abb")
    elif validate_string(fsm_float, string):
        print("This line belongs to the digit+(.digit+)?(E(+|-)?digit+)?")
    else:
        print("This string does not belong to any of these languages")


if __name__ == "__main__":
    main()
