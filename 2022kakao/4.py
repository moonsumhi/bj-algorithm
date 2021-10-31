import copy

INFO = []
MAX_SCORE = 0
answer = []
K = 0

def backtracking(remained, cur_score, visited, state, bound):
    global MAX_SCORE, answer

    if bound < MAX_SCORE:
        return

    if remained == 0:
        apeach_score = 0
        for i in range(11):
            if INFO[i] == 0 and state[i] == 0:
                continue
            if INFO[i] >= state[i]:
                apeach_score += (10-i)

        compare_score = cur_score - apeach_score

        if compare_score > MAX_SCORE:
            MAX_SCORE = compare_score
            answer = copy.deepcopy(state)
        elif compare_score == MAX_SCORE:
            # compare
            for i in range(11):
                if answer[::-1][i] < state[::-1][i]:
                    answer = copy.deepcopy(state)
        return

    else:
        for i in range(11):
            if visited[i]:
                continue
            visited[i] = True
            if remained-(INFO[i]+1) >= 0:
                state[i] = INFO[i]+1
                backtracking(remained - (INFO[i] + 1), cur_score + (10 - i), visited, state, bound)
            else:
                state[i] = 0
                next_v = 0
                if (10-i-K) >= 0:
                    next_v = (10-i-K)
                # print("curr_state: ", state)
                # print("curr: ", i)
                # print("curr_bound: ", bound-(10-i)+next_v-(10-i)+next_v)
                if i == 10 and remained:
                    state[i] = remained
                    backtracking(0, cur_score, visited, state, bound - (10 - i) + next_v - (10 - i) + next_v)
                else:
                    backtracking(remained, cur_score, visited, state, bound-(10-i)+next_v-(10-i)+next_v)
            visited[i] = False
            state[i] = 0

def solution(n, info):
    global INFO, answer, MAX_SCORE, K
    INFO = info
    K = n
    state = [0]*11

    visited = [False]*11
    bound = 0
    for i in range(11):
        if i < K:
            bound += (10-i)
        else:
            bound -= (10-i)

    backtracking(n, 0, visited, state, bound)
    if MAX_SCORE == 0:
        return [-1]
    print(answer)
    return answer

solution(10, [0,0,0,0,0,0,0,0,3,4,3])