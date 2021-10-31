from collections import deque

def check_bfs(x, y, cur_color):
    global board

    poplist = [(x, y)]
    q = deque()
    q.append((x, y))

    visited = [[False for __ in range(6)] for _ in range(6)]
    visited[x][y] = True
    cnt = 1
    while q:
        cur_x, cur_y = q.popleft()

        for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_x, next_y = cur_x+i, cur_y+j
            if next_x < 0 or next_y < 0 or next_x >= 6 or next_y >= 6:
                continue
            if visited[next_x][next_y]:
                continue
            visited[next_x][next_y] = True
            if board[next_x][next_y] == cur_color:
                poplist.append((next_x, next_y))
                cnt += 1
                q.append((next_x, next_y))

    if cnt >= 3:
        redraw_board(poplist)


def redraw_board(removed):
    global board
    for i in removed:
        x, y = i
        board[x][y] = 0

    tmp_zip = list(zip(*board[::-1]))

    tmp_zip = [list(i) for i in tmp_zip]
    print("~~~~", tmp_zip)

    for i in range(6):
        tmp_zip[i] = list(filter(lambda x: x != 0, tmp_zip[i]))

    for i in range(6):
        if len(tmp_zip[i]) != 6:
            for j in range(6-len(tmp_zip[i])):
                tmp_zip[i].append(0)

    tmp_board = list(zip(*tmp_zip))
    tmp_board = [list(i) for i in tmp_board]
    tmp_board = tmp_board[::-1]

    board = tmp_board

def print_graph(g):
    print("===========")
    for i in g:
        print(i)

board = [[0]*6 for _ in range(6)]
def solution(macaron):
    global board

    answer = []
    colors = []

    for cmd in macaron:
        col, color = cmd
        colors.append(color)
        col = col-1
        row = -1
        for i in range(5, -1, -1):
            if board[i][col] == 0:
                board[i][col] = color
                row = i
                break

        check_bfs(row, col, color)
        print("!! board")
        print_graph(board)

        for i in range(5, -1, -1):
            for j in range(5, -1, -1):
                if board[i][j] in colors:
                    check_bfs(i, j, board[i][j])

    print("answer: ")
    print_graph(board)

    answer = []
    for i in board:
        a = list(map(str, i))
        answer.append("".join(a))
    print(answer)

    return answer

solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]])