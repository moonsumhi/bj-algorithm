import heapq

D = [(-1, 0), (0, -1), (0, 1), (1, 0)]
s_size = 2
ans = 0
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def print_board(g):
    print("==============")
    for i in g:
        print(i)

def bfs(loc):
    global s_size, board, ans

    q = []
    heapq.heappush(q, (0, loc[0], loc[1]))

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[loc[0]][loc[1]] = True
    fish = 0
    while q:
        s, x, y = heapq.heappop(q)

        if ([x,y] != loc) and (0 < board[x][y] < s_size):
            fish += 1
            ans = s
            board[x][y] = 0
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[x][y] = True
            q = []

        if fish == s_size:
            s_size += 1
            fish = 0

        for i, j in D:
            nx, ny = x+i, y+j
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if board[nx][ny] <= s_size:
                heapq.heappush(q, (s+1, nx, ny))


s_loc = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            s_loc = [i, j]

bfs(s_loc)
print(ans)

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4

# 6
# 6 0 6 0 6 1
# 0 0 0 0 0 2
# 2 3 4 5 6 6
# 0 0 0 0 0 2
# 0 2 0 0 0 0
# 3 9 3 0 0 1
