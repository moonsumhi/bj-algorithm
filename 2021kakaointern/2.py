from collections import deque

def bfs(s, board):
    q = deque()
    q.append((s, 0))
    visited = [[False]*5 for _ in range(5)]
    visited[s[0]][s[1]] = True

    while q:
        cur, d = q.popleft()
        x, y = cur

        if d > 2 or board[x][y] == 'X':
            continue
        if board[x][y] == 'P' and cur != s:
            return False
        else:
            print(cur, d)
            for i in (1,0),(0,1),(-1,0),(0,-1):
                nx, ny = x + i[0], y + i[1]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny]:
                    continue
                else:
                    visited[nx][ny] = True
                    q.append(((nx, ny), d+1))
    return True

def find_p(board):
    for k in range(5):
        for p in range(5):
            if board[k][p] == 'P':
                if not bfs((k, p), board):
                    return 0
    return 1

def solution(places):
    answer = []
    for i in places:
        board = []
        for j in i:
            board.append(list(j))

        print(board)
        answer.append(find_p(board))
    print(answer)


    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])