from collections import deque

def print_graph(g):
    print("====")
    for i in g:
        print(i)

def bfs(x, y):
    global D, graph, answer

    q = deque()
    q.append((0, x, y))
    dist = [[float('inf') for _ in range(M)] for _ in range(N)]
    dist[x][y] = 0
    tmp_visited = [[False for _ in range(M)] for _ in range(N)]
    tmp_visited[x][y] = True

    while q:
        cnt, cx, cy = q.popleft()

        for i,j in D:
            nx, ny = cx+i, cy+j
            if nx < 0 or ny < 0 or nx >= N or ny >= M or graph[nx][ny] == 'W':
                continue
            if tmp_visited[nx][ny]:
                continue
            tmp_visited[nx][ny] = True
            if cnt+1 < dist[nx][ny]:
                dist[nx][ny] = cnt+1
                q.append((cnt+1, nx, ny))
                answer = max(answer, dist[nx][ny])



N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
D = [(0,1),(1,0),(0,-1),(-1,0)]

print_graph(graph)

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            bfs(i,j)

print(answer)

# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW