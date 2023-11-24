def fib_number_finder(n: int) -> int:
    if 0 <= n <= 1:
        return n
    elif 1 < n <= 90:
        f, s = 0, 1
        output_num = 1
        num = 1
        while num < n:
            output_num = f + s
            f = s
            s = output_num
            num += 1
        return output_num
    raise ValueError


def main():
    try:
        n = int(
            input(
                "Input n and program will find the Fibonacci number with the index n:\n"
            )
        )
        print(f"Result is: {fib_number_finder(n)}")
    except ValueError:
        print("ERROR!\nEnter only one integer number in range [0:90]")


if __name__ == "__main__":
    main()
