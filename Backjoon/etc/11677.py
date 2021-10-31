from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))

    visited = [False] * (N + 1)
    visited[x] = True
    ans = (-1, 0)
    while q:
        curr, cost = q.popleft()

        if cost > ans[1]:
            ans = (curr, cost)
        print(ans)

        for y,w in graph[curr]:
            if visited[y]:
                continue
            visited[y] = True
            q.append((y,cost+w))

    return ans


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    x = list(map(int, input().split()))
    a = x[0]
    for i in range(1, len(x), 2):
        if x[i] == -1:
            break
        b, w = x[i:i+2]
        graph[a].append((b, w))
print(graph)

s, s_cost = bfs(1)
ans = bfs(s)

print(ans[1])


# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1