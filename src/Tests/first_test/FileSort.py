import os, os.path
import sys


def input_parser():
    a, b = int(sys.argv[1]), int(sys.argv[2])
    file_f, file_g = sys.argv[3], sys.argv[4]
    script_path = os.path.dirname(__file__)
    return a, b, os.path.join(script_path, file_f), os.path.join(script_path, file_g)


def error_executor(f, g):
    if not os.path.isfile(file_f):
        print("File f doesn't exist")
        sys.exit()
    if os.path.isfile(file_g):
        print("File g already exist")
        sys.exit()


def file_sorter(a, b, file_f):
    sorted_file_data = [[], [], []]
    with open(file_f) as f_in:
        for line in f_in:
            for number in line.split():
                if int(number) < a:
                    sorted_file_data[0].append(number)
                elif a <= int(number) <= b:
                    sorted_file_data[1].append(number)
                else:
                    sorted_file_data[2].append(number)
    return sorted_file_data


def output_file(lst, file):
    g = open(file, "w")
    for i in range(3):
        for elem in lst[i]:
            g.write(elem + " ")
        g.write("\n")
    g.close()


if __name__ == "__main__":
    a, b, file_f, file_g = input_parser()
    error_executor(file_f, file_g)
    sorted_file_data = file_sorter(a, b, file_f)
    output_file(sorted_file_data, file_g)
