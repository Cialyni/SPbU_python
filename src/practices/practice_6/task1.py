def parse_user_input(s):
    flag = True
    try:
        s = s.split()
        float(s[0]), float(s[1]), float(s[2])
    except ValueError:
        flag = False
        raise ValueError("Need 3 float arguments in one string with space: A B C")
    finally:
        if len(s) == 3 and flag:
            return float(s[0]), float(s[1]), float(s[2])
        else:
            raise ValueError("Need 3 float arguments in one string with space: A B C")


def inputer():
    s = input(
        "to solve an equation Ax^2 + Bx + C = 0\nEnter the coefficients A, B, C in 1 line\n"
    )
    a, b, c = parse_user_input(s)
    return a, b, c


def linear_equation_solve(k, b):  # kx + b = 0
    if not k and not b:
        raise ValueError("infinite number of solutions with k = b = 0")
    elif not k and b:
        raise ZeroDivisionError("division by zero: k = 0")
    else:
        return -b / k


def quadratic_equation_solve(a, b, c):  # Ax^2 + Bx + C = 0
    x1, x2 = None, None
    D = b * b - 4 * a * c
    if a == 0:
        return (linear_equation_solve(b, c),)
    if D < 0:
        raise ValueError("Negative discriminant, can not solve it")
    if D == 0:
        return (-b / (2 * a),)
    if D > 0:
        x1 = (-b - D**0.5) / (2 * a)
        x2 = (-b + D**0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)


def main():
    a, b, c = inputer()
    ans = quadratic_equation_solve(a, b, c)
    return ans


if __name__ == "__main__":
    print(*main())
