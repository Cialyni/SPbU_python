# x**4 + x**3 + x**2 + x + 1 = (x**2 + x) * (x**2 + 1) + 1


def input_func():
    print("Calculating x^4 + x^3 + x^2 + x + 1, enter x: ")
    x = int(input())
    return x


def algorithm(x):
    first_multiplication = x * x
    second_multiplication = (first_multiplication + x) * (first_multiplication + 1) + 1
    return second_multiplication


def output_func(x):
    print("x^4 + x^3 + x^2 + x + 1 = ", x)
    print("Process end")


if __name__ == "__main__":
    output_func(algorithm(input_func()))
