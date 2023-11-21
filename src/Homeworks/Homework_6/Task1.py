from AVL_Tree import create_tree_map, has_key, get, put, remove, traverse, get_lower_bound


if __name__ == '__main__':
    avl_tree_object = create_tree_map()
    shop_result_file = open('shop_results.txt', 'w')
    shop_balance_file = open('shop_balance_file.txt', 'w')
    with open("shop_logs.txt") as f_in:
        for i, line in enumerate(f_in):
            if i:
                command = line.split()
                if command[0] == "ADD":
                    size = int(command[1])
                    count = int(command[2])
                    if has_key(avl_tree_object, size):
                        old_count = get(avl_tree_object, size)
                        put(avl_tree_object, size, count + old_count)
                    else:
                        put(avl_tree_object, size, count)
                elif command[0] == "GET":
                    try:
                        size = int(command[1])
                        shop_result_file.write(str(get(avl_tree_object, size)) + '\n')
                    except AttributeError:
                        shop_result_file.write('0' + '\n')
                elif command[0] == "SELECT":
                    try:
                        size = int(command[1])
                        needed_size = get_lower_bound(avl_tree_object, size)
                        needed_size_count = get(avl_tree_object, needed_size)
                        if needed_size_count == 1:
                            remove(avl_tree_object, needed_size)
                            shop_result_file.write(str(needed_size) + '\n')
                        else:
                            put(avl_tree_object, needed_size, needed_size_count - 1)
                            shop_result_file.write(str(needed_size) + '\n')
                    except AttributeError:
                        shop_result_file.write('SORRY' + '\n')
                elif command[0] == 'exit':
                    print('Exiting')
                    break
    for elem in traverse(avl_tree_object, 'in-order'):
        shop_balance_file.writelines(f'{elem} {get(avl_tree_object, elem)}\n')