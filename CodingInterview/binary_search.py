from typing import List


def search(nums: List[int], target: int) -> int:
    def binary_search(left: int, right: int) -> int:
        print(left, right)
        if left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                return binary_search(mid + 1, right)
            elif target == nums[mid]:
                return mid
            else:
                return binary_search(left, mid - 1)
        else:
            return -1

    return binary_search(0, len(nums) - 1)


print(search([-1, 0, 3, 5, 9, 12], 9))

from bisect import bisect_left

# pythonic
def search(nums: List[int], target: int) -> int:
    index = bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
