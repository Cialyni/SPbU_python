def to_decimal(x):
    ans = 0
    if x[-1] == "0":
        for i in range(len(x) - 1):
            ans += int(x[i]) * (2**i)
    else:
        x = bin_sum(x, "111")  # -1 in decimal
        x = [1 if i == "0" else 0 for i in x]
        for i in range(len(x)):
            ans += x[i] * (2**i)
        ans *= -1
    return ans


def bin_normalization(first_binary, second_binary):
    first_binary = (
        first_binary + first_binary[-1] * (len(second_binary) - len(first_binary))
        if len(first_binary) < len(second_binary)
        else first_binary
    )
    second_binary = (
        second_binary + second_binary[-1] * (len(first_binary) - len(second_binary))
        if len(first_binary) > len(second_binary)
        else second_binary
    )
    return first_binary, second_binary


def bin_sum(x, y):
    ans = ""
    x, y = bin_normalization(x, y)
    bit = 0
    for i in range(len(x)):
        xi, yi = int(x[i]), int(y[i])
        res = (xi + yi + bit) % 2
        if xi + yi + bit >= 2:
            ans += str(res)
            bit = 1
        else:
            ans += str(res)
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


def to_additional_code(binary_x):
    binary_x = ["1" if elem == "0" else "0" for elem in binary_x]
    binary_x += "11"
    binary_x = bin_sum(binary_x, "100")  # 1 in decimal
    return binary_x


def to_binary(x):
    bin_x = to_direct_code(x)
    if x < 0:
        bin_x = to_additional_code(bin_x)
    else:
        bin_x += "00"
    return bin_x


if __name__ == "__main__":
    try:
        a = int(input("Enter 1-st decimal number"))
        b = int(input("Enter 2-nd decimal number:"))
    except ValueError:
        print("Input numbers!")
    finally:
        bin_a, bin_b, bin_negative_b = to_binary(a), to_binary(b), to_binary(-b)
        print(  # f-string so cool 0_0. Why I don't use them early???
            f"{a} + {b} = {to_decimal(bin_sum(bin_a, bin_b))}\n{a} - {b} = {to_decimal(bin_sum(bin_a, bin_negative_b))}"
        )
