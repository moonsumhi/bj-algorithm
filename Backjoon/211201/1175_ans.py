import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
d = [[[[-1]*4 for k in range(4)] for j in range(m)] for i in range(n)]

ans = -1
x1, y1, x2, y2 = -1, -1, -1, -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            for k in range(4):
                q.append((i, j, k, 0))
                d[i][j][k][0] = 0
        elif a[i][j] == 'C':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j

while q:
    x, y, direction, s = q.popleft()
    if s == 3:
        ans = d[x][y][direction][s]
        break
    for k in range(4):
        if direction == k:
            continue
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != '#':
                ns = s
                if a[nx][ny] == 'C':
                    if nx == x1 and ny == y1:
                        ns |= 1
                    else:
                        ns |= 2
                if d[nx][ny][k][ns] == -1:
                    d[nx][ny][k][ns] = d[x][y][direction][s] + 1
                    q.append((nx, ny, k, ns))
print(ans)







# 2 3
# SCC
# ...