def to_decimal(x):
    ans = 0
    if x[-1] == "0":
        for i in range(len(x) - 1):
            ans += int(x[i]) * (2**i)
    else:
        x = bin_sum(x, "111")  # -1 in decimal
        x = [int(not int(i)) for i in x]
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
        xi, yi = int(x[i]), int(y[i])
        if xi + yi + bit >= 2:
            ans += str((xi + yi + bit) % 2)
            bit = 1
        else:
            ans += str((xi + yi + bit) % 2)
            bit = 0
    if len(ans) == len(x):
        ans += ans[-1]
    return ans


def to_direct_code(x):
    bin_x = ""
    x = abs(x)
    while x > 0:
        bin_x += str(x % 2)
        x //= 2
    return bin_x


def to_additional_code(x):
    x = [int(not int(elem)) for elem in x]
    x += "11"
    x = bin_sum(x, "100")  # 1 in decimal
    return x


def to_binary(x):
    bin_x = to_direct_code(x)
    if x < 0:
        bin_x = to_additional_code(bin_x)
    else:
        bin_x += "00"
    return bin_x


if __name__ == "__main__":
    try:
        a, b = int(input("Enter 1-st decimal number")), int(
            input("Enter 2-nd decimal number:")
        )
        bin_a, bin_b, bin_negative_b = to_binary(a), to_binary(b), to_binary(-b)
        print(  # f-string so cool 0_0. Why I don't use them early???
            f"{a} + {b} = {to_decimal(bin_sum(bin_a, bin_b))}\n{a} - {b} = {to_decimal(bin_sum(bin_a, bin_negative_b))}"
        )
    except ValueError:
        print("Input numbers!")
    finally:
        print("End of program")
