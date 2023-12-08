from FSM import validate_string, create_fs_machine


def main():
    string = input(
        "Enter a string to verify that it belongs to the language: (a|b)*abb\n"
    )
    fsm = create_fs_machine()
    if validate_string(fsm, string):
        print("This line belongs to the (a|b)*abb")
    else:
        print("This line does not belong to the (a|b)*abb")


if __name__ == "__main__":
    main()
