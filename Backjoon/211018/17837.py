import sys

n, k = map(int, (input().split()))
chess_board = []
for _ in range(n):
    chess_board.append(list(map(int, input().split())))

#→, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
reversed_d = {0:1, 1:0, 2:3, 3:2}
chess = [[] for _ in range(k+1)]
chess_map = [[[] for __ in range(n)] for _ in range(n)]
for i in range(1, k+1):
    r, c, d = map(int, input().split())
    chess_map[r-1][c-1].append(i)
    chess[i] = [r-1, c-1, d-1]

def move(number):
    x, y, d = chess[number]
    nx, ny = x+dx[d], y+dy[d]

    if nx < 0 or ny < 0 or nx >= n or ny >= n or chess_board[nx][ny] == 2:
        nd = reversed_d[d]
        nx, ny = x+dx[nd], y+dy[nd]
        chess[number][2] = nd

        if nx < 0 or ny < 0 or nx >= n or ny >= n or chess_board[nx][ny] == 2:
            return 0

    s = chess_map[x][y].index(number)
    chess_set = chess_map[x][y][s:]
    chess_map[x][y] = chess_map[x][y][:s]
    if chess_board[nx][ny] == 1:
        for i in chess_set[::-1]:
            chess_map[nx][ny].append(i)
            chess[i][:2] = [nx, ny]
    else:
        for i in chess_set:
            chess_map[nx][ny].append(i)
            chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1

    return 0


def print_board(g):
    for i in g:
        print(i)

cnt = 1
while cnt <= 1000:
    for i in range(1, k+1):

        if move(i):
            print(cnt)
            sys.exit()
        # if cnt <= 7:
        #     print("number: ", i)
        #     print("chess: ", chess)
        #     print("chess map: ")
        #     print_board(chess_map)
        #     print("cnt: ", cnt)
    cnt += 1
print(-1)

# 6 10
# 0 1 2 0 1 1
# 1 2 0 1 1 0
# 2 1 0 1 1 0
# 1 0 1 1 0 2
# 2 0 1 2 0 1
# 0 2 1 0 2 1
# 1 1 1
# 2 2 2
# 3 3 4
# 4 4 1
# 5 5 3
# 6 6 2
# 1 6 3
# 6 1 2
# 2 4 3
# 4 2 1