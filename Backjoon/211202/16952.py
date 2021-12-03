import copy
from collections import deque
dx1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy1 = [1, 2, 2, 1, -1, -2, -2, -1]
dx2 = [0, 0, 1, -1]
dy2 = [1, -1, 0, 0]
dx3 = [1, 1, -1, -1]
dy3 = [1, -1, 1, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[[[[-1, -1] for _ in range(3)] for k in range(n*n)] for j in range(n)] for i in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        a[i][j] -= 1
        if a[i][j] == 0:
            for k in range(3):
                d[i][j][0][k] = [0, 0]
                q.append((i, j, 0, k))

ans = [-1, -1]
while q:
    x, y, num, piece = q.popleft()
    if num == n*n-1:
        if ans[0] == -1 or ans[0] >= d[x][y][num][piece][0]:
            if ans[1] == -1 or ans[1] > d[x][y][num][piece][1]:
                ans = copy.deepcopy(d[x][y][num][piece])
    for i in range(3):
        if piece == i:
            continue
        if d[x][y][num][i][0] == -1 or (d[x][y][num][piece][0] + 1 <= d[x][y][num][i][0] and d[x][y][num][piece][1] + 1 < d[x][y][num][i][1]):
            d[x][y][num][i][0] = d[x][y][num][piece][0]+1
            d[x][y][num][i][1] = d[x][y][num][piece][1]+1
            q.append((x, y, num, i))

    if piece == 0:
        for k in range(8):
            nx, ny = x+dx1[k], y+dy1[k]
            if 0 <= nx < n and 0 <= ny < n:
                next_num = num
                if a[nx][ny] == num+1:
                    next_num = num+1
                if d[nx][ny][next_num][piece][0] == -1 or (d[x][y][num][piece][0] + 1 <= d[nx][ny][next_num][piece][0] and d[x][y][num][piece][1] < d[nx][ny][next_num][piece][1]):
                    d[nx][ny][next_num][piece] = [d[x][y][num][piece][0] + 1, d[x][y][num][piece][1]]
                    q.append((nx, ny, next_num, piece))

    elif piece == 1:
        for k in range(4):
            l = 1
            while True:
                nx ,ny = x+dx2[k]*l, y+dy2[k]*l
                if 0 <= nx < n and 0 <= ny < n:
                    next_num = num
                    if a[nx][ny] == num+1:
                        next_num = num+1
                    if d[nx][ny][next_num][piece][0] == -1 or (d[x][y][num][piece][0] + 1 <= d[nx][ny][next_num][piece][0] and d[x][y][num][piece][1] < d[nx][ny][next_num][piece][1]):
                        d[nx][ny][next_num][piece] = [d[x][y][num][piece][0] + 1, d[x][y][num][piece][1]]
                        q.append((nx, ny, next_num, piece))
                else:
                    break
                l += 1
    else:
        for k in range(4):
            l = 1
            while True:
                nx, ny = x + dx3[k]*l, y+dy3[k]*l
                if 0 <= nx < n and 0 <= ny < n:
                    next_num = num
                    if a[nx][ny] == num+1:
                        next_num = num+1
                    if d[nx][ny][next_num][piece][0] == -1 or (d[x][y][num][piece][0] + 1 <= d[nx][ny][next_num][piece][0] and d[x][y][num][piece][1] < d[nx][ny][next_num][piece][1]):
                        d[nx][ny][next_num][piece] = [d[x][y][num][piece][0] + 1, d[x][y][num][piece][1]]
                        q.append((nx, ny, next_num, piece))
                else:
                    break
                l += 1

print(*ans, sep=' ')




# 3
# 1 9 3
# 8 6 7
# 4 2 5