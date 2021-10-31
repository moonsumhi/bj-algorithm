def backtracking(state):
    global candi

    if len(state) == len(candi):
        print(*state)
        return

    for i in candi:
        if i in state:
            continue
        state.append(i)
        backtracking(state)
        state.remove(i)

N = int(input())
candi = list(range(1, N+1))
backtracking([])

# 3