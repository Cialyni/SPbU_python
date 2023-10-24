def is_float_numbers(s):
    flag = True
    try:
        for i in s.split():
            float(i)
    except ValueError:
        flag = False
    finally:
        if len(s.split()) == 3:
            return True and flag
        return False


def inputer():
    print(
        "to solve an equation Ax^2 + Bx + C = 0\nEnter the coefficients A, B, C in 1 line"
    )
    s = input()
    if is_float_numbers(s):
        a, b, c = float(s.split()[0]), float(s.split()[1]), float(s.split()[2])
        return a, b, c
    raise KeyboardInterrupt("Need 3 float arguments in one string with space: A B C")


def linear_equation_solve(k, b):  # kx + b = 0
    x = None
    try:
        x = -b / k
    except ZeroDivisionError:
        if k == b:
            raise ValueError("This equation has infinity counts of roots")
        raise ZeroDivisionError("this equation is not linear")
    finally:
        return x


def quadratic_equation_solve(A, B, C):  # Ax^2 + Bx + C = 0
    x1, x2 = None, None
    D = B * B - 4 * A * C
    if D < 0:
        raise ValueError("Negative discriminant, can not solve it")
    try:
        x1 = (-B - D**0.5) / (2 * A)
        x2 = (-B + D**0.5) / (2 * A)
        if D == 0:
            x2 = None
    except ZeroDivisionError:
        x1 = linear_equation_solve(B, C)
    finally:
        return x1, x2


def main():
    a, b, c = inputer()
    x1, x2 = quadratic_equation_solve(a, b, c)
    return x1, x2


if __name__ == "__main__":
    print(*main())
