V, E = map(int, input().split())
graph = [[] for _ in range(E+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(x, state):
    global visited

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            state.append(i)
            dfs(i, state)
            state.remove(i)
        else:
            state
            return


visited = [False] * (V + 1)
for i in range(1, V+1):
    if not visited[i]:
        dfs(i, [i])



# 7 9
# 1 4
# 4 5
# 5 1
# 1 6
# 6 7
# 2 7
# 7 3
# 3 7
# 7 2