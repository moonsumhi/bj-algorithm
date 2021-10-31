from itertools import combinations
from collections import defaultdict
import bisect


def solution(info, query):
    answer = []
    candis = []
    for i in info:
        x = i.split()
        score = int(x[-1])
        x = x[:-1]
        candis.append((score, x))
    candis.sort()

    candis_dict = defaultdict(list)
    for i in candis:
        score, x = i
        for j in range(5):
            tmp = combinations(x, j)
            for k in tmp:
                candis_dict[k].append(score)

    for i in query:
        x = i.replace("and", "").replace("-", "").split()
        score = int(x[-1])
        x = tuple(x[:-1])
        answer.append(len(candis_dict[x]) - bisect.bisect_left(candis_dict[x], score))

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])