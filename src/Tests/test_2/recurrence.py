def recurrence_number_finder(n: int) -> int:
    if n < 0 or n > 100:
        raise ValueError("N must be in diapason [0, 100]")
    if 0 <= n <= 2:
        return n - 1
    fn_1, fn_2, fn_3 = 1, 0, -1  # fn_1 = f(n-1)
    for i in range(2, n):
        fn_3, fn_2, fn_1 = fn_2, fn_1, fn_3 * 3 + fn_2 * 2 + fn_1
    return fn_1


def main():
    try:
        n = int(
            input(
                "Input integer number n in diapason [0, 100] to find F(n) = F(n-3) * 3 + F(n-2) * 2 + F(n-1)\n"
            )
        )
        print("Result is", recurrence_number_finder(n))
    except ValueError as err:
        print("ERROR!")
        if err.args[0] == "N must be in diapason [0, 100]":
            print(err.args[0])
        else:
            print("Input only one integer number")


if __name__ == "__main__":
    main()
