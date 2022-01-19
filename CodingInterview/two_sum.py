from typing import List
from bisect import bisect_left


def two_pointer_two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]


def bisect_two_sum(numbers: List[int], target: int) -> List[int]:

    for i, v in enumerate(numbers):
        expected = target - v
        j = bisect_left(numbers, expected, lo=i + 1)
        if j < len(numbers) and numbers[j] == expected:
            return [i + 1, j + 1]


def bs_two_sum(numbers: List[int], target: int) -> List[int]:

    for i, v in enumerate(numbers):
        left, right = i + 1, len(numbers) - 1
        expected = target - v
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return [i + 1, mid + 1]


if __name__ == "__main__":
    print(two_pointer_two_sum([2, 7, 11, 15], 9))
    print(bs_two_sum([2, 7, 11, 15], 9))
    print(bisect_two_sum([2, 7, 11, 15], 9))
