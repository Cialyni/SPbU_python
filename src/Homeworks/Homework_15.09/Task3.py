import sys
import os


def parcer(sys_args):
    command = ""
    command_X = 0
    for i, elem in enumerate(sys_args):
        if elem == "-m" or elem == "bash":
            continue
        if elem == "wc":
            if sys.argv[i + 1] == "-c":
                command = "wc_c"
            if sys.argv[i + 1] == "-l":
                command = "wc_l"
            if sys.argv[i + 1] == "-w":
                command = "wc_w"
            if sys.argv[i + 1] == "-m":
                command = "wc_m"
        if elem == "head":
            if sys.argv[i + 1] == "-n":
                command = "head_n"
                command_X = sys.argv[i + 2]
            if sys.argv[i + 1] == "-c":
                command = "head_c"
                command_X = sys.argv[i + 2]
        if elem == "tail":
            if sys.argv[i + 1] == "-n":
                command = "tail_n"
                command_X = sys.argv[i + 2]
            if sys.argv[i + 1] == "-c":
                command = "tail_c"
                command_X = sys.argv[i + 2]
    return sys_args[-1], command, int(command_X)


def wc(command, file_path, file_name):
    if command == "wc_c":
        print("wc -c {}: {}".format(file_name, os.path.getsize(file_path)))
    else:
        with open(file_path) as infile:
            lines = 0
            words = 0
            characters = 0
            for line in infile:
                wordslist = line.split()
                lines = lines + 1
                words = words + len(wordslist)
                characters += sum(len(word) for word in wordslist)
        if command == "wc_m":
            print("wc -m {}: {}".format(file_name, characters))
        if command == "wc_l":
            print("wc -m {}: {}".format(file_name, lines))
        if command == "wc_w":
            print("wc -m {}: {}".format(file_name, words))


def head(command, command_X, file_path, file_name):
    if command == "head_n":
        with open(file_path) as infile:
            for i, line in enumerate(infile):
                if i < command_X:
                    print(line, end="")
                else:
                    return
    if command == "head_c":
        byte_counter = 0
        with open(file_path) as infile:
            for line in infile:
                for elem in line:
                    if byte_counter >= command_X:
                        return
                    print(elem, end="")
                    byte_counter += 1


def tail(command, command_X, file_path, file_name):
    if command == "tail_n":
        with open(file_path) as infile:
            info = infile.read()[::-1]
            for i, line in enumerate(info):
                if i <= command_X + 1:
                    print(line, end="")
                else:
                    return
    if command == "tail_c":
        byte_counter = 1
        with open(file_path) as infile:
            info = infile.read()[::-1]
            for line in info:
                for elem in line:
                    if byte_counter >= command_X:
                        return
                    print(elem, end="")
                    byte_counter += 1


if __name__ == "__main__":
    file_name, command, command_X = parcer(sys.argv)
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    file_path = os.path.join(script_dir, file_name)
    if command in "wc_c wc_l wc_w wc_m":
        wc(command, file_path, file_name)
    if command in "head_n head_c":
        head(command, command_X, file_path, file_name)
    if command in "tail_n tail_c":
        tail(command, command_X, file_path, file_name)
