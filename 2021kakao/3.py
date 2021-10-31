from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    info_dict = defaultdict(list)
    info_list = []

    for i in info:
        x = i.split()
        x[-1] = int(x[-1])
        info_list.append(x)
    info_list.sort(key=lambda x: x[-1])
    print(info_list)

    for i in info_list:
        score = i[-1]
        key = i[:-1]
        for j in range(5):
            for k in combinations(key, j):
                info_dict[k].append(score)

    print(info_dict)

    answer = []
    # query
    for q in query:
        q = q.replace('and', '')
        q = q.replace('-', '')
        a = q.split()
        score = int(a[-1])
        a = tuple(a[:-1])
        answer.append(len(info_dict[a])-bisect.bisect_left(info_dict[a], score))
    print(answer)



    return

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
