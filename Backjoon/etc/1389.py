

N, M = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1,N+1):
    graph[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ans = float('inf')
ans_idx = -1
for idx, v in enumerate(graph):
    curr = sum(v[1:])
    if curr < ans:
        ans_idx = idx
        ans = curr

print(ans_idx)





# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2