from collections import deque

def draw_cheese(c):
    print("==========")
    for i in c:
        print(i)


def bfs(x, y):
    global visited, Cheese, N, M

    q = deque()
    q.append((x, y))

    mem = [[0 for _ in range(M)] for _ in range(N)]
    while q:
        cur_x, cur_y = q.popleft()

        for i,j in D:
            nxt_x, nxt_y = cur_x+i, cur_y+j
            if nxt_x < 0 or nxt_y < 0 or nxt_x >= N or nxt_y >= M:
                continue
            if (not Cheese[nxt_x][nxt_y]) and (visited[nxt_x][nxt_y]):
                continue
            visited[nxt_x][nxt_y] = True

            if Cheese[nxt_x][nxt_y]:
                mem[nxt_x][nxt_y] += 1
                continue

            q.append((nxt_x, nxt_y))

    cheese2air(mem)

def cheese2air(mem):
    global Cheese, N, M

    for i in range(N):
        for j in range(M):
            if mem[i][j] >= 2:
                Cheese[i][j] = 0


def still_cheese():
    for i in range(N):
        for j in range(M):
            if Cheese[i][j]:
                return True
    return False

N, M = map(int, input().split())
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Cheese = []
for _ in range(N):
    Cheese.append(list(map(int, input().split())))

ans = 0
s = still_cheese()
while s:
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i, j in [(0, 0), (0, M-1), (N-1, 0), (N-1, M-1)]:
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
    draw_cheese(Cheese)
    ans += 1
    s = still_cheese()
print(ans)


# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0