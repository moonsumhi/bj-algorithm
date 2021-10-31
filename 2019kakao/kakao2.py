from collections import Counter
import bisect

def solution(N, stages):
    answer = []
    P = len(stages)
    failed_player = Counter(stages)
    failures = {i:0 for i in range(1, N+1)}
    stages.sort()
    for i in range(1, N + 1):
        played = P-bisect.bisect_left(stages, i)
        if i in failed_player:
            failures[i] = failed_player[i]/played

    answer = list(failures.items())
    answer.sort(key=lambda x: x[1], reverse=True)
    result = [k for k,v in answer]

    return result

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])