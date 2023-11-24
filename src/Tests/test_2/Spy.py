import functools
from datetime import datetime

FOO_LOGS = []


def spy(func):
    def spy_inner(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        global FOO_LOGS
        FOO_LOGS.append((str(start_time), args))
        return result

    return spy_inner


def print_usage_statistic(function):
    if function.__name__ == "spy_inner":
        for elem in FOO_LOGS:
            yield elem[0], elem[1]
    else:
        raise Warning("No decorator")


@spy
def foo(num):
    print(num)


def main():
    foo(30)
    foo("hello")
    foo(5)

    for time, parameters in print_usage_statistic(foo):
        all_parameters = ""
        for i in parameters:
            all_parameters += str(i)
        print(
            f"function foo was called at {time} " f"with parameters:\n{all_parameters}"
        )


if __name__ == "__main__":
    main()
