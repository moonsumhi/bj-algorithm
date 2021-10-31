def move(d):
    global dice

    if d == 0:
        dice[0],dice[2], dice[3], dice[5], = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


N, M, x, y, K = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))
print(Map)

# r l u d, v
D = [(0,1),(0,-1),(-1,0),(1,0)]
dice = [0, 0, 0, 0, 0, 0]
Order = list(map(int, input().split()))
for i in Order:
    new_x, new_y = x+D[i-1][0], y+D[i-1][1]
    if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M:
        continue
    else:
        x, y = new_x, new_y

    move(i - 1)
    if Map[new_x][new_y] == 0:
        Map[new_x][new_y] = dice[5]
    else:
        dice[5] = Map[new_x][new_y]
        Map[new_x][new_y] = 0

    print(dice[0])

# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2