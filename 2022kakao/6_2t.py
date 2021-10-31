def solution(board, skill):
    answer = 0
    board_dict = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            board_dict[(i,j)] = board[i][j]

    print(board_dict)

    for i in skill:
        a_r, a_c = i[1], i[2]
        b_r, b_c = i[3], i[4]


        n_x, n_y = i[1]+1, i[2]+1
        if i[0] == 1:
            board_dict[(i[1], i[2])] -= i[-1]
        else:
            board_dict[(i[1],i[2])] += i[-1]


    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])