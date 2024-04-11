def smallest_repunit_div_by_k(k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1
    num = 1
    ans = 1
    while True:
        if num % k == 0:
            return ans
        num = num * 10 + 1
        ans += 1
