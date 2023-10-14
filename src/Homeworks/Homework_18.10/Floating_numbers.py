import math


def float_to_binary(x):
    bin_x = ""
    int_part, fraction_part = list(map(int, x.split(".")))
    bin_x += "+" if int_part > 0 else "-"
    int_part = abs(int_part)
    fraction_part = float("0." + str(fraction_part))
    while abs(int_part):
        bin_x += str(int_part % 2)
        int_part //= 2
    bin_x = bin_x[0] + bin_x[1:][::-1]
    bin_x += "."
    if not fraction_part:
        bin_x += "0"

    while fraction_part:
        bin_x += str(math.floor(fraction_part * 2))
        fraction_part *= 2
        if fraction_part >= 1:
            fraction_part -= 1
    return bin_x


def to_exponential(bin_x):
    period = 0
    dot_ind = bin_x.find(".")
    while dot_ind != 1:
        bin_x = (
            bin_x[: dot_ind - 1]
            + bin_x[dot_ind - 1 : dot_ind + 1][::-1]
            + bin_x[dot_ind + 1 :]
        )
        period += 1
        dot_ind -= 1
    bin_x = bin_x.replace(".", "0.")
    return bin_x + "*2^" + str(period)


def unexponential(x, p, m):
    new_x = x[0]
    period = int(x.split("^")[-1])
    for i in range(min(period, p)):
        new_x += x[3 + i]
    new_x += "."
    for i in range(min(len(x) - 7 - period, m)):
        new_x += x[period + 3 + i]
    return new_x


def type_change(x):
    period = int(x.split("^")[-1])
    print("Choose type:\n1 = FP64\n2 = FP32\n3 = FP16")
    command = int(input())
    if command == 1:
        print("Result with FP64:", to_exponential(unexponential(x, 11, 53)))
        return unexponential(x, 11, 53)
    if command == 2:
        print("Result with FP32:", to_exponential(unexponential(x, 8, 23)))
        return unexponential(x, 8, 23)
    if command == 3:
        print("Result with FP16:", to_exponential(unexponential(x, 5, 10)))
        return unexponential(x, 5, 10)


if __name__ == "__main__":
    print("Enter a number: ")
    a = input()
    bin_a = float_to_binary(a)
    exponential_a = to_exponential(bin_a)
    print("Result:", exponential_a)
    new_type_a = type_change(exponential_a)
