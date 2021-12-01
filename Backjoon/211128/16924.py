import copy


def check(board, i, j):

    l = 0
    k = 1
    while True:
        if i+k < len(board) and i-k >= 0 and j+k < len(board[0]) and j-k >= 0:
            if board[i+k][j] == '*' and board[i-k][j] == '*' and board[i][j+k] == '*' and board[i][j-k] == '*':
                l = k
            else:
                break
        else:
            break
        k += 1

    return l


def delete_from_board(tmp_board, i, j, max_cross):

    for t in range(1, max_cross+1):
        tmp_board[i+t][j] = '.'
        tmp_board[i-t][j] = '.'
        tmp_board[i][j+t] = '.'
        tmp_board[i][j-t] = '.'


def print_board(board):
    print("=============")
    for i in board:
        print(i)


def controller(board, x, y):

    tmp_board = copy.deepcopy(board)

    answer = []
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if board[i][j] == '*':
                max_cross = check(board, i, j)
                if max_cross:
                    tmp_board[i][j] = '.'
                    delete_from_board(tmp_board, i, j, max_cross)
                    answer.append((i, j, max_cross))

    for n in range(x):
        if list(filter(lambda z: z != '.', tmp_board[n])):
            return -1
    else:
        return answer


x, y = map(int, input().split())
board = []
for _ in range(x):
    board.append(list(input()))

answer = controller(board, x, y)
if answer != -1:
    print(len(answer))
    for i in answer:
        print(i[0]+1, i[1]+1, i[2], end=' ')
        print()
else:
    print(-1)




# 6 8
# ....*...
# ...**...
# ..*****.
# ...**...
# ....*...
# ........