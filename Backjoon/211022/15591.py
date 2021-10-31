import copy

N, Q = map(int, input().split())
INF = float('inf')
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, usado = map(int, input().split())
    graph[a].append([b, usado])
    graph[b].append([a, usado])

questions = []
for _ in range(Q):
    questions.append(list(map(int, input().split())))

def bfs(k, v):
    q = copy.deepcopy(graph[v])

    visited = [False] * (N+1)
    ans = 0
    while q:
        c, u = q.pop()

        if not visited[c] and c != v:
            visited[c] = True
            if u >= k:
                ans += 1
                q.extend(graph[c])
    print(ans)

for q in questions:
    bfs(q[0], q[1])

# 4 3
# 1 2 3
# 2 3 2
# 2 4 4
# 1 2
# 4 1
# 3 1