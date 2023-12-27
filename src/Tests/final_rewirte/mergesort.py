from typing import Any


def check_params(array: list[Any]):
    for i in range(1, len(array)):
        if type(array[i - 1]) != type(array[i]):
            return False
        if type(array[i]) not in [int, str, list, tuple, float, bool]:
            return False
    return type(array[0]) in [int, str, list, tuple, float, bool]


def merge(array1: list[Any], array2: list[Any]):
    result = []
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            result.append(array1[0])
            array1.remove(array1[0])
        else:
            result.append(array2[0])
            array2.remove(array2[0])
    while len(array1) > 0:
        result.append(array1[0])
        array1.remove(array1[0])
    while len(array2) > 0:
        result.append(array2[0])
        array2.remove(array2[0])
    return result


def sort(array: list[Any]):
    if not check_params(array):
        raise ValueError("All arguments must be of the same type")

    def _sort(array: list[Any]):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        left_array = _sort(array[:mid])
        right_array = _sort(array[mid:])
        return merge(left_array, right_array)

    return _sort(array)
