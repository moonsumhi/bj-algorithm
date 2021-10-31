import copy


def backtracking(cost, bound):
    if bound < MAX_V:
        return

    if cost > N:
        return

    if benefit > MAX_V:
        MAX_v = benefit
        answer = copy.deepcopy(state)
        return

    for i in range(11):
        if visited[i]:
            continue
        visited[i]




def solution(n, info):
    answer = []

    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])