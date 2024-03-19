from typing import List


def min_sum(nums1: List[int], nums2: List[int]) -> int:
    count1 = nums1.count(0)
    sum1 = sum(nums1) + count1

    count2 = nums2.count(0)
    sum2 = sum(nums2) + count2

    if sum1 == sum2:
        return sum1

    if sum1 >= sum2:
        return sum1 if count2 else -1
    else:
        return sum2 if count1 else -1
