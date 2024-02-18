from typing import List


def nextPermutation(nums: List[int]) -> List[int]:
    suff_ind = len(nums) - 1
    while nums[suff_ind] <= nums[suff_ind - 1] and suff_ind > 0:
        suff_ind -= 1
    if suff_ind == 0:
        nums.reverse()
    else:
        suff_upper_bound_ind = suff_ind
        for i in range(suff_ind + 1, len(nums)):
            if nums[i] > nums[suff_ind - 1]:
                suff_upper_bound_ind = i
            else:
                break
        nums[suff_ind - 1], nums[suff_upper_bound_ind] = (
            nums[suff_upper_bound_ind],
            nums[suff_ind - 1],
        )
        nums[suff_ind:] = sorted(nums[suff_ind:])
    return nums
