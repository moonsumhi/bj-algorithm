from typing import List
import collections
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = list()

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(1, k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk


