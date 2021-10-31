from collections import deque

def padding(board):
    global N

    for i in range(N):
        while len(board[i]) < N:
            board[i].append(0)

    return board

def arng_board(board, d):
    new_board = []
    if d == "R":
        for i in board:
            new_board.append(i[::-1])
    elif d == "L":
        new_board = board
    elif d == "U":
        new_board = list(map(list, zip(*board)))
    elif d == "D":
        tmp = list(map(list, zip(*board)))
        for i in tmp:
            new_board.append(i[::-1])
    print(new_board)
    return new_board


def combine(board, d):
    global N

    board = arng_board(board, d)

    new_board = [[] for _ in range(N)]
    for i in range(N):
        tmp = list(filter(lambda x: x != 0, board[i]))
        q = deque(tmp)
        stack = []

        while q:
            curr = q.popleft()

            if not stack:
                stack.append(curr)
                continue
            else:
                prev = stack.pop()
                if curr == prev:
                    new_board[i].append(curr * 2)
                else:
                    new_board[i].append(prev)
                    stack.append(curr)
        if stack:
            new_board[i].append(stack.pop())

    padding(new_board)

    print("new_board : ", new_board)

    return new_board


def bfs(B):
    global N, Biggest, Visited


    q = deque()
    q.append((B, 0))

    while q:
        board, s = q.popleft()

        max_v = max(map(max, board))
        print("max_v : ", max_v)
        Biggest = max(Biggest, max_v)

        if s >= 5:
            continue

        #direction
        for i in ["R", "L", "U", "D"]:
            #combine
            print("i : ", i)
            new_board = combine(board, i)
            if new_board in Visited:
                continue
            print("q added")
            Visited.append(new_board)
            q.append((new_board, s+1))



N = int(input())
Board = []
for _ in range(N):
    Board.append(list(map(int, input().split())))
Biggest = max(map(max, Board))
Visited = []
print("Board : ", Board)
print("Biggest : ", Biggest)

bfs(Board)
print(Biggest)


# 3
# 2 2 2
# 4 4 4
# 8 8 8