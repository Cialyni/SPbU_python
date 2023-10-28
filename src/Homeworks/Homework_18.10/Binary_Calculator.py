import math


def binary_inversion(x):
    return int(not int(x))


def to_decimal(x):
    ans = 0
    if x[-1] == "0":
        for i in range(len(x) - 1):
            ans += int(x[i]) * (2**i)
    else:
        x = bin_sum(x, "111")  # -1 in decimal
        x = [binary_inversion(x[i]) for i in range(len(x))]
        for i in range(len(x)):
            ans += x[i] * (2**i)
        ans *= -1
    return ans


def bin_normalization(x, y):
    x = x + x[-1] * (len(y) - len(x)) if len(x) < len(y) else x
    y = y + y[-1] * (len(x) - len(y)) if len(x) > len(y) else y
    return x, y


def bin_sum(x, y):
    ans = ""
    x, y = bin_normalization(x, y)
    bit = 0
    for i in range(len(x)):
        if int(x[i]) + int(y[i]) + bit >= 2:
            ans += str((int(x[i]) + int(y[i]) + bit) % 2)
            bit = 1
        else:
            ans += str((int(x[i]) + int(y[i]) + bit) % 2)
            bit = 0
    return ans


def to_binary(x):
    bin_x = ""
    copy_x = abs(x)
    while copy_x > 0:
        bin_x += str(copy_x % 2)
        copy_x //= 2
    if x < 0:
        bin_x = [str(int(elem) ^ 1) for elem in bin_x]
        bin_x += "11"
        bin_x = bin_sum(bin_x, "100")  # 1 in decimal
    else:
        bin_x += "00"
    return bin_x


def numbers_input():
    a = int(input("Enter 1-st decimal number"))
    b = int(input("Enter 2-nd decimal number:"))
    return a, b


if __name__ == "__main__":
    a, b = numbers_input()
    bin_a, bin_b, bin_negative_b = to_binary(a), to_binary(b), to_binary(-b)
    print(
        "{} + {} = {}\n{} - {} = {}".format(
            a,
            b,
            to_decimal(bin_sum(bin_a, bin_b)),
            a,
            b,
            to_decimal(bin_sum(bin_a, bin_negative_b)),
        )
    )
