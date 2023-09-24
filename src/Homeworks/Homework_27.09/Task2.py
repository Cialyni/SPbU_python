import os
import sys


def input_parser():
    print(sys.argv)
    file_txt_name = sys.argv[1]
    file_csv_name = sys.argv[2]
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, file_txt_name), os.path.join(script_dir, file_csv_name)


def frequency_find(file_txt_path):
    word_dict = {}
    with open(file_txt_path) as f_in:
        for line in f_in:
            word_lst = line.split()
            for word in word_lst:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


def frequency_record(file_csv_path, frequency_dict):
    file = open(file_csv_path, 'w')
    for elem in frequency_dict:
        file.write(str(elem) + ' ' + str(frequency_dict[elem]) + '\n')


if __name__ == "__main__":
    input_parser()
    file_txt_path, file_csv_path = input_parser()
    frequency_dict = frequency_find(file_txt_path)
    frequency_record(file_csv_path, frequency_dict)
