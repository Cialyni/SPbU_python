def smallest_repunit_div_by_k(k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1
    smallest_divisible_by_k = 1
    num_len = 1
    while smallest_divisible_by_k % k != 0:
        smallest_divisible_by_k = smallest_divisible_by_k * 10 + 1
        num_len += 1
    return num_len
