import math


def hello_func():
    print('Hi! Input N and i write all not contractible fraction with denominator from 1 to N sorted by increasing')
    n = int(input())
    return n


def fraction_normalization(fraction):
    tmp = math.gcd(fraction[1], fraction[2])
    fraction[1] //= tmp
    fraction[2] //= tmp
    return fraction

def fraction_check(fraction):
    if fraction[1] >= fraction[2]:
        return False
    return True


def fraction_output(fraction):
    print(fraction[1], '/', fraction[2], sep = '')

def main_logic(n):
    ans = []
    for numerator in range(1, n + 1):
        for denominator in range(1, n + 1):
            fraction = [numerator / denominator, numerator, denominator]
            fraction_normalization(fraction)
            if fraction_check(fraction) and not (fraction in ans):
                ans.append(fraction)
    return ans


if __name__ == '__main__':
    n = hello_func()
    ans = main_logic(n)
    ans = sorted(ans)
    for i in ans:
        fraction_output(i)
    print('This is the end of program')
