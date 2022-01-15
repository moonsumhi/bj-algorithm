from typing import List


def to_swap(n1: str, n2: str) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)


def largest_num(nlist: List[int]) -> str:
    for i in range(1, len(nlist)):
        j = i
        while j > 0 and to_swap(nlist[j - 1], nlist[j]):
            nlist[j - 1], nlist[j] = nlist[j], nlist[j - 1]
            j -= 1
    return str(int("".join(map(str, nlist))))


print(largest_num([3, 30, 34, 5, 9]))
