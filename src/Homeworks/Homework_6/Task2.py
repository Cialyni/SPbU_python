from AVL_Tree import (
    Tree,
    create_tree_map,
    has_key,
    get,
    put,
    remove,
    traverse,
    get_lower_bound,
    TreeNode,
    split,
    join,
    remove_keys,
    getAll,
)
import sys


def rename(map: Tree, old_name: str, new_name: str) -> Tree:
    def _rename(root: TreeNode, new_name: str):
        if not root is None:
            home, block = root.key[1], root.key[2]
            root.key = [new_name, home, block]
            _rename(root.right, new_name)
            _rename(root.left, new_name)

    first, second = split(map, old_name)
    second, third = split(second, old_name + "z")
    _rename(second.root, new_name)
    join(second, third)
    join(first, second)
    return first


def program(mode="interactive"):
    map = create_tree_map()
    if mode == "static":
        s1, s2 = input("enter input file name: "), input("enter output file name: ")
        f_in = open(s1, "r")
        f_out = open(s2, "w")
    else:
        f_in = sys.stdin
        f_out = sys.stdout

    while True:
        command = f_in.readline().split()
        if not command:
            break
        if command[0] == "exit":
            break
        elif command[0] == "CREATE":
            address = [command[1], int(command[2]), int(command[3])]
            index = int(command[4])
            put(map, address, index)
        elif command[0] == "RENAME":
            old_name, new_name = command[1], command[2]
            map = rename(map, old_name, new_name)
        elif command[0] == "GET":
            address = [command[1], int(command[2]), int(command[3])]
            try:
                f_out.write(str(get(map, address)) + "\n")
            except AttributeError:
                f_out.write("None\n")
        elif command[0] == "DELETE_BLOCK":
            address = [command[1], int(command[2]), int(command[3])]
            remove(map, address)
        elif command[0] == "DELETE_HOUSE":
            address = [command[1], int(command[2])]
            remove_keys(map, address, address + [1e9])
        elif command[0] == "DELETE_STREET":
            address = [command[1]]
            remove_keys(map, address, address + [1e9])
        elif command[0] == "LIST":
            address1 = [command[1], int(command[2]), int(command[3])]
            address2 = [command[4], int(command[5]), int(command[6])]
            address_lst = getAll(map, address1, address2)
            if len(address_lst):
                for key in address_lst:
                    f_out.write(key[0] + " " + str(key[1]) + " " + str(key[2]) + "\n")
                f_out.write("\n")
            else:
                f_out.write("\n")


if __name__ == "__main__":
    command = input("select the program mode:\n   interactive - 1\n   static - 2\n")
    if command == "1":
        program(mode="interactive")
    else:
        program(mode="static")
