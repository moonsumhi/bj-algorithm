def drawing(graph):
    for i in graph:
        print(i)

def solution(board, moves):
    answer = 0
    BOARD_SIZE = len(board)
    mystack = []
    moves = [i-1 for i in moves]

    new_board = []
    for i in zip(*board):
        new_board.append(list(i))


    for i in moves:
        print("move, mystack: ", i, mystack)
        drawing(new_board)
        for j in range(BOARD_SIZE):
            if new_board[i][j] != 0:
                mystack.append(new_board[i][j])
                new_board[i][j] = 0
                break
        if len(mystack) >= 2:
            if mystack[-1] == mystack[-2]:
                answer += 2
                mystack.pop()
                mystack.pop()


    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])