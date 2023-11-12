import math


def int_part_to_binary(x):
    bin_x = "+" if x >= 0 else "-"
    x = abs(int(x))
    while abs(x):
        bin_x += str(x % 2)
        x //= 2
    return bin_x[0] + bin_x[1:][::-1]


def fraction_part_to_binary(x):
    bin_x = ""
    while x:
        bin_x += str(math.floor(x * 2))
        x *= 2
        if x >= 1:
            x -= 1
    return bin_x


def float_to_binary(x):
    fraction_part, int_part = math.modf(x)[0], math.modf(x)[1]
    bin_x = int_part_to_binary(int_part) + "." + fraction_part_to_binary(fraction_part)
    return bin_x


def to_exponential(bin_x):
    period = bin_x.find(".") - 1
    bin_x = bin_x.replace(".", "")
    bin_x = bin_x[0] + "0." + bin_x[1:]
    return bin_x + "*2^" + str(period)


def un_exponential(x, p, m):
    new_x = x[0]
    first_binary_digit_index_in_exponential_view = 3
    count_of_all_informative_simbols = 7
    period = int(x.split("^")[-1])
    for i in range(min(period, p)):
        new_x += x[first_binary_digit_index_in_exponential_view + i]
    new_x += "."
    for i in range(min(len(x) - count_of_all_informative_simbols - period, m)):
        new_x += x[period + first_binary_digit_index_in_exponential_view + i]
    return new_x


def type_change(x):
    period = int(x.split("^")[-1])
    print("Choose type:\n1 = FP64\n2 = FP32\n3 = FP16")
    command = int(input())
    if command == 1:
        print("Result with FP64:", to_exponential(un_exponential(x, 11, 53)))
        return un_exponential(x, 11, 53)
    if command == 2:
        print("Result with FP32:", to_exponential(un_exponential(x, 8, 23)))
        return un_exponential(x, 8, 23)
    if command == 3:
        print("Result with FP16:", to_exponential(un_exponential(x, 5, 10)))
        return un_exponential(x, 5, 10)
    raise ValueError("Chose 1 or 2 or 3")


if __name__ == "__main__":
    try:
        a = float(input("Enter a number: "))
        bin_a = float_to_binary(a)
        exponential_a = to_exponential(bin_a)
        print("Result:", exponential_a)
        new_type_a = type_change(exponential_a)
    except ValueError:
        print("Enter number not something else")
