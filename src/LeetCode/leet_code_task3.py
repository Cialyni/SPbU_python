def find_min_substring_with_size(s: str, k: int) -> str:
    ans_s = list(s[0])
    for i in range(1, len(s)):
        while len(ans_s) > 0 and k and s[i] < ans_s[-1]:
            ans_s.pop()
            k -= 1
        if ans_s or s[i] != "0":
            ans_s.append(s[i])
    if k != 0:
        ans_s = ans_s[: len(ans_s) - k]
    return "".join(ans_s) or "0"
