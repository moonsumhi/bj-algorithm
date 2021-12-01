from typing import List
import heapq

def topKthLargest(self, nums: List[int], k: int) -> int:
    heap = list()

    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)

# heapify를 사용해보자

def topKthLargest2(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums)-k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

# heapq의 모듈을 사용해보자 (nlargest)

def findKthLargest3(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

# 정렬을 이용한 풀이

def findKthLargest4(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]


