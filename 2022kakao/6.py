def solution(board, skill):
    answer = 0
    for i in skill:
        a_r, a_c = i[1],i[2]
        b_r, b_c = i[3],i[4]

        for j in range(a_r, b_r+1):
            for k in range(a_c, b_c+1):
                if i[0] == 1:
                    board[j][k] -= i[-1]
                else:
                    board[j][k] += i[-1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    print(answer)
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])