import os
import sys
import re


def input_parser():
    file_input_name = sys.argv[1]
    file_output_name = sys.argv[2]
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, file_input_name), os.path.join(script_dir, file_output_name)


def command_parser(s):
    return list(filter(None, s.replace('[', ']').split(']')))


def DELETE(dnk, start, end):
    ind_s = dnk.find(start)
    ind_e = dnk.find(end) + len(end)
    if start in dnk:
        dnk = dnk[:ind_s] + dnk[ind_e:]
    return dnk


def REPLACE(dnk, template, fragment):
    dnk = dnk.replace(template, fragment, 1)
    return dnk


def INSERT(dnk, start, fragment):
    ind = dnk.find(start) + len(start)
    if start in dnk:
        dnk = dnk[:ind] + fragment + dnk[ind:]
    return dnk


def executor(command_lst, dnk):
    if command_lst[0] == 'INSERT':
        start = command_lst[1]
        fragment = command_lst[2]
        dnk = INSERT(dnk, start, fragment)
    if command_lst[0] == 'DELETE':
        start = command_lst[1]
        end = command_lst[2]
        dnk = DELETE(dnk, start, end)
    if command_lst[0] == 'REPLACE':
        template = command_lst[1]
        fragment = command_lst[2]
        dnk = REPLACE(dnk, template, fragment)
    return dnk


def rebuild_dnk(file_input_path):
    n, m = 0, 0
    dnk = ''
    file_output = open(file_output_path, 'w')
    with open(file_input_path) as f_in:
        for i, line in enumerate(f_in):
            if i == 0:
                n = int(line)
            if i == 1:
                dnk = line
            if i == 2:
                m = int(line)
            if i >= 3:
                command_lst = command_parser(line)
                dnk = executor(command_lst, dnk)
                file_output.writelines('DNK after changes: ' + dnk)


if __name__ == "__main__":
    input_parser()
    file_input_path, file_output_path = input_parser()
    rebuild_dnk(file_input_path)
