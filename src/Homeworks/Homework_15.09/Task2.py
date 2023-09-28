import math


def disclaimer():
    print(
        ".............................................................................\n"
        "Hellow\n"
        "In this program Vectors will be set with COORDINATES in 2 Rational numbers with space\n"
        "Matrix will be set as n-string with line break\n"
        "If you want to go back - enter ESC\n"
        "Calculations take place in two-dimensional space\n"
        "............................................................................."
    )


def vec_input(num=1):
    print("\nEntering vector №{}: ".format(num))
    print("Enter X, Y, Z, ... : ")
    vec = list(map(float, input().split()))
    return vec


def scalar_multiplication(vec1, vec2):
    return sum(vec1[i] * vec2[i] for i in range(len(vec1)))


def vector_len(vec):
    return round(sum(elem**2 for elem in vec) ** 0.5, 5)


def vectors_angle(vec1, vec2):
    return round(
        math.acos(
            scalar_multiplication(vec1, vec2) / (vector_len(vec1) * vector_len(vec2))
        )
        * 180
        / math.pi,
        3,
    )


def vector():
    key = 1
    while key != 0:
        print(
            "\nChoose option: ",
            "    Go back - 0",
            "    Find len - 1",
            "    Find angle - 2",
            "    Scalar multiplication - 3\n",
            sep="\n",
        )
        key = int(input())
        if key == 3:
            vec1 = vec_input(1)
            vec2 = vec_input(2)
            print(
                "\033[1m{}{}\033[0m".format(
                    "\nScalar multiplication of this vector = ",
                    scalar_multiplication(vec1, vec2),
                )
            )
        if key == 1:
            vec = vec_input()
            print(
                "\033[1m{}{}\033[0m".format("\nLen of this vector = ", vector_len(vec))
            )
        if key == 2:
            vec1 = vec_input(1)
            vec2 = vec_input(2)
            print(
                "\033[1m{}{}\033[0m".format(
                    "\nAngle of this vector (degree) = ", vectors_angle(vec1, vec2)
                )
            )


def matrix_input(num=1):
    print("\nEntering matrix №{}: ".format(num))
    print("Input matrix size N, M: ")
    n, m = map(int, input().split())
    print("Input matrix: ")
    return n, m, list(list(map(int, input().split())) for i in range(n))


def matrix_addition(matr1, matr2):
    return (
        matr1[0],
        matr1[1],
        [
            [matr1[2][i][j] + matr2[2][i][j] for j in range(matr1[1])]
            for i in range(matr1[0])
        ],
    )


def matrix_multiplication(matr1, matr2):
    return (
        matr1[0],
        matr1[1],
        [
            [
                sum(matr1[2][i][k] * matr2[2][k][j] for k in range(matr1[1]))
                for j in range(matr2[1])
            ]
            for i in range(matr1[0])
        ],
    )


def matrix_output(matr):
    for line in matr[2]:
        print(*line)


def transponirovanie(matr):
    return (
        matr[1],
        matr[0],
        [[matr[2][i][j] for i in range(matr[0])] for j in range(matr[1])],
    )


def matrix():
    key = 1
    while key != 0:
        print(
            "\nChoose option: ",
            "    Go back - 0",
            "    Addition - 1",
            "    Multiplication - 2",
            "    Transponirovanie - 3\n",
            sep="\n",
        )
        key = int(input())
        if key == 1:
            matr1 = matrix_input(1)
            matr2 = matrix_input(2)
            if matr1[0] != matr2[0] or matr1[1] != matr2[1]:
                print(
                    "\033[1m{}\033[0m".format(
                        "\n!!! Incorrect Data: expected equal matrix size !!!\n"
                    )
                )
                break
            print("\033[1m{}\033[0m".format("\nResult of addition: "))
            matr3 = matrix_addition(matr1, matr2)
            matrix_output(matr3)

        if key == 2:
            matr1 = matrix_input(1)
            matr2 = matrix_input(2)
            if matr1[0] != matr2[1] or matr1[1] != matr2[0]:
                print(
                    "\033[1m{}\033[0m".format(
                        "\n!!! Incorrect Data: expected N1 = M2 !!!\n"
                    )
                )
                break
            print("\033[1m{}\033[0m".format("\nResult of multiplicaltion: "))
            matr3 = matrix_multiplication(matr1, matr2)
            matrix_output(matr3)

        if key == 3:
            matr = matrix_input()
            matr = transponirovanie(matr)
            print("\033[1m{}\033[0m".format("\nResult of Transponirovanie: "))
            matrix_output(matr)


def UI():
    key = 1
    while key != 0:
        print(
            "\nEnter 0 to end program",
            "Enter 1 to work with vectors",
            "Enter 2 to work matrixs\n",
            sep="\n",
        )
        key = int(input())
        if key == 1:
            vector()
        if key == 2:
            matrix()


if __name__ == "__main__":
    disclaimer()
    UI()
