from AVL_Tree import (
    Tree,
    create_tree_map,
    has_key,
    get,
    put,
    remove,
    traverse,
    get_lower_bound,
)
import argparse


def add_size_count(map: Tree, size: int, count: int) -> ():
    if has_key(map, size):
        old_count = get(map, size)
        put(map, size, count + old_count)
    else:
        put(map, size, count)


def get_size(map: Tree, size: int, file) -> ():
    try:
        file.write(str(get(map, size)) + "\n")
    except AttributeError:
        file.write("0" + "\n")


def select_size(map: Tree, size: int, file):
    try:
        needed_size = get_lower_bound(map, size)
        needed_size_count = get(map, needed_size)
        if needed_size_count == 1:
            remove(map, needed_size)
            file.write(str(needed_size) + "\n")
        else:
            put(map, needed_size, needed_size_count - 1)
            file.write(str(needed_size) + "\n")
    except AttributeError:
        file.write("SORRY" + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_file", type=str, default="shop_logs.txt")
    parser.add_argument("--balance_file", type=str, default="shop_balance_file.txt")
    parser.add_argument("--result_file", type=str, default="shop_results.txt")
    args = parser.parse_args()
    map = create_tree_map()
    shop_result_file = open(args.result_file, "w")
    shop_balance_file = open(args.balance_file, "w")
    with open(args.log_file) as f_in:
        for i, line in enumerate(f_in):
            if i:
                command = line.split()
                if command[0] == "ADD":
                    size = int(command[1])
                    count = int(command[2])
                    add_size_count(map, size, count)
                elif command[0] == "GET":
                    size = int(command[1])
                    get_size(map, size, shop_result_file)
                elif command[0] == "SELECT":
                    size = int(command[1])
                    select_size(map, size, shop_result_file)
                elif command[0] == "exit":
                    print("Exiting")
                    break
    for elem in traverse(map, "in-order"):
        shop_balance_file.writelines(f"{elem} {get(map, elem)}\n")
    shop_result_file.close()
    shop_balance_file.close()
