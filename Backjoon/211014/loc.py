def solution(rows, columns, queries):

    board = [[0 for __ in range(columns)] for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1

    answer =  []
    for query in queries:
        s_x, s_y, e_x, e_y = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        print("query: ", s_x, s_y, e_x, e_y)

        #upper
        upper = []
        for i in range(s_y, e_y+1):
            upper.append([s_x, i, board[s_x][i]])

        print("upper: ", upper)

        #lower
        lower = []
        for i in range(s_y, e_y+1):
            lower.append([e_x, i, board[e_x][i]])
        lower = lower[::-1]

        print("lower: ", lower)

        #middle
        middle_left = []
        middle_right = []
        for i in range(s_x+1, e_x):
            middle_left.append([i, s_y, board[i][s_y]])
            middle_right.append([i, e_y, board[i][e_y]])
        middle_left = middle_left[::-1]

        print("middle_left : ", middle_left)
        print("middle_right: ", middle_right)

        result = upper + middle_right + lower + middle_left
        min_v = min(list(zip(*result))[-1])
        print("result: ", result)

        tmp = result[0]
        for i in range(1, len(result)):
            prev_x, prev_y, prev_v = tmp
            x, y, v = result[i]
            board[x][y] = prev_v
            tmp = [x, y, v]
        x, y, v = result[0]
        board[x][y] = tmp[-1]

        print("============")
        for b in board:
            print(b)

        answer.append(min_v)

    print(answer)


    return answer

solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])