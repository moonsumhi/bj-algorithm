def building_condition(loc, t, board0, board1):
    x, y = loc
    n = len(board0)-1

    if t == 0:
        if ((x == n) or (board1[x][y] == 1) or (board1[x][y-1] == 1) or (board0[x+1][y] == 1)):
            return True
    else:
        if ((board0[x+1][y] == 1) or (board0[x+1][y+1] == 1) or (board1[x][y-1] == 1 and board1[x][y+1] == 1)):
            return True

    return False


def delete_building(board0, board1):
    n = len(board0)-1
    for i in range(n + 1):
        for j in range(n + 1):
            if board0[i][j] == 1:
                if not building_condition((i, j), 0, board0, board1):
                    return False
            if board1[i][j] == 1:
                if not building_condition((i, j), 1, board0, board1):
                    return False

    return True


def solution(n, build_frame):
    answer = []
    board0 = [[0]*(n+1) for _ in range(n+1)]
    board1 = [[0]*(n+1) for _ in range(n+1)]
    for order in build_frame:
        x, y, t, cd = order
        x, y = n-y, x
        # create
        if cd == 1:
            if building_condition((x,y), t, board0, board1):
                if t == 0:
                    board0[x][y] = 1
                else:
                    board1[x][y] = 1

        # delete
        if cd == 0:
            if t == 0:
                board0[x][y] = 0
            else:
                board1[x][y] = 0

            if not delete_building(board0, board1):
                if t == 0:
                    board0[x][y] = 1
                else:
                    board1[x][y] = 1

    for i in range(n+1):
        for j in range(n+1):
            x, y = j, n - i
            if board0[i][j] == 1:
                answer.append([x, y, 0])
            if board1[i][j] == 1:
                answer.append([x, y, 1])

    answer.sort()
    print(answer)


    return answer

solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])