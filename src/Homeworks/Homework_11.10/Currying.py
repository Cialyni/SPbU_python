import sys
from functools import partial, wraps, reduce


def test_func(*args):
    for i in args:
        print(i, end=" ")
    print("\n")


def curry_explicit(function, arity):
    if arity < 0:
        raise ValueError(
            "ERROR!\ncheck the number of arguments that you specify and send to the function, as well as the validity "  
            "of the arity"
        )

    @wraps(function)
    def curried(*args):
        if len(args) == arity:
            return function(*args)
        return lambda args2: curried(*(args + (args2, )))

    return curried


def uncurry_explicit(function, arity):
    @wraps(function)
    def uncurried(*args):
        if len(args) != arity:
            raise ValueError(
                "ERROR!\ncheck the number of arguments that you specify and send to the function, as well as the "
                "validity of the arity"
            )
        return reduce(lambda x, y: x(y), args, function)

    return uncurried


if __name__ == "__main__":
    f1 = curry_explicit(test_func, 3)
    f1(1)(0)(-1)  # -> 1 10 -1
    f1 = uncurry_explicit(f1, 3)
    f1(4, 5, 0)  # -> 4 5 0
