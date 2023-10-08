import os
import sys


def input_parser():
    file_input_name = sys.argv[1]
    file_output_name = sys.argv[2]
    script_path = os.path.dirname(__file__)
    return os.path.join(script_path, file_input_name), os.path.join(
        script_path, file_output_name
    )


def command_parser(s):
    return list(s.replace("[", "").replace("]", "").split(" "))


def delete(dnk, start, end):
    ind_s = dnk.find(start)
    ind_e = dnk.find(end) + len(end)
    if ind_s != -1:
        dnk = dnk[:ind_s] + dnk[ind_e:]
    return dnk


def replace(dnk, template, fragment):
    dnk = dnk.replace(template, fragment, 1)
    return dnk


def insert(dnk, start, fragment):
    ind = dnk.find(start) + len(start)
    if ind != len(start) - 1:
        dnk = dnk[:ind] + fragment + dnk[ind:]
    return dnk


def executor(command_lst, dnk):
    command = command_lst[0]
    arg1, arg2 = command_lst[1], command_lst[2].replace("\n", "")
    if command == "INSERT":
        start = arg1
        fragment = arg2
        dnk = insert(dnk, start, fragment)
    if command == "DELETE":
        start = arg1
        end = arg2
        dnk = delete(dnk, start, end)
    if command == "REPLACE":
        template = arg1
        fragment = arg2
        dnk = replace(dnk, template, fragment)
    return dnk


def rebuild_dnk(file_input_path, file_output_path):
    dnk = ""
    file_output = open(file_output_path, "w")
    with open(file_input_path) as f_in:
        for i, line in enumerate(f_in):
            if i == 0 or i == 2:
                pass
            if i == 1:
                dnk = line
            if i >= 3:
                command_lst = command_parser(line)
                dnk = executor(command_lst, dnk)
                file_output.writelines("DNK after changes: " + dnk)
    file_output.close()


if __name__ == "__main__":
    file_input_path, file_output_path = input_parser()
    rebuild_dnk(file_input_path, file_output_path)
