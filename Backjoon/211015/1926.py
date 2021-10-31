from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def bfs(x, y, size):
    global ans, board, visited

    q = deque()
    q.append([x,y])

    while q:
        cur_x, cur_y = q.popleft()

        for i, j in [(0,1),(1,0),(0,-1),(-1,0)]:
            nxt_x, nxt_y = cur_x+i, cur_y+j
            if nxt_x < 0 or nxt_y < 0 or nxt_x >= N or nxt_y >= M:
                continue
            if visited[nxt_x][nxt_y]:
                continue
            visited[nxt_x][nxt_y] = True
            if board[nxt_x][nxt_y]:
                board[nxt_x][nxt_y] = 0
                size += 1
                q.append([nxt_x, nxt_y])

    ans = max(ans, size)

ans = 0
cnt = 0
visited = [[False for __ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]:
            visited[i][j] = True
            board[i][j] = 0
            bfs(i, j, 1)
            cnt += 1
print(cnt)
print(ans)

# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1