import os, os.path
import sys
from collections import Counter, OrderedDict


def error_executor(file):
    if not os.path.isfile(file):
        raise FileExistsError("File f doesn't exist")


def file_to_sorted_dict(file_in):
    s = ""
    with open(file_in) as f_in:
        for line in f_in:
            s += line
    return OrderedDict(sorted(Counter(s).items()))


def dict_validater(dct):
    validate_dct = {}
    for i in dct:
        if i.isalpha():
            validate_dct[i] = dct[i]
    return validate_dct


def file_output(file_out, sort_dct):
    f_out = open(file_out, "w")
    output = ""
    for i in sort_dct:
        output += i + ": " + str(sort_dct[i]) + "\n"
    f_out.write(output)
    f_out.close()


if __name__ == "__main__":
    try:
        file_in, file_out = sys.argv[1], sys.argv[2]
        error_executor(file_in)
        char_dict = file_to_sorted_dict(file_in)
        char_dict = dict_validater(char_dict)
        file_output(file_out, char_dict)
        error_info = "Process was completed without errors"
    except FileExistsError:
        error_info = "File f doesn't exist"
    finally:
        print(error_info)
