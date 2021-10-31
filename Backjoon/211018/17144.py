import copy

r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

machine = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            machine.append((i,j))

def print_graph(g):
    print("==========")
    for i in g:
        print(i)

for k in range(t):

    new_board = [[0 for __ in range(c)] for _ in range(r)]
    for i, j in machine:
        new_board[i][j] = -1
    # spread
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                cnt = 0
                for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nxt_x, nxt_y = x+i, y+j
                    if nxt_x < 0 or nxt_y < 0 or nxt_x >= r or nxt_y >= c:
                        continue
                    if board[nxt_x][nxt_y] == -1:
                        continue
                    new_board[nxt_x][nxt_y] += board[x][y]//5
                    cnt += 1
                new_board[x][y] += board[x][y] - (board[x][y]//5)*cnt

    print("after spreading ============")
    print_graph(new_board)

    upper, lower = machine
    # upper side
    x, y = upper
    prev = new_board[x][1]
    new_board[x][1] = 0
    for i in range(2, c):
        new_board[x][i], prev = prev, new_board[x][i]
    for i in range(x-1, -1, -1):
        new_board[i][-1], prev = prev, new_board[i][-1]
    for i in range(c-2,-1, -1):
        new_board[0][i], prev = prev, new_board[0][i]
    for i in range(1, x):
        new_board[i][0], prev = prev, new_board[i][0]

    print("moving (upper side) =========")
    print_graph(new_board)

    # lower side
    x, y = lower
    prev = new_board[x][1]
    new_board[x][1] = 0
    for i in range(2, c):
        new_board[x][i], prev = prev, new_board[x][i]
    for i in range(x+1,r):
        new_board[i][-1], prev = prev, new_board[i][-1]
    for i in range(c-2,-1, -1):
        new_board[r-1][i], prev = prev, new_board[r-1][i]
    for i in range(r-2, x, -1):
        new_board[i][0], prev = prev, new_board[i][0]

    print("moving (lower side) ========")
    print_graph(new_board)
    board = copy.deepcopy(new_board)

print(sum(map(sum, new_board)) + 2)



# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0