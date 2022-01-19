import math
import heapq
from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:

    heap = []
    for point in points:
        dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
        heapq.heappush(heap, (dist, point))

    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
