import copy
from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    print(new_board)
    dp = [[int(1e9)]*N for _ in range(N)]
    corner_nums = [[int(1e9)]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    directions = {'left':(0,-1), 'right':(0,1), 'up':(-1,0), 'down':(1,0)}
    q = deque()
    #x,y,cost,prev
    q.append((0,0,0,visited,None))
    print(visited)

    while q:
        x, y, cost, visited, prev = q.popleft()

        for k, v in directions.items():
            n_v = copy.deepcopy(visited)
            nx, ny = x+v[0], y+v[1]
            n_cost = cost
            if nx < 0 or ny < 0 or nx >= N or ny >= N or n_v[nx][ny]:
                continue
            if board[nx][ny] == 1:
                continue
            n_v[nx][ny] = True
            if prev in ['left', 'right']:
                if k in ['up', 'down']:
                    # corner
                    n_cost += 600
                else:
                    # not corner
                    n_cost += 100
            elif prev == None:
                n_cost += 100
            else:
                if k in ['up', 'down']:
                    # not corner
                    n_cost += 100
                else:
                    # corner
                    n_cost += 600
            if dp[nx][ny] >= n_cost:
                dp[nx][ny] = n_cost
                print(nx, ny, dp[nx][ny], k)
            q.append((nx, ny, n_cost, n_v, k))

    print(dp[N-1][N-1])

    return answer

# solution([[0,0,0],[0,0,0],[0,0,0]])
# solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
# solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# solution([[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]])