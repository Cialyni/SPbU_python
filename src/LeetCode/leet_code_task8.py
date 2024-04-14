from typing import List


def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr)
    ans = []
    while r - l > 1:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid
        else:
            l = mid
    cur_count = 0
    while cur_count < k:
        if l < 0:
            ans.append(arr[r])
            r += 1
            cur_count += 1
            continue
        if r >= len(arr):
            ans.append(arr[l])
            l -= 1
            cur_count += 1
            continue
        if abs(x - arr[l]) <= abs(x - arr[r]) or (
            abs(x - arr[l]) <= abs(x - arr[r]) and arr[l] < arr[r]
        ):
            ans.append(arr[l])
            l -= 1
        else:
            ans.append(arr[r])
            r += 1
        cur_count += 1
    return sorted(ans)
