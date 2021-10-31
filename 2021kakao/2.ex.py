from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    candi = [[] for _ in range(max(course)+1)]
    for i in course:
        for order in orders:
            for c in combinations(order, i):
                tmp = list((map(str, c)))
                tmp.sort()
                candi[i].append("".join(tmp))
    for i in course:
        max_v = 0
        for k, v in Counter(candi[i]).most_common():
            print(k, v)
            if v >= max_v and v>= 2:
                max_v = v
                answer.append(k)
            else:
                break
    answer.sort()
    print(answer)
    return answer

solution(["XYZ", "XWY", "WXA"], [2,3,4])