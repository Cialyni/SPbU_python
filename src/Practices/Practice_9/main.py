from src.Practices.Practice_9.fsm import (
    create_fs_machine,
    give_message_about_string,
    create_aboba_fs_machine,
    create_float_fs_machine,
)
import string


def main():
    line = input("Enter a string to verify that you belong to one of the languages\n")
    fsm_aboba = create_aboba_fs_machine()
    fsm_float = create_float_fs_machine()
    print(give_message_about_string([fsm_aboba, fsm_float], line), end='')


if __name__ == "__main__":
    main()
