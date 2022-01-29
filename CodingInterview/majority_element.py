from typing import List


def majorityElement(nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])

    print(f"nums: {nums}")
    print(f"a, b : {a}, {b}")

    return [b, a][nums.count(a) > half]


def majorityElement2(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


print(majorityElement([1, 2, 4, 4, 2, 3, 1, 2, 2, 2, 2]))
