import math


def hello_func():
    print(
        "Hi! Input N and i write all not contractible fraction with denominator from 1 to N sorted by increasing"
    )
    n = int(input())
    return n


def fraction_normalization(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def all_fraction_find(n):
    ans = set()
    for denominator in range(1, n + 1):
        for numerator in range(1, denominator + 1):
            fraction = fraction_normalization(numerator, denominator)
            if not (fraction in ans):
                ans.add(fraction)
    return ans


def answer_output(ans):
    output = ""
    for i in ans:
        output += str(i[0]) + "/" + str(i[1]) + "\n"
    return output


if __name__ == "__main__":
    n = hello_func()
    ans = all_fraction_find(n)
    ans = sorted(
        ans, key=lambda fraction: fraction[0] / fraction[1]
    )  # fraction = [numerator, denominator]
    print(answer_output(ans))
    print("This is the end of program")
