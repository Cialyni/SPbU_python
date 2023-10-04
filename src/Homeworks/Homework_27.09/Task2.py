import os
import sys


def input_parser():
    file_txt = sys.argv[1]
    file_csv = sys.argv[2]
    script_path = os.path.dirname(__file__)
    return os.path.join(script_path, file_txt), os.path.join(script_path, file_csv)


def frequency_find(file_txt):
    word_dict = {}
    with open(file_txt) as f_in:
        for line in f_in:
            word_lst = line.split()
            for word in word_lst:
                word_dict = word_dict.get(word, 0) + 1
    return word_dict


def frequency_record(file_csv, frequency_dict):
    file = open(file_csv, "w")
    for elem in frequency_dict:
        file.write(str(elem) + " " + str(frequency_dict[elem]) + "\n")
    file.close()


if __name__ == "__main__":
    input_parser()
    file_txt_path, file_csv_path = input_parser()
    frequency_dict = frequency_find(file_txt_path)
    frequency_record(file_csv_path, frequency_dict)
