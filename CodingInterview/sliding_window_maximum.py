from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    results: List[int] = []
    window = deque()
    current_max = float("-inf")
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        if current_max == float("-inf"):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        if current_max == window.popleft():
            current_max = float("-inf")

    return results


if __name__ == "__main__":
    print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
