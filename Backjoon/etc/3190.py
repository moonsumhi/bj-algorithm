from collections import deque

def rotate(prev, cmd):
    global R, L
    if cmd == "D":
        tmp = R.index(prev)
        nxt = (tmp+1)%4
        return R[nxt]
    else:
        tmp = L.index(prev)
        nxt = (tmp+1)%4
        return L[nxt]


def bfs(h, d):
    global Board, Moves, N

    q = deque()
    b = deque()
    b.append(h)
    q.append((h, b, d, 0))

    while q:
        head, body, direction, s = q.popleft()

        if Moves and Moves[0][0] == s:
            t, cd = Moves.popleft()
            direction = rotate(direction, cd)
            print(direction)

        new_head = (head[0]+direction[0], head[1]+direction[1])
        print("new_head : ", new_head)
        print("body: ", body)
        if new_head[0] <= 0 or new_head[0] > N or new_head[1] <= 0 or new_head[1] > N:
            print(s+1)
            return

        # 자기몸 부딪힘
        if new_head in body:
            print(s+1)
            return

        if Board[new_head[0]][new_head[1]]:
            Board[new_head[0]][new_head[1]] = 0
            body.append(new_head)
        else:
            body.popleft()
            body.append(new_head)
        q.append((new_head, body, direction, s+1))


N = int(input())
K = int(input())
Apples = []
for _ in range(K):
    Apples.append(tuple(map(int, input().split())))
Moves_num = int(input())
Moves = deque()
for _ in range(Moves_num):
    s, d = input().split()
    Moves.append((int(s), d))

print(Apples)
print(Moves)

Board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for x, y in Apples:
    Board[x][y] = 1

R, L = [(0,1),(1,0),(0,-1),(-1,0)], [(-1,0),(0,-1),(1,0),(0,1)]
head = (1, 1)
direction = (0, 1)
bfs(head, direction)





# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D