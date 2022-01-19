from bisect import bisect_left
from typing import List, Set


# O(nlogn)
def bisect_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()
    nums1.sort()

    # nums1을 돌면 : 3log 5 -> nums2를 정렬 : 5log5
    # nums2를 돌면 : 5log 3 -> nums1을 정렬 : 3log3
    # 5log3 < 5log5 므로 nums2를 도는게 이득

    for n2 in nums2:
        i = bisect_left(nums1, n2)
        print(i)
        if 0 <= i < len(nums1) and n2 == nums1[i]:
            result.add(n2)
    return list(result)


# O(nlogn) - two pointer
def two_pointer_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()
    nums1.sort()
    nums2.sort()

    p1 = p2 = 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            result.add(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1

    return list(result)


if __name__ == "__main__":
    print(bisect_intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(two_pointer_intersection([4, 9, 5], [9, 4, 9, 8, 4]))
