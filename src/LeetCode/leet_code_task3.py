def find_min_substring_with_size(s: str, k: int) -> list[int]:
    result = [int(s[0])]
    for digit in s[1:]:
        while len(result) > 0 and k > 0 and int(digit) < result[-1]:
            result.pop()
            k -= 1
        if len(result) > 0 or digit != "0":
            result.append(int(digit))
    if k != 0:
        result = result[: len(result) - k]
    return result or [0]
