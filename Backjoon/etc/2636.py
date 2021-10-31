from collections import deque


def bfs(x, y, visited):
    global Cheese, D, N, M

    q = deque()
    q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for i, j in D:
            nx, ny = cx+i, cy+j
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if Cheese[nx][ny] == 0:
                q.append((nx, ny))
            else:
                Cheese[nx][ny] = 0


def sum_cheese():
    global Cheese, N

    ans = 0
    for i in range(N):
        ans += sum(Cheese[i])

    return ans


def start():
    global Cheese

    t = 0
    r = sum_cheese()
    for i in range(N):
        for j in range(M):
            if Cheese[i][j] == 0:
                visited = [[False] * M for _ in range(N)]
                visited[i][j] = True
                bfs(i, j, visited)
                t += 1
                cr = sum_cheese()
                if cr > 0:
                    r = cr
                else:
                    return t, r


N, M = map(int, input().split())
Cheese = [list(map(int, input().split())) for _ in range(N)]
D = [(0,1),(1,0),(0,-1),(-1,0)]

t, r = start()
print(t)
print(r)





# 13 12
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0 0 0
# 0 1 1 1 0 0 0 1 1 0 0 0
# 0 1 1 1 1 1 1 0 0 0 0 0
# 0 1 1 1 1 1 0 1 1 0 0 0
# 0 1 1 1 1 0 0 1 1 0 0 0
# 0 0 1 1 0 0 0 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0